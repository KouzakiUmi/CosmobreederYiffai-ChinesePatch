"""Render compact editorial views; IDs and full provenance remain in packet JSON."""
from pathlib import Path
from hashlib import sha256
import json
import sys

ROOT=Path(__file__).resolve().parents[4]
if len(sys.argv)!=2:raise SystemExit('prepare_readers.py r1/corpus/snapshot')
folder=Path(sys.argv[1]).resolve()
if not folder.is_relative_to(ROOT/'localization/editorial/r1/corpus'):raise ValueError('Editorial corpus only')
receipts=[]
for source in sorted((folder/'packets').glob('packet-*.json')):
    target=source.with_suffix('.reader.md')
    if target.exists():raise ValueError('New compact views only')
    scenes=json.loads(source.read_text('utf8'));text=['# '+source.stem+' 连续场景精简阅读稿','',
      '当前中文取最终归档；空译行可能由既有合句消费。源文/当前文都必须按整场连读。',
      '更多unit/occurrence/别名/原草稿/原provider证据见同名packet JSON。控制边不等于运行时触发顺序。','']
    for g in scenes:
        text+=['## '+g['scene_id']+' | '+g['mode']+' | '+g['kind']+' | '+g['logical_path']+' | '+g['root']]
        sequence=[(r.get('line') or 0,'row',r) for r in g['rows']]+[(r['line'],'control',r) for r in g['controls']]
        for _,kind,r in sorted(sequence,key=lambda x:x[0]):
            if kind=='control':text.append('CONTROL L'+str(r['line'])+' '+r['source'])
            else:
                text.append('ROW '+r['review_row_id']+' | L'+str(r.get('line') or '-')+' '+r.get('speaker','')+' | '+
                    json.dumps({'EN':r['source'],'ZH':r['current_line'],'kind':r['current_kind']},ensure_ascii=False))
        text.append('')
    target.write_text('\n'.join(text)+'\n',encoding='utf8')
    receipts.append({'packet':source.stem,'path':target.relative_to(ROOT).as_posix(),'sha256':sha256(target.read_bytes()).hexdigest(),
                     'lines':len(text),'scenes':len(scenes),'rows':sum(len(s['rows']) for s in scenes)})
out=folder/'readers-manifest.json'
if out.exists():raise ValueError('New readers manifest only')
out.write_text(json.dumps(receipts,ensure_ascii=False,indent=2)+'\n',encoding='utf8')
print(json.dumps(receipts,ensure_ascii=False,indent=2))
