"""Cross-check one r9-polish batch: two independent review routes vs the order.

Read-only. Validates structure (coverage, row identities, prefix and marker
preservation, width estimate) and reports agreement between routes. It does not
judge translation quality; that is the main agent's decision table.
"""
from pathlib import Path
from collections import Counter, defaultdict
import argparse
import json
import re

ROOT = Path(__file__).resolve().parents[4]
R9 = ROOT / 'localization/editorial/r9-polish'

DS = re.compile(r'^(\s*\*\s?|\s*[^<>{}#*\s][^:]{0,40}:\s?)(.*)$')
MARKERS = re.compile(r'@[A-Za-z][A-Za-z0-9_]*|\$\{[^{}]+\}|\{[^{}\r\n]+\}|</?[A-Za-z][^<>\r\n]*>|\|')
ASCII = re.compile(r'[\x20-\x7e]')


def prefix_of(line):
    m = DS.match(line or '')
    return m.group(1) if m else ''


def body_of(line):
    m = DS.match(line or '')
    return m.group(2) if m else (line or '')


def width_px(text):
    """Rough story-box estimate: full-width 12px, ASCII 6px, spaces 3px."""
    total = 0
    for ch in text or '':
        if ch == ' ':
            total += 3
        elif ASCII.fullmatch(ch):
            total += 6
        else:
            total += 12
    return total


def load_jsonl(path):
    if not path.exists():
        return None
    rows = []
    for n, line in enumerate(path.read_text('utf8').splitlines(), 1):
        if not line.strip():
            continue
        try:
            rows.append(json.loads(line))
        except json.JSONDecodeError as exc:
            raise ValueError('%s:%d bad JSON: %s' % (path.name, n, exc)) from exc
    return rows


