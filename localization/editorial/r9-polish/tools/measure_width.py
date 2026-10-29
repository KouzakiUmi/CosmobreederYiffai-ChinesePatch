"""Measure story-box wrapping for the batch, using the real 12px glyph table.

Reports current and proposed wrap counts (240px, story box) so a proposal cannot
silently push a line past the 3-line page limit. Read-only.
"""
from pathlib import Path
import argparse
import importlib.util
import json
import os

ROOT = Path(__file__).resolve().parents[4]
LOC = ROOT / 'localization'
R9 = LOC / 'editorial/r9-polish'
spec = importlib.util.spec_from_file_location('preview_layout', LOC / 'tools/preview-layout.py')
pl = importlib.util.module_from_spec(spec)
spec.loader.exec_module(pl)


def main():
    p = argparse.ArgumentParser(description=__doc__)
    p.add_argument('batch')
    p.add_argument('--box', type=int, default=240)
    a = p.parse_args()
    base = R9 / a.batch
    order = json.loads((base / 'orders' / (a.batch + '.json')).read_text('utf8'))
    head, chars, _ = pl.load_font(str(LOC / 'runtime/bbc2-12px.fnt'),
                                  str(LOC / 'runtime/bbc2-cjk-12.png'))

    def wraps(text):
        return len(pl.layout(text, chars, a.box))

    rows = {r['row_id']: r for s in order['scenes'] for r in s['rows']}
    props = {}
    for route in ('gemini', 'ds'):
        path = base / route / 'findings.jsonl'
        if not path.exists():
            continue
        for line in path.read_text('utf8').splitlines():
            if not line.strip():
                continue
            f = json.loads(line)
            rid = (f.get('row_ids') or [None])[0]
            if rid and f.get('proposed_zh') is not None:
                props.setdefault(rid, {})[route] = f['proposed_zh']
    out = {'batch': a.batch, 'box_px': a.box, 'rows': [], 'over_limit': []}
    for rid, row in rows.items():
        cur = row['current'] or ''
        if not cur.strip():
            continue
        rec = {'row_id': rid, 'scene_id': next(s['scene_id'] for s in order['scenes']
                                              if any(r['row_id'] == rid for r in s['rows'])),
               'current_wraps': wraps(cur)}
        for route, text in props.get(rid, {}).items():
            rec[route + '_wraps'] = wraps(text)
        rec['over_3'] = any(rec.get(k, 0) > 3 for k in ('current_wraps', 'gemini_wraps', 'ds_wraps'))
        if rec['over_3']:
            out['over_limit'].append(rec)
        if rid in props:
            out['rows'].append(rec)
    print(json.dumps({'over_limit': out['over_limit'], 'measured': len(out['rows'])},
                     ensure_ascii=False, indent=1))
    (base / 'review' / 'width-report.json').write_text(
        json.dumps(out, ensure_ascii=False, indent=1) + '\n', encoding='utf8')


if __name__ == '__main__':
    main()
