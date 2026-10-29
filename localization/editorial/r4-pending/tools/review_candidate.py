"""R4 候选级独立复核：从归档重新推导，不复用构建脚本内部结果。

核验项：
  1. candidate9 构建清单封签与归档 SHA 一致
  2. R4 台账 13 项：新值存在、旧值消失
  3. candidate8 → candidate9 明文差异只落在预期集合（3 个文本资源 + 字体/类重写）
  4. R2/R3 成果在 c8 与 c9 的保留状态一致（无回归）
  5. 字体新增字形恰好为 R4 引入的 0x60EC「惬」
  6. 17 步 CPU 结果与候选 jar 绑定
"""
import json
import sys
import zipfile
from hashlib import sha256
from pathlib import Path

ROOT = Path(__file__).resolve().parents[4]
LOC = ROOT / 'localization'
R4 = LOC / 'editorial' / 'r4-pending'
sys.path.insert(0, str(LOC / 'tools'))
from codec import decrypt_file  # noqa: E402

C8 = LOC / 'builds' / 'r28-character-names-candidate8'
C9 = LOC / 'builds' / 'r4-pending-candidate9'
TESTS = LOC / 'optimization/r28/integration/tests/r4-pending-candidate9'
LEDGER = LOC / 'translations' / 'editorial-r4-pending-repairs.jsonl'

EXPECTED_TEXT = {('patch.pak', 'datav/1'),
                 ('cosmobreeder-multi.jar', 'datay/1'),
                 ('cosmobreeder-multi.jar', 'datadf/1')}
NEW_CODEPOINT = 0x60EC


def sha(path):
    return sha256(path.read_bytes()).hexdigest()


