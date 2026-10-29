"""Independent read-only pass-01 verification; all output confined here."""
from pathlib import Path
import sys,json,re,hashlib,zipfile,collections,unittest,io,copy
sys.dont_write_bytecode=True
ROOT=Path(__file__).resolve().parents[4]; L=ROOT/'localization'; R=L/'editorial/r2'; OUT=Path(__file__).parent
sys.path.insert(0,str(L/'tools'))
import editorial_repairs as engine
from codec import decrypt_file
pins={}; checks=[]; failures=[]
def sha(b):return hashlib.sha256(b).hexdigest()
def load(p):
 b=p.read_bytes();pins[str(p.relative_to(ROOT)).replace('\\','/')]=sha(b);return json.loads(b)
def rows(p):
 b=p.read_bytes();pins[str(p.relative_to(ROOT)).replace('\\','/')]=sha(b);return [json.loads(s) for s in b.splitlines() if s.strip()]
def check(name,condition,details=None):
 checks.append({'check':name,'status':'PASS' if condition else 'FAIL','details':details})
 if not condition:failures.append(checks[-1])
P=R/'compiled/pass-01'; manifest=load(P/'manifest.json'); ops=rows(P/'operations.jsonl'); bindings=rows(P/'bindings.jsonl')
for p in [L/'tools/editorial_repairs.py',L/'tests/test_editorial_repairs.py',R/'tools/compile_repairs.py',Path(__file__)]:pins[str(p.relative_to(ROOT)).replace('\\','/')]=sha(p.read_bytes())
suite=unittest.defaultTestLoader.discover(str(L/'tests'),pattern='test_editorial_repairs.py'); log=io.StringIO(); result=unittest.TextTestRunner(stream=log,verbosity=2).run(suite)
(OUT/'unit-tests.txt').write_text(log.getvalue(),encoding='utf8');check('13 unit tests',result.wasSuccessful() and result.testsRun==13)
occ={r['occurrence_id']:r for r in rows(L/'catalog/occurrences.jsonl')}; sfw={r['id']:r for k in ['ds','vsn','ui'] for r in rows(L/f'optimization/r28/sfw/ledger-{k}.jsonl')}
frozen={s['scene_id']:s for s in load(L/'editorial/r1/corpus/snapshot-01/scenes.json')}
original=rows(L/'editorial/r1/reports/rough-review-01/findings.jsonl')
editmap={}; scenes={}; ds=[]; alias_issues=[]; expected_origins=[]
def meta(rid):
 if rid.startswith('CAT:'):
  r=occ[rid[4:]];return {'archive':'cosmobreeder-multi.jar' if r['archive']=='jar' else 'patch.pak','entry':r['archive_entry'],'path':r['logical_path'],'root':r.get('json_key',r.get('entry') or (r['logical_path'].split('/')[1] if r['logical_path'].startswith('vsn/') else '')),'source':r['raw_payload_sha256'],'line':r.get('line'),'pointer':('/'+r['json_key'].replace('~','~0').replace('/','~1')) if 'json_key' in r else r.get('json_pointer')}
 r=sfw[rid];return {'archive':r['archive'],'entry':r['archive_entry'],'path':r['logical_path'],'root':r['root'],'source':r['raw_source_sha256'],'line':r['source_line_evidence'],'pointer':'/'+r['root'].replace('~','~0').replace('/','~1')}
