"""Can line-head punctuation be fixed by inserting explicit breaks?

The engine wraps greedily by pixel width and has no kinsoku rules, so a
continuation line can open with `，` `。` `！` `？` `…`. `PixelLayout` treats
CR/LF as explicit breaks, so the fix would be to place one where it keeps the
mark off the line head.

This measures feasibility before anyone writes a ledger:

* how many rows have a bad line head at all;
* how many can be fixed **without changing the total number of display rows**
  (that is the condition that keeps pagination and animation timing intact).

Strategy for a bad head: pull the mark back onto the previous line if it fits;
otherwise move the previous line's last character down, so the mark lands
mid-line. Both are then re-wrapped and re-measured, and the row count is
compared against the original.
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

CAND = ROOT / 'localization/builds/r9-polish-candidate50'
BUDGET = 240
HAN = re.compile('[\u4e00-\u9fff]')
BAD_HEAD = '，。、；：？！）》」』”’·…—'

render.CAND = CAND
GLYPHS = render.load_font('story12')[0]


def width(text):
    return sum(GLYPHS.get(ord(ch), {'xadvance': 0})['xadvance'] for ch in text)


def player(text):
    body = text.strip()
    if not body or body[0] in '{}#<':
        return False
    if body.startswith(('include ', 'if ', 'else', 'do ')) or '&&' in body or '||' in body:
        return False
    return HAN.search(body) is not None


def wrap(text):
    """Greedy wrap, honouring explicit breaks, exactly like the engine."""
    rows = []
    for segment in text.split('\n'):
        cur, used = '', 0
        for ch in segment:
            advance = GLYPHS.get(ord(ch), {'xadvance': 0})['xadvance']
            if used + advance > BUDGET and cur:
                rows.append(cur)
                cur, used = '', 0
            cur += ch
            used += advance
        rows.append(cur)
    return rows


def attempt(text):
    """Try to remove bad line heads; return (new_text, heads_fixed) or None."""
    rows = wrap(text)
    if len(rows) < 2:
        return None
    if not any(row and row[0] in BAD_HEAD for row in rows[1:]):
        return None

    segments = list(rows)
    fixed = 0
    for i in range(1, len(segments)):
        if not segments[i] or segments[i][0] not in BAD_HEAD:
            continue
        mark = segments[i][0]
        # 1) the mark fits at the end of the previous line
        if width(segments[i - 1] + mark) <= BUDGET:
            segments[i - 1] += mark
            segments[i] = segments[i][1:]
            fixed += 1
            continue
        # 2) move the previous line's last character down, so the mark is mid-line
        if segments[i - 1]:
            moved = segments[i - 1][-1]
            segments[i - 1] = segments[i - 1][:-1]
            segments[i] = moved + segments[i]
            fixed += 1
    if not fixed:
        return None
    if any(row and row[0] in BAD_HEAD for row in segments[1:]):
        return None
    new_text = '\n'.join(segments)
    if len(wrap(new_text)) != len(rows):
        return None
    if not any(width(row) <= BUDGET for row in segments):
        return None
    return new_text, fixed


def main():
    total_rows = 0
    fixable = 0
    changed_total_rows = 0
    marks = Counter()
    examples = []
    for archive in ('cosmobreeder-multi.jar', 'patch.pak'):
        for entry in ('datadf/1', 'datadm/1'):
            state, _ = t.resource_state(CAND, archive, entry, 'line')
            for number, line in enumerate(state['lines'], 1):
                if not player(line):
                    continue
                rows = wrap(line)
                if not any(row and row[0] in BAD_HEAD for row in rows[1:]):
                    continue
                total_rows += 1
                for row in rows[1:]:
                    if row and row[0] in BAD_HEAD:
                        marks[row[0]] += 1
                result = attempt(line)
                if result is None:
                    changed_total_rows += 1
                    continue
                fixable += 1
                if len(examples) < 3:
                    examples.append((entry, number, rows, result[0].split('\n')))
    print('rows with a bad line head :', total_rows)
    print('fixable, same row count   :', fixable)
    print('not cleanly fixable       :', total_rows - fixable)
    print('by mark                   :', dict(marks.most_common()))
    for entry, number, before, after in examples:
        print('\n%s:%d' % (entry, number))
        print('  before:', ' / '.join(before))
        print('  after :', ' / '.join(after))


if __name__ == '__main__':
    main()
