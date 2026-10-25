"""Build r26: independent true12 story/VSN font, retained narrow/menu fixes. Never start game."""
from pathlib import Path
import argparse
import base64
import hashlib
import json
import os
import shutil
import sys
import subprocess
import uuid
import zipfile
from io import BytesIO
from PIL import Image
import build_dialogue as common

ROOT=common.ROOT;LOC=common.LOC;BASE=common.BASE;JDK=common.JDK;JRE=common.JRE;EXPORTS=common.EXPORTS
sys.path.insert(0,str(LOC/'tools'))
from codec import decrypt_file,encrypt_file
import dialogue_joins,dialogue_sfw
import build_story_font12


ASSET_PYTHON = sys.executable


def font_assets():
    # Use the producer's pinned Pillow environment; PNG encoding differs between
    # Pillow releases even when the uncompressed native glyph pixels are equal.
    # The producer is read-only. Only its bytes enter this authorized archive build.
    script="import sys,json,base64;sys.path.insert(0,'localization/tools');import build_story_font12 as f;m,a=f.build_story_font12_assets('localization/work/story-font12/font12.zip');print(json.dumps({'manifest':m,'files':{n:base64.b64encode(b).decode('ascii') for n,b in a.items()}}))"
    result=subprocess.run([str(ASSET_PYTHON),'-B','-c',script],cwd=ROOT,stdout=subprocess.PIPE,stderr=subprocess.PIPE)
    if result.returncode:raise RuntimeError(result.stderr.decode('utf8','replace'))
    generated=json.loads(result.stdout);manifest=generated['manifest'];files={n:base64.b64decode(value,validate=True) for n,value in generated['files'].items()}
    for name,expected in manifest['inventory'].items():
        if hashlib.sha256(files[name]).hexdigest()!=expected:raise ValueError('Story font producer transport SHA')
    if hashlib.sha256(files['story12.fnt']).hexdigest()!=build_story_font12.FONT_SHA256 or hashlib.sha256(files['bbc2-shared-story12.png']).hexdigest()!=build_story_font12.PNG_SHA256:raise ValueError('Sealed font bytes drift')
    entries={'story12.fnt':files['story12.fnt']}
    entries.update({'story12/'+name:data for name,data in files.items()})
    return manifest,files,entries


def overlay_font(archive,files):
    index=json.loads(decrypt_file(archive.read('dataq/0')))
    key='dataq/'+str(index['/sprites.png'])
    atlas_key='dataq/'+str(index['/sprites.atlas'])
    atlas=decrypt_file(archive.read(atlas_key)).decode('utf8').replace('\r\n','\n')
    if 'size: 4096, 6144' not in atlas:raise ValueError('Expanded source atlas dimensions')
    with Image.open(BytesIO(decrypt_file(archive.read(key)))) as image:original=image.convert('RGBA')
    with Image.open(BytesIO(files['bbc2-shared-story12.png'])) as image:page=image.convert('RGBA')
    with Image.open(LOC/'runtime/bbc2-cjk-10.png') as image:old_page=image.convert('RGBA')
    box=(0,4096,2048,6144)
    if original.size!=(4096,6144) or page.size!=(2048,2048) or original.crop(box).tobytes()!=old_page.tobytes():raise ValueError('Font source region drift')
    modified=original.copy();modified.paste(page,(0,4096))
    if modified.crop((0,0,4096,4096)).tobytes()!=original.crop((0,0,4096,4096)).tobytes() or modified.crop((2048,4096,4096,6144)).tobytes()!=original.crop((2048,4096,4096,6144)).tobytes():raise ValueError('Nonfont atlas pixels changed')
    out=BytesIO();modified.save(out,format='PNG')
    return key,seal(out.getvalue())
