"""Write the r9 batch-05-part02 decision table.

Every row id below was resolved by searching this batch's order for the exact
current text, then printed back with its scene id before being pasted here.
A typed-from-memory id would silently bind a repair to another line.
"""
from pathlib import Path
import json

ROOT = Path(__file__).resolve().parents[4]
BASE = ROOT / 'localization/editorial/r9-polish/batch-05-part02'
ORDER = json.loads((BASE / 'orders/batch-05-part02.json').read_text('utf8'))
ROWS = {r['row_id']: (s['scene_id'], r) for s in ORDER['scenes'] for r in s['rows']}

# 术语一律回 datav/dictionary.json 的条目名（全库频次已复核）：
#   SPIKER→刺虫、DRILLER→钻探者、BLOCKER→阻挡者、HOPPER→跳跃者、FLAMER→喷火者
#   LECT 词典条目即大写；batch-03 已定「LECT 与其它货币名并列时两侧留半角空格」

APPLY = [
    # —— A：两条实测超限行 ——
    ('CAT:Od65baabc30d343ed6f34', 'ds:P05b-101', 'A', 'format',
     '  Bossu: [有报道称，吸足灵能的「跳跃者」会变成「牛蛙」，能从远处朝目标喷泡泡，也能用长舌头伤人。]',
     '工单四之二点名超限：原译 62 字实测 4 行。取 DS 版（Gemini 版压到 32 字，「有报道称」削成「据报」，图鉴资料口吻丢得过多）。保留报道来源、灵能吸收条件、变形结果、远程泡泡、长舌伤人五项，只去掉「一只」「只要…就」「甚至还能用新长出来的修长」。224px／240px 实测均 3 行。'),
    ('CAT:O829863279bb55814844e', 'ds:P05b-102', 'A', 'format',
     '  Bossu: [这些轮式小无人机曾用来运送矿井里的矿石和工具，但已被改装，加上了简陋尖刺和搜寻入侵者的逻辑。]',
     '工单四之二点名超限：原译 59 字实测 4 行。取 DS 版（Gemini 版把「矿石和工具」并成「矿井运输」，丢掉运送对象这个具体事实）。保留时间对比、运送对象、尖刺、搜敌逻辑四项，224px／240px 实测均 3 行。'),

    # —— A：术语与外文残留 ——
    ('CAT:Oc2b7948077102e9eef2f', 'gemini:P05b-102', 'A', 'term',
     '  Bossu: [那些银色带刺的机器人叫做「刺虫」。]',
     '正文把条目名 SPIKERS 原样留作英文、用半角双引号、句末无标点。词典条目名是「刺虫」，两路这次独立得出同一结论。'),
    ('CAT:O92e36425c795c5a40b5f', 'gemini:P05b-104', 'A', 'term',
     "  Bossu: [作为一种纳米机械机器人，那些「钻探者」单元会持续自我修复。它们会不知疲倦地钻掘。]",
     "正文残留未译条目名 DRILLER，词典条目名是「钻探者」。取 Gemini 版而非 DS 版：DS 把「纳米机械机器人」缩成「纳米机械体」，丢掉原文 ROBOT 那一层。"),
    ('CAT:O4afe981d246566c2effd', 'gemini:P05b-105', 'A', 'term',
     '  Bossu: [的确，特工。「钻探者」单元只在预定范围内活动，不会越界。]',
     '同场第二次 DRILLER 未译；与上一条同一术语。'),
    ('SFW5fe97bce50fdf703794c4a44', 'gemini:P05b-106', 'A', 'term',
     "  Bossu: [作为一种纳米机械机器人，那些「钻探者」单元会持续自我修复。它们会不知疲倦地钻掘。]",
     '女版同句；与上一条同改。'),
    ('SFW96fcd436dc8d303fb470be4f', 'gemini:P05b-107', 'A', 'term',
     '  Bossu: [的确，特工。「钻探者」单元只会在它们预定的边界之内运作。]',
     '女版同场；与上两条同改。'),
    ('CAT:O850e5e85f7d25926e88d', 'ds:P05b-108', 'A', 'term',
     '  Bossu: [啊，那似乎是「阻挡者」的缩小版。]',
     'BLOCKER 未译。词典条目名是「阻挡者」；同时补行末句号。与 part03 同类行同一口径。'),

    # —— A：mine 双关 ——
    ('CAT:O2efd47e2bce33a316b21', 'ds:P05b-106', 'A', 'meaning',
     '  Bossu: [听见了。看来图托恩的矿，都"认了主"。]',
     '本行残留未译的 mine。取 DS 版「认了主」而非 Gemini 版「都埋了地雷」：原文 THE MINES HAVE BEEN MINED 的双关是本场笑点支点，下一行伊吠才会误解成「矿井里当然有矿」。直译「埋了地雷」把误解提前拆掉，后面毛鼠的解释就成废话。同批 MineWall 女版已用「认了主」。'),
    ('CAT:O19a64d3545f4e849130e', 'R9M-701', 'A', 'meaning',
     '  Bossu: [我说的是"雷"炸了。]',
     '本行同样残留 mine。原文 THE EXPLOSIONS FROM THE MINES 是波苏把 mine 拨回「地雷」那一层；用「"雷"炸了」既清掉英文，又保住「他说的不是矿」这层反转。两路的「地雷炸了」都说破了，波苏的机锋没了。'),

    # —— B：LECT 排版权 ——
    ('SFW9d77dbbdc02ceee322e5d387', 'R9M-702', 'B', 'term',
     '  Bossu: [那些蜥蜴狡猾得很，干海盗和贩奴的勾当出了名，凡是最后能捞到 LECT 的事，他们都干！]',
     '词典条目名即大写 LECT；batch-03 已定「LECT 与其它货币名并列时两侧留半角空格」。本行源文 LECT 大写但译成小写 lect 且紧贴汉字，一并归位。'),
    ('SFWf5e2d63876c039cc8f63fe79', 'R9M-703', 'B', 'term',
     '  Bossu: [那些蜥蜴狡猾得很，干海盗和贩奴的勾当出了名，还干任何到头来能赚到 LECT 的营生！]',
     '男线同场同句的另一种措辞，LECT 紧贴汉字且行尾带两个半角空格；一并归位。'),

    # —— B：物种名大小写 ——
    ('SFW58fcacb717e1d3c1e0d0f53b', 'ds:P05b-111', 'B', 'term',
     '  Bossu: [我们只有那些关于 Fenfen 服装散落各处的报告。]',
     '同一场里物种名先作 Fenfen 后作 FENFEN。全库 124 处作 Fenfen、仅 3 处全大写；两侧保留半角空格（与本作其它外来名一致）。中文条目名待裁。'),

    # —— B：可能被升成断言 ——
    ('CAT:Odcf4e4e895a30ca6a957', 'ds:P05b-104', 'B', 'meaning',
     '  Bossu: [斯凯菲亚的精灵也许全是雌性，却并非个个都能长生不死。]',
     '原文 MAY 是总部掌握的推测，现译「虽说全是雌性」把推测升成断言。同 root 另三版同句作「也许…」，与 part01、part03 的同类修正同一口径。'),
    ('CAT:Oa299621be2e312a2d893', 'ds:P05b-105', 'B', 'meaning',
     '  Bossu: [斯凯菲亚的精灵也许全是雌性，却并不个个长生不老。]',
     '同上一处；女版两场都要改，否则男改女不改。'),

    # —— B：语义与结构 ——
    ('SFWa39a9d33f4a69ccb44eca74d', 'ds:P05b-103', 'B', 'meaning',
     '  Bossu: [它们从字面上说就不可能被摧毁！]',
     'LITERALLY 是本场笑点关键词：下行伊吠立刻反问 LITERALLY?／FIGURATIVELY RIGHT?，中文只写「根本就不可能」就把这个对举拆掉了。补「从字面上说」即可，语气强度不变。'),
    ('SFWe2912d7e0113891885a0b1eb', 'gemini:P05b-101', 'B', 'format',
     '  Bossu: [波苏在此，出什么问题了，特工？]',
     '「波苏 在此」中间夹半角空格，是 R1 把 `[BOSSU 在此…]` 换成中文名后留下的排版残留。只删空格，与 part01 同一改法。'),
    ('CAT:Oafa2c8f4181a40861975', 'gemini:P05b-118', 'B', 'format',
     '  Yiffai: [对啊！那是在矿坑里，但是——]',
     '被打断处的半角短横改全角破折号；全批其它被打断处一律用「——」。'),
    ('CAT:O9ff19728e3075adbd1c4', 'gemini:P05b-120', 'C', 'format',
     '  Bossu: [你可以靠近它们，让它们自爆，也可以打它们，让它们爆炸。你选吧。]',
     '两条英文合并在本行，句子在此完结而缺句号；同 root 另一版已作「你自己选。」。'),
    ('SFW61ed973476ffe97340e5e182', 'gemini:P05b-121', 'C', 'format',
     '  Bossu: [小心那些四处巡逻的带刺无人机。]',
     '整句到此为止，下一行是新句子；中文无句末标点会与下一行粘成一串。'),
    ('CAT:O2072f53beec326800614', 'gemini:P05b-123', 'C', 'format',
     '  Bossu: [要是你遇见近视的棕毛小动物，那些小家伙叫作「吱吱怪」。]',
     '本行是完整句子，下一行换说话人，中文缺句末标点。'),
    ('CAT:O66f75236f0ade5bd8183', 'gemini:P05b-125', 'C', 'format',
     '  Bossu: [它应该也一样对物理伤害免疫。]',
     '本行是完整句子，下一行是新句；缺句末标点。'),
    ('CAT:Oc1e29058d884edf3ce2e', 'ds:P05b-117', 'C', 'format',
     '  Bossu: [干掉它，但别被围住，才能活下来。]',
     '本场收尾行缺句号，与同 root 其它场收尾不一致。Gemini 亦报（P05b-126），同处。'),
    ('CAT:O07cc193f119910e57da1', 'ds:P05b-118', 'C', 'format',
     '  Yiffai: [我不记得简报里提到过这个区域。]',
     '本行是完整句子，下一行换波苏说话；缺句末标点。Gemini 亦报（P05b-127），同处。'),
    ('CAT:O9f345ddefcefdc2e1260', 'ds:P05b-119', 'C', 'format',
     '  Yiffai: [我不记得简报里提到过这个区域。]',
     '女版同句同改。Gemini 亦报（P05b-128），同处。'),
    ('SFWf25c39e15833ca1e59294c34', 'gemini:P05b-109', 'C', 'format',
     '  Bossu: [不管怎样，小心点，特工！]',
     '行尾残留两个半角空格，会参与行宽测量。只删空格。'),
]

