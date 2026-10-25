# -*- coding: utf-8 -*-
"""给 classic 字体做中文版。

背景：游戏 UI 菜单（设置、暂停、标题等 14 个 class）用的是 `classic` 字体
（Press Start 2P 8px），只有英文 193 个字形。中文标签在这些界面会静默不画，
表现为「菜单一片空白，只有数字和箭头」。之前只给 `bbc2` 做了中文，
所以对话正常、菜单空白。

做法：
  1. 从原版 sprites.png 抠出 classic 那块（512x512），放在新页左上角原样保留
     —— 原有的 193 个字形坐标不用改，英文/数字显示不变
  2. 用 FusionPixel 8px 渲染全部译文用到的中文，从 (512,0) 开始排
  3. 新页 2048x2048，塞进 sprites.png 右侧原本空着的区域，图集不用变大
  4. 生成 classic.fnt：原 193 个 char 原样保留，追加中文

    PYTHONDONTWRITEBYTECODE=1 PYTHONIOENCODING=utf-8 python localization/tools/make-classic-cjk.py
"""
import hashlib
import io
import json
import os
import re
import sys
import zipfile

from PIL import Image, ImageDraw, ImageFont

ROOT = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
LOC = os.path.join(ROOT, 'localization')
sys.path.insert(0, os.path.join(LOC, 'tools'))
from codec import decrypt_file  # noqa: E402

GAME = os.environ.get('COSMOBREEDER_GAME_DIR', os.path.join(ROOT, '.local', 'game'))
ORIG_PAK = os.path.join(GAME, '_汉化补丁备份', 'patch.pak')
ORIG_JAR = os.path.join(GAME, '_汉化补丁备份', 'cosmobreeder-multi.jar')
SRC_TTF = os.environ.get('COSMOBREEDER_CJK_TTF', os.path.join(ROOT, '.local', 'fonts', 'fusion-pixel-8px-proportional-zh_hans.ttf'))

PAGE = 2048          # 新页尺寸
CELL = 8             # 8px 字形格
X0 = 512             # 中文从 x=512 起，左边 512 留给原 classic 图
OUT_PNG = os.path.join(LOC, 'runtime', 'classic-cjk.png')
OUT_FNT = os.path.join(LOC, 'runtime', 'classic.fnt')


def atlas_region(atlas, name):
    m = re.search(r'^' + re.escape(name) + r'\n((?:[ \t].*\n)+)', atlas, re.M)
    if not m:
        sys.exit('atlas 里没有 region: ' + name)
    body = m.group(1)
    xy = re.search(r'xy: (\d+), (\d+)', body)
    wh = re.search(r'size: (\d+), (\d+)', body)
    return int(wh.group(1)), int(wh.group(2)), int(xy.group(1)), int(xy.group(2))


