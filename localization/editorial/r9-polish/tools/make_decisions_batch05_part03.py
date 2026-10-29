"""Write the r9 batch-05-part03 decision table.

Row ids are read back from the batch order and checked against the current
text, so a stale id fails loudly instead of binding a repair to another line.
"""
from pathlib import Path
import json

ROOT = Path(__file__).resolve().parents[4]
BASE = ROOT / 'localization/editorial/r9-polish/batch-05-part03'
ORDER = json.loads((BASE / 'orders/batch-05-part03.json').read_text('utf8'))
ROWS = {r['row_id']: (s['scene_id'], r) for s in ORDER['scenes'] for r in s['rows']}

# 本批术语全部回到 datav/dictionary.json 的条目名，并已按全库频次复核：
#   BLOCKER→阻挡者（词典；正文 5 处全留英文 Blocker）
#   FLAMER→喷火者（词典；正文 4 处误作「喷火兽」）
#   HOPPER→跳跃者（词典；女版 2 处误作「跳跳兽」，男版已是「跳跃者」）
#   TURRET→炮塔（词典；正文 19:1）、CANNON→加农炮（正文 31 处）
#   draconid→龙类（无词典条目，正文通行说法）

APPLY = [
    # —— A：超限行 ——
    ('CAT:O6a441ed4e465d53414e1', 'ds:P05c-106', 'A', 'format',
     '  Bossu: [有报道称，吸足灵能的「跳跃者」会变成「牛蛙」，能从远处朝目标喷泡泡，也能用长舌头伤人。]',
     '工单四之二点名超限：原译 57 字实测 4 行。取 DS 版（Gemini 版压到 30 字，把「有报道称」削成「据报」、「喷吐泡泡」削成「远喷泡泡」，图鉴资料口吻丢得过多）。DS 版保留报道来源、灵能吸收条件、变形结果、远程泡泡、长舌伤人五项事实，只去掉「一只」「只要…就」「甚至还能用新长出来的修长」这些修饰。'),

    # —— A：可能被升成断言 ——
    ('CAT:O25871effa77ad5bdc2c5', 'ds:P05c-101', 'B', 'meaning',
     '  Bossu: [斯凯菲亚的精灵也许全是雌性，却并非全都长生不死。]',
     '原文 MAY 是总部掌握的推测，现译「虽说全是雌性」把推测升成断言。同 root 另两版同句作「也许…雌性」，与 part01 的同类修正保持同一口径。'),

    # —— A：术语 ——
    ('CAT:O9fe6271f3979738aa046', 'ds:P05c-105', 'A', 'term',
     '  Bossu: [那看来是一只阻挡者。]',
     '正文残留未译的 BLOCKER。词典条目名为「阻挡者」，正文 5 处同类行全部留着英文 Blocker，本批一并归位。'),
    ('CAT:O082400a1a8bda600d198', 'R9M-601', 'B', 'term',
     '  Bossu: [之前有些特工的报告提到过，阻挡者对“精神”攻击较为脆弱。]',
     '同上，BLOCKERS 未译；与上一条同一场。'),
    ('CAT:O0c10e334cb4b99352c88', 'R9M-602', 'B', 'term',
     '  Bossu: [那看来是一只阻挡者。]',
     'Blocker 未译；女版同场同句（SCaf4aa1fa18c98fd1）。'),
    ('CAT:O3e46e393283fa9b6a801', 'R9M-603', 'B', 'term',
     '  Bossu: [之前有些特工的报告提到过，阻挡者对“精神”攻击较为脆弱。]',
     'Blocker 未译，且行末缺句号；与上一条同场。'),
    ('CAT:Oe28e0416ea4cd397e7c7', 'ds:P05c-105b', 'B', 'term',
     '  Bossu: [啊，那似乎是阻挡者的缩小版。]',
     '触手类条目里引用 BLOCKER 也留英文；统一为「阻挡者」并补句号。'),
    ('CAT:Ofb481ed7de5a55002a18', 'ds:P05c-111', 'B', 'term',
     '  Bossu: [我们只有那些关于 Fenfen 服装散落各处的报告。]',
     '同一场里物种名先作 Fenfen 后作 FENFEN。全库 124 处作 Fenfen、仅 3 处全大写；两侧保留半角空格（与本作其它外来名一致）。中文条目名待裁，本条只统一英文写法。'),
    ('CAT:O12d6e85c7e089bcb4dd6', 'gemini:P05c-111', 'B', 'term',
     '  Bossu: [的确。你要是有什么对付这类家伙的办法，最好也拿去用在跳跃者身上。]',
     'HOPPER 词典条目名是「跳跃者」；本行仍作「跳跳兽」，与同 root 男版（已作「跳跃者」）不一致。与上一条起名台词同一术语，两条都要改。'),
    ('CAT:Oc7f0070dd59c5752f4c3', 'ds:P05c-115', 'A', 'term',
     '  Bossu: [暂且就把它们叫“跳跃者”吧。]',
     '起名台词把 HOPPER 译成「跳跳兽」，而词典条目名是「跳跃者」；同 root 男版同句已作「跳跃者」，女版这一处是唯一偏离。只改名字，引号体例保持本行原有的弯引号。'),
    ('CAT:Of1c8f9cb526700a44f48', 'ds:P05c-112', 'B', 'term',
     '  Bossu: [“喷火者”属于龙类的一员。]',
     'FLAMER 词典条目名是「喷火者」，正文 4 处作「喷火兽」；DRACONID 无词典条目，正文通行说法是「龙类」（MauserHints「巨大的龙类」、Wyvern 场「会飞的龙类生物」），「龙兽科」是自造科名。两句一起归位。'),
    ('CAT:O1bb4879b9e1f724e2849', 'ds:P05c-113', 'B', 'term',
     '  Bossu: [要当心领地意识强的喷火者，它们会拼命朝任何闯进来的家伙喷火。]',
     '同场第二次 FLAMER；与上一条同一术语。'),
    ('CAT:O37b51f1ec51d96dcdd08', 'ds:P05c-107', 'B', 'term',
     '  Yiffai: [波苏，是这些加农炮变强了，还是我变弱了？]',
     'CANNON 在正文 31 处一律作「加农炮」，同 root 三场（CannonFloor/Ceiling/Wall）都用「加农炮」；本行写成「炮」，读者会与炮塔混淆。'),
    ('CAT:O016dfddd78a53a28315d', 'R9M-604', 'B', 'term',
     '  Yiffany: [波苏，是这些加农炮变强了，还是我变弱了？]',
     '女版同句同一问题。'),
    ('CAT:O7562468c9c7e5dcb99a4', 'ds:P05c-108', 'B', 'term',
     '  Bossu: [那些装在天花板上的炮塔全都失控了，大概是因为电力系统受损。]',
     'TURRET 词典条目名是「炮塔」，正文 19 处作「炮塔」、仅此 1 处作「炮台」；同 root 另一版同句已作「炮塔」。'),

    # —— B：跨版本不同步 ——
    ('CAT:O8c616a92219aed7662b4', 'ds:P05c-109', 'B', 'continuity',
     '  Yiffany: [当然，当然！伊吠妮通话完毕！]',
     'YIFFANY OUT 的收线套语在 BossuDex 内实测「通话完毕」11／「通话结束」2／「完毕」1／「撤了」1／「下线」1；「撤了」把收线写成离场。同 root 男版同句已作「通话完毕」。'),

    # —— B：结构与标点 ——
    ('CAT:O7b750d29eb54635b03ca', 'ds:P05c-102', 'B', 'format',
     '  Yiffai: [它们这样往我身上扑，倒更像是要把我撞倒，而不是把我弄上——]',
     '原文被截断，中文行尾留半角短横「-」；全批其它被打断处一律用「——」。'),
    ('CAT:Oaf5bc145532722948306', 'ds:P05c-103', 'B', 'format',
     '  Yiffai: [事实上，我还记录过它们起跳前会低吼。]',
     '本行是一个完整句子，下一行换波苏说话，中文却无句末标点。'),
    ('SFWc04f9c85ef1239f6c652706e', 'R9M-605', 'B', 'format',
     '  Yiffai: [事实上，我还记录过它们起跳前会低吼。]',
     '女版同句同改。'),
    ('CAT:O69f017199f0a64757e1b', 'ds:P05c-104', 'B', 'format',
     '  Yiffai: [说、说得也是……我还以为它们就是想打架。]',
     '本行是完整句子，下一行换波苏说话；缺句末标点。'),
    ('CAT:Oa6d18b09a8386995abec', 'ds:P05c-110', 'B', 'format',
     '  Yiffany: [嘿，波苏，我发现了几只小小的拟人犬家伙，但它们身上有点非常古怪的地方……]',
     '「嘿 波苏」中间夹半角空格，是译名替换留下的排版残留。'),
    ('SFWfd2c4208f624717be854fef7', 'ds:P05c-116', 'B', 'format',
     '  Yiffany: [我说啊，波苏，我不是人鱼，对吧？]',
     '同类型：半角空格夹在汉字之间，原文是逗号前的拖长称呼。'),
    ('SFW21077e81213c5d4b82446ec3', 'ds:P05c-117', 'B', 'format',
     '  Bossu: [图托恩上发生的怪事，导致有人目击到非实体的水母。]',
     '本行合并了两条英文，后一条 current 为空；句子在此完结而缺句号。'),
    ('CAT:O152354ab88dd9adae275', 'ds:P05c-118', 'B', 'format',
     '  Bossu: [那些蜥蜴狡猾得很，干海盗和贩奴的勾当出了名，还干任何到头来能赚到 LECT 的营生！]',
     '行尾残留两个半角空格；「LECT」与本作其它货币名并列时两侧留半角空格，本行紧贴汉字。只动排版，词形与语义不动。'),
    ('CAT:O21ef44fdf2e5f0271bc2', 'ds:P05c-120', 'B', 'format',
     '  Bossu: [你可以靠近它们，诱使它们自爆，或者打它们，让它们爆炸。你自己选。]',
     '两条英文合并在本行，句子在此完结而缺句号。'),
    ('CAT:Oabd418e018976095f395', 'ds:P05c-121', 'B', 'format',
     '  Bossu: [你可以靠近它们，让它们自爆，也可以打它们，让它们爆炸。你选吧。]',
     '男版同句同改。'),
    ('CAT:Of339f5abe9ca663acf16', 'ds:P05c-122', 'B', 'format',
     '  Bossu: [小心那些四处巡逻的带刺无人机。]',
     '整句到此为止，下一行是新句子；中文无句末标点会与下一行粘成一串。'),
    ('CAT:Oe8390f2ba6e9527ea456', 'R9M-606', 'B', 'format',
     '  Bossu: [小心那些四处巡逻的带刺无人机。]',
     '男版同句同改。'),
    ('SFWb5e4d1e156ca29cfd8b70e17', 'R9M-607', 'B', 'format',
     '  Bossu: [小心那些四处巡逻的带刺无人机。]',
     'SFW 女版同句同改。'),
    ('CAT:Od72b8bf1eaba1dc8db7a', 'ds:P05c-123', 'B', 'format',
     '  Bossu: [它应该也一样对物理伤害免疫。]',
     '本行是完整句子，下一行是新句；缺句末标点。'),

    # —— B：语序与语义 ——
    ('CAT:Of2eca1e7830ec0889d46', 'ds:P05c-114', 'B', 'idiom',
     '  Bossu: [它们简直就像灵能扰动化出的实体……]',
     '「被扰乱的灵能」是英文词序直搬；全库 psychic disturbance 通行译「灵能扰动」（12 处），同 root Jellyfish 场作「灵能躁动形成的幻影」。取「灵能扰动」并理顺语序，「化身」改「实体」以别于「幽灵者」这个具体名。'),
    ('CAT:Od2cc19423522ce03cf14', 'ds:P05c-119', 'B', 'idiom',
     '  Bossu: [看来这片区域的感应地雷，引信都被持续的震动激活了。]',
     '原译把「都被持续的震动激活了引信」按英文语序放在后面，中文读来像「地雷被激活了引信」；把引信提到主语位置后句子才成立。触发条件与结果不变。'),
    ('CAT:Oeb08b46de7a471930845', 'ds:P05c-124', 'B', 'idiom',
     '  Bossu: [我们当时觉得这些报告不可靠，没有采信，但是……]',
     '「把这些报告当作不可靠的给驳回了」是 DISMISS AS 的逐字直搬，「当作…给驳回」中文不成句。改为自然说法，判断与转折都不动。'),
    ('CAT:O093f9bd3100328387cf4', 'ds:P05c-126', 'B', 'meaning',
     '  Bossu: [被牢牢绑住，同伴则埋伏在附近。]',
     '原文 THEIR COMRADES HIDE NEARBY 是并列的两个情形；现译「让同伴埋伏在附近」读成「（绑住他）以便让同伴埋伏」，因果关系是加上去的。改成并列，不加因果。'),
    ('CAT:O07f26b9210ed19bf7a37', 'ds:P05c-127', 'B', 'meaning',
     '  Yiffany: [酒吧认识过一个。他老是为赌输的那些黄金和珠宝唉声叹气……]',
     '原文 HE\'D GAMBLED AWAY 是输掉，「为输光的那些黄金和珠宝唉声叹气」缺了「赌」这个动作，读起来像珠宝被别人输光。补「赌」字，其余不动。'),
    ('SFW108334757bc419a688eb6bdf', 'ds:P05c-125', 'C', 'voice',
     '  Yiffany: [这、这些一直朝我扑过来的机器虫是怎么搞的？]',
     'KEEP COMING AT ME 是被成群扑来，「冲过来」偏中性；「怎么回事」偏书面，与结巴脱口而出的口气不合。与 part01 男版同一处改法保持同源。'),
]

