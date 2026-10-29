"""Independent read-only source audit; writes only its review directory."""
from pathlib import Path
import sys,json,re,hashlib,zipfile,collections,importlib.util
sys.dont_write_bytecode=True
ROOT=Path(__file__).resolve().parents[5]
R3=ROOT/'localization/editorial/r3-names'; HERE=Path(__file__).resolve().parent
sys.path.insert(0,str(ROOT/'localization/tools'))
from codec import decrypt_file
sha=lambda b:hashlib.sha256(b).hexdigest()
load=lambda p:json.loads(p.read_text(encoding='utf8'))
F=R3/'compiled/final-01'; manifest=load(F/'manifest.json'); registry=load(ROOT/'localization/translations/character-names.json'); inv=load(R3/'engineering/inventory.json')
ops=[json.loads(x) for x in (F/'operations.jsonl').read_text(encoding='utf8').splitlines()]; bindings=load(F/'bindings.json'); bm={b['op_id']:b for b in bindings}
checks=collections.Counter(); holds=[]; details=[]
def check(ok,label):
 if not ok: raise AssertionError(label)
 checks[label]+=1
# Independent recursive JSON lexer: raw token locations, value pointers and all keys.
def tokens(s):
 dec=json.JSONDecoder(); out={}; keys=[]
 def ws(i):
  while i<len(s) and s[i].isspace():i+=1
  return i
 def node(i,p):
  i=ws(i)
  if s[i]=='{':
   i=ws(i+1)
   if s[i]=='}':return i+1
   while True:
    k,j=dec.raw_decode(s,i);keys.append((p,k,s[i:j]));i=ws(j);assert s[i]==':';q=p+'/'+k.replace('~','~0').replace('/','~1');i=ws(node(i+1,q))
    if s[i]=='}':return i+1
    assert s[i]==',';i=ws(i+1)
  if s[i]=='[':
   i=ws(i+1);n=0
   if s[i]==']':return i+1
   while True:
    i=ws(node(i,p+'/'+str(n)));n+=1
    if s[i]==']':return i+1
    assert s[i]==',';i=ws(i+1)
  v,j=dec.raw_decode(s,i);out[p]=(i,j,v);return j
 assert ws(node(0,''))==len(s)
 return out,keys
names={n['name_id']:n for n in registry['names']}
check(len(names)==36,'registry36')
inputs={}
for p in [ROOT/'localization/translations/character-names.json',R3/'NAMING_RULES.md',R3/'tools/compile_names.py',R3/'engineering/inventory.py',R3/'engineering/test_names.py',R3/'engineering/inventory.json',F/'manifest.json',F/'operations.jsonl',F/'bindings.json',R3/'review/names-01.json',ROOT/'localization/translations/editorial-r2-repairs.jsonl',ROOT/'localization/layout/src/PRG/RadioLabels.java',ROOT/'localization/layout/tests/RadioLabelsTest.java',R3/'tools/sync_radio_names.py',ROOT/'localization/layout/tools/java/RadioLabelsPatch.java']:
 inputs[p.relative_to(ROOT).as_posix()]=sha(p.read_bytes())
formal=ROOT/'localization/translations/character-name-repairs.jsonl'
check(formal.read_bytes()==(F/'operations.jsonl').read_bytes(),'formal_ops_exact_final01');inputs[formal.relative_to(ROOT).as_posix()]=sha(formal.read_bytes())
for field,path in [('registrySHA',ROOT/'localization/translations/character-names.json'),('inventorySHA',R3/'engineering/inventory.json'),('compilerSHA',R3/'tools/compile_names.py'),('operationsSHA',F/'operations.jsonl'),('bindingsSHA',F/'bindings.json')]:check(manifest[field]==sha(path.read_bytes()),'manifest_input_SHA')
before={}; after={}; groups=collections.defaultdict(list)
for o in ops:groups[(o['archive'],o['archive_entry'])].append(o)
for a,pin in manifest['baseline_archiveSHA'].items():
 ap=ROOT/manifest['baseline']/a;check(sha(ap.read_bytes())==pin,'archive_SHA');inputs[ap.relative_to(ROOT).as_posix()]=pin
 with zipfile.ZipFile(ap) as z:
  check(z.testzip() is None,'archive_CRC')
  for r in inv['resources']:
   if r['archive']==a:
    k=(a,r['entry']);before[k]=decrypt_file(z.read(r['entry']));check(sha(before[k])==r['plaintextSHA'],'all_inventory_plaintext_SHA')