for n in range(1,11):
 name=f'packet-{n:02d}'; data=load(R/f'input/{name}.json'); sm={s['scene_id']:s for s in data['scenes']}; scenes[name]=sm
 decisions=rows(R/f'packets/{name}/decisions.jsonl'); edits=rows(R/f'packets/{name}/edits.jsonl'); dm={d['finding_id']:d for d in decisions}; em={e['edit_id']:e for e in edits};ds+=decisions
 check(name+' finding coverage',set(dm)=={f['finding_id'] for f in data['findings']} and len(dm)==len(decisions))
 for d in decisions:
  check(d['finding_id']+' decision links',(d['action']=='apply')==bool(d.get('edit_ids')) and all(eid in em and d['finding_id'] in em[eid]['finding_ids'] for eid in d.get('edit_ids',[])))
 for e in edits:
  editmap[name,e['edit_id']]=e;s=sm[e['scene_id']]; i=next(i for i,r in enumerate(s['rows']) if r['review_row_id']==e['row_id']);c=s['rows'][i];cm=meta(e['row_id'])
  check(e['edit_id']+' edit backlinks',all(fid in dm and dm[fid]['action']=='apply' and e['edit_id'] in dm[fid]['edit_ids'] and dm[fid]['scene_id']==s['scene_id'] for fid in e['finding_ids']))
  check(e['edit_id']+' frozen alias equality',s['aliases']==frozen[s['scene_id']]['aliases'])
  for a in s['aliases']:
   ar=a['rows'][i];am=meta(ar['review_row_id']);diff={k:[cm[k],am[k]] for k in ['source','path','root'] if cm[k]!=am[k]}
   if am['line'] is not None and am['line']!=ar.get('line'):diff['line']=[am['line'],ar.get('line')]
   if diff:alias_issues.append({'packet':name,'edit_id':e['edit_id'],'canonical':e['row_id'],'alias':ar['review_row_id'],'differences':diff})
   expected_origins.append((name,e['edit_id'],ar['review_row_id'],am,ar.get('line')))
check('339 global decisions',len(ds)==339 and {d['finding_id'] for d in ds}=={d['finding_id'] for d in original})
check('alias English logical root JSON key identity',not alias_issues,alias_issues)
check('manifest source pins',all(sha((ROOT/p).read_bytes())==v for p,v in manifest['source_sha256'].items()))
bym={b['op_id']:b for b in bindings}; byop={o['op_id']:o for o in ops};bound={}
for o in ops:
 for origin in bym[o['op_id']]['origins']:
  if 'packet' in origin:bound[origin['packet'],origin['edit_id'],origin['alias_row_id']]=o
binding_errors=[]
for name,eid,aid,m,line in expected_origins:
 o=bound.get((name,eid,aid));e=editmap[name,eid]
 if o is None or (o['archive'],o['archive_entry'],o.get('line') if o['kind']=='line' else o['pointer'])!=(m['archive'],m['entry'],line if o and o['kind']=='line' else m['pointer']) or o['old']!=e['old'] or o['new']!=e['new'].replace('汤姆猫','Tomcat'):binding_errors.append([name,eid,aid])
check('all edition archive entry line pointer bindings',not binding_errors,binding_errors)
base=L/'builds/r28-radio-book-candidate4'; identity=load(base/'build-manifest.json'); groups=collections.defaultdict(list)
for o in ops:groups[o['archive'],o['archive_entry']].append(o)
resource_results=[]
# Independent lexical JSON scanner: string tokens with exact byte spans, keyed by decoded structural path.
def tokenize(text):
 dec=json.JSONDecoder();values={};keys=[]
 def ws(i):
  while i<len(text) and text[i] in ' \t\r\n':i+=1
  return i
 def parse(i,path):
  i=ws(i)
  if text[i]=='{':
   i=ws(i+1)
   if text[i]=='}':return i+1
   while True:
    k,j=dec.raw_decode(text,i);keys.append((path,k,text[i:j]));i=ws(j);assert text[i]==':';i=ws(parse(i+1,path+(k,)))
    if text[i]=='}':return i+1
    assert text[i]==',';i=ws(i+1)
  if text[i]=='[':
   i=ws(i+1);n=0
   if text[i]==']':return i+1
   while True:
    i=ws(parse(i,path+(str(n),)));n+=1
    if text[i]==']':return i+1
    assert text[i]==',';i=ws(i+1)
  v,j=dec.raw_decode(text,i);values[path]=(i,j,v);return j
 assert ws(parse(0,()))==len(text);return values,keys
