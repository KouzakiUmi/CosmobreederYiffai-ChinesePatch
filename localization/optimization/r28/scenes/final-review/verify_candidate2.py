"""Read-only candidate2 class identity bridge to candidate1 ASM method audit."""
from pathlib import Path
from collections import Counter
import hashlib,json,zipfile
ROOT=Path(__file__).resolve().parents[5]
HERE=Path(__file__).resolve().parent
old=ROOT/'localization/builds/r28-full-opt-candidate1'
new=ROOT/'localization/builds/r28-full-opt-candidate2'
out=HERE/'candidate2-class-equivalence.json'
if out.exists():raise SystemExit('New evidence only')
sha=lambda b:hashlib.sha256(b).hexdigest()
audit=json.loads((HERE.parent/'final-method-review.json').read_text('utf8'))
if sha((old/'cosmobreeder-multi.jar').read_bytes())!=audit['candidate_jar_sha256']:raise SystemExit('Reviewed candidate1 changed')
records=[];ok=True
for name in ['cosmobreeder-multi.jar','patch.pak']:
 a=old/name;b=new/name
 a_before=sha(a.read_bytes());b_before=sha(b.read_bytes())
 with zipfile.ZipFile(a) as za,zipfile.ZipFile(b) as zb:
  ai=[i.filename for i in za.infolist() if i.filename.endswith('.class')]
  bi=[i.filename for i in zb.infolist() if i.filename.endswith('.class')]
  aset=set(ai);bset=set(bi)
  duplicate_a=[k for k,n in Counter(ai).items() if n!=1]
  duplicate_b=[k for k,n in Counter(bi).items() if n!=1]
  checks=[];different=[]
  for key in sorted(aset&bset):
   left=za.read(key);right=zb.read(key);eq=left==right
   checks.append({'entry':key,'bytes':len(right),'candidate1_sha256':sha(left),'candidate2_sha256':sha(right),'bytes_identical':eq})
   if not eq:different.append(key)
  equal=aset==bset and not duplicate_a and not duplicate_b and not different
  record={'archive':name,'candidate1_path':a.relative_to(ROOT).as_posix(),'candidate2_path':b.relative_to(ROOT).as_posix(),'candidate1_sha256':a_before,'candidate2_sha256':b_before,'candidate1_class_count':len(ai),'candidate2_class_count':len(bi),'entry_sets_identical':aset==bset,'candidate1_duplicate_class_entries':duplicate_a,'candidate2_duplicate_class_entries':duplicate_b,'only_candidate1':sorted(aset-bset),'only_candidate2':sorted(bset-aset),'different_class_entries':different,'all_class_bytes_identical':equal,'classes':checks}
  records.append(record);ok&=equal
 if sha(a.read_bytes())!=a_before or sha(b.read_bytes())!=b_before:raise SystemExit('Archive changed during read-only verification')
report={'status':'PASS_ALL_CLASS_ENTRIES_IDENTICAL' if ok else 'FAIL','candidate1_method_review':'localization/optimization/r28/scenes/final-method-review.json','candidate1_method_review_sha256_at_binding':sha((HERE.parent/'final-method-review.json').read_bytes()),'candidate1_method_review_status':audit['status'],'inference':'Candidate2 contains exactly the reviewed candidate1 class-entry sets and bytes; the 13-class/845-method static whitelist result transfers without reapplying or executing game code. No assertion about resource semantics from class identity alone.','candidate_modified':False,'patcher_apply_invoked':False,'game_started':False,'archives':records}
out.write_text(json.dumps(report,ensure_ascii=False,indent=2)+'\n',encoding='utf8')
for r in records:print(r['archive'],r['candidate2_class_count'],'classes; equal=',r['all_class_bytes_identical'],'SHA256=',r['candidate2_sha256'])
if not ok:raise SystemExit('Candidate2 class identity failed')
print(report['status'])
