"""Seal the already-verified candidate and checklist into a NON-INSTALLER ZIP.
Never launch Java/game or modify candidate/source/install/save files.
"""
from __future__ import annotations
import argparse
import hashlib
import json
from pathlib import Path
import re
import shutil
import sys
import uuid
import zipfile

ROOT=Path(__file__).resolve().parents[3]
sys.path.insert(0,str(ROOT/'localization/tools'))
from layout_bundle import read_layout_bundle
from build_layout import verify_inputs


def sha(path):return hashlib.sha256(path.read_bytes()).hexdigest()


README='''# 实验候选交付：非安装版

**状态：CANDIDATE_NOT_ACCEPTED。不要覆盖原安装，不要双击JAR，不要直接运行旧验证包。**

本包不含安装器、启动脚本或JRE，不会自动启用任何布局。三个原型默认关闭；VSN和道具页没有猜测的容器默认值。当前交付仅用于离线检查与下一阶段验收准备，不是全游戏中文排版完成。

## 1. 包内文件

- [候选清单](<candidate/package-manifest.json>)：12个原class改写、34个helper；两个归档SHA及实际验证日志。
- [验收清单](<acceptance-checklist.md>)：已验证项及仍未验证的门槛。
- [第一阶段摘要](<verification-summary.json>)、[绘制验证摘要](<verification-followup.json>)。
- [动态文字碰撞报告](<replay-report.json>)：CPU重放，不是截图。
- [左右对照图](<previews/compare-normal-0-4x.png>)：左原绘制、右候选；原始图集RGBA，无shader/CRT。
- [包内逐文件校验清单](<delivery-manifest.json>)。

## 2. 已通过的有限验证

布局核心37,928项断言；Python门禁64项；存档、主道具页及真实r21字幕/animation copy夹具通过。原JRE以-Xverify:all加载最终46类，不初始化Main。

无启动存档探针22场景、1450个SN调用、3172项断言；重放器9项测试。11个成功候选帧动态文字alpha重叠0；预期拒绝的9中文名字不计作通过。保留所有数据与原选择列表，不截断正文或缩回8px。

## 3. 启用边界

默认关闭时，原画面不会改善；不能把能启动当成已适配。候选的显式原型接口要求相应profile，配置、完整源码及复现命令仍以原仓库实施说明为准。本ZIP不是独立构建环境，也没有提供经过验证的窗口内矩形。

主道具页保留42项图标网格，超高说明没有已证安全翻页输入；其他classic/DS等入口仍待扩展。compact10仅为独立资产候选，未全局替换classic。不要把此包交给旧安装器当载荷。

## 4. 隔离风险

历史验证曾写回原存档。现有旧载荷实际包含save/options两个setter，仍不能证明安全：存档服务缓存文件句柄，加载失败也可能写备份；另有错误日志、native和进程外Steam边界。仅复制目录、改cwd或改设置路径不等于隔离。

本阶段没有启动完整游戏、Steam或安装器，没有读取或修改用户存档。完整G3运行前必须在安全的可丢弃环境验证写入边界。不得拿原存档试错，亦不得通过关闭保护重试。

## 5. 证据边界

绘制探针使用合成数据、测试专用存档枚举、部分构造器绕过与空注册表，执行真实绘制/格式化/CPU glyph-run方法，但不执行存档服务、GL或输入动作。Java测试guard不是OS沙箱，不保护实际游戏native程序。

重放统计只覆盖动态文字alpha；不证明图标/面板、真实父clip、CRT、合法全部数据域、键鼠/手柄或实际事件时序。原SFW开场英文仍是非目标，不能据此宣称SFW中文通过。图片背景字样不代表补丁版本，身份以SHA为准。

## 6. 正式版本仍待完成

见[验收清单](<acceptance-checklist.md>)。所有安全、矩形、时序和画面门槛通过后才可准备正式安装器。本包不执行安装或回退；未曾安装本包，因此没有需要修改原安装的回退操作。
'''


