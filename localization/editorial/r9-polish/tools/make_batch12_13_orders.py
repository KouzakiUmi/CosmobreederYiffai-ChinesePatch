"""Write the ORDER.md for the two scope-expansion batches.

batch-12 reuses the interface order (batch-10) because the medium is the same —
short labels rendered into fixed-width panels — but the rows are dictionary
entries and mission-log fields, so the pipe/segment rules are replaced by
label rules. batch-13 reuses the battle-hint order (batch-11) because Mauser's
narration is a gameplay hint too.

Read-only over the templates; writes only the ORDER.md files.
"""
from pathlib import Path
import json

R9 = Path(__file__).resolve().parents[1]
R9 = Path(__file__).resolve().parents[1]


def order_json(batch):
    return json.loads((R9 / batch / 'orders' / (batch + '.json')).read_text('utf8'))


def summary(batch):
    order = order_json(batch)
    scenes = order['scenes']
    rows = sum(len(s['rows']) for s in scenes)
    return len(scenes), rows


def batch12(part, parts, template):
    batch = 'batch-12-part%02d' % part
    scenes, rows = summary(batch)
    t = template
    t = t.replace('# batch-10-part01 精校工单：界面与系统文本（UI 与其他）（第 1／3 部分）',
                  '# %s 精校工单：界面与系统文本——未覆盖的词典与任务日志条目（第 %d／%d 部分）'
                  % (batch, part, parts))
    t = t.replace('batch-10-part01', batch)
    t = t.replace('batch-10 的', 'batch-12 的')
    t = t.replace('98 场、459 行', '%d 场、%d 行' % (scenes, rows))
    t = t.replace('`tools/build_batch.py batch-10 --parts 3 --part K`',
                  '`tools/build_batch.py batch-12 --parts 3 --part K`')
    t = t.replace('R9 batch-01～09 的改动都在其它 root，与本批场景不相交',
                  'R9 batch-01～11 的改动都在其它 root，与本批场景不相交'
                  '（本批是 `BATCHES` 选择器产出的「其余部分」：已由前批覆盖的场次已被排除）')
    t = t.replace(
        '- **本批是界面与系统文本**：主要类别是 `format`（段数、`|` 标记、对齐空格、按键名、坐标）与 `term`（界面术语一致性）；`voice` 只在结局名单与资料卡文案里出现，`gameplay` 只在数值／条件类标签里出现（`DEFEAT 1～4`、作弊码说明）。',
        '- **本批是词典条目与任务日志**：主要类别是 `term`（同一生物／道具／地名的多种写法）与 `format`（`|` 占位、行尾空格、坐标）；`voice` 只在任务日志正文里出现，`meaning` 集中在明显误译的短标签。')
    t = t.replace(
        '5. 容器限制（已实测）：卡面 16 列 × 128px、≤15 行；数据书 224px、≤3 行；剧情框 12px／240px 折行、每页 3 行。界面行变长会挤爆版面或触发翻页异常，改写须保证同一单元的段数与行数不增；确实必须更长时在 `note` 写 `行宽待实测` 并说明理由。',
        '5. 本批值是**短标签**：词典标签与任务日志字段共用固定列宽，改写后长度不得超过原文（英文原长即上限）；只能同长或更短，不得加解释性文字。确实必须更长时在 `note` 写 `行宽待实测` 并说明理由。')
    t = t.replace(
        '12. `|` 是行切分标记（卡面三行就是三段）：段数与位置一律不动，改写后仍是同样段数，每段尽量 ≤ 约 20 个全角字。\n'
        '13. 制作名单（`ui.end`）、赞助者名单（`ui.backers`）的行首行尾空格是居中装置：不报、不删、不改。\n'
        '14. 按键名（`UP+ATK`、`R2`、`L1`、`TRIANGLE`、`CIRCLE`、`START/OPTIONS`、`DPAD UP`、`L STICK LEFT`）、坐标数字与逗号后半角空格（`109, 088`）原样保留。\n'
        '15. `/patchDictionary/navmap` 与 `navmap` 是同一批地名的两侧（patch／jar）：同一地名要两侧一起改，只改一侧会让游戏内显示不一致。',
        '12. **场景名（`root`）是内部键，不是文本**：`ClassicBulber`、`Bomb`、`SpecialHookshot` 这类键名一律不改、不提案；只改值（`current`）。\n'
        '13. **短标签按库内多数写法统一**：同一英文在两侧（sfw／nsfw）或两处写法不同时，先数频次再定方向，并把两侧 `row_id` 一起报；不要凭印象改。\n'
        '14. **任务日志 `text` 场是占位样例行**（原文 `Line 1 | Line 2 …`）：与英文结构一致就记 `retain`，不重写、不"润色"。\n'
        '15. 地名（泽罗尼亚、艾斯卡姆尔、斯凯菲亚、仓库B、流放地、图托恩等）与物品名要与已落地写法一致；商店 `displayName` 与 `ui.item` 的物品名一致。\n'
        '16. `|` 与行尾空格：值内若含 `|`，它是字段分隔，不改位置；行尾空格判据只看英文原文行行尾，英文没有就删。')
    t = t.replace('`P10-0101`', '`P12-%02d01`' % part)
    return t


