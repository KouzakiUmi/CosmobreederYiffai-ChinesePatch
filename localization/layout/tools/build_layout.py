"""Compile, test and assemble a NEW candidate from the frozen local r21.

No installation, game main, save IO, system PATH update or translation changes.
Every Java invocation is bounded and recorded. The actual game JRE performs the
headless tests/verification; the project-local JDK is only the build toolchain.
"""
from __future__ import annotations
import argparse
import hashlib
import json
import os
from pathlib import Path
import re
import shutil
import subprocess
import sys
import uuid
import zipfile

ROOT = Path(__file__).resolve().parents[3]
LOC = ROOT / 'localization'
LAYOUT = LOC / 'layout'
sys.path.insert(0, str(LOC / 'tools'))
from layout_bundle import apply_layout_bundle, read_layout_bundle
from layout_fonts import build_compact_font, validate_compact_font
from codec import decrypt_file

EXPORTS = ['--add-exports', 'java.base/jdk.internal.org.objectweb.asm=ALL-UNNAMED',
           '--add-exports', 'java.base/jdk.internal.org.objectweb.asm.tree=ALL-UNNAMED']


def sha(raw):
    return hashlib.sha256(raw).hexdigest()


def write_json(path, value):
    with path.open('x', encoding='utf-8', newline='\n') as output:
        json.dump(value, output, ensure_ascii=False, indent=2)
        output.write('\n')


def run(command, logs, name, cwd=ROOT):
    result = subprocess.run([str(arg) for arg in command], cwd=cwd,
                            stdout=subprocess.PIPE, stderr=subprocess.STDOUT,
                            encoding='utf-8', errors='replace', timeout=180)
    text = result.stdout
    (logs / (name + '.log')).write_text(text, encoding='utf-8')
    print(name, 'exit', result.returncode, text[-1600:], flush=True)
    if result.returncode:
        raise RuntimeError(name + ' failed; see ' + str(logs / (name + '.log')))
    return {'name': name, 'exit_code': result.returncode,
            'log_sha256': sha(text.encode('utf-8'))}


def verify_inputs():
    baseline = json.loads((LAYOUT / 'baseline.json').read_text(encoding='utf-8'))
    jar = ROOT / baseline['original_jar']
    if sha(jar.read_bytes()) != baseline['original_jar_sha256']:
        raise ValueError('Original local JAR identity changed')
    for name, expected in baseline['baseline_archives'].items():
        if sha((ROOT / baseline['baseline_build'] / name).read_bytes()) != expected:
            raise ValueError('Frozen r21 identity changed: ' + name)
    for name, expected in baseline['runtime_resources'].items():
        if sha((LOC / 'runtime' / name).read_bytes()) != expected:
            raise ValueError('Frozen font/license identity changed: ' + name)
    return baseline, jar