REJECT = [
    ('gemini:P05c-101', 'B', 'term', 'SC3011f2ede9bd4f18', 'CAT:O9fe6271f3979738aa046',
     '与本表 ds:P05c-105 同一行的同一处改动，已按行落地；本条不另立操作。'),
    ('gemini:P05c-102', 'B', 'term', 'SC3011f2ede9bd4f18', 'CAT:O082400a1a8bda600d198',
     '与本表 R9M-601 同一行；已按行落地。'),
    ('gemini:P05c-103', 'B', 'term', 'SCaf4aa1fa18c98fd1', 'CAT:O0c10e334cb4b99352c88',
     '与本表 R9M-602 同一行；已按行落地。'),
    ('gemini:P05c-104', 'B', 'term', 'SCaf4aa1fa18c98fd1', 'CAT:O3e46e393283fa9b6a801',
     '与本表 R9M-603 同一行；已按行落地。'),
    ('gemini:P05c-105', 'A', 'format', 'SCe041bcb2aac8daaa', 'CAT:O6a441ed4e465d53414e1',
     '与本表 ds:P05c-106 同一处超限压缩；Gemini 版压到 30 字，把「有报道称」削成「据报」、「喷吐泡泡」削成「远喷泡泡」，图鉴资料口吻损失过多，取 DS 版。'),
    ('gemini:P05c-107', 'B', 'format', 'SC3a3a119fd7820329', 'CAT:Ofb481ed7de5a55002a18',
     '与本表 ds:P05c-111 同一行；Gemini 版把「FENFEN」改成紧贴汉字的「关于Fenfen服装」，全库 Fenfen 与本作其它外来名一样两侧留半角空格，取 DS 版。已按行落地。'),
    ('gemini:P05c-109', 'B', 'term', 'SC7738d5683df9b077', 'CAT:O1bb4879b9e1f724e2849',
     '与本表 ds:P05c-113 同一行同一处改动，已按行落地；本条不另立操作。'),
    ('gemini:P05c-108', 'A', 'term', 'SC7738d5683df9b077', 'CAT:Of1c8f9cb526700a44f48',
     '与本表 ds:P05c-112 同一处改动，术语方向一致；本条因引号体例取 DS 版（保留本行原有的弯引号，不在单点改体例），已按行落地。'),
    ('gemini:P05c-110', 'A', 'term', 'SC14a6bdcb7cbb5e2a', 'CAT:Oc7f0070dd59c5752f4c3',
     '与本表 ds:P05c-115 同一处改动；术语方向一致，引号体例取 DS 版（保留弯引号），已按行落地。'),
    ('gemini:P05c-113', 'C', 'format', 'SCd989e3ef96634b81', 'CAT:O21ef44fdf2e5f0271bc2',
     '与本表 ds:P05c-120 同一行；已按行落地。'),
    ('gemini:P05c-114', 'C', 'format', 'SCfac2344cdaea3f1b', 'CAT:Oabd418e018976095f395',
     '与本表 ds:P05c-121 同一行；已按行落地。'),
    ('gemini:P05c-115', 'C', 'format', 'SC2ea0ca051866975b', 'CAT:Of339f5abe9ca663acf16',
     '与本表 ds:P05c-122 同一行；已按行落地。'),
    ('gemini:P05c-116', 'C', 'format', 'SC56eac4767b4dbc1a', 'CAT:Oe8390f2ba6e9527ea456',
     '与本表 R9M-606 同一行；已按行落地。'),
    ('gemini:P05c-117', 'C', 'format', 'SC242d9e3c6d253668', 'SFWb5e4d1e156ca29cfd8b70e17',
     '与本表 R9M-607 同一行；已按行落地。'),
    ('gemini:P05c-119', 'C', 'format', 'SC402bf1e2fe40a8bd', 'CAT:Od72b8bf1eaba1dc8db7a',
     '与本表 ds:P05c-123 同一行；已按行落地。'),
    ('gemini:P05c-120', 'C', 'format', 'SFW8c9e4f266f5170d665e6fc6e', 'SFW8c9e4f266f5170d665e6fc6e',
     '提案把句末补成逗号「，」以接续下一行。但下一行是另一说话人（男线）或另一条英文，跨界补逗号会让两行在渲染时读成一个未完句；这类跨行连接一率不加标点，本条驳回。'),
    ('gemini:P05c-106', 'C', 'format', 'SC3a3a119fd7820329', 'CAT:Oa6d18b09a8386995abec',
     '与本表 ds:P05c-110 同一行；已按行落地。'),
    ('gemini:P05c-112', 'C', 'format', 'SCec58e954ab659019', 'SFWfd2c4208f624717be854fef7',
     '与本表 ds:P05c-116 同一行；已按行落地。'),
]

