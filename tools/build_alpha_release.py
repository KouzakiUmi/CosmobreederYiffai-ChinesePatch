"""Build release only from user-provided originals and existing r27 outputs."""
import argparse
import json
from pathlib import Path
import subprocess
import sys
import zipfile

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / 'src'))
from cosmobreeder_patch.delta import build, apply, sha
from cosmobreeder_patch.installer import NAMES

def main():
    p = argparse.ArgumentParser()
    p.add_argument('--source', type=Path, default=ROOT / 'backup')
    p.add_argument('--target', type=Path, default=ROOT / 'localization/builds/r27-story12-shaderfix-test5')
    p.add_argument('--output', type=Path, default=ROOT / 'dist/alpha0.1')
    p.add_argument('--exe', action='store_true')
    a = p.parse_args()
    if a.output.exists():
        raise ValueError('输出目录已存在，拒绝覆盖；请指定新的 --output')
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
    for notice in notices:
        shutil.copyfile(notice, a.output / notice.name)
    m = {'version': 'alpha0.1', 'prerelease': True, 'baseline': 'r27-story12-shaderfix-test5', 'format': 'CBDELTA1-COPY-XOR', 'files': {}}
    for n in NAMES:
        e = build(a.source / n, a.target / n, payload / (n + '.cbd'))
        e['delta'] = n + '.cbd'
        m['files'][n] = e
        check = a.output / (n + '.reconstruction-check')
        apply(a.source / n, payload / e['delta'], check, e)
        check.unlink()  # Only our newly created verification output.
    (payload / 'manifest.json').write_text(json.dumps(m, indent=2) + '\n', 'utf-8')
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
    if a.exe:
        work = ROOT / '.local/release-audit/delta-release/pyinstaller'
        notice_args = [arg for notice in notices for arg in ('--add-data', str(notice) + ':.')]
        subprocess.run([sys.executable, '-m', 'PyInstaller', '--noconfirm', '--onefile', *notice_args,
                        '--name', 'CosmobreederYiffai-alpha0.1-setup', '--paths', str(ROOT / 'src'),
                        '--add-data', str(payload.resolve()) + ':payload',
                        '--add-data', str(licenses.resolve()) + ':licenses', '--distpath', str(a.output.resolve()),
                        '--workpath', str(work / 'work'), '--specpath', str(work / 'spec'),
                        str(ROOT / 'src/cosmobreeder_patch/__main__.py')], check=True)
    lines = [sha(f) + '  ' + f.relative_to(a.output).as_posix() for f in sorted(a.output.rglob('*')) if f.is_file()]
    (a.output / 'SHA256SUMS').write_text('\n'.join(lines) + '\n', 'utf-8')
    print(json.dumps(m, indent=2))

if __name__ == '__main__':
    main()
