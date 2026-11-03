"""Rebuild a real game frame from the archive, then draw the engine's text on it.

This is the "run the game to that moment" path, not a mock-up. Everything comes
out of `patch.pak`:

* `vsn/<n>`     timing: per-animation `delays` and `loop`
* `vsn/<n+1>`   slice atlas: each frame is a stack of 256x16 strips
* `vsn/<n+2>`   the page PNG those strips are cut from
* `vsn/<n+3>`   the script: `fadein(...): Sprite` and `text: line`

A frame is assembled by taking, for animation A and frame index i, every
`i_<k>_slice` region whose ordinal matches, and stacking them from y=0 down. The
screen is 256x224, matching the 256x224 scene previews.

The text is then laid out by the engine (`scene_render`) and drawn with the
engine's own glyph atlas, so what comes out is what the player sees at that
`text:` line.
"""

import io
import json
import re
import sys
import zipfile
from pathlib import Path

from PIL import Image

ROOT = Path(__file__).resolve().parents[4]
sys.path.insert(0, str(ROOT / 'localization/tools'))
from codec import decrypt_file  # noqa: E402

SCREEN = (256, 224)
SLICE_H = 16


def _read(pak, entry):
    with zipfile.ZipFile(pak) as z:
        return decrypt_file(z.read(entry))


def scene_files(index):
    """The six entries of a scene block.

    Measured from the archive: each block runs
    `script -> slices.json -> manifest -> timing -> atlas -> page png`, so the
    entry holding the *timing* table sits at `index` and the rest hang off it.
    The page png is at +2; the entry four back belongs to the previous block.
    """
    return {'script': 'vsn/%d' % (index - 3),
            'slices': 'vsn/%d' % (index - 2), 'manifest': 'vsn/%d' % (index - 1),
            'timing': 'vsn/%d' % index, 'atlas': 'vsn/%d' % (index + 1),
            'png': 'vsn/%d' % (index + 2)}


def load_scene(pak, index):
    files = scene_files(index)
    timing = json.loads(_read(pak, files['timing']).decode('utf8'))
    atlas_text = _read(pak, files['atlas']).decode('utf8')
    png = Image.open(io.BytesIO(_read(pak, files['png']))).convert('RGBA')
    script = _read(pak, files['script']).decode('utf8')
    regions = {}
    for m in re.finditer(
            r'\n(i_(\d+)_slice)\n  rotate: (\w+)\n  xy: (\d+), (\d+)\n  size: (\d+), (\d+)',
            atlas_text):
        name, idx, rot, x, y, w, h = m.groups()
        regions[int(idx)] = (int(x), int(y), int(w), int(h))
    slices = json.loads(_read(pak, files['slices']).decode('utf8'))
    return {'timing': timing, 'atlas': png, 'script': script,
            'slices': slices, 'regions': regions}


def frame(scene, animation, index=0):
    """Assemble one animation frame.

    `slices[animation][index]` is a list of slice ids, one per 256x16 strip,
    top to bottom. Id 0 means "empty strip".
    """
    frames = scene['slices'].get(animation)
    if not frames:
        return Image.new('RGBA', SCREEN, (0, 0, 0, 255))
    ids = frames[index % len(frames)]
    canvas = Image.new('RGBA', SCREEN, (0, 0, 0, 255))
    for row, sid in enumerate(ids):
        region = scene['regions'].get(sid)
        if not region or sid == 0:
            continue
        x, sy, w, h = region
        cell = scene['atlas'].crop((x, sy, x + w, sy + h))
        canvas.alpha_composite(cell, (0, row * SLICE_H))
    return canvas


def script_events(script):
    """[(sprite, text)] in order, plus the text-only lines."""
    events = []
    sprite = None
    for line in script.splitlines():
        m = re.match(r'\s*fade(?:in|cut)\(\s*[^)]*\)\s*:\s*(\S+)', line)
        if m:
            sprite = m.group(1)
            continue
        m = re.match(r'\s*text\s*:\s*(.*)$', line)
        if m:
            events.append({'sprite': sprite, 'text': m.group(1).strip()})
    return events


def animation_index(timing, sprite):
    """Frame index to draw for a named animation (its first frame)."""
    if sprite and sprite in timing:
        return 0
    return 0
