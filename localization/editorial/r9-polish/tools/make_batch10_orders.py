"""Derive the three batch-10 ORDER.md files from the batch-09 template.

The batch-09 part03 order is the current template. batch-10 is interface and
system text, so the container limits, the protected markers and the categories
differ; every substitution below asserts on its anchor so a template drift
fails loudly instead of producing a half-correct order.
"""
from pathlib import Path
import json

ROOT = Path(__file__).resolve().parents[4]
R9 = ROOT / 'localization/editorial/r9-polish'
TPL = R9 / 'batch-09-part03/orders/ORDER.md'
EXCERPT = R9 / 'batch-10/orders/reference-excerpt.md'

CONTAINER_OLD = (
    '5. 剧情框约 240px、12px 字；单行正文尽量不超过约 20 个全角字。'
    '确实必须更长时，在 `note` 写 `行宽待实测` 并说明理由。'
)
CONTAINER_NEW = """5. 容器限制（已实测）：卡面 16 列 × 128px、≤15 行；数据书 224px、≤3 行；剧情框 12px／240px 折行、每页 3 行。界面行变长会挤爆版面或触发翻页异常，改写须保证同一单元的段数与行数不增；确实必须更长时在 `note` 写 `行宽待实测` 并说明理由。"""

EXTRA_CONSTRAINTS = """12. `|` 是行切分标记（卡面三行就是三段）：段数与位置一律不动，改写后仍是同样段数，每段尽量 ≤ 约 20 个全角字。
13. 制作名单（`ui.end`）、赞助者名单（`ui.backers`）的行首行尾空格是居中装置：不报、不删、不改。
14. 按键名（`UP+ATK`、`R2`、`L1`、`TRIANGLE`、`CIRCLE`、`START/OPTIONS`、`DPAD UP`、`L STICK LEFT`）、坐标数字与逗号后半角空格（`109, 088`）原样保留。
15. `/patchDictionary/navmap` 与 `navmap` 是同一批地名的两侧（patch／jar）：同一地名要两侧一起改，只改一侧会让游戏内显示不一致。"""

CURRENT_OLD = (
    '`current` 是 `localization/builds/r9-polish-candidate31` 的实际显示行'
    '（R9 batch-01～08 已并入），不是初翻草稿。'
    '正式台账 `zh-CN.jsonl` 只用于追溯，不得据其覆盖当前行。'
)
CURRENT_NEW = (
    '`current` 是快照 `localization/editorial/r1/corpus/snapshot-03` 的实际显示行'
    '（候选 candidate13 基线），由 `tools/build_batch.py batch-10 --parts 3 --part K` 生成；'
    'R9 batch-01～09 的改动都在其它 root，与本批场景不相交，正式台账 `zh-CN.jsonl` 只用于追溯，'
    '不得据其覆盖当前行。'
)

CASES_NOTE_OLD = '- **needs_evidence**：原文自相矛盾、说话人／触发条件存疑。用 `status` 表达，不冒充 A/B/C。'
CASES_NOTE_NEW = CASES_NOTE_OLD + """
- **本批是界面与系统文本**：主要类别是 `format`（段数、`|` 标记、对齐空格、按键名、坐标）与 `term`（界面术语一致性）；`voice` 只在结局名单与资料卡文案里出现，`gameplay` 只在数值／条件类标签里出现（`DEFEAT 1～4`、作弊码说明）。"""


def sub(text, old, new, where):
    n = text.count(old)
    assert n == 1, f'{where}: expected 1 occurrence, found {n}: {old[:40]!r}'
    return text.replace(old, new)


def main():
    template = TPL.read_text('utf8')
    excerpt = EXCERPT.read_text('utf8')
    for k in (1, 2, 3):
        part = f'batch-10-part0{k}'
        order = json.loads((R9 / part / 'orders' / f'{part}.json').read_text('utf8'))
        scenes, rows = len(order['scenes']), sum(len(s['rows']) for s in order['scenes'])
        text = template
        text = sub(text,
                   '# batch-09-part03 精校工单：区域场景与条件分支（第 3／4 部分）',
                   f'# {part} 精校工单：界面与系统文本（UI 与其他）（第 {k}／3 部分）', part)
        text = sub(text,
                   '`localization/editorial/r9-polish/batch-09-part03/orders/batch-09-part03.reader.md`'
                   ' | 工单正文：229 场、399 行、英文＋candidate26 当前中文',
                   f'`localization/editorial/r9-polish/{part}/orders/{part}.reader.md`'
                   f' | 工单正文：{scenes} 场、{rows} 行、英文＋快照基线当前中文', part)
        text = sub(text,
                   '`localization/editorial/r9-polish/batch-09-part03/orders/batch-09-part03.json`',
                   f'`localization/editorial/r9-polish/{part}/orders/{part}.json`', part)
        text = sub(text,
                   '`localization/editorial/r9-polish/batch-09-part03/orders/reference-excerpt.md`'
                   ' | 人物、称呼、术语、容器限制摘录',
                   f'`localization/editorial/r9-polish/{part}/orders/reference-excerpt.md`'
                   ' | 界面文本特点、名字与地名写法、容器限制摘录', part)
        text = sub(text, CURRENT_OLD, CURRENT_NEW, part)
        text = sub(text, CASES_NOTE_OLD, CASES_NOTE_NEW, part)
        text = sub(text, CONTAINER_OLD, CONTAINER_NEW, part)
        anchor = '11. **术语改动必须给出处**'
        idx = text.index(anchor)
        end = text.index('\n\n', idx)
        text = text[:end] + '\n' + EXTRA_CONSTRAINTS + text[end:]
        assert 'P09-0301' in text
        text = text.replace('P09-0301', f'P10-0{k}01')
        out = R9 / part / 'orders' / 'ORDER.md'
        out.write_text(text, 'utf8')
        (R9 / part / 'orders' / 'reference-excerpt.md').write_text(excerpt, 'utf8')
        print(f'{part}: scenes={scenes} rows={rows} -> {out.relative_to(ROOT)}')


if __name__ == '__main__':
    main()