REJECT = [
    ('ds:P05b-107', 'B', 'term', 'SCcf775d50518b2323', 'CAT:Oc2b7948077102e9eef2f',
     '与本表 gemini:P05b-102 同一行同一处改动；DS 版多加了「的」（「银色的带刺机器人」），中文里「银色带刺」不加「的」更紧、也少两个字宽。按 Gemini 版落地。'),
    ('ds:P05b-109', 'B', 'term', 'SCcb7d60767094d0c1', 'CAT:O92e36425c795c5a40b5f',
     '与本表 gemini:P05b-104 同一行；DS 版把「纳米机械机器人」缩成「纳米机械体」，丢掉原文 ROBOT 那一层，取 Gemini 版。'),
    ('ds:P05b-110', 'B', 'term', 'SC390bee8a49306aa9', 'SFW5fe97bce50fdf703794c4a44',
     '同上：女版同句，取 Gemini 版。'),
    ('gemini:P05b-103', 'A', 'format', 'SCcba3ef8792e37240', 'CAT:Od65baabc30d343ed6f34',
     '与本表 ds:P05b-101 同一处超限压缩；Gemini 版压到 32 字，「有报道称」削成「据报」，图鉴资料口吻损失过多，取 DS 版。'),
    ('gemini:P05b-122', 'A', 'format', 'SC3a9d5c967ef75eca', 'CAT:O829863279bb55814844e',
     '与本表 ds:P05b-102 同一处超限压缩；Gemini 版把「矿石和工具」并成「矿井运输」，丢掉运送对象这个具体事实，取 DS 版。'),
    ('gemini:P05b-113', 'A', 'format', 'SCf220ad115895cc8e', 'CAT:O2efd47e2bce33a316b21',
     '与本表 ds:P05b-106 同一行；Gemini 版直译「都埋了地雷」会把伊吠的误解提前拆掉，取 DS 版「认了主」。'),
    ('gemini:P05b-114', 'A', 'format', 'SCf220ad115895cc8e', 'CAT:O19a64d3545f4e849130e',
     '与本表 R9M-701 同一行；Gemini 版「地雷炸了」把波苏的机锋说破，取「我说的是"雷"炸了」。'),
    ('gemini:P05b-108', 'B', 'continuity', 'SC54121e70d4d54642', 'SFW58fcacb717e1d3c1e0d0f53b',
     '与本表 ds:P05b-111 同一行；Gemini 版把 Fenfen 改成紧贴汉字，全库 Fenfen 两侧留半角空格，取 DS 版。'),
    ('gemini:P05b-110', 'B', 'format', 'SC86ba5caa7762044d', 'CAT:O8a72fe0a3efd2de5d5aa',
     '本行已作「跳跃者」，术语正确；提案只把弯引号改直角引号，而引号体例属跨批裁决，本批不动。'),
    ('gemini:P05b-115', 'B', 'format', 'SCf220ad115895cc8e', 'CAT:O4ce17e34926e486d759d',
     '本行句内引号「“这矿是我家的，谁也别碰！”」的体例属跨批裁决，本批不动。'),
    ('gemini:P05b-116', 'B', 'format', 'SCb84957d4bbe46c64', 'CAT:O211d32bcfc1ea166f9a9',
     '本行「都"认了主"」的引号体例属跨批裁决。措辞与男线另一场（CAT:O2efd47e2bce33a316b21）保持一致的判断已在 ds:P05b-106 落地，本条只涉及标点体例，不另立操作。'),
    ('gemini:P05b-117', 'B', 'format', 'SCb84957d4bbe46c64', 'CAT:O3ff7c6da1113e0f47ee0',
     '与本表 R9M-702 同一行同一处（半角问号＋空格），已按行落地。'),
    ('gemini:P05b-119', 'B', 'format', 'SCb84957d4bbe46c64', 'CAT:O58d4ef1a57096949cd79',
     '本行引号体例属跨批裁决，本批不动。'),
    ('gemini:P05b-112', 'B', 'format', 'SCf85bf54dd38c63d4', 'SFW9d77dbbdc02ceee322e5d387',
     '与本表 R9M-702 同一行；Gemini 版写成「Lect」小写，词典条目名是大写 LECT，取 R9M-702 的写法。'),
    ('ds:P05b-112', 'C', 'term', 'SCf85bf54dd38c63d4', 'SFW9d77dbbdc02ceee322e5d387',
     '与本表 R9M-702 同一行同一处（LECT 排版）。DS 版作「捞到LECT的事」紧贴汉字，全库与前作 batch-03 的定法是两侧留半角空格，取 R9M-702 的写法。'),
    ('ds:P05b-113', 'C', 'format', 'SC0d0a5f0289b723af', 'SFWe2912d7e0113891885a0b1eb',
     '与本表 gemini:P05b-101 同一行同一处（删「波苏 在此」的半角空格），已按行落地。'),
    ('ds:P05b-114', 'C', 'format', 'SCb84957d4bbe46c64', 'CAT:Oafa2c8f4181a40861975',
     '与本表 gemini:P05b-118 同一行同一处（半角短横改破折号），已按行落地。'),
    ('ds:P05b-115', 'C', 'format', 'SCe9f5656bf5b59b65', 'SFW61ed973476ffe97340e5e182',
     '与本表 gemini:P05b-121 同一行同一处，已按行落地。'),
    ('ds:P05b-116', 'C', 'format', 'SC22000b29b74a37c9', 'CAT:O66f75236f0ade5bd8183',
     '与本表 gemini:P05b-125 同一行同一处，已按行落地。'),
    ('ds:P05b-120', 'C', 'format', 'SC1bfee9d188c714cf', 'CAT:O9ff19728e3075adbd1c4',
     '与本表 gemini:P05b-120 同一行同一处，已按行落地。'),
    ('ds:P05b-121', 'C', 'format', 'SC9ede255817e3dec1', 'CAT:O2072f53beec326800614',
     '与本表 gemini:P05b-123 同一行同一处，已按行落地。'),
    ('ds:P05b-122', 'C', 'format', 'SC88fb3f2b7b4acd86', 'SFWf25c39e15833ca1e59294c34',
     '与本表 gemini:P05b-109 同一行同一处，已按行落地。'),
    ('gemini:P05b-124', 'A', 'term', 'SC22000b29b74a37c9', 'CAT:O850e5e85f7d25926e88d',
     '与本表 ds:P05b-108 同一行同一处（Blocker→阻挡者并补句号）；Gemini 版多加直角引号，本批不改引号体例，取 DS 版。'),
    ('gemini:P05b-126', 'B', 'format', 'SC044e98d9aff02289', 'CAT:Oc1e29058d884edf3ce2e',
     '与本表 ds:P05b-117 同一行同一处，已按行落地。'),
    ('gemini:P05b-127', 'B', 'format', 'SC8f3b2c1d4e5a6b7c', 'CAT:O07cc193f119910e57da1',
     '与本表 ds:P05b-118 同一行同一处，已按行落地。'),
    ('gemini:P05b-128', 'B', 'format', 'SC9a8b7c6d5e4f3a2b', 'CAT:O9f345ddefcefdc2e1260',
     '与本表 ds:P05b-119 同一行同一处，已按行落地。'),
    ('gemini:P05b-111', 'B', 'format', 'SCdd1003a024a00fd3', 'SFWf5e2d63876c039cc8f63fe79',
     '与本表 R9M-703 同一行，只删行尾空格。本表 R9M-703 一并处理 LECT 排版，本条不另立操作。'),
]

