"""Isolated frozen-r27 Pattern CPU/pixel regression. Never install/start game.
Run with system Python 3.12 -B; writes only a NEW run-* directory beside this file.
No builder import, font regeneration, resource rewrite or shipped archive rewrite.
"""
from pathlib import Path
from io import BytesIO
import hashlib
import json
import os
import re
import subprocess
import sys
import uuid
import zipfile

ROOT = Path(__file__).resolve().parents[4]
HERE = Path(__file__).resolve().parent
JAR = ROOT / 'localization/builds/r27-story12-shaderfix-test5/cosmobreeder-multi.jar'
JDK = ROOT / 'localization/toolchains/microsoft-jdk17/jdk-17.0.20.1+1/bin'
JRE = ROOT / 'research/testgame_cjk_verified/jre/bin/java.exe'
EXPORTS = ['--add-exports', 'java.base/jdk.internal.org.objectweb.asm=ALL-UNNAMED',
           '--add-exports', 'java.base/jdk.internal.org.objectweb.asm.tree=ALL-UNNAMED']


def sha(data):
    return hashlib.sha256(data).hexdigest()


def main():
    from PIL import Image
    sys.path.insert(0, str(ROOT / 'localization/tools'))
    from codec import decrypt_file
    work = HERE / ('run-' + uuid.uuid4().hex)
    work.mkdir()
    classes = work / 'classes'
    tools = work / 'tools'
    fonts = work / 'fonts'
    for p in (classes, tools, fonts):
        p.mkdir()
    result = {'scope': 'frozen r27 isolated CPU and atlas pixels; no game, GL, deployment, installer or save IO',
              'archive_sha256': sha(JAR.read_bytes()), 'steps': [], 'work': str(work.relative_to(ROOT))}
    assert result['archive_sha256'] == 'dc6b0cedc3a3b2f6f51941a2cef449d33ec87d314ee64ea63495c3ffdebd06be'
    pak = JAR.with_name('patch.pak')
    result['pak_sha256'] = sha(pak.read_bytes())
    assert result['pak_sha256'] == 'd2e21deeb85d74e981770b247625ee7ceb7ed39ae566305c1833c2c3d97b54d5'
    manifest = ROOT / 'docs/font-layout-audit-20261025/regressions/vsn.tsv'
    fixture_count = 0
    with zipfile.ZipFile(JAR) as sfw, zipfile.ZipFile(pak) as nsfw:
        archives = {'sfw': sfw, 'nsfw': nsfw}
        indexes = {v: json.loads(decrypt_file(z.read('vsn/0'))) for v, z in archives.items()}
        for row in manifest.read_text('utf8').splitlines():
            variant, scene, path = row.split('\t')
            entry = 'vsn/' + str(indexes[variant]['/' + scene + '/script.vsn'])
            assert Path(path).read_bytes() == decrypt_file(archives[variant].read(entry)), ('fixture/archive drift', variant, scene)
            fixture_count += 1
    assert fixture_count == 106
    result['fixture_scripts_byte_identical_to_frozen_archives'] = fixture_count
    source_paths = [Path(__file__), ROOT / 'localization/layout/src/PRG/StoryFont12.java',
                    ROOT / 'localization/layout/src/PRG/PatternSymbols.java', ROOT / 'localization/layout/tests/PatternSymbolsTest.java',
                    ROOT / 'localization/layout/tools/java/StoryFont12Patch.java', ROOT / 'localization/layout/tests/StoryFont12Test.java']
    result['source_sha256'] = {str(p.relative_to(ROOT)).replace('\\', '/'): sha(p.read_bytes()) for p in source_paths}

    def run(name, args):
        args = [str(a) for a in args]
        p = subprocess.run(args, cwd=ROOT, stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
        log = work / (name + '.log')
        log.write_bytes(p.stdout)
        result['steps'].append({'name': name, 'exit_code': p.returncode, 'log': str(log.relative_to(ROOT)), 'command': args})
        (work / 'results.json').write_text(json.dumps(result, ensure_ascii=False, indent=2) + '\n', encoding='utf8')
        print(name, 'exit', p.returncode, flush=True)
        if p.returncode:
            raise RuntimeError('Inspect ' + str(log.relative_to(ROOT)))
        return p.stdout.decode('utf8')

    with zipfile.ZipFile(JAR) as z:
        for source, name in [('story12.fnt', 'story12.fnt'), ('dingbats.fnt', 'dingbats.fnt'),
                             ('bbc2.fnt', 'bbc2.fnt'), ('bbc2.fnt', 'bbc2-10px.fnt'), ('classic.fnt', 'classic.fnt')]:
            (fonts / name).write_bytes(z.read(source))
        index = json.loads(decrypt_file(z.read('dataq/0')))
        atlas = decrypt_file(z.read('dataq/' + str(index['/sprites.atlas']))).decode('utf8')
        block = re.search(r'(?m)^dingbats\r?\n(?:  [^\n]*\n)*', atlas)[0]
        x, y = map(int, re.search(r'xy: (\d+), (\d+)', block).groups())
        w, h = map(int, re.search(r'size: (\d+), (\d+)', block).groups())
        with Image.open(BytesIO(decrypt_file(z.read('dataq/' + str(index['/sprites.png']))))) as image:
            ding = image.convert('RGBA').crop((x, y, x + w, y + h))
        assert ding.size == (256, 128)
        palette = {}
        for line in z.read('dingbats.fnt').decode('utf8').splitlines():
            if not line.startswith('char '):
                continue
            f = {k: int(v) for k, v in re.findall(r'(\w+)=(-?\d+)', line)}
            if 33 <= f['id'] <= 126 or 160 <= f['id'] <= 255:
                pixels = list(ding.crop((f['x'], f['y'], f['x'] + f['width'], f['y'] + f['height'])).getdata())
                red = sum(r > 0 for r, g, b, a in pixels)
                alpha = sum(a > 0 for r, g, b, a in pixels)
                assert red > 0 and alpha > 0, ('empty original glyph', f['id'])
                assert (f['width'], f['height'], f['xadvance']) == (11, 12, 8)
                palette[str(f['id'])] = {'red_ink_pixels': red, 'alpha_ink_pixels': alpha}
        result['original_dingbats'] = {'fnt_sha256': sha(z.read('dingbats.fnt')), 'visible_legacy_glyphs': len(palette),
                                      'palette_glyphs': {str(cp): palette[str(cp)] for cp in list(range(65, 91)) + list(range(97, 123))},
                                      'all_preserved_legacy_glyphs_have_original_red_and_alpha_ink': True}
        result['story_png_sha256'] = sha(z.read('story12/bbc2-shared-story12.png'))
        assert result['story_png_sha256'] == '486935a160007265569428c871ce3f949fd1b3a1d68f3690ea7f6572276540bd'
    src = ROOT / 'localization/layout/src/PRG'
    tests = ROOT / 'localization/layout/tests'
    java_tools = ROOT / 'localization/layout/tools/java'
    run('compile-runtime', [JDK / 'javac.exe', '--release', '8', '-encoding', 'UTF-8', '-cp', JAR, '-d', classes,
                            src / 'StoryFont12.java', src / 'PatternSymbols.java'])
    cp = os.pathsep.join(map(str, [classes, JAR]))
    run('compile-tools', [JDK / 'javac.exe', *EXPORTS, '-encoding', 'UTF-8', '-cp', cp, '-d', tools,
                          java_tools / 'StoryFont12Patch.java', java_tools / 'BridgePatch.java'])
    run('compile-tests', [JDK / 'javac.exe', *EXPORTS, '-encoding', 'UTF-8', '-cp', cp + os.pathsep + str(tools), '-d', classes,
                          tests / 'PatternSymbolsTest.java', tests / 'StoryFont12Test.java'])
    cp += os.pathsep + str(tools)
    summary = run('pattern-cpu', [JRE, '-Dfile.encoding=UTF-8', '-Xverify:all', '-cp', cp, 'PatternSymbolsTest',
                                  ROOT / 'docs/font-layout-audit-20261025/regressions/vsn.tsv',
                                  fonts / 'dingbats.fnt', fonts / 'story12.fnt', fonts / 'bbc2.fnt'])
    result['pattern_summary'] = summary.strip()
    run('story12-cpu', [JRE, *EXPORTS, '-Dfile.encoding=UTF-8', '-Xverify:all', '-cp', cp, 'StoryFont12Test', '--cpu', fonts])
    run('original-patcher-preflight', [JDK / 'java.exe', *EXPORTS, '-Xverify:all', '-cp', cp, 'StoryFont12Test', '--preflight',
                                     ROOT / 'backup/cosmobreeder-multi.jar'])
    result['runtime_inventory'] = sorted(str(p.relative_to(classes)).replace('\\', '/') for p in (classes / 'PRG').glob('*.class'))
    assert result['runtime_inventory'] == ['PRG/PatternSymbols.class', 'PRG/StoryFont12$Font.class', 'PRG/StoryFont12$Metrics.class', 'PRG/StoryFont12.class']
    result['runtime_sha256'] = {n: sha((classes / n).read_bytes()) for n in result['runtime_inventory']}
    assert all(int.from_bytes((classes / n).read_bytes()[6:8], 'big') == 52 for n in result['runtime_inventory'])
    assert sha(JAR.read_bytes()) == result['archive_sha256'] and sha(pak.read_bytes()) == result['pak_sha256']
    assert result['source_sha256'] == {str(p.relative_to(ROOT)).replace('\\', '/'): sha(p.read_bytes()) for p in source_paths}, 'concurrent source drift'
    result['archive_and_source_pins_unchanged_after_tests'] = True
    (work / 'results.json').write_text(json.dumps(result, ensure_ascii=False, indent=2) + '\n', encoding='utf8')
    print('PATTERN_ALL_OK', work.relative_to(ROOT), flush=True)


if __name__ == '__main__':
    main()