def batch13(template):
    batch = 'batch-13'
    scenes, rows = summary(batch)
    t = template
    t = t.replace('# batch-11 精校工单：其余零散条目（战败提示与失真广播）（1／1）',
                  '# batch-13 精校工单：毛鼠旁白提示（MauserHints）（1／1）')
    t = t.replace('batch-11', 'batch-13')
    t = t.replace('109 场、505 行', '%d 场、%d 行' % (scenes, rows))
    t = t.replace('R9 batch-01～09 的改动都在其它 root，与本批场景不相交',
                  'R9 batch-01～11 的改动都在其它 root，与本批场景不相交；'
                  '`MauserHints_AreaA` 已在 batch-01 精校过，不在本批范围内')
    t = t.replace(
        '- **本批是战败提示与失真广播**：主要类别是 `gameplay`（打法提示的条件与数值）、`voice`（毛鼠／波苏的提示口吻）与 `format`（失真噪声、合句尾行）。',
        '- **本批是毛鼠的旁白提示**：主要类别是 `gameplay`（提示指向的地图物件、条件与顺序）、`voice`（毛鼠碎嘴、带情绪的口吻）与 `continuity`（提示与已落地剧情是否对得上）。')
    t = t.replace(
        '12. `DefeatHints.*` 是战败后的玩法提示，不是剧情：条件、方向、数值、「会／不会」、先后顺序不得改；男女两版分别处理称呼（男线主角称星杀「姐」，女线称「弟弟」，不得互换）。\n'
        '13. 失真文本（`Starkill.*`、`Static.*`）：全库失真字幕体例未终裁，本批只报单行内部可指认的错误（整句漏译、施受反转、人物挂错、把英文残形留在中文里），不统一噪声写法，也不把 `KKZZT`／`ZKRT` 一类噪声译成中文。\n'
        '14. 场景名里的 `noamendfreq`／`no select`／`override` 是脚本选择条件：不改、不提案、不算漏译。',
        '12. `MauserHints*` 是毛鼠报给你的旁白提示，不是剧情台词：提示指向的物件、可交互对象、方向与先后顺序不得改；不得把提示改写成「建议」或加剧情。\n'
        '13. **先查 R8 的谜题提示裁决**：`localization/editorial/r8-puzzle/README.md` 已裁决过一批提示措辞，与之冲突的提案不要提；`MauserHints_AreaA` 已由 batch-01 精校，不在本批。\n'
        '14. 场景名里的 `noamendfreq`／`no select`／`override` 是脚本选择条件：不改、不提案、不算漏译。\n'
        '15. 提示是「短促的一句话」：改写后长度不得明显超过原文（提示框窄），也不能靠加标点凑语气。')
    t = t.replace('`P11-0101`', '`P13-0101`')
    return t


def main():
    tpl12 = (R9 / 'batch-10-part01/orders/ORDER.md').read_text('utf8')
    for part in (1, 2, 3):
        batch = 'batch-12-part%02d' % part
        (R9 / batch / 'orders/ORDER.md').write_text(batch12(part, 3, tpl12), 'utf8')
        print('wrote', batch, 'ORDER.md')
    tpl13 = (R9 / 'batch-11/orders/ORDER.md').read_text('utf8')
    (R9 / 'batch-13/orders/ORDER.md').write_text(batch13(tpl13), 'utf8')
    print('wrote batch-13 ORDER.md')


if __name__ == '__main__':
    main()
