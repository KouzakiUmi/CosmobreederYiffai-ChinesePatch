"""Package a COMPLETE r28 independent candidate as an alpha0.1-compatible delta.

Only --candidate and a NEW direct child dist/r28... --output are accepted.
No installer mutation, EXE build, install/uninstall, game launch or save access.
The unchanged source installer is staged and invoked ONLY with --verify-payload.
"""
from __future__ import annotations
import argparse
from hashlib import sha256
import json
import os
from pathlib import Path
import re
import subprocess
import sys
import zipfile

ROOT = Path(__file__).resolve().parents[4]
sys.path.insert(0, str(ROOT / 'src'))
from cosmobreeder_patch.delta import build, apply, sha, BLOCK, MAGIC, MAX_FILE
from cosmobreeder_patch.installer import NAMES

COMPONENTS = frozenset(('core', 'pattern', 'compact', 'scenes', 'sfw', 'vsn', 'images'))
BUILD_VERSION = 'r28-full-opt-candidate'
BUILD_STATUS = 'integrated_candidate_not_real_clip_CRT_input_acceptance'
INTEGRATION_BASELINE = 'r27-story12-shaderfix-test5'
BASE_PINS = {
    'cosmobreeder-multi.jar': 'dc6b0cedc3a3b2f6f51941a2cef449d33ec87d314ee64ea63495c3ffdebd06be',
    'patch.pak': 'd2e21deeb85d74e981770b247625ee7ceb7ed39ae566305c1833c2c3d97b54d5',
}
SOURCE_PINS = {
    'cosmobreeder-multi.jar': 'cd37e445b36b8ad1b64a0089fe718362ec130af9219ee02f215d223ba8fa6221',
    'patch.pak': '2f9da7d49ece8427c5ae733f725bec0fe6b0b49c18d0331c06857d1ff758b2fa',
}
SOURCE_SIZES = {'cosmobreeder-multi.jar': 44859941, 'patch.pak': 12523943}
MODULES = ('__init__.py', '__main__.py', 'delta.py', 'installer.py')
ROOT_NOTICES = ('LICENSE', 'NOTICE', 'THIRD_PARTY_NOTICES.md')
REQUIRED_LICENSES = (
    'fonts/OFL.txt', 'fonts/NOTICE.txt', 'fonts/LICENSES/ark-pixel/OFL.txt',
    'fonts/LICENSES/cubic-11/OFL.txt', 'fonts/LICENSES/galmuri/LICENSE.txt',
    'runtime/Python-LICENSE.txt', 'runtime/PyInstaller-COPYING.txt',
    'runtime/Tk-license.terms', 'runtime/Tcl-license.terms',
)
NATIVE8_COMPONENTS = ('boutique-bitmap-7x7/OFL.txt', 'galmuri/LICENSE.txt',
                      'misaki/misaki.txt', 'miseki-bitmap/LICENSE.txt')
ZIP_NAME = 'CosmobreederYiffaiCN-r28-candidate-python.zip'


def require(ok, reason):
    if not ok:
        raise ValueError(reason)


def dump(path, value):
    path.write_text(json.dumps(value, ensure_ascii=False, indent=2) + '\n', encoding='utf-8', newline='\n')


def safe_path(path, root=ROOT, *, must_exist=True):
    """Reject links in EVERY ancestor; do not resolve away evidence first."""
    path = Path(os.path.abspath(path))
    root = Path(os.path.abspath(root))
    require(path.is_relative_to(root), '路径必须位于当前工程内: ' + str(path))
    current = path
    while current != root:
        require(not current.is_symlink(), '拒绝链接路径: ' + str(current))
        current = current.parent
    require(not root.is_symlink() and path.resolve() == path, '拒绝链接/路径漂移')
    require(not must_exist or path.exists(), '缺少路径: ' + str(path))
    return path


