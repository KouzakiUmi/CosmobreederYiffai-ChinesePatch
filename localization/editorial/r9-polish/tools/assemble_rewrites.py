"""Validate the four rewritten parts and assemble them into one review table.

Checks every proposal against the real font, the real wrap rule and the corpus:

* the drawn rows must match the stated widths and fit 240px;
* the listed `split_pairs` must be gone;
* no *new* solid pair may appear at any row boundary;
* the text must not lose or gain a bracket, and must stay within 240px per row.

Anything that fails is reported, not silently dropped: the point is to know what
the rewrite actually achieved.
"""
import json
import sys
from collections import Counter
from pathlib import Path

R9 = Path(__file__).resolve().parents[1]
ROOT = R9.parents[2]
sys.path.insert(0, str(ROOT / 'localization/editorial/r7-render/tools'))
sys.path.insert(0, str(R9 / 'tools'))
import render  # noqa: E402
import r9_targets as t  # noqa: E402

CAND = ROOT / 'localization/builds/r9-polish-candidate52'
ORDERS = R9 / 'batch-25/orders'
BUDGET = 240
SOLID_PAIR = 30
BREAK = '\u2028'

render.CAND = CAND
GLYPHS = render.load_font('story12')[0]


def width(text):
    return sum(GLYPHS.get(ord(ch), {'xadvance': 0})['xadvance'] for ch in text)


def wrap(text):
    rows, cur, used = [], '', 0
    for ch in text:
        advance = GLYPHS.get(ord(ch), {'xadvance': 0})['xadvance']
        if used + advance > BUDGET and cur:
            rows.append(cur)
            cur, used = '', 0
        cur += ch
        used += advance
    if cur:
        rows.append(cur)
    return rows


def boundaries(rows):
    return [rows[i][-1] + rows[i + 1][0] for i in range(len(rows) - 1)
            if rows[i] and rows[i + 1]]


def main():
    bigrams = Counter()
    for archive in ('cosmobreeder-multi.jar', 'patch.pak'):
        for entry in ('datadf/1', 'datadm/1'):
            for line in t.resource_state(CAND, archive, entry, 'line')[0]['lines']:
                body = line
                han = [c for c in body if '\u4e00' <= c <= '\u9fff']
                for a, b in zip(han, han[1:]):
                    bigrams[a + b] += 1

    targets = json.loads((ORDERS / 'rewrite-targets.json').read_text('utf8'))['rows']
    proposals = []
    problems = []
    for part in (1, 2, 3, 4):
        path = ORDERS / ('part-%d-rewritten.json' % part)
        if not path.exists():
            problems.append({'kind': 'missing-part', 'part': part})
            continue
        data = json.loads(path.read_text('utf8'))
        for item in data['items']:
            base = targets[item['id']]
            rewritten = item.get('rewritten')
            if not rewritten:
                problems.append({'kind': 'no-proposal', 'id': item['id'],
                                 'line': base['line'], 'note': item.get('note', '')})
                continue
            drawn = wrap(rewritten)
            widths = [width(r) for r in drawn]
            issues = []
            if any(w > BUDGET for w in widths):
                issues.append('row over 240px: %r' % widths)
            if drawn != item.get('rows'):
                issues.append('stated rows differ from real wrap')
            if widths != item.get('widths'):
                issues.append('stated widths differ: %r vs %r' % (item.get('widths'), widths))
            still = [p for p in base['split_pairs'] if p in boundaries(drawn)]
            if still:
                issues.append('still splits %r' % still)
            introduced = [p for p in boundaries(drawn)
                          if bigrams.get(p, 0) >= SOLID_PAIR and p not in base['split_pairs']]
            if introduced:
                issues.append('introduces %r' % introduced)
            if base['current'].count('[') != item.get('rewritten', '').count('[') and \
                    base['current'].count('[') > 0:
                issues.append('bracket count changed')
            proposals.append({
                'id': item['id'], 'archive': base['archive'], 'entry': base['entry'],
                'line': base['line'], 'mode': base['mode'],
                'english': base['english'], 'old_body': base['body'],
                'new_body': rewritten, 'old_rows': base['drawn'], 'new_rows': drawn,
                'old_widths': base['widths'], 'new_widths': widths,
                'split_pairs': base['split_pairs'],
                'issues': issues, 'note': item.get('note', ''),
            })
            if issues:
                problems.append({'kind': 'issue', 'id': item['id'],
                                 'line': base['line'], 'issues': issues})

    ok = [p for p in proposals if not p['issues']]
    rows_before = Counter(len(p['old_rows']) for p in ok)
    rows_after = Counter(len(p['new_rows']) for p in ok)
    print('targets            :', len(targets))
    print('proposals          :', len(proposals))
    print('clean proposals    :', len(ok))
    print('with issues        :', len(proposals) - len(ok))
    print('no proposal        :', sum(1 for p in problems if p['kind'] == 'no-proposal'))
    print('rows before/after  :', dict(sorted(rows_before.items())),
          '->', dict(sorted(rows_after.items())))
    for p in problems[:10]:
        print('  ', p)

    (ORDERS / 'rewrite-review.json').write_text(
        json.dumps({'clean': ok, 'problems': problems}, ensure_ascii=False, indent=1) + '\n',
        encoding='utf8')
    print('wrote rewrite-review.json')


if __name__ == '__main__':
    main()
