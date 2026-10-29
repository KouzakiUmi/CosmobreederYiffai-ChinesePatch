"""Focused candidate-census CLI contract check; no full-corpus rerun.
Uses the successful frozen run's CPU-only fonts/helpers and one actual HardFox
script, but recompiles the current test source into a new isolated directory.
"""
from pathlib import Path
import json
import hashlib
import os
import re
import subprocess
import uuid

ROOT = Path(__file__).resolve().parents[4]
HERE = Path(__file__).resolve().parent
BASE = HERE / 'run-b754944448e54c01a4905b9f6f9e7bd4'
JAR = ROOT / 'localization/builds/r27-story12-shaderfix-test5/cosmobreeder-multi.jar'
JDK = ROOT / 'localization/toolchains/microsoft-jdk17/jdk-17.0.20.1+1/bin'
JRE = ROOT / 'research/testgame_cjk_verified/jre/bin/java.exe'


def main():
    work = HERE / ('candidate-cli-' + uuid.uuid4().hex)
    work.mkdir()
    report = {'scope': 'candidate optional census CLI only, actual one-script parser/jo/arr fixture; no final candidate archive claim', 'steps': []}

    def run(label, args, expected=0, contains=None):
        p = subprocess.run([str(x) for x in args], cwd=ROOT, stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
        (work / (label + '.log')).write_bytes(p.stdout)
        report['steps'].append({'name': label, 'exit_code': p.returncode, 'expected_exit': expected, 'log': str((work / (label + '.log')).relative_to(ROOT))})
        assert p.returncode == expected, label
        if contains:
            assert contains.encode() in p.stdout, label

    cp = os.pathsep.join(map(str, [work, BASE / 'classes', JAR]))
    run('compile', [JDK / 'javac.exe', '--release', '8', '-encoding', 'UTF-8', '-cp', cp, '-d', work,
                    ROOT / 'localization/layout/tests/PatternSymbolsTest.java'])
    rows = (ROOT / 'docs/font-layout-audit-20261025/regressions/vsn.tsv').read_text('utf8').splitlines()
    row = next(r for r in rows if r.startswith('nsfw\tf_ClassicPigobinV3\t'))
    manifest = work / 'one-script.tsv'
    manifest.write_text(row + '\n', encoding='utf8')
    script = Path(row.split('\t')[2]).read_text('utf8')
    bodies = re.findall(r'^lang\((?:Fox|HardFox)\):\s?(.*)$', script, re.M)
    hc = sum(any(0x3400 <= ord(c) <= 0x9fff for c in b) for b in bodies)
    han = sum(0x3400 <= ord(c) <= 0x9fff for b in bodies for c in b)
    expected = work / 'expected.properties'
    expected.write_text(f'commands={len(bodies)}\nhan_commands={hc}\nhan={han}\n', encoding='utf8')
    command = [JRE, '-Xverify:all', '-Dfile.encoding=UTF-8', '-cp', cp, 'PatternSymbolsTest', manifest,
               BASE / 'fonts/dingbats.fnt', BASE / 'fonts/story12.fnt', BASE / 'fonts/bbc2.fnt']
    run('candidate-census-pass', command + [expected], contains='census=candidate-expected')
    mismatch = work / 'mismatch.properties'
    mismatch.write_text(f'commands={len(bodies) + 1}\nhan_commands={hc}\nhan={han}\n', encoding='utf8')
    run('candidate-census-reject', command + [mismatch], expected=1, contains='independent expected language census')
    missing = work / 'missing.properties'
    missing.write_text('commands=5\n', encoding='utf8')
    run('candidate-census-missing-reject', command + [missing], expected=1, contains='candidate census requires han_commands')
    exports = ['--add-exports', 'java.base/jdk.internal.org.objectweb.asm=ALL-UNNAMED',
               '--add-exports', 'java.base/jdk.internal.org.objectweb.asm.tree=ALL-UNNAMED']
    storycp = cp + os.pathsep + str(BASE / 'tools')
    run('story-compile', [JDK / 'javac.exe', *exports, '-encoding', 'UTF-8', '-cp', storycp, '-d', work,
                          ROOT / 'localization/layout/tests/StoryFont12Test.java'])
    story = [JRE, *exports, '-Xverify:all', '-Dfile.encoding=UTF-8', '-cp', storycp, 'StoryFont12Test', '--cpu', BASE / 'fonts']
    run('story-count-pass', story + ['2312'], contains='expected_native=2312')
    run('story-count-reject', story + ['2313'], expected=1, contains='expected 2313, got 2312')
    report['independent_expected_census'] = {'commands': len(bodies), 'han_commands': hc, 'han': han}
    report['test_source_sha256'] = {name: hashlib.sha256((ROOT / 'localization/layout/tests' / name).read_bytes()).hexdigest()
                                    for name in ['PatternSymbolsTest.java', 'StoryFont12Test.java']}
    report['success'] = True
    (work / 'results.json').write_text(json.dumps(report, ensure_ascii=False, indent=2) + '\n', encoding='utf8')
    print('PATTERN_CANDIDATE_CLI_OK', work.relative_to(ROOT))


if __name__ == '__main__':
    main()