for k,data in before.items():
 s=data.decode('utf8'); replacements=[]; os=groups[k]
 jt,jkeys=tokens(s) if k[1].split('/')[0] in ('datav','datay') else ({},[])
 lines=s.splitlines(keepends=True); starts=[];pos=0
 for line in lines:starts.append(pos);pos+=len(line)
 for o in os:
  check(sha(data)==o['before_resource_sha256'],'op_resource_SHA');b=bm[o['op_id']]
  if o['kind']=='json':
   st,en,value=jt[o['pointer']];check(isinstance(value,str),'json_scalar_string');check(value==o['old'],'op_old')
   check(s[st:en]==json.dumps(o['old'],ensure_ascii=False),'JSON_original_raw_encoding_canonical')
   newraw=json.dumps(o['new'],ensure_ascii=False);replacements.append((st,en,newraw))
   if not o['pointer'].startswith('/ui.'):
    holds.append({'op_id':o['op_id'],'archive':k[0],'entry':k[1],'pointer':o['pointer'],'reason':'display consumer not yet independently established'})
   prefix=''
  else:
   li=o['line']-1;value=lines[li].rstrip('\r\n');check(value==o['old'],'op_old');st=starts[li];en=st+len(value);replacements.append((st,en,o['new']))
   prefixes={c.get('prefix','') for c in b['source_carriers']};check(len(prefixes)==1,'same_field_prefix');prefix=prefixes.pop();check(value.startswith(prefix) and o['new'].startswith(prefix),'prefix_unchanged')
  old=o['old'][len(prefix):];new=o['new'][len(prefix):];spans=b['authorized_spans_in_value'];cursor=0;parts=[]
  marker=re.compile(r'@[A-Za-z][A-Za-z0-9_]*|\$\{[^{}]+\}|\{[^{}\r\n]+\}|%(?:[1-9]\d*\$)?(?:[-+#0]*\d*(?:\.\d+)?)?[sdifouxXeEgGc](?![A-Za-z])|</?[A-Za-z][^<>\r\n]*>|\|')
  check(marker.findall(old)==marker.findall(new),'marker_order_exact')
  idrx=re.compile(r'(?<![A-Za-z0-9_])(?:[A-Za-z]+[0-9][A-Za-z0-9_-]*|[A-Za-z][A-Za-z0-9]*_[A-Za-z0-9_]+)(?![A-Za-z0-9_])')
  check(idrx.findall(old)==idrx.findall(new),'program_ID_and_The0_exact')
  check([x for x in old.splitlines() if not x.strip()]==[x for x in new.splitlines() if not x.strip()],'empty_join_lines_exact')
  for c in b['source_carriers']:
   sourcepath=ROOT/c['source_blob'];sourcebytes=sourcepath.read_bytes();check(sha(sourcebytes)==c['source_resourceSHA'],'source_blob_SHA')
   sourcetext=sourcebytes.decode('utf8');actual=tokens(sourcetext)[0][c['pointer']][2] if 'pointer' in c else sourcetext.splitlines()[c['line']-1]
   expected=c['source'] if 'pointer' in c else c.get('source_raw_line')
   check(actual==expected,'source_sample_alignment')
  for e in spans:
   check(cursor<=e['start']<e['end']<=len(old),'ordered_legal_spans');check(old[e['start']:e['end']]==e['old'],'span_old');n=names[e['name_id']];rule=n
   if e['nickname']:
    rule=n['nicknames'][0];check(any(c['archive']==k[0] and c['entry']==k[1] and c.get('line')==o.get('line') for c in rule['allowed_carriers']),'nickname_exact_scope');check(any(re.search(r'(?<![A-Za-z0-9_@])TOM(?![A-Za-z0-9_])',c.get('source') or '') for c in b['source_carriers']),'nickname_uppercase_TOM')
   check(any(e['old_form'].casefold()==x.casefold() for x in rule['old_forms']),'registry_old_form');check(e['target']==rule['target'],'registry_target')
   rep=e['existing_stutter_repetitions'];pre=e['old'][:-len(e['old_form'])]
   check(len(pre)==2*rep,'stutter_count');check(all(pre[i+1] in '-、，' and pre[i].casefold() in {e['old_form'][0].casefold(),*[x[0].casefold() for x in rule['source_forms']],*(['汤'] if e['name_id']=='Tomcat' else [])} for i in range(0,len(pre),2)),'stutter_old_sound')
   expected=''.join(e['target'][0]+pre[i+1] for i in range(0,len(pre),2))+e['target'];check(e['new']==expected,'stutter_new_sound_only')
   parts.extend([old[cursor:e['start']],e['new']]);cursor=e['end']
  parts.append(old[cursor:]);check(''.join(parts).encode()==new.encode(),'all_non_name_bytes_preserved_in_field')
  # Inspect suspicious script-looking lines; ordinary string/name is not proof of display.
  if o['kind']=='line' and not (prefix.lstrip().startswith(('*','text:','lang(','auto(')) or re.fullmatch(r'\s*[A-Za-z][A-Za-z0-9_/]*:\s*',prefix)):
   holds.append({'op_id':o['op_id'],'archive':k[0],'entry':k[1],'line':o['line'],'prefix':prefix,'old':o['old'],'reason':'script carrier consumer requires verification'})
 replacements.sort();check(all(x[1]<=y[0] for x,y in zip(replacements,replacements[1:])),'nonoverlap_resource')
 result=s
 for st,en,newraw in reversed(replacements):result=result[:st]+newraw+result[en:]
 raw=result.encode();after[k]=raw
 check(re.findall(rb'\r\n|\r|\n',data)==re.findall(rb'\r\n|\r|\n',raw),'physical_EOL')
 if jt:
  at,akeys=tokens(result);check(jkeys==akeys,'all_JSON_keys_raw_identical');changed={o['pointer'] for o in os};check(all(at[p][2]==v[2] for p,v in jt.items() if p not in changed),'all_non_target_JSON_values')
 if not os:check(raw==data,'non_target_resource_bytes')
 else:
  base=F/'plaintext'/k[0]/k[1];check(Path(str(base)+'.before.txt').read_bytes()==data,'preview_before_exact');check(Path(str(base)+'.after.txt').read_bytes()==raw,'independent_splice_preview_exact');details.append({'archive':k[0],'entry':k[1],'beforeSHA':sha(data),'afterSHA':sha(raw),'operations':len(os)})