def validate_candidate(candidate):
    """Read-only schema/SHA gate. A partial pilot is NEVER relabelled as full."""
    candidate = safe_path(candidate)
    require(candidate.is_dir(), 'candidate必须为目录')
    path = safe_path(candidate / 'build-manifest.json')
    require(path.stat().st_size <= 16 * 1024 * 1024, 'build-manifest过大')
    m = json.loads(path.read_text(encoding='utf-8'))
    require(isinstance(m, dict) and m.get('version') == BUILD_VERSION, '不是r28完整候选构建清单')
    require(m.get('status') == BUILD_STATUS and m.get('full_component_set') is True,
            '仅支持完整integrated candidate；拒绝partial/pilot/building')
    selected = m.get('selected_components')
    require(isinstance(selected, list) and all(isinstance(x, str) for x in selected)
            and len(selected) == len(COMPONENTS) and set(selected) == COMPONENTS,
            '必须恰好包含七组件，不能缺项/重复/未知组件')
    require(m.get('base_archives') == BASE_PINS, '候选r27增量基线SHA不匹配')
    for flag in ('game_started', 'user_save_accessed', 'installed', 'real_clip_CRT_input_verified'):
        require(m.get(flag) is False, '候选执行边界字段必须明确为false: ' + flag)
    commands = m.get('commands')
    require(isinstance(commands, list) and commands and all(isinstance(c, dict) and isinstance(c.get('name'), str) and type(c.get('exit_code')) is int and c['exit_code'] == 0 for c in commands),
            '构建步骤必须均成功')
    require({'compile-runtime', 'compile-tools', 'patch-targets', 'verify-final-classes'} <= {c.get('name') for c in commands},
            '缺少必要构建步骤证据')
    archives = m.get('archives')
    require(isinstance(archives, dict) and set(archives) == set(NAMES), '必须锁定最终JAR和PAK两目标')
    for name in NAMES:
        target = safe_path(candidate / name)
        e = archives[name]
        require(isinstance(e, dict) and type(e.get('bytes')) is int and 1 <= e['bytes'] <= MAX_FILE,
                '目标尺寸无效: ' + name)
        require(isinstance(e.get('sha256'), str) and re.fullmatch('[0-9a-f]{64}', e['sha256']) is not None,
                '目标SHA无效: ' + name)
        require(target.is_file() and target.stat().st_size == e['bytes'] and sha(target) == e['sha256'],
                '最终目标与build-manifest不一致: ' + name)
    acceptance_path = safe_path(candidate / 'acceptance.json')
    require(acceptance_path.is_file() and acceptance_path.stat().st_size <= 16 * 1024 * 1024,
            'acceptance文件无效或过大')
    acceptance = json.loads(acceptance_path.read_text(encoding='utf-8'))
    require(isinstance(acceptance, dict) and acceptance.get('status') ==
            'passed_cpu_and_independent_review_not_real_clip_CRT_input',
            'acceptance状态必须为CPU及独立复核通过，不能缺验收或失败')
    accepted_archives = acceptance.get('archives')
    require(isinstance(accepted_archives, dict) and set(accepted_archives) == set(NAMES)
            and all(isinstance(accepted_archives[name], str)
                    and accepted_archives[name] == archives[name]['sha256']
                    and accepted_archives[name] == sha(candidate / name) for name in NAMES),
            'acceptance归档SHA必须与当前两实际目标一一相同')
    build_id = m.get('build_id', candidate.name)
    require(isinstance(build_id, str) and re.fullmatch('[A-Za-z0-9][A-Za-z0-9._-]{0,127}', build_id) is not None,
            'build_id必须为简单非路径标识')
    return candidate, m, build_id, sha(path)


