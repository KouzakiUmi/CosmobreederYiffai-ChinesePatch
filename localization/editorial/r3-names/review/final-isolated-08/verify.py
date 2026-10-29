"""Independent candidate8 archive audit. No game/build/install; review-only output."""
from pathlib import Path
import sys,json,hashlib,zipfile,re,struct,io,argparse
sys.dont_write_bytecode=True
ROOT=Path(__file__).resolve().parents[5];L=ROOT/'localization';R=L/'editorial/r3-names';OUT=Path(__file__).parent
sys.path.insert(0,str(L/'tools'))
from codec import decrypt_file
from layout_fonts import parse_fnt
from projectlib import parse_atlas
from PIL import Image,ImageDraw
B=L/'builds/r28-editorial-repairs-candidate6';F=L/'builds/r28-character-names-candidate8';P=R/'compiled/final-01'
sha=lambda b:hashlib.sha256(b).hexdigest();evidence={};checks=[]
def pin(p):
 data=p.read_bytes();evidence[p.relative_to(ROOT).as_posix()]=sha(data);return data
def load(p):return json.loads(pin(p))
def rows(p):return [json.loads(s) for s in pin(p).splitlines() if s.strip()]
def check(name,ok,detail=None):
 checks.append({'check':name,'status':'PASS' if ok else 'FAIL','details':detail})
def pointer(v,p):
 for k in p.lstrip('/').split('/'):
  k=k.replace('~1','/').replace('~0','~');v=v[int(k)] if isinstance(v,list) else v[k]
 return v
ap=argparse.ArgumentParser();ap.add_argument('--final',action='store_true');args=ap.parse_args()
build=load(F/'build-manifest.json');nm=load(P/'manifest.json');eng=load(R/'review/engineering-01.json');pin(R/'review/engineering-01.md');sem=load(R/'review/names-01.json');reg=load(L/'translations/character-names.json');ops=rows(L/'translations/character-name-repairs.jsonl');r2=rows(L/'translations/editorial-r2-repairs.jsonl');comp=load(L/'optimization/r28/names/component.json');builder=pin(L/'optimization/r28/integration/build_candidate.py').decode();pin(Path(__file__))
check('full10 components actual build',build['selected_components']==['core','pattern','compact','scenes','sfw','vsn','images','radio','editorial','names'] and build['full_component_set'] and build['status']=='integrated_candidate_not_real_clip_CRT_input_acceptance' and all(c['exit_code']==0 for c in build['commands']),build['commands'])
check('names after R2 before font; all-component and evidence gates source review',builder.index('repaired,editorial_reports=')<builder.index('renamed,name_reports=')<builder.index('font_assets=optimized_fonts.build_assets') and "if 'names' in selected and set(selected)!=set(COMPONENTS)" in builder and "carrier_review['evidence_sha256']" in builder and "name_manifest['baseline_archiveSHA']" in builder and "'--check'" in builder)
check('formal839 operation bytes match frozen preview',pin(L/'translations/character-name-repairs.jsonl')==pin(P/'operations.jsonl') and len(ops)==839)
check('exact36 semantic targets and no blockers',len(reg['names'])==36 and {n['name_id']:n['target'] for n in reg['names']}=={n['name_id']:n['target'] for n in sem['names']} and not any(n['blocking_issues'] for n in sem['names']) and sha(pin(ROOT/reg['semantic_review']['path']))==reg['semantic_review']['sha256'])
for label,mapping in [('frozen engineering evidence',eng['evidence_sha256']),('actual builder source snapshot',build['source_sha256'])]:
 drift=[]
 for name,h in mapping.items():
  if sha(pin(ROOT/name))!=h:drift.append(name)
 check(label+' all SHA unchanged',not drift,drift)
check('builder source snapshot includes carrier review and all carrier evidence',all(p in build['source_sha256'] for p in list(eng['evidence_sha256'])+[comp['carrier_review']]))
check('manifest names reports bound',build['resource_reports']['names']['operation_count']==839 and build['resource_reports']['names']['r2_preservation']==778 and build['resource_reports']['names']['registry_sha256']==nm['registrySHA'] and build['resource_reports']['names']['operations_sha256']==nm['operationsSHA'])
# Exact generated helper source and staging compilation identity.
helper=L/'layout/src/PRG/RadioLabels.java';staged=F/'staging-src/localization/layout/src/PRG/RadioLabels.java'
helper_bytes=pin(helper);staged_bytes=pin(staged)
check('RadioLabels staged source exact reviewed helper except Windows source EOL translation',helper_bytes.replace(b'\r\n',b'\n')==staged_bytes.replace(b'\r\n',b'\n'),{'source_bytes':len(helper_bytes),'staged_bytes':len(staged_bytes),'source_CRLF':helper_bytes.count(b'\r\n'),'staged_CRLF':staged_bytes.count(b'\r\n'),'scope':'Only Java source staging; game data EOL is byte-exact via frozen preview.'})
fm={};fontpins={}
for parent in [B,F]:
 f=load(parent/'font-manifest.json');fm[parent.name]=f
 for role,v in f['roles'].items():
  for h in [v['original_sha256'],v['sha256']]:fontpins[h.encode()]=('<ROLE_SHA:'+role+'>').encode()
