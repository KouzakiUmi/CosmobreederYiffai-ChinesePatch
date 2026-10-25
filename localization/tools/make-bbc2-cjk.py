# -*- coding: utf-8 -*-
"""给 bbc2（对话/旁白/无线电主字体）做中文版：8px，与原版英文同字号同字宽。

原版 bbc2 是 size=8 / lineHeight=8 / 英文 xadvance=8。游戏按 xadvance 累加
判断折行，所以中文字宽必须也等于 8，否则：
  · 每行按 8px 预留、按实际 xadvance 绘制，宽出来的部分直接冲出文本框
  · 行高不够时中文与上一行粘连

实测约束（用户给出）：
  · 无线电消息一行 15 字
  · 剧情文字一行 20 字
两者都对应“中文字宽 = 英文字宽 = 8px”的等宽网格。

布局：原版 ASCII 图（128x128）仍在左上角，坐标不变；中文从 (128,0) 起排，
每格 8x8，xadvance=8。

    PYTHONDONTWRITEBYTECODE=1 PYTHONIOENCODING=utf-8 python localization/tools/make-bbc2-cjk.py
"""
import json
import os
import re
import shutil
import sys

from PIL import Image, ImageDraw, ImageFont

ROOT = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
LOC = os.path.join(ROOT, 'localization')
RUNTIME = os.path.join(LOC, 'runtime')
SRC_TTF = os.environ.get('COSMOBREEDER_CJK_TTF', os.path.join(ROOT, '.local', 'fonts', 'fusion-pixel-8px-proportional-zh_hans.ttf'))

PAGE = 2048
CELL = 8                     # 8x8 字形格，xadvance 也用 8
X0 = 128                     # 原版 ASCII 图宽 128
OUT_PNG = os.path.join(RUNTIME, 'bbc2-cjk-8.png')
OUT_FNT = os.path.join(RUNTIME, 'bbc2.fnt')


def main():
    # --- 原版 ASCII 图与 97 个字形定义：都在现有 cjkfont.png / bbc2.fnt 里
    src_page = Image.open(os.path.join(RUNTIME, 'cjkfont.png')).convert('RGBA')
    if src_page.size != (2048, 2048):
        sys.exit('cjkfont.png 尺寸异常: %s' % (src_page.size,))
    ascii_img = src_page.crop((0, 0, X0, 128))
    if ascii_img.getbbox() is None:
        sys.exit('cjkfont.png 左上角没有 ASCII 图')

    # 原版的 97 个字形必须全部保留（含 id=163 的 £，它 >=128 但不是中文）
    import zipfile
    GAME = os.environ.get('COSMOBREEDER_GAME_DIR', os.path.join(ROOT, '.local', 'game'))
    jar = zipfile.ZipFile(os.path.join(GAME, '_汉化补丁备份', 'cosmobreeder-multi.jar'))
    keep = {}
    for l in jar.read('bbc2.fnt').decode('utf8').splitlines():
        if l.startswith('char '):
            d = dict(re.findall(r'(\w+)=(-?\d+)', l))
            keep[int(d['id'])] = {k: int(v) for k, v in d.items()}
    print('保留原版字形: %d 个' % len(keep))

    cs = json.load(open(os.path.join(LOC, 'work', 'font8-charset.json'), encoding='utf-8'))
    need = [ch for ch in cs['all'] if ord(ch) > 127 and ord(ch) not in keep]
    print('需要的中文字形: %d 个' % len(need))

    page = Image.new('RGBA', (PAGE, PAGE), (0, 0, 0, 0))
    page.paste(ascii_img, (0, 0))

    font = ImageFont.truetype(SRC_TTF, CELL)
    cols = (PAGE - X0) // CELL
    new_chars = []
    for i, ch in enumerate(need):
        col, row = i % cols, i // cols
        bx, by = X0 + col * CELL, row * CELL
        if by + CELL > PAGE:
            sys.exit('放不下：%d 个字形' % len(need))
        cell = Image.new('RGBA', (CELL, CELL), (0, 0, 0, 0))
        # 8px 字体实际字形在 y=3..9，减去 3 才不会被 8x8 格子裁掉底部
        ImageDraw.Draw(cell).text((0, -3), ch, font=font, fill=(255, 255, 255, 255))
        page.paste(cell, (bx, by))
        new_chars.append({'id': ord(ch), 'x': bx, 'y': by, 'width': CELL, 'height': CELL,
                          'xoffset': 0, 'yoffset': 0, 'xadvance': CELL})

    page.save(OUT_PNG)
    print('wrote', OUT_PNG, page.size)

    total = len(keep) + len(new_chars)
    out = [
        'info face="BBC Micro Regular + Cosmo CJK 8" size=8 bold=0 italic=0 charset="" unicode=0 '
        'stretchH=100 smooth=1 aa=1 padding=1,1,1,1 spacing=-2,-2',
        'common lineHeight=8 base=8 scaleW=%d scaleH=%d pages=1 packed=0' % (PAGE, PAGE),
        'page id=0 file="bbc2.png"',
        'chars count=%d' % total,
    ]
    for cid in sorted(keep):
        c = keep[cid]
        out.append('char id=%-5d x=%-5d y=%-5d width=%-3d height=%-3d xoffset=%-3d yoffset=%-3d '
                   'xadvance=%-3d page=0 chnl=0' %
                   (cid, c.get('x', 0), c.get('y', 0), c.get('width', 0), c.get('height', 0),
                    c.get('xoffset', 0), c.get('yoffset', 0), c.get('xadvance', 8)))
    for c in new_chars:
        out.append('char id=%-5d x=%-5d y=%-5d width=%-3d height=%-3d xoffset=%-3d yoffset=%-3d '
                   'xadvance=%-3d page=0 chnl=0' %
                   (c['id'], c['x'], c['y'], c['width'], c['height'],
                    c['xoffset'], c['yoffset'], c['xadvance']))
    out.append('kernings count=0')          # 必须在所有 char 之后
    bak = OUT_FNT + '.10px.bak'
    head_line = open(OUT_FNT, encoding='utf-8').readline() if os.path.isfile(OUT_FNT) else ''
    if 'size=10' in head_line and not os.path.isfile(bak):
        shutil.copy2(OUT_FNT, bak)
        print('旧 10px 版备份到', os.path.basename(bak))
    with open(OUT_FNT, 'w', encoding='utf-8', newline='\n') as f:
        f.write('\n'.join(out) + '\n')
    print('wrote', OUT_FNT, '(%d glyphs, size=8 lineHeight=8 xadvance=8)' % total)

    # --- 自检
    bad = []
    for ch in '窗口大小设置音乐滤镜剧情无线电':
        cid = ord(ch)
        c = next((n for n in new_chars if n['id'] == cid), None) or keep.get(cid)
        if not c:
            bad.append((ch, 'missing'))
            continue
        g = page.crop((c['x'], c['y'], c['x'] + CELL, c['y'] + CELL))
        if g.getbbox() is None:
            bad.append((ch, 'empty'))
    if bad:
        sys.exit('自检失败: %r' % bad)
    print('自检通过')
    return 0


if __name__ == '__main__':
    sys.exit(main())