def collect_text_inputs():
    """Exact installer code plus ALL old legal texts and native8 component texts."""
    files = {}
    inputs = {}
    def add(source, destination, is_code=False):
        source = safe_path(source)
        require(source.is_file() and source.stat().st_size <= 8 * 1024 * 1024, '声明/源码无效或过大')
        raw = source.read_bytes()
        text = raw.decode('utf-8')
        require('\x00' not in text, '拒绝非文本声明/源码')
        require(destination not in files, '重复的打包路径: ' + destination)
        if not is_code:
            require(not any(destination.lower().endswith(x) for x in ('.jar', '.pak', '.png', '.bdf', '.ttf', '.otf', '.exe', '.class')),
                    '许可目录不能包含游戏/字体二进制')
        files[destination] = raw
        inputs[source.relative_to(ROOT).as_posix()] = sha256(raw).hexdigest()
    for name in MODULES:
        add(ROOT / 'src/cosmobreeder_patch' / name, name, True)
    for name in ROOT_NOTICES:
        add(ROOT / name, name)
    legal = safe_path(ROOT / 'licenses')
    for name in REQUIRED_LICENSES:
        require((legal / name).is_file(), '缺少必要许可证: ' + name)
    for root, dirs, names in os.walk(legal, followlinks=False):
        for name in dirs:
            safe_path(Path(root) / name)
        for name in sorted(names):
            path = Path(root) / name
            add(path, 'licenses/' + path.relative_to(legal).as_posix())
    native = safe_path(ROOT / 'work/item-font8/asset')
    add(native / 'OFL.txt', 'licenses/fonts/native8/OFL.txt')
    for relative in NATIVE8_COMPONENTS:
        require((native / 'LICENSES' / relative).is_file(), '缺少native8上游声明: ' + relative)
    for root, dirs, names in os.walk(native / 'LICENSES', followlinks=False):
        for name in dirs:
            safe_path(Path(root) / name)
        for name in sorted(names):
            path = Path(root) / name
            add(path, 'licenses/fonts/native8/LICENSES/' + path.relative_to(native / 'LICENSES').as_posix())
    return files, inputs


def byte_equal(first, second):
    with open(first, 'rb') as a, open(second, 'rb') as b:
        while True:
            x, y = a.read(1024 * 1024), b.read(1024 * 1024)
            if x != y:
                return False
            if not x:
                return True


def verify_staged(staged_root, payload, log_dir):
    """This is the ONLY installer action this script can invoke."""
    env = dict(os.environ)
    env.pop('PYTHONPATH', None)
    env['PYTHONDONTWRITEBYTECODE'] = '1'
    env['PYTHONIOENCODING'] = 'utf-8'
    command = [sys.executable, '-B', '-m', 'cosmobreeder_patch', '--payload', str(payload), '--verify-payload']
    result = subprocess.run(command, cwd=staged_root, env=env, capture_output=True, timeout=120)
    (log_dir / 'verify-payload.stdout.txt').write_bytes(result.stdout)
    (log_dir / 'verify-payload.stderr.txt').write_bytes(result.stderr)
    require(result.returncode == 0, 'staged --verify-payload失败；检查checks日志')
    value = json.loads(result.stdout.decode('utf-8'))
    require(value == {'version': 'alpha0.1', 'status': 'verified', 'game_started': False}, 'staged verifier返回意外结果')
    return {'exit_code': result.returncode, 'action': '--verify-payload', 'result': value}


def validate_zip_members(names, expected):
    require(len(names) == len(set(names)) and set(names) == set(expected), 'ZIP与严格允许清单不一致')
    for name in names:
        require(name.startswith('cosmobreeder_patch/') and '\\' not in name and '..' not in Path(name).parts,
                'ZIP路径不安全')
        require(not name.lower().endswith(('.jar', '.pak', '.png', '.bdf', '.ttf', '.otf', '.exe', '.class', '.pyc')),
                'ZIP禁止完整游戏/原图/字体/编译产物: ' + name)