VERSION='r27-story12-shaderfix-test5';NAME='CosmobreederYiffaiCN-'+VERSION
ACTIVATION={'save_single_card':False,'story_wrap':True,'radio_wrap':True,'continue_wrap_8':True,'vsn_wrap':True,'story_font_12px':True,'item_font_8px':True,'ending_report_8px':True}
TARGETS={'PRG/JR.class','PRG/Nb.class','PRG/amH.class','PRG/anp.class','PRG/Yg.class','PRG/Le.class','PRG/Lg.class','PRG/Lb.class','PRG/Kr.class','PRG/Kc.class','PRG/jo.class','PRG/Na.class'}
RUNTIME=['cosmoloc/layout/PixelLayout.java','cosmoloc/layout/DialogueGrid.java','cosmoloc/layout/FontAccess.java','PRG/LayoutBridge.java','PRG/DialogueWrap.java','PRG/SubtitleLayout.java','PRG/ItemFont8.java','PRG/EndingReportLayout.java','PRG/StoryFont12.java']
TESTS=['DialogueGridTest.java','DialogueWrapTest.java','ContinueWrapTest.java','SubtitleLayoutTest.java','ItemFont8Test.java','EndingReportLayoutTest.java','StoryFont12Test.java']
TOOLS=['VsnPatch.java','BridgePatch.java','DialoguePatch.java','SubtitlePatch.java','ItemFont8Patch.java','EndingReportPatch.java','StoryFont12Patch.java','FullTextBuild.java','VerifyLayout.java']


def seal(data):
    result=encrypt_file(data,os.urandom(32),os.urandom(8))
    if decrypt_file(result)!=data:raise ValueError('Encrypted resource roundtrip')
    return result


def compile_runtime(work,logs):
    classes=work/'runtime';classes.mkdir();tools=work/'tools';tools.mkdir();tests=work/'tests';tests.mkdir()
    src=LOC/'layout/src';ts=LOC/'layout/tests';js=LOC/'layout/tools/java'
    common.run([JDK/'javac.exe','--release','8','-encoding','UTF-8','-cp',ROOT/'backup/cosmobreeder-multi.jar','-d',classes,*[src/p for p in RUNTIME]],ROOT,logs/'compile-runtime.log')
    common.run([JDK/'javac.exe',*EXPORTS,'-encoding','UTF-8','-cp',str(classes)+os.pathsep+str(ROOT/'backup/cosmobreeder-multi.jar'),'-d',tools,*[js/p for p in TOOLS]],ROOT,logs/'compile-tools.log')
    common.run([JDK/'javac.exe',*EXPORTS,'-encoding','UTF-8','-cp',os.pathsep.join(map(str,[classes,tools,ROOT/'backup/cosmobreeder-multi.jar'])),'-d',tests,*[ts/p for p in TESTS]],ROOT,logs/'compile-tests.log')
    targets=work/'targets.jar';common.run([JDK/'java.exe',*EXPORTS,'-cp',tools,'FullTextBuild',BASE/'cosmobreeder-multi.jar',classes,targets],ROOT,logs/'patch-all.log')
    with zipfile.ZipFile(targets) as z:
        if set(z.namelist())!=TARGETS:raise ValueError('Unexpected patch inventory')
        code={n:z.read(n) for n in z.namelist()}
    for p in classes.rglob('*.class'):
        data=p.read_bytes();name=p.relative_to(classes).as_posix()
        if int.from_bytes(data[6:8],'big')!=52:raise ValueError('Runtime must be Java8')
        if not name.startswith(('PRG/','cosmoloc/layout/')):raise ValueError('Unexpected runtime file')
        code[name]=data
    testjar=work/'tests.jar'
    with zipfile.ZipFile(testjar,'w') as z:
        for p in tests.rglob('*.class'):z.write(p,p.relative_to(tests).as_posix())
    return classes,tools,testjar,code


def dictionary_override(data):
    tree=json.loads(data);old=dict(tree);applied=[]
    for row in (LOC/'translations/layout-short-overrides.jsonl').read_text('utf8').splitlines():
        record=json.loads(row);key=record['key'];value=tree[key]
        if value==record['expected_r21']:tree[key]=record['replacement'];applied.append(key)
        elif value.strip()=='FMOD STUDIO BY FIRELIGHT':pass # Original English branch already fits31 cells.
        else:raise ValueError('Ending dictionary source drift: '+key)
    if set(k for k in tree if tree[k]!=old[k])!=set(applied):raise ValueError('Unrelated dictionary changed')
    return json.dumps(tree,ensure_ascii=False,separators=(',',':')).encode('utf8'),applied


