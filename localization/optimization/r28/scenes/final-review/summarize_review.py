"""Format independent read-only ASM audit evidence; does not touch candidate."""
from pathlib import Path
import hashlib,json,difflib
HERE=Path(__file__).resolve().parent
raw=HERE/'review-raw-01.json'
data=json.loads(raw.read_text('utf8'))
summary=[]
for cls in data['classes']:
 for method in cls['methods']:
  if method['identical']:continue
  old=method['baseline_instructions'];new=method['candidate_instructions']
  delta=[]
  for tag,a,b,c,d in difflib.SequenceMatcher(None,old,new,autojunk=False).get_opcodes():
   if tag!='equal':delta.append({'kind':tag,'baseline_range':[a,b],'candidate_range':[c,d],'baseline':old[a:b],'candidate':new[c:d]})
  method['logical_sequence_deltas']=delta
  summary.append({'class':cls['class'],'method':method['method'],'descriptor':method['descriptor'],'changes':method['changes'],'deltas':delta})
data['review_provenance']={'probe_source':'localization/optimization/r28/scenes/final-review/FinalMethodReview.java','probe_source_sha256':hashlib.sha256((HERE/'FinalMethodReview.java').read_bytes()).hexdigest(),'raw_evidence_sha256':hashlib.sha256(raw.read_bytes()).hexdigest(),'raw_evidence':'localization/optimization/r28/scenes/final-review/review-raw-01.json','patcher_apply_invoked':False,'game_class_loading':False,'candidate_modified':False}
(HERE/'changed-method-summary.json').write_text(json.dumps(summary,ensure_ascii=False,indent=2)+'\n',encoding='utf8')
(HERE.parent/'final-method-review.json').write_text(json.dumps(data,ensure_ascii=False,indent=2)+'\n',encoding='utf8')
print('candidate SHA256:',data['candidate_jar_sha256'])
print('identical methods:',data['same_methods'],'changed methods:',data['changed_methods'])
for cls in data['classes']:
 changed=[m['method']+m['descriptor'] for m in cls['methods'] if not m['identical']]
 print(cls['class'],'total=',len(cls['methods']),'changed=',changed)
print('Kc prefix/tail:',next(m['changes'] for c in data['classes'] if c['class']=='PRG/Kc' for m in c['methods'] if not m['identical'])[0]['prefix_including_source_store_identical'])
