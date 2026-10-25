"""Build the isolated r22-test1 installer. Does not install or start the game.
Reuses the existing GUI/backend in a fresh work directory, never the formal payload.
"""
from __future__ import annotations
import argparse
import contextlib
import hashlib
import importlib
import io
import json
import os
from pathlib import Path
import re
import shutil
import subprocess
import sys
import uuid
import zipfile

ROOT=Path(__file__).resolve().parents[2]
LOC=ROOT/'localization';HERE=LOC/'packaging'
sys.path.insert(0,str(LOC/'tools'));sys.path.insert(0,str(LOC/'layout/tools'))
import classfile
from build_layout import verify_inputs
from layout_bundle import read_layout_bundle
classfile.OPS[0xb9]=('invokeinterface','cp2pad')
VERSION='r22-test1'
NAME='CosmobreederYiffaiCN-Layout-r22-test1'


def sha(path):return hashlib.sha256(path.read_bytes()).hexdigest()


def execute(argv,cwd,log,env=None):
    result=subprocess.run([str(a) for a in argv],cwd=str(cwd),env=env,stdout=subprocess.PIPE,stderr=subprocess.STDOUT)
    log.write_bytes(result.stdout)
    print(log.stem,'exit',result.returncode,flush=True)
    if result.returncode:raise RuntimeError('Step failed; inspect '+str(log))


def normalize(cf,method):
    code=cf.code_of(method)
    if not code:return None
    rows=classfile.disasm(cf,code[0]);positions={pc:i for i,(pc,_,_) in enumerate(rows)}
    def operand(arg):
        arg=re.sub(r'^#\d+\s+','',arg)
        return re.sub(r'->\s*(-?\d+)',lambda m:'->i'+str(positions.get(int(m.group(1)),m.group(1))),arg)
    return [(op.replace('ldc_w','ldc'),operand(arg)) for _,op,arg in rows]


def make_test_jar(work,logs):
    base=LOC/'builds/layout-r22-candidate-v2'
    manifest=json.loads((base/'package-manifest.json').read_text('utf8'))
    bundle,identity=read_layout_bundle(base/'layout-bundle')
    if identity!=manifest['plan']['layout_bundle']['manifest_sha256']:raise ValueError('Base bundle identity changed')
    for entry in manifest['archives']:
        if sha(base/entry['archive'])!=entry['sha256']:raise ValueError('Base archive changed')
    for relative,h in bundle['source_sha256'].items():
        if sha(ROOT/relative)!=h:raise ValueError('Base source drift: '+relative)
    original_source=LOC/'layout/src/PRG/SaveMenuLayout.java'
    text=original_source.read_text('utf8')
    old='private static volatile boolean prototypeEnabled = Boolean.getBoolean("cosmo.layout.save.prototype");'
    new='private static volatile boolean prototypeEnabled = Boolean.parseBoolean(System.getProperty("cosmo.layout.save.prototype", "true"));'
    if text.count(old)!=1:raise ValueError('Test-default source hook is not unique')
    src=work/'runtime-src/PRG/SaveMenuLayout.java';src.parent.mkdir(parents=True)
    src.write_text(text.replace(old,new),encoding='utf8')
    classes=work/'runtime';classes.mkdir()
    javac=LOC/'toolchains/microsoft-jdk17/jdk-17.0.20.1+1/bin/javac.exe'
    java=ROOT/'research/testgame_cjk_verified/jre/bin/java.exe'
    execute([javac,'--release','8','-encoding','UTF-8','-Xlint:all','-cp',base/'cosmobreeder-multi.jar','-d',classes,src],ROOT,logs/'compile-test-runtime.log')
    produced=[p.relative_to(classes).as_posix() for p in classes.rglob('*.class')]
    if produced!=['PRG/SaveMenuLayout.class']:raise ValueError('Unexpected test runtime inventory')
    helper=(classes/'PRG/SaveMenuLayout.class').read_bytes()
    target=work/'cosmobreeder-multi.jar'
    with zipfile.ZipFile(base/'cosmobreeder-multi.jar') as before,zipfile.ZipFile(target,'w',zipfile.ZIP_DEFLATED,compresslevel=6) as after:
        old_helper=before.read('PRG/SaveMenuLayout.class')
        a=classfile.load(old_helper);b=classfile.load(helper)
        am={(m['name'],m['desc']):m for m in a.methods};bm={(m['name'],m['desc']):m for m in b.methods}
        if set(am)!=set(bm) or a.this_name!=b.this_name or b.major!=52:raise ValueError('Test helper shape changed')
        for key in am:
            if key[0]!='<clinit>' and normalize(a,am[key])!=normalize(b,bm[key]):raise ValueError('Non-toggle runtime method changed: '+str(key))
        for info in before.infolist():after.writestr(info,helper if info.filename=='PRG/SaveMenuLayout.class' else before.read(info.filename))
    with zipfile.ZipFile(base/'cosmobreeder-multi.jar') as before,zipfile.ZipFile(target) as after:
        if set(before.namelist())!=set(after.namelist()) or after.testzip() is not None:raise ValueError('Test JAR entry mismatch')
        changed=[n for n in before.namelist() if before.read(n)!=after.read(n)]
        if changed!=['PRG/SaveMenuLayout.class']:raise ValueError('More than one test-only helper changed')
    probe=work/'probe';probe.mkdir()
    execute([javac,'--release','8','-encoding','UTF-8','-cp',target,'-d',probe,HERE/'tests/TestInstallProfileProbe.java',LOC/'layout/tools/java/VerifyLayout.java'],ROOT,logs/'compile-probe.log')
    cp=str(probe)+os.pathsep+str(target)
    execute([java,'-Xverify:all','-cp',cp,'TestInstallProfileProbe',target,'true'],ROOT,logs/'profile-default-on.log')
    execute([java,'-Xverify:all','-Dcosmo.layout.save.prototype=false','-cp',cp,'TestInstallProfileProbe',target,'false'],ROOT,logs/'profile-explicit-off.log')
    names=work/'classes-to-verify.txt';names.write_text('\n'.join(n[:-6].replace('/','.') for n in bundle['classes'])+'\n',encoding='utf8')
    execute([java,'-Xverify:all','-cp',cp,'VerifyLayout',names],ROOT,logs/'verify-test-classes.log')
    return base,target,{'source_candidate_manifest_sha256':sha(base/'package-manifest.json'),
        'source_candidate_jar_sha256':sha(base/'cosmobreeder-multi.jar'),'test_jar_sha256':sha(target),
        'changed_from_candidate':['PRG/SaveMenuLayout.class'],'non_clinit_methods_unchanged':len(am)-1,
        'old_helper_sha256':hashlib.sha256(old_helper).hexdigest(),'test_helper_sha256':hashlib.sha256(helper).hexdigest(),
        'test_source_sha256':sha(src),'test_default':'save on; VSN/item diagnostic; explicit save=false still disables'}


