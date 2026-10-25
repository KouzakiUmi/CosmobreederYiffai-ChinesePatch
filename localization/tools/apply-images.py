#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""把 work/image-staging/ 里重绘好的位图贴回已构建的包。

单独成一步而不是塞进 package.py，是因为 package.py 明确写了位图替换
「deliberately not automatic」——那些是 256x224 的像素画，改错了不会报错，
只会在游戏里看见一张花掉的图。所以这里做成显式、可核验的独立步骤。

    PYTHONDONTWRITEBYTECODE=1 PYTHONIOENCODING=utf-8 python localization/tools/apply-images.py \
        --package builds/final-8146-r4 --output builds/final-8146-r5-images

做的事：
  1. 解开产物 pak 里的 dataq/sprites.png（此时已经由 package.py 换成了含中文字库的 4096x6144 版）
  2. 按 catalog/fixed_images.jsonl 记录的 xy/size，把 staging 图贴回原位置
  3. 硬校验：目标矩形之外一个像素都不许变
  4. 重新加密写回

只写 --output 这个新目录，不改 --package。
"""
import argparse
import io
import json
import os
import shutil
import sys
import zipfile

from PIL import Image

ROOT = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
LOC = os.path.join(ROOT, 'localization')
sys.path.insert(0, os.path.join(LOC, 'tools'))
from codec import decrypt_file, encrypt_file  # noqa: E402

# asset_id -> 本工具期望读到的 staging 文件
STAGING = {
    'Acfb74ff046445762b007': 'card-viewer.png',
    'A3ad10e4fc08b09e2bef4': 'bestiary-title.png',
    'A4b6160b4569cc8b87687': 'pretitle-gamepad.png',
    'Ada8d2a93e89e1525cbf1': 'pretitle-plain.png',
}


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument('--package', required=True, help='已由 package.py 构建好的包目录')
    ap.add_argument('--output', required=True, help='新的输出目录，不能已存在')
    ap.add_argument('--sprite-entry', default='dataq/6', help='sprites.png 在 pak 里的条目名')
    a = ap.parse_args()

    pkg = os.path.abspath(a.package)
    out = os.path.abspath(a.output)
    if not os.path.isdir(pkg):
        sys.exit('package dir not found: %s' % pkg)
    if os.path.exists(out):
        sys.exit('refuse to overwrite existing output: %s' % out)

    # 1. 资源坐标
    rows = [json.loads(l) for l in open(os.path.join(LOC, 'catalog/fixed_images.jsonl'), encoding='utf-8')]
    meta = {r['asset_id']: r for r in rows if r['asset_id'] in STAGING}
    missing = set(STAGING) - set(meta)
    if missing:
        sys.exit('asset metadata missing: %s' % ', '.join(sorted(missing)))

    # 2. 找出 pak
    pak_name = next((n for n in os.listdir(pkg) if n.endswith('.pak')), None)
    if not pak_name:
        sys.exit('no .pak in %s' % pkg)
    pak_path = os.path.join(pkg, pak_name)

    # 3. 复制整个包，然后只改 pak
    shutil.copytree(pkg, out)
    out_pak = os.path.join(out, pak_name)

    with zipfile.ZipFile(pak_path) as z:
        if a.sprite_entry not in z.namelist():
            sys.exit('sprite entry %s not in %s' % (a.sprite_entry, pak_name))
        entries = {n: z.read(n) for n in z.namelist()}
        infos = {i.filename: i for i in z.infolist()}

    sheet = Image.open(io.BytesIO(decrypt_file(entries[a.sprite_entry]))).convert('RGBA')
    before = sheet.copy()

    staged = 0
    for asset_id, fname in STAGING.items():
        src = os.path.join(LOC, 'work', 'image-staging', fname)
        if not os.path.exists(src):
            print('  skip %s (%s not staged)' % (asset_id, fname))
            continue
        r = meta[asset_id]
        x, y = r['xy']
        w, h = r['size']
        new = Image.open(src).convert('RGBA')
        if new.size != (w, h):
            sys.exit('%s size %s != declared %s' % (fname, new.size, (w, h)))
        sheet.paste(new, (x, y))
        staged += 1
        print('  pasted %-24s at (%d,%d) %dx%d' % (fname, x, y, w, h))

    if not staged:
        sys.exit('nothing pasted; refusing to write an unchanged package')

    # 4. 硬校验：目标矩形外不许有任何变化
    allowed = [(meta[i]['xy'][0], meta[i]['xy'][1],
                meta[i]['xy'][0] + meta[i]['size'][0],
                meta[i]['xy'][1] + meta[i]['size'][1]) for i in STAGING if i in meta]
    pb, pn = before.load(), sheet.load()
    W, H = sheet.size
    stray = 0
    for yy in range(H):
        for xx in range(W):
            if pb[xx, yy] != pn[xx, yy]:
                if not any(x0 <= xx < x1 and y0 <= yy < y1 for x0, y0, x1, y1 in allowed):
                    stray += 1
    if stray:
        sys.exit('FAIL: %d pixels changed outside the declared rectangles' % stray)
    print('  guard OK: no pixels changed outside the %d target rectangles' % staged)

    # 5. 重新编码并加密
    buf = io.BytesIO()
    sheet.save(buf, format='PNG')
    entries[a.sprite_entry] = encrypt_file(buf.getvalue(), os.urandom(32), os.urandom(8))

    # 6. 重写 zip，保持条目顺序与压缩方式
    with zipfile.ZipFile(out_pak, 'w', zipfile.ZIP_DEFLATED, compresslevel=6) as z:
        for n in entries:
            info = infos[n]
            zi = zipfile.ZipInfo(n, date_time=info.date_time)
            zi.compress_type = zipfile.ZIP_DEFLATED
            zi.external_attr = info.external_attr
            z.writestr(zi, entries[n])

    print('wrote %s' % out_pak)

    # 7. 同步 manifest 里的归档哈希——贴图改了 pak 字节，不更新就会和产物对不上
    man_path = os.path.join(out, 'package-manifest.json')
    if os.path.exists(man_path):
        import hashlib
        m = json.load(open(man_path, encoding='utf-8'))
        for arch in m.get('archives', []):
            fp = os.path.join(out, arch['archive'])
            if os.path.exists(fp):
                data = open(fp, 'rb').read()
                arch['sha256'] = hashlib.sha256(data).hexdigest()
                arch['bytes'] = len(data)
        m.setdefault('plan', {})['bitmap_redraw_included'] = True
        m['plan']['bitmap_note'] = (
            '%d assets repainted from work/image-staging and pasted into %s by tools/apply-images.py '
            '(verified: 0 pixels changed outside the target rectangles)' % (staged, a.sprite_entry))
        with open(man_path, 'w', encoding='utf-8', newline='\n') as f:
            f.write(json.dumps(m, ensure_ascii=False, indent=2) + '\n')
        print('manifest hashes refreshed')
    else:
        print('warning: no package-manifest.json to refresh')

    print('originals untouched: %s' % pkg)
    return 0


if __name__ == '__main__':
    sys.exit(main())