def norm_class(b):
 assert b[:4]==b'\xca\xfe\xba\xbe';n=int.from_bytes(b[8:10],'big');i=10;idx=1;out=[]
 while idx<n:
  tag=b[i];i+=1
  if tag==1:
   size=int.from_bytes(b[i:i+2],'big');i+=2;v=b[i:i+size];i+=size;out.append((tag,fontpins.get(v,v)))
  else:
   size={3:4,4:4,5:8,6:8,7:2,8:2,9:4,10:4,11:4,12:4,15:3,16:2,17:4,18:4,19:2,20:2}[tag];out.append((tag,b[i:i+size]));i+=size
   if tag in (5,6):idx+=1
  idx+=1
 return b[:10],out,b[i:]
targets={(o['archive'],o['archive_entry']) for o in ops};bytarget={};archives={};changed={};classdetails=[];fontdetails=[];rawchanges={};allplaintext={};packaged_helper_sha=None
for archive in ['cosmobreeder-multi.jar','patch.pak']:
 archives[archive]=sha(pin(F/archive));check(archive+' actual archive SHA matches build',archives[archive]==build['archives'][archive]['sha256']);check(archive+' accepted candidate6 SHA',sha(pin(B/archive))==nm['baseline_archiveSHA'][archive])
 with zipfile.ZipFile(B/archive) as z,zipfile.ZipFile(F/archive) as q:
  bn=z.namelist();an=q.namelist();check(archive+' unique entry names and no entry add/remove',len(bn)==len(set(bn)) and len(an)==len(set(an)) and set(bn)==set(an),{'added':sorted(set(an)-set(bn)),'removed':sorted(set(bn)-set(an))});check(archive+' CRC',q.testzip() is None)
  old={n:z.read(n) for n in bn};new={n:q.read(n) for n in an};changed[archive]=[n for n in bn if old[n]!=new[n]];plain_changed=[];errors=[];raw_same_count=0;textcount=0;data_count=0
  route=json.loads(decrypt_file(old['dataq/0']));atlasentry='dataq/'+str(route['/sprites.atlas']);pageentry='dataq/'+str(route['/sprites.png']);check(archive+' atlas routing/metadata unchanged',old['dataq/0']==new['dataq/0'] and old[atlasentry]==new[atlasentry]);_,regions=parse_atlas(decrypt_file(old[atlasentry]).decode())
  for n in bn:
   if not re.fullmatch(r'data[a-z]+/[0-9]+|vsn/[0-9]+',n):continue
   data_count+=1
   if n==pageentry:continue
   k=(archive,n)
   if old[n]==new[n] and k not in targets:raw_same_count+=1;continue
   a=decrypt_file(old[n]);b=decrypt_file(new[n]);allplaintext[k]=(a,b)
   expected=pin(P/'plaintext'/archive/(n+'.after.txt')) if k in targets else a
   if k in targets:check(archive+'/'+n+' accepted source preview BEFORE',a==pin(P/'plaintext'/archive/(n+'.before.txt')))
   if b!=expected:errors.append(n)
   if a!=b:plain_changed.append(n)
   if re.fullmatch(r'(datadf|datadm|datav|datay|vsn)/[1-9][0-9]*',n):textcount+=1
  check(archive+' all encrypted non-atlas entries equal exact name preview or baseline',not errors,{'data_entries':data_count,'raw_identical_non_targets':raw_same_count,'checked_reencrypted_or_target':textcount,'mismatches':errors,'plaintext_changed':plain_changed});check(archive+' precisely authorized plaintext resource set',set(plain_changed)=={e for a,e in targets if a==archive})
  # Whole classes except exact role hash constants, never method-level normalization.
  for n in bn:
   if not n.endswith('.class'):continue
   if old[n]==new[n]:continue
   if n=='PRG/RadioLabels.class':
    packaged_helper_sha=sha(new[n]);ok=new[n]==pin(F/'classes'/n);check('RadioLabels packaged class exact builder output',ok)
    check('RadioLabels independent compiler output exists',(OUT/'independent-classes/PRG/RadioLabels.class').is_file())
    check('RadioLabels packaged class exact independently compiled current source',new[n]==pin(OUT/'independent-classes/PRG/RadioLabels.class'));pin(OUT/'helper-compile.log')
    classdetails.append({'entry':n,'approved':'reviewed exact generated map + independently compiled source','oldSHA':sha(old[n]),'newSHA':sha(new[n])})
   else:
    equal=norm_class(old[n])==norm_class(new[n]);check(n+' entire class remainder identical after only known role-SHA neutralization',equal);classdetails.append({'entry':n,'approved_role_SHA_only':equal,'oldSHA':sha(old[n]),'newSHA':sha(new[n])})
  if archive=='cosmobreeder-multi.jar':check(archive+' actual JF hidden identity gate class byte-identical','PRG/JF.class' in old and old['PRG/JF.class']==new['PRG/JF.class'])
  # Pixel identity outside complete font producer regions; old glyphs compared by codepoint.
  oi=Image.open(io.BytesIO(decrypt_file(old[pageentry]))).convert('RGBA');ni=Image.open(io.BytesIO(decrypt_file(new[pageentry]))).convert('RGBA');check(archive+' atlas full dimensions',oi.size==ni.size)
  mask=Image.new('L',oi.size,0);draw=ImageDraw.Draw(mask)
  for region_name in ['bbc2','classic']:
   rg=next(r for r in regions if r['name']==region_name);x,y=rg['xy'];w,h=rg['size'];draw.rectangle((x,y,x+w-1,y+h-1),fill=255)
  restored=ni.copy();restored.paste(oi,(0,0),mask);check(archive+' all non-font atlas artwork pixels byte-identical',restored.tobytes()==oi.tobytes())
  for role,filename,region_name in [('default','bbc2.fnt','bbc2'),('classic','classic.fnt','classic'),('story12','story12.fnt','bbc2')]:
   f1=parse_fnt(old[filename].decode());f2=parse_fnt(new[filename].decode());rg=next(r for r in regions if r['name']==region_name);x,y=rg['xy'];metric=[];ink=[];relocated=[];ascii_changed=[]
   check(archive+' '+role+' font globals/kernings unchanged',f1.info==f2.info and f1.common==f2.common and f1.pages==f2.pages and f1.kernings==f2.kernings)
   for cp,g in f1.glyphs.items():
    h=f2.glyphs.get(cp)
    if h is None:metric.append(cp);continue
    if any(g[k]!=h[k] for k in g if k not in ['x','y']):metric.append(cp)
    if (g['x'],g['y'])!=(h['x'],h['y']):relocated.append(cp)
    crop=lambda v:(x+v['x'],y+v['y'],x+v['x']+v['width'],y+v['y']+v['height'])
    if oi.crop(crop(g)).tobytes()!=ni.crop(crop(h)).tobytes():ink.append(cp)
    if cp<128 and (h!=g or f1.char_lines[cp]!=f2.char_lines[cp]):ascii_changed.append(cp)
   detail={'archive':archive,'role':role,'old_codepoints':len(f1.glyphs),'new_codepoints':len(f2.glyphs),'relocated':relocated,'changed_nonposition_metrics':metric,'changed_ink':ink,'changed_ASCII_records':ascii_changed};fontdetails.append(detail);check(archive+' '+role+' all old glyph ink/nonposition metrics/ASCII full records',not metric and not ink and not ascii_changed,detail)
   check(archive+' '+role+' live font SHA pinned',sha(new[filename])==fm[F.name]['roles'][role]['sha256'])
   if role=='classic':
    required=''.join(n['target'] for n in reg['names']);bad=[]
    for c in required:
     g=f2.glyphs.get(ord(c))
     if not g or g['xadvance']!=8 or ord(c)>127 and any(g[k]!=v for k,v in [('width',8),('height',8),('xoffset',0),('yoffset',0)]):bad.append(c)
    check(archive+' all36 label glyph actual classic8 grid',not bad,bad)
  # Diagnostic copies must be genuinely paired with production fonts, not arbitrary extras.
  for n in changed[archive]:
   if n.startswith('r28-font/'):
    suffix=n[len('r28-font/'):]
    if suffix in ['bbc2.fnt','classic.fnt','story12.fnt']:check(archive+' '+n+' diagnostic/live equality',new[n]==new[suffix])
    elif suffix in ['bbc2.png','classic.png']:
     rg=next(r for r in regions if r['name']==suffix[:-4]);x,y=rg['xy'];w,h=rg['size'];im=Image.open(io.BytesIO(new[n])).convert('RGBA');check(archive+' '+n+' diagnostic/live pixels',im.size==(w,h) and im.tobytes()==ni.crop((x,y,x+w,y+h)).tobytes())
    elif suffix=='manifest.json':check(archive+' diagnostic font manifest exact',json.loads(new[n])==fm[F.name])
    else:check(archive+' no unapproved diagnostic content change '+n,False)
  allowed={pageentry,'bbc2.fnt','classic.fnt','story12.fnt'}
  unexpected=[n for n in changed[archive] if not re.fullmatch(r'data[a-z]+/[0-9]+|vsn/[0-9]+',n) and not n.endswith('.class') and not n.startswith('r28-font/') and n not in allowed]
  check(archive+' no unrelated raw asset change',not unexpected,unexpected)
  rawchanges[archive]={'raw_changed':len(changed[archive]),'plaintext_name_resources':len(plain_changed),'raw_identical_non_target_data':raw_same_count}
