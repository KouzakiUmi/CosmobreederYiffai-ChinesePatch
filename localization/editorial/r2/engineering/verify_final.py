"""Final archive-only independent verification, no production writes."""
from pathlib import Path
import sys,json,hashlib,zipfile,re,struct,io
sys.dont_write_bytecode=True
ROOT=Path(__file__).resolve().parents[4];L=ROOT/'localization';R=L/'editorial/r2';OUT=Path(__file__).parent
sys.path.insert(0,str(L/'tools'))
from codec import decrypt_file
from layout_fonts import parse_fnt
from projectlib import parse_atlas
from PIL import Image,ImageChops,ImageDraw
sha=lambda b:hashlib.sha256(b).hexdigest()
evidence={};checks=[]
def pin(p):
 b=p.read_bytes();evidence[p.relative_to(ROOT).as_posix()]=sha(b);return b
def load(p):return json.loads(pin(p))
def rows(p):return [json.loads(s) for s in pin(p).splitlines() if s.strip()]
def check(n,ok,detail=None):checks.append(dict(check=n,status='PASS' if ok else 'FAIL',details=detail))
P=R/'compiled/pass-02';B=L/'builds/r28-radio-book-candidate4';F=L/'builds/r28-editorial-repairs-candidate6'
m=load(P/'manifest.json');sem=load(P/'semantic-acceptance.json');build=load(F/'build-manifest.json');comp=load(L/'optimization/r28/editorial/component.json');ops=rows(L/'translations/editorial-r2-repairs.jsonl');pin(P/'operations.jsonl');pin(L/'optimization/r28/integration/build_candidate.py');pin(R/'tools/compile_repairs.py');pin(Path(__file__))
check('ledger compile semantic identity',sha((P/'operations.jsonl').read_bytes())==sha((L/ 'translations/editorial-r2-repairs.jsonl').read_bytes())==m['operations_sha256']==sem['operations_sha256'] and len(ops)==778)
for label,obj,key in [('compiler',m,'source_sha256'),('semantic',sem,'evidence_sha256'),('build',build,'source_sha256')]:
 drift=[]
 for p,h in obj[key].items():
  if sha(pin(ROOT/p))!=h:drift.append(p)
 check(label+' source evidence SHA',not drift,drift)
cor=rows(R/'corrections/round-01.jsonl');review=load(R/'review/corrections-01.json');ce={e['edit_id']:e for e in rows(P/'canonical-edits.jsonl')};approved={e['edit_id']:e for e in review['edits']}
check('six full-new corrections reviewed and compiled',len(cor)==6 and all(approved[c['edit_id']]['verdict']=='pass' and approved[c['edit_id']]['new_proposed']==c['new_proposed']==ce[c['edit_id']]['new'] and ce[c['edit_id']]['pre_correction_new']==c['old_proposed'] for c in cor))
check('339 semantic closure',sem['findings_checked']==339 and sem['original_pass']==333 and len(sem['revision_findings_resolved'])==6 and m['decision_count']==339 and m['canonical_edits']==536)
source=(L/'optimization/r28/integration/build_candidate.py').read_text('utf8')
check('builder all-component gate apply position source/evidence checks',"set(selected)!=set(COMPONENTS)" in source and source.index("if 'sfw' in selected:")<source.index('repaired,editorial_reports=')<source.index('font_assets=optimized_fonts.build_assets') and "semantic['evidence_sha256']" in source and "editorial_manifest['source_sha256']" in source)
check('component exact official bindings',comp['ledger']=='localization/translations/editorial-r2-repairs.jsonl' and comp['review_manifest']=='localization/editorial/r2/compiled/pass-02/manifest.json' and comp['semantic_manifest']=='localization/editorial/r2/compiled/pass-02/semantic-acceptance.json')
targets={(o['archive'],o['archive_entry']) for o in ops};changed={};archives={};classdetails=[];fontdetails=[];pixel_details=[]
approved_font_pins={}
for parent in [B,F]:
 fmanifest=load(parent/'font-manifest.json')
 for name,role in fmanifest['roles'].items():
  for value in [role['sha256'],role['original_sha256']]:approved_font_pins[value.encode()]=('<FONT_SHA:'+name+'>').encode()