def prepare(work,base,testjar):
    stage=work/'prepared';stage.mkdir();payload=stage/'payload';payload.mkdir()
    shutil.copyfile(testjar,payload/'cosmobreeder-multi.jar');shutil.copyfile(base/'patch.pak',payload/'patch.pak')
    original={'jar':LOC.parent/'backup/cosmobreeder-multi.jar','patch':LOC.parent/'backup/patch.pak'}
    def entry(name,origin):
        p=payload/name
        return {'path':name,'payload':name,'sha256':sha(p),'size':p.stat().st_size,
                'original':{'sha256':sha(origin),'size':origin.stat().st_size}}
    variants={}
    for label,source in [('original',ROOT/'backup'),('r21',LOC/'builds/final-8146-r21-images')]:
        jar=entry('cosmobreeder-multi.jar',source/'cosmobreeder-multi.jar')
        pak=entry('patch.pak',source/'patch.pak')
        variants[label+'-nsfw']={'label':label+' NSFW → r22测试版','available':True,
            'detect':{'cosmobreeder-multi.jar':{'sha256':jar['original']['sha256']},'patch.pak':{'sha256':pak['original']['sha256']}},'files':[jar,pak]}
        variants[label+'-vanilla']={'label':label+' 本体 → r22测试版','available':True,
            'detect':{'cosmobreeder-multi.jar':{'sha256':jar['original']['sha256']},'patch.pak':{'absent':True}},'files':[jar]}
    jar=entry('cosmobreeder-multi.jar',ROOT/'backup/cosmobreeder-multi.jar');pak=entry('patch.pak',ROOT/'backup/patch.pak')
    for suffix,files,rule in [('nsfw',[jar,pak],{'sha256':pak['sha256']}),('vanilla',[jar],{'absent':True})]:
        variants['installed-'+suffix]={'label':'已安装的r22排版测试版','available':False,
            'detect':{'cosmobreeder-multi.jar':{'sha256':jar['sha256']},'patch.pak':rule},'files':files}
    man={'name':'Cosmobreeder Yiffai 中文排版测试版','game':'Cosmobreeder Yiffai (Steam)',
         'version':VERSION,'built':'2026-10-25','status':'layout_test_not_accepted','experimental':True,
         'activation':{'save_single_card':True,'vsn':False,'item':False},'variants':variants,
         'notes':['仅默认启用存档单卡片，其他两处保留诊断。','未完成实机clip/CRT/输入验收。',
                  '安装器不读写存档，但运行游戏不是安全沙箱。','测试版独立备份/状态，卸载还原到安装前，不覆盖旧汉化备份。']}
    (stage/'manifest.json').write_text(json.dumps(man,ensure_ascii=False,indent=2)+'\n',encoding='utf8')
    source=(HERE/'patch_tool.py').read_text('utf8')
    for old,new in [('BACKUP_DIRNAME = "_汉化补丁备份"','BACKUP_DIRNAME = "_中文排版测试备份"'),('STATE_NAME = "install-state.json"','STATE_NAME = "layout-test-install-state.json"')]:
        if source.count(old)!=1:raise ValueError('Base backend constant hook changed')
        source=source.replace(old,new)
    # An unchanged PAK is a supported source file, not a duplicate install.
    old='if cur == e["sha256"]:\n            warnings.append'
    new='if cur == e["sha256"] and cur != e["original"]["sha256"]:\n            warnings.append'
    if source.count(old)!=1:raise ValueError('No-change payload compatibility hook changed')
    source=source.replace(old,new)
    source=source.replace('安装完成。直接启动游戏就是中文。','测试版安装完成：存档单卡片默认启用；开场/道具仍诊断，未启动游戏。')
    source=source.replace('要还原原版，重新运行本程序并点','要还原到安装测试版之前，重新运行本程序并点')
    (stage/'base_patch_tool.py').write_text(source,encoding='utf8')
    shutil.copyfile(HERE/'layout_test_backend.py',stage/'patch_tool.py')
    source=(HERE/'launcher.py').read_text('utf8')
    changes={
        'APP_NAME = "Cosmobreeder Yiffai 简体中文补丁"':'APP_NAME = "Cosmobreeder Yiffai 中文排版测试版 r22-test1"',
        'self.geometry("760x600")':'self.geometry("780x660")',
        'text="把游戏文本和四张图换成中文。只改两个文件，安装前自动备份。"':'text="测试版：启用存档单卡片；开场/道具仍诊断。未完成实机验收，请先备份存档。", wraplength=740',
        'text="应包含 cosmobreeder-multi.jar 和 patch.pak 的那一层目录。"':'text="选择原版或已知r21的游戏根目录；本体版可没有patch.pak。请完全退出游戏。"',
        '("安装", "install")':'("安装测试版", "install")',
        '"CosmobreederYiffaiCN", "logs"':'"CosmobreederYiffaiCN-LayoutTest", "logs"',
        '"确认卸载", "将用安装时的备份还原成原版。继续吗？"':'"确认还原测试版", "将还原到安装测试版之前（可能是旧汉化版本）。继续吗？"',
        '"install": "安装完成，启动游戏就是中文。"':'"install": "测试版已安装：存档单卡片默认启用；开场/道具仍诊断。未启动游戏。"',
        '"uninstall": "已还原成原版。"':'"uninstall": "已还原到安装测试版之前。"',
        'patch_tool.main()\n                    result = 0':'result = patch_tool.main() or 0',
    }
    for old,new in changes.items():
        if source.count(old)!=1:raise ValueError('Launcher hook not unique: '+old)
        source=source.replace(old,new)
    marker='        if command == "uninstall":'
    source=source.replace(marker,'        if command == "install" and not messagebox.askyesno("确认安装未验收测试版",\n                "仅启用存档单卡片；可能异常，未通过实机验收。\\n安装器不动存档，但运行游戏不是隔离。请自行备份存档。\\n\\n目录：" + self.game_dir.get() + "\\n\\n继续安装测试版？"):\n            return\n'+marker)
    marker='def main():\n    App().mainloop()'
    verify='''def main():
    if len(sys.argv) == 3 and sys.argv[1] == "--verify-payload":
        import json
        try:
            report = patch_tool.verify_payload()
            report["tcl_patchlevel"] = tk.Tcl().eval("info patchlevel")
            code = 0
        except Exception as failure:
            report = {"error": str(failure), "game_started": False, "installed": False}
            code = 1
        with open(sys.argv[2], "x", encoding="utf-8") as stream:
            json.dump(report, stream, ensure_ascii=False, indent=2)
        raise SystemExit(code)
    App().mainloop()'''
    if source.count(marker)!=1:raise ValueError('GUI verification entry hook changed')
    source=source.replace(marker,verify)
    (stage/'launcher.py').write_text(source,encoding='utf8')
    spec=f'''# generated test-only onefile spec, no installation at build time
import os
_HERE = os.path.abspath(SPECPATH)
a = Analysis([os.path.join(_HERE,'launcher.py')],pathex=[_HERE],binaries=[],
 datas=[(os.path.join(_HERE,'manifest.json'),'.'),(os.path.join(_HERE,'payload'),'payload')],
 hiddenimports=['patch_tool','base_patch_tool'],hookspath=[],hooksconfig={{}},runtime_hooks=[],
 excludes=['numpy','PIL','pandas','matplotlib','scipy','pytest'],noarchive=False,optimize=0)
pyz=PYZ(a.pure)
exe=EXE(pyz,a.scripts,a.binaries,a.datas,[],name={NAME!r},debug=False,
 bootloader_ignore_signals=False,strip=False,upx=False,console=False,
 disable_windowed_traceback=False,argv_emulation=False,uac_admin=False)
'''
    (stage/'LayoutTest.spec').write_text(spec,encoding='utf8')
    return stage,man