# Exact final839 fields and every R2 complete target, relying on frozen independent span proof.
for o in ops:
 k=(o['archive'],o['archive_entry']);a,b=allplaintext[k]
 get=lambda d:d.decode().splitlines()[o['line']-1] if o['kind']=='line' else pointer(json.loads(d),o['pointer'])
 check('all839 exact old/new complete fields',get(a)==o['old'] and get(b)==o['new'])
opmap={(o['archive'],o['archive_entry'],o['kind'],o.get('line',o.get('pointer'))):o for o in ops}
for o in r2:
 k=(o['archive'],o['archive_entry'])
 if k in allplaintext:a,b=allplaintext[k]
 else:
  with zipfile.ZipFile(B/k[0]) as z,zipfile.ZipFile(F/k[0]) as q:a,b=decrypt_file(z.read(k[1])),decrypt_file(q.read(k[1]))
 get=lambda d:d.decode().splitlines()[o['line']-1] if o['kind']=='line' else pointer(json.loads(d),o['pointer'])
 name=opmap.get((*k,o['kind'],o.get('line',o.get('pointer'))));check('all778 R2 exact except authorized name fields',get(a)==o['new'] and get(b)==(name['new'] if name else o['new']))
# Source-state behavior restrictions independently reviewed in frozen report; actual JF identical above.
oldsrc=pin(B/'staging-src/localization/layout/src/PRG/RadioLabels.java').decode();newsrc=pin(helper).decode()
strip=lambda s:'\n'.join(x for x in s.splitlines() if '// Generated from ' not in x)
check('RadioLabels no draw/geometry/role-code change before generated mappings',strip(oldsrc[:oldsrc.index('    private static boolean localized')])==strip(newsrc[:newsrc.index('    private static boolean localized')]))
check('40 conservative records not claimed globally approved',len(nm['pending_review'])==40,dict(__import__('collections').Counter(x['reason'] for x in nm['pending_review'])))
pending_safe=[]
for item in nm['pending_review']:
 c=item['carrier'];key=(c['archive'],c['entry']);locator=c.get('line',c.get('pointer'));kind='line' if 'line' in c else 'json'
 scoped=opmap.get((*key,kind,locator));pending_safe.append(not scoped or 'NAME:'+item['name_id'] not in scoped['finding_ids'])
