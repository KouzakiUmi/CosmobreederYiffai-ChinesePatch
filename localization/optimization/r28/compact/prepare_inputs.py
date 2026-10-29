"""Frozen dictionary test data only; writes this component directory, no saves."""
import json,hashlib,argparse
from pathlib import Path
ROOT=Path(__file__).resolve().parents[4]
DEFAULT_OUT=Path(__file__).resolve().parent
parser=argparse.ArgumentParser()
parser.add_argument('--pak-json',type=Path)
parser.add_argument('--jar-json',type=Path)
parser.add_argument('--output-dir',type=Path,default=DEFAULT_OUT)
args=parser.parse_args()
OUT=args.output_dir.resolve(strict=True)
r28=(ROOT/'localization/optimization/r28').resolve(strict=True)
tests=r28/'integration/tests'
relative=OUT.relative_to(tests) if OUT.is_relative_to(tests) else None
if not OUT.is_dir() or not (OUT==r28/'compact' or (relative is not None and len(relative.parts)==2 and relative.name=='compact')):
    parser.error('output must be pre-existing r28/compact or r28/integration/tests/<run>/compact')
rows=[]
for variant,name,override in [('PAK','dictionary-nsfw.json',args.pak_json),('JAR','dictionary.json',args.jar_json)]:
    p=override if override else ROOT/'docs/font-layout-audit-20261025/regressions'/name
    d=json.loads(p.read_text('utf8'))
    for key,value in sorted(d.items()):
        if key.endswith('.desc') and '.' not in key[:-5] and key[:-5]+'.name' in d:
            rows.append((variant,key[:-5],d[key[:-5]+'.name'],value))
(OUT/'item-corpus.tsv').write_text('\n'.join('\t'.join(v.replace('\\','\\\\').replace('\n','\\n').replace('\r','\\r').replace('\t','\\t') for v in row) for row in rows)+'\n',encoding='utf8')
print('ITEM_CORPUS records='+str(len(rows))+' PAK='+str(sum(r[0]=='PAK' for r in rows))+' JAR='+str(sum(r[0]=='JAR' for r in rows)))
