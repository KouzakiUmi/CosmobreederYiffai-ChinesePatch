"""Run actual frozen-r27 parser/layout regression in this component's directory."""
from pathlib import Path
import hashlib
import json
import os
import subprocess
import sys
import zipfile

HERE = Path(__file__).resolve().parent
ROOT = HERE.parents[3]
LOC = ROOT / 'localization'
sys.path.insert(0, str(LOC / 'tools'))
from codec import decrypt_file
from vsn_joins import rewrite_vsn, _load, sha


def run(command, log):
    with log.open('wb') as out:
        result = subprocess.run([str(x) for x in command], cwd=ROOT, stdout=out, stderr=subprocess.STDOUT)
    print(log.name, 'exit', result.returncode)
    if result.returncode:
        raise RuntimeError('Integration failed; inspect ' + str(log))


def main():
    manifest, _ = _load()
    build = LOC / 'builds/r27-story12-shaderfix-test5'
    work = HERE / 'integration'
    work.mkdir(exist_ok=True)
    classes = work / 'classes'; classes.mkdir(exist_ok=True)
    jdk = LOC / 'toolchains/microsoft-jdk17/jdk-17.0.20.1+1/bin'
    jar = build / 'cosmobreeder-multi.jar'
    # JDK java is a fixture JVM, not the game's executable/entry point.
    java = jdk / 'java.exe'
    reports, rows = [], []
    with zipfile.ZipFile(build / 'patch.pak') as z:
        assert sha((build / 'patch.pak').read_bytes()) == manifest['frozen_archive_sha256']
        for path, pin in manifest['resources'].items():
            old = decrypt_file(z.read(pin['archive_entry']))
            new, report = rewrite_vsn(path, old)
            name = path.split('/')[1]
            before = work / (name + '-before.vsn')
            after = work / (name + '-after.vsn')
            before.write_bytes(old); after.write_bytes(new)
            rows.append('\t'.join([name, str(before), str(after)]))
            reports.append(report)
    tsv = work / 'inputs.tsv'; tsv.write_text('\n'.join(rows)+'\n', 'utf8')
    run([jdk/'javac.exe', '-J-Duser.language=en', '-J-Duser.country=US', '-J-Dfile.encoding=UTF-8', '-encoding', 'UTF-8', '-cp', jar, '-d', classes,
         HERE/'VsnRuntimeAssertions.java', HERE/'VsnJoinIntegrationTest.java'], work/'compile.log')
    run([java, '-Xverify:all', '-cp', str(classes)+os.pathsep+str(jar), 'VsnJoinIntegrationTest',
         LOC/'runtime/bbc2.fnt', tsv], work/'parser-layout.log')
    text = (work/'parser-layout.log').read_text('utf8')
    assert 'PASS VSN joins r27 parser integration:' in text
    summary = {'status': 'passed', 'scope': 'isolated actual r27 JVM parser/layout, not game/GL/clip/CRT',
               'jdk_java': str(java.relative_to(ROOT)), 'input_jar': str(jar.relative_to(ROOT)),
               'input_jar_sha256': sha(jar.read_bytes()), 'applied_groups': sum(r['applied_groups'] for r in reports),
               'removed_text_nodes': sum(r['removed_text_nodes'] for r in reports),
               'automatic_delay_delta_seconds': 0, 'result': text.strip(),
               'resources': reports}
    (HERE/'integration-report.json').write_text(json.dumps(summary, ensure_ascii=False, indent=2)+'\n', 'utf8')
    print(text.strip())

if __name__ == '__main__': main()
