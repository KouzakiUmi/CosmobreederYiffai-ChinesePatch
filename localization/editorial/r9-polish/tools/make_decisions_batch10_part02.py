"""Write the r9 batch-10-part02 decision table (single-route: DS only).

The Gemini route produced nothing for any batch-10 part, so this part rests on
the DS findings plus the main agent's trailing-space pass.

`EASTERN PASSAGE` is fixed on this side only; its jar-side sibling lives in
batch-10-part03, so the two sides meet again one candidate later instead of
drifting apart for good.
"""
from pathlib import Path
import sys

sys.path.insert(0, str(Path(__file__).resolve().parent))
from r9_decisions import Batch

SKIP = ('ui.end', 'ui.backers', 'ui.options')

b = Batch('batch-10-part02')

b.apply_finding('ds', 'P10-0201',
                '后半句「回忆涌上心头，又迟疑起来」在原文里没有对应词，上一句漏译了 WALLOP（痛打一顿）；'
                '按原文两段重写，段数不变。')
b.apply_finding('ds', 'P10-0202', '本批 ui.item 把 BESTIALIARY 定为「兽类图鉴」，同屏入口仍是简称「兽鉴」，统一。')
b.apply_finding('ds', 'P10-0203',
                '同 root 的 EAST 一律作「东部」（DEPOT B EAST／SCEAFYA EAST）；本行是 patch.pak 侧，'
                'jar 侧同句在 batch-10-part03，两侧在下一候选合拢。')
b.apply_finding('ds', 'P10-0204', '「你来他就来精神」两个「来」挤在一句里读着打结；改后保留原意与三段结构。')

b.emit_trailing_space(skip_roots=SKIP,
                      reason='中文行尾（JSON 值末的换行之前）多出空格，英文原文行尾没有；只删空格，不动换行。')

print(b.close())
