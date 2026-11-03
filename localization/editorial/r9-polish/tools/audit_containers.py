"""Measure every hard-wrapped container against the real glyph table.

Dialogue wraps itself (240px, 3 lines per page), so a Chinese line that runs
longer or shorter than the English is not a defect. Four containers do **not**
wrap on their own — they are fixed grids and they throw when the text does not
fit:

| container | source of truth | limit |
| --- | --- | --- |
| 角色卡 `cardFormat` | `SceneText.fixedGrid(display, 16, rows, false)` | 16 列 × 128px，15 行 |
| 成就 `achievementFormat` | `fixedGrid(text, 30, 2, false)` | 30 列 × 240px，2 行 |
| 数据书 `dataBlock` | `PixelLayout` 224px | 3 行 |
| 结局数据块 `formatData` | `fixedGrid(text, 28, 3, true)` | 28 列 × 224px，3 行 |

`|` starts a new grid line; within a line the engine wraps at the pixel budget
and each extra wrapped row still counts against the row limit. So "how many
lines does this value really take" is: split on `|`, wrap each piece at the
budget with the real advances, sum the wrapped rows, compare with the limit.

Usage: python tools/audit_containers.py r9-polish-candidate46
"""
from pathlib import Path
import json
import sys

R9 = Path(__file__).resolve().parents[1]
ROOT = R9.parents[2]
sys.path.insert(0, str(ROOT / 'localization/editorial/r7-render/tools'))
sys.path.insert(0, str(R9 / 'tools'))
import render  # noqa: E402
import r9_targets as t  # noqa: E402

CANDIDATE = ROOT / 'localization/builds' / (sys.argv[1] if len(sys.argv) > 1 else 'r9-polish-candidate46')
render.CAND = CANDIDATE
GLYPHS = {role: render.load_font(role)[0] for role in ('story12', 'classic')}


def advance(ch, role='classic'):
    return GLYPHS[role].get(ord(ch), {'xadvance': 0})['xadvance']


def wrap_lines(text, budget, role):
    """Greedy wrap as PixelLayout does it; returns the number of display rows."""
    rows, current, width = 1, [], 0
    for ch in text:
        w = advance(ch, role)
        if width + w > budget and current:
            rows += 1
            current, width = [], 0
        current.append(ch)
        width += w
    return rows


def grid_rows(value, columns, rows_limit, role='classic', styles=False):
    """(display_rows, over_limit, widest_row) for a fixed-grid value."""
    capacity = columns
    budget = columns * 8
    total = 0
    widest = 0
    for paragraph in value.split('|'):
        styled = styles and paragraph.startswith('$')
        payload = paragraph[1:] if styled else paragraph
        payload = payload.replace('\r', '').replace('\n', '').replace('\u2028', '').replace('\u2029', '')
        cap = capacity - (1 if styled else 0)
        channel = min(budget - (8 if styled else 0), cap * 8)
        widest = max(widest, sum(advance(c, role) for c in payload))
        total += wrap_lines(payload, channel, role)
    return total, total > rows_limit, widest


def main():
    problems = []
    counts = {'card': 0, 'achv': 0, 'data': 0, 'ending': 0}
    for archive in ('cosmobreeder-multi.jar', 'patch.pak'):
        state, _ = t.resource_state(CANDIDATE, archive, 'datav/1', 'json')
        for key, value in state['document'].items():
            if not isinstance(value, str):
                continue
            if key.startswith('ui.card.') and value.strip():
                counts['card'] += 1
                # 15 rows both sides: the original English backs already ship 13–14
                # segments (`backup/cosmobreeder-multi.jar`), so the reachable limit
                # is NT=15; R7's earlier note of 11 for backs does not hold.
                limit = 15
                rows, over, widest = grid_rows(value, 16, limit)
                if over or widest > 128:
                    problems.append((archive, key, rows, limit, widest))
            elif key.startswith('ui.achievement.') and value.strip():
                counts['achv'] += 1
                rows, over, widest = grid_rows(value, 30, 2)
                if over or widest > 240:
                    problems.append((archive, key, rows, 2, widest))
            elif key.startswith('ui.data.') and value.strip():
                counts['data'] += 1
                role = 'story12'
                rows, over, widest = grid_rows(value, 28, 3, role)
                if over:
                    problems.append((archive, key, rows, 3, widest))
            elif key.startswith('ui.end.') and '|' in value:
                counts['ending'] += 1
                rows, over, widest = grid_rows(value, 28, 3, styles=True)
                if over:
                    problems.append((archive, key, rows, 3, widest))
    print(json.dumps({'candidate': CANDIDATE.name, 'checked': counts, 'problem_count': len(problems)}, ensure_ascii=False))
    for p in problems[:40]:
        print('  %-22s %-44s rows %d > %d  widest %dpx' % p)


if __name__ == '__main__':
    main()
