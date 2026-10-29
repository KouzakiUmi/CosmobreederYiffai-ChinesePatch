"""生成 R4 组件构建门禁（build-gate.json）。

门禁记录：台账哈希、裁决表哈希、证据哈希、独立核验结果，以及对锚定基线
（candidate8）的资源做一次真实引擎 dry-run 的结果。
构建时 build_candidate.py 会重算并比对，任何漂移即拒绝。
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
import editorial_repairs as engine  # noqa: E402

CAND = LOC / 'builds' / 'r28-character-names-candidate8'
LEDGER = LOC / 'translations' / 'editorial-r4-pending-repairs.jsonl'
DECISIONS = R4 / 'reports' / 'pending-01' / 'decisions.tsv'
EVIDENCE = R4 / 'evidence' / 'runtime-evidence.json'


def sha(path):
    return sha256(path.read_bytes()).hexdigest()


def main():
    # 台账与裁决表必须已由 build_decisions.py 生成
    for required in (LEDGER, DECISIONS, EVIDENCE):
        if not required.exists():
            raise SystemExit(f'missing prerequisite: {required.relative_to(ROOT)}')

    records = [json.loads(s) for s in LEDGER.read_text('utf-8').splitlines() if s.strip()]
    acc = json.loads((CAND / 'acceptance.json').read_text('utf-8'))
    archives = {name: zipfile.ZipFile(CAND / name) for name in acc['archives']}

    entries = {}
    for op in records:
        key = (op['archive'], op['archive_entry'])
        if key not in entries:
            entries[key] = decrypt_file(archives[key[0]].read(key[1]))
    out, reports = engine.apply_entries(entries, records)
    if set(out) != set(entries):
        raise SystemExit('dry-run produced unexpected entry set')
    for op in records:
        text = out[(op['archive'], op['archive_entry'])].decode('utf-8')
        if op['new'] not in text:
            raise SystemExit(f"dry-run missing new value: {op['op_id']}")

    # 每条 apply 的 finding 必须在裁决表中标为 apply
    rows = [l.split('\t') for l in DECISIONS.read_text('utf-8').splitlines() if l.strip()][1:]
    disposition = {r[0]: r[1] for r in rows}
    apply_findings = sorted({op['finding_ids'][0] for op in records})
    bad = [f for f in apply_findings if disposition.get(f) != 'apply']
    if bad:
        raise SystemExit(f'findings not marked apply: {bad}')

    gate = {
        'schema': 'cosmo-editorial-r4-build-gate/v1',
        'status': 'verified_for_application',
        'scope': 'R2 deferred items only; not a full proofread or real-machine acceptance',
        'decisions_total': len(rows),
        'apply_findings': apply_findings,
        'operations': len(records),
        'ledger_sha256': sha(LEDGER),
        'decisions_sha256': sha(DECISIONS),
        'evidence_sha256': sha(EVIDENCE),
        'verifier': {
            'path': 'localization/editorial/r4-pending/tools/verify_decisions.py',
            'sha256': sha(R4 / 'tools' / 'verify_decisions.py'),
        },
        'dry_run': {
            'engine': 'localization/tools/editorial_repairs.py:apply_entries',
            'base_candidate': 'localization/builds/r28-character-names-candidate8',
            'base_archives_sha256': acc['archives'],
            'operations_applied': sum(len(r['operations_applied']) for r in reports),
            'resources': reports,
        },
        'required_chars': sorted({c for op in records for c in op['new'] if ord(c) > 0x7F}),
        'not_installed': True,
        'game_started': False,
    }
    target = R4 / 'reports' / 'pending-01' / 'build-gate.json'
    target.write_text(json.dumps(gate, ensure_ascii=False, indent=2) + '\n', encoding='utf-8')
    print('gate:', target.relative_to(ROOT))
    print('operations:', gate['operations'], 'apply findings:', len(apply_findings))
    print('required chars:', ''.join(gate['required_chars'])[:60])
    for r in reports:
        print(' apply', r['archive'], r['archive_entry'], 'targets', r['targets_changed'])


if __name__ == '__main__':
    main()
