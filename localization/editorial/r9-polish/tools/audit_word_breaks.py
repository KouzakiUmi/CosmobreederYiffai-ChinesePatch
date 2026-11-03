"""Can a word-break be repaired without changing how many rows are drawn?

The engine wraps greedily by pixel width, so a Chinese word can be split across
two display rows (`矮` / `人`). `PixelLayout` treats U+2028 as a hard break, so
moving the break to a word boundary is possible — but only if the drawn row
count stays the same, otherwise pagination and animation timing shift.

This measures that, on the **display body** (the speaker prefix is not laid out):

* how many rows contain a split word at all;
* how many can be repaired with the row count unchanged;
* what the repairs look like.

A split is "the two characters either side of a greedy break form a frequent
collocation": the pair occurs at least `MIN_PAIR` times in the corpus. That is a
frequency proxy, not a segmentation — it misses rare proper nouns and can flag
cross-word pairs. Both limits are stated in the report.
"""
import re
import sys
from collections import Counter
from pathlib import Path

R9 = Path(__file__).resolve().parents[1]
ROOT = R9.parents[2]
sys.path.insert(0, str(ROOT / 'localization/editorial/r7-render/tools'))
sys.path.insert(0, str(R9 / 'tools'))
import render  # noqa: E402
import r9_targets as t  # noqa: E402

CAND = ROOT / 'localization/builds/r9-polish-candidate51'
BUDGET = 240
BREAK = '\u2028'
MIN_PAIR = 8
HAN = re.compile('[\u4e00-\u9fff]')
ACTOR = re.compile('^(\\s*\\*\\s?|\\s*[^<>{}#*\\s][^:]{0,40}:\\s?)(.*)$')

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


def breaks_of(rows):
    """(index of the row that ends, pair of characters across the break)."""
    out = []
    for i in range(len(rows) - 1):
        if rows[i] and rows[i + 1]:
            out.append((i, rows[i][-1] + rows[i + 1][0]))
    return out


def player(body):
    stripped = body.strip()
    if not stripped or stripped[0] in '{}#<':
        return False
    if stripped.startswith(('include ', 'if ', 'else', 'do ')) or '&&' in body or '||' in body:
        return False
    return HAN.search(body) is not None


def repair(body, rows, splits, bigrams):
    """Insert a break so the split pair lands on one side, keeping the row count.

    Two moves are tried at each split, cheapest first: pull the word's first
    character down (moves one character), then pull the whole first row's tail
    down in growing steps. The second move is what handles rows already near
    240px — there the tail has to travel several characters before the break
    lands on a word boundary.
    """
    if not splits:
        return None
    flat = body.replace(BREAK, '')
    for idx, pair in splits:
        head = ''.join(rows[:idx + 1])
        tail = ''.join(rows[idx + 1:])
        for back in range(1, min(len(head), 14) + 1):
            moved = head[-back:]
            new_rows = list(rows[:idx]) + [head[:-back], moved + tail]
            candidate = BREAK.join(row for row in new_rows if row)
            if candidate.replace(BREAK, '') != flat:
                continue
            drawn = wrap(candidate)
            if len(drawn) != len(rows):
                continue
            remaining = [p for _, p in breaks_of(drawn) if bigrams.get(p, 0) >= MIN_PAIR]
            if len(remaining) >= len(splits):
                continue
            return candidate, len(splits) - len(remaining)
    return None


def main():
    bigrams = Counter()
    for archive in ('cosmobreeder-multi.jar', 'patch.pak'):
        for entry in ('datadf/1', 'datadm/1'):
            for line in t.resource_state(CAND, archive, entry, 'line')[0]['lines']:
                body = body_of(line)
                if not HAN.search(body):
                    continue
                han = [c for c in body if '\u4e00' <= c <= '\u9fff']
                for a, b in zip(han, han[1:]):
                    bigrams[a + b] += 1

    rows_with_split = 0
    repair_same_rows = 0
    repair_changes_rows = 0
    no_repair = 0
    pairs = Counter()
    examples = []
    for archive in ('cosmobreeder-multi.jar', 'patch.pak'):
        for entry in ('datadf/1', 'datadm/1'):
            for number, line in enumerate(t.resource_state(CAND, archive, entry, 'line')[0]['lines'], 1):
                body = body_of(line)
                if not player(body):
                    continue
                drawn = wrap(body)
                splits = [(i, pair) for i, pair in breaks_of(drawn) if bigrams.get(pair, 0) >= MIN_PAIR]
                if not splits:
                    continue
                rows_with_split += 1
                for _, pair in splits:
                    pairs[pair] += 1
                result = repair(body, drawn, splits, bigrams)
                if result is None:
                    no_repair += 1
                    continue
                new_body, fixed = result
                if len(wrap(new_body)) == len(drawn):
                    repair_same_rows += 1
                    if len(examples) < 3:
                        examples.append((entry, number, drawn, wrap(new_body), fixed))
                else:
                    repair_changes_rows += 1
    print('rows with a split word        :', rows_with_split)
    print('repairable, same row count    :', repair_same_rows)
    print('repairable, row count changes :', repair_changes_rows)
    print('no clean repair               :', no_repair)
    print('split pairs                   :', pairs.most_common(8))
    for entry, number, before, after, fixed in examples:
        print('\n%s:%d  (fixed %d)' % (entry, number, fixed))
        print('  before:', ' / '.join(before))
        print('  after :', ' / '.join(after))


if __name__ == '__main__':
    main()
