"""Bind r9 decisions to the ledger and emit the build gate.

Cross-checks decisions.tsv, the source-locked ledger and the batch order, then
re-runs the pure-byte dry run against the base candidate. Writes only the gate
JSON under r9-polish/batch-NN/review.
"""
from pathlib import Path
from hashlib import sha256
import argparse
import json
import re
import sys
import zipfile

ROOT = Path(__file__).resolve().parents[4]
LOC = ROOT / 'localization'
sys.path.insert(0, str(LOC / 'tools'))
from codec import decrypt_file
from editorial_repairs import apply_entries
sys.path.insert(0, str(Path(__file__).resolve().parent))
import r9_targets as targets  # noqa: E402
from text_rules import effective_final  # noqa: E402  (shared with the ledger builder)

SNAPSHOT_BASE = {
    'snapshot-02': 'r8-puzzle-candidate12',
    'snapshot-03': 'r9-polish-candidate13',
}
R9 = LOC / 'editorial/r9-polish'
MODE_ARCHIVE = {'sfw': 'cosmobreeder-multi.jar', 'nsfw': 'patch.pak'}
COLUMNS = ('finding_id', 'route', 'severity', 'category', 'scene_id', 'row_id',
           'decision', 'final_zh', 'reason')


def file_sha(path):
    return sha256(path.read_bytes()).hexdigest()


def load_decisions(path):
    header, rows = None, []
    for n, line in enumerate(path.read_text('utf8').splitlines(), 1):
        if not line.strip():
            continue
        cells = line.split('\t')
        if header is None:
            header = cells
            if tuple(header) != COLUMNS:
                raise ValueError('decisions header mismatch: %s' % header)
            continue
        if len(cells) != len(COLUMNS):
            raise ValueError('decisions line %d has %d columns' % (n, len(cells)))
        rows.append(dict(zip(COLUMNS, cells)))
    return rows


def main():
    p = argparse.ArgumentParser(description=__doc__)
    p.add_argument('batch')
    p.add_argument('--gate', type=Path)
    p.add_argument('--base', default=None, help='build name whose plaintext is this batch baseline')
    a = p.parse_args()
    base = R9 / a.batch
    order = json.loads((base / 'orders' / (a.batch + '.json')).read_text('utf8'))
    rows = {r['row_id']: (s['mode'], s['scene_id'], r) for s in order['scenes'] for r in s['rows']}
    roots = {r['row_id']: s['root'] for s in order['scenes'] for r in s['rows']}
    decisions_path = base / 'review' / 'decisions.tsv'
    decisions = load_decisions(decisions_path)
    applies = [d for d in decisions if d['decision'] == 'apply']
    snapshot = order.get('corpus_snapshot', '').rsplit('/', 1)[-1]
    base_name = a.base or SNAPSHOT_BASE[snapshot]
    candidate = LOC / 'builds' / base_name
    ledger_name = 'editorial-r9-polish-repairs.jsonl' if a.batch == 'batch-01' else ('editorial-r9-%s-repairs.jsonl' % a.batch)
    ledger_path = LOC / 'translations' / ledger_name
    ops = [json.loads(line) for line in ledger_path.read_text('utf8').splitlines() if line.strip()]
    op_findings = {}
    for op in ops:
        for fid in op['finding_ids']:
            op_findings.setdefault(fid, []).append(op['op_id'])
    problems = []
    for d in applies:
        if d['finding_id'] not in op_findings:
            problems.append('apply finding without ledger op: ' + d['finding_id'])
            continue
        mode, scene_id, row = rows[d['row_id']]
        archive, entry, kind, loc_name, locator = targets.target_of(
            row, mode, candidate, roots[d['row_id']])
        matched = [op for op in ops
                   if op['archive'] == archive and op['archive_entry'] == entry
                   and op['kind'] == kind and op.get(loc_name) == locator]
        if not matched:
            problems.append('no op for row ' + d['row_id'])
            continue
        op = matched[0]
        if op['new'] != effective_final(d['final_zh'], row['current']):
            problems.append('ledger text differs from decision: ' + d['finding_id'])
        if op['old'] != row['current']:
            problems.append('ledger old differs from order current: ' + d['finding_id'])
    for op in ops:
        if not op['finding_ids']:
            problems.append('op without findings: ' + op['op_id'])
    plain = {}
    for op in ops:
        key = (op['archive'], op['archive_entry'])
        if key not in plain:
            with zipfile.ZipFile(candidate / key[0]) as z:
                plain[key] = decrypt_file(z.read(key[1]))
    out, reports = apply_entries(plain, ops)
    gate = {
        'schema': 'cosmo-editorial-r9-build-gate/v1',
        'status': 'verified_for_application' if not problems else 'rejected',
        'scope': '%s applied Chinese rewrites; not a full proofread or real-machine acceptance' % a.batch,
        'base_candidate': candidate.relative_to(ROOT).as_posix(),
        'decisions_total': len(decisions),
        'apply_findings': sorted({d['finding_id'] for d in applies}),
        'operations': len(ops),
        'ledger': ledger_path.relative_to(ROOT).as_posix(),
        'ledger_sha256': file_sha(ledger_path),
        'decisions_sha256': file_sha(decisions_path),
        'verifier': {'path': 'localization/editorial/r9-polish/tools/verify_round.py',
                     'sha256': file_sha(Path(__file__).resolve())},
        'dry_run': {'engine': 'localization/tools/editorial_repairs.py:apply_entries',
                    'operations_applied': sum(len(r['operations_applied']) for r in reports),
                    'resources': [{k: r[k] for k in ('archive', 'archive_entry',
                                                     'before_resource_sha256', 'after_resource_sha256',
                                                     'targets_changed')} for r in reports]},
        'problems': problems,
        'not_installed': True,
        'game_started': False,
    }
    if problems:
        print(json.dumps(problems, ensure_ascii=False, indent=1))
        raise SystemExit(1)
    path = a.gate or (base / 'review' / 'build-gate.json')
    path.write_text(json.dumps(gate, ensure_ascii=False, indent=1) + '\n', encoding='utf8')
    print(json.dumps({k: gate[k] for k in ('status', 'decisions_total', 'operations')}, ensure_ascii=False))
    print('gate:', path.relative_to(ROOT))


if __name__ == '__main__':
    main()
