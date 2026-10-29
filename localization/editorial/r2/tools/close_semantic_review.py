"""Close all 339 scoped decisions and six independent returns; not global approval."""
from pathlib import Path
from hashlib import sha256
import json,argparse

ROOT=Path(__file__).resolve().parents[4];R2=ROOT/'localization/editorial/r2'
def load(p):return json.loads(p.read_text('utf8'))
def records(p):return [json.loads(s) for s in p.read_text('utf8').splitlines() if s.strip()]
def sha(p):return sha256(p.read_bytes()).hexdigest()

def main():
    p=argparse.ArgumentParser(description=__doc__);p.add_argument('--compiled',type=Path,required=True)
    p.add_argument('--promote',action='store_true');a=p.parse_args();compiled=a.compiled.resolve()
    if not compiled.is_relative_to(R2/'compiled'):raise ValueError('Compiled scope')
    out=compiled/'semantic-acceptance.json'
    if out.exists():raise ValueError('New closure only')
    manifest=load(compiled/'manifest.json');decisions=records(compiled/'decisions.jsonl');edits=records(compiled/'canonical-edits.jsonl')
    if manifest['status']!='validated_full_repair_candidate' or len(decisions)!=339:raise ValueError('Complete validated repair required')
    checks=[];evidence={};checked_edits=set()
    def pin(name,value):
        path=(ROOT/name.replace('\\','/')).resolve()
        if not path.is_relative_to(ROOT) or sha(path)!=value:raise ValueError('Review input drift '+name)
        evidence[path.relative_to(ROOT).as_posix()]=value
    for pair in ('01-02','03-04','05-06','07-08','09-10'):
        path=R2/'review'/('pair-'+pair+'.json');review=load(path)
        for name,value in review['input_sha256'].items():pin(name,value)
        evidence[path.relative_to(ROOT).as_posix()]=sha(path)
        for c in review['checks']:
            if c['verdict'] not in ('pass','revise','hold'):raise ValueError('Unknown verdict')
            checked_edits.update(c['edit_ids_checked']);checks.append(c)
    if len(checks)!=339 or len({c['finding_id'] for c in checks})!=339:raise ValueError('Independent decision coverage')
    if {c['finding_id'] for c in checks}!={d['finding_id'] for d in decisions}:raise ValueError('Decision set drift')
    if checked_edits!={e['edit_id'] for e in edits}:raise ValueError('Actual node review coverage')
    if any(c['verdict']=='hold' for c in checks):raise ValueError('Unresolved blocking hold')
    correction_path=R2/'corrections/round-01.jsonl';corrections=records(correction_path)
    review_path=R2/'review/corrections-01.json';cr=load(review_path)
    for item in cr['inputs']:pin(item['path'],item['sha256'])
    evidence[review_path.relative_to(ROOT).as_posix()]=sha(review_path)
    evidence[correction_path.relative_to(ROOT).as_posix()]=sha(correction_path)
    corrected={c['edit_id']:c for c in corrections};verified={c['edit_id']:c for c in cr['edits']}
    if set(corrected)!=set(verified) or set(corrected)!=set(manifest['independent_corrections_applied']):
        raise ValueError('Correction node coverage')
    if {c['finding_id'] for c in checks if c['verdict']=='revise'}!={c['finding_id'] for c in corrections}:
        raise ValueError('Unclosed revision finding')
    edit_map={e['edit_id']:e for e in edits}
    for eid,c in corrected.items():
        if verified[eid]['verdict']!='pass' or verified[eid]['new_proposed']!=c['new_proposed'] or edit_map[eid]['new']!=c['new_proposed']:
            raise ValueError('Correction final text drift '+eid)
    if sha(compiled/'operations.jsonl')!=manifest['operations_sha256']:raise ValueError('Operation ledger drift')
    official=ROOT/'localization/translations/editorial-r2-repairs.jsonl'
    if a.promote:
        if official.exists():raise ValueError('Do not overwrite prior official repair ledger')
        official.write_bytes((compiled/'operations.jsonl').read_bytes())
        if sha(official)!=manifest['operations_sha256']:raise ValueError('Promotion byte identity')
    value={'status':'passed_scoped_repair_semantic_review_not_global_proofread','findings_checked':339,
           'canonical_nodes_checked':len(edits),'original_pass':sum(c['verdict']=='pass' for c in checks),
           'revision_findings_resolved':sorted(c['finding_id'] for c in corrections),
           'resolved_revision_edits':sorted(corrected),'decision_actions':manifest['decision_actions'],
           'safe_partial_findings':manifest['safe_partial_findings'],'operations_sha256':manifest['operations_sha256'],
           'evidence_sha256':evidence,'official_repair_ledger':official.relative_to(ROOT).as_posix() if a.promote else None,
           'full_game_proofread':False,'game_started':False,'installed':False,
           'not_verified':['Systematic next-round whole-game stylistic proofreading','45 explicitly deferred records',
                           'Real GPU/CRT/full clip/input/IME/equipment/save traversal; CPU geometry is separate',
                           'SFW S-S fragment is retained, not reconstructed']}
    out.write_text(json.dumps(value,ensure_ascii=False,indent=2)+'\n',encoding='utf8')
    print(json.dumps({k:value[k] for k in ('status','findings_checked','canonical_nodes_checked','original_pass','revision_findings_resolved','decision_actions','official_repair_ledger')},ensure_ascii=False,indent=2))

if __name__=='__main__':main()
