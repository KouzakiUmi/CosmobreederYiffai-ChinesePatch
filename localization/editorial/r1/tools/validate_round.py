"""Validate editorial identity/coverage, never mistake it for semantic approval."""
from pathlib import Path
from collections import Counter
from hashlib import sha256
import argparse
import json

ROOT=Path(__file__).resolve().parents[4]
R1=ROOT/'localization/editorial/r1'


def jsonl(path):
    return [json.loads(s) for s in path.read_text('utf8').splitlines() if s.strip()]


def main():
    p=argparse.ArgumentParser(description=__doc__)
    p.add_argument('--snapshot',type=Path,required=True)
    p.add_argument('--output',type=Path,required=True)
    p.add_argument('--require-complete',action='store_true')
    a=p.parse_args();snapshot=a.snapshot.resolve();out=a.output.resolve()
    if not snapshot.is_relative_to(R1/'corpus') or not out.is_relative_to(R1) or out.exists():
        raise ValueError('New editorial report only')
    manifest=json.loads((snapshot/'manifest.json').read_text('utf8'))
    readers=json.loads((snapshot/'readers-manifest.json').read_text('utf8'))
    errors=[];packets=[];all_scenes=set();alias_rows=set();catalog_units=set();counts=Counter()
    for name,pin in manifest['source_sha256'].items():
        path=(ROOT/name).resolve()
        if not path.is_relative_to(ROOT) or sha256(path.read_bytes()).hexdigest()!=pin:
            errors.append('Source drift '+name)
    for r in readers:
        path=ROOT/r['path']
        if sha256(path.read_bytes()).hexdigest()!=r['sha256']:errors.append('Reader drift '+r['packet'])
    for pinfo in manifest['packets']:
        name=pinfo['packet'];scenes=json.loads((snapshot/'packets'/(name+'.json')).read_text('utf8'))
        scene_map={s['scene_id']:s for s in scenes}
        if len(scene_map)!=len(scenes):errors.append('Duplicate scene '+name)
        for scene in scenes:
            sid=scene['scene_id']
            if sid in all_scenes:errors.append('Scene in multiple packets '+sid)
            all_scenes.add(sid)
            counts['canonical_rows']+=len(scene['rows'])
            for row in scene['rows']:
                if sha256(row['source'].encode('utf8')).hexdigest()!=row['source_sha256']:
                    errors.append('Source string hash '+row['review_row_id'])
                counts['kind_'+scene['kind']]+=1
            for alias in scene['aliases']:
                if len(alias['rows'])!=len(scene['rows']):errors.append('Alias cardinality '+sid)
                for row in alias['rows']:
                    rid=row['review_row_id']
                    if rid in alias_rows:errors.append('Duplicate alias row '+rid)
                    alias_rows.add(rid)
                    if rid.startswith('CAT:'):catalog_units.add(row['unit_id'])
        folder=R1/'audit'/name
        status={'packet':name,'expected_scenes':len(scenes),'expected_rows':sum(len(s['rows']) for s in scenes),
                'covered_scenes':0,'read_full_scenes':0,'read_full_rows':0,'findings':0,'state':'not_submitted'}
        if (folder/'coverage.jsonl').is_file() and (folder/'findings.jsonl').is_file():
            coverage=jsonl(folder/'coverage.jsonl');findings=jsonl(folder/'findings.jsonl')
            receipts={r['scene_id']:r for r in coverage};fmap={f['finding_id']:f for f in findings}
            if len(receipts)!=len(coverage):errors.append('Duplicate coverage '+name)
            if len(fmap)!=len(findings):errors.append('Duplicate findings '+name)
            if set(receipts)!=set(scene_map):errors.append('Missing/extra coverage '+name)
            for sid,receipt in receipts.items():
                if sid not in scene_map:continue
                expected={r['review_row_id'] for r in scene_map[sid]['rows']}
                aliases={r['review_row_id'] for alias in scene_map[sid]['aliases'] for r in alias['rows']}
                canonical=receipt.get('canonical_row_ids')
                if canonical is not None and (set(canonical)!=expected or len(canonical)!=len(expected)):
                    errors.append('Coverage row identity '+sid)
                # Some authors explicitly enumerate all identical-edition aliases.
                # Both accepted forms must be exact, not arbitrary supersets.
                if set(receipt['row_ids']) not in (expected,aliases) or len(receipt['row_ids'])!=len(set(receipt['row_ids'])):
                    errors.append('Coverage alias identity '+sid)
                if receipt['read_status']=='read_full':
                    status['read_full_scenes']+=1;status['read_full_rows']+=len(expected)
                    if scene_map[sid]['kind'] in ('dialogue','vsn') and not receipt['context_checked']:
                        errors.append('Missing script-context acknowledgement '+sid)
                    if not receipt['context_checked']:counts['reading_without_runtime_context_claim']+=1
                for fid in receipt.get('findings',[]):
                    if fid not in fmap or fmap[fid]['scene_id']!=sid:errors.append('Finding reference '+fid)
            for finding in findings:
                sid=finding['scene_id']
                if sid not in scene_map:errors.append('Unknown finding scene '+sid);continue
                allowed_rows={r['review_row_id'] for alias in scene_map[sid]['aliases'] for r in alias['rows']}
                if not finding['row_ids'] or not set(finding['row_ids'])<=allowed_rows:
                    errors.append('Finding row scope '+finding['finding_id'])
                for key in ('source_quote','current_quote','reason','evidence_refs','status','category','severity','proposed_zh'):
                    if key not in finding:errors.append('Missing finding field '+key)
                if finding.get('status') not in ('proposal','needs_evidence','retained','rejected'):
                    errors.append('Unapproved editorial status '+finding['finding_id'])
                counts['severity_'+finding.get('severity','unknown')]+=1
            logpath=folder/'reading-log.json'
            if not logpath.is_file():
                errors.append('Missing reading log '+name)
            else:
                log=json.loads(logpath.read_text('utf8'))
                reader_path=snapshot/'packets'/(name+'.reader.md')
                expected_pin=sha256(reader_path.read_bytes()).hexdigest()
                if log.get('input_sha256')!=expected_pin:errors.append('Reading input identity '+name)
                read_lines=set()
                for span in log.get('read_ranges',[]):
                    if isinstance(span,list) and len(span)==2:first,last=span
                    elif isinstance(span,dict):first,last=span.get('start'),span.get('end')
                    else:errors.append('Invalid reading range '+name);continue
                    if not isinstance(first,int) or not isinstance(last,int) or first<1 or last<first:
                        errors.append('Invalid reading range bounds '+name);continue
                    read_lines.update(range(first,last+1))
                expected_lines=set(range(1,len(reader_path.read_text('utf8').splitlines())+1))
                if status['read_full_scenes']==len(scenes) and not expected_lines<=read_lines:
                    errors.append('Incomplete declared read ranges '+name)
                refs=json.dumps(log.get('references_read',[]),ensure_ascii=False)
                if any(n not in refs for n in ('characters-primary','characters-support','world-and-plot')):
                    errors.append('Missing character/world references '+name)
            status.update(covered_scenes=len(receipts),findings=len(findings),state='submitted')
            if status['read_full_scenes']==len(scenes):status['state']='read_full_claimed_not_semantic_approval'
        if a.require_complete and status['read_full_scenes']!=len(scenes):errors.append('Incomplete reading '+name)
        packets.append(status)
    if len(alias_rows)!=manifest['all_source_rows']:errors.append('Alias source coverage cardinality')
    if len(catalog_units)!=manifest['catalog_units']:errors.append('Catalog unit coverage cardinality')
    if len(all_scenes)!=manifest['canonical_scenes']:errors.append('Scene cardinality')
    value={'status':'FAIL' if errors else 'PASS_STRUCTURAL_ONLY','errors':errors,'counts':dict(counts),
           'catalog_units':len(catalog_units),'source_rows':len(alias_rows),'scenes':len(all_scenes),'packets':packets,
           'semantic_approval':False,'formal_translations_modified':False,
           'limits':['Coverage receipts are reviewer declarations; checks do not prove comprehension or correctness.',
                     'Code/image inventory does not prove player-visible usage or artwork review.',
                     'No applied translation, archive rebuild or game validation is performed.']}
    out.parent.mkdir(parents=True,exist_ok=True)
    out.write_text(json.dumps(value,ensure_ascii=False,indent=2)+'\n',encoding='utf8')
    print(json.dumps({'status':value['status'],'errors':errors,'scenes':len(all_scenes),'source_rows':len(alias_rows),
                      'packets':[{k:v for k,v in r.items() if k not in ('expected_rows',)} for r in packets]},ensure_ascii=False,indent=2))
    if errors:raise SystemExit(1)


if __name__=='__main__':main()
