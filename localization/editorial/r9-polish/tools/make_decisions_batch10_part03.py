"""Write the r9 batch-10-part03 decision table (single-route: DS only).

The Gemini route never produced a file for batch-10, so this part rests on the
DS findings plus the main agent's trailing-space pass and one cross-side
supplement: the jar-side `navmap.AreaB` twin of the passage renamed in
batch-10-part02.

Two findings are rejected rather than argued: the BadEnding line mapping cannot
be established from the order (the English only becomes a sentence in a
specific row order the order does not record), and the Tier1 shard touches a
multi-line composite whose other shards are laid out on a fixed grid.
"""
from pathlib import Path
import sys

sys.path.insert(0, str(Path(__file__).resolve().parent))
from r9_decisions import Batch

SKIP = ('ui.end', 'ui.backers', 'ui.options')

b = Batch('batch-10-part03')

b.apply_finding('ds', 'P10-0301', '同一句在 sfw 侧已作「你好，世界」，nsfw 侧仍留英文，属跨侧分叉。')
b.apply_finding('ds', 'P10-0302', '同批把 HOTSHOT 定为「高手」；「宇宙专业」把等级读成专业，改成「宇宙高手」与同批定名一致。')
b.apply_finding('ds', 'P10-0303', '「给了你一个粗声的笑」是 English 语序直搬；三段结构与信息量不变。')
b.apply_finding('ds', 'P10-0304', '同一张繁殖卡的收尾句在库内 16 处作「真是棒极了的宠物！」；本行是 sfw 侧遗留的一处。')
b.apply_finding('ds', 'P10-0305', 'nubs 在库内 9 处作「凸粒」、6 处作「肉突」；按多数统一，只换一处词、13 段与行尾换行都不动。')
b.apply_finding('ds', 'P10-0306',
                '后半句「回忆涌上心头，又迟疑起来」原文没有对应词，WALLOP 被漏译；'
                '与 batch-10-part02 的 P10-0201 是同一句的两侧，措辞取一致。',
                '揍了小狼崽一顿之后，|和它交上了朋友！')
b.apply_finding('ds', 'P10-0309', '全角感叹号后面跟半角空格加半角「!」，卡面同一行混排两种标点；合并成全角。')

# This batch's `/patchDictionary/navmap.AreaB` row is not a second copy of the
# passage renamed in batch-10-part02: navmap keys exist only in patch.pak, and
# `/patchDictionary/...` is the display namespace for the same keys, so that
# entry is already fixed and this order row is stale. Left untouched on purpose.

b.reject('ds:P10-0307',
         'BadEnding 是把五行英文按特定显示行序拼成一句的排版块，而工单的行序是 row_id 排序；'
         '在不知道实际行序的情况下改任一段都可能把句子拆错，留置待渲染证据。')
b.reject('ds:P10-0308',
         'Tier1 是六级阶级名按固定网格拼出的复合块：原文把 BEGINNER 放在独立一行，'
         '提案把它并进上一行并删掉「对…来说」框架，其余分片无法验证，改动风险大于收益，留置。')

b.emit_trailing_space(skip_roots=SKIP,
                      reason='中文行尾（JSON 值末的换行之前）多出空格，英文原文行尾没有；只删空格，不动换行。')

print(b.close())
