#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""只读扫描：找出译文里疑似"校对备注 / 核对说明"被写进正文的行。

这不是译文质量检查，是找**元语言污染**：本该出现在 findings 里的句子
（"改为「…」"、"统一为…"、"原文是…"）被当成译文提交了。

    PYTHONDONTWRITEBYTECODE=1 PYTHONIOENCODING=utf-8 python localization/tools/scan-meta.py

只读，不写任何译文。输出候选清单供人工逐条判断。
"""
import json
import os
import re
import sys

_ROOT = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
CANON = os.path.join(_ROOT, 'localization', 'translations', 'zh-CN.jsonl')

# 高置信度：这些词出现在玩家可见的台词里几乎不可能是正常对话
HARD = [
    r'改为', r'改成', r'统一为', r'应改', r'应作', r'应译',
    r'原文是', r'原句', r'原文为', r'原文用', r'原文写',
    r'校对', r'备注', r'待定', r'存疑', r'建议改为', r'建议统一',
    r'TODO', r'FIXME', r'待核', r'待确认',
    # 2026-10-24 补：这两组曾经漏网，实际把整句批注当译文提交了
    r'统一译法', r'改译', r'按原意', r'建议保留', r'需另作', r'请核对',
    r'相邻片段', r'口吻', r'暂译', r'试译',
    # 「标注」「如「」「保持一致」用过，但正常台词里本就会出现（"地图上还带标注"），
    # 误报率高，已移除。要抓这类必须靠上下文，不能靠单字词。
]
# 中置信度：可能是正常台词，需看上下文
SOFT = [
    r'保留原文', r'保留英文', r'不改', r'一致即可', r'措辞',
    r'译作', r'译为', r'视作', r'按原文',
]
# 引号包裹（指令残留常带「」或 ""），需与原文引号数对比
QUOTE = re.compile(r'[「」『』"“”]')


def load_rows():
    out = []
    with open(CANON, encoding='utf-8') as f:
        for ln, line in enumerate(f, 1):
            line = line.strip()
            if not line:
                continue
            r = json.loads(line)
            eff = (r.get('translation') or '').strip() or (r.get('draft') or '').strip()
            if not eff:
                continue
            out.append((ln, r, eff))
    return out


def count_quotes(s):
    return len(QUOTE.findall(s or ''))


def main():
    if not os.path.exists(CANON):
        sys.exit('missing %s' % CANON)
    rows = load_rows()
    print('扫描 %d 条非空译文' % len(rows))

    hard_re = re.compile('|'.join(HARD))
    soft_re = re.compile('|'.join(SOFT))

    hard, soft, quote = [], [], []
    for ln, r, eff in rows:
        if hard_re.search(eff):
            hard.append((ln, r, eff))
        elif soft_re.search(eff):
            soft.append((ln, r, eff))
        else:
            # 原文没有引号而译文有：可能是指令残留的「…」
            srcq = count_quotes(r.get('source', ''))
            if count_quotes(eff) > srcq and count_quotes(eff) > 0:
                quote.append((ln, r, eff))

    print()
    print('=== 高置信度（含"改为/统一/原文/校对/备注"等元语言）: %d ===' % len(hard))
    for ln, r, eff in hard:
        print('  L%-5d %s' % (ln, r['id']))
        print('        源: %s' % (r.get('source', '')[:150]))
        print('        译: %s' % eff[:150])
        print('        状态=%s 批次=%s' % (r.get('status'), r.get('draft_batch') or r.get('reviewer')))
    if not hard:
        print('  （无）')

    print()
    print('=== 中置信度（含"保留/译作/措辞"等，可能是正常台词）: %d ===' % len(soft))
    for ln, r, eff in soft[:60]:
        print('  L%-5d %s' % (ln, r['id']))
        print('        源: %s' % (r.get('source', '')[:150]))
        print('        译: %s' % eff[:150])
    if len(soft) > 60:
        print('  … 其余 %d 条省略' % (len(soft) - 60))

    print()
    print('=== 引号数多于原文（可能是「…」指令残留）: %d ===' % len(quote))
    for ln, r, eff in quote[:60]:
        print('  L%-5d %s' % (ln, r['id']))
        print('        源: %s' % (r.get('source', '')[:150]))
        print('        译: %s' % eff[:150])
    if len(quote) > 60:
        print('  … 其余 %d 条省略' % (len(quote) - 60))
    return 0


if __name__ == '__main__':
    sys.exit(main())