# Every R2 target must match candidate6; only exact R3 target changes allowed.
r2=[json.loads(x) for x in (ROOT/'localization/translations/editorial-r2-repairs.jsonl').read_text(encoding='utf8').splitlines() if x.strip()]
for o in r2:
 k=(o['archive'],o['archive_entry']);get=lambda raw:raw.decode().splitlines()[o['line']-1] if o['kind']=='line' else tokens(raw.decode())[0][o['pointer']][2]
 check(get(before[k])==o['new'],'R2_baseline_exact');match=[x for x in groups[k] if x['kind']==o['kind'] and x.get('line',x.get('pointer'))==o.get('line',o.get('pointer'))];check(get(after[k])==(match[0]['new'] if match else o['new']),'R2_only_name_change')
# Static data sync in memory; no author outputs written.
p=R3/'tools/sync_radio_names.py';spec=importlib.util.spec_from_file_location('sync',p);sync=importlib.util.module_from_spec(spec);spec.loader.exec_module(sync)
for p,expected in sync.outputs().items():check(p.read_text(encoding='utf8')==expected,'radio_sync_current');inputs[p.relative_to(ROOT).as_posix()]=sha(p.read_bytes())
helper=(ROOT/'localization/layout/src/PRG/RadioLabels.java').read_text(encoding='utf8');aliases=[]
for n in registry['names']:
 check(len(n['target'])<=6,'frequency_six_columns')
 for a in dict.fromkeys(n['source_forms']+n['radio_aliases']):
  aliases.append(a.casefold());check(('if ("'+a+'".equalsIgnoreCase(name)) return '+('name' if n['preserve_ascii_case'] else '"'+n['target']+'"')+';') in helper,'alias_mapping_exact')
check(len(set(aliases))==37,'alias37');check('localized(text) ? "classic" : role' in helper,'Latin_role_preserved_static');check('"The0".equalsIgnoreCase(name)) return name;' in helper,'The0_case_static')
result={'schema':'r3.engineering-independent-review.v1','status':'HOLD' if holds else 'PASS','phase':'candidate6_to_final01_preview_only','checks':dict(checks),'operations':len(ops),'resources':len(before),'touched_resources':sum(bool(v) for v in groups.values()),'r2_operations':len(r2),'inputs':inputs,'holds':holds,'resource_splices':details,'limits':['Does not replace 36-name semantic human review.','Candidate7 packaged classes/fonts and final17 CPU not available for this phase; not run.','No game runtime or display consumer proof inferred from a string type.'],'writes':'only review/engineering-isolated-01 and engineering-01.json/.md'}
(HERE/'audit-result.json').write_text(json.dumps(result,ensure_ascii=False,indent=2)+'\n',encoding='utf8')
print(json.dumps({'status':result['status'],'checks':dict(checks),'holds':holds},ensure_ascii=True))