check('all40 conservative carriers not applied under their unapproved name identity',all(pending_safe),{'records':len(pending_safe)})
check('Macsen/Gitgud no visible name operations',not any(any(x in o['finding_ids'] for x in ['NAME:Macsen','NAME:Gitgud']) for o in ops))
# Supplementary eligible-body old-form audit; excludes actor prefixes and pending/context carriers.
inv=load(R/'engineering/inventory.json');residual=[];cache={}
for n in reg['names']:
 for c in inv['characters'][n['name_id']]['carriers']:
  if c.get('needs_manual_alignment') or not c.get('matched_variants'):continue
  if c.get('classification') not in ['proper_name_candidate','fenfen_reverse_puzzle_title_not_blanket_name']:continue
  if c.get('classification')=='fenfen_reverse_puzzle_title_not_blanket_name' and n['name_id'] not in ['Sevaw','Erauqs']:continue
  k=(c['archive'],c['entry'])
  if k not in cache:
   if k in allplaintext:cache[k]=allplaintext[k][1]
   else:
    with zipfile.ZipFile(F/k[0]) as q:cache[k]=decrypt_file(q.read(k[1]))
  if 'pointer' in c:value=pointer(json.loads(cache[k]),c['pointer'])
  else:
   line=cache[k].decode().splitlines()[c['line']-1];prefix=c.get('prefix','');assert line.startswith(prefix);value=line[len(prefix):]
  for form in n['old_forms']:
   if form.casefold()==n['target'].casefold():continue
   for hit in re.finditer(re.escape(form),value,re.I if re.search('[A-Za-z]',form) else 0):
    a,b=hit.span();latin=bool(re.search('[A-Za-z0-9]',form))
    if a and (value[a-1] in '@_/\\\\' or latin and re.match('[A-Za-z0-9]',value[a-1])):continue
    if b<len(value) and (value[b] in '_/\\\\' or latin and re.match('[A-Za-z0-9]',value[b])):continue
    if a>=2 and value[a-1]=='.' and re.match('[A-Za-z0-9_]',value[a-2]):continue
    if b+1<len(value) and value[b]=='.' and re.match('[A-Za-z0-9_]',value[b+1]):continue
    residual.append({'name_id':n['name_id'],'archive':k[0],'entry':k[1],'locator':c.get('line',c.get('pointer')),'form':form})
