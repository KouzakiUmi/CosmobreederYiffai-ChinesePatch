"""Frozen dictionary test data only; writes this component directory, no saves."""
import json,argparse,sys
from pathlib import Path
ROOT=Path(__file__).resolve().parents[3]
sys.path.insert(0,str(ROOT/'tools/lib'))
from output_paths import check_outputs, workspace_output
parser=argparse.ArgumentParser()
parser.add_argument('--pak-json',type=Path)
parser.add_argument('--jar-json',type=Path)
parser.add_argument('--output-dir',type=Path,required=True)
args=parser.parse_args()
OUT=workspace_output(ROOT,args.output_dir,parents=('payload','build'))
if not OUT.is_dir():
    parser.error('output directory must exist')
check_outputs(OUT,('item-corpus.tsv',))
rows=[]
for variant,name,override in [('PAK','dictionary-nsfw.json',args.pak_json),('JAR','dictionary.json',args.jar_json)]:
    p=override if override else ROOT/'tests/java/fixtures'/name
    d=json.loads(p.read_text('utf8'))
    for key,value in sorted(d.items()):
        if key.endswith('.desc') and '.' not in key[:-5] and key[:-5]+'.name' in d:
            rows.append((variant,key[:-5],d[key[:-5]+'.name'],value))
(OUT/'item-corpus.tsv').write_text('\n'.join('\t'.join(v.replace('\\','\\\\').replace('\n','\\n').replace('\r','\\r').replace('\t','\\t') for v in row) for row in rows)+'\n',encoding='utf8')
print('ITEM_CORPUS records='+str(len(rows))+' PAK='+str(sum(r[0]=='PAK' for r in rows))+' JAR='+str(sum(r[0]=='JAR' for r in rows)))