def package(output):
    output=output.resolve();allowed=(ROOT/'localization/builds').resolve()
    if output.suffix.lower()!='.zip' or output.exists() or not output.is_relative_to(allowed):
        raise ValueError('Output must be a new ZIP under localization/builds')
    verify_inputs()
    candidate=ROOT/'localization/builds/layout-r22-candidate-v2'
    manifest_raw=(candidate/'package-manifest.json').read_bytes();manifest=json.loads(manifest_raw)
    bundle,identity=read_layout_bundle(candidate/'layout-bundle')
    if identity!=manifest['plan']['layout_bundle']['manifest_sha256']:raise ValueError('Bundle/package identity mismatch')
    for record in manifest['archives']:
        if sha(candidate/record['archive'])!=record['sha256']:raise ValueError('Candidate archive changed')
    for relative,expected in bundle['source_sha256'].items():
        if sha(ROOT/relative)!=expected:raise ValueError('Implementation source drift: '+relative)
    for path in candidate.rglob('*'):
        if path.is_symlink():raise ValueError('Do not copy symlinks into delivery')
    work=ROOT/'localization/work/layout-delivery'/uuid.uuid4().hex;work.mkdir(parents=True)
    tree=work/'delivery';tree.mkdir()
    shutil.copytree(candidate,tree/'candidate')
    (tree/'README.md').write_text(README,encoding='utf-8')
    checklist=(ROOT/'localization/layout/validation/acceptance-checklist.md').read_text(encoding='utf-8')
    replacements={
        '../README.md':'README.md',
        '../../builds/layout-r22-candidate-v2/package-manifest.json':'candidate/package-manifest.json',
        'save-probe-notes.md':'README.md#5-证据边界',
        'isolation-preflight.md':'README.md#4-隔离风险',
        '../README.md#3-原型如何启用':'README.md#3-启用边界',
    }
    checklist=re.sub(r'\]\(<([^>]+)>\)',lambda m:'](<'+replacements.get(m.group(1),m.group(1))+'>)',checklist)
    (tree/'acceptance-checklist.md').write_text(checklist,encoding='utf-8')
    for name,path in {
        'verification-summary.json':ROOT/'localization/layout/verification-summary.json',
        'verification-followup.json':ROOT/'localization/layout/validation/verification-followup.json',
        'replay-report.json':ROOT/'localization/work/layout-drawing-replays/run-v3/replay-report.json',
    }.items():shutil.copyfile(path,tree/name)
    preview=tree/'previews';preview.mkdir()
    for name in ('compare-normal-0-4x.png','normal-off-0-4x.png','normal-on-0-4x.png','delete-on-visible-0-4x.png'):
        shutil.copyfile(ROOT/'localization/work/layout-drawing-replays/run-v3'/name,preview/name)
    files={p.relative_to(tree).as_posix():{'sha256':sha(p),'bytes':p.stat().st_size}
           for p in sorted(tree.rglob('*')) if p.is_file()}
    seal={'schema_version':1,'status':'EXPERIMENTAL_NOT_ACCEPTED_NOT_AN_INSTALLER',
          'source_candidate':'layout-r22-candidate-v2','source_package_manifest_sha256':hashlib.sha256(manifest_raw).hexdigest(),
          'layout_manifest_sha256':identity,'runtime_activation':'explicit_candidate_profiles_only',
          'game_started':False,'installed':False,'files':files,
          'self_hash_excluded':'delivery-manifest.json is not recursively included in its own file list'}
    (tree/'delivery-manifest.json').write_text(json.dumps(seal,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
    # Check local document references only after the manifest itself exists.
    for document in tree.glob('*.md'):
        for relative in re.findall(r'\]\(<([^>]+)>\)',document.read_text(encoding='utf-8')):
            if '://' not in relative and not (document.parent/relative.split('#')[0]).is_file():
                raise ValueError('Broken portable document link: '+relative)
    if (tree/'candidate/package-manifest.json').read_bytes()!=manifest_raw:
        raise ValueError('Copied candidate manifest changed')
    copied_bundle,copied_identity=read_layout_bundle(tree/'candidate/layout-bundle')
    if copied_identity!=identity:raise ValueError('Copied bundle identity changed')
    for record in manifest['archives']:
        if sha(tree/'candidate'/record['archive'])!=record['sha256']:raise ValueError('Copied archive identity changed')
    temporary=work/'delivery.zip'
    with zipfile.ZipFile(temporary,'w',zipfile.ZIP_DEFLATED,compresslevel=6) as archive:
        for path in sorted(tree.rglob('*')):
            if path.is_file():archive.write(path,path.relative_to(tree).as_posix())
    with zipfile.ZipFile(temporary) as archive:
        if archive.testzip() is not None:raise ValueError('Delivery ZIP integrity failed')
        expected_names=set(files)|{'delivery-manifest.json'}
        if set(archive.namelist())!=expected_names:raise ValueError('Delivery file set mismatch')
        for name,record in files.items():
            if hashlib.sha256(archive.read(name)).hexdigest()!=record['sha256']:raise ValueError('Delivery entry mismatch: '+name)
    verify_inputs()
    for relative,expected in bundle['source_sha256'].items():
        if sha(ROOT/relative)!=expected:raise ValueError('Source changed during delivery: '+relative)
    if output.exists() or output.resolve()!=output or not output.resolve().is_relative_to(allowed):
        raise ValueError('Delivery output changed before publish')
    print('Publish NEW experimental ZIP:',temporary.resolve(),'->',output.resolve(),flush=True)
    temporary.rename(output)
    print(json.dumps({'zip':str(output),'sha256':sha(output),'bytes':output.stat().st_size,
                      'status':seal['status'],'files':len(files)+1,'game_started':False,'installed':False},ensure_ascii=False,indent=2))


def main():
    parser=argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--output',type=Path,required=True)
    package(parser.parse_args().output)


if __name__=='__main__':
    sys.stdout.reconfigure(encoding='utf-8');main()