check('independent eligible body old-name residual zero; actor prefixes excluded',not residual,residual)
parent_residual=load(R/'review/residual-audit-final.json');check('parent residual-final evidence confirms zero and excludes actor IDs',parent_residual['count']==0 and not parent_residual['remaining'] and parent_residual['actor_prefixes_excluded_by_design'])
# Complete inherited limitations, not silently reset by R3.
r2final=load(L/'editorial/r2/engineering/final-review.json');not_verified=list(dict.fromkeys(r2final['not_verified']+[
 'R3 40 conservative records:39 contextual Werehund/Werepup carriers and1 source-only/manual-alignment record; not blanket-approved.',
 'Macsen/Gitgud no visible-name carriers; helper map is not authorization to reveal names or bypass JF.',
 '36 localization name targets are independently reviewed creative choices, not author-official etymologies.',
 'Local package and CPU results do not constitute game runtime/GPU/full-map/installation/save acceptance.'
]));cpu=None
if args.final:
 cpu=load(L/'optimization/r28/integration/tests/character-names-final8/results.json')
 check('actual candidate8 completed17 CPU all exit0 and correct archive',cpu.get('status')=='passed_cpu_only_not_real_clip_CRT_input' and len(cpu.get('steps',[]))==17 and all(x['exit_code']==0 for x in cpu['steps']) and cpu['candidate_sha256']==archives['cosmobreeder-multi.jar'],cpu.get('steps'))
 drift=[]
 for p,h in cpu.get('test_source_sha256',{}).items():
  if sha(pin(ROOT/p.replace('\\','/')))!=h:drift.append(p)
 check('CPU test source provenance stable',not drift and cpu.get('test_sources_unchanged_after_run') is True,drift)
 log=L/'optimization/r28/integration/tests/character-names-final8/logs/radio-labels.log';txt=pin(log).decode('utf8');check('actual packed helper37aliases/classic8/Latinrole/frequency test',all(s in txt for s in ['RADIO_CANDIDATE_OK','RADIO_LABELS_OK','names=36','aliases=37','geometry=8px/48px/104px']),txt)
 for p in (L/'optimization/r28/integration/tests/character-names-final8/logs').glob('*.log'):pin(p)
else:not_verified.append('Final17 CPU not yet consumed; awaiting parent completion notice.')
report={'status':'PASS' if all(x['status']=='PASS' for x in checks) else 'FAIL','phase':'final_candidate8' if args.final else 'preflight_candidate8','archives':archives,'evidence_sha256':evidence,'changed_entries':changed,'checks':checks,'not_verified':not_verified,'limits':r2final['limits']+['Complete non-font atlas pixels checked; old font glyphs may move, but all old-codepoint ink and nonposition metrics and ASCII full records preserved.','No install/Git write/delegation/game/parent build/full CPU rerun; only review output.','Frozen engineering01 is unchanged and imported for895-span semantic-boundary/protected-byte proof.'],'raw_change_summary':rawchanges,'font_details':fontdetails,'class_details':classdetails,'pending_records':nm['pending_review'],'cpu_results':cpu}
p=R/'review/final-review.json' if args.final else OUT/'preflight.json';p.write_text(json.dumps(report,ensure_ascii=False,indent=2)+'\n',encoding='utf8')
print(json.dumps({'status':report['status'],'archives':archives,'failures':[x for x in checks if x['status']=='FAIL'],'class_details':classdetails,'raw_change_summary':rawchanges},ensure_ascii=True,indent=2))