# Normalize only approved constant-pool UTF8 changes; preserve entire remainder including method bytecode.
def normalize_class(b):
 n=int.from_bytes(b[8:10],'big');i=10;idx=1;out=[]
 while idx<n:
  tag=b[i];i+=1
  if tag==1:
   size=int.from_bytes(b[i:i+2],'big');i+=2;v=b[i:i+size];i+=size
   if v in approved_font_pins:v=approved_font_pins[v]
   v=v.replace('汤姆猫'.encode(),b'Tomcat');out.append((tag,v))
  else:
   size={3:4,4:4,5:8,6:8,7:2,8:2,9:4,10:4,11:4,12:4,15:3,16:2,18:4,19:2,20:2}[tag];out.append((tag,b[i:i+size]));i+=size
   if tag in (5,6):idx+=1
  idx+=1
 return out,b[i:]
for a in ['cosmobreeder-multi.jar','patch.pak']:
 archives[a]=sha(pin(F/a));check(a+' final manifest SHA',archives[a]==build['archives'][a]['sha256'])
 with zipfile.ZipFile(B/a) as z,zipfile.ZipFile(F/a) as q:
  before=set(z.namelist());after=set(q.namelist());check(a+' entry inventory',before==after,{'added':sorted(after-before),'removed':sorted(before-after)})
  changed[a]=[n for n in sorted(before&after) if z.read(n)!=q.read(n)]
  text_errors=[];remaining=[];text_count=0
  for n in sorted(before):
   if re.fullmatch(r'(datadf|datadm|vsn|datav|datay)/[1-9][0-9]*',n):
    old=decrypt_file(z.read(n));new=decrypt_file(q.read(n));text_count+=1
    expected=(P/'entries'/a/n).read_bytes() if (a,n) in targets else old
    if expected!=new:text_errors.append(n)
    if '汤姆猫'.encode() in new:remaining.append(n)
  check(a+' all plaintext reviewed target and non-target equality',not text_errors,{'resources':text_count,'mismatches':text_errors})
  check(a+' localized readable text has no unapproved name',not remaining,remaining)
  for n in changed[a]:
   if n.endswith('.class'):
    allowed=n in ['PRG/RadioLabels.class','PRG/DialogueWrap.class','PRG/EndingReportLayout.class','PRG/StoryFont12.class','PRG/SubtitleLayout.class'];equal=normalize_class(z.read(n))==normalize_class(q.read(n))
    if n=='PRG/RadioLabels.class':
     rp=Path('staging-src/localization/layout/src/PRG/RadioLabels.java');oldsource=pin(B/rp).decode('utf8');newsource=pin(F/rp).decode('utf8');expected=oldsource.replace(' || text.contains("汤姆猫")','').replace('return "汤姆猫"','return "Tomcat"');equal=expected==newsource and q.read(n)==pin(F/'classes'/n);check('RadioLabels exact display-name source-only changes',equal)
    classdetails.append({'entry':n,'approved_constants_only':equal});check(n+(' exact source transformation and packaged compiled class identity' if n=='PRG/RadioLabels.class' else ' method bytes unchanged except known font SHA constants'),allowed and equal)
  route=json.loads(decrypt_file(z.read('dataq/0')));atlas=decrypt_file(z.read('dataq/'+str(route['/sprites.atlas']))).decode();_,regions=parse_atlas(atlas);page='dataq/'+str(route['/sprites.png']);oldimg=Image.open(io.BytesIO(decrypt_file(z.read(page)))).convert('RGBA');newimg=Image.open(io.BytesIO(decrypt_file(q.read(page)))).convert('RGBA');mask=Image.new('L',oldimg.size,0);draw=ImageDraw.Draw(mask)
  fm=load(F/'font-manifest.json')
  for r in fm['added_rectangles']:
   region=next(v for v in regions if v['name']==r['region']);x,y=region['xy'];x1,y1,x2,y2=r['box'];draw.rectangle((x+x1,y+y1,x+x2-1,y+y2-1),fill=255)
  fixed=newimg.copy();fixed.paste(oldimg,(0,0),mask);check(a+' non-producer font-region and artwork pixels preserved',fixed.tobytes()==oldimg.tobytes())
  for role,fn,reg in [('default','bbc2.fnt','bbc2'),('classic','classic.fnt','classic'),('story12','story12.fnt','bbc2')]:
   f1=parse_fnt(z.read(fn).decode());f2=parse_fnt(q.read(fn).decode());r=next(v for v in regions if v['name']==reg);x,y=r['xy'];metric=[];reloc=[];pixels=[]
   for cp,g in f1.glyphs.items():
    h=f2.glyphs.get(cp)
    if h is None:metric.append(cp);continue
    if any(g[k]!=h[k] for k in g if k not in ['x','y']):metric.append(cp)
    if (g['x'],g['y'])!=(h['x'],h['y']):reloc.append(cp)
    box=lambda v:(x+v['x'],y+v['y'],x+v['x']+v['width'],y+v['y']+v['height'])
    if oldimg.crop(box(g)).tobytes()!=newimg.crop(box(h)).tobytes():pixels.append(cp)
   fontdetails.append({'archive':a,'role':role,'changed_metrics':metric,'relocated':reloc,'changed_glyph_ink':pixels})
   check(a+' '+role+' all old glyph metrics ink ASCII metrics',not metric and not pixels and all(f2.glyphs.get(cp)==g for cp,g in f1.glyphs.items() if cp<128),fontdetails[-1])
  allowed_extra={'dataq/6','bbc2.fnt','classic.fnt','story12.fnt'}
  unexpected=[n for n in changed[a] if (a,n) not in targets and not re.fullmatch(r'(datadf|datadm|vsn|datav|datay)/[1-9][0-9]*',n) and n not in allowed_extra and not n.startswith('r28-font/') and not n.endswith('.class')]
  check(a+' changed entry allowlist',not unexpected,unexpected)
