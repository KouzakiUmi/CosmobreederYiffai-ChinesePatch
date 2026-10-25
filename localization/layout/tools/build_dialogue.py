"""Build the focused 10px story/radio test payload and installer; never starts the game."""
from pathlib import Path
import argparse
import hashlib
import importlib
import json
import os
import shutil
import subprocess
import sys
import uuid
import zipfile

ROOT=Path(__file__).resolve().parents[3];LOC=ROOT/'localization'
sys.path.insert(0,str(LOC/'tools'));sys.path.insert(0,str(LOC/'packaging'))
from build_layout import verify_inputs
from codec import decrypt_file,encrypt_file
import dialogue_joins
import dialogue_sfw
import build_layout_test_installer as installer

VERSION='r23-textflow-test1';NAME='CosmobreederYiffaiCN-'+VERSION
JDK=LOC/'toolchains/microsoft-jdk17/jdk-17.0.20.1+1/bin'
JRE=ROOT/'research/testgame_cjk_verified/jre/bin/java.exe'
EXPORTS=['--add-exports','java.base/jdk.internal.org.objectweb.asm=ALL-UNNAMED','--add-exports','java.base/jdk.internal.org.objectweb.asm.tree=ALL-UNNAMED']
BASE=LOC/'builds/final-8146-r21-images'
ACTIVATION={'save_single_card':False,'story_wrap':True,'radio_wrap':True,'vsn_prototype':False,'item_prototype':False}


def sha(path):return hashlib.sha256(path.read_bytes()).hexdigest()


def run(args,work,log,env=None):
    result=subprocess.run([str(a) for a in args],cwd=work,env=env,stdout=subprocess.PIPE,stderr=subprocess.STDOUT)
    log.write_bytes(result.stdout);print(log.stem,'exit',result.returncode,flush=True)
    if result.returncode:raise RuntimeError('Failed step; inspect '+str(log))


def runtime(work,logs):
    classes=work/'runtime';classes.mkdir();tools=work/'tools';tools.mkdir()
    source=LOC/'layout/src';tests=LOC/'layout/tests'
    files=[source/'cosmoloc/layout/PixelLayout.java',source/'cosmoloc/layout/DialogueGrid.java',source/'PRG/DialogueWrap.java',tests/'DialogueWrapTest.java',tests/'DialogueGridTest.java']
    run([JDK/'javac.exe','--release','8','-encoding','UTF-8','-Xlint:all','-cp',ROOT/'backup/cosmobreeder-multi.jar','-d',classes,*files],ROOT,logs/'compile-runtime.log')
    js=LOC/'layout/tools/java'
    run([JDK/'javac.exe',*EXPORTS,'-encoding','UTF-8','-d',tools,js/'VsnPatch.java',js/'DialoguePatch.java',js/'DialogueBuild.java',js/'VerifyLayout.java'],ROOT,logs/'compile-tools.log')
    target=work/'patched-targets.jar'
    run([JDK/'java.exe',*EXPORTS,'-cp',tools,'DialogueBuild',BASE/'cosmobreeder-multi.jar',classes,target],ROOT,logs/'patch-targets.log')
    replacements={}
    with zipfile.ZipFile(target) as z:
        if set(z.namelist())!={'PRG/JR.class','PRG/Nb.class'}:raise ValueError('Target inventory')
        replacements.update({n:z.read(n) for n in z.namelist()})
    for p in classes.rglob('*.class'):
        name=p.relative_to(classes).as_posix()
        if name.startswith(('PRG/DialogueWrap','cosmoloc/layout/')):
            data=p.read_bytes()
            if int.from_bytes(data[6:8],'big')!=52:raise ValueError('Runtime Java8 major')
            replacements[name]=data
    return classes,tools,replacements


def rewrite(source,dest,replacements):
    with zipfile.ZipFile(source) as before,zipfile.ZipFile(dest,'w',zipfile.ZIP_DEFLATED,compresslevel=6) as after:
        names=set(before.namelist())
        for info in before.infolist():after.writestr(info,replacements.get(info.filename,before.read(info.filename)))
        for name,data in sorted(replacements.items()):
            if name not in names:after.writestr(name,data)
    with zipfile.ZipFile(source) as before,zipfile.ZipFile(dest) as after:
        if after.testzip() is not None:raise ValueError('Archive CRC')
        for name in set(before.namelist())-set(replacements):
            if before.read(name)!=after.read(name):raise ValueError('Unrelated archive entry changed: '+name)


