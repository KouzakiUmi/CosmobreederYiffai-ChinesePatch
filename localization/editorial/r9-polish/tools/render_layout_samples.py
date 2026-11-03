"""Render real candidate text through the real fonts, one container at a time.

R7's `render.py` draws a list of lines; it does not decide where the engine
breaks a line. This does: it applies each container's real rule (dialogue
240px/3 rows, card 16×128px/15 rows, data book 224px/3 rows), wraps the Chinese
with the pinned glyph table, and writes one PNG per sample plus an `index.json`
with the measurements, so a reader can look at the picture and at the numbers.

Samples are chosen where layout can actually go wrong: the longest lines, the
lines that just barely fit, the lines that wrap, merged sentences and card backs.

Usage:
    python tools/render_layout_samples.py --kind dialogue --limit 24
    python tools/render_layout_samples.py --kind card
    python tools/render_layout_samples.py --kind data --limit 40
    python tools/render_layout_samples.py --kind other --limit 30
"""
from pathlib import Path
import argparse
import json
import re
import sys

R9 = Path(__file__).resolve().parents[1]
ROOT = R9.parents[2]
sys.path.insert(0, str(ROOT / 'localization/editorial/r7-render/tools'))
sys.path.insert(0, str(R9 / 'tools'))
import render  # noqa: E402
import r9_targets as t  # noqa: E402

CANDIDATE = 'r9-polish-candidate47'
LINE_WIDTH = 240          # StoryFont12.LINE_WIDTH
PAGE_ROWS = 3             # dialogue page: 3 lines
CARD_COLUMNS, CARD_PX, CARD_ROWS = 16, 128, 15
DATA_PX, DATA_ROWS = 224, 3


def load(candidate):
    """Effective dictionary values: patch.pak overrides the jar at runtime.

    The jar side of a card back is the untranslated skeleton (`| | | | ...`); the
    pak side carries the prose. Rendering the jar would only produce blank grids.
    """
    render.CAND = (ROOT / 'localization/builds' / candidate).resolve()
    glyphs = {role: render.load_font(role)[0] for role in ('story12', 'classic')}
    merged = {}
    for archive in ('cosmobreeder-multi.jar', 'patch.pak'):
        state, _ = t.resource_state(render.CAND, archive, 'datav/1', 'json')
        for key, value in state['document'].items():
            if isinstance(value, str) and value.strip():
                merged[key] = value
            elif key not in merged:
                merged[key] = value
    return glyphs, merged


VSN_PREFIX = re.compile(r'^(\s*(?:text|lang\([^)]*\)|auto\([^)]*\))\s*:\s?)(.*)$')


def strip_prefix(text):
    """VSN lines carry `text: ` / `lang(x): `; the engine draws only the payload."""
    match = VSN_PREFIX.match(text)
    return match.group(2) if match else text


def advance(text, glyphs, role):
    return sum(glyphs[role].get(ord(ch), {'xadvance': 0})['xadvance'] for ch in text)


def wrap(text, glyphs, role, budget):
    """Greedy wrap exactly like the engine's pixel layout; returns display rows."""
    rows, current, width = [], '', 0
    for ch in text:
        w = glyphs[role].get(ord(ch), {'xadvance': 0})['xadvance']
        if width + w > budget and current:
            rows.append(current)
            current, width = '', 0
        current += ch
        width += w
    rows.append(current)
    return rows


def render_lines(lines, role, path, min_width=None):
    """Draw the lines, then pad the canvas out to the real panel width."""
    canvas = render.render(lines, role)
    if min_width and canvas.width < min_width:
        from PIL import Image
        panel = Image.new('RGBA', (min_width, canvas.height), (16, 16, 16, 255))
        panel.alpha_composite(canvas, (0, 0))
        canvas = panel
    path.parent.mkdir(parents=True, exist_ok=True)
    canvas.save(path)


def dialogue_samples(glyphs, document, limit):
    """Longest / borderline / wrapping dialogue lines, with the speaker prefix kept."""
    scenes = json.loads((ROOT / 'localization/editorial/r1/corpus/snapshot-03/scenes.json').read_text('utf8'))
    lines_cache = {}
    picked = []

    def lines_of(archive, entry):
        # nsfw scenes live in patch.pak; only the jar carries datay/vsn for sfw.
        if (archive, entry) not in lines_cache:
            state, _ = t.resource_state(render.CAND, archive, entry, 'line')
            lines_cache[(archive, entry)] = state['lines']
        return lines_cache[(archive, entry)]

    def entry_of(scene):
        # The occurrence catalog already records which entry each row lives in.
        for row in scene['rows']:
            if row.get('archive_entry'):
                return row['archive_entry']
        return scene['logical_path'].split('/')[0] + '/1'

    def is_player_text(text):
        """Skip the script side of the same file: conditions, braces, includes."""
        body = text.strip()
        if not body or body[0] in '{}#<' or body.startswith(('if ', 'else', 'do ')):
            return False
        if '&&' in body or '||' in body:
            return False
        return any('一' <= ch <= '鿿' for ch in body)

    for scene in scenes:
        if scene['kind'] not in ('dialogue', 'vsn'):
            continue
        entry = entry_of(scene)
        for row in scene['rows']:
            line = row.get('line')
            if line is None:
                continue
            try:
                text = lines_of('patch.pak' if scene['mode'] == 'nsfw' else 'cosmobreeder-multi.jar', entry)[line - 1]
            except IndexError:
                continue
            if not is_player_text(text):
                continue
            text = strip_prefix(text)
            width = advance(text, glyphs, 'story12')
            picked.append({'scene': scene['root'], 'entry': entry, 'line': line,
                           'text': text, 'width': width,
                           'rows': len(wrap(text, glyphs, 'story12', LINE_WIDTH)),
                           'merged': row.get('merged_or_blank_current') is True})
    picked.sort(key=lambda x: -x['width'])
    return picked[:limit]


