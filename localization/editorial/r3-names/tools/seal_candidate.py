"""Seal the name-only candidate, not real-game/GPU or save acceptance."""
from pathlib import Path
from hashlib import sha256
import argparse,json,sys,zipfile
ROOT=Path(__file__).resolve().parents[4];R3=ROOT/'localization/editorial/r3-names'
sys.path.insert(0,str(ROOT/'localization/tools'))
from codec import decrypt_file

def digest(p):return sha256(p.read_bytes()).hexdigest()
def load(p):return json.loads(p.read_text('utf8'))
def require(value,message):
    if not value:raise ValueError(message)

def main():
    p=argparse.ArgumentParser(description=__doc__);p.add_argument('--candidate',type=Path,required=True)
    p.add_argument('--tests',type=Path,required=True);p.add_argument('--review',type=Path,required=True);a=p.parse_args()
    candidate=a.candidate.resolve();tests=a.tests.resolve();rp=a.review.resolve();output=candidate/'acceptance.json'
    require(candidate.is_relative_to(ROOT/'localization/builds') and not output.exists(),'New local candidate only')
    base=ROOT/'localization/builds/r28-editorial-repairs-candidate6';parent=load(base/'acceptance.json')
    build=load(candidate/'build-manifest.json');result=load(tests/'results.json');review=load(rp)
    preflight=load(R3/'review/engineering-01.json');manifest=load(R3/'compiled/final-01/manifest.json')
    registry_path=ROOT/'localization/translations/character-names.json';registry=load(registry_path)
    semantic_path=ROOT/registry['semantic_review']['path'];semantic=load(semantic_path)
    ledger=ROOT/'localization/translations/character-name-repairs.jsonl'
    names=('cosmobreeder-multi.jar','patch.pak');archives={n:digest(candidate/n) for n in names}
    require(parent['archives']=={n:digest(base/n) for n in names},'Frozen parent archive drift')
    require(parent['build_manifest_sha256']==digest(base/'build-manifest.json'),'Frozen parent build drift')
    for item in parent['evidence']:
        f=(ROOT/item['path']).resolve();require(f.is_relative_to(ROOT) and digest(f)==item['sha256'],'Parent evidence drift')
    require(build['full_component_set'] and build['status']=='integrated_candidate_not_real_clip_CRT_input_acceptance','Full pipeline')
    require(all(build['archives'][n]['sha256']==archives[n] for n in names),'Build archive identity')
    require(result['status']=='passed_cpu_only_not_real_clip_CRT_input' and result['candidate_sha256']==archives[names[0]],'Actual CPU archive identity')
    require(len(result['steps'])==17 and all(s['exit_code']==0 for s in result['steps']) and result['test_sources_unchanged_after_run'],'CPU steps/source stability')
    require(review['status']=='PASS' and review['archives']==archives and preflight['status']=='PASS','Independent actual archive acceptance')
    require(registry['status']=='reviewed_for_application' and len(registry['names'])==36,'All-name reviewed registry')
    require(digest(semantic_path)==registry['semantic_review']['sha256'] and not any(n['blocking_issues'] for n in semantic['names']),'Semantic authority')
    require({n['name_id']:n['target'] for n in registry['names']}=={n['name_id']:n['target'] for n in semantic['names']},'All semantic targets')
    require(manifest['all_entry_preflight']=='passed' and manifest['operation_count']==839,'Exact name-only source compilation')
    require(digest(registry_path)==manifest['registrySHA'] and digest(ledger)==manifest['operationsSHA'],'Exact formal source bindings')
    require(manifest['r2_preservation']['non_name_preserved']==778,'All R2 non-name repairs retained')
    require(manifest['name_counts']['Tomcat']['nickname_occurrences']==3,'Only three TOM nickname occurrences')
    require(load(R3/'review/residual-audit-final.json')['count']==0,'No eligible old display-name residuals')
    for pins in (build['source_sha256'],result['test_source_sha256'],review['evidence_sha256'],preflight['evidence_sha256']):
        for name,pin in pins.items():
            f=(ROOT/name.replace('\\','/')).resolve();require(f.is_relative_to(ROOT) and digest(f)==pin,'Source/evidence drift '+name)
    extracted=0
    for archive,variant in zip(names,('sfw','nsfw')):
        with zipfile.ZipFile(candidate/archive) as z:
            require((tests/('dictionary-'+variant+'.json')).read_bytes()==decrypt_file(z.read('datav/1')),'Actual dictionary inputs')
            for logical,entry in json.loads(decrypt_file(z.read('vsn/0'))).items():
                if not logical.endswith('/script.vsn'):continue
                scene=logical.strip('/').split('/')[-2]
                require((tests/'vsn'/(variant+'-'+scene+'.txt')).read_bytes()==decrypt_file(z.read('vsn/'+str(entry))),'Actual VSN inputs')
                extracted+=1
    evidence=[rp,tests/'results.json',R3/'review/engineering-01.json',semantic_path,R3/'compiled/final-01/manifest.json',
              registry_path,ledger,R3/'review/residual-audit-final.json',base/'acceptance.json']
    value={'schema':1,'status':'passed_cpu_and_independent_review_not_real_clip_CRT_input','archives':archives,
           'build_manifest_sha256':digest(candidate/'build-manifest.json'),
           'evidence':[{'path':f.relative_to(ROOT).as_posix(),'sha256':digest(f)} for f in evidence],
           'actual_candidate_jvm_steps':result['steps'],'changed_entries':review['changed_entries'],
           'names_reviewed':36,'source_locked_name_operations':839,'r2_non_name_repairs_preserved':778,
           'actual_both_edition_vsn_inputs_checked':extracted,'nickname_occurrences':3,
           'game_started':False,'installed':False,'user_save_accessed':False,
           'not_verified':list(dict.fromkeys(parent['not_verified']+review['not_verified']+preflight['not_verified']))}
    require(archives=={n:digest(candidate/n) for n in names},'Final archive stability')
    output.write_text(json.dumps(value,ensure_ascii=False,indent=2)+'\n',encoding='utf8')
    print(json.dumps({k:value[k] for k in ('status','archives','names_reviewed','source_locked_name_operations','r2_non_name_repairs_preserved')},ensure_ascii=False,indent=2))
if __name__=='__main__':main()
