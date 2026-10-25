# -*- coding: utf-8 -*-
"""离线排版预览：用真实的 .fnt + 字形页，按游戏规则（xadvance 累加折行）渲染文本。

用途：改字体/改译文后先在这里看效果，不必每次都装进游戏实机试。

    # 单条文本
    python localization/tools/preview-layout.py --text "[YIFFAI] [要是出了坏事，那会保存我的数据，对？]" --box 240
    # 按 unit id 取译文
    python localization/tools/preview-layout.py --unit D95c2e5c8106281011816 --box 240
    # 两种框宽并排，输出对比图
    python localization/tools/preview-layout.py --unit D95c2e5c8106281011816 --box 120 --box 240 --scale 4
    # 批量体检：统计所有译文折行后的行数
    python localization/tools/preview-layout.py --audit --box 240 --max-lines 3
"""
import argparse
import json
import os
import re
import sys

from PIL import Image

ROOT = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
LOC = os.path.join(ROOT, 'localization')
RUNTIME = os.path.join(LOC, 'runtime')

# 游戏配色：BBC 风格的琥珀黄字 / 黑底
FG = (255, 180, 0, 255)
BG = (16, 16, 16, 255)


def parse_fnt(path):
    head = {}
    chars = {}
    for line in open(path, encoding='utf8').read().splitlines():
        if line.startswith('info '):
            head.update({k: v for k, v in re.findall(r'(\w+)="?([^"\s]+)"?', line)})
        elif line.startswith('common '):
            head.update({k: int(v) for k, v in re.findall(r'(\w+)=(-?\d+)', line)})
        elif line.startswith('page '):
            m = re.search(r'file="([^"]+)"', line)
            if m:
                head['page_file'] = m.group(1)
        elif line.startswith('char '):
            d = dict(re.findall(r'(\w+)=(-?\d+)', line))
            c = {k: int(v) for k, v in d.items()}
            chars[c['id']] = c
    return head, chars


def load_font(fnt_path=None, page_path=None):
    fnt_path = fnt_path or os.path.join(RUNTIME, 'bbc2.fnt')
    head, chars = parse_fnt(fnt_path)
    stem = os.path.splitext(os.path.basename(fnt_path))[0]
    if page_path is None:
        # fnt 的 page file 指向的是游戏内名，实际预览用我们生成的字形页；
        # 优先按 info size 选对应字号的那张
        size = head.get('size')
        candidates = []
        if size:
            candidates.append(os.path.join(RUNTIME, stem + '-cjk-%s.png' % size))
        candidates += [os.path.join(RUNTIME, stem + '-cjk.png'),
                       os.path.join(RUNTIME, stem + '-cjk-8.png'),
                       os.path.join(RUNTIME, stem + '-cjk-10.png')]
        page_path = next((p for p in candidates if os.path.isfile(p)), None)
    if not page_path or not os.path.isfile(page_path):
        sys.exit('找不到字形页：%s' % stem)
    page = Image.open(page_path).convert('RGBA')
    return head, chars, page


def glyph_image(page, c, color=FG):
    g = page.crop((c['x'], c['y'], c['x'] + c['width'], c['y'] + c['height']))
    tinted = Image.new('RGBA', g.size, color)
    tinted.putalpha(g.getchannel('A'))
    return tinted


def layout(text, chars, box_w, default_adv=8, fixed_adv=None):
    """按 xadvance 累加折行；行首空格丢弃。返回 [[glyph,...], ...]。"""
    lines = []
    cur = []
    w = 0
    for ch in text:
        if ch == '\n':
            lines.append(cur)
            cur, w = [], 0
            continue
        c = chars.get(ord(ch))
        adv = fixed_adv if fixed_adv else (c['xadvance'] if c else default_adv)
        if cur and w + adv > box_w:
            lines.append(cur)
            cur, w = [], 0
            if ch == ' ':
                continue
        cur.append((ch, c, adv))
        w += adv
    lines.append(cur)
    return lines


def render(lines, page, line_h, box_w, pad=2):
    used = max((sum(a for _, _, a in ln) for ln in lines), default=box_w)
    width = min(box_w, used) + pad * 2
    height = line_h * len(lines) + pad * 2
    img = Image.new('RGBA', (width, height), BG)
    for li, ln in enumerate(lines):
        x = pad
        y = pad + li * line_h
        for ch, c, adv in ln:
            if c and c['width'] and c['height']:
                g = glyph_image(page, c)
                img.alpha_composite(g, (x + c['xoffset'], y + c['yoffset']))
            x += adv
    return img


