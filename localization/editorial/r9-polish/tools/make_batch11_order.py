"""Derive batch-11's ORDER.md from the batch-09 part03 template.

batch-11 is the last loose batch: boss defeat hints plus the distorted Starkill
/Static broadcasts. Every substitution asserts on its anchor so template drift
fails loudly.
"""
from pathlib import Path
import json

ROOT = Path(__file__).resolve().parents[4]
R9 = ROOT / 'localization/editorial/r9-polish'
TPL = R9 / 'batch-09-part03/orders/ORDER.md'
BATCH = 'batch-11'

CURRENT_OLD = (
    '`current` 是 `localization/builds/r9-polish-candidate31` 的实际显示行'
    '（R9 batch-01～08 已并入），不是初翻草稿。'
    '正式台账 `zh-CN.jsonl` 只用于追溯，不得据其覆盖当前行。'
)
CURRENT_NEW = (
    '`current` 是快照 `localization/editorial/r1/corpus/snapshot-03` 的实际显示行'
    '（候选 candidate13 基线），由 `tools/build_batch.py batch-11` 生成；'
    'R9 batch-01～09 的改动都在其它 root，与本批场景不相交，正式台账 `zh-CN.jsonl` 只用于追溯，'
    '不得据其覆盖当前行。'
)

CASES_OLD = '- **needs_evidence**：原文自相矛盾、说话人／触发条件存疑。用 `status` 表达，不冒充 A/B/C。'
CASES_NEW = CASES_OLD + """
- **本批是战败提示与失真广播**：主要类别是 `gameplay`（打法提示的条件与数值）、`voice`（毛鼠／波苏的提示口吻）与 `format`（失真噪声、合句尾行）。"""

EXTRA = """12. `DefeatHints.*` 是战败后的玩法提示，不是剧情：条件、方向、数值、「会／不会」、先后顺序不得改；男女两版分别处理称呼（男线主角称星杀「姐」，女线称「弟弟」，不得互换）。
13. 失真文本（`Starkill.*`、`Static.*`）：全库失真字幕体例未终裁，本批只报单行内部可指认的错误（整句漏译、施受反转、人物挂错、把英文残形留在中文里），不统一噪声写法，也不把 `KKZZT`／`ZKRT` 一类噪声译成中文。
14. 场景名里的 `noamendfreq`／`no select`／`override` 是脚本选择条件：不改、不提案、不算漏译。"""


def sub(text, old, new):
    n = text.count(old)
    assert n == 1, f'expected 1 occurrence, found {n}: {old[:50]!r}'
    return text.replace(old, new)


def main():
    order = json.loads((R9 / BATCH / 'orders' / f'{BATCH}.json').read_text('utf8'))
    scenes, rows = len(order['scenes']), sum(len(s['rows']) for s in order['scenes'])
    text = TPL.read_text('utf8')
    text = sub(text, '# batch-09-part03 精校工单：区域场景与条件分支（第 3／4 部分）',
               '# batch-11 精校工单：其余零散条目（战败提示与失真广播）（1／1）')
    text = sub(text,
               '`localization/editorial/r9-polish/batch-09-part03/orders/batch-09-part03.reader.md`'
               ' | 工单正文：229 场、399 行、英文＋candidate26 当前中文',
               f'`localization/editorial/r9-polish/{BATCH}/orders/{BATCH}.reader.md`'
               f' | 工单正文：{scenes} 场、{rows} 行、英文＋快照基线当前中文')
    text = sub(text,
               '`localization/editorial/r9-polish/batch-09-part03/orders/batch-09-part03.json`',
               f'`localization/editorial/r9-polish/{BATCH}/orders/{BATCH}.json`')
    text = sub(text,
               '`localization/editorial/r9-polish/batch-09-part03/orders/reference-excerpt.md`'
               ' | 人物、称呼、术语、容器限制摘录',
               f'`localization/editorial/r9-polish/{BATCH}/orders/reference-excerpt.md`'
               ' | 战败提示与失真广播的口径、亲属方向、术语摘录')
    text = sub(text, CURRENT_OLD, CURRENT_NEW)
    text = sub(text, CASES_OLD, CASES_NEW)
    anchor = '11. **术语改动必须给出处**'
    end = text.index('\n\n', text.index(anchor))
    text = text[:end] + '\n' + EXTRA + text[end:]
    assert 'P09-0301' in text
    text = text.replace('P09-0301', 'P11-0101')
    out = R9 / BATCH / 'orders' / 'ORDER.md'
    out.write_text(text, 'utf8')
    print(f'{BATCH}: scenes={scenes} rows={rows} -> {out.relative_to(ROOT)}')


if __name__ == '__main__':
    main()
