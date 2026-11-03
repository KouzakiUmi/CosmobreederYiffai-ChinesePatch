"""Which split words are bad enough to justify changing pagination?

The user's rule: pagination stays put unless a row is *especially* bad **and**
the fix reduces pages **and** the row is not at a staging hand-off (`cut`,
`fadecut`, `snap`, `music`, `rewind!` — the points where the background or the
actor changes).

This enumerates, for every row that still splits a word:

* how bad it is — a long word cut in two, or several splits in one row;
* whether repairing it would *reduce* the drawn row count (fewer pages);
* whether it sits immediately before a staging command with no other dialogue
  between them (a hand-off).

Only rows meeting all three are reported as candidates. Everything else stays.
"""
import re
import sys
import zipfile
from collections import Counter
from pathlib import Path

R9 = Path(__file__).resolve().parents[1]
ROOT = R9.parents[2]
sys.path.insert(0, str(ROOT / 'localization/editorial/r7-render/tools'))
sys.path.insert(0, str(R9 / 'tools'))
import render  # noqa: E402
import r9_targets as t  # noqa: E402

CAND = ROOT / 'localization/builds/r9-polish-candidate52'
BUDGET = 240
BREAK = '\u2028'
MIN_PAIR = 8
SOLID_PAIR = 30
# a word of this length cut in two counts as a long word
LONG_WORD = 3
HAN = re.compile('[\u4e00-\u9fff]')
ACTOR = re.compile('^(\\s*\\*\\s?|\\s*[^<>{}#*\\s][^:]{0,40}:\\s?)(.*)$')
STAGING = re.compile('^(?:cut|fadecut|snap|music|rewind|wait|queue|fade)\\b', re.I)
TEXT_LINE = re.compile('^\\s*(?:text|lang\\([^)]*\\)|auto\\([^)]*\\))\\s*:\\s?')

render.CAND = CAND
GLYPHS = render.load_font('story12')[0]


def width(text):
    return sum(GLYPHS.get(ord(ch), {'xadvance': 0})['xadvance'] for ch in text)


def body_of(line):
    match = ACTOR.match(line)
    return match.group(2) if match else line


def wrap(body):
    rows = []
    for segment in body.split(BREAK):
        cur, used = '', 0
        for ch in segment:
            advance = GLYPHS.get(ord(ch), {'xadvance': 0})['xadvance']
            if used + advance > BUDGET and cur:
                rows.append(cur)
                cur, used = '', 0
            cur += ch
            used += advance
        if cur:
            rows.append(cur)
    return rows


def pairs_of(body, bigrams):
    drawn = wrap(body)
    return [(i, drawn[i][-1] + drawn[i + 1][0]) for i in range(len(drawn) - 1)
            if drawn[i] and drawn[i + 1] and bigrams.get(drawn[i][-1] + drawn[i + 1][0], 0) >= MIN_PAIR]


def solid_pair(pair, bigrams):
    """Is this two-character pair a firmly established word?

    The loose test (>= MIN_PAIR) flags almost anything, because `的` combines
    with everything. A firmly established pair occurs far more often than that
    floor, and that is what makes a split look wrong on screen.
    """
    return bigrams.get(pair, 0) >= SOLID_PAIR


def long_word_at(body, rows, idx, bigrams):
    """Length of the collocation that straddles the break, capped at 4."""
    left = ''.join(rows[:idx + 1])
    right = ''.join(rows[idx + 1:])
    best = 1
    for take_left in range(1, 4):
        for take_right in range(1, 4):
            if take_left > len(left) or take_right > len(right):
                continue
            candidate = left[-take_left:] + right[:take_right]
            if len(candidate) < 2:
                continue
            if all(solid_pair(candidate[i:i + 2], bigrams) for i in range(len(candidate) - 1)):
                best = max(best, len(candidate))
    return best


def main():
    bigrams = Counter()
    scripts = {}
    for archive in ('cosmobreeder-multi.jar', 'patch.pak'):
        for entry in ('datadf/1', 'datadm/1'):
            scripts[(archive, entry)] = t.resource_state(CAND, archive, entry, 'line')[0]['lines']
        with zipfile.ZipFile(CAND / archive) as z:
            names = sorted(n for n in z.namelist() if n.startswith('vsn/') and n != 'vsn/0')
        for entry in names:
            try:
                scripts[(archive, entry)] = t.resource_state(CAND, archive, entry, 'line')[0]['lines']
            except Exception:
                continue
    for lines in scripts.values():
        for line in lines:
            body = body_of(line)
            if not HAN.search(body):
                continue
            han = [c for c in body if '\u4e00' <= c <= '\u9fff']
            for a, b in zip(han, han[1:]):
                bigrams[a + b] += 1

    total_rows = 0
    candidates = []
    for (archive, entry), lines in scripts.items():
        for number, line in enumerate(lines, 1):
            body = body_of(line)
            if not HAN.search(body):
                continue
            splits = pairs_of(body, bigrams)
            solid = [(i, p) for i, p in splits if solid_pair(p, bigrams)]
            if not splits:
                continue
            total_rows += 1
            worst = max(long_word_at(body, wrap(body), i, bigrams) for i, _ in splits)
            # is the next dialogue line separated from this one by a staging command?
            handoff = False
            for nxt in lines[number:]:
                stripped = nxt.strip()
                if not stripped:
                    continue
                if STAGING.match(stripped):
                    handoff = True
                    break
                if TEXT_LINE.match(nxt) or ACTOR.match(nxt):
                    break
            candidates.append({
                'archive': archive, 'entry': entry, 'line': number,
                'splits': len(splits), 'worst_word': worst,
                'handoff': handoff,
                'drawn_rows': len(wrap(body)),
            })

    bad = [c for c in candidates if c['worst_word'] >= LONG_WORD]
    print('rows still splitting a word :', total_rows)
    print('rows that are "especially bad" (long word or 2+ splits):', len(bad))
    print('  of those at a staging hand-off:', sum(1 for c in bad if c['handoff']))
    print('  of those not at a hand-off    :', sum(1 for c in bad if not c['handoff']))
    dist = Counter(c['worst_word'] for c in bad)
    print('worst-word length distribution:', dict(sorted(dist.items())))
    import json
    out = R9 / 'batch-24/orders/bad-splits.json'
    out.parent.mkdir(parents=True, exist_ok=True)
    keep = []
    for c in candidates:
        lines = scripts[(c['archive'], c['entry'])]
        body = body_of(lines[c['line'] - 1])
        c['text'] = body
        c['drawn'] = wrap(body)
        keep.append(c)
    out.write_text(json.dumps({'candidate': CAND.name, 'solid_pair': SOLID_PAIR,
                               'rows': keep}, ensure_ascii=False, indent=1) + chr(10), encoding='utf8')
    print('wrote', out.relative_to(ROOT))
    for c in bad[:8]:
        print('  %s:%d splits=%d worst=%d handoff=%s rows=%d'
              % (c['entry'], c['line'], c['splits'], c['worst_word'], c['handoff'], c['drawn_rows']))


if __name__ == '__main__':
    main()