def resources(work,font_files,font_entries):
    changes,reports=common.text_resources();sfw={};sfw_reports=[];dict_reports=[]
    changes.update(font_entries)
    with zipfile.ZipFile(BASE/'patch.pak') as z:
        key,encrypted=overlay_font(z,font_files);changes[key]=encrypted
        data,keys=dictionary_override(decrypt_file(z.read('datav/1')));changes['datav/1']=seal(data)
        (work/'candidate-dictionary.json').write_bytes(data);dict_reports.append({'archive':'patch.pak','keys':keys,'sha256':hashlib.sha256(data).hexdigest()})
    sfw.update(font_entries)
    with zipfile.ZipFile(ROOT/'backup/cosmobreeder-multi.jar') as original,zipfile.ZipFile(BASE/'cosmobreeder-multi.jar') as localized:
        key,encrypted=overlay_font(localized,font_files);sfw[key]=encrypted
        for logical,entry in [('datadf/all.ds','datadf/1'),('datadm/all.ds','datadm/1')]:
            result,report=dialogue_sfw.rewrite_sfw(logical,decrypt_file(original.read(entry)),decrypt_file(localized.read(entry)),dialogue_joins.load_records())
            sfw[entry]=seal(result);sfw_reports.append(report)
        data,keys=dictionary_override(decrypt_file(localized.read('datav/1')));sfw['datav/1']=seal(data)
        dict_reports.append({'archive':'cosmobreeder-multi.jar','keys':keys,'sha256':hashlib.sha256(data).hexdigest()})
    return changes,reports,sfw,sfw_reports,dict_reports


def vsn_inputs(work):
    directory=work/'vsn-resources';directory.mkdir();manifest=[]
    for archive,variant in [('cosmobreeder-multi.jar','sfw'),('patch.pak','nsfw')]:
        with zipfile.ZipFile(BASE/archive) as z:
            index=json.loads(decrypt_file(z.read('vsn/0')))
            for logical,entry in sorted(index.items()):
                if not logical.endswith('/script.vsn'):continue
                scene=logical.strip('/').split('/')[-2];path=directory/(variant+'-'+scene+'.txt')
                path.write_bytes(decrypt_file(z.read('vsn/'+str(entry))));manifest.append(variant+'\t'+scene+'\t'+str(path))
    result=work/'vsn-resources.tsv';result.write_text('\n'.join(manifest)+'\n',encoding='utf8');return result


README='''# r27 剧情12px黄色实心字块修正版

本版专修r26实际截图中的实心黄色条块。真实cosmo/vsn终端着色器用纹理红通道而非透明度判断笔画；r26透明白背景错误地让144个像素全部变成笔画。新字格空白改RGBA(0,0,0,0)，全部2312新字形逐像素验证红通道与原生alpha笔画一致；例如“中”恢复37个笔画像素，不再整格144点。字体FNT、字号、换行及Java运行逻辑完全不改，不修改游戏着色器。

## 沿用的12px场景设置

按用户最新要求，中文开场/结束叙事报告及普通全宽剧情使用独立story12原生字库，约20汉字/240px换行，左边距从16调整为8，最右248仍在logical256内；原16px行距、显露/翻页/事件保持。纯英文完整页及Fox/HardFox图案保持原角色与位置。

无线电10px/150px、Continue10px/80px（约8汉字）、道具classic8、存档10px原布局不变。保留956组合句，不带单卡片。

新字体采用官方Fusion Pixel原生12px源与完整OFL许可，非放大10px位图。与default10共享原纹理，在原图集空白处追加；原10px glyph坐标和像素、classic/dingbats及其他图片区域均受保护。新字库由已授权的正常打包API直接收录归档，不创建此前被Windows拒绝的中间目录，也不声称该目录问题已修好。

请完全退出游戏、自己备份存档。装过r23/r24等旧排版测试版时先用旧EXE“卸载/还原”，再装本包，不用force覆盖未知文件。安装器不自动启动游戏、不读写存档；复制目录不是存档沙箱。

当前包的实际合句数、双方传输站回归、原版/r21×本体/NSFW还原夹具及完整测试日志见build-manifest.json、join-report.json与verification-logs。明确的独立句、停顿、变量及测试等边界不硬拼。

CPU记录式SN覆盖真实绘制入口，但还不是实机clip/CRT/所有输入验收。请重点复测此前开场超屏、报告长段、旧传输站同句以及道具名称/说明；截图反馈最后一页和边缘文字是否完整。
'''


