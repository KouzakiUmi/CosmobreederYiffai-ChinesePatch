"""Original alpha installer build: originals -> frozen targets -> delta/ZIP/EXE.

The original installer, GUI and alpha0.1 state protocol stay unchanged. r28
candidates additionally require their sealed acceptance and bundled font notices.
Never install or start the game. Existing output directories are never overwritten.
"""
import argparse
import json
import os
from pathlib import Path
import subprocess
import sys
import zipfile

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / 'src'))
from cosmobreeder_patch.delta import build, apply, sha
from cosmobreeder_patch.installer import NAMES, verify


def target_identity(target):
    """Retain the legacy default; bind r28 to its already-sealed final targets."""
    manifest = target / 'build-manifest.json'
    info = json.loads(manifest.read_text('utf-8')) if manifest.is_file() else {}
    candidate = target.name.startswith('r28') or info.get('version') == 'r28-full-opt-candidate'
    if not candidate:
        return {'baseline': target.name}, None
    acceptance = target / 'acceptance.json'
    if not acceptance.is_file():
        raise ValueError('r28目标缺少已通过的验收记录')
    record = json.loads(acceptance.read_text('utf-8'))
    actual = {n: sha(target / n) for n in NAMES}
    if (record.get('status') != 'passed_cpu_and_independent_review_not_real_clip_CRT_input'
            or record.get('archives') != actual
            or record.get('build_manifest_sha256') != sha(manifest)
            or info.get('full_component_set') is not True
            or info.get('version') != 'r28-full-opt-candidate'
            or info.get('status') != 'integrated_candidate_not_real_clip_CRT_input_acceptance'
            or any(info.get('archives', {}).get(n, {}).get('sha256') != actual[n] for n in NAMES)):
        raise ValueError('r28验收状态或目标SHA不匹配')
    return {'baseline': target.name, 'build_id': target.name, 'candidate': True,
            'integration_baseline': 'r27-story12-shaderfix-test5'}, acceptance


def native_font_notices(target):
    """Read complete notices from the accepted target, never copy font binaries."""
    sources = {'OFL8.txt': 'OFL.txt', 'NOTICE.txt': 'NOTICE.txt'}
    components = ('boutique-bitmap-7x7/OFL.txt', 'galmuri/LICENSE.txt',
                  'misaki/misaki.txt', 'miseki-bitmap/LICENSE.txt')
    sources.update({'LICENSES8/' + n: 'LICENSES/' + n for n in components})
    result = {}
    with zipfile.ZipFile(target / NAMES[0]) as z:
        for source, dest in sources.items():
            data = z.read('r28-font/' + source)
            data.decode('utf-8')
            result['fonts/native8/' + dest] = data
    return result


def exe_command(payload, licenses, notices, output):
    work = output.resolve() / 'build'
    notice_args = [arg for notice in notices for arg in ('--add-data', str(notice.resolve()) + ':.')]
    return [sys.executable, '-m', 'PyInstaller', '--noconfirm', '--onefile', '--noupx',
            '--python-option', 'X utf8', '--hide-console', 'hide-early', *notice_args,
            '--name', 'CosmobreederYiffai-alpha0.1-setup', '--paths', str(ROOT / 'src'),
            '--add-data', str(payload.resolve()) + ':payload',
            '--add-data', str(licenses.resolve()) + ':licenses', '--distpath', str(output.resolve()),
            '--workpath', str(work / 'work'), '--specpath', str(work / 'spec'),
            str(ROOT / 'src/cosmobreeder_patch/__main__.py')]


