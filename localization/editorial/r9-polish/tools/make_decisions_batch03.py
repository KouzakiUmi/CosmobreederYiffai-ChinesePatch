"""Write the r9 batch-03 decision table from reviewed choices."""
from pathlib import Path
import json

ROOT = Path(__file__).resolve().parents[4]
BASE = ROOT / 'localization/editorial/r9-polish/batch-03'
ORDER = json.loads((BASE / 'orders/batch-03.json').read_text('utf8'))
ROWS = {r['row_id']: (s['scene_id'], r) for s in ORDER['scenes'] for r in s['rows']}

# row_id, finding_id, severity, category, new line, reason
APPLY = [
    ('CAT:O9e8c6bc92c5b884e1cb3', 'ds:P03-001', 'A', 'meaning',
     '  Yiffai: 我……我很抱歉……伊、伊吠，通话完毕！',
     'OUT 是无线电断线，现译「先走了」写成离开现场；女线同场为「伊吠妮结束通话！」。男线改用通讯收线，不补动作。'),
    ('CAT:O1d1de1873ef4c286442a', 'R9M-301', 'A', 'meaning',
     '  Yiffai: 我……我很抱歉……伊、伊吠，通话完毕！',
     'GenderSwappedPickup 男线同文同句，一并统一。'),
    ('CAT:O8ed5328423c2d0e56b38', 'ds:P03-004', 'A', 'meaning',
     '  Bossu: [你快到那个房间了，你弟弟就是在那儿被黑暗能量吞噬的。]',
     'OVERTAKEN BY DARK ENERGY 是「被黑暗能量吞噬／侵蚀」；现译「被黑暗能量控制」把状态写成被操控，与男线同场另一句的分叉也不一致。'),
    ('CAT:O24cd6378b36499ce88d2', 'ds:P03-005', 'A', 'relationship',
     '  Bossu: [你快要接近那间房间了，你姐姐就是在那儿被黑暗能量吞噬的。]',
     '男线女主视角这段 SIBLING 指姐姐（女线整部作品的关系已由 R3 与参照确认）；「手足」把已定的姐弟关系悬空。'),
    ('CAT:O633dd30d9d8ac4dd23cf', 'gemini:P03-003', 'B', 'term',
     '  Bossu: [听好了，根据PPP法令2348.832.01A条，我命令你把无线电还给它的主人。]',
     '本作通讯设备在全库 42 处作「无线电」，「通讯器」只见此二处；同一句在同一批里出现两个装置名。法令编号逐字保留。'),
    ('CAT:Oa5cf4f42568296c05e07', 'R9M-302', 'B', 'term',
     '  Bossu: [听好了，根据PPP法令2348.832.01A条，我命令你把无线电还给它的主人。]',
     'SlimePickup 同文同句，与 FeralPickup 一并统一。'),
    ('CAT:O34a712d957a3b37024a7', 'gemini:P03-007', 'B', 'term',
     '  Bossu: [干得好，伊吠，潘科是顶尖特工之一。]',
     '全库 471 处 agent 作「特工」，「干员」仅 13 处散见；R2 已明确不把现用「特工」批量改掉。此处只改本行的「干员」并去掉人名旁多出的空格。'),
    ('SFW756f2f673f7ffa4300e97c94', 'R9M-303', 'B', 'term',
     '  Bossu: [干得好，伊吠，潘科是顶尖特工之一。]',
     '同一句的 SFW 版同改。'),
    ('CAT:O66e4355b77d4646c9ea6', 'gemini:P03-014', 'B', 'format',
     '  Bossu: [我们刚收到特工塞塔特尼的消息，说你成功救出了对方。]',
     '人名两侧的多余空格在 12px 行里露出等宽缝；本作人名不带空格。'),
    ('SFW87e6ee1c64e37e3cb5269294', 'R9M-304', 'B', 'format',
     '  Bossu: [我们刚收到特工塞塔特尼的消息，说你成功救出了对方。]',
     'SFW 版同句同改。'),
    ('SFW179934b1d5a42a73a1099914', 'gemini:P03-024', 'B', 'voice',
     '  Bossu: [好小子，期待看到那份数据！]',
     'GOOD BOY 是对男线主角的固定表扬；现译「乖，等着看你的数据！」既丢称呼又像哄宠物。女线同句作「好女孩」。'),
    ('CAT:Oe50425a960f590eded1e', 'ds:P03-029', 'B', 'term',
     '  Bossu: [抱歉，我们不能冒险让你传送到实心地表里，何况你还是我们仅存的希望。]',
     '「实心地表」在两版间摇摆（另见「传进实体里」）；本行保留多数版用法，只删「唯一的」与「仅存」的同义堆叠。'),
    ('SFWfc559e66b4dabf26ba221dd8', 'R9M-305', 'B', 'term',
     '  Bossu: [抱歉，我们不能冒险让你传送到实心地表里，何况你还是我们仅存的希望。]',
     'SFW 男线同句同改，保持与 NSFW 一致。'),
    ('CAT:Oa3ec12f202e77e320ba6', 'ds:P03-026', 'B', 'format',
     '  Bossu: [干得好，特工，你该为自己骄傲！]',
     '句末缺标点；同场其他感叹句都用「！」，此处按语气补感叹号而非句号。'),
    ('CAT:Ocda83356b46fcd58e4fb', 'R9M-306', 'B', 'format',
     '  Bossu: [干得好，特工，你该为自己骄傲！]',
     '女线同句同改。'),
    ('CAT:O31052ad862684434c0fe', 'ds:P03-015', 'B', 'term',
     '  Yiffany: [哈哈，那当然！通话完毕，通话结束。]',
     '原文 OVER AND OUT 是两个收线词连用；现译只留「通话结束」丢一层，改成两个都说。'),
    ('SFW6a5d562adaa4c8f78930364c', 'R9M-307', 'B', 'term',
     '  Yiffany: [哈哈，那当然！通话完毕，通话结束。]',
     'SFW 女线同句同改。'),
    ('CAT:Of0aa61857047c59585d7', 'gemini:P03-016', 'B', 'term',
     '  Yiffai: [明白了。伊吠通话完毕！]',
     '本作主角报尾以「通话完毕」为主（33 处），「结束通话」仅 4 处；行尾还留着一个半角空格。同时收掉行尾空格。'),
    ('SFW10d37e708bc1861e9cb97381', 'R9M-308', 'B', 'term',
     '  Yiffai: [明白了。伊吠通话完毕！]',
     'SFW 男线同句同改，并收掉行尾空格。'),
    ('CAT:O20555292d580fdb20496', 'R9M-309', 'B', 'term',
     '  Yiffany: [好啦好啦，行——！伊吠妮通话完毕！]',
     '同一场景另一行的「结束通话」与全库主用法不一，一并归位。'),
    ('CAT:O6d5345f204ca314d9fa7', 'ds:P03-035', 'C', 'format',
     '  Bossu: [我们总算把维修工作外包给了当地的一个犬科，它不介意用 LECT 结算报酬。]',
     'LECT 与本作其他货币名（Lect／信用点）并列时两侧留半角空格；只动排版，金额与结算方式不变。'),
    ('CAT:O14fc544563ff2640ae12', 'R9M-311', 'C', 'format',
     '  Bossu: [我们总算把维修工作外包给了当地的一个犬科，它不介意用 LECT 结算报酬。]',
     '男线同句同改，两版排版一致。'),
    ('CAT:Oc3d736938ce9949f1320', 'ds:P03-021', 'B', 'term',
     '  Yiffai: [黏糊……？]',
     '男线本行上一行已是「咕噜。咕叽。」，本行再写「咕叽」就同词重复；女线同位作「黏糊」，两边统一到「黏糊」，也让拟声与感叹分层。'),
    ('CAT:O4ded814da2349897ea9b', 'ds:P03-024', 'B', 'continuity',
     '  Bossu: [是谁？立刻表明身份！]',
     'WHO IS THIS 在本批有四种写法（谁在说话／这是谁／你是谁）；这三处是同一类无线电应答，统一成同一句。'),
    ('CAT:O515a967befb33dbac36c', 'R9M-312', 'B', 'continuity',
     '  Bossu: [是谁？立刻表明身份！]',
     'Feral 男线同句同改。'),
    ('CAT:Obbab98e0426919542b97', 'R9M-313', 'B', 'continuity',
     '  Bossu: [是谁？立刻表明身份！]',
     'Slime 男线同句同改。'),
    ('CAT:Obab3ebaa86f955410de1', 'R9M-314', 'B', 'continuity',
     '  Bossu: [是谁？立刻表明身份！]',
     'Slime 女线同句同改。'),
    ('CAT:O5e6ecefda5125c3d1b0d', 'R9M-315', 'B', 'continuity',
     '  Bossu: [是谁？]',
     'Kobo 场只有一句 WHO IS THIS，保持同口径但不加后半句（原文确实只有一句）。'),
]