def main():
    global ASSET_PYTHON
    ap=argparse.ArgumentParser(description=__doc__);ap.add_argument('--output',type=Path,required=True);ap.add_argument('--asset-python',type=Path,required=True,help='Producer interpreter with the pinned Pillow12.3 environment');a=ap.parse_args()
    ASSET_PYTHON=a.asset_python.resolve()
    if not ASSET_PYTHON.is_file():raise ValueError('Asset producer interpreter missing')
    output=a.output.resolve();allowed=(LOC/'builds').resolve()
    if output.exists() or output==allowed or not output.is_relative_to(allowed):raise ValueError('New build output only')
    common.verify_inputs();sources=[Path(__file__),Path(common.__file__),LOC/'tools/dialogue_joins.py',LOC/'tools/dialogue_sfw.py',LOC/'translations/dialogue-joins.jsonl',LOC/'translations/dialogue-join-coverage.json',LOC/'translations/layout-short-overrides.jsonl']
    sources += [LOC/'layout/src'/p for p in RUNTIME]+[LOC/'layout/tests'/p for p in TESTS]+[LOC/'layout/tools/java'/p for p in TOOLS]
    sources += [LOC/'tools/build_item_font8.py',LOC/'tools/build_story_font12.py',LOC/'work/story-font12/font12.zip']
    sources += [LOC/p for p in ['catalog/units.jsonl','catalog/occurrences.jsonl','catalog/resources.jsonl','translations/zh-CN.jsonl','packaging/build_layout_test_installer.py','packaging/layout_test_backend.py','tests/test_dialogue_joins.py','tests/test_dialogue_sfw.py','tests/test_story12_shader.py']]
    pins={p.relative_to(ROOT).as_posix():common.sha(p) for p in sources}
    work=LOC/'work/full-text-builds'/uuid.uuid4().hex;work.mkdir(parents=True);logs=work/'logs';logs.mkdir();print('WORK',work,flush=True)
    common.run([ASSET_PYTHON,'-B','-m','unittest','discover','-s',LOC/'tests','-p','test_story12_shader.py','-v'],ROOT,logs/'story12-shader-regression.log')
    common.run([sys.executable,'-B','-m','unittest','discover','-s',LOC/'tests','-p','test_dialogue*.py','-v'],ROOT,logs/'dialogue-unit.log')
    classes,tools,testjar,code=compile_runtime(work,logs)
    story_font_manifest,story_font_files,story_font_entries=font_assets()
    changes,join_reports,sfw,sfw_reports,dict_reports=resources(work,story_font_files,story_font_entries)
    jar=work/'cosmobreeder-multi.jar';pak=work/'patch.pak';common.rewrite(BASE/'cosmobreeder-multi.jar',jar,{**code,**sfw});common.rewrite(BASE/'patch.pak',pak,changes)
    manifest=vsn_inputs(work)
    with zipfile.ZipFile(jar) as z:
        (work/'classic.fnt').write_bytes(z.read('classic.fnt'))
    cp=os.pathsep.join(map(str,[testjar,jar,tools]));vm=[JRE,'-Dfile.encoding=UTF-8','-Xverify:all']
    joins_tsv=work/'joined-text.tsv';joins_tsv.write_text(''.join(record['join_id']+'\t'+base64.b64encode(record['merged_translation'].encode('utf8')).decode('ascii')+'\n' for record in dialogue_joins.load_records()),encoding='utf8')
    common.run([*vm,'-cp',cp,'DialogueWrapTest',LOC/'runtime/bbc2.fnt',joins_tsv],ROOT,logs/'dialogue-runtime.log')
    common.run([*vm,'-cp',cp,'DialogueGridTest'],ROOT,logs/'grid-runtime.log')
    common.run([*vm,'-cp',cp,'ContinueWrapTest',LOC/'runtime/bbc2.fnt'],ROOT,logs/'continue-runtime.log')
    for suffix,java,props in [('original',JRE,[]),('tr',JRE,['-Duser.language=tr','-Duser.country=TR']),('jdk',JDK/'java.exe',[])]:
        common.run([java,'-Dfile.encoding=UTF-8',*props,'-Xverify:all','-cp',cp,'SubtitleLayoutTest',LOC/'runtime/bbc2.fnt',manifest],ROOT,logs/('subtitle-'+suffix+'.log'))
    common.run([*vm,'-cp',cp,'EndingReportLayoutTest',work/'classic.fnt',work/'candidate-dictionary.json'],ROOT,logs/'ending-runtime.log')
    common.run([JDK/'java.exe',*EXPORTS,'-cp',cp,'StoryFont12Test','--preflight',BASE/'cosmobreeder-multi.jar'],ROOT,logs/'story12-patch-gates.log')
    common.run([*vm,*EXPORTS,'-cp',os.pathsep.join(map(str,[jar,testjar,tools])),'StoryFont12Test','--cpu',LOC/'runtime'],ROOT,logs/'story12-runtime.log')
    # ItemFont8Test build/CPU integration is supplied by the exact helper test CLI.
    common.run([JDK/'java.exe',*EXPORTS,'-cp',cp,'ItemFont8Test',BASE/'cosmobreeder-multi.jar',classes,LOC/'runtime',work/'item-unit.jar'],ROOT,logs/'item-patch-gates.log')
    common.run([*vm,*EXPORTS,'-cp',os.pathsep.join(map(str,[jar,work/'item-unit.jar',testjar,tools])),'ItemFont8Test','--cpu',jar,LOC/'runtime'],ROOT,logs/'item-runtime.log')
    common.run([sys.executable,'-B',LOC/'tools/build_item_font8.py','--audit-existing'],ROOT,logs/'item-corpus-audit.log')
    names=work/'classes.txt';names.write_text('\n'.join(n[:-6].replace('/','.') for n in code)+'\n',encoding='utf8')
    common.run([*vm,'-cp',cp,'VerifyLayout',names],ROOT,logs/'verify-final-classes.log')
    with zipfile.ZipFile(BASE/'cosmobreeder-multi.jar') as before,zipfile.ZipFile(jar) as after:
        for name in ['PRG/Mf.class','PRG/LX.class','PRG/LY.class','PRG/Iu.class','bbc2.fnt','classic.fnt','dingbats.fnt']:
            if before.read(name)!=after.read(name):raise ValueError('Original save/font changed: '+name)
        if 'PRG/SaveMenuLayout.class' in after.namelist():raise ValueError('No single-card code')
    common.VERSION=VERSION;common.NAME=NAME;common.ACTIVATION=ACTIVATION
    prepared,installer_manifest=common.prepare_installer(work,jar)
    installer_manifest['status']='story12_test_not_real_clip_CRT'
    installer_manifest['name']='Cosmobreeder Yiffai 12号字幕实心字块修正版'
    installer_manifest['notes']=['中文开场/报告/普通全宽剧情原生12px，约20字240px；局部左边距8。','无线电10px150、Continue10px80/约8字、道具classic8、存档原10不变。','独立story12角色与共享原纹理，原10px字形像素不变。','保留956合句及原显露/分页/事件；尚未实机验收。']
    (prepared/'manifest.json').write_text(json.dumps(installer_manifest,ensure_ascii=False,indent=2)+'\n',encoding='utf8')
    launcher=prepared/'launcher.py';branding=launcher.read_text('utf8')
    branding=branding.replace('10px剧情20字／无线电15字自然换行与同句合并；存档原布局。','开场/剧情/报告12号字、约20字换行；窄栏及道具/存档保持。')
    launcher.write_text(branding,encoding='utf8')
    common.run([sys.executable,'-B','-m','unittest','discover','-s',LOC/'tests','-p','test_layout_test_installer.py','-v'],ROOT,logs/'installer-unit.log')
    common.installer.integrate(work,prepared,installer_manifest,logs)
    env=os.environ.copy();env.update(PYINSTALLER_CONFIG_DIR=str(work/'cache'),PYTHONDONTWRITEBYTECODE='1',TEMP=str(work/'tmp'),TMP=str(work/'tmp'));(work/'tmp').mkdir()
    common.run([sys.executable,'-m','PyInstaller','--noconfirm','--distpath',work/'dist','--workpath',work/'pyi',prepared/'LayoutTest.spec'],prepared,logs/'pyinstaller.log',env)
    exe=work/'dist'/(NAME+'.exe');frozen=work/'frozen-check.json';common.run([exe,'--verify-payload',frozen],work,logs/'frozen-check.log',env)
    from PyInstaller.archive.readers import CArchiveReader
    arc=CArchiveReader(str(exe));embedded={n.replace('\\','/'):n for n in arc.toc}
    if json.loads(arc.extract(embedded['manifest.json']))!=installer_manifest:raise ValueError('Embedded manifest mismatch')
    for p in (prepared/'payload').iterdir():
        if hashlib.sha256(arc.extract(embedded['payload/'+p.name])).hexdigest()!=common.sha(p):raise ValueError('Embedded SHA')
    if json.loads(frozen.read_text('utf8'))['activation']!=ACTIVATION:raise ValueError('Frozen inactive code')
    result=work/'result';result.mkdir()
    for p in [exe,jar,pak,frozen]:shutil.copyfile(p,result/p.name)
    shutil.copyfile(prepared/'manifest.json',result/'installer-manifest.json');shutil.copytree(logs,result/'verification-logs')
    for p in ['dialogue-joins.jsonl','dialogue-join-coverage.json','layout-short-overrides.jsonl']:shutil.copyfile(LOC/'translations'/p,result/p)
    (result/'测试说明.md').write_text(README,encoding='utf8')
    (result/'join-report.json').write_text(json.dumps({'canonical_patch':join_reports,'sfw_jar':sfw_reports,'dictionary_overrides':dict_reports},ensure_ascii=False,indent=2)+'\n',encoding='utf8')
    build={'version':VERSION,'status':'tested_cpu_not_real_clip_CRT','activation':ACTIVATION,'game_started':False,'installed_to_original_game':False,'user_save_accessed':False,
           'widths_px':{'continue':80,'vsn_opening_report_cjk':240,'vsn_legacy_ascii':220,'radio':150,'story_cjk':240},
           'fonts':{'story_role':'story12','story_size_px':12,'default_size_px':10,'item_role':'classic8','native_story_manifest':story_font_manifest},
           'story_font_added_entries':sorted(story_font_entries),
           'atlas_font_region_modified':[0,4096,2048,6144],
           'source_sha256':pins,'changed_classes':sorted(TARGETS),'helper_inventory':sorted(set(code)-TARGETS),
           'archives':[{'archive':p.name,'sha256':common.sha(p),'bytes':p.stat().st_size} for p in [jar,pak]],
           'exe':{'name':exe.name,'sha256':common.sha(exe),'bytes':exe.stat().st_size},
           'canonical_join_groups':sum(r['applied_groups'] for r in join_reports),'canonical_removed_nodes':sum(r['removed_text_nodes'] for r in join_reports),
           'sfw_join_groups':sum(r['applied_groups'] for r in sfw_reports),'sfw_source_mismatch_skips':sum(len(r['skipped']) for r in sfw_reports)}
    (result/'build-manifest.json').write_text(json.dumps(build,ensure_ascii=False,indent=2)+'\n',encoding='utf8');(result/(exe.name+'.sha256')).write_text(common.sha(exe)+'  '+exe.name+'\n',encoding='ascii')
    common.verify_inputs()
    if any(common.sha(ROOT/p)!=h for p,h in pins.items()):raise ValueError('Source changed during build')
    if output.exists() or output.resolve()!=output or not output.is_relative_to(allowed):raise ValueError('Publish path drift')
    print('Publish exact NEW build:',result.resolve(),'->',output,flush=True);result.rename(output)
    print(json.dumps({'output':str(output),'exe':exe.name,'sha256':build['exe']['sha256'],'activation':ACTIVATION},ensure_ascii=False,indent=2))


if __name__=='__main__':sys.stdout.reconfigure(encoding='utf8');main()