def measure(lines, chars):
    return [sum(a for _, _, a in ln) for ln in lines]


def load_units():
    return [json.loads(l) for l in open(os.path.join(LOC, 'catalog', 'units.jsonl'), encoding='utf-8')]


def load_translations():
    p = os.path.join(LOC, 'translations', 'zh-CN.jsonl')
    return {r['id']: r for r in (json.loads(l) for l in open(p, encoding='utf-8'))}


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument('--font', default=None, help='fnt 路径，默认 runtime/bbc2.fnt')
    ap.add_argument('--page', default=None, help='字形页 png 路径，默认按 fnt 名推断')
    ap.add_argument('--text', default=None)
    ap.add_argument('--unit', default=None, help='unit id，取译文；--source 取原文')
    ap.add_argument('--source', action='store_true', help='配 --unit 时渲染原文')
    ap.add_argument('--box', type=int, action='append', help='文本框宽度 px，可重复')
    ap.add_argument('--scale', type=int, default=3, help='放大倍数')
    ap.add_argument('--fixed-advance', type=int, default=None,
                    help='强制所有字按固定步进排（模拟 Id 这类写死 8 的逐字路径）')
    ap.add_argument('--out', default=None)
    ap.add_argument('--audit', action='store_true', help='批量统计折行行数')
    ap.add_argument('--max-lines', type=int, default=3)
    ap.add_argument('--category', default=None, help='audit 时只看某类')
    a = ap.parse_args()

    head, chars, page = load_font(a.font, a.page)
    line_h = head.get('lineHeight', 8)

    if a.audit:
        units = load_units()
        tr = load_translations()
        boxes = a.box or [240]
        over = []
        for u in units:
            if a.category and u['category'] != a.category:
                continue
            txt = u['source'] if a.source else (tr.get(u['id']) or {}).get('translation')
            if not txt:
                continue
            worst = 0
            detail = {}
            for bw in boxes:
                n = len(layout(txt, chars, bw))
                detail[bw] = n
                worst = max(worst, n)
            if worst > a.max_lines:
                over.append((u['id'], u['category'], worst, len(txt), detail, txt[:44]))
        over.sort(key=lambda r: -r[2])
        print('框宽 %s，行高 %d，超过 %d 行的：%d 条' % (boxes, line_h, a.max_lines, len(over)))
        for r in over[:40]:
            print('  %s %-8s %d 行 len=%d %s | %s' % (r[0], r[1], r[2], r[3], r[4], r[5]))
        if len(over) > 40:
            print('  ... 共 %d 条' % len(over))
        return 0

    text = a.text
    if a.unit:
        u = next((u for u in load_units() if u['id'] == a.unit), None)
        if not u:
            sys.exit('找不到 unit: ' + a.unit)
        text = u['source'] if a.source else (load_translations().get(a.unit) or {}).get('translation')
        if not text:
            sys.exit('该 unit 没有译文')
    if not text:
        sys.exit('需要 --text 或 --unit')

    boxes = a.box or [240]
    panels = []
    for bw in boxes:
        lines = layout(text, chars, bw, fixed_adv=a.fixed_advance)
        img = render(lines, page, line_h, bw)
        mx = max(measure(lines, chars))
        print('框宽 %-4d → %d 行，最宽 %d px%s' % (bw, len(lines), mx, '  ← 溢出' if mx > bw else ''))
        for i, ln in enumerate(lines):
            print('   %d: %s' % (i + 1, ''.join(ch for ch, _, _ in ln)))
        panels.append((bw, img))

    if panels:
        gap = 8
        W = sum(p.width for _, p in panels) + gap * (len(panels) - 1)
        H = max(p.height for _, p in panels)
        canvas = Image.new('RGBA', (W, H), (32, 32, 32, 255))
        x = 0
        for _, p in panels:
            canvas.alpha_composite(p, (x, 0))
            x += p.width + gap
        if a.scale > 1:
            canvas = canvas.resize((W * a.scale, H * a.scale), Image.NEAREST)
        out = a.out or os.path.join(ROOT, 'localization', 'work', 'fontprobe', 'preview.png')
        os.makedirs(os.path.dirname(out), exist_ok=True)
        canvas.convert('RGB').save(out)
        print('写圖', out)
    return 0


if __name__ == '__main__':
    sys.exit(main())
