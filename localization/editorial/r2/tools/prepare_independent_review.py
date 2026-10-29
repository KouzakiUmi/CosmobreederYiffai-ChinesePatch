"""Expose actual reviewed node drafts, not old free-paragraph proposals."""
from pathlib import Path
from collections import defaultdict
from hashlib import sha256
import json,textwrap

ROOT=Path(__file__).resolve().parents[4];R2=ROOT/'localization/editorial/r2'
OUT=R2/'review-input'
if OUT.exists():raise ValueError('New independent review input only')
OUT.mkdir(parents=True)
receipts=[]
for n in range(1,11):
    packet='packet-%02d'%n
    data=json.loads((R2/'input'/(packet+'.json')).read_text('utf8'))
    folder=R2/'packets'/packet
    decisions=[json.loads(s) for s in (folder/'decisions.jsonl').read_text('utf8').splitlines()]
    edits=[json.loads(s) for s in (folder/'edits.jsonl').read_text('utf8').splitlines()]
    byrow={e['row_id']:e for e in edits}
    out=['# '+packet+' 实际节点独立复核','',
         '全部原文/旧节点/修后节点按场景。长行90字符显示折行，不是脚本真实换行。',
         'AFTER取已提交节点草稿并执行用户明确Tomcat命名决定；实际资源已由来源锁定引擎全批预检。',
         '逐项检查apply/reject/defer是否成立。不能将此表当已批准；发现应给具体finding/edit与理由。','']
    def display(label,value):
        if value is None:out.append(label+': <null;用途未核>');return
        if value=='':out.append(label+': <EMPTY;合句消费尾>');return
        for i,chunk in enumerate(textwrap.wrap(value,width=90,replace_whitespace=False,drop_whitespace=False,break_long_words=True,break_on_hyphens=False)):
            out.append(label+(': ' if i==0 else '+ ')+chunk)
    for scene in data['scenes']:
        sid=scene['scene_id'];out+=['## '+sid+' | '+scene['mode']+' | '+scene['logical_path']+' | '+scene['root']]
        seq=[(r.get('line') or 0,'row',r) for r in scene['rows']]+[(r['line'],'control',r) for r in scene['controls']]
        for _,kind,row in sorted(seq,key=lambda v:v[0]):
            if kind=='control':out.append('CONTROL L'+str(row['line'])+' '+row['source']);continue
            rid=row['review_row_id'];e=byrow.get(rid);before=row['current_line']
            after=e['new'] if e else before
            if isinstance(after,str):after=after.replace('汤姆猫','Tomcat')
            out.append('ROW '+rid+' | L'+str(row.get('line') or '-')+' | '+('EDIT '+e['edit_id'] if e else 'no manual edit'))
            display('EN',row['source']);display('BEFORE',before);display('AFTER',after)
        for f in data['findings']:
            if f['scene_id']!=sid:continue
            d=next(d for d in decisions if d['finding_id']==f['finding_id'])
            out+=['### '+f['finding_id']+' | action='+d['action'],
                  '原问题：'+f['reason'],'本轮理由：'+d['reason'],
                  'EDIT_IDS '+json.dumps(d.get('edit_ids',[]),ensure_ascii=False)]
            if d.get('resolution'):out.append('RESOLUTION '+d['resolution']+' '+d.get('remaining_uncertainty',''))
        out.append('')
    path=OUT/(packet+'.md');path.write_text('\n'.join(out)+'\n',encoding='utf8')
    receipts.append({'packet':packet,'lines':len(path.read_text('utf8').splitlines()),'sha256':sha256(path.read_bytes()).hexdigest(),
                     'decisions_sha256':sha256((folder/'decisions.jsonl').read_bytes()).hexdigest(),
                     'edits_sha256':sha256((folder/'edits.jsonl').read_bytes()).hexdigest()})
(OUT/'manifest.json').write_text(json.dumps(receipts,ensure_ascii=False,indent=2)+'\n',encoding='utf8')
print(json.dumps(receipts,ensure_ascii=False,indent=2))
