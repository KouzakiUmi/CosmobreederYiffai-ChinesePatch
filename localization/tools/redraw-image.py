#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""用游戏自带的中文像素字体（BBC Micro + Cosmo CJK 12）重绘位图上的英文文字。

为什么不用 AI 生图：这些图是 256x224 的像素画，字体是 8px 网格的 BBC Micro。
AI 编辑无法保证像素网格对齐，一定会糊。直接复用游戏内同一字族的 CJK 12px
字形贴回去，风格天然一致，且每个像素都可控。

    PYTHONDONTWRITEBYTECODE=1 PYTHONIOENCODING=utf-8 python localization/tools/redraw-image.py --asset <asset_id>

产物写到 work/image-staging/，不碰 assets/fixed/ 与游戏安装目录。
"""
import argparse
import os
import re
import sys

from PIL import Image

ROOT = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
LOC = os.path.join(ROOT, 'localization')


def load_font(fnt_path):
    chars = {}
    for line in open(fnt_path, encoding='utf-8'):
        m = re.match(
            r'char id=(\d+)\s+x=(-?\d+)\s+y=(-?\d+)\s+width=(\d+)\s+height=(\d+)\s+'
            r'xoffset=(-?\d+)\s+yoffset=(-?\d+)\s+xadvance=(-?\d+)', line)
        if m:
            i, x, y, w, h, xo, yo, xa = map(int, m.groups())
            chars[i] = dict(x=x, y=y, w=w, h=h, xo=xo, yo=yo, xa=xa)
    return chars


class Painter:
    def __init__(self, img, sheet, chars):
        self.img = img
        self.sheet = sheet
        self.chars = chars

    def measure(self, text):
        return sum(self.chars[ord(c)]['xa'] for c in text if ord(c) in self.chars)

    def draw(self, text, x, baseline, color, align='left', right_edge=None):
        """baseline 是字形基线；中文 yoffset=-3 即字形上沿在 baseline-3。"""
        total = self.measure(text)
        if align == 'right' and right_edge is not None:
            x = right_edge - total
        elif align == 'center' and right_edge is not None:
            x = right_edge - total // 2
        cx = x
        for ch in text:
            i = ord(ch)
            g = self.chars.get(i)
            if not g:
                raise SystemExit('glyph missing for %r (U+%04X)' % (ch, i))
            if g['w'] > 0 and g['h'] > 0:
                src = self.sheet.crop((g['x'], g['y'], g['x'] + g['w'], g['y'] + g['h']))
                solid = Image.new('RGBA', src.size, tuple(color) + (255,))
                self.img.paste(solid, (cx + g['xo'], baseline + g['yo']), src)
            cx += g['xa']
        return cx


def clear_box(img, box, fill):
    """把矩形区域填成纯色。用于擦掉原英文。"""
    x0, y0, x1, y1 = box
    img.paste(Image.new('RGB', (x1 - x0 + 1, y1 - y0 + 1), fill), (x0, y0))


# ---------------------------------------------------------------- 每张图的工单
# 坐标来自对原图的像素扫描。
#
# A4b6160b 与 Ada8d2a93 是同一张启动画面的两个变体，布局完全一致，
# 只有顶部横幅不同：前者横幅里有 THIS SOFTWARE IS FOR ADULTS ONLY，
# 后者横幅是空的（纯黄底 + 斜纹边框）。所以横幅的「干净背景」可以直接
# 从后者复制过来——比自己重建斜纹可靠得多。
_PRETITLE_BODY = dict(
    fills=[
        ((0, 38, 255, 64), (0, 0, 0)),   # 原 THIS GAME IS BEST PLAYED / WITH A CONTROL PAD
        ((0, 79, 255, 94), (0, 0, 0)),   # 原 TO ACCESS GAME CONFIGURATION（12px 字要占到 94）
        ((0, 95, 255, 113), (0, 0, 0)),  # 原 PRESS (L+R) ON GAMEPAD / OR PRESS (Q+E) ON KEYBOARD
    ],
    texts=[
        dict(text='本游戏建议使用手柄游玩', align='center', right_edge=128, baseline=48, color=(248, 184, 0)),
        dict(text='访问游戏设置', align='center', right_edge=128, baseline=86, color=(248, 184, 0)),
        dict(text='按手柄 L+R', align='center', right_edge=67, baseline=103, color=(248, 184, 0)),
        dict(text='或', align='center', right_edge=128, baseline=103, color=(248, 184, 0)),
        dict(text='按键盘 Q+E', align='center', right_edge=188, baseline=103, color=(248, 184, 0)),
    ],
)

JOBS = {
    # 卡片查看器标题条：白条 y=1..15，左 COSMOCARD VIEWER，右上两行 "A" KEY TO / FLIP CARD
    'Acfb74ff046445762b007': dict(
        out='card-viewer.png',
        fills=[((3, 1, 252, 15), (252, 252, 252))],
        texts=[
            # 左：宇宙卡查看器  6 字 * 12px = 72px，从 x=8 起
            dict(text='宇宙卡查看器', x=8, baseline=5, color=(0, 0, 252)),
            # 右：按「A」翻卡，右对齐到 x=249
            dict(text='按「A」翻卡', align='right', right_edge=249, baseline=5, color=(0, 0, 252)),
        ],
    ),
    # 图鉴标题条：白条 y=1..23，两行字（原 2..13 与 17..23）。
    # 12px 中文两行需要 24px，白条只有 23px；靠字形顶部 1px 空白错开：
    # baseline=4 时笔画落在 y=2..12，baseline=15 时落在 y=13..23，正好不重叠。
    'A3ad10e4fc08b09e2bef4': dict(
        out='bestiary-title.png',
        fills=[((3, 1, 252, 23), (252, 252, 252))],
        texts=[
            dict(text='图鉴子菜单', x=8, baseline=4, color=(0, 0, 252)),
            dict(text='-选择下方条目查看-', align='center', right_edge=128, baseline=15, color=(0, 0, 252)),
        ],
    ),
    # 启动画面（手柄提示版）：横幅需要从空横幅版借背景
    'A4b6160b4569cc8b87687': dict(
        out='pretitle-gamepad.png',
        template=('Ada8d2a93e89e1525cbf1', [(0, 10, 255, 21)]),
        fills=[
            ((0, 10, 255, 21), (248, 184, 0)),  # 黄底，随后画棕字
        ] + _PRETITLE_BODY['fills'],
        texts=[
            dict(text='本软件仅限成人使用', align='center', right_edge=128, baseline=13, color=(80, 48, 0)),
        ] + _PRETITLE_BODY['texts'],
    ),
    # 启动画面（空横幅版）：横幅本来就没字，只改下部
    'Ada8d2a93e89e1525cbf1': dict(
        out='pretitle-plain.png',
        fills=_PRETITLE_BODY['fills'],
        texts=_PRETITLE_BODY['texts'],
    ),
}


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument('--asset', required=True)
    a = ap.parse_args()

    job = JOBS.get(a.asset)
    if not job:
        sys.exit('no redraw job for asset %s (known: %s)' % (a.asset, ', '.join(JOBS)))

    src = os.path.join(LOC, 'assets', 'fixed', a.asset + '.png')
    if not os.path.exists(src):
        sys.exit('missing source image %s' % src)

    img = Image.open(src).convert('RGB')
    sheet = Image.open(os.path.join(LOC, 'runtime', 'cjkfont.png')).convert('RGBA')
    chars = load_font(os.path.join(LOC, 'runtime', 'bbc2.fnt'))

    # 1. 记录原始像素，供事后核对"只有指定区域变了"
    before = img.copy()

    # 2. 从模板图借干净背景（用于横幅这种带装饰底纹、无法靠填色重建的区域）
    if job.get('template'):
        tpl_asset, boxes = job['template']
        tpl_path = os.path.join(LOC, 'assets', 'fixed', tpl_asset + '.png')
        if not os.path.exists(tpl_path):
            sys.exit('missing template image %s' % tpl_path)
        tpl = Image.open(tpl_path).convert('RGB')
        for x0, y0, x1, y1 in boxes:
            img.paste(tpl.crop((x0, y0, x1 + 1, y1 + 1)), (x0, y0))

    # 3. 擦掉原英文
    for box, fill in job['fills']:
        clear_box(img, box, fill)

    # 4. 画中文
    p = Painter(img, sheet, chars)
    for t in job['texts']:
        p.draw(t['text'], t.get('x', 0), t['baseline'], t['color'],
               align=t.get('align', 'left'), right_edge=t.get('right_edge'))

    # 5. 核对：改动必须落在 fills / template 声明的矩形里
    px0, px1 = img.load(), before.load()
    w, h = img.size
    allowed = []
    for (x0, y0, x1, y1), _ in job['fills']:
        allowed.append((x0, y0, x1, y1))
    if job.get('template'):
        for x0, y0, x1, y1 in job['template'][1]:
            allowed.append((x0, y0, x1, y1))
    stray = 0
    for y in range(h):
        for x in range(w):
            if px0[x, y] != px1[x, y]:
                if not any(a0 <= x <= a1 and b0 <= y <= b1 for a0, b0, a1, b1 in allowed):
                    stray += 1
    if stray:
        sys.exit('FAIL: %d pixels changed outside the declared boxes' % stray)

    outdir = os.path.join(LOC, 'work', 'image-staging')
    os.makedirs(outdir, exist_ok=True)
    out = os.path.join(outdir, job['out'])
    img.save(out)
    print('wrote %s (%dx%d)' % (out, img.size[0], img.size[1]))
    print('changed pixels all inside declared boxes: OK')
    return 0


if __name__ == '__main__':
    sys.exit(main())