def text_resources():
    replacements={};reports=[]
    with zipfile.ZipFile(BASE/'patch.pak') as z:
        for logical,entry in [('datadf/all.ds','datadf/1'),('datadm/all.ds','datadm/1')]:
            original=(ROOT/'extract/patch'/logical).read_bytes();localized=decrypt_file(z.read(entry))
            joined,report=dialogue_joins.apply_joins(logical,original,localized)
            replacements[entry]=encrypt_file(joined,os.urandom(32),os.urandom(8));reports.append(report)
    return replacements,reports


def prepare_installer(work,jar):
    installer.VERSION=VERSION;installer.NAME=NAME
    prepared,man=installer.prepare(work,BASE,jar)
    # The original factory remains archived and unchanged; replace only generated test branding.
    man['version']=VERSION;man['activation']=ACTIVATION;man['status']='story_radio_10px_test_not_G3'
    man['name']='Cosmobreeder Yiffai 剧情与无线电换行测试版'
    man['notes']=['存档保留原布局及10px字体，不含单卡片。','剧情20/无线电15汉字等效像素预算，原打字/分页机制。','仅合并经逐组审校并通过来源门禁的续句。','先备份存档；测试版不等于已通过实机验收。']
    # Both payload files must come from this new test build, not the base PAK.
    shutil.copyfile(jar.parent/'patch.pak',prepared/'payload/patch.pak')
    pak=prepared/'payload/patch.pak';pak_sha=sha(pak)
    for variant in man['variants'].values():
        variant['label']=variant['label'].replace('r22测试版','r23正文测试版')
        for entry in variant['files']:
            if entry['path']=='patch.pak':entry.update(sha256=pak_sha,size=pak.stat().st_size)
        if variant['label']=='已安装的r22排版测试版':
            variant['label']='已安装的剧情/无线电换行测试版'
            if variant['detect']['patch.pak'].get('sha256'):variant['detect']['patch.pak']['sha256']=pak_sha
    (prepared/'manifest.json').write_text(json.dumps(man,ensure_ascii=False,indent=2)+'\n',encoding='utf8')
    for file in ('launcher.py','base_patch_tool.py'):
        p=prepared/file;text=p.read_text('utf8')
        text=text.replace('r22-test1',VERSION)
        text=text.replace('测试版：启用存档单卡片；开场/道具仍诊断。未完成实机验收，请先备份存档。','测试版：10px剧情20字／无线电15字自然换行与同句合并；存档原布局。请先备份存档。')
        text=text.replace('仅启用存档单卡片；可能异常，未通过实机验收。','启用剧情／无线电换行和译文合句；存档原布局。未通过实机验收。')
        text=text.replace('存档单卡片默认启用；开场/道具仍诊断','剧情／无线电10px换行与合句已启用；存档保留原布局')
        p.write_text(text,encoding='utf8')
    return prepared,man


README='''# 剧情／无线电10px换行测试版

重点改换行和译文续句，不再改造存档界面。存档维持原布局、10px字体；不带单卡片。

- 剧情按20个汉字等效宽度(200px)、无线电按15个汉字等效宽度(150px)保守测试；英文、数字和标点按封存10px字体的实际glyph/kerning测量。
- 保留原三行分页、打字、完成／跳过与事件机制；不再只处理开场八条字幕。
- 译文续句只按逐组审校的occurrence台账合并，不跨说话人、表情、事件或分支，不把所有相邻台词硬拼。源canonical/unit仍保留，实际本地化输出为完整句。

安装前自行备份存档并完全退出游戏。双击EXE选择SHA匹配的原版／r21；未知版本拒绝覆盖，不提供force。若装过之前的单卡片测试版，请先用那一版的“卸载／还原”退到安装前。

使用当前同一EXE可还原到安装本测试版之前，旧汉化备份和状态保留。测试备份为`_中文排版测试备份`，状态为`layout-test-install-state.json`；不要删除或交叉使用安装器。

安装器不读写存档、不自动启动游戏。运行游戏不是安全沙箱，复制目录并不证明存档隔离。真实clip、CRT、全部输入和全部动态值域尚未做窗口内验收；本EXE未签名，如安全系统拦截请核对来源和SHA，不建议关闭防护。
'''


