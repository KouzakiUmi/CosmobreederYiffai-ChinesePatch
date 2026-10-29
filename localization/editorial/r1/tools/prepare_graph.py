"""Extract source DS entry/include structure; lexical edges are not runtime reachability."""
from pathlib import Path
from hashlib import sha256
import json
import re
import sys
import zipfile

ROOT=Path(__file__).resolve().parents[4]
sys.path.insert(0,str(ROOT/'localization/tools'))
from codec import decrypt_file

if len(sys.argv)!=2:
    raise SystemExit('prepare_graph.py NEW-r1-corpus-snapshot/script-graph.json')
out=Path(sys.argv[1]).resolve()
if out.exists() or not out.is_relative_to(ROOT/'localization/editorial/r1/corpus'):
    raise ValueError('New corpus graph only')
nodes=[];pins={}
for mode,name in [('sfw','cosmobreeder-multi.jar'),('nsfw','patch.pak')]:
    path=ROOT/'backup'/name;pins[path.relative_to(ROOT).as_posix()]=sha256(path.read_bytes()).hexdigest()
    with zipfile.ZipFile(path) as z:
        for entry in ['datadf/1','datadm/1']:
            source=decrypt_file(z.read(entry)).decode('utf8').splitlines()
            headers=[(i,line.strip()[1:-1]) for i,line in enumerate(source) if re.fullmatch(r'\s*<[^>]+>\s*',line)]
            for index,(start,root) in enumerate(headers):
                end=headers[index+1][0] if index+1<len(headers) else len(source)
                body=source[start:end]
                edges=[]
                for offset,line in enumerate(body):
                    for match in re.finditer(r'\binclude\s*\{\s*([^}]+?)\s*\}',line):
                        edges.append({'target':match.group(1),'line':start+offset+1})
                controls=[{'line':start+i+1,'source':line} for i,line in enumerate(body)
                          if re.match(r'^\s*(?:include\b|if\b|else\b|[{}])',line)]
                nodes.append({'mode':mode,'archive_entry':entry,'root':root,'source_range':[start+1,end],
                              'include_edges':edges,'conditional_controls':controls})
value={'status':'lexical_source_graph_not_runtime_reachability','source_sha256':pins,'nodes':nodes,
       'notes':['Conditions are retained as source text; no symbolic evaluation or path ordering is claimed.',
                'Entries without text still matter as include callers; resolve aliases before attributing anonymous speakers.']}
out.write_text(json.dumps(value,ensure_ascii=False,indent=2)+'\n',encoding='utf8')
print(json.dumps({'entries':len(nodes),'include_edges':sum(len(n['include_edges']) for n in nodes)},ensure_ascii=False))
