"""Seal a CPU-verified, independently reviewed candidate. Never install or run game."""
from pathlib import Path
from hashlib import sha256
import argparse,json,sys,zipfile
ROOT=Path(__file__).resolve().parents[4];OPT=ROOT/'localization/optimization/r28'
sys.path.insert(0,str(ROOT/'localization/tools'))
from codec import decrypt_file
SHA=lambda p:sha256(p.read_bytes()).hexdigest()

def main():
 p=argparse.ArgumentParser();p.add_argument('--candidate',type=Path,required=True);p.add_argument('--tests',type=Path,required=True);a=p.parse_args()
 candidate=a.candidate.resolve();testdir=a.tests.resolve()
 if not candidate.is_relative_to(ROOT/'localization/builds') or not testdir.is_relative_to(OPT/'integration/tests'):raise ValueError('Isolated candidate and tests only')
 out=candidate/'acceptance.json'
 if out.exists():raise ValueError('New acceptance record only')
 build=json.loads((candidate/'build-manifest.json').read_text('utf8'))
 if not build['full_component_set'] or build['status']!='integrated_candidate_not_real_clip_CRT_input_acceptance':raise ValueError('Not a full integrated candidate')
 archives={n:SHA(candidate/n) for n in ['cosmobreeder-multi.jar','patch.pak']}
 if any(build['archives'][n]['sha256']!=v for n,v in archives.items()):raise ValueError('Candidate archive changed')
 tests=json.loads((testdir/'results.json').read_text('utf8'))
 if tests['status']!='passed_cpu_only_not_real_clip_CRT_input' or len(tests['steps'])!=16 or any(s['exit_code'] for s in tests['steps']):raise ValueError('Full actual-candidate test suite must pass')
 if tests['candidate_sha256']!=archives['cosmobreeder-multi.jar'] or not tests['test_sources_unchanged_after_run']:raise ValueError('JVM input/source identity')
 resource_path=OPT/'core/final-review.json';resource=json.loads(resource_path.read_text('utf8'))
 if resource['status']!='PASS' or resource['archive_sha256']!=archives or any(not c.get('passed',True) for c in resource['checks']):raise ValueError('Resource review')
 font_path=OPT/'pattern/new-review/final-candidate-review.json';font=json.loads(font_path.read_text('utf8'))
 if font['status']!='PASS' or font['findings'] or {n:r['sha256'] for n,r in font['archives'].items()}!=archives:raise ValueError('Font/image review')
 methods_path=OPT/'scenes/final-method-review.json';methods=json.loads(methods_path.read_text('utf8'));binding=methods['candidate2_binding']
 if methods['status']!='PASS_STATIC_METHOD_WHITELIST' or binding['status']!='PASS_ALL_CLASS_ENTRIES_IDENTICAL' or methods['changed_methods']!=methods['whitelist_methods']:raise ValueError('Method whitelist review')
 if binding['final_jar_sha256']!=archives['cosmobreeder-multi.jar'] or binding['final_pak_sha256']!=archives['patch.pak']:raise ValueError('Method final identity')
 # Bind the dynamically consumed test fixtures to BOTH actual final archives.
 script_count=0;seen=set()
 with zipfile.ZipFile(candidate/'cosmobreeder-multi.jar') as jar,zipfile.ZipFile(candidate/'patch.pak') as pak:
  zs={'sfw':jar,'nsfw':pak};indexes={v:json.loads(decrypt_file(z.read('vsn/0'))) for v,z in zs.items()}
  for line in (testdir/'vsn.tsv').read_text('utf8').splitlines():
   variant,scene,path=line.split('\t');identity=(variant,scene)
   if identity in seen:raise ValueError('Duplicate dynamic script input')
   seen.add(identity);target=Path(path).resolve()
   if not target.is_relative_to(testdir/'vsn'):raise ValueError('Fixture path escaped')
   entry='vsn/'+str(indexes[variant]['/'+scene+'/script.vsn'])
   if target.read_bytes()!=decrypt_file(zs[variant].read(entry)):raise ValueError('Dynamic script fixture drift')
   script_count+=1
  if script_count!=106:raise ValueError('Incomplete script input set')
  for name in ['bbc2.fnt','classic.fnt','story12.fnt','dingbats.fnt']:
   if jar.read(name)!=(testdir/'fonts'/name).read_bytes():raise ValueError('JVM font input drift')
  for variant,z in zs.items():
   if decrypt_file(z.read('datav/1'))!=(testdir/('dictionary-'+variant+'.json')).read_bytes():raise ValueError('Dictionary fixture drift')
 evidence=[testdir/'results.json',resource_path,font_path,methods_path]
 value={'schema':1,'status':'passed_cpu_and_independent_review_not_real_clip_CRT_input',
  'archives':archives,'build_manifest_sha256':SHA(candidate/'build-manifest.json'),
  'evidence':[{'path':f.relative_to(ROOT).as_posix(),'sha256':SHA(f)} for f in evidence],
  'actual_candidate_jvm_steps':tests['steps'],'actual_archive_scripts':script_count,
  'fixtures_rechecked_against_both_final_archives':True,'test_sources_unchanged_after_run':True,
  'independent_resource_checks':resource['checked_items'],'independent_font_image_checks':font['checks'],
  'existing_target_methods':methods['same_methods']+methods['changed_methods'],'changed_methods_whitelisted':methods['changed_methods'],
  'game_started':False,'installed':False,'user_save_accessed':False,
  'not_verified':['full game reachability/input/IME/equipment actions','GPU/shader/CRT/filtering','full parent clip/FBO/complete scene layering','real user saves','all unknown/dynamic future text or unreviewed image assets'],
  'intentional_preservations':['four SFW corrupted-radio source fragments','brand/copyright/unconfirmed micro-symbol image frames']}
 if any(SHA(candidate/n)!=h for n,h in archives.items()):raise ValueError('Candidate changed during finalization')
 out.write_text(json.dumps(value,ensure_ascii=False,indent=2)+'\n',encoding='utf8')
 print(json.dumps({'status':value['status'],'archives':archives,'script_inputs':script_count},indent=2))
if __name__=='__main__':main()
