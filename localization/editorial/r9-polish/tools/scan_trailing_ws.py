"""List rows whose Chinese line has trailing whitespace the English source lacks.

The single-judgement rule (R9 README 五之三): the only criterion is whether the
English source line ends with whitespace. `catalog/occurrences.jsonl:trailing_ws`
describes the Chinese line and must not be used -- it produces the circular
"both sides agree, so both are mirrors" conclusion.

Source lookup: row_id -> occurrence_id -> unit_id -> catalog/units.jsonl:source.
SFW-numbered rows can lack an occurrence record; those fall back to the batch
order's own `source` field.

Read-only: prints rows, writes nothing.
"""
from pathlib import Path
import json
import sys

ROOT = Path(__file__).resolve().parents[4]
R9 = ROOT / 'localization/editorial/r9-polish'
CATALOG = ROOT / 'localization/catalog'


def load_sources():
    occ, units = {}, {}
    for line in (CATALOG / 'occurrences.jsonl').read_text('utf8').splitlines():
        if line.strip():
            d = json.loads(line)
            occ[d['occurrence_id']] = d['unit_id']
    for line in (CATALOG / 'units.jsonl').read_text('utf8').splitlines():
        if line.strip():
            d = json.loads(line)
            units[d['id']] = d['source']
    return occ, units


def scan(batch):
    base = R9 / batch
    order = json.loads((base / 'orders' / (batch + '.json')).read_text('utf8'))
    occ, units = load_sources()
    defects, mirrors = [], []
    for scene in order['scenes']:
        for row in scene['rows']:
            cur = row.get('current') or ''
            if not cur or cur == cur.rstrip():
                continue
            rid = row['row_id']
            uid = occ.get(rid.replace('CAT:', ''))
            src = units.get(uid) if uid else None
            traced = src is not None
            if src is None:
                src = row.get('source') or ''
            if src != src.rstrip():
                mirrors.append((rid, scene['scene_id'], traced))
            else:
                defects.append((rid, scene['scene_id'], cur, row.get('source') or '', traced))
    return defects, mirrors


def main():
    if len(sys.argv) < 2:
        raise SystemExit('usage: scan_trailing_ws.py <batch> [...]')
    for batch in sys.argv[1:]:
        defects, mirrors = scan(batch)
        print(f'== {batch}: defects={len(defects)} mirrors={len(mirrors)}')
        for rid, scene, cur, src, traced in defects:
            print(json.dumps({'row_id': rid, 'scene_id': scene, 'current': cur,
                              'source': src, 'traced_to_unit': traced},
                             ensure_ascii=False))
        untraced = [m for m in mirrors if not m[2]]
        print(f'   mirrors without occurrence record: {len(untraced)}')


if __name__ == '__main__':
    main()
