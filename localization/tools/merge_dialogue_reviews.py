"""Validate explicit content-review decisions into a proposed join ledger, never auto-approve."""
from pathlib import Path
import hashlib
import json
import sys
import zipfile

HERE=Path(__file__).resolve().parent;sys.path.insert(0,str(HERE))
import dialogue_joins as joins
from codec import decrypt_file


def sha(p):return hashlib.sha256(p.read_bytes()).hexdigest()


def main():
    root=HERE.parent;work=root/'work/dialogue-joins';out=work/'proposed-ledger.jsonl'
    if out.exists():raise ValueError('Proposed output exists')
    candidates=json.loads((work/'candidates-v1.json').read_text('utf8'))['groups']
    by_id={g['group_id']:g for g in candidates}
    records=joins.load_records();base_sha=sha(joins.LEDGER)
    stats={'base_count':len(records),'decisions':[],'conflicts':[],'invalid':[],'duplicates':[],'review_files':{}}
    seen=set()
    for part in range(3):
        path=work/('review-output-'+str(part)+'.json');review=json.loads(path.read_text('utf8'))
        expected=json.loads((work/('review-input-'+str(part)+'.json')).read_text('utf8'))
        if [(r['group_id'],r['index']) for r in review]!=[(r['group_id'],r['index']) for r in expected]:raise ValueError('Review identity/order mismatch')
        stats['review_files'][path.name]=sha(path)
        for decision in review:
            gid=decision['group_id'];g=by_id[gid]
            if gid in seen:raise ValueError('Duplicate review group')
            seen.add(gid)
            if decision['decision']=='skip':stats['decisions'].append(decision);continue
            if decision['decision']!='accept' or g['test_only'] or not decision['merged_translation']:raise ValueError('Unusable review decision')
            ids=[n['occurrence_id'] for n in g['nodes']];new_ids=set(ids)
            overlap=[r for r in records if new_ids.intersection(x['occurrence_id'] for x in r['inputs'])]
            if overlap:
                if len(overlap)==1 and set(x['occurrence_id'] for x in overlap[0]['inputs'])==new_ids:
                    stats['duplicates'].append({'group_id':gid,'kept':overlap[0]['join_id']});continue
                stats['conflicts'].append({'group_id':gid,'existing':[r['join_id'] for r in overlap]});continue
            try:
                record=joins.build_record(ids,decision['merged_translation'],decision['reason'],agent='gpt-6.1-sol/content-review-part-'+str(part))
            except joins.JoinValidationError as error:
                stats['invalid'].append({'group_id':gid,'index':g['index'],'error':str(error),'review':decision});continue
            record['origin'].update({'review_artifact_sha256':sha(path),'candidate_group_id':gid})
            records.append(record);stats['decisions'].append(decision)
            print('validated',g['index'],flush=True)
    if len(seen)!=len(candidates):raise ValueError('Incomplete review coverage')
    # Validate the complete proposed dataset against genuine unjoined R21 resources.
    with zipfile.ZipFile(root/'builds/final-8146-r21-images/patch.pak') as archive:
        stats['resource_reports']=[]
        for logical,entry in [('datadf/all.ds','datadf/1'),('datadm/all.ds','datadm/1')]:
            original=(root.parent/'extract/patch'/logical).read_bytes()
            _,report=joins.apply_joins(logical,original,decrypt_file(archive.read(entry)),records=records)
            stats['resource_reports'].append(report)
    stats.update(proposed_count=len(records),base_ledger_sha256=base_sha,
                 skipped_count=sum(d['decision']=='skip' for d in stats['decisions']))
    out.write_text(''.join(json.dumps(r,ensure_ascii=False,separators=(',',':'))+'\n' for r in records),encoding='utf8')
    (work/'merge-review-report.json').write_text(json.dumps(stats,ensure_ascii=False,indent=2)+'\n',encoding='utf8')
    print(json.dumps({k:stats[k] for k in ('base_count','proposed_count','skipped_count')},ensure_ascii=False))
    print('invalid',len(stats['invalid']),'conflicts',len(stats['conflicts']),'duplicates',len(stats['duplicates']))
    print('PROPOSED ONLY',out)


if __name__=='__main__':main()
