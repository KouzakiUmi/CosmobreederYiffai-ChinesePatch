"""Read-only DS risk extraction; writes only this component's review packet."""
from pathlib import Path
import json
import re
import sys
import zipfile

HERE=Path(__file__).resolve().parent
ROOT=HERE.parents[4]
LOC=ROOT/'localization'
sys.path.insert(0,str(LOC/'tools'))
from projectlib import read_jsonl
from codec import decrypt_file


def prepare():
    units={u['id']:u for u in read_jsonl(LOC/'catalog/units.jsonl')}
    trans={t['id']:t for t in read_jsonl(LOC/'translations/zh-CN.jsonl')}
    occ=[o for o in read_jsonl(LOC/'catalog/occurrences.jsonl') if o['category']=='dialogue']
    joins=read_jsonl(LOC/'translations/dialogue-joins.jsonl')
    joined={i['occurrence_id']:j for j in joins for i in j['inputs']}
    scripts={}
    with zipfile.ZipFile(LOC/'builds/r27-story12-shaderfix-test5/patch.pak') as z:
        for p,e in [('datadf/all.ds','datadf/1'),('datadm/all.ds','datadm/1')]:
            scripts[p]=decrypt_file(z.read(e)).decode('utf8').splitlines()
    def context(path,line):
        rows=scripts[path];lo=line-1;hi=line
        while lo>0 and not re.fullmatch(r'<[^<>]+>',rows[lo]):lo-=1
        while hi<len(rows) and not re.fullmatch(r'<[^<>]+>',rows[hi]):hi+=1
        return [{'line':n,'r27':rows[n-1]} for n in range(lo+1,hi+1)]
    cases=[]
    for uid,t in trans.items():
        if not re.search(r'[\u3400-\u9fff]-[\u3400-\u9fff]',t.get('draft') or ''):continue
        os=[o for o in occ if o['unit_id']==uid]
        if not os:continue
        cases.append({'case_id':f'DH{len(cases)+1:02}', 'kind':'unit-cjk-word-hyphen','unit':units[uid], 'translation':t,
                      'occurrences':[{'occurrence':o,'joined':joined.get(o['occurrence_id']),
                                      'effective_line':joined[o['occurrence_id']]['physical_lines'][0] if o['occurrence_id'] in joined else o['line'],
                                      'context':context(o['logical_path'],joined[o['occurrence_id']]['physical_lines'][0] if o['occurrence_id'] in joined else o['line'])} for o in os]})
    risk=json.loads((ROOT/'docs/font-layout-audit-20261025/text-review/results/corpus-risk-stats.json').read_text('utf8'))
    merged=risk['merged_text_artifacts']['merged_with_ascii_hyphen']
    for row in merged:
        j=next(j for j in joins if j['join_id']==row['join_id'])
        cases.append({'case_id':f'DM{len([c for c in cases if c["kind"]=="merged-ascii-hyphen"])+1:02}',
                      'kind':'merged-ascii-hyphen','join':j,'source_units':[units[i['unit_id']] for i in j['inputs']],
                      'context':context(j['logical_path'],j['physical_lines'][0])})
    residual=json.loads((ROOT/'docs/font-layout-audit-20261025/text-review/results/ds-join-residuals.json').read_text('utf8'))
    for n,row in enumerate(residual['unjoined_without_recorded_reason'],1):
        os=[o for o in occ if o['logical_path']==row['logical_path'] and o['line'] in row['lines']]
        cases.append({'case_id':f'DS{n:02}','kind':'unrecorded-skip','edge':row,'occurrences':os,
                      'source_units':[units[o['unit_id']] for o in os],
                      'context':context(row['logical_path'],row['lines'][0])})
    (HERE/'review-packet.json').write_text(json.dumps(cases,ensure_ascii=False,indent=2)+'\n','utf8')
    text=[]
    for c in cases:
        text.append(c['case_id']+' '+c['kind'])
        if 'unit' in c:
            text.extend(['EN '+c['unit']['source'],'CN '+c['translation']['draft']])
            for row in c['occurrences']:
                o=row['occurrence'];text.append(o['logical_path']+':'+str(o['line'])+' effective:'+str(row['effective_line'])+' '+o['occurrence_id'])
                text.extend(str(r['line'])+' '+r['r27'] for r in row['context'])
        else:
            text.extend('EN '+u['source'] for u in c['source_units'])
            if 'join' in c:text.append('CN '+c['join']['merged_translation'])
            text.extend(str(r['line'])+' '+r['r27'] for r in c['context'])
        text.append('')
    (HERE/'review-packet.txt').write_text('\n'.join(text),'utf8')
    print('cases:',len(cases),'unit CJK hyphens:',sum(c['kind']=='unit-cjk-word-hyphen' for c in cases))

if __name__=='__main__':prepare()