def readme(build_id, manifest):
    supported = '\n'.join(f'- `{n}` 原版SHA-256：`{SOURCE_PINS[n]}`' for n in NAMES)
    targets = '\n'.join(f'- `{n}` 候选SHA-256：`{manifest["files"][n]["target_sha256"]}`' for n in NAMES)
    return f'''# Cosmobreeder Yiffai 简中 r28 独立候选（Python源码差分版）

构建标识：**{build_id}**。仅候选，未经真实GPU/CRT/窗口缩放/输入命中/动态clip及存档I/O实机验收；不保证全部文字已翻译。非官方、未签名、无担保，不包含完整游戏、原图、字体二进制或Python运行时。

安装器协议仍为 **alpha0.1**，这是兼容现有状态/备份格式，不代表内容是旧r27。
候选内容基线：**r28-full-opt-candidate**；工程增量基线：**{INTEGRATION_BASELINE}**。
差分应用基线：**下列支持的原版SHA**，不是r27补丁文件，不支持覆盖任意旧汉化。

## 重要：先还原旧补丁

如已安装alpha0.1或任何其他补丁，必须先使用该旧补丁自己的安装器/备份还原至原版，再核对原版SHA。不要用本候选的还原功能处理旧版本记录：目标SHA不同，安装器会拒绝。
状态文件仍为`cosmobreeder-alpha0.1-state.json`，备份目录仍为`_cosmobreeder_alpha0.1_backup`。不要重命名、删除或手工覆盖旧备份/状态。已有状态或备份时本包不会绕过保护。

{supported}

原版普通档只包含JAR时安装器只应用JAR差分；含成人补丁PAK时必须两文件均匹配。请合法持有匹配原版；不要尝试对本候选目标或旧汉化重复打补丁。关闭游戏和Java后再由用户自行决定是否安装。

## 先做无安装payload校验

使用Python 3.12，在解压后包含`cosmobreeder_patch`目录的上一层运行：

```text
python -B -m cosmobreeder_patch --verify-payload
python -B -m cosmobreeder_patch --licenses
```

这两个命令不安装、不启动游戏。用户日后如要应用，可先用`--check --game-dir "游戏目录"`检查；实际安装/还原使用同一安装器的`--install`/`--uninstall`选项。本次制包**仅运行了--verify-payload**，未执行任何安装、还原或游戏命令。

## 目标及许可

{targets}

ZIP严格只包含两份源依赖CBDELTA1差分、未修改的安装器Python源码、许可/声明、此README和机读报告。完整JAR/PAK只在用户匹配原版上重建；文件级XOR差分可能较大，但不是完整游戏档。
现有[项目许可](<LICENSE>)、[原声明](<NOTICE>)和[第三方声明](<THIRD_PARTY_NOTICES.md>)逐字保留。额外原生8px中文贡献及其四组上游声明完整附在[许可目录](<licenses/fonts/native8/OFL.txt>)；见[候选补充声明](<licenses/r28-candidate-NOTICE.txt>)。许可证不重新授予原游戏素材的再分发权。

[制包验证与边界](<package-report.json>)记录完整七组件、源/目标/差分SHA、逐字节重建及staged payload校验。此报告不冒充实机验收。
'''


