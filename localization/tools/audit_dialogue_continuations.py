"""Produce review candidates only. Never changes translations or approves joins."""
from pathlib import Path
import argparse
import hashlib
import json
import re

PROJECT=Path(__file__).resolve().parents[1]


def rows(path):
    with path.open(encoding='utf8') as source:
        return [json.loads(line) for line in source if line.strip()]


def unwrap(value):
    value=value.strip()
    return value[1:-1].strip() if value.startswith('[') and value.endswith(']') else value


def audit():
    units={r['id']:r for r in rows(PROJECT/'catalog/units.jsonl')}
    translations={r['id']:(r.get('translation') or r.get('draft') or '') for r in rows(PROJECT/'translations/zh-CN.jsonl')}
    occurrences=sorted((r for r in rows(PROJECT/'catalog/occurrences.jsonl') if r['category']=='dialogue'),key=lambda r:(r['logical_path'],r['line']))
    edges=[]
    for a,b in zip(occurrences,occurrences[1:]):
        if (a['logical_path'],a['entry'],a['prefix'],a['line']+1)!=(b['logical_path'],b['entry'],b['prefix'],b['line']):continue
        ta,tb=translations[a['unit_id']],translations[b['unit_id']]
        if not ta or not tb:continue
        left,right=unwrap(units[a['unit_id']]['source']),unwrap(units[b['unit_id']]['source'])
        zh=unwrap(ta);unfinished=not re.search(r'[.!?…\-—]$',left)
        words=re.findall(r'[A-Za-z]+',left)
        reason=[]
        if zh.endswith(('，','、','：','；')):reason.append('Chinese continuation punctuation')
        if unfinished and right[:1].islower():reason.append('English lower-case continuation')
        if unfinished and words and words[-1].upper() in {'TO','FOR','THE','YOUR','AND','THIS','OF','IN','THAT','WITH','A','CAN'}:
            reason.append('English incomplete phrase')
        if reason:edges.append((a,b,reason))
    grouped=[]
    for a,b,reasons in edges:
        if grouped and grouped[-1]['nodes'][-1]['occurrence_id']==a['occurrence_id']:
            grouped[-1]['nodes'].append(b);grouped[-1]['reasons'].extend(reasons)
        else:grouped.append({'nodes':[a,b],'reasons':list(reasons)})
    for index,group in enumerate(grouped):
        nodes=group['nodes'];first=nodes[0]
        group.update({'index':index,'group_id':'J'+hashlib.sha256('|'.join(n['occurrence_id'] for n in nodes).encode()).hexdigest()[:20],
                      'logical_path':first['logical_path'],'entry':first['entry'],'prefix':first['prefix'],
                      'speaker':first['speaker'],'test_only':first['entry'].split()[0].startswith('Test_')})
        group['reasons']=sorted(set(group['reasons']))
        group['nodes']=[dict(n,source=units[n['unit_id']]['source'],draft=translations[n['unit_id']],
                             protected_tokens=units[n['unit_id']].get('protected_tokens',[])) for n in nodes]
    return {'status':'candidates_not_approved','pair_count':len(edges),'group_count':len(grouped),'groups':grouped}


def main():
    ap=argparse.ArgumentParser(description=__doc__);ap.add_argument('--output',type=Path,required=True);args=ap.parse_args()
    dest=args.output.resolve();allowed=(PROJECT/'work').resolve()
    if dest.exists() or dest==allowed or not dest.is_relative_to(allowed):raise ValueError('New work output only')
    result=audit();dest.parent.mkdir(parents=True,exist_ok=True);dest.write_text(json.dumps(result,ensure_ascii=False,indent=2)+'\n',encoding='utf8')
    print('Review candidates only:',result['pair_count'],'pairs /',result['group_count'],'groups;',dest)


if __name__=='__main__':main()