REJECT = [
    ('ds:P03-002', 'A', 'meaning', 'SC1ac13281cd0015e4', 'CAT:O389c17fd2594fa89c4b7',
     'COMMANDEER THEIR RADIO 的 THEIR 是复数泛指，波苏此时已喊出「特工伊吠妮」，中文写「他们的」并无歧义，改成「她的」是把推断写实；保留原译。'),
    ('ds:P03-003', 'A', 'meaning', 'SC472e7b3d8ffa443a', 'SFWea0b5d5779c0924002d7613',
     'THEY 在 SFW 版指前一句的被救者单个；改「对方」会与该段已出现的「救出了对方」重复堆叠，收益不足，保留原译。'),
    ('ds:P03-010', 'B', 'idiom', 'SC127cc528b609c1cf', 'SFW89aa149fad8028feb7a3b6b9',
     'HOLD YOUR OWN 译「撑住场面」在本句可读，改成「顶住了」只是同义替换；两版一致，不改。'),
    ('ds:P03-019', 'B', 'idiom', 'SC0cf0a0ca5caff10d', 'CAT:O98a4f6cbcabfcff2e823',
     'FAUNA MAGIC 现译「和动物打交道的拿手本事」与本场其余台词语域一致；「动物魔法」会引入原文没有的奇幻感，驳回。'),
    ('gemini:P03-001', 'A', 'meaning', 'SCfc3fa29ba595ed81', 'CAT:Oe1a023ea3f4c5e26556c',
     '女线 GOOP 现译「黏糊」与上一行 GLUG/GLOOP 的「咕噜。咕叽。」不撞词；改成「咕叽」会与紧邻上一行重复。同批男线那一处才是撞词的一方，方向相反，故驳回本条的改法。'),
]