# CPU results consumed only after parent completion notice.
testpath=L/'optimization/r28/integration/tests/editorial-final6/results.json'
if testpath.exists():
 tests=load(testpath);check('CPU completed results',tests.get('status')=='passed_cpu_only_not_real_clip_CRT_input' and len(tests.get('steps',[]))==17 and all(s['exit_code']==0 for s in tests['steps']) and tests['candidate_sha256']==archives['cosmobreeder-multi.jar'],tests)
 drift=[]
 for p,h in tests.get('test_source_sha256',{}).items():
  if sha(pin(ROOT/p.replace('\\','/')))!=h:drift.append(p)
 check('CPU test source provenance',not drift and tests.get('test_sources_unchanged_after_run') is True,drift)
else:check('CPU completed results',False,'Await parent completion and exact results filename')
parent_acceptance=load(B/'acceptance.json')
not_verified=sorted(set(sem['not_verified']+parent_acceptance['not_verified']+['No GPU/game real-run validation; no install or save traversal.']))
report={'status':'PASS' if all(c['status']=='PASS' for c in checks) else 'FAIL','archives':archives,'evidence_sha256':evidence,'not_verified':not_verified,'changed_entries':changed,'checks':checks,'limits':['Codec reused; no cryptographic implementation audit.','Font glyph coordinates may change within producer-owned appended bands; old glyph ink and non-position metrics checked independently.'],'font_details':fontdetails,'class_details':classdetails}
(OUT/'final-review.json').write_text(json.dumps(report,ensure_ascii=False,indent=2)+'\n',encoding='utf8')
(OUT/'final-review.md').write_text('# 最终工程独立核验\n\n状态：**'+report['status']+'**\n\n'+ '\n'.join('- '+c['check']+'：'+c['status'] for c in checks)+'\n\n## 限制与未验证\n'+ '\n'.join('- '+s for s in report['limits']+not_verified)+'\n',encoding='utf8')
print(json.dumps({'status':report['status'],'failures':[c for c in checks if c['status']=='FAIL'],'font_details':fontdetails,'class_details':classdetails},ensure_ascii=False,indent=2))