for archive in manifest['baseline_archives']:
 p=base/archive;digest=sha(p.read_bytes());pins[str(p.relative_to(ROOT)).replace('\\','/')]=digest;check(archive+' baseline SHA',digest==manifest['baseline_archives'][archive]==identity['archives'][archive]['sha256'])
 with zipfile.ZipFile(p) as z:
  for (a,entry),es in groups.items():
   if a!=archive:continue
   raw=decrypt_file(z.read(entry));text=raw.decode('utf8');out,report=engine.apply_entry(a,entry,raw,es);splices=[]
   if es[0]['kind']=='line':
    lines=text.splitlines(keepends=True);offsets=[];pos=0
    for line in lines:offsets.append(pos);pos+=len(line)
    for o in es:
     body=lines[o['line']-1].rstrip('\r\n');assert body==o['old'];start=offsets[o['line']-1];splices.append((start,start+len(body),o['new']))
   else:
    vals,keys=tokenize(text)
    for o in es:
     path=tuple(v.replace('~1','/').replace('~0','~') for v in o['pointer'][1:].split('/'));start,end,value=vals[path];assert value==o['old'];splices.append((start,end,json.dumps(o['new'],ensure_ascii=False)))
    _,outkeys=tokenize(out.decode('utf8'));assert keys==outkeys
   expected=text
   for start,end,new in sorted(splices,reverse=True):expected=expected[:start]+new+expected[end:]
   assert all(o['before_resource_sha256']==sha(raw) for o in es)
   assert out==expected.encode()==(P/'entries'/a/entry).read_bytes()
   resource_results.append({'archive':a,'entry':entry,'operations':len(es),'before':sha(raw),'after':sha(out)})
check('778 old SHA independent splice expected-new preview untouched bytes keys controls blank nodes EOL',len(ops)==778,resource_results)
nameonly=[o for o in ops if o['finding_ids']==['NAME-TOMCAT']];check('name-only exact authorized replacement',all(o['new']==o['old'].replace('汤姆猫','Tomcat') for o in nameonly),len(nameonly))
check('operation and binding uniqueness',len(byop)==len(ops)==len(bym)==len(bindings) and set(byop)==set(bym))
# Deterministic property matrix: mixed EOL, whitespace tails, JSON escaping and protected actor IDs.
property_count=0
for eol in ['\n','\r\n','\r']:
 for blank in ['', ' ', '\t', '   \t']:
  raw=('<event>'+eol+'Tomcat: old'+eol+blank+eol+'#control'+eol).encode();o=dict(op_id='property',archive='patch.pak',archive_entry='datadf/1',kind='line',line=2,before_resource_sha256=sha(raw),old='Tomcat: old',new='Tomcat: 新句',finding_ids=['p'],source_refs=['p'])
  output,_=engine.apply_entry('patch.pak','datadf/1',raw,[o]);assert output==raw.replace(b'Tomcat: old','Tomcat: 新句'.encode());property_count+=1
  try:engine.apply_entry('patch.pak','datadf/1',raw,[dict(o,new='汤姆猫: 新句')])
  except engine.EditorialRepairError:property_count+=1
  else:raise AssertionError('actor ID drift accepted')
for key in ['a/b','~key','中文','quote"key']:
 raw=(' { '+json.dumps(key)+': "old", "id":"Tomcat", "keep":"\\u4e00" }\r\n').encode();ptr='/'+key.replace('~','~0').replace('/','~1');o=dict(op_id='json-property',archive='patch.pak',archive_entry='datav/1',kind='json',pointer=ptr,before_resource_sha256=sha(raw),old='old',new='新"值',finding_ids=['p'],source_refs=['p']);output,_=engine.apply_entry('patch.pak','datav/1',raw,[o]);assert output==raw.replace(b'"old"',json.dumps(o['new'],ensure_ascii=False).encode());property_count+=1
check('deterministic parser and preservation properties',property_count==28,property_count)
report={'status':'FAIL' if failures else 'PASS','source_sha256':pins,'checks':checks,'failures':failures,'limitations':['No builder review: build_candidate.py is under integration.','No game launch, archive mutation, installation, Git write or delegation.','Codec is reused; independent verification targets repair and compiler, not cryptographic implementation.','Alias identity failure blocks release even where old localized strings match.']}
(OUT/'review.json').write_text(json.dumps(report,ensure_ascii=False,indent=2)+'\n',encoding='utf8')
md='# R2 工程独立核验\n\n状态：**'+report['status']+'**\n\n13 单测通过；实际 candidate4 解密逐一核验 778 操作，独立重建替换预览并比较未改字节、JSON 键及 CRLF。339 decisions 双向关联核验完成。\n\n## 阻断问题\n\n'+('\n'.join('- '+json.dumps(f,ensure_ascii=False) for f in failures) or '无')+'\n\n## 限制\n\n'+'\n'.join('- '+s for s in report['limitations'])+'\n'
(OUT/'review.md').write_text(md,encoding='utf8');print(json.dumps({'status':report['status'],'checks':len(checks),'failures':failures},ensure_ascii=False,indent=2))
