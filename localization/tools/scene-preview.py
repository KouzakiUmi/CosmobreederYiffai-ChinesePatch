# -*- coding: utf-8 -*-
"""场景级排版预览：拿真实游戏截图当底图，擦掉原文，用我们的字体重绘。

和 preview-layout.py 的区别：那个只看文字，这个把文字放回真实 UI 框里，
能直接看出「会不会撞框、护边、行距够不够」。

做法：
  1. 底图是 6 倍放大的真实截图（游戏逻辑分辨率 256x224）
  2. 先把目标区域内的文字像素抹掉（保留边框装饰）
  3. 在逻辑尺度(1:1)渲染文本，再 NEAREST 放大 6 倍贴回去

    python localization/tools/scene-preview.py --scene radio --sizes 8 10 12

场景定义在 SCENES 里，坐标都是截图像素（从真实截图量出来的）。
"""
import io
import json
import os
import re
import sys

from PIL import Image, ImageDraw, ImageFont

ROOT = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
LOC = os.path.join(ROOT, 'localization')
RUNTIME = os.path.join(LOC, 'runtime')
WORK = os.path.join(LOC, 'work')

FG = (255, 180, 0, 255)
BLACK = (0, 0, 0, 255)

# 各场景：底图、要擦掉文字的区域(截图像素)、文字起点(逻辑坐标)、可用行宽(逻辑px)、目标文本
SCENES = {
    'save': {
        'atlas': 'CosmoSaveMenuBG',
        'scale': 4,
        'erase': [],
        'origin': (6, 44),
        'line_step': 16,
        'box': 250,
        'fixed_advance': 8,
        'text': '伊法伊  LVL12 TRY03 遗迹'+chr(10)+'          05:32:11'+chr(10)+'伊法妮  LVL08 TRY12 营地'+chr(10)+'          11:20:45',
        'note': '完整存档行：名字+LVL+TRY+位置，Id 逐字步进 8',
    },
    'save-xadv': {
        'atlas': 'CosmoSaveMenuBG',
        'scale': 4,
        'erase': [],
        'origin': (6, 44),
        'line_step': 16,
        'box': 250,
        'text': '伊法伊  LVL12 TRY03 遗迹'+chr(10)+'          05:32:11'+chr(10)+'伊法妮  LVL08 TRY12 营地'+chr(10)+'          11:20:45',
        'note': '同上，按字形 advance 排',
    },
    'item': {
        'atlas': 'CosmoItemMenuBG',      # 真实道具菜单背景(256x192)
        'scale': 4,
        'erase': [],
        'origin': (6, 20),
        'line_step': 12,
        'box': 116,
        'text': '无线电'+chr(10)+'医疗包'+chr(10)+'精神力水晶'+chr(10)+'宇宙卡',
        'note': '道具列表（左栏）',
    },
    'radio': {
        'base': os.path.join(WORK, 'fontprobe', 'shot.png'),
        'scale': 6,
        # 原文有两段：第一行在框顶线之上(y≈700..737)，第二行"？]"在框内(y≈792..838)。
        # 边框线在 y≈738..752，避开不擦。
        # 原图文字分两段：第一行压在框顶线之上(y≈700..760)，第二行"？]"在框内(y≈792..840)。
        # 框顶线 y≈738..752 保持不变，其余文字像素擦黑，模拟"把文字放回框内"。
        'erase': [(30, 698, 1502, 776), (30, 788, 1502, 845)],
        # 原文字压在框顶线上，擦的时候会连框线一起擦掉，这里按原位置补一条
        'repaint': [(18, 736, 1514, 754, 'line')],
        'origin': (8, 127),           # 逻辑坐标：框内首行文字左上
        'line_step': 16,
        'box': 240,
        'text': '[YIFFAI] [要是出了坏事，那会保存我的数据，对？]',
        'note': '无线电/通信正文（真实截图 y=748..990 的对话框）',
    },
}


def parse_fnt(path):
    head, chars = {}, {}
    for line in open(path, encoding='utf8').read().splitlines():
        if line.startswith('info '):
            head.update({k: v for k, v in re.findall(r'(\w+)=("?[^"\s]+"?)', line)})
        elif line.startswith('common '):
            head.update({k: int(v) for k, v in re.findall(r'(\w+)=(-?\d+)', line)})
        elif line.startswith('char '):
            d = dict(re.findall(r'(\w+)=(-?\d+)', line))
            c = {k: int(v) for k, v in d.items()}
            chars[c['id']] = c
    head['size'] = int(str(head.get('size', '8')).strip('"'))
    return head, chars


def load_font(size):
    fnt = os.path.join(RUNTIME, 'bbc2.fnt') if size is None else None
    cand = [os.path.join(RUNTIME, 'bbc2-%dpx.fnt' % size)]
    if fnt is None:
        fnt = next((p for p in cand if os.path.isfile(p)), None)
    if fnt is None or not os.path.isfile(fnt):
        sys.exit('找不到 %s 的 fnt（可先把对应字号备份复制成 runtime/bbc2-<n>px.fnt）' % size)
    head, chars = parse_fnt(fnt)
    page_path = os.path.join(RUNTIME, 'bbc2-cjk-%d.png' % head['size'])
    if not os.path.isfile(page_path):
        page_path = os.path.join(RUNTIME, 'bbc2-cjk.png')
    return head, chars, Image.open(page_path).convert('RGBA')


