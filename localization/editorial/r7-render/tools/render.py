"""用候选归档里的真实位图字体渲染文本，模拟改动前后的画面。

字体：candidate11 的 story12.fnt（12px，LINE_WIDTH=240，超宽在游戏里会抛异常）
与 classic.fnt（道具/名称用 8px）。图集：r28-font/bbc2.png、r28-font/classic.png。
字体度量与像素全部取自候选归档，不做近似。
"""
import io
import sys
import zipfile
from pathlib import Path

from PIL import Image

ROOT = Path(__file__).resolve().parents[4]
LOC = ROOT / 'localization'
CAND = LOC / 'builds' / 'r6-consistency-candidate11'

FONTS = {
    'story12': ('fonts/story12.fnt', 'r28-font/bbc2.png'),
    'classic': ('fonts/classic.fnt', 'r28-font/classic.png'),
}


def parse_fnt(text):
    glyphs = {}
    meta = {}
    for line in text.splitlines():
        parts = line.split()
        if not parts:
            continue
        tag = parts[0]
        attrs = {}
        for tok in parts[1:]:
            if '=' in tok:
                k, _, v = tok.partition('=')
                attrs[k] = v.strip('"')
        if tag == 'common':
            meta.update(common=attrs)
        elif tag == 'char':
            cp = int(attrs['id'])
            glyphs[cp] = {k: int(attrs[k]) for k in
                          ('x', 'y', 'width', 'height', 'xoffset', 'yoffset', 'xadvance')}
    meta['lineHeight'] = int(meta['common']['lineHeight'])
    return glyphs, meta


def load_font(role):
    fnt_rel, png_rel = FONTS[role]
    fnt = (CAND / fnt_rel).read_text('utf-8')
    glyphs, meta = parse_fnt(fnt)
    with zipfile.ZipFile(CAND / 'cosmobreeder-multi.jar') as z:
        atlas = Image.open(io.BytesIO(z.read(png_rel))).convert('RGBA')
    return glyphs, meta, atlas


def line_width(text, glyphs):
    return sum(glyphs.get(ord(c), {'xadvance': 0})['xadvance'] for c in text)


def render(lines, role='story12', padding=4):
    glyphs, meta, atlas = load_font(role)
    lh = meta['lineHeight']
    width = max([line_width(l, glyphs) for l in lines] + [1]) + padding * 2
    height = lh * len(lines) + padding * 2
    canvas = Image.new('RGBA', (width, height), (16, 16, 16, 255))
    for row, text in enumerate(lines):
        pen = padding
        top = padding + row * lh
        for ch in text:
            g = glyphs.get(ord(ch))
            if g is None:
                pen += 0
                continue
            if g['width'] and g['height']:
                box = (g['x'], g['y'], g['x'] + g['width'], g['y'] + g['height'])
                glyph = atlas.crop(box)
                canvas.alpha_composite(glyph, (pen + g['xoffset'], top + g['yoffset']))
            pen += g['xadvance']
    return canvas


def save(canvas, name):
    out = Path(__file__).resolve().parents[1] / 'out' / name
    out.parent.mkdir(parents=True, exist_ok=True)
    canvas.save(out)
    return out


def measure(lines, role='story12'):
    glyphs, meta, _ = load_font(role)
    return [line_width(l, glyphs) for l in lines], meta['lineHeight']


if __name__ == '__main__':
    # 自检：渲染一段已知文本并输出宽度
    sample = ['精灵的', '高阶女士', '恩莉耶，']
    widths, lh = measure(sample)
    print('self-check widths:', widths, 'lineHeight:', lh)
    print('png:', save(render(sample), 'selfcheck.png'))