def main():
    # --- 1. 原 classic 图
    z = zipfile.ZipFile(ORIG_PAK)
    atlas = decrypt_file(z.read('dataq/5')).decode('utf8')
    w, h, x, y = atlas_region(atlas, 'classic')
    print('原 classic 区域: %dx%d @ (%d,%d)' % (w, h, x, y))
    sheet = Image.open(io.BytesIO(decrypt_file(z.read('dataq/6')))).convert('RGBA')
    classic_img = sheet.crop((x, y, x + w, y + h))
    print('  抠出 %dx%d' % classic_img.size)
    if classic_img.size != (512, 512):
        sys.exit('预期 512x512，实际 %s' % (classic_img.size,))

    # --- 2. 原 fnt
    jar = zipfile.ZipFile(ORIG_JAR)
    fnt_text = jar.read('classic.fnt').decode('utf8')
    # BMFont 要求 kernings 在所有 char 之后；解析器读到它就会结束字符段
    head = [l for l in fnt_text.splitlines() if not l.startswith(('char ', 'kernings '))]
    chars = [l for l in fnt_text.splitlines() if l.startswith('char ')]
    print('原 fnt: %d 个 char' % len(chars))

    def parse_char(line):
        d = dict(re.findall(r'(\w+)=(-?\d+)', line))
        return {k: int(v) for k, v in d.items()}

    orig = {}
    for line in chars:
        c = parse_char(line)
        orig[c['id']] = c

    # --- 3. 需要的中文字形
    cs = json.load(open(os.path.join(LOC, 'work', 'font8-charset.json'), encoding='utf-8'))
    need = [ch for ch in cs['all'] if ord(ch) not in orig and ord(ch) > 127]
    print('需要新增的中文字形: %d' % len(need))

    # --- 4. 排版：原图在左上，中文从 (512,0) 起逐格排
    page = Image.new('RGBA', (PAGE, PAGE), (0, 0, 0, 0))
    page.paste(classic_img, (0, 0))

    font = ImageFont.truetype(SRC_TTF, CELL)
    cols = (PAGE - X0) // CELL
    new_chars = []
    for i, ch in enumerate(need):
        col, row = i % cols, i // cols
        bx, by = X0 + col * CELL, row * CELL
        if by + CELL > PAGE:
            sys.exit('字库页放不下：%d 个字形' % len(need))
        cell = Image.new('RGBA', (CELL, CELL), (0, 0, 0, 0))
        d = ImageDraw.Draw(cell)
        # 8px 字体实际字形占 y=3..9，不减去 3 会被 8x8 格子裁掉底部两行
        d.text((0, -3), ch, font=font, fill=(255, 255, 255, 255))
        bbox = cell.getbbox()
        page.paste(cell, (bx, by))
        # 全部按 8x8 等宽处理，xadvance=8，与原英文节奏一致
        new_chars.append({'id': ord(ch), 'x': bx, 'y': by, 'width': CELL, 'height': CELL,
                          'xoffset': 0, 'yoffset': 0, 'xadvance': CELL, 'page': 0, 'chnl': 0})
        if bbox is None:
            print('  警告：%r 渲染为空' % ch)

    print('  排了 %d 个字形，占 %d 行' % (len(new_chars), (len(need) + cols - 1) // cols))

    page.save(OUT_PNG)
    print('wrote', OUT_PNG, page.size)

    # --- 5. 新 fnt
    out = []
    for line in head:
        if line.startswith('info '):
            line = re.sub(r'face="[^"]*"', 'face="Press Start 2P + Cosmo CJK 8"', line)
            line = re.sub(r'size=\d+', 'size=8', line)
        if line.startswith('common '):
            line = re.sub(r'scaleW=\d+', 'scaleW=%d' % PAGE, line)
            line = re.sub(r'scaleH=\d+', 'scaleH=%d' % PAGE, line)
        out.append(line)
    total = len(orig) + len(new_chars)
    out = [l.replace('chars count=%d' % len(orig), 'chars count=%d' % total)
           if l.startswith('chars count=') else l for l in out]
    for cid, c in sorted(orig.items()):
        out.append('char id=%-5d x=%-5d y=%-5d width=%-3d height=%-3d xoffset=%-3d yoffset=%-3d '
                   'xadvance=%-3d page=0 chnl=0' %
                   (cid, c['x'], c['y'], c['width'], c['height'],
                    c.get('xoffset', 0), c.get('yoffset', 0), c.get('xadvance', 0)))
    for c in new_chars:
        out.append('char id=%-5d x=%-5d y=%-5d width=%-3d height=%-3d xoffset=%-3d yoffset=%-3d '
                   'xadvance=%-3d page=0 chnl=0' %
                   (c['id'], c['x'], c['y'], c['width'], c['height'],
                    c['xoffset'], c['yoffset'], c['xadvance']))
    out.append('kernings count=0')
    with open(OUT_FNT, 'w', encoding='utf-8', newline='\n') as f:
        f.write('\n'.join(out) + '\n')
    print('wrote', OUT_FNT, '(%d glyphs)' % total)

    # --- 6. 自检：随机抽几个字，确认有像素
    bad = []
    for ch in need[:40]:
        cid = ord(ch)
        c = next(c for c in new_chars if c['id'] == cid)
        g = page.crop((c['x'], c['y'], c['x'] + c['width'], c['y'] + c['height']))
        if g.getbbox() is None:
            bad.append(ch)
    if bad:
        sys.exit('这些字渲染为空: %r' % bad)
    print('自检通过：抽样字形都有像素')
    return 0


if __name__ == '__main__':
    sys.exit(main())