def layout(text, chars, box, fixed_adv=None):
    lines, cur, w = [], [], 0
    for ch in text:
        if ch == '\n':
            lines.append(cur); cur, w = [], 0; continue
        c = chars.get(ord(ch))
        adv = fixed_adv or (c['xadvance'] if c else 8)
        if cur and w + adv > box:
            lines.append(cur); cur, w = [], 0
            if ch == ' ':
                continue
        cur.append((ch, c, adv)); w += adv
    lines.append(cur)
    return lines


def render_lines(lines, chars, page, line_h, box):
    w = max(sum(a for _, _, a in ln) for ln in lines)
    img = Image.new('RGBA', (max(w, 1), line_h * len(lines)), BLACK)
    for li, ln in enumerate(lines):
        x = 0
        for ch, c, adv in ln:
            if c and c['width'] and c['height']:
                g = page.crop((c['x'], c['y'], c['x'] + c['width'], c['y'] + c['height']))
                tint = Image.new('RGBA', g.size, FG); tint.putalpha(g.getchannel('A'))
                img.alpha_composite(tint, (x + c['xoffset'], li * line_h + c['yoffset']))
            x += adv
    return img


def atlas_bg(region):
    """从 pak 图集里裁一块界面背景，铺黑底返回（背景是 256x224 逻辑尺寸）。"""
    import zipfile
    sys.path.insert(0, os.path.join(LOC, 'tools'))
    from codec import decrypt_file
    GAME = os.environ.get('COSMOBREEDER_GAME_DIR', os.path.join(ROOT, '.local', 'game'))
    z = zipfile.ZipFile(os.path.join(GAME, '_汉化补丁备份', 'patch.pak'))
    idx = json.loads(decrypt_file(z.read('dataq/0')))
    atlas = decrypt_file(z.read('dataq/' + str(idx['/sprites.atlas']))).decode('utf8')
    sheet = Image.open(io.BytesIO(decrypt_file(z.read('dataq/' + str(idx['/sprites.png']))))).convert('RGBA')
    m = re.search(r'^' + re.escape(region) + r'\n((?:[ \t].*\n)+)', atlas, re.M)
    if not m:
        sys.exit('atlas 里没有 region: ' + region)
    body = m.group(1)
    xy = re.search(r'xy: (\d+), (\d+)', body); wh = re.search(r'size: (\d+), (\d+)', body)
    x, y = int(xy.group(1)), int(xy.group(2)); w, h = int(wh.group(1)), int(wh.group(2))
    part = sheet.crop((x, y, x + w, y + h))
    bg = Image.new('RGB', part.size, (0, 0, 0))
    bg.paste(part, (0, 0), part)
    return bg


def build(scene, size, out):
    s = scene['scale']
    if scene.get('atlas'):
        # 图集里是 256x224 的原生界面，先按 scale 放大成"屏幕像素"
        base = atlas_bg(scene['atlas']).resize(
            (atlas_bg(scene['atlas']).width * s, atlas_bg(scene['atlas']).height * s), Image.NEAREST)
    else:
        # 已经是放大后的真实截图
        base = Image.open(scene['base']).convert('RGB')
    work = base.copy()
    d = ImageDraw.Draw(work)
    for x0, y0, x1, y1 in scene['erase']:
        d.rectangle([x0, y0, x1, y1], fill=(0, 0, 0))
    # 补回被擦掉的框线：从原图采样黄色，避免色差
    for x0, y0, x1, y1, kind in scene.get('repaint', []):
        col = base.getpixel(((x0 + x1) // 2, max(y0 - 4, 0)))
        if sum(col) < 200:
            col = (255, 176, 0)
        d.rectangle([x0, y0, x1, y1], fill=col)

    head, chars, page = load_font(size)
    line_h = scene.get('line_step') or head.get('lineHeight', 8)
    lines = layout(scene['text'], chars, scene['box'], fixed_adv=scene.get('fixed_advance'))
    block = render_lines(lines, chars, page, line_h, scene['box'])

    big = block.resize((block.width * s, block.height * s), Image.NEAREST)
    ox, oy = scene['origin']
    ox, oy = ox * s, oy * s
    work.paste(big, (ox, oy), big)
    work.save(out)
    return lines, head['size'], line_h


def main():
    import argparse
    ap = argparse.ArgumentParser()
    ap.add_argument('--scene', required=True, choices=sorted(SCENES))
    ap.add_argument('--sizes', type=int, nargs='+', default=[8, 10, 12])
    ap.add_argument('--text', default=None, help='覆盖场景文本')
    ap.add_argument('--outdir', default=os.path.join(WORK, 'scene'))
    a = ap.parse_args()

    sc = dict(SCENES[a.scene])
    if a.text:
        sc['text'] = a.text
    os.makedirs(a.outdir, exist_ok=True)
    for size in a.sizes:
        out = os.path.join(a.outdir, '%s-%dpx.png' % (a.scene, size))
        lines, real, lh = build(sc, size, out)
        mx = max(sum(len(ch) for ch, _, _ in ln) for ln in lines)
        print('%2dpx 行高%d → %d 行 / 每行最多 %d 字  → %s' % (real, lh, len(lines), mx, out))
    return 0


if __name__ == '__main__':
    sys.exit(main())
