"""New isolated CPU outputs only. No game entry, installation, deployment or save API."""
from pathlib import Path
import hashlib,json,os,subprocess,sys,zipfile
ROOT=Path(__file__).resolve().parents[4]
HERE=Path(__file__).resolve().parent
JDK=ROOT/'localization/toolchains/microsoft-jdk17/jdk-17.0.20.1+1/bin'
JRE=ROOT/'research/testgame_cjk_verified/jre/bin/java.exe'
JAR=ROOT/'localization/builds/r27-story12-shaderfix-test5/cosmobreeder-multi.jar'
EXPORTS=['--add-exports','java.base/jdk.internal.org.objectweb.asm=ALL-UNNAMED','--add-exports','java.base/jdk.internal.org.objectweb.asm.tree=ALL-UNNAMED']
if len(sys.argv)!=2:raise SystemExit('run_tests.py NEW-output-directory-name')
name=sys.argv[1]
if not name.isascii() or not name.replace('-','').isalnum():raise SystemExit('Simple new output name only')
OUT=HERE/name
OUT.mkdir()
for p in ['runtime','tools','tests']:(OUT/p).mkdir()
steps=[]
def run(label,args):
    p=subprocess.run([str(x) for x in args],cwd=ROOT,stdout=subprocess.PIPE,stderr=subprocess.STDOUT)
    (OUT/(label+'.log')).write_bytes(p.stdout)
    steps.append({'label':label,'exit_code':p.returncode,'command':[str(x) for x in args]})
    (OUT/'results.json').write_text(json.dumps({'steps':steps},ensure_ascii=False,indent=2),encoding='utf8')
    print(label,p.returncode,flush=True)
    if p.returncode:raise SystemExit('Read '+str(OUT/(label+'.log')))
cp=lambda *p:os.pathsep.join(map(str,p))
SRC=ROOT/'localization/layout/src/PRG'
TOOLS=ROOT/'localization/layout/tools/java'
TESTS=ROOT/'localization/layout/tests'
run('compile-runtime',[JDK/'javac.exe','-J-Duser.language=en','--release','8','-encoding','UTF-8','-cp',JAR,'-d',OUT/'runtime',SRC/'SceneText.java',SRC/'EndingReportLayout.java'])
run('compile-tools',[JDK/'javac.exe','-J-Duser.language=en',*EXPORTS,'-encoding','UTF-8','-d',OUT/'tools',TOOLS/'SceneTextPatch.java'])
run('patch',[JDK/'java.exe',*EXPORTS,'-cp',OUT/'tools','SceneTextPatch',JAR,OUT/'targets.jar'])
run('compile-tests',[JDK/'javac.exe','-J-Duser.language=en',*EXPORTS,'-encoding','UTF-8','-cp',cp(OUT/'runtime',OUT/'tools',JAR),'-d',OUT/'tests',TESTS/'EndingReportLayoutTest.java',TESTS/'SceneTextTest.java'])
AUDIT=ROOT/'docs/font-layout-audit-20261025/regressions'
vm=[JRE,'-Dfile.encoding=UTF-8','-Dscenes.report='+str(OUT/'breeding-corpus.json'),'-Xverify:all',*EXPORTS,'-cp',cp(OUT/'tests',OUT/'runtime',OUT/'targets.jar',OUT/'tools',JAR)]
for variant,dictionary in [('sfw','dictionary.json'),('nsfw','dictionary-nsfw.json')]:
    run('ending-'+variant,[*vm,'EndingReportLayoutTest',AUDIT/'fonts/classic.fnt',AUDIT/dictionary])
run('scenes',[*vm,'SceneTextTest',JAR,AUDIT/'fonts',AUDIT/'dictionary.json',AUDIT/'dictionary-nsfw.json'])
files=[SRC/'SceneText.java',SRC/'EndingReportLayout.java',TOOLS/'SceneTextPatch.java',TESTS/'SceneTextTest.java',TESTS/'EndingReportLayoutTest.java']
manifest={'status':'CPU_ONLY_NOT_GAME_SCREENSHOT','input_jar_sha256':hashlib.sha256(JAR.read_bytes()).hexdigest(),'source_sha256':{p.relative_to(ROOT).as_posix():hashlib.sha256(p.read_bytes()).hexdigest() for p in files},'steps':steps,'game_started':False,'gl_started':False,'save_accessed':False}
(OUT/'results.json').write_text(json.dumps(manifest,ensure_ascii=False,indent=2),encoding='utf8')
print('CPU-only completed:',OUT)
