"""Preflight complete source-edge reviews; emit a proposed ledger, never install."""
from pathlib import Path
from contextlib import ExitStack
from unittest.mock import patch
import hashlib
import json
import sys
import zipfile
HERE=Path(__file__).resolve().parent;sys.path.insert(0,str(HERE))
import dialogue_joins as joins
from codec import decrypt_file
from projectlib import PROJECT


def sha(data):return hashlib.sha256(data).hexdigest()


def main():
    work=PROJECT/'work/dialogue-joins-r24';target=work/'proposed-ledger.jsonl'
    if target.exists():raise ValueError('Proposed output exists')
    all_data=json.loads((work/'all-candidates.json').read_text('utf8'));groups=all_data['groups']
    old=joins.load_records();old_sha=sha(joins.LEDGER.read_bytes())
    accepted=[];skipped=set();seen=set();review_hashes={}
    for part in range(4):
        inp=json.loads((work/('review-input-'+str(part)+'.json')).read_text('utf8'))
        path=work/('review-output-'+str(part)+'.json');data=json.loads(path.read_text('utf8'));review_hashes[path.name]=sha(path.read_bytes())
        if [(x['group_id'],x['index']) for x in inp]!=[(x['group_id'],x['index']) for x in data]:raise ValueError('Review group coverage/order')
        for source,review in zip(inp,data):
            seen.add(source['group_id']);ids=[n['occurrence_id'] for n in source['nodes']]
            expected=set(zip(ids,ids[1:]));covered=set();occupied=set()
            for merge in review['merges']:
                mids=merge['occurrence_ids']
                if len(mids)<2 or mids[0] not in ids:raise ValueError('Invalid merge members')
                at=ids.index(mids[0])
                if ids[at:at+len(mids)]!=mids or occupied.intersection(mids) or source['test_only']:raise ValueError('Noncontiguous/overlapping/test merge')
                edges=set(zip(mids,mids[1:]));covered.update(edges);occupied.update(mids)
                accepted.append((source,merge,part))
            for edge in review['skipped_edges']:
                pair=(edge['left'],edge['right'])
                if pair not in expected or pair in covered or pair in skipped or not edge['reason'].strip():raise ValueError('Invalid/duplicate skipped edge')
                covered.add(pair);skipped.add(pair)
            if covered!=expected:raise ValueError('Unreviewed source edges: '+source['group_id'])
    if len(seen)!=len(groups):raise ValueError('Missing review group')
    units=joins.load_units();occ=joins.load_occurrences();translations=joins.current_translations();metrics=joins.glyph_metrics()
    original_read=joins.read_jsonl;resources_cache={}
    def cached_read(path):
        key=str(path)
        if key not in resources_cache:resources_cache[key]=original_read(path)
        return resources_cache[key]
    records=[];invalid=[]
    # Cache immutable input tables only within this build command. Production API is unchanged.
    with ExitStack() as stack:
        for name,value in [('load_units',units),('load_occurrences',occ),('current_translations',translations),('glyph_metrics',metrics)]:
            stack.enter_context(patch.object(joins,name,lambda v=value:v))
        stack.enter_context(patch.object(joins,'read_jsonl',cached_read))
        for source,merge,part in accepted:
            try:
                record=joins.build_record(merge['occurrence_ids'],merge['merged_translation'],merge['reason'],agent='gpt-6.1-sol/all-source-review-part-'+str(part))
            except joins.JoinValidationError as error:
                invalid.append({'group_id':source['group_id'],'index':source['index'],'error':str(error),'merge':merge});continue
            record['origin'].update({'review_artifact_sha256':review_hashes['review-output-'+str(part)+'.json'],'source_candidate_group_id':source['group_id']})
            records.append(record);print('validated',source['index'],flush=True)
    new_members={i['occurrence_id'] for r in records for i in r['inputs']}
    replaced=[];kept=[]
    for r in old:
        mids=[i['occurrence_id'] for i in r['inputs']]
        if new_members.intersection(mids) or skipped.intersection(zip(mids,mids[1:])):replaced.append(r['join_id'])
        else:kept.append(r)
    records=kept+records
    reports=[]
    if not invalid:
        with zipfile.ZipFile(PROJECT/'builds/final-8146-r21-images/patch.pak') as z:
            for logical,entry in [('datadf/all.ds','datadf/1'),('datadm/all.ds','datadm/1')]:
                _,report=joins.apply_joins(logical,(PROJECT.parent/'extract/patch'/logical).read_bytes(),decrypt_file(z.read(entry)),records=records);reports.append(report)
    result={'status':'proposed_only','review_group_count':len(seen),'reviewed_edge_count':all_data['pair_count'],
            'accepted_merges':len(accepted),'skipped_edge_count':len(skipped),'kept_existing':len(kept),'replaced_existing':replaced,
            'old_ledger_sha256':old_sha,'proposed_count':len(records),'invalid':invalid,'review_artifact_sha256':review_hashes,'resource_reports':reports}
    (work/'merge-report.json').write_text(json.dumps(result,ensure_ascii=False,indent=2)+'\n',encoding='utf8')
    if invalid:raise ValueError('Reviewed text failed strict gates; see merge-report.json; active ledger NOT changed')
    target.write_text(''.join(json.dumps(r,ensure_ascii=False,separators=(',',':'))+'\n' for r in records),encoding='utf8')
    print('PROPOSED',len(records),'records',len(accepted),'new merges',len(skipped),'explicit skipped edges')


if __name__=='__main__':main()
