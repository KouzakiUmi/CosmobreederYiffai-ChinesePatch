"""Render the game's real scenes with the shipped Chinese text.

This is the end-to-end check: a frame rebuilt from the archive's own slices,
with the text the candidate actually ships, laid out by the engine's own
`SubtitleLayout`, drawn with the jar's own glyph atlas.

Everything on screen comes out of `patch.pak` / the candidate jar:

| layer | source |
| --- | --- |
| background art | `vsn/<n>` slice atlas + page png, assembled per `slices.json` |
| Chinese text | the candidate's `vsn` script (`text:` lines) |
| line breaks | `SubtitleLayout.pages` (240px, 3 rows) via `scene_render` |
| glyph pixels | `story12.fnt` + `r28-font/bbc2.png` from the jar |

What is *not* from the archive: the vertical placement of the subtitle band.
It was measured from `research/intro-*.png` (a real capture, 784x711, canvas
starting at y=32, scaled 3.06x) at game-space y≈161..173, and is recorded in
`TEXT_BAND` so a real dialogue capture can correct it later.
"""

import sys
from pathlib import Path

from PIL import Image

sys.path.insert(0, str(Path(__file__).resolve().parent))
import asset_render as AR  # noqa: E402
import scene_frame as SF  # noqa: E402
import scene_render as SR  # noqa: E402

ROOT = Path(__file__).resolve().parents[4]
# Measured, not authored: see the module docstring.
TEXT_BAND = 168
LINE_STEP = 13
LEFT = 8


def compose(candidate, pak, scene_index, event_index, out):
    """Draw scene `scene_index`, text event `event_index`, to `out`."""
    scene = SF.load_scene(pak, scene_index)
    events = SF.script_events(scene['script'])
    if not events:
        raise ValueError('scene %d has no text events' % scene_index)
    event = events[event_index]

    res = SR.render(str(candidate), [
        ('t', 'subtitle', 'x', 'x', 0, event['text'])])
    pages = [v for k, v in res.items()][0]['pages']

    frame = SF.frame(scene, event['sprite'], 0).copy()
    glyphs, atlas = AR.load_font(str(candidate), 'story12')
    y = TEXT_BAND
    for line in pages[0]['lines']:
        if not line:
            y += LINE_STEP
            continue
        AR.draw_text(frame, glyphs, atlas, line, LEFT, y)
        y += LINE_STEP
    frame.save(out)
    return {'text': event['text'], 'lines': pages[0]['lines'], 'pages': len(pages)}


def dialogue_scenes(pak):
    """Scene indices whose script contains `text:` lines."""
    out = []
    for index in range(140, 404, 6):
        try:
            scene = SF.load_scene(pak, index)
        except Exception:
            continue
        if SF.script_events(scene['script']):
            out.append(index)
    return out