def integrate(work,stage,man,logs):
    sys.path.insert(0,str(stage))
    backend=importlib.import_module('patch_tool')
    # All targets are task-owned fixtures; no auto-discovery or game process.
    root=work/'install-fixtures';root.mkdir()
    with (logs/'installer-roundtrip.log').open('w',encoding='utf8') as record,contextlib.redirect_stdout(record):
        for variant in ('original-nsfw','r21-nsfw','original-vanilla','r21-vanilla'):
            folder=root/variant;folder.mkdir()
            src=ROOT/'backup' if variant.startswith('original') else LOC/'builds/final-8146-r21-images'
            names=['cosmobreeder-multi.jar']+(['patch.pak'] if variant.endswith('-nsfw') else [])
            before={}
            for name in names:shutil.copyfile(src/name,folder/name);before[name]=sha(folder/name)
            for name in ('cosmo.sav','cosmobreeder_options.json','install-state.json'):
                (folder/name).write_bytes(('private-fixture-sentinel:'+name).encode())
            old=folder/'_汉化补丁备份';old.mkdir();(old/'marker').write_text('untouched',encoding='utf8')
            sentinels={name:sha(folder/name) for name in ('cosmo.sav','cosmobreeder_options.json','install-state.json')}
            from types import SimpleNamespace
            args=SimpleNamespace(game_dir=str(folder),force=False,backup_dir=None)
            assert backend.cmd_install(args)==0
            for item in man['variants'][variant]['files']:assert sha(folder/item['path'])==item['sha256']
            assert backend.cmd_check(args)==0
            assert backend.cmd_uninstall(args)==0
            assert all(sha(folder/name)==h for name,h in before.items())
            assert all(sha(folder/name)==h for name,h in sentinels.items())
            assert (old/'marker').read_text('utf8')=='untouched'
            assert not (folder/'layout-test-install-state.json').exists()
            print('ROUNDTRIP_PASS',variant)
    print('installer-roundtrip exit 0: original/r21, NSFW/vanilla',flush=True)


