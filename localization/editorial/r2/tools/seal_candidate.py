"""Seal source-locked repair candidate after actual CPU and independent checks."""
from pathlib import Path
from hashlib import sha256
import argparse,json,sys,zipfile
ROOT=Path(__file__).resolve().parents[4];R2=ROOT/'localization/editorial/r2'
sys.path.insert(0,str(ROOT/'localization/tools'))
from codec import decrypt_file

def digest(p):return sha256(p.read_bytes()).hexdigest()
def load(p):return json.loads(p.read_text('utf8'))
def require(value,message):
    if not value:raise ValueError(message)

def main():
    p=argparse.ArgumentParser(description=__doc__);p.add_argument('--candidate',type=Path,required=True)
    p.add_argument('--tests',type=Path,required=True);p.add_argument('--review',type=Path,required=True)
    a=p.parse_args();candidate=a.candidate.resolve();tests=a.tests.resolve();reviewpath=a.review.resolve()
    require(candidate.is_relative_to(ROOT/'localization/builds'),'Candidate scope')
    output=candidate/'acceptance.json';require(not output.exists(),'New acceptance only')
    base=ROOT/'localization/builds/r28-radio-book-candidate4';parent=load(base/'acceptance.json')
    build=load(candidate/'build-manifest.json');result=load(tests/'results.json');review=load(reviewpath)
    compiled=R2/'compiled/pass-02';repair=load(compiled/'manifest.json');semantic=load(compiled/'semantic-acceptance.json')
    names=('cosmobreeder-multi.jar','patch.pak');actual={n:digest(candidate/n) for n in names}
    require(parent['archives']=={n:digest(base/n) for n in names},'Frozen accepted parent drift')
    require(parent['build_manifest_sha256']==digest(base/'build-manifest.json'),'Parent build drift')
    for item in parent['evidence']:
        path=(ROOT/item['path']).resolve();require(path.is_relative_to(ROOT) and digest(path)==item['sha256'],'Parent evidence drift')
    require(build['full_component_set'] and build['status']=='integrated_candidate_not_real_clip_CRT_input_acceptance','Integrated full candidate')
    require(all(build['archives'][n]['sha256']==actual[n] for n in names),'Build archive pins')
    require(result['status']=='passed_cpu_only_not_real_clip_CRT_input' and result['candidate_sha256']==actual[names[0]],'Actual JVM test identity')
    require(len(result['steps'])==17 and all(s['exit_code']==0 for s in result['steps']),'All actual CPU steps')
    require(result['test_sources_unchanged_after_run'],'Test source stability')
    require(review['status']=='PASS' and review['archives']==actual,'Independent final archive identity')
    require(repair['full_339_coverage'] and repair['status']=='validated_full_repair_candidate','Complete source-locked repair')
    require(semantic['status']=='passed_scoped_repair_semantic_review_not_global_proofread' and semantic['findings_checked']==339,'Independent all-finding closure')
    require(semantic['operations_sha256']==repair['operations_sha256']==digest(ROOT/'localization/translations/editorial-r2-repairs.jsonl'),'Exact approved repair data')
    for pins in (build['source_sha256'],result['test_source_sha256'],semantic['evidence_sha256'],review['evidence_sha256']):
        for name,pin in pins.items():
            path=(ROOT/name.replace('\\','/')).resolve()
            require(path.is_relative_to(ROOT) and digest(path)==pin,'Evidence/source drift '+name)
    # Bind both content editions' actual extracted UI and VSN test inputs, not just JAR.
    extracted=0
    for archive,variant in zip(names,('sfw','nsfw')):
        with zipfile.ZipFile(candidate/archive) as z:
            require((tests/('dictionary-'+variant+'.json')).read_bytes()==decrypt_file(z.read('datav/1')),'Actual dictionary test input')
            index=json.loads(decrypt_file(z.read('vsn/0')))
            for logical,entry in index.items():
                if logical.endswith('/script.vsn'):
                    scene=logical.strip('/').split('/')[-2]
                    require((tests/'vsn'/(variant+'-'+scene+'.txt')).read_bytes()==decrypt_file(z.read('vsn/'+str(entry))),'Actual VSN test input')
                    extracted+=1
    evidence=[tests/'results.json',reviewpath,base/'acceptance.json',compiled/'manifest.json',compiled/'semantic-acceptance.json',
              ROOT/'localization/translations/editorial-r2-repairs.jsonl',R2/'engineering/review.json']
    value={'schema':1,'status':'passed_cpu_and_independent_review_not_real_clip_CRT_input','archives':actual,
           'build_manifest_sha256':digest(candidate/'build-manifest.json'),
           'evidence':[{'path':f.relative_to(ROOT).as_posix(),'sha256':digest(f)} for f in evidence],
           'actual_candidate_jvm_steps':result['steps'],'changed_entries':review['changed_entries'],
           'repair_decisions':repair['decision_actions'],'source_locked_operations':repair['expanded_operations'],
           'independent_findings_checked':339,'six_revision_nodes_closed':semantic['resolved_revision_edits'],
           'actual_both_edition_vsn_inputs_checked':extracted,
           'parent_evidence_inherited_only_for_identical_content':True,
           'game_started':False,'installed':False,'user_save_accessed':False,
           'not_verified':list(dict.fromkeys(parent['not_verified']+review['not_verified']+semantic['not_verified']))}
    require(actual=={n:digest(candidate/n) for n in names},'Final archive stability')
    output.write_text(json.dumps(value,ensure_ascii=False,indent=2)+'\n',encoding='utf8')
    print(json.dumps({k:value[k] for k in ('status','archives','repair_decisions','source_locked_operations','actual_both_edition_vsn_inputs_checked')},ensure_ascii=False,indent=2))
if __name__=='__main__':main()
