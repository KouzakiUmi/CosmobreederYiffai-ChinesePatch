"""Build the source-locked R9 ledger from decisions and verify it by dry-run.

Reads the r9 order (row -> physical line), the current candidate archives, and a
decisions.tsv. Emits op records bound to whole-resource SHAs, then validates the
whole batch with editorial_repairs.apply_entries. Writes only under r9-polish and
localization/translations (new ledger file).
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
from text_rules import SYMBOL_FOR_NEWLINE, effective_final, expand_newlines  # noqa: E402,F401

SNAPSHOT_BASE = {
    'snapshot-02': 'r8-puzzle-candidate12',
    'snapshot-03': 'r9-polish-candidate13',
}
R9 = LOC / 'editorial/r9-polish'
LINES = re.compile(r'[^\r\n]*(?:\r\n|\r|\n|\Z)')
MODE_ARCHIVE = {'sfw': 'cosmobreeder-multi.jar', 'nsfw': 'patch.pak'}
COLUMNS = ('finding_id', 'route', 'severity', 'category', 'scene_id', 'row_id',
           'decision', 'final_zh', 'reason')


def bodies(entry_archive, candidate):
    z = zipfile.ZipFile(candidate / entry_archive[0])
    raw = decrypt_file(z.read(entry_archive[1]))
    parts = LINES.findall(raw.decode('utf8'))
    if parts and parts[-1] == '':
        parts.pop()
    return [re.sub(r'(?:\r\n|\r|\n)\Z', '', p) for p in parts], sha256(raw).hexdigest()




def load_decisions(path):
    rows = []
    header = None
    for n, line in enumerate(path.read_text('utf8').splitlines(), 1):
        if not line.strip():
            continue
        cells = line.split('\t')
        if header is None:
            header = cells
            if tuple(header) != COLUMNS:
                raise ValueError('decisions.tsv header mismatch: %s' % header)
            continue
        if len(cells) != len(COLUMNS):
            raise ValueError('decisions.tsv:%d expected %d columns' % (n, len(COLUMNS)))
        rows.append(dict(zip(COLUMNS, cells)))
    return rows


def main():
    p = argparse.ArgumentParser(description=__doc__)
    p.add_argument('batch')
    p.add_argument('--decisions', type=Path)
    p.add_argument('--out', type=Path)
    p.add_argument('--dry-run', action='store_true')
    p.add_argument('--base', default=None, help='build name whose plaintext is this batch baseline')
    a = p.parse_args()
    base = R9 / a.batch
    order = json.loads((base / 'orders' / (a.batch + '.json')).read_text('utf8'))
    rows = {}
    scene_root = {}
    for scene in order['scenes']:
        for r in scene['rows']:
            rows[r['row_id']] = (scene['mode'], scene['scene_id'], r)
            scene_root[r['row_id']] = scene['root']
    snapshot = order.get('corpus_snapshot', '').rsplit('/', 1)[-1]
    base_name = a.base or SNAPSHOT_BASE[snapshot]
    candidate = LOC / 'builds' / base_name
    decisions_path = a.decisions or (base / 'review' / 'decisions.tsv')
    decisions = load_decisions(decisions_path)
    applied = [d for d in decisions if d['decision'] == 'apply']
    cache, shas = {}, {}
    grouped = {}
    for d in applied:
        if d['row_id'] not in rows:
            raise ValueError('unknown row_id %s' % d['row_id'])
        mode, scene_id, row = rows[d['row_id']]
        root = scene_root[d['row_id']]
        archive, entry, kind, loc_name, locator = targets.target_of(row, mode, candidate, root)
        key = (archive, entry)
        if key not in cache:
            cache[key], shas[key] = targets.resource_state(candidate, archive, entry, kind)
        old = targets.old_text(cache[key], kind, locator, row)
        if old != row['current']:
            raise ValueError('baseline drift on %s: archive %r order %r'
                             % (d['row_id'], old, row['current']))
        target = (archive, entry, kind, str(locator))
        new = effective_final(d['final_zh'], old)
        if target in grouped:
            if grouped[target]['new'] != new:
                raise ValueError('conflicting decisions on %s' % d['row_id'])
            grouped[target]['finding_ids'] = sorted(set(grouped[target]['finding_ids'] + [d['finding_id']]))
            continue
        op = {
            'archive': archive, 'archive_entry': entry, 'kind': kind,
            'before_resource_sha256': shas[key], 'old': old, 'new': new,
            'finding_ids': [d['finding_id']], 'source_refs': [d['scene_id'], 'R9:' + a.batch],
        }
        op[loc_name] = locator
        grouped[target] = op
    ops = []
    for target, op in sorted(grouped.items(), key=lambda kv: (kv[0][0], kv[0][1], kv[0][2], kv[0][3])):
        op = dict(op)
        op['op_id'] = 'R9-%04d' % (len(ops) + 1)
        ops.append(op)
    plain = {k: targets.read_resource(candidate, k[0], k[1]) for k in cache}
    out, reports = apply_entries(plain, ops)
    summary = {'batch': a.batch, 'decisions': len(decisions), 'applied': len(applied),
               'operations': len(ops), 'targets': len(reports),
               'per_resource': [{k: r[k] for k in ('archive', 'archive_entry',
                                                   'before_resource_sha256', 'after_resource_sha256',
                                                   'targets_changed')} for r in reports]}
    if a.dry_run:
        print(json.dumps(summary, ensure_ascii=False, indent=1))
        return
    default_name = 'editorial-r9-polish-repairs.jsonl' if a.batch == 'batch-01' else ('editorial-r9-%s-repairs.jsonl' % a.batch)
    out_path = a.out or (LOC / 'translations' / default_name)
    # JSONL is one operation per line, and Python's `splitlines()` also breaks on
    # U+2028 — so a raw U+2028 inside a value would corrupt the ledger on the next
    # read. Store the sentinel instead; `text_rules` expands it.
    out_path.write_text(''.join(json.dumps(op, ensure_ascii=False, sort_keys=False)
                                .replace('\u2028', '\\u2028') + '\n'
                                for op in ops), encoding='utf8')
    summary['ledger'] = out_path.relative_to(ROOT).as_posix()
    summary['base_candidate'] = candidate.relative_to(ROOT).as_posix()
    (base / 'review' / 'ledger-report.json').write_text(
        json.dumps(summary, ensure_ascii=False, indent=1) + '\n', encoding='utf8')
    print(json.dumps(summary, ensure_ascii=False, indent=1))


if __name__ == '__main__':
    main()
