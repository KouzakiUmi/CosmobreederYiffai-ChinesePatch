"""Composite the real pages onto a picture, using the game's own glyph atlas.

`scene_render.render` gives the pages the engine would draw. This module draws
them with the shipped bitmap font — the same `bbc2.png` / `story12.fnt` pair the
jar carries — so the result is what the player's eyes get, not an ASCII
approximation.

What is real here:

* glyph pixels and advances, read from the jar's `.fnt` + atlas;
* line breaks and page splits, from `DialogueWrap` via `scene_render`;
* colours, sampled from the game's own screenshots.

What is not: the dialogue frame is drawn to match the game's look, not lifted
from an asset we do not have. `frame_geometry()` records what was assumed so a
later pass with real art can replace it without touching the text path.
"""

import io
import zipfile
from pathlib import Path

from PIL import Image, ImageDraw

ROOT = Path(__file__).resolve().parents[4]

# Sampled from research/intro-*.png, which are real game screenshots:
# background (2,2,0), amber ink (255,155,0) / (232,176,0), white (243,243,243).
INK = (255, 155, 0, 255)
PANEL = (2, 2, 0, 255)
FRAME = (232, 176, 0, 255)

FONT_ENTRIES = {
    'story12': ('story12.fnt', 'r28-font/bbc2.png'),
    'bbc2': ('bbc2.fnt', 'r28-font/bbc2.png'),
}


def load_font(candidate, role='story12'):
    """Parse the jar's `.fnt` and atlas into {codepoint: (x, y, w, h, xadvance)}."""
    jar = Path(candidate).resolve() / 'cosmobreeder-multi.jar'
    fnt_name, png_name = FONT_ENTRIES[role]
    with zipfile.ZipFile(jar) as z:
        text = z.read(fnt_name).decode('utf8')
        atlas = Image.open(io.BytesIO(z.read(png_name))).convert('RGBA')
    glyphs = {}
    for line in text.splitlines():
        if not line.startswith('char '):
            continue
        fields = dict(p.split('=', 1) for p in line.split() if '=' in p)
        cp = int(fields['id'])
        glyphs[cp] = (int(fields['x']), int(fields['y']), int(fields['width']),
                      int(fields['height']), int(fields['xoffset']), int(fields['yoffset']),
                      int(fields['xadvance']))
    return glyphs, atlas


def draw_text(image, glyphs, atlas, text, x, y, scale=1, ink=INK):
    """Blit one line of text at (x, y); returns the advance used.

    The atlas stores white glyphs; the game tints them, so the alpha channel is
    used as a mask and recoloured here rather than compositing the white pixels.
    """
    cursor = x
    for ch in text:
        g = glyphs.get(ord(ch))
        if g is None:
            cursor += 8 * scale
            continue
        gx, gy, gw, gh, gxo, gyo, adv = g
        if gw and gh:
            cell = atlas.crop((gx, gy, gx + gw, gy + gh))
            if scale != 1:
                cell = cell.resize((gw * scale, gh * scale), Image.NEAREST)
            mask = cell.split()[-1]
            tinted = Image.new('RGBA', cell.size, ink)
            tinted.putalpha(mask)
            image.alpha_composite(tinted, (cursor + gxo * scale, y + gyo * scale))
        cursor += adv * scale
    return cursor - x


def line_width(glyphs, text, scale=1):
    return sum(glyphs.get(ord(c), (0, 0, 0, 0, 0, 0, 8))[6] for c in text) * scale


def frame_geometry(lines, scale=1, pad=16, line_gap=6):
    """Box size for a page. Assumed, not taken from an asset — see module doc."""
    width = max((line_width(glyphs_placeholder, l, scale) for l in lines), default=0)
    return width + pad * 2, len(lines) * (12 * scale + line_gap) + pad * 2


glyphs_placeholder = {}


def render_page(glyphs, atlas, lines, scale=1, pad=16, line_gap=6):
    """Draw a framed dialogue page containing `lines`."""
    global glyphs_placeholder
    glyphs_placeholder = glyphs
    w, h = frame_geometry([l for l in lines if l], scale, pad, line_gap)
    img = Image.new('RGBA', (max(w, 260), h), (0, 0, 0, 0))
    d = ImageDraw.Draw(img)
    d.rectangle([0, 0, img.width - 1, img.height - 1], fill=PANEL, outline=FRAME)
    y = pad
    for line in lines:
        if not line:
            y += 12 * scale + line_gap
            continue
        draw_text(img, glyphs, atlas, line, pad, y, scale)
        y += 12 * scale + line_gap
    return img
