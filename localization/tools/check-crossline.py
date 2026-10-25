#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""跨行断句检查：按「文本框」而不是按「行」来审。

游戏的对话被切成一个个文本框，一个文本框里有若干行。译文逐行生成时，
很容易出现「单行看着对、连起来读就断错」的情况——比如原文用逗号连着，
中文却在行末收了句号；或者一句话跨两个框，两行都写成完整问句，重复了。

单行扫描永远发现不了这类问题，必须按框分组、把相邻行拼起来看。

    PYTHONDONTWRITEBYTECODE=1 PYTHONIOENCODING=utf-8 python localization/tools/check-crossline.py
    ... --show-context   连相邻几行一起打印，便于判断

只读。输出候选，需人工判断——大部分「原文未结句而译文结句」其实是正常的，
因为原文本身就有两句，只是第一句末尾没写标点。
"""
import argparse
import collections
import json
import os
import re
import sys

ROOT = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
LOC = os.path.join(ROOT, 'localization')
CJK_END = '。！？'


def load():
    units = {}
    with open(os.path.join(LOC, 'catalog', 'units.jsonl'), encoding='utf-8') as f:
        for line in f:
            u = json.loads(line)
            units[u['id']] = u
    trans = {}
    with open(os.path.join(LOC, 'translations', 'zh-CN.jsonl'), encoding='utf-8') as f:
        for line in f:
            r = json.loads(line)
            trans[r['id']] = (r.get('translation') or '').strip() or (r.get('draft') or '').strip()
    return units, trans


def parse_ctx(u):
    """从 context_examples 还原 (归档, 文本框名, 行号)。"""
    out = []
    for c in (u.get('context_examples') or []):
        m = re.match(r'(.+?)\s*\|\s*(.+?)\s*\|\s*line\s+(\d+)', c)
        if m:
            out.append((m.group(1), m.group(2), int(m.group(3))))
    return out


def tail_char(s):
    """去掉行尾的右括号/方括号/空白，取最后一个有意义的字符。"""
    s = (s or '').rstrip()
    s = re.sub(r'[\s\]\}）)]+$', '', s)
    return s[-1] if s else ''


def src_ends_sentence(s):
    """原文这一行是否真的收句了。

    关键：`...` 是省略号，不算收句。第一版没排除它，958 条候选全是假阳性
    ——原文 `Wait... is this...` 被当成「句子结束了」。
    """
    b = (s or '').rstrip()
    b = re.sub(r'[\s\]\}）)]+$', '', b)
    if not b:
        return False
    if b.endswith('...') or b.endswith('…'):
        return False
    return b[-1] in '.!?'


def zh_ends_sentence(s):
    b = (s or '').rstrip()
    b = re.sub(r'[\s\]\}）)]+$', '', b)
    return bool(b) and b[-1] in CJK_END


def build_groups(units):
    groups = collections.defaultdict(dict)
    for u in units.values():
        for arch, entry, line in parse_ctx(u):
            groups[(arch, entry)][line] = u['id']
    return groups


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument('--show-context', action='store_true', help='打印相邻行')
    ap.add_argument('--window', type=int, default=1, help='上下文行数，默认 1')
    a = ap.parse_args()

    units, trans = load()
    groups = build_groups(units)

    rows = []
    for (arch, entry), lines in groups.items():
        ks = sorted(lines)
        if len(ks) < 2:
            continue
        for i, k in enumerate(ks[:-1]):
            uid = lines[k]
            t = trans.get(uid)
            if not t:
                continue
            src = units[uid].get('source', '')
            st = tail_char(src)
            tt = tail_char(t)
            src_open = st not in '.!?' and st != ''
            zh_closed = tt in CJK_END
            if src_open and zh_closed:
                # 原文还在说，译文却收了句 —— 把一句话断成两句
                rows.append(('SPLIT', uid, arch, entry, k, ks, lines, i))
            elif src_ends_sentence(src) and not zh_ends_sentence(t):
                # 原文收句了，译文没跟 —— 通常是把句号漏了
                rows.append(('MISSING-STOP', uid, arch, entry, k, ks, lines, i))

    print('文本框总数 %d，其中多行 %d' % (
        len(groups), sum(1 for v in groups.values() if len(v) > 1)))
    kinds = collections.Counter(r[0] for r in rows)
    print('候选 %d 处  %s' % (len(rows), dict(kinds)))
    print('  SPLIT       原文还在说，译文却收句 —— 断成了两句')
    print('  MISSING-STOP 原文收句了，译文没跟 —— 多半漏了句号')
    print('（两类都要逐条看：原文常有两句而第一句末尾没标点，那属正常。）\n')

    for kind, uid, arch, entry, k, ks, lines, i in rows:
        print('--- [%s] %s | %s line %d' % (kind, arch, entry, k))
        if a.show_context:
            for kk in ks[max(0, i - a.window):i + 2 + a.window]:
                u2 = lines[kk]
                mark = '>>' if u2 == uid else '  '
                print('%s line %d  src: %s' % (mark, kk, repr(units[u2].get('source', ''))[:80]))
                print('             cur: %s' % repr(trans.get(u2, ''))[:80])
        else:
            print('   src: %s' % repr(units[uid].get('source', ''))[:90])
            print('   cur: %s' % repr(trans.get(uid, ''))[:90])
        print()

    return 0


if __name__ == '__main__':
    sys.exit(main())