def package_candidate(candidate, output):
    candidate, cm, build_id, manifest_sha = validate_candidate(candidate)
    output = safe_path(output, must_exist=False)
    require(output.parent == ROOT / 'dist' and re.fullmatch('r28[A-Za-z0-9._-]*', output.name) is not None,
            'output必须是全新的dist/r28...直接子目录')
    require(not output.exists(), '输出目录已存在，拒绝覆盖；使用全新--output')
    require(not output.is_relative_to(candidate) and not candidate.is_relative_to(output), '输入输出不能重叠')
    for name in NAMES:
        source = safe_path(ROOT / 'backup' / name)
        require(source.is_file() and source.stat().st_size == SOURCE_SIZES[name] and sha(source) == SOURCE_PINS[name],
                'backup原版双SHA/尺寸验证失败: ' + name)
        with zipfile.ZipFile(candidate / name) as z:
            require(z.testzip() is None, '最终候选归档CRC失败: ' + name)
    text_files, text_pins = collect_text_inputs()
    acceptance_raw = safe_path(candidate / 'acceptance.json').read_bytes()
    acceptance_sha = sha256(acceptance_raw).hexdigest()
    acceptance = json.loads(acceptance_raw.decode('utf-8'))
    require(acceptance.get('status') == 'passed_cpu_and_independent_review_not_real_clip_CRT_input'
            and acceptance.get('archives') == {n: cm['archives'][n]['sha256'] for n in NAMES},
            'acceptance在制包前发生变化')
    # Nothing is written until the complete candidate, original pair and legal tree pass.
    output.mkdir()
    staged_root = output / 'staged'
    package = staged_root / 'cosmobreeder_patch'
    payload = package / 'payload'
    payload.mkdir(parents=True)
    checks = output / 'checks'
    checks.mkdir()
    for name, raw in text_files.items():
        dest = package / name
        dest.parent.mkdir(parents=True, exist_ok=True)
        dest.write_bytes(raw)
    extra_notice = 'licenses/r28-candidate-NOTICE.txt'
    (package / extra_notice).write_text(
        'r28 independent candidate supplement; alpha0.1 installer protocol retained.\n'
        'Additional native8 contribution: Fusion Pixel Font 2026.10.16, TakWolf, SIL OFL 1.1.\n'
        'Native8 BDF SHA256: 44a2d82b3dd782b505fa2297f10d8fd65499f9476d47b0331a22a133419b0ec3.\n'
        'Native12 BDF SHA256: b1e9a54fdd1c1e86fdc32efa16a04d8bd2897391ddb441238cee66947d6e3388.\n'
        'Native8 upstream notices: BoutiqueBitmap7x7/MisakiGothic, Galmuri, Misaki, Miseki Bitmap; full supplied texts retained.\n'
        'Some default10 added cells are nearest-sampled derivatives of native12, not native10.\n'
        'No standalone font, game ASCII atlas or original artwork is distributed here.\n'
        'Existing root notices and complete licenses/ remain unchanged; OFL does not relicense original game assets.\n', encoding='utf-8', newline='\n')
    m = {'version': 'alpha0.1', 'prerelease': True, 'candidate': True, 'baseline': BUILD_VERSION,
         'integration_baseline': INTEGRATION_BASELINE, 'source_baseline': 'supported-original-SHA256',
         'build_id': build_id, 'format': 'CBDELTA1-COPY-XOR', 'files': {},
         'game_started': False, 'installed': False, 'user_save_accessed': False,
         'real_clip_CRT_input_verified': False}
    proofs = {}
    for index, name in enumerate(NAMES):
        source, target = ROOT / 'backup' / name, candidate / name
        e = build(source, target, payload / (name + '.cbd'))
        e['delta'] = name + '.cbd'
        require(e['source_sha256'] == SOURCE_PINS[name] and e['target_sha256'] == cm['archives'][name]['sha256'],
                '源或候选在制差分期间变化')
        require(e['source_size'] == SOURCE_SIZES[name] and e['target_size'] == cm['archives'][name]['bytes'], '源/目标尺寸漂移')
        check = checks / f'target-reconstruction-{index}.bin'
        require(not check.exists(), '重建校验文件意外已存在')
        try:
            apply(source, payload / e['delta'], check, e)
            require(byte_equal(check, target), '差分重建与最终目标不逐字节相同')
            proofs[name] = {'sha256_equal': sha(check) == e['target_sha256'], 'byte_for_byte_equal': True}
        finally:
            # This NEW output owns this fixed temporary path; never clean user input.
            expected = output / 'checks' / f'target-reconstruction-{index}.bin'
            require(check.absolute() == expected and check.resolve().is_relative_to(output), '重建清理路径漂移')
            if check.exists():
                check.unlink()
        m['files'][name] = e
    dump(payload / 'manifest.json', m)
    verified = verify_staged(staged_root, payload, checks)
    (package / 'README.md').write_text(readme(build_id, m), encoding='utf-8', newline='\n')
    report = {'schema': 1, 'status': 'packaged_candidate_not_real_clip_CRT_input_acceptance',
              'build_id': build_id, 'installer_protocol': 'alpha0.1', 'candidate_baseline': BUILD_VERSION,
              'integration_baseline': INTEGRATION_BASELINE, 'source_baseline': 'supported-original-SHA256',
              'selected_components': sorted(COMPONENTS), 'full_component_set': True,
              'candidate_build_manifest_sha256': manifest_sha, 'base_archives': BASE_PINS,
              'files': m['files'], 'reconstruction': proofs, 'staged_verify_payload': verified,
              'installer_and_legal_source_sha256': text_pins, 'installer_source_unmodified': True,
              'game_started': False, 'installed': False, 'uninstalled': False, 'user_save_accessed': False,
              'real_clip_CRT_input_verified': False, 'exe_built': False,
              'zip_policy': 'exact allowlist: two deltas, installer Python source, full legal text, README, JSON reports; no complete game/archive/image/font binary',
              'cpu_runtime_test_report_consumed': False}
    report['acceptance_record_consumed'] = True
    report['acceptance_sha256'] = acceptance_sha
    (package / 'acceptance.json').write_bytes(acceptance_raw)
    dump(package / 'package-report.json', report)
    expected_rel = set(text_files) | {extra_notice, 'README.md', 'package-report.json', 'acceptance.json', 'payload/manifest.json'} | {'payload/' + n + '.cbd' for n in NAMES}
    actual_rel = {p.relative_to(package).as_posix() for p in package.rglob('*') if p.is_file()}
    require(actual_rel == expected_rel, 'staged包出现未允许文件（含pycache）')
    expected_members = {'cosmobreeder_patch/' + n for n in expected_rel}
    validate_zip_members(sorted(expected_members), expected_members)
    for name in NAMES:
        require(sha(ROOT / 'backup' / name) == SOURCE_PINS[name] and sha(candidate / name) == cm['archives'][name]['sha256'], '制包输入发生并发变化')
    require(sha(candidate / 'build-manifest.json') == manifest_sha, '构建清单发生并发变化')
    require(sha(candidate / 'acceptance.json') == acceptance_sha, '验收记录发生并发变化')
    archive = output / ZIP_NAME
    with zipfile.ZipFile(archive, 'x', zipfile.ZIP_DEFLATED, compresslevel=9) as z:
        for rel in sorted(expected_rel):
            z.write(package / rel, 'cosmobreeder_patch/' + rel)
    with zipfile.ZipFile(archive) as z:
        validate_zip_members(z.namelist(), expected_members)
        require(z.testzip() is None, '最终ZIP CRC验证失败')
        for rel in expected_rel:
            require(sha256(z.read('cosmobreeder_patch/' + rel)).hexdigest() == sha(package / rel), 'ZIP成员内容不匹配')
    checksum_files = sorted(p for p in output.rglob('*') if p.is_file())
    (output / 'SHA256SUMS').write_text(''.join(sha(p) + '  ' + p.relative_to(output).as_posix() + '\n' for p in checksum_files), encoding='utf-8', newline='\n')
    summary = {'status': report['status'], 'build_id': build_id, 'zip': archive.name,
               'zip_sha256': sha(archive), 'zip_bytes': archive.stat().st_size,
               'zip_member_count': len(expected_members), 'verify_payload': 'passed', 'reconstruction': proofs,
               'installed': False, 'game_started': False, 'user_save_accessed': False}
    return summary


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--candidate', type=Path, required=True)
    parser.add_argument('--output', type=Path, required=True)
    args = parser.parse_args()
    print(json.dumps(package_candidate(args.candidate, args.output), ensure_ascii=False, indent=2))


if __name__ == '__main__':
    main()
