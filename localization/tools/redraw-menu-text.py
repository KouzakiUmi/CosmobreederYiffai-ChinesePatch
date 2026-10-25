# -*- coding: utf-8 -*-
"""把界面背景位图里的烘焙英文重绘成中文。

这些背景图（CosmoSaveMenuBG / CosmoItemMenuBG / ...）是纯三色位图：
  黑 (0,0,0) 底、白 (252,252,252) 边框、蓝 (0,0,252) 文字。
所以可以精确定位文字像素、擦成黑、再用同色画中文，不破坏边框。

    python localization/tools/redraw-menu-text.py --list
    python localization/tools/redraw-menu-text.py --scene save --out localization/work/menu/save.png
"""
import json
import os
import re
import sys
import zipfile

from PIL import Image, ImageDraw, ImageFont

ROOT = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
LOC = os.path.join(ROOT, 'localization')
RUNTIME = os.path.join(LOC, 'runtime')
GAME = os.environ.get('COSMOBREEDER_GAME_DIR', os.path.join(ROOT, '.local', 'game'))
TTF = os.environ.get('COSMOBREEDER_CJK_TTF', os.path.join(ROOT, '.local', 'fonts', 'fusion-pixel-8px-proportional-zh_hans.ttf'))

BLUE = (0, 0, 252, 255)
BLACK = (0, 0, 0, 255)

# 每个场景：背景 region 名，要擦掉的文字带（会跳过边框列），以及要画的中文块
# block: (x, y, text, align)  align: left/center，center 时需要给 (x0,x1)
SCENES = {
    'save': {
        'region': 'CosmoSaveMenuBG',
        # 文字带（y0,y1）—— 里面所有非边框蓝像素都擦掉
        'erase': [(1, 14), (24, 40), (196, 220)],
        'blocks': [
            (8, 2, '个人档案写入器', 'left'),
            (8, 2, '', 'left'),          # 占位，下面单独处理
        ],
        'texts': {
            # (x0,x1,y,text)  center=True 表示在该栏内居中
            'title':  (8, 250, 2, '个人档案写入器', False),
            'col1a':  (8, 98, 24, '文件名', True),
            'col1b':  (8, 98, 32, '存档数据', True),
            'col2a':  (104, 205, 24, '等级 尝试', True),
            'col2b':  (104, 205, 32, '位置 通信', True),
            'col3':   (212, 250, 24, '时间', True),
            'tip1':   (9, 250, 196, '默认按键设置：', False),
            'tip2':   (9, 250, 204, '用 (Q)+(E) 进入配置菜单', False),
            'tip3':   (9, 250, 212, '或 (左肩)+(右肩)', False),
        },
    },
}


def load_bg(region):
    sys.path.insert(0, os.path.join(LOC, 'tools'))
    from codec import decrypt_file
    z = zipfile.ZipFile(os.path.join(GAME, '_汉化补丁备份', 'patch.pak'))
    idx = json.loads(decrypt_file(z.read('dataq/0')))
    atlas = decrypt_file(z.read('dataq/' + str(idx['/sprites.atlas']))).decode('utf8')
    sheet = Image.open(__import__('io').BytesIO(decrypt_file(z.read('dataq/' + str(idx['/sprites.png']))))).convert('RGBA')
    nl = chr(92) + 'n'
    m = re.search(r'^' + re.escape(region) + r'\n((?:[ \t].*\n)+)', atlas, re.M)
    if not m:
        sys.exit('atlas 里没有 region: ' + region)
    body = m.group(1)
    xy = re.search(r'xy: (\d+), (\d+)', body); wh = re.search(r'size: (\d+), (\d+)', body)
    x, y = int(xy.group(1)), int(xy.group(2)); w, h = int(wh.group(1)), int(wh.group(2))
    part = sheet.crop((x, y, x + w, y + h))
    bg = Image.new('RGBA', part.size, BLACK)
    bg.paste(part, (0, 0), part)
    return bg


def is_blue(px, x, y):
    c = px[x, y]
    return c[2] > 200 and c[0] < 60 and c[1] < 60


def main():
    import argparse
    ap = argparse.ArgumentParser()
    ap.add_argument('--scene', default='save', choices=sorted(SCENES))
    ap.add_argument('--out', default=None)
    a = ap.parse_args()
    sc = SCENES[a.scene]
    img = load_bg(sc['region'])
    W, H = img.size
    px = img.load()
    d = ImageDraw.Draw(img)

    # 1) 擦掉文字带里的蓝色像素（跳过左右 5px 边框柱）
    erased = 0
    for y0, y1 in sc['erase']:
        for y in range(y0, min(y1 + 1, H)):
            for x in range(6, W - 5):
                if is_blue(px, x, y):
                    px[x, y] = BLACK
                    erased += 1
    print('擦掉蓝色文字像素 %d 个' % erased)

    # 2) 用同色画中文
    font = ImageFont.truetype(TTF, 8)
    for key, (x0, x1, y, text, center) in sc['texts'].items():
        if not text:
            continue
        w = sum(font.getbbox(ch)[2] for ch in text) if False else None
        # 逐个字画，按 8px 步进（和游戏网格一致）
        tw = len(text) * 8
        x = x0 + ((x1 - x0) - tw) // 2 if center else x0
        for i, ch in enumerate(text):
            d.text((x + i * 8, y), ch, font=font, fill=BLUE)
    out = a.out or os.path.join(LOC, 'work', 'menu', '%s.png' % a.scene)
    os.makedirs(os.path.dirname(out), exist_ok=True)
    img.save(out)
    print('wrote', out, img.size)
    return 0


if __name__ == '__main__':
    sys.exit(main())
