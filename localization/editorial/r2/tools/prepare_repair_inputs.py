"""Prepare all-finding repair work orders, retaining complete affected scenes."""
from pathlib import Path
from hashlib import sha256
from collections import defaultdict
import json
import textwrap

ROOT=Path(__file__).resolve().parents[4]
R1=ROOT/'localization/editorial/r1';R2=ROOT/'localization/editorial/r2'
OUT=R2/'input'
if OUT.exists():raise ValueError('New repair input only')
findings=[json.loads(s) for s in (R1/'reports/rough-review-01/findings.jsonl').read_text('utf8').splitlines()]
by_packet=defaultdict(list)
for row in findings:by_packet[row['packet']].append(row)
OUT.mkdir(parents=True)
manifest=[]
for packet,found in sorted(by_packet.items()):
    src=R1/'corpus/snapshot-01/packets'/(packet+'.json')
    scenes=json.loads(src.read_text('utf8'));wanted={f['scene_id'] for f in found}
    selected=[s for s in scenes if s['scene_id'] in wanted]
    if len(selected)!=len(wanted):raise ValueError('Finding scene mismatch')
    value={'packet':packet,'findings':found,'scenes':selected,
           'source_packet_sha256':sha256(src.read_bytes()).hexdigest(),
           'contract':'localization/editorial/r2/REPAIR_CONTRACT.md'}
    path=OUT/(packet+'.json');path.write_text(json.dumps(value,ensure_ascii=False,indent=2)+'\n',encoding='utf8')
    md=['# '+packet+' 修前复审与节点稿','',
        '先读REPAIR_CONTRACT。覆盖本包全部发现；源/当前节点按完整场景阅读。',
        '下方EN/ZH的长行按90字符显示折行，属于阅读显示，不是原脚本换行；old精确值取同名JSON。',
        '被合句消费的空行保持空行；每个非空节点只给一个合并后的最终edit；actor/命令前缀不动。','']
    for scene in selected:
        sid=scene['scene_id'];sf=[f for f in found if f['scene_id']==sid]
        md+=['## '+sid+' | '+scene['mode']+' | '+scene['kind']+' | '+scene['logical_path']+' | '+scene['root']]
        md.append('ALIASES '+json.dumps([{'mode':a['mode'],'scene_id':a['scene_id']} for a in scene['aliases']],ensure_ascii=False))
        sequence=[(r.get('line') or 0,'row',r) for r in scene['rows']]+[(r['line'],'control',r) for r in scene['controls']]
        for _,kind,row in sorted(sequence,key=lambda x:x[0]):
            if kind=='control':md.append('CONTROL L'+str(row['line'])+' '+row['source']);continue
            md.append('ROW '+row['review_row_id']+' | L'+str(row.get('line') or '-')+' | '+row.get('speaker','')+' | '+row['current_kind'])
            for key,label in [('source','EN'),('current_line','ZH')]:
                text=row.get(key)
                if text is None:md.append(label+': <null;用途未核>')
                elif text=='':md.append(label+': <EMPTY;合句尾行可能已消费>')
                else:
                    chunks=textwrap.wrap(text,width=90,replace_whitespace=False,drop_whitespace=False,break_long_words=True,break_on_hyphens=False)
                    md.extend((label+': ' if i==0 else label+'+ ') + chunk for i,chunk in enumerate(chunks))
        for f in sf:
            md+=['### '+f['finding_id']+' | '+f['severity']+' | '+f['status']+' | '+f['category'],
                  'ROW_IDS '+json.dumps(f['row_ids'],ensure_ascii=False),
                  '原粗校理由：'+f['reason'],'原建议（不能直接作节点稿）：']
            md.extend(textwrap.wrap(f['proposed_zh'] or '<无建议，先补证>',width=90,replace_whitespace=False,drop_whitespace=False) or [''])
            md+=['独立抽核：'+f.get('review_conclusion','not_spotchecked'),f.get('review_reason',''),
                 '下一步：'+f.get('next_action','independent_review'),'']
        md.append('')
    view=OUT/(packet+'.md');view.write_text('\n'.join(md)+'\n',encoding='utf8')
    manifest.append({'packet':packet,'findings':len(found),'scenes':len(selected),'display_lines':len(view.read_text('utf8').splitlines()),
                     'json_sha256':sha256(path.read_bytes()).hexdigest(),'md_sha256':sha256(view.read_bytes()).hexdigest()})
(OUT/'manifest.json').write_text(json.dumps(manifest,ensure_ascii=False,indent=2)+'\n',encoding='utf8')
print(json.dumps(manifest,ensure_ascii=False,indent=2))