HOLD = [
    ('gemini:P05c-118', 'B', 'format', 'SC402bf1e2fe40a8bd', 'CAT:Oe28e0416ea4cd397e7c7',
     '与本表 ds:P05c-105b 同一行同一处改动，已按 ds 版落地（含补句号）；本条重复，不另立操作。'),
    ('R9M-609', 'C', 'format', 'SC14a6bdcb7cbb5e2a', 'CAT:O85d7a4cc8a5e12558595',
     '全批「“”」与「「」」两套引号并存（本 part 9 对 10），属跨 part 格式裁决。本批只在既有行内保持原体例，不做全局统一——单批统一只会让批与批之间更不一致。'),
]

def main():
    lines = ['finding_id\troute\tseverity\tcategory\tscene_id\trow_id\tdecision\tfinal_zh\treason']
    seen = set()
    for rid, fid, sev, cat, new, reason in APPLY:
        if rid not in ROWS:
            raise SystemExit('unknown row ' + rid)
        if fid in seen:
            raise SystemExit('duplicate finding ' + fid)
        seen.add(fid)
        scene_id, row = ROWS[rid]
        if not (row['current'] or '').strip():
            raise SystemExit('blank line target ' + rid)
        if row['current'] == new:
            raise SystemExit('no-op ' + rid)
        lines.append('\t'.join((fid, fid.split(':')[0], sev, cat, scene_id, rid, 'apply', new, reason)))
    for fid, sev, cat, scene_id, rid, reason in REJECT:
        if rid not in ROWS:
            raise SystemExit('unknown row ' + rid)
        lines.append('\t'.join((fid, fid.split(':')[0], sev, cat, scene_id, rid, 'reject', '', reason)))
    for fid, sev, cat, scene_id, rid, reason in HOLD:
        if rid not in ROWS:
            raise SystemExit('unknown row ' + rid)
        lines.append('\t'.join((fid, fid.split(':')[0], sev, cat, scene_id, rid, 'hold', '', reason)))
    (BASE / 'review/decisions.tsv').write_text('\n'.join(lines) + '\n', encoding='utf8')
    print(json.dumps({'decisions': len(lines) - 1, 'apply': len(APPLY),
                      'reject': len(REJECT), 'hold': len(HOLD)}, ensure_ascii=False))


if __name__ == '__main__':
    main()
