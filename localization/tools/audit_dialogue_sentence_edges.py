"""Audit every adjacent source-sentence continuation, without approving any merge."""
from pathlib import Path
import hashlib
import json
import re
from audit_dialogue_continuations import PROJECT, rows, unwrap


def main():
    units={u['id']:u for u in rows(PROJECT/'catalog/units.jsonl')}
    tr={u['id']:(u.get('translation') or u.get('draft') or '') for u in rows(PROJECT/'translations/zh-CN.jsonl')}
    occ=sorted((o for o in rows(PROJECT/'catalog/occurrences.jsonl') if o['category']=='dialogue'),key=lambda o:(o['logical_path'],o['line']))
    edges=[]
    for a,b in zip(occ,occ[1:]):
        if (a['logical_path'],a['entry'],a['prefix'],a['line']+1)!=(b['logical_path'],b['entry'],b['prefix'],b['line']):continue
        left=unwrap(units[a['unit_id']]['source']).rstrip().rstrip('\"\u201d\u2019')
        if not left or re.search(r'[.!?…\-—]$',left) or not tr[a['unit_id']] or not tr[b['unit_id']]:continue
        edges.append((a,b))
    groups=[]
    for a,b in edges:
        if groups and groups[-1][-1]['occurrence_id']==a['occurrence_id']:groups[-1].append(b)
        else:groups.append([a,b])
    out=PROJECT/'work/dialogue-joins-r24';out.mkdir(parents=True,exist_ok=True)
    all_groups=[]
    for index,nodes in enumerate(groups):
        first=nodes[0];group={'index':index,'group_id':'S'+hashlib.sha256('|'.join(n['occurrence_id'] for n in nodes).encode()).hexdigest()[:20],
             'logical_path':first['logical_path'],'entry':first['entry'],'prefix':first['prefix'],
             'test_only':first['entry'].split()[0].startswith('Test_'),
             'nodes':[{k:n[k] for k in ('occurrence_id','unit_id','line','previous_line','next_line')}|
                      {'source':units[n['unit_id']]['source'],'draft':tr[n['unit_id']],'protected_tokens':units[n['unit_id']].get('protected_tokens',[])} for n in nodes]}
        all_groups.append(group)
    for part in range(4):
        path=out/('review-input-'+str(part)+'.json')
        if path.exists():raise ValueError('Review input exists')
        selected=[g for g in all_groups if g['index']%4==part]
        path.write_text(json.dumps(selected,ensure_ascii=False,indent=2)+'\n',encoding='utf8');print(part,len(selected),path)
    meta={'status':'all_source_edges_candidates_not_approved','pair_count':len(edges),'group_count':len(groups),'groups':all_groups}
    (out/'all-candidates.json').write_text(json.dumps(meta,ensure_ascii=False,indent=2)+'\n',encoding='utf8')
    print('ALL SOURCE CONTINUATIONS',len(edges),'edges',len(groups),'groups')


if __name__=='__main__':main()