README='''# 中文排版测试安装包 r22-test1

这是未验收测试版，不是稳定版。默认启用存档单卡片；开场字幕、道具详情仍只诊断，没有猜填未知容器。

1. 先自行备份存档，完全退出游戏和其他补丁工具。
2. 双击测试EXE，选择游戏根目录。支持原版及已知r21，本体/NSFW自动按SHA识别；未知版本停止，不提供强制覆盖。
3. 确认测试风险后安装。安装器仅写JAR/PAK和独立测试备份/状态，不读取或改写存档，不自动启动游戏。
4. 测试结束用同一程序“卸载 / 还原”，回到安装测试版之前；旧汉化的备份/状态保留。

测试备份：`_中文排版测试备份`；测试记录：`layout-test-install-state.json`。请保留备份，不要与旧安装器交叉还原。

存档单卡片将完整姓名、LVL/TRY/hex、地点及图标分行显示，选择列表不变。长字段可能明确报错；真实clip/CRT/输入和全部存档数据域尚未通过G3。其他classic/DS入口未扩展，不能当成全游戏排版完成。

原存档隔离未证明，运行游戏不是安全沙箱；建议在可丢弃环境试用。现有JVM参数若显式设置`-Dcosmo.layout.save.prototype=false`，仍会禁用单卡片。没有修改启动INI。

EXE未作数字签名；若安全系统拦截，请先核对SHA和来源，不建议关闭防护。本次只构建/验证安装器，没有替你安装或启动游戏。
'''


