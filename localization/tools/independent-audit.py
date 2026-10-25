#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""独立核验：不依赖 batch.py，用自己的实现从零复核正式库。

存在的意义是**不共用同一套代码**。batch.py 的 C1–C10 是合并时的自检，
本脚本在需要独立验收时重算同一批不变量，两边都过才算过。

    PYTHONDONTWRITEBYTECODE=1 PYTHONIOENCODING=utf-8 python localization/tools/independent-audit.py

只读，不写任何译文或目录。退出码 0 = 全过，1 = 有 FAIL。
"""
import json
import os
import re
import sys
import unicodedata

ROOT = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))


def path(*p):
    return os.path.join(ROOT, *p)


def read_jsonl(p):
    out = []
    with open(p, encoding='utf-8') as f:
        for line in f:
            line = line.strip()
            if line:
                out.append(json.loads(line))
    return out


def effective(rec):
    return (rec.get('translation') or '').strip() or (rec.get('draft') or '').strip()


def marker_sig(s):
    """自己实现一份标记签名，不 import 项目代码。"""
    s = s or ''
    return {
        'open_sq': s.count('['),
        'close_sq': s.count(']'),
        'pipes': s.count('|'),
        'underscores': len(re.findall(r'_{2,}', s)),
        'placeholders': tuple(sorted(re.findall(r'\{[^}]*\}', s))),
        'angle_pairs': len(re.findall(r'<[^<>]*>', s)),
    }


class Audit:
    def __init__(self):
        self.fails = []
        self.warns = []
        self.info = {}

    def fail(self, code, detail):
        self.fails.append((code, detail))

    def warn(self, code, detail):
        self.warns.append((code, detail))


def main():
    a = Audit()
    units = read_jsonl(path('localization', 'catalog', 'units.jsonl'))
    canon = read_jsonl(path('localization', 'translations', 'zh-CN.jsonl'))

    # ---- A1 行数与 id 一一对应
    if len(units) != len(canon):
        a.fail('A1', 'row count differs: units=%d canonical=%d' % (len(units), len(canon)))
    uid = [u['id'] for u in units]
    cid = [r['id'] for r in canon]
    if uid != cid:
        a.fail('A2', 'id order differs between units.jsonl and zh-CN.jsonl')
    if len(set(cid)) != len(cid):
        a.fail('A3', 'duplicate ids in canonical')

    by_unit = {u['id']: u for u in units}
    translated = 0
    latin_hits = []
    empty = []
    marker_bad = []
    ctrl = []
    nonbmp = []

    for rec in canon:
        u = by_unit.get(rec['id'])
        if not u:
            a.fail('A4', 'canonical id not in units: %s' % rec['id'])
            continue
        t = effective(rec)
        if not t:
            empty.append(rec['id'])
            continue
        translated += 1

        # A5 控制字符
        for ch in t:
            o = ord(ch)
            if o < 32 and ch not in '\r\n\t':
                ctrl.append((rec['id'], hex(o)))
                break

        # A6 标记签名必须与原文一致
        if marker_sig(t) != marker_sig(u.get('source', '')):
            marker_bad.append((rec['id'], marker_sig(u.get('source')), marker_sig(t)))

        # A7 拉丁残留（4 个以上连续字母），只统计不改
        for m in re.findall(r'[A-Za-z]{4,}', t):
            latin_hits.append((rec['id'], m, u.get('source', '')[:60], t[:50]))

        # A8 生僻字 / 非 BMP 字符（字体页可能缺字）
        for ch in t:
            if ord(ch) > 0xFFFF:
                nonbmp.append((rec['id'], ch))
                break

    # ---- 汇总
    a.info['units'] = len(units)
    a.info['translated'] = translated
    a.info['empty'] = len(empty)
    a.info['latin_rows'] = len({h[0] for h in latin_hits})

    if ctrl:
        a.fail('A5', '%d rows with control characters: %s' % (len(ctrl), ctrl[:5]))
    if marker_bad:
        a.fail('A6', '%d rows with marker drift: %s' % (len(marker_bad), marker_bad[:3]))
    if nonbmp:
        a.warn('A8', '%d rows with non-BMP chars (font coverage risk): %s' % (len(nonbmp), nonbmp[:5]))

    # ---- A9 空译文分布（应当只有已登记的故意留空）
    if empty:
        cats = {}
        for i in empty:
            c = by_unit[i].get('category', '?')
            cats[c] = cats.get(c, 0) + 1
        a.info['empty_by_category'] = cats

    # ---- A10 拉丁残留按词聚合，便于判断是专名还是漏译
    agg = {}
    for rid, word, src, tr in latin_hits:
        agg.setdefault(word.upper(), set()).add(word)
    a.info['latin_distinct'] = len(agg)
    top = sorted(agg.items(), key=lambda kv: -len(kv[1]))
    a.info['latin_sample'] = top[:0]

    print('=' * 62)
    print('独立核验（不复用 batch.py 代码）')
    print('=' * 62)
    print('单元总数        %d' % a.info['units'])
    print('已译            %d' % a.info['translated'])
    print('空译文          %d  %s' % (a.info['empty'], a.info.get('empty_by_category', {})))
    print('含拉丁残留行    %d  （不同词 %d 个）' % (a.info['latin_rows'], a.info['latin_distinct']))
    print()

    if a.fails:
        print('FAIL %d 项' % len(a.fails))
        for code, detail in a.fails:
            print('  [%s] %s' % (code, detail))
    else:
        print('FAIL 0 项')
    if a.warns:
        print('WARN %d 项' % len(a.warns))
        for code, detail in a.warns:
            print('  [%s] %s' % (code, detail))
    else:
        print('WARN 0 项')

    # 拉丁词频表单独输出，供人工挑漏译
    print()
    print('拉丁词（按出现行数降序，前 40）:')
    for w, forms in top[:40]:
        print('  %-22s %s' % (w, '/'.join(sorted(forms)) if len(forms) > 1 else ''))

    return 0 if not a.fails else 1


if __name__ == '__main__':
    sys.exit(main())