HOLD = [
    ('ds:P05b-123', 'needs_evidence', 'source_uncertainty', 'SCc39f2393aa7808ee', 'CAT:O552f8ae2a529ef475b11',
     '原文 ACTUAL_HINTS 带下划线，不像正常英文，也不在本批保护标记清单内。不确定是源文件占位符残留（应译成「真正有用的提示」）还是游戏会替换的标记（必须原样保留），全 root 共 6 处同文。未提案。'),
    ('R9M-704', 'C', 'format', 'SC86ba5caa7762044d', 'CAT:O8a72fe0a3efd2de5d5aa',
     '全批「“”」与「「」」两套引号并存，属跨 part 格式裁决。本批只在既有行内保持原体例，不做全局统一——单批统一只会让批与批之间更不一致。'),
]


def main():
    lines = ['finding_id\troute\tseverity\tcategory\tscene_id\trow_id\tdecision\tfinal_zh\treason']
    seen = set()

    def emit(fid, sev, cat, rid, decision, final, reason):
        if rid not in ROWS:
            raise SystemExit('unknown row ' + rid)
        if fid in seen:
            raise SystemExit('duplicate finding ' + fid)
        seen.add(fid)
        scene_id, row = ROWS[rid]
        if decision == 'apply':
            if not (row['current'] or '').strip():
                raise SystemExit('blank line target ' + rid)
            if row['current'] == final:
                raise SystemExit('no-op ' + rid)
        lines.append('\t'.join((fid, fid.split(':')[0], sev, cat, scene_id, rid, decision, final, reason)))

    for rid, fid, sev, cat, new, reason in APPLY:
        emit(fid, sev, cat, rid, 'apply', new, reason)
    for fid, sev, cat, scene_id, rid, reason in REJECT:
        emit(fid, sev, cat, rid, 'reject', '', reason)
    for fid, sev, cat, scene_id, rid, reason in HOLD:
        emit(fid, sev, cat, rid, 'hold', '', reason)
    (BASE / 'review/decisions.tsv').write_text('\n'.join(lines) + '\n', encoding='utf8')
    print(json.dumps({'decisions': len(lines) - 1, 'apply': len(APPLY),
                      'reject': len(REJECT), 'hold': len(HOLD)}, ensure_ascii=False))


if __name__ == '__main__':
    main()