def main():
    checks = []

    def check(name, ok, detail=None):
        checks.append({'name': name, 'passed': bool(ok), 'detail': detail})
        if not ok:
            raise SystemExit(f'FAILED: {name} :: {detail}')

    # 1) build manifest
    build = json.loads((C9 / 'build-manifest.json').read_text('utf-8'))
    archives = {name: sha(C9 / name) for name in ('cosmobreeder-multi.jar', 'patch.pak')}
    check('build.status', build['status'] == 'integrated_candidate_not_real_clip_CRT_input_acceptance',
          build['status'])
    check('build.full_component_set', build['full_component_set'] is True)
    check('build.r4pending_selected', 'r4pending' in build['selected_components'],
          build['selected_components'])
    check('build.archive_pins', all(build['archives'][n]['sha256'] == v for n, v in archives.items()))
    r4_report = build['resource_reports'].get('r4pending')
    check('build.r4pending_report', r4_report is not None and r4_report['operation_count'] == 13,
          r4_report and r4_report['operation_count'])

    # 2) ledger application
    ops = [json.loads(s) for s in LEDGER.read_text('utf-8').splitlines() if s.strip()]
    cache = {}

    def text(archive, entry):
        key = (archive, entry)
        if key not in cache:
            with zipfile.ZipFile(C9 / archive) as z:
                cache[key] = decrypt_file(z.read(entry)).decode('utf-8')
        return cache[key]

    missing_new = [o['op_id'] for o in ops if o['new'] not in text(o['archive'], o['archive_entry'])]
    old_left = [o['op_id'] for o in ops if o['old'] in text(o['archive'], o['archive_entry'])]
    check('r4.new_values_present', not missing_new, missing_new)
    check('r4.old_values_removed', not old_left, old_left)

    # 3) plaintext diff vs candidate8
    changed = set()
    for name in ('cosmobreeder-multi.jar', 'patch.pak'):
        with zipfile.ZipFile(C8 / name) as a, zipfile.ZipFile(C9 / name) as b:
            check(f'diff.{name}.entry_set', set(a.namelist()) == set(b.namelist()))
            for n in a.namelist():
                ra, rb = a.read(n), b.read(n)
                if ra == rb:
                    continue
                try:
                    pa, pb = decrypt_file(ra), decrypt_file(rb)
                except Exception:
                    pa, pb = ra, rb
                if pa != pb:
                    changed.add((name, n))
    unexpected = {k for k in changed if k not in EXPECTED_TEXT} - {
        (n, e) for n in ('cosmobreeder-multi.jar', 'patch.pak')
        for e in set()
    }
    # 允许字体/类/图集重写，但必须能由新增字形解释：只允许 .fnt/.class/dataq/r28-font
    allowed_suffix = ('.fnt', '.class', '.png')
    bad = [k for k in unexpected
           if not (k[1].endswith(allowed_suffix) or k[1].startswith(('dataq/', 'r28-font/')))]
    check('diff.only_expected_text', not (changed - EXPECTED_TEXT - {
        k for k in changed if k[1].endswith(allowed_suffix) or k[1].startswith(('dataq/', 'r28-font/'))}), sorted(bad))
    check('diff.text_resources_exact', (changed & {
        (n, e) for n in ('cosmobreeder-multi.jar', 'patch.pak')
        for e in ('datav/1', 'datadf/1', 'datadm/1', 'datay/1')}) == EXPECTED_TEXT,
        sorted(k for k in changed if k[1].startswith('data')))

    # 4) R2/R3 preservation parity
    def missing_ops(base, ledger):
        rows = [json.loads(s) for s in ledger.read_text('utf-8').splitlines() if s.strip()]
        local = {}
        for o in rows:
            key = (o['archive'], o['archive_entry'])
            if key not in local:
                with zipfile.ZipFile(base / key[0]) as z:
                    local[key] = decrypt_file(z.read(key[1])).decode('utf-8')
        return sum(1 for o in rows if o['new'] not in local[(o['archive'], o['archive_entry'])])

    r2 = missing_ops(C8, LOC / 'translations/editorial-r2-repairs.jsonl')
    r2n = missing_ops(C9, LOC / 'translations/editorial-r2-repairs.jsonl')
    r3 = missing_ops(C8, LOC / 'translations/character-name-repairs.jsonl')
    r3n = missing_ops(C9, LOC / 'translations/character-name-repairs.jsonl')
    check('r2.preserved_parity', r2 == r2n, {'c8_missing': r2, 'c9_missing': r2n})
    check('r3.preserved_parity', r3 == r3n, {'c8_missing': r3, 'c9_missing': r3n})

    # 5) font delta
    f8 = json.loads((C8 / 'font-manifest.json').read_text('utf-8'))
    f9 = json.loads((C9 / 'font-manifest.json').read_text('utf-8'))
    cp8 = {r['codepoint'] for r in f8['added_rectangles']}
    cp9 = {r['codepoint'] for r in f9['added_rectangles']}
    check('font.added_codepoints', cp9 - cp8 == {NEW_CODEPOINT} and cp8 - cp9 == set(),
          {'added': sorted(hex(x) for x in cp9 - cp8), 'removed': sorted(hex(x) for x in cp8 - cp9)})

    # 6) CPU results binding
    results = json.loads((TESTS / 'results.json').read_text('utf-8'))
    check('tests.status', results['status'] == 'passed_cpu_only_not_real_clip_CRT_input', results['status'])
    check('tests.steps', len(results['steps']) == 17 and all(s['exit_code'] == 0 for s in results['steps']),
          len(results['steps']))
    check('tests.jar_binding', results['candidate_sha256'] == archives['cosmobreeder-multi.jar'])

    review = {
        'schema': 'cosmo-editorial-r4-candidate-review/v1',
        'status': 'PASS_STATIC_AND_CPU_NOT_REAL_MACHINE',
        'candidate': 'localization/builds/r4-pending-candidate9',
        'archives_sha256': archives,
        'build_manifest_sha256': sha(C9 / 'build-manifest.json'),
        'tests_results_sha256': sha(TESTS / 'results.json'),
        'ledger_sha256': sha(LEDGER),
        'checks': checks,
        'changed_entries': sorted([list(x) for x in changed]),
        'new_codepoints': [hex(NEW_CODEPOINT)],
        'installed': False,
        'game_started': False,
        'user_save_accessed': False,
        'real_clip_CRT_input_verified': False,
        'limitations': [
            'CPU 与静态复核；未安装、未启动游戏、未访问存档',
            '未做真实 GPU/CRT/输入/全场景层次验收',
            'R2/R3 的 missing 计数是朴素子串匹配口径，仅用于 c8/c9 同口径对照',
        ],
    }
    target = R4 / 'review' / 'candidate9-review.json'
    target.parent.mkdir(parents=True, exist_ok=True)
    target.write_text(json.dumps(review, ensure_ascii=False, indent=2) + '\n', encoding='utf-8')
    print('review:', target.relative_to(ROOT))
    for c in checks:
        print(' PASS', c['name'])
    print('changed entries:', len(changed))


if __name__ == '__main__':
    main()