def main():
    p = argparse.ArgumentParser(description=__doc__)
    p.add_argument('batch')
    a = p.parse_args()
    base = R9 / a.batch
    order = json.loads((base / 'orders' / (a.batch + '.json')).read_text('utf8'))
    scenes = {s['scene_id']: s for s in order['scenes']}
    rows = {r['row_id']: (s['scene_id'], r) for s in order['scenes'] for r in s['rows']}
    report = {'batch': a.batch, 'routes': {}, 'cross': {}}
    route_data = {}
    for route in ('gemini', 'ds'):
        d = base / route
        findings = load_jsonl(d / 'findings.jsonl')
        coverage = load_jsonl(d / 'coverage.jsonl')
        info = {'findings': 0, 'coverage': 0, 'problems': [], 'severity': Counter(),
                'categories': Counter(), 'status': Counter(), 'rows_proposed': 0}
        if findings is None:
            info['problems'].append('missing findings.jsonl')
        else:
            info['findings'] = len(findings)
            seen_ids, touched = set(), set()
            for f in findings:
                fid = f.get('finding_id')
                if not fid or fid in seen_ids:
                    info['problems'].append('bad/duplicate finding_id: %r' % fid)
                seen_ids.add(fid)
                sc = scenes.get(f.get('scene_id'))
                if not sc:
                    info['problems'].append('%s unknown scene' % fid)
                    continue
                rids = f.get('row_ids') or []
                if not rids:
                    info['problems'].append('%s empty row_ids' % fid)
                for rid in rids:
                    if rid not in rows:
                        info['problems'].append('%s unknown row %s' % (fid, rid))
                    elif rows[rid][0] != sc['scene_id']:
                        info['problems'].append('%s cross-scene row %s' % (fid, rid))
                    touched.add(rid)
                info['severity'][str(f.get('severity'))] += 1
                info['categories'][str(f.get('category'))] += 1
                info['status'][str(f.get('status'))] += 1
                prop = f.get('proposed_zh')
                if prop is None:
                    continue
                for rid in rids[:1]:
                    if rid not in rows:
                        continue
                    cur = rows[rid][1]['current'] or ''
                    if not cur.strip():
                        info['problems'].append('%s proposes into blank joined tail %s' % (fid, rid))
                        continue
                    if prefix_of(prop) != prefix_of(cur):
                        info['problems'].append('%s prefix drift on %s' % (fid, rid))
                    if Counter(MARKERS.findall(prop)) != Counter(MARKERS.findall(cur)):
                        info['problems'].append('%s marker drift on %s' % (fid, rid))
                    grew = width_px(body_of(prop)) - width_px(body_of(cur))
                    if grew > 24:
                        info['problems'].append('%s width +%dpx on %s' % (fid, grew, rid))
            info['rows_proposed'] = len(touched)
        if coverage is None:
            info['problems'].append('missing coverage.jsonl')
        else:
            info['coverage'] = len(coverage)
            seen = set()
            for c in coverage:
                sid = c.get('scene_id')
                if sid not in scenes:
                    info['problems'].append('coverage unknown scene %r' % sid)
                    continue
                if sid in seen:
                    info['problems'].append('coverage duplicate %s' % sid)
                seen.add(sid)
                if c.get('read_status') not in ('read_full', 'partial', 'not_read'):
                    info['problems'].append('coverage bad read_status %r' % c.get('read_status'))
                missing = {r['row_id'] for r in scenes[sid]['rows']} - set(c.get('row_ids') or [])
                if missing:
                    info['problems'].append('coverage %s missing rows %d' % (sid, len(missing)))
            if len(seen) != len(scenes):
                info['problems'].append('coverage scenes %d/%d' % (len(seen), len(scenes)))
        info['severity'] = dict(info['severity'])
        info['categories'] = dict(info['categories'])
        info['status'] = dict(info['status'])
        report['routes'][route] = info
        route_data[route] = findings or []
    # Cross-route agreement keyed on the first row of each finding.
    proposals = defaultdict(dict)
    for route, findings in route_data.items():
        for f in findings:
            rid = (f.get('row_ids') or [None])[0]
            if rid and f.get('proposed_zh') is not None:
                proposals[rid].setdefault(route, f['proposed_zh'])
    both = [r for r, v in proposals.items() if len(v) == 2]
    same = [r for r in both if proposals[r]['gemini'] == proposals[r]['ds']]
    report['cross'] = {
        'rows_with_proposal': len(proposals),
        'rows_both_routes': len(both),
        'rows_identical_text': len(same),
        'rows_conflicting_text': len(both) - len(same),
        'only_gemini': sum(1 for v in proposals.values() if set(v) == {'gemini'}),
        'only_ds': sum(1 for v in proposals.values() if set(v) == {'ds'}),
        'conflicts': [{'row_id': r, 'scene_id': rows[r][0], 'current': rows[r][1]['current'],
                       'gemini': proposals[r]['gemini'], 'ds': proposals[r]['ds']} for r in both if r not in same],
    }
    findings_by_row = defaultdict(list)
    for route, findings in route_data.items():
        for f in findings:
            for rid in (f.get('row_ids') or [])[:1]:
                findings_by_row[rid].append('%s:%s:%s' % (route, f.get('finding_id'), f.get('severity')))
    sheet = ['\t'.join(('row_id', 'scene_id', 'routes', 'severities', 'current', 'gemini_zh', 'ds_zh', 'findings'))]
    for rid in sorted(proposals):
        scene_id, row = rows[rid]
        sev = ','.join(sorted({x.split(':')[-1] for x in findings_by_row.get(rid, [])}))
        sheet.append('\t'.join((rid, scene_id, '+'.join(sorted(proposals[rid])), sev,
                                (row['current'] or '').replace('\t', ' '),
                                proposals[rid].get('gemini', '').replace('\t', ' '),
                                proposals[rid].get('ds', '').replace('\t', ' '),
                                ' '.join(findings_by_row.get(rid, [])))))
    (base / 'review' / 'worksheet.tsv').write_text('\n'.join(sheet) + '\n', encoding='utf8')
    out = base / 'review' / 'structure-report.json'
    out.parent.mkdir(parents=True, exist_ok=True)
    out.write_text(json.dumps(report, ensure_ascii=False, indent=1) + '\n', encoding='utf8')
    print(json.dumps({k: v for k, v in report.items() if k != 'cross'}, ensure_ascii=False, indent=1))
    print(json.dumps({k: v for k, v in report['cross'].items() if k != 'conflicts'}, ensure_ascii=False, indent=1))
    print('report:', out.relative_to(ROOT))


if __name__ == '__main__':
    main()
