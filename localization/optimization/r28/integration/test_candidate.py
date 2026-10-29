"""Fresh-JVM CPU validation of an actual candidate, not worker overlay classpaths.
Writes only a NEW test directory, does not call game/installer/GL/save entry points.
"""
from pathlib import Path
import argparse,base64,hashlib,json,os,re,subprocess,sys,zipfile
ROOT=Path(__file__).resolve().parents[4];HERE=Path(__file__).resolve().parent
sys.path.insert(0,str(ROOT/'localization/tools'))
from codec import decrypt_file
JDK=ROOT/'localization/toolchains/microsoft-jdk17/jdk-17.0.20.1+1/bin';JRE=ROOT/'research/testgame_cjk_verified/jre/bin/java.exe'
EXPORTS=['--add-exports','java.base/jdk.internal.org.objectweb.asm=ALL-UNNAMED','--add-exports','java.base/jdk.internal.org.objectweb.asm.tree=ALL-UNNAMED']
TEST_NAMES=['PixelLayoutTest','DialogueGridTest','DialogueWrapTest','ContinueWrapTest','SubtitleLayoutTest','PatternSymbolsTest']

def main():
 p=argparse.ArgumentParser(description=__doc__);p.add_argument('--candidate',type=Path,required=True);p.add_argument('--output',type=Path,required=True);p.add_argument('--diagnostic-continue',action='store_true');a=p.parse_args()
 candidate=a.candidate.resolve();out=a.output.resolve()
 if out.exists() or not out.is_relative_to(HERE):raise ValueError('NEW integration-local test output only')
 if not (candidate/'build-manifest.json').is_file():raise ValueError('Candidate build manifest required')
 out.mkdir(parents=True)
 for name in ['classes','tools','fonts','vsn','logs']:(out/name).mkdir()
 jar=candidate/'cosmobreeder-multi.jar';base=ROOT/'localization/builds/r27-story12-shaderfix-test5/cosmobreeder-multi.jar'
 result={'status':'running_cpu_only','candidate_sha256':hashlib.sha256(jar.read_bytes()).hexdigest(),'steps':[],'game_started':False,'user_save_accessed':False}
 def save():(out/'results.json').write_text(json.dumps(result,ensure_ascii=False,indent=2),encoding='utf8')
 def run(name,args):
  r=subprocess.run([str(x) for x in args],cwd=ROOT,stdout=subprocess.PIPE,stderr=subprocess.STDOUT);(out/'logs'/(name+'.log')).write_bytes(r.stdout)
  result['steps'].append({'name':name,'exit_code':r.returncode});save();print(name,'exit',r.returncode,flush=True)
  if r.returncode:
   result['status']='failed_cpu_only';save()
   if not a.diagnostic_continue or name in ('compile-tests','compact-inputs','compact-compile'):
    raise RuntimeError('Inspect '+str(out/'logs'/(name+'.log')))
 with zipfile.ZipFile(jar) as z:
  extended={'PRG/CompactFields.class','PRG/SceneText.class'}<=set(z.namelist())
  for name in ['bbc2.fnt','classic.fnt','story12.fnt','dingbats.fnt']:(out/'fonts'/name).write_bytes(z.read(name))
  (out/'fonts/bbc2-10px.fnt').write_bytes(z.read('bbc2.fnt'))
 vsn=[];census={'commands':0,'han_commands':0,'han':0}
 for archive,variant in [('cosmobreeder-multi.jar','sfw'),('patch.pak','nsfw')]:
  with zipfile.ZipFile(candidate/archive) as z:
   (out/('dictionary-'+variant+'.json')).write_bytes(decrypt_file(z.read('datav/1')))
   index=json.loads(decrypt_file(z.read('vsn/0')))
   for logical,value in sorted(index.items()):
    if not logical.endswith('/script.vsn'):continue
    scene=logical.strip('/').split('/')[-2];raw=decrypt_file(z.read('vsn/'+str(value)));path=out/'vsn'/(variant+'-'+scene+'.txt');path.write_bytes(raw);vsn.append(variant+'\t'+scene+'\t'+str(path))
    for line in raw.decode('utf8').splitlines():
     m=re.match(r'^lang\((Fox|HardFox)\):\s?(.*)$',line)
     if m:
      census['commands']+=1;count=sum(0x3400<=ord(c)<=0x9fff for c in m[2]);census['han']+=count;census['han_commands']+=bool(count)
 (out/'vsn.tsv').write_text('\n'.join(vsn)+'\n',encoding='utf8')
 (out/'pattern-census.properties').write_text(''.join(k+'='+str(v)+'\n' for k,v in census.items()),encoding='utf8')
 result['independent_pattern_census']=census;result['actual_archive_script_inputs']=len(vsn);save()
 sys.path.insert(0,str(ROOT/'localization/optimization/r28/core'))
 from pattern_ink import export
 result['pattern_ink']=export(jar,base,out);save()
 sources=[ROOT/'localization/layout/tests'/(name+'.java') for name in TEST_NAMES]+[ROOT/'localization/optimization/r28/core/CoreRegression.java']
 if extended:
  sources.extend(ROOT/'localization/layout/tests'/(name+'.java') for name in ['SceneTextTest','EndingReportLayoutTest','StoryFont12Test'])
  sources.append(ROOT/'localization/layout/tools/java/BridgePatch.java')
 with zipfile.ZipFile(jar) as z:radio='PRG/RadioLabels.class' in z.namelist()
 if radio:sources.append(ROOT/'localization/layout/tests/RadioLabelsTest.java')
 snapshot_sources=list(sources)
 if extended:
  snapshot_sources.extend([ROOT/'docs/font-layout-audit-20261025/simulation/CpuEvidence.java',ROOT/'localization/layout/tests/CompactFieldsCpuTest.java',ROOT/'localization/optimization/r28/compact/prepare_inputs.py',ROOT/'localization/optimization/r28/compact/render_compact.py'])
 result['test_source_sha256']={str(p.relative_to(ROOT)):hashlib.sha256(p.read_bytes()).hexdigest() for p in snapshot_sources};save()
 cp=os.pathsep.join(map(str,[jar,candidate/'tools']))
 run('compile-tests',[JDK/'javac.exe',*EXPORTS,'-encoding','UTF-8','-cp',cp,'-d',out/'classes',*sources])
 vm=[JRE,'-Dfile.encoding=UTF-8','-Xverify:all',*EXPORTS,'-cp',os.pathsep.join(map(str,[jar,out/'classes',candidate/'tools']))]
 if radio:run('radio-labels', [*vm,'RadioLabelsTest',base,jar,out/'fonts/classic.fnt'])
 run('core-regression',[*vm,'CoreRegression',base])
 run('pixel-layout',[*vm,'PixelLayoutTest'])
 run('dialogue-grid',[*vm,'DialogueGridTest'])
 run('dialogue-wrap',[*vm,'DialogueWrapTest',out/'fonts/bbc2.fnt',ROOT/'docs/font-layout-audit-20261025/regressions/joined.tsv'])
 run('continue',[*vm,'ContinueWrapTest',out/'fonts/bbc2.fnt'])
 run('subtitle',[*vm,'SubtitleLayoutTest',out/'fonts/bbc2.fnt',out/'vsn.tsv','--pattern-symbols',out/'pattern-ink.properties'])
 run('pattern',[*vm,'PatternSymbolsTest',out/'vsn.tsv',out/'fonts/dingbats.fnt',out/'fonts/story12.fnt',out/'fonts/bbc2.fnt',out/'pattern-census.properties'])
 if extended:
  run('ending-sfw',[*vm,'EndingReportLayoutTest',out/'fonts/classic.fnt',out/'dictionary-sfw.json'])
  run('ending-nsfw',[*vm,'EndingReportLayoutTest',out/'fonts/classic.fnt',out/'dictionary-nsfw.json'])
  scenevm=[JRE,'-Dfile.encoding=UTF-8','-Dscenes.report='+str(out/'breeding-corpus.json'),'-Xverify:all',*EXPORTS,'-cp',os.pathsep.join(map(str,[out/'classes',jar,candidate/'tools']))]
  run('scenes',[*scenevm,'SceneTextTest','--candidate',jar,out/'fonts',out/'dictionary-sfw.json',out/'dictionary-nsfw.json'])
  build=json.loads((candidate/'build-manifest.json').read_text('utf8'))
  from build_story_font12 import wide
  native_count=2312+sum(wide(cp) for cp in build['font_manifest']['roles']['story12']['added_ids'])
  run('story12-lifecycle',[*vm,'StoryFont12Test','--cpu',out/'fonts',str(native_count)])
  compact=out/'compact';compact.mkdir();(compact/'classes').mkdir()
  compact_root=ROOT/'localization/optimization/r28/compact'
  run('compact-inputs',[sys.executable,'-B',compact_root/'prepare_inputs.py','--pak-json',out/'dictionary-nsfw.json','--jar-json',out/'dictionary-sfw.json','--output-dir',compact])
  compact_sources=[ROOT/'docs/font-layout-audit-20261025/simulation/CpuEvidence.java',ROOT/'localization/layout/tests/CompactFieldsCpuTest.java']
  run('compact-compile',[JDK/'javac.exe','-encoding','UTF-8','-source','8','-target','8','-cp',jar,'-d',compact/'classes',*compact_sources])
  run('compact-cpu',[JRE,'-Dfile.encoding=UTF-8','-Xverify:all','-cp',os.pathsep.join(map(str,[jar,compact/'classes'])),'PRG.CompactFieldsCpuTest',jar,jar,compact])
  run('compact-pixels',[sys.executable,'-B',compact_root/'render_compact.py',jar,'--output-dir',compact])
 result['test_sources_unchanged_after_run']=all(hashlib.sha256((ROOT/n).read_bytes()).hexdigest()==h for n,h in result['test_source_sha256'].items())
 if not result['test_sources_unchanged_after_run']:raise RuntimeError('Test source changed concurrently; retain logs and rerun fresh after workers finish')
 if any(step['exit_code'] for step in result['steps']):
  result['status']='failed_cpu_only';save();raise RuntimeError('One or more candidate tests failed; inspect results.json')
 result['status']='passed_cpu_only_not_real_clip_CRT_input';save();print(json.dumps({'output':str(out.relative_to(ROOT)),'status':result['status']},ensure_ascii=False))
if __name__=='__main__':main()