HOLD = [
    ('R9M-316', 'B', 'continuity', 'SC1ac13281cd0015e4', 'CAT:O5e6ecefda5125c3d1b0d',
     '本批 WHO IS THIS 有五处四种写法，其中两处（本行「这是谁？」与 KoboPickup 的「你是谁？」）原文只有一句、没有「立刻表明身份」后半句。是否把这一句也补足成统一句式涉及改写源句信息量，留待与「无线电应答套语」的全局口径一并定。'),
    ('R9M-317', 'B', 'format', 'SC5d1f63ab15b52fb9', 'SFWc00f5f149929e58137123612',
     '本行与下一行「其他特工来说也是个好兆头。」构成跨行合句；两版断行位置不同（女线已并作一行）。合并或保留需与字体折行一并决定，本批不动。'),
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
        if not row['current'] or not new:
            raise SystemExit('blank line target ' + rid)
        lines.append('\t'.join((fid, fid.split(':')[0], sev, cat, scene_id, rid, 'apply', new, reason)))
    for fid, sev, cat, scene_id, rid, reason in REJECT:
        lines.append('\t'.join((fid, fid.split(':')[0], sev, cat, scene_id, rid, 'reject', '', reason)))
    for fid, sev, cat, scene_id, rid, reason in HOLD:
        lines.append('\t'.join((fid, 'main', sev, cat, scene_id, rid, 'hold', '', reason)))
    out = BASE / 'review/decisions.tsv'
    out.write_text('\n'.join(lines) + '\n', encoding='utf8')
    print(json.dumps({'decisions': len(lines) - 1, 'apply': len(APPLY),
                      'reject': len(REJECT), 'hold': len(HOLD)}, ensure_ascii=False))


if __name__ == '__main__':
    main()
