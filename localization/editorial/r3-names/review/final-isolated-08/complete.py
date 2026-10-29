from pathlib import Path
import json,hashlib
H=Path(__file__).resolve().parent;ROOT=H.parents[4];R=H.parent;p=R/'final-review.json'
d=json.loads(p.read_text(encoding='utf8'));assert d['status']=='PASS'
for k,h in d['evidence_sha256'].items():assert hashlib.sha256((ROOT/k).read_bytes()).hexdigest()==h,k
for pth in [H/'final.log',H/'render_report.py',H/'parent-unit-test-attestation.json',ROOT/'localization/optimization/r28/integration/test_candidate.py']:
 d['evidence_sha256'][pth.relative_to(ROOT).as_posix()]=hashlib.sha256(pth.read_bytes()).hexdigest()
d['supplementary_parent_test_attestation']=json.loads((H/'parent-unit-test-attestation.json').read_text(encoding='utf8'))
d['checks'].append({'check':'parent-reported supplementary13 compiler tests plus3 nickname/2negative assertions','status':'PASS','details':'Attested by parent completion message; not independently rerun or represented as raw local test log. Separate actual17CPU archive tests verified.'})
p.write_text(json.dumps(d,ensure_ascii=False,indent=2)+'\n',encoding='utf8')