def build(output, jdk):
    output = output.resolve()
    allowed = (LOC / 'builds').resolve()
    if output == allowed or not output.is_relative_to(allowed) or output.exists():
        raise ValueError('Output must be a NEW child of localization/builds')
    destination = output
    baseline, original = verify_inputs()
    javac = jdk / 'bin/javac.exe'
    java = jdk / 'bin/java.exe'
    game_java = ROOT / 'research/testgame_cjk_verified/jre/bin/java.exe'
    for path in (javac, java, game_java):
        if not path.is_file(): raise ValueError('Missing Java tool: ' + str(path))
    work = LOC / 'work/layout-builds' / uuid.uuid4().hex
    work.mkdir(parents=True)
    # Assemble privately; publish only after ALL font/archive/final-JVM gates pass.
    output = work / 'candidate'
    logs = work / 'logs'; logs.mkdir()
    helpers = work / 'runtime'; helpers.mkdir()
    tests = work / 'tests'; tests.mkdir()
    tools = work / 'tools'; tools.mkdir()
    sources = sorted((LAYOUT / 'src').rglob('*.java'))
    test_sources = sorted((LAYOUT / 'tests').glob('*.java'))
    tool_sources = sorted((LAYOUT / 'tools/java').glob('*.java'))
    source_paths = [*sources, *test_sources, *tool_sources, LAYOUT/'baseline.json',
                    Path(__file__), LOC/'tools/layout_bundle.py', LOC/'tools/layout_fonts.py',
                    LOC/'tools/package.py']
    source_hashes = {str(p.relative_to(ROOT)).replace('\\', '/'): sha(p.read_bytes()) for p in source_paths}
    required = ['VsnLayout.java', 'SaveMenuLayout.java', 'ItemMenuLayout.java']
    if not set(required).issubset({p.name for p in sources}):
        raise ValueError('Not all P1 adapters have implementation sources')
    results = []
    results.append(run([javac, '-J-Dfile.encoding=UTF-8', '--release', '8', '-encoding', 'UTF-8',
                        '-Xlint:all', '-cp', original, '-d', helpers, *sources], logs, 'compile-runtime'))
    classpath = os.pathsep.join(map(str, (helpers, original)))
    results.append(run([javac, '-J-Dfile.encoding=UTF-8', *EXPORTS, '-encoding', 'UTF-8',
                        '-Xlint:all', '-cp', classpath, '-d', tools, *tool_sources], logs, 'compile-tools'))
    test_cp = os.pathsep.join(map(str, (helpers, tools, original)))
    results.append(run([javac, '-J-Dfile.encoding=UTF-8', *EXPORTS, '-encoding', 'UTF-8',
                        '-Xlint:all', '-cp', test_cp, '-d', tests, *test_sources], logs, 'compile-tests'))
    pins = work / 'pins.properties'
    pins.write_text(''.join(name + '=' + value + '\n' for name, value in sorted(baseline['target_classes'].items())),
                    encoding='ascii')
    patched = work / 'patched'
    results.append(run([java, '-Dfile.encoding=UTF-8', *EXPORTS, '-cp', test_cp,
                        'LayoutPatcher', original, patched, pins,
                        'BridgePatch,VsnPatch,SaveMenuPatch,ItemMenuPatch'], logs, 'patch-classes'))
    # Obfuscation includes both PRG/Iu and PRG/iu. Windows exploded classpaths
    # are case-insensitive: use a ZIP/JAR even for intermediate JVM verification.
    patched_archive = work / 'layout-patched.jar'
    with zipfile.ZipFile(patched_archive, 'w', zipfile.ZIP_DEFLATED) as archive:
        for path in sorted(patched.rglob('*.class')):
            archive.writestr(str(path.relative_to(patched)).replace('\\', '/'), path.read_bytes())
    baseline_jar = ROOT / baseline['baseline_build'] / 'cosmobreeder-multi.jar'
    baseline_pak = ROOT / baseline['baseline_build'] / 'patch.pak'
    vsn_fixtures = []
    for label, archive in [('nsfw', baseline_pak), ('sfw', baseline_jar)]:
        fixture = work / ('r21-' + label + '-ClassicPreTitle.txt')
        with zipfile.ZipFile(archive) as source_zip:
            fixture.write_bytes(decrypt_file(source_zip.read('vsn/5')))
        vsn_fixtures.append(fixture)
    for source in test_sources:
        text = source.read_text(encoding='utf-8')
        package = re.search(r'^package\s+([\w.]+)\s*;', text, re.M)
        name = (package.group(1) + '.' if package else '') + source.stem
        # Runtime parser/Unicode patch must be r21's real baseline, not vanilla afH.
        cp = os.pathsep.join(map(str, (tests, patched_archive, helpers, tools, baseline_jar)))
        arguments = {'SaveMenuLayoutTest': [original],
                     'ItemMenuLayoutTest': [original, helpers],
                     'VsnLayoutTest': ['--baseline', *vsn_fixtures, LOC/'runtime/bbc2.fnt']}.get(source.stem, [])
        results.append(run([game_java, '-Dfile.encoding=UTF-8', '-Xverify:all', *EXPORTS,
                            '-cp', cp, name, *arguments], logs, source.stem))
        if source.stem == 'SaveMenuLayoutTest':
            results.append(run([game_java, '-Dfile.encoding=UTF-8', '-Xverify:all',
                                '-Dcosmo.layout.save.prototype=true', *EXPORTS, '-cp', cp,
                                name, '--property-probe'], logs, 'save-property-activation'))
    # Resolve every runtime helper and target without game class initialization.
    names = sorted({str(p.relative_to(helpers)).replace('\\', '/')[:-6].replace('/', '.')
                    for p in helpers.rglob('*.class')} | {n.replace('/', '.') for n in baseline['target_classes']})
    names_path = work / 'verify-classes.txt'
    names_path.write_text('\n'.join(names) + '\n', encoding='utf-8')
    cp = os.pathsep.join(map(str, (patched_archive, helpers, tools, original)))
    results.append(run([game_java, '-Dfile.encoding=UTF-8', '-Xverify:all', '-cp', cp,
                        'VerifyLayout', names_path], logs, 'verify-patched-classes'))
    # Everything above must pass before the user-facing candidate directory exists.
    output.mkdir(parents=True)
    bundle = output / 'layout-bundle'; bundle.mkdir()
    classes = {}
    for base in (patched, helpers):
        for path in sorted(base.rglob('*.class')):
            entry = str(path.relative_to(base)).replace('\\', '/')
            if entry in classes: raise ValueError('Duplicate class output: ' + entry)
            raw = path.read_bytes()
            if int.from_bytes(raw[6:8], 'big') > 52: raise ValueError('Java8 runtime compatibility lost')
            target = bundle / 'classes' / entry
            target.parent.mkdir(parents=True, exist_ok=True)
            target.write_bytes(raw)
            classes[entry] = {'path': 'classes/' + entry, 'sha256': sha(raw)}
    font_dir = bundle / 'fonts'; font_dir.mkdir()
    sealed = {}
    for name in baseline['runtime_resources']:
        raw = (LOC / 'runtime' / name).read_bytes()
        (font_dir / name).write_bytes(raw)
        sealed['fonts/' + name] = sha(raw)
    compact_dir = bundle / 'compact10-candidate'
    build_compact_font(compact_dir)
    validate_compact_font(compact_dir)
    for path in sorted(compact_dir.iterdir()):
        if path.is_file(): sealed[str(path.relative_to(bundle)).replace('\\', '/')] = sha(path.read_bytes())
    bindings = {}
    for role, fnt, png in [('default', 'bbc2.fnt', 'bbc2-cjk-10.png'),
                           ('classic', 'classic.fnt', 'classic-cjk.png')]:
        bindings[role] = {'fnt_entry': fnt, 'fnt_sha256': baseline['runtime_resources'][fnt],
                          'png_sha256': baseline['runtime_resources'][png], 'runtime_png': png}
    for path in source_paths:
        key = str(path.relative_to(ROOT)).replace('\\', '/')
        if sha(path.read_bytes()) != source_hashes[key]:
            raise ValueError('Source changed while compiling/testing: ' + key)
    manifest = {'schema_version': 1, 'baseline_revision': baseline.get('baseline_revision', 1),
                'game_version': baseline['game_version'],
                'status': 'candidate_not_accepted', 'runtime_activation': 'explicit_candidate_profiles_only',
                'components': ['vsn-opening', 'save-single-card', 'item-selected-detail'],
                'original_classes': {n + '.class': value for n, value in baseline['target_classes'].items()},
                'classes': classes, 'font_bindings': bindings, 'sealed_resources': sealed,
                'source_sha256': source_hashes,
                'verification': results,
                'release_blockers': ['G3: actual content rectangles/clip/CRT and input/event regression not verified',
                                     'Item description overflow has no proven safe existing page input',
                                     'Non-target classic scenes remain at original 8px and are not accepted'],
                'compact10_registered': False, 'game_started': False, 'installed': False}
    write_json(bundle / 'layout-manifest.json', manifest)
    read_layout_bundle(bundle)
    build_dir = ROOT / baseline['baseline_build']
    baseline_jar = build_dir / 'cosmobreeder-multi.jar'
    with zipfile.ZipFile(baseline_jar) as source:
        replacements = {name: source.read(name) for name in ('bbc2.fnt', 'classic.fnt')}
        summary = apply_layout_bundle(source, replacements, bundle)
        candidate = output / 'cosmobreeder-multi.jar'
        with zipfile.ZipFile(candidate, 'w', zipfile.ZIP_DEFLATED, compresslevel=6) as target:
            for info in source.infolist():
                target.writestr(info, replacements.pop(info.filename, source.read(info.filename)))
            for name, raw in sorted(replacements.items()): target.writestr(name, raw)
    shutil.copyfile(build_dir / 'patch.pak', output / 'patch.pak')
    archive_records = []
    for name in ('cosmobreeder-multi.jar', 'patch.pak'):
        path = output / name
        with zipfile.ZipFile(path) as archive:
            if archive.testzip() is not None: raise ValueError('Candidate ZIP integrity failed')
        archive_records.append({'archive': name, 'sha256': sha(path.read_bytes()), 'bytes': path.stat().st_size})
    with zipfile.ZipFile(baseline_jar) as before, zipfile.ZipFile(output/'cosmobreeder-multi.jar') as after:
        changed = sorted(n for n in before.namelist() if before.read(n) != after.read(n))
        added = sorted(set(after.namelist()) - set(before.namelist()))
        if set(changed) != set(manifest['original_classes']): raise ValueError('Unexpected archive change set')
        if set(added) != set(classes) - set(manifest['original_classes']): raise ValueError('Unexpected helper entries')
    cp = os.pathsep.join(map(str, (output/'cosmobreeder-multi.jar', tools)))
    results.append(run([game_java, '-Dfile.encoding=UTF-8', '-Xverify:all', '-cp', cp,
                        'VerifyLayout', names_path], logs, 'verify-final-archive'))
    package = {'plan': {'source_installation_write': False, 'bitmap_redraw_included': True,
                         'layout_bundle': summary, 'status': 'candidate_not_accepted',
                         'baseline_build': baseline['baseline_build']},
               'archives': archive_records, 'changed_existing_entries': changed, 'added_entries': added,
               'font_and_art_unchanged': True, 'game_started': False, 'installed': False,
               'verification': results, 'work_logs': str(logs.relative_to(ROOT)).replace('\\', '/')}
    write_json(output / 'package-manifest.json', package)
    # Seal test logs in deliverable so evidence does not depend on a temporary path.
    shutil.copytree(logs, output / 'verification-logs')
    verify_inputs()
    for path in source_paths:
        key = str(path.relative_to(ROOT)).replace('\\', '/')
        if sha(path.read_bytes()) != source_hashes[key]:
            raise ValueError('Source changed before publish: ' + key)
    if destination.exists() or destination.resolve() != destination or not destination.resolve().is_relative_to(allowed):
        raise ValueError('Candidate destination changed before publish')
    destination.parent.mkdir(parents=True, exist_ok=True)
    print('Publish NEW candidate from', output.resolve(), 'to', destination.resolve(), flush=True)
    output.rename(destination)
    output = destination
    print(json.dumps({'candidate': str(output), 'status': package['plan']['status'],
                      'changed_classes': len(changed), 'helpers': len(added),
                      'game_started': False, 'installed': False}, ensure_ascii=False, indent=2))


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--output', type=Path, required=True)
    parser.add_argument('--jdk', type=Path, default=LOC/'toolchains/microsoft-jdk17/jdk-17.0.20.1+1')
    args = parser.parse_args()
    build(args.output, args.jdk.resolve())


if __name__ == '__main__':
    sys.stdout.reconfigure(encoding='utf-8')
    main()