def main():
    p = argparse.ArgumentParser()
    p.add_argument('--source', type=Path, default=ROOT / 'backup')
    p.add_argument('--target', type=Path, default=ROOT / 'localization/builds/r27-story12-shaderfix-test5')
    p.add_argument('--output', type=Path, default=ROOT / 'dist/alpha0.1')
    p.add_argument('--exe', action='store_true')
    a = p.parse_args()
    if a.output.exists():
        raise ValueError('输出目录已存在，拒绝覆盖；请指定新的 --output')
    identity, acceptance = target_identity(a.target)
    extra_notices = native_font_notices(a.target) if acceptance else {}
    source_pins = {n: sha(a.source / n) for n in NAMES}
    target_pins = {n: sha(a.target / n) for n in NAMES}
    code_files = sorted((ROOT / 'src/cosmobreeder_patch').glob('*.py'))
    code_pins = {f.name: sha(f) for f in code_files}
    notices = [ROOT / name for name in ('LICENSE', 'NOTICE', 'THIRD_PARTY_NOTICES.md')]
    license_root = ROOT / 'licenses'
    required = ('fonts/OFL.txt', 'fonts/NOTICE.txt', 'fonts/LICENSES/ark-pixel/OFL.txt',
                'fonts/LICENSES/cubic-11/OFL.txt', 'fonts/LICENSES/galmuri/LICENSE.txt',
                'runtime/Python-LICENSE.txt', 'runtime/PyInstaller-COPYING.txt', 'runtime/Tk-license.terms', 'runtime/Tcl-license.terms')
    license_files = sorted(p for p in license_root.rglob('*') if p.is_file())
    for notice in notices + [license_root / n for n in required]:
        if not notice.is_file():
            raise ValueError('缺少必要许可证: ' + str(notice.relative_to(ROOT)))
    for notice in notices + license_files:
        if notice.is_symlink():
            raise ValueError('许可证不能为链接')
        notice.read_text('utf-8')  # Require the entire license tree to be text, not game assets.
    payload = a.output / 'payload'
    payload.mkdir(parents=True)
    licenses = a.output / 'licenses'
    import shutil
    shutil.copytree(license_root, licenses)
    for name, data in extra_notices.items():
        dest = licenses / name
        if dest.exists():
            raise ValueError('附加许可不能覆盖既有文件: ' + name)
        dest.parent.mkdir(parents=True, exist_ok=True)
        dest.write_bytes(data)
    if acceptance:
        shutil.copyfile(acceptance, a.output / 'acceptance.json')
    for notice in notices:
        shutil.copyfile(notice, a.output / notice.name)
    m = {'version': 'alpha0.1', 'prerelease': True, **identity, 'format': 'CBDELTA1-COPY-XOR', 'files': {}}
    report = {'builder_entry': 'tools/build_alpha_release.py', 'installer_protocol': 'alpha0.1',
              'baseline': identity['baseline'], 'source_sha256': source_pins,
              'target_sha256': target_pins, 'installer_source_sha256': code_pins,
              'native_font_notices': sorted(extra_notices), 'reconstruction': {}, 'checks': [],
              'installed': False, 'uninstalled': False, 'game_started': False, 'user_save_accessed': False}
    for n in NAMES:
        e = build(a.source / n, a.target / n, payload / (n + '.cbd'))
        e['delta'] = n + '.cbd'
        m['files'][n] = e
        check = a.output / (n + '.reconstruction-check')
        apply(a.source / n, payload / e['delta'], check, e)
        if sha(check) != target_pins[n] or check.read_bytes() != (a.target / n).read_bytes():
            raise ValueError('差分重建不等于冻结目标: ' + n)
        report['reconstruction'][n] = 'byte-for-byte-equal'
        expected = (a.output / (n + '.reconstruction-check')).absolute()
        if check.absolute() != expected or not check.resolve().is_relative_to(a.output.resolve()):
            raise ValueError('临时重建文件清理路径漂移')
        check.unlink()  # Only this new output's verified reconstruction file.
    (payload / 'manifest.json').write_text(json.dumps(m, indent=2) + '\n', 'utf-8', newline='\n')
    verify(payload)
    report['checks'].append({'name': 'original-installer-payload-verification', 'exit_code': 0})
    (a.output / 'README.md').write_text(
        '# 原补丁工具重制包\n\n'
        '参考FizRP重制图形界面，保留差分、备份／还原和alpha0.1状态协议；内容基线：`' + identity['baseline'] + '`。\n\n'
        '支持1.0.5_full：自动识别原版SFW档（仅JAR）与官方NSFW档（JAR+PAK），分别严格校验源SHA-256。未知源拒绝修改。\n'
        '界面沿用旧版自动查找：读取Steam安装位置与多库配置，检查安装器附近目录；支持手动选择。找到目录后校验原版／NSFW档位，不自动安装。\n'
        '界面提供载荷自检、后台操作与运行记录；双击隐藏控制台，命令行校验仍保留。\n'
        '已有旧补丁时，须先用旧补丁自己的安装器／备份还原原版，不能覆盖旧记录。\n'
        'EXE内置Python，无需另装Python；Python ZIP需要Python3.12。EXE未签名。\n'
        '本次仅构建和无安装验证，未执行真实安装／卸载、启动游戏或访问存档。\n\n'
        '无安装校验命令：\n```text\nCosmobreederYiffai-alpha0.1-setup.exe --verify-payload\n'
        'CosmobreederYiffai-alpha0.1-setup.exe --licenses\n```\n', encoding='utf-8')
    with zipfile.ZipFile(a.output / 'CosmobreederYiffai-alpha0.1-python.zip', 'w', zipfile.ZIP_DEFLATED) as z:
        for f in (ROOT / 'src/cosmobreeder_patch').glob('*.py'):
            z.write(f, 'cosmobreeder_patch/' + f.name)
        for f in payload.iterdir():
            z.write(f, 'cosmobreeder_patch/payload/' + f.name)
        for f in licenses.rglob('*'):
            if f.is_file():
                z.write(f, 'cosmobreeder_patch/licenses/' + f.relative_to(licenses).as_posix())
        for notice in notices:
            z.write(notice, 'cosmobreeder_patch/' + notice.name)
        for name in ('README.md', 'acceptance.json'):
            if (a.output / name).is_file():
                z.write(a.output / name, 'cosmobreeder_patch/' + name)
    if a.exe:
        work = a.output.resolve() / 'build'
        (work / 'spec').mkdir(parents=True)
        env = dict(os.environ, PYINSTALLER_CONFIG_DIR=str(work / 'cache'), PYTHONDONTWRITEBYTECODE='1')
        env.pop('PYTHONPATH', None)
        with open(work / 'pyinstaller.log', 'wb') as log:
            subprocess.run(exe_command(payload, licenses, notices, a.output), cwd=ROOT,
                           env=env, stdout=log, stderr=subprocess.STDOUT, check=True)
        exe = (a.output / 'CosmobreederYiffai-alpha0.1-setup.exe').resolve()
        env['PATH'] = str(Path(os.environ.get('SystemRoot', 'C:/Windows')) / 'System32')
        for key in ('PYTHONPATH', 'PYTHONHOME', 'PYTHONUTF8', 'PYTHONIOENCODING'):
            env.pop(key, None)
        for action in ('--verify-payload', '--licenses'):
            result = subprocess.run([str(exe), action], cwd=work, env=env, capture_output=True, check=True)
            (work / (action[2:] + '.stdout.txt')).write_bytes(result.stdout)
            (work / (action[2:] + '.stderr.txt')).write_bytes(result.stderr)
            text = result.stdout.decode('utf-8').replace('\r\n', '\n')
            if action == '--verify-payload':
                if json.loads(text) != {'version': 'alpha0.1', 'status': 'verified', 'game_started': False}:
                    raise ValueError('原安装器EXE负载验证返回异常')
            else:
                for path in notices + sorted(p for p in licenses.rglob('*') if p.is_file()):
                    key = path.name if path in notices else path.relative_to(a.output).as_posix()
                    if key not in text or path.read_text('utf-8') not in text:
                        raise ValueError('原安装器EXE许可显示不完整: ' + key)
            report['checks'].append({'name': action, 'exit_code': result.returncode})
        report['exe_sha256'] = sha(exe)
        report['exe_name'] = exe.name
    if any(sha(a.source / n) != source_pins[n] or sha(a.target / n) != target_pins[n] for n in NAMES):
        raise ValueError('构建源或冻结目标发生变化')
    if any(sha(f) != code_pins[f.name] for f in code_files):
        raise ValueError('原安装器源码发生变化')
    report.update(status='passed-original-tool-build-no-install', installer_source_unmodified=True)
    (a.output / 'build-report.json').write_text(json.dumps(report, ensure_ascii=False, indent=2) + '\n', encoding='utf-8')
    lines = [sha(f) + '  ' + f.relative_to(a.output).as_posix() for f in sorted(a.output.rglob('*')) if f.is_file()]
    (a.output / 'SHA256SUMS').write_text('\n'.join(lines) + '\n', 'utf-8', newline='\n')
    print(json.dumps(m, indent=2))

if __name__ == '__main__':
    main()