def main():
    parser=argparse.ArgumentParser(description=__doc__);parser.add_argument('--output',type=Path,required=True)
    args=parser.parse_args();destination=args.output.resolve();allowed=(LOC/'builds').resolve()
    if destination.exists() or destination==allowed or not destination.is_relative_to(allowed):raise ValueError('Output must be a new build directory')
    verify_inputs()
    source_paths=[Path(__file__),HERE/'patch_tool.py',HERE/'launcher.py',HERE/'layout_test_backend.py',
                  HERE/'tests/TestInstallProfileProbe.java',LOC/'tests/test_layout_test_installer.py']
    source_pins={p.relative_to(ROOT).as_posix():sha(p) for p in source_paths}
    work=LOC/'work/layout-test-installer'/uuid.uuid4().hex;work.mkdir(parents=True)
    logs=work/'logs';logs.mkdir()
    base,testjar,runtime_info=make_test_jar(work,logs)
    stage,man=prepare(work,base,testjar)
    execute([sys.executable,'-B','-m','unittest','discover','-s',LOC/'tests','-p','test_layout_test_installer.py','-v'],ROOT,logs/'backend-unit.log')
    integrate(work,stage,man,logs)
    env=os.environ.copy();env['PYINSTALLER_CONFIG_DIR']=str(work/'cache');env['PYTHONDONTWRITEBYTECODE']='1'
    env['TEMP']=env['TMP']=str(work/'tmp');(work/'tmp').mkdir()
    dist=work/'dist'
    execute([sys.executable,'-m','PyInstaller','--noconfirm','--distpath',dist,'--workpath',work/'pyi-build',stage/'LayoutTest.spec'],stage,logs/'pyinstaller.log',env)
    exe=dist/(NAME+'.exe')
    from PyInstaller.archive.readers import CArchiveReader
    archive=CArchiveReader(str(exe));mapping={n.replace('\\','/'):n for n in archive.toc}
    embedded=json.loads(archive.extract(mapping['manifest.json']))
    if embedded!=man:raise ValueError('Embedded manifest mismatch')
    for path in (stage/'payload').iterdir():
        if hashlib.sha256(archive.extract(mapping['payload/'+path.name])).hexdigest()!=sha(path):raise ValueError('Embedded payload mismatch')
    report=work/'frozen-verification.json'
    execute([exe,'--verify-payload',report],work,logs/'frozen-verify.log',env)
    frozen=json.loads(report.read_text('utf8'))
    if frozen.get('activation')!=man['activation'] or frozen.get('version')!=VERSION or frozen.get('game_started') is not False:
        raise ValueError('Frozen installer verification failed')
    result=work/'result';result.mkdir();shutil.copyfile(exe,result/exe.name)
    (result/'测试版说明.md').write_text(README,encoding='utf8')
    shutil.copyfile(stage/'manifest.json',result/'payload-manifest.json')
    shutil.copytree(logs,result/'verification-logs');shutil.copyfile(report,result/'frozen-verification.json')
    (result/(exe.name+'.sha256')).write_text(sha(exe)+'  '+exe.name+'\n',encoding='ascii')
    info={'schema_version':1,'version':VERSION,'status':'test_installer_not_G3_accepted','exe':exe.name,'sha256':sha(exe),
          'bytes':exe.stat().st_size,'activation':man['activation'],'runtime':runtime_info,
          'verification':{'profile_on_and_explicit_off':True,'verified_classes_no_init':46,'roundtrip_variants':4,
                          'embedded_payload_sha_checked':True,'frozen_payload_and_tcl_check':True},
          'game_started':False,'installed_to_original_game':False,'save_accessed':False,
          'source_sha256':source_pins,
          'prepared_source_sha256':{p.name:sha(p) for p in stage.iterdir() if p.is_file()}}
    (result/'build-manifest.json').write_text(json.dumps(info,ensure_ascii=False,indent=2)+'\n',encoding='utf8')
    verify_inputs()
    for path in source_paths:
        if sha(path)!=source_pins[path.relative_to(ROOT).as_posix()]:raise ValueError('Build source changed before publish')
    if destination.exists() or destination.resolve()!=destination or not destination.resolve().is_relative_to(allowed):raise ValueError('Destination changed')
    print('Publish NEW test installer directory:',result.resolve(),'->',destination,flush=True)
    result.rename(destination)
    print(json.dumps({'output':str(destination),'exe':exe.name,'sha256':info['sha256'],'activation':man['activation'],'game_started':False},ensure_ascii=False,indent=2))


if __name__=='__main__':
    sys.stdout.reconfigure(encoding='utf8');main()
