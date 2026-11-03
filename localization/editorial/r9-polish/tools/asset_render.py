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

# Colours come from two different sources, and they do not agree.
#
# `shaders/vsn_term_shade.frag` and `cosmo_term_shade.frag` define
#   inner_color = vec4(0.972, 0.721, 0.0, 1.0)   -> (248, 184, 0)
#   glow_color  = vec4(0.313, 0.188, 0.0, 1.0)   -> ( 80,  48, 0)
#
# A real capture (research/intro-05.png) contains NEITHER of those two colours;
# it has (255,155,0), (232,176,0) and (88,57,0) instead, and the counts are
# exact 0 for the shader constants. So that screen was not shaded by
# vsn_term_shade. (80,48,0) does occur in scene pages, i.e. it is authored art.
#
# The amber the player actually sees on the pretitle is therefore produced
# somewhere else -- most likely by the palette remap (`vsn_fade` + a `*LUT.png`
# texture). That path is NOT reproduced here.
#
# Which value to use:
#   INK_DRAWN  -- the shader constant; correct for a layer that goes through
#                 vsn_term_shade, wrong for the pretitle capture.
#   INK_CAPTURED -- measured off the real screenshot; use when matching that look.
#
# Neither is "the" answer until the remap path is settled. Rendering with
# INK_DRAWN and calling it a real screenshot would be wrong.
INK_DRAWN = (248, 184, 0, 255)
GLOW = (80, 48, 0, 255)
INK_CAPTURED = (255, 155, 0, 255)
INK = INK_DRAWN
PANEL = (2, 2, 0, 255)
FRAME = (248, 184, 0, 255)

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


def shade_terminal(layer, texture_size=(256, 224), v_top=1.0, v_bottom=0.0):
    """Reimplement `vsn_term_shade.frag` on a text layer.

    Source of the constants: `shaders/vsn_term_shade.frag` in the jar. Source of
    `texture_size`: `PRG/jl` sets the uniform to 256.0f / 224.0f at bytecode
    offsets 108..132, and applies the shader to the *text* layer before
    compositing -- so a correct render shades the text alone, then composites
    over the background, which is what `real_scene.compose` does.

    The rule, in order:
      * pixel == (0,0,255,255)  -> glow
      * pixel.red > 0           -> ink        (alpha is NOT consulted)
      * otherwise sample left, right and v-; unless the row falls on the
        periodic 8-row gap, also sample v+; glow if any sampled red > 0,
        else fully transparent.

    Sampling is nearest with clamp-to-edge, matching the atlas' declared
    `Nearest, Nearest` / `repeat: none`. Linear filtering or sub-region UVs
    would need a different sampler, so do not reuse this outside that setup.
    """
    from PIL import Image
    import math
    src = layer.convert('RGBA')
    w, h = src.size
    tw, th = map(float, texture_size)
    if min(w, h, tw, th) <= 0 or v_top == v_bottom:
        raise ValueError('invalid dimensions/UV interval')
    pix = src.load()
    out = Image.new('RGBA', (w, h))
    dst = out.load()

    def sample(u, v):
        x = min(w - 1, max(0, math.floor(u * w)))
        y = min(h - 1, max(0, math.floor(
            (v - v_top) / (v_bottom - v_top) * h)))
        return pix[x, y]

    for y in range(h):
        v = v_top + (v_bottom - v_top) * ((y + 0.5) / h)
        for x in range(w):
            u = (x + 0.5) / w
            base = pix[x, y]
            if base == (0, 0, 255, 255):
                dst[x, y] = GLOW
            elif base[0] > 0:
                dst[x, y] = INK
            else:
                red = (sample(u - 1 / tw, v)[0]
                       + sample(u + 1 / tw, v)[0]
                       + sample(u, v - 1 / th)[0])
                # int(mod(py + 1.0, 8.0)) != 0; a plain `y % 8` loses the
                # half-pixel centre and the UV direction.
                if int((v * th + 1.0) % 8.0) != 0:
                    red += sample(u, v + 1 / th)[0]
                dst[x, y] = GLOW if red > 0 else (0, 0, 0, 0)
    return out