def card_samples(glyphs, document):
    out = []
    for key in sorted(k for k in document if k.startswith('ui.card.') and document[k].strip()):
        value = document[key]
        cells = []
        total = 0
        for paragraph in value.split('|'):
            payload = paragraph.strip('\r\n')
            rows = wrap(payload, glyphs, 'classic', CARD_PX)
            total += len(rows)
            cells.extend(rows)
        out.append({'key': key, 'text': value, 'rows': total,
                    'widest': max((advance(c, glyphs, 'classic') for c in cells), default=0),
                    'cells': cells})
    return out


def data_samples(glyphs, document, limit):
    out = []
    for key in sorted(k for k in document if k.startswith(('ui.data.', 'ui.end.')) and document[k].strip()):
        value = document[key]
        rows = []
        for paragraph in value.split('|'):
            payload = paragraph.lstrip('$').strip('\r\n')
            rows.extend(wrap(payload, glyphs, 'story12', DATA_PX))
        out.append({'key': key, 'text': value, 'rows': len(rows),
                    'widest': max((advance(r, glyphs, 'story12') for r in rows), default=0),
                    'cells': rows})
    out.sort(key=lambda x: (-x['rows'], -x['widest']))
    return out[:limit]


def other_samples(glyphs, document, limit):
    """Radio, continue prompt, subtitle and pattern strings share the small fonts."""
    # Small-font containers: the continue prompt and the achievement hints.
    keys = [k for k in document
            if k.startswith(('ui.gameOver.', 'ui.options.continue')) or
               (k.startswith('ui.achievement.') and k.endswith('.hint')) and document[k].strip()]
    out = []
    for key in sorted(keys):
        value = document[key]
        role = 'classic'
        rows = []
        for paragraph in value.split('|'):
            rows.extend(wrap(paragraph.strip('\r\n'), glyphs, role, 10 * 15))
        out.append({'key': key, 'text': value, 'rows': len(rows),
                    'widest': max((advance(r, glyphs, role) for r in rows), default=0), 'cells': rows})
    out.sort(key=lambda x: -x['widest'])
    return out[:limit]


def main():
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument('--candidate', default=CANDIDATE)
    ap.add_argument('--kind', required=True, choices=('dialogue', 'card', 'data', 'other'))
    ap.add_argument('--limit', type=int, default=24)
    ap.add_argument('--output', type=Path, default=R9 / 'out/layout')
    a = ap.parse_args()

    glyphs, document = load(a.candidate)
    outdir = a.output / a.kind
    index = {'candidate': a.candidate, 'kind': a.kind, 'samples': []}

    if a.kind == 'dialogue':
        samples = dialogue_samples(glyphs, document, a.limit)
    elif a.kind == 'card':
        samples = card_samples(glyphs, document)
    elif a.kind == 'data':
        samples = data_samples(glyphs, document, a.limit)
    else:
        samples = other_samples(glyphs, document, a.limit)

    for i, sample in enumerate(samples, 1):
        name = '%s-%02d.png' % (a.kind, i)
        if a.kind == 'dialogue':
            rows = wrap(sample['text'], glyphs, 'story12', LINE_WIDTH)
            render_lines(rows, 'story12', outdir / name, min_width=LINE_WIDTH)
            sample['png'] = name
        else:
            cells = sample.pop('cells')
            panel_width = CARD_PX if a.kind == 'card' else (DATA_PX if a.kind == 'data' else LINE_WIDTH)
            render_lines(cells, 'classic' if a.kind == 'card' else 'story12', outdir / name, min_width=panel_width)
            sample['png'] = name
        index['samples'].append(sample)

    outdir.mkdir(parents=True, exist_ok=True)
    (outdir / 'index.json').write_text(json.dumps(index, ensure_ascii=False, indent=1) + '\n', encoding='utf8')
    print(json.dumps({'kind': a.kind, 'samples': len(index['samples']), 'dir': str(outdir)}, ensure_ascii=False))
    for s in index['samples'][:5]:
        label = s.get('scene') or s.get('key')
        print('  %-34s %4dpx  %d rows' % (label[:34], int(s['width'] if 'width' in s else s['widest']), s['rows']))


if __name__ == '__main__':
    main()
