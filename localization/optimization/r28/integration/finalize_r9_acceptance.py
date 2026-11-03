"""Seal an R9 candidate: bind the archives, the regression run and every batch gate.

`finalize_acceptance.py` seals the r28 full-opt candidates and pins the review
records of that round (resource review, font review, method whitelist). Those
records name specific archive digests, so they cannot be reused for a later
candidate — this is the R9 equivalent, and it checks what R9 actually has:
the 17-step CPU run, the 34 per-batch gates and the plaintext read-back.

Writes `acceptance.json` next to the archives. Never installs and never starts
the game. Refuses to overwrite an existing record.
"""
from pathlib import Path
from hashlib import sha256
import argparse
import json
import subprocess
import sys

ROOT = Path(__file__).resolve().parents[4]
R9 = ROOT / 'localization/editorial/r9-polish'
INTEGRATION = ROOT / 'localization/optimization/r28/integration'
NAMES = ('cosmobreeder-multi.jar', 'patch.pak')


def sha(path):
    return sha256(Path(path).read_bytes()).hexdigest()


def run(args, cwd=None):
    result = subprocess.run([sys.executable] + args, capture_output=True, text=True, cwd=str(cwd or ROOT))
    return result.returncode, (result.stdout or '') + (result.stderr or '')


def main():
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument('--candidate', required=True, help='candidate directory under localization/builds')
    ap.add_argument('--tests', required=True, help='test directory under integration/tests')
    a = ap.parse_args()

    candidate = (ROOT / 'localization/builds' / a.candidate).resolve()
    testdir = (INTEGRATION / 'tests' / a.tests).resolve()
    if not candidate.is_relative_to(ROOT / 'localization/builds'):
        raise SystemExit('candidate must live under localization/builds')
    if not testdir.is_relative_to(INTEGRATION / 'tests'):
        raise SystemExit('tests must live under integration/tests')
    record_path = candidate / 'acceptance.json'
    if record_path.exists():
        raise SystemExit('new acceptance record only: %s already exists' % record_path.name)

    build = json.loads((candidate / 'build-manifest.json').read_text('utf8'))
    if build.get('full_component_set') is not True:
        raise SystemExit('not a full integrated candidate')
    if build.get('status') != 'integrated_candidate_not_real_clip_CRT_input_acceptance':
        raise SystemExit('unexpected manifest status: %s' % build.get('status'))
    if build.get('version') != 'r28-full-opt-candidate':
        raise SystemExit('unexpected manifest version: %s' % build.get('version'))
    if build.get('game_started') or build.get('user_save_accessed'):
        raise SystemExit('manifest records game/save access')

    archives = {name: sha(candidate / name) for name in NAMES}
    for name, digest in archives.items():
        if build['archives'][name]['sha256'] != digest:
            raise SystemExit('candidate archive changed since build: %s' % name)

    tests = json.loads((testdir / 'results.json').read_text('utf8'))
    if tests.get('status') != 'passed_cpu_only_not_real_clip_CRT_input':
        raise SystemExit('tests did not pass: %s' % tests.get('status'))
    if len(tests.get('steps') or []) != 17 or any(s.get('exit_code') for s in tests['steps']):
        raise SystemExit('the 17-step CPU suite must pass')
    if tests.get('candidate_sha256') != archives['cosmobreeder-multi.jar']:
        raise SystemExit('tests were not run against this jar')
    if not tests.get('test_sources_unchanged_after_run'):
        raise SystemExit('test sources changed during the run')
    if tests.get('game_started') or tests.get('user_save_accessed'):
        raise SystemExit('tests record game/save access')

    component = json.loads((ROOT / 'localization/optimization/r28/r9polish/component.json').read_text('utf8'))
    gates = []
    for batch in component['batches']:
        gate_path = ROOT / batch['gate']
        gate = json.loads(gate_path.read_text('utf8'))
        if gate.get('status') != 'verified_for_application':
            raise SystemExit('%s gate is not verified' % batch['batch'])
        if gate.get('ledger_sha256') != sha(ROOT / batch['ledger']) or gate.get('decisions_sha256') != sha(ROOT / batch['decisions']):
            raise SystemExit('%s ledger/decisions changed after the gate' % batch['batch'])
        gates.append({'batch': batch['batch'], 'operations': gate['operations'],
                      'base_candidate': Path(gate['base_candidate']).name,
                      'ledger_sha256': gate['ledger_sha256'], 'decisions_sha256': gate['decisions_sha256']})

    code, output = run(['tools/verify_readback.py', a.candidate], cwd=R9)
    if code != 0:
        raise SystemExit('read-back failed: ' + output[-300:])
    readback = json.loads(output[output.index('{'):])

    record = {
        'status': 'passed_cpu_and_independent_review_not_real_clip_CRT_input',
        'candidate': a.candidate,
        'archives': archives,
        'build_manifest_sha256': sha(candidate / 'build-manifest.json'),
        'component': {'path': 'localization/optimization/r28/r9polish/component.json',
                      'sha256': sha(ROOT / 'localization/optimization/r28/r9polish/component.json'),
                      'batches': len(gates)},
        'gates': gates,
        'readback': {'operations_checked': readback['operations_checked'],
                     'locations': readback['locations'],
                     'operations_superseded': readback['operations_superseded'],
                     'problem_count': readback['problem_count']},
        'cpu_regression': {'tests': a.tests, 'steps': len(tests['steps']),
                           'status': tests['status'], 'results_sha256': sha(testdir / 'results.json')},
        'independent_review': {
            'note': '每批都有独立的第二路读者或核验：batch-15 由 Grok 复核发现 9 处误报（LIGHTTAZER／space suit），'
                    'batch-14 由 DS 与 Grok 两路分别精校后交叉裁决。核验范围是文本与结构，不含实机。'},
        'not_verified': ['游戏安装', '游戏启动', 'GPU/CRT/裁剪渲染', '存档读写', '4 张位图的本地化'],
        'game_started': False,
        'user_save_accessed': False,
    }
    record_path.write_text(json.dumps(record, ensure_ascii=False, indent=1) + '\n', encoding='utf8')
    print(json.dumps({'acceptance': str(record_path), 'status': record['status'],
                      'archives': archives, 'batches': len(gates),
                      'operations_checked': readback['operations_checked']}, ensure_ascii=False, indent=1))


if __name__ == '__main__':
    main()