def main():
    ap=argparse.ArgumentParser(description=__doc__);ap.add_argument('--output',type=Path,required=True);args=ap.parse_args()
    output=args.output.resolve();allowed=(LOC/'builds').resolve()
    if output.exists() or output==allowed or not output.is_relative_to(allowed):raise ValueError('New build output only')
    verify_inputs()
    pins=[Path(__file__),LOC/'layout/src/cosmoloc/layout/PixelLayout.java',LOC/'layout/src/cosmoloc/layout/DialogueGrid.java',LOC/'layout/src/PRG/DialogueWrap.java',LOC/'layout/tests/DialogueGridTest.java',LOC/'layout/tests/DialogueWrapTest.java',LOC/'layout/tools/java/DialoguePatch.java',LOC/'layout/tools/java/DialogueBuild.java',LOC/'tools/dialogue_joins.py',LOC/'tools/dialogue_sfw.py',LOC/'translations/dialogue-joins.jsonl',LOC/'packaging/build_layout_test_installer.py',LOC/'packaging/layout_test_backend.py']
    pins += [LOC/'translations/zh-CN.jsonl',LOC/'catalog/units.jsonl',LOC/'catalog/occurrences.jsonl',LOC/'catalog/resources.jsonl',LOC/'tests/test_dialogue_joins.py',LOC/'tests/test_dialogue_sfw.py',LOC/'tests/fixtures/dialogue-joins-initial.jsonl']
    before={p.relative_to(ROOT).as_posix():sha(p) for p in pins}
    work=LOC/'work/dialogue-builds'/uuid.uuid4().hex;work.mkdir(parents=True);logs=work/'logs';logs.mkdir()
    run([sys.executable,'-B','-m','unittest','discover','-s',LOC/'tests','-p','test_dialogue*.py','-v'],ROOT,logs/'dialogue-unit.log')
    classes,tools,code=runtime(work,logs)
    jar=work/'runtime-validation.jar';rewrite(BASE/'cosmobreeder-multi.jar',jar,code)
    for suffix,java,props in [('original',JRE,[]),('tr',JRE,['-Duser.language=tr','-Duser.country=TR']),('jdk',JDK/'java.exe',[])]:
        run([java,'-Dfile.encoding=UTF-8',*props,'-Xverify:all','-cp',str(classes)+os.pathsep+str(jar),'DialogueWrapTest',LOC/'runtime/bbc2.fnt'],ROOT,logs/('runtime-'+suffix+'.log'))
    run([JRE,'-Xverify:all','-cp',classes,'DialogueGridTest'],ROOT,logs/'grid-core.log')
    changes,text_reports=text_resources();rewrite(BASE/'patch.pak',work/'patch.pak',changes)
    sfw_changes={};sfw_reports=[]
    with zipfile.ZipFile(ROOT/'backup/cosmobreeder-multi.jar') as original,zipfile.ZipFile(BASE/'cosmobreeder-multi.jar') as localized:
        for logical,entry in [('datadf/all.ds','datadf/1'),('datadm/all.ds','datadm/1')]:
            joined,report=dialogue_sfw.rewrite_sfw(logical,decrypt_file(original.read(entry)),decrypt_file(localized.read(entry)),dialogue_joins.load_records())
            sfw_changes[entry]=encrypt_file(joined,os.urandom(32),os.urandom(8));sfw_reports.append(report)
    jar=work/'cosmobreeder-multi.jar';rewrite(BASE/'cosmobreeder-multi.jar',jar,{**code,**sfw_changes})
    with zipfile.ZipFile(BASE/'cosmobreeder-multi.jar') as base,zipfile.ZipFile(jar) as check:
        for name in ('PRG/Mf.class','PRG/LX.class','PRG/LY.class','PRG/Iu.class','PRG/Le.class','PRG/Lg.class','PRG/Lb.class','bbc2.fnt'):
            if base.read(name)!=check.read(name):raise ValueError('Original menu/font changed')
        if 'PRG/SaveMenuLayout.class' in check.namelist():raise ValueError('Single-card code must not enter this build')
    names=work/'classes.txt';names.write_text('\n'.join(k[:-6].replace('/','.') for k in code)+'\n',encoding='utf8')
    run([JRE,'-Xverify:all','-cp',str(tools)+os.pathsep+str(jar),'VerifyLayout',names],ROOT,logs/'verify-final-classes.log')
    prepared,man=prepare_installer(work,jar)
    run([sys.executable,'-B','-m','unittest','discover','-s',LOC/'tests','-p','test_layout_test_installer.py','-v'],ROOT,logs/'installer-unit.log')
    installer.integrate(work,prepared,man,logs)
    env=os.environ.copy();env.update(PYINSTALLER_CONFIG_DIR=str(work/'cache'),PYTHONDONTWRITEBYTECODE='1',TEMP=str(work/'tmp'),TMP=str(work/'tmp'));(work/'tmp').mkdir()
    run([sys.executable,'-m','PyInstaller','--noconfirm','--distpath',work/'dist','--workpath',work/'pyi',prepared/'LayoutTest.spec'],prepared,logs/'pyinstaller.log',env)
    exe=work/'dist'/(NAME+'.exe')
    from PyInstaller.archive.readers import CArchiveReader
    archive=CArchiveReader(str(exe));mapping={k.replace('\\','/'):k for k in archive.toc}
    if json.loads(archive.extract(mapping['manifest.json']))!=man:raise ValueError('Embedded manifest')
    for p in (prepared/'payload').iterdir():
        if hashlib.sha256(archive.extract(mapping['payload/'+p.name])).hexdigest()!=sha(p):raise ValueError('Embedded payload SHA')
    frozen=work/'frozen-check.json';run([exe,'--verify-payload',frozen],work,logs/'frozen-check.log',env)
    info=json.loads(frozen.read_text('utf8'))
    if info.get('activation')!=ACTIVATION or info.get('installed') is not False:raise ValueError('Frozen test activation')
    result=work/'result';result.mkdir()
    for p in (exe,jar,work/'patch.pak',frozen):shutil.copyfile(p,result/p.name)
    shutil.copyfile(prepared/'manifest.json',result/'installer-manifest.json');shutil.copyfile(LOC/'translations/dialogue-joins.jsonl',result/'dialogue-joins.jsonl')
    (result/'测试说明.md').write_text(README,encoding='utf8');shutil.copytree(logs,result/'verification-logs')
    (result/'join-report.json').write_text(json.dumps({'canonical_patch':text_reports,'sfw_jar':sfw_reports},ensure_ascii=False,indent=2)+'\n',encoding='utf8')
    (result/(exe.name+'.sha256')).write_text(sha(exe)+'  '+exe.name+'\n',encoding='ascii')
    manifest={'version':VERSION,'status':'story_radio_10px_test_not_G3','activation':ACTIVATION,'game_started':False,'installed_to_original_game':False,'user_save_accessed':False,'source_sha256':before,
              'archives':[{'archive':p.name,'sha256':sha(p),'bytes':p.stat().st_size} for p in (jar,work/'patch.pak')],
              'exe':{'name':exe.name,'sha256':sha(exe),'bytes':exe.stat().st_size},'changed_classes':['PRG/JR.class','PRG/Nb.class'],
              'added_helpers':sorted(k for k in code if k not in ('PRG/JR.class','PRG/Nb.class')),
              'join_groups':sum(r['applied_groups'] for r in text_reports),'removed_split_nodes':sum(r['removed_text_nodes'] for r in text_reports),
              'sfw_join_groups':sum(r['applied_groups'] for r in sfw_reports),'sfw_join_skips':sum(len(r['skipped']) for r in sfw_reports),
              'sfw_join_status':'exact original JAR root/prefix/source matches; no PAK offsets reused'}
    (result/'build-manifest.json').write_text(json.dumps(manifest,ensure_ascii=False,indent=2)+'\n',encoding='utf8')
    verify_inputs()
    if any(sha(ROOT/path)!=h for path,h in before.items()):raise ValueError('Source changed during build')
    if output.exists() or output.resolve()!=output or not output.is_relative_to(allowed):raise ValueError('Publish path changed')
    print('Publish NEW dialogue test build:',result.resolve(),'->',output,flush=True);result.rename(output)
    print(json.dumps({'output':str(output),'exe':exe.name,'sha256':manifest['exe']['sha256'],'join_groups':manifest['join_groups'],'activation':ACTIVATION},ensure_ascii=False,indent=2))


if __name__=='__main__':sys.stdout.reconfigure(encoding='utf8');main()
