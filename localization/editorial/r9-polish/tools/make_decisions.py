"""Write the r9 batch-01 decision table from reviewed choices.

Each entry is a main-agent ruling on one or both routes' findings, or on a
main-agent finding discovered while cross-checking. The scene id is resolved from
the order, unknown row ids fail loudly.
"""
from pathlib import Path
import json

ROOT = Path(__file__).resolve().parents[4]
BASE = ROOT / 'localization/editorial/r9-polish/batch-01'
ORDER = json.loads((BASE / 'orders/batch-01.json').read_text('utf8'))
ROWS = {r['row_id']: (s['scene_id'], r) for s in ORDER['scenes'] for r in s['rows']}

APPLY = [
    # row_id, finding_id, severity, category, new line, reason
    ('CAT:O44059f129ac9b6ad4ee0', 'gemini:P01-001', 'B', 'term',
     '  * 要是在外面找到无线电，记住：在物品菜单里按SELECT就能使用它！',
     'radio 在本作是无线电教学的核心设备，女线误作「收音机」且同句重复两次；男线同文已作「无线电…使用它」，统一后两版一致。'),
    ('CAT:Odd9c1febae40a1891df4', 'gemini:P01-002', 'B', 'idiom',
     '  * 这石头便宜点卖给你！',
     'I\'ll let you have it for a good price 是让买方占便宜的口气；「按好价钱把它让给你」把让利方向读成卖方定价，像物资调拨。女线 nsfw 同场已是「这石头便宜点卖给你！」，三处同文统一。'),
    ('SFW29e9055d0639a2d407f39c1d', 'gemini:P01-003', 'B', 'idiom',
     '  * 这石头便宜点卖给你！',
     '同上，datadm sfw 版同句同病，与男女线 nsfw 统一。'),
    ('SFW7e7cb8e176543dd2ded24acf', 'gemini:P01-004', 'B', 'idiom',
     '  * 这石头便宜点卖给你！',
     '同上，datadf sfw 版同句同病。'),
    ('SFW1c5fdba33d4cbabd67498b0b', 'ds:P01-005', 'B', 'voice',
     '  * 你、你是条好狗，对吧？',
     '英文 NICE DOG 与下一行 GOOD BOY 是两步试探，现译两行都写「乖狗狗」把两步压成一句；男线 nsfw 同段已作「好狗」，sfw 对齐。'),
    ('SFW262bf54487e808f6dec93610', 'R9M-001', 'B', 'voice',
     '  * 你、你是条好狗，对吧？',
     '与男线 sfw 同句同改；女线此句为 NICE DOG，下一行才是 GOOD GIRL，重复度不同但用词仍应分开。'),
    ('CAT:O3d8412cae97cbaf45f3b', 'gemini:P01-005', 'B', 'relationship',
     '  * 乖狗狗！带上你的主人再回来吧！',
     '主角处于犬形态且被误认为宠物狗，GOOD BOY 是对狗的夸赞；「好小子」是对少年的称呼，与「你的主人」搭配突兀。女线同场作「好姑娘！」。'),
    ('CAT:O45c65d8356906bf52d1d', 'ds:P01-006', 'B', 'term',
     '  Mauser: [你进入了一片旧矿井的竖井网。小心点！]',
     'OLD MINE SHAFTS 指竖直井筒网络；「废弃矿道」既丢 network 又把竖井写成横向巷道。同 root 其余行与女线都用「竖井」。'),
    ('CAT:Oa205ce8bc123b48eabed', 'ds:P01-007', 'B', 'term',
     '  Mauser: [你进入了旧矿井的竖井网。小心！]',
     '同句女线原译「巷道网」，与男线同句同一结构问题；统一为「竖井网」并保留原有的「旧」与感叹号。'),
    ('CAT:O7f7cb9d899c5e25ff614', 'ds:P01-008', 'B', 'term',
     '  Mauser: [地底那么深，很难扫描清楚。不过，我在矿井更深处探测到了几道安保门的信号。你的新门卡应该能让你通过。]',
     'SECURITY DOOR 在本批男线同句、以及门卡语境下作「安保门」；「安全门」在中文里指逃生门，与凭门卡刷入的保安装置不是一回事。'),
    ('CAT:Ode233c9a85316eb262e6', 'ds:P01-009', 'B', 'term',
     '      Mauser: [我已规划好通往地表的路线。那是矿坑最西北角的一条出入竖井。]',
     'ACCESS SHAFT 是矿区通往地表的井；女线同句已作「出入竖井」，「通道竖井」不是既有说法。'),
    ('CAT:O127ed134323b54dcb0b9', 'ds:P01-011', 'B', 'idiom',
     '      Mauser: [有了那只反重力踝环，你应该就能更轻松地穿越竖井，往矿井更深处探索了。]',
     'SHOULD BE ABLE…THAT SHOULD ALLOW 被逐词搬成两个「应该」，读成两次猜测；合并成一句因果，保留 should 的一次建议语气，不把「应该能」升成「一定能」。'),
    ('CAT:Oa360d276310a49fc658a', 'ds:P01-010', 'B', 'idiom',
     '      Mauser: [有了那只反重力踝环，你应该就能更轻松地穿越竖井，往矿井更深处探索了。]',
     '男线同句同病，且「矿洞」与同 root 其余行的「矿井」不一；只并句并归位术语，踝环与探索范围的玩法含义不动。'),
    ('CAT:O102345c815895245984a', 'gemini:P01-007', 'B', 'continuity',
     '    Mauser: [哎呀，伊吠妮，你跑回那片区域干嘛呀？]',
     '本场触发条件是已进过 C 区又折回 A 区，毛鼠问的是「你怎么又回来了」；现译「那片区域那边怎么了」把疑问落到那块的变故上，与后句「用传送门去别的区域不是更有意思吗」接不上。合并两路：取女线口语度与男线问法，避免 DS 稿「你回的那片区域怎么了」仍把焦点放回区域状况。'),
    ('CAT:O8f9c5f4bfa42286c1d0c', 'ds:P01-013', 'B', 'term',
     '  Mauser: [就在刚才，我们开始记录到矿井东北区域出现的奇怪能量波动。]',
     '同 root 的 OpenMode／End／DragonHint 都作「矿井」，此处「矿洞」成了同一区域的第二个地名；只换这一个词。'),
    ('CAT:O7472968809e55be5b8fb', 'ds:P01-014', 'B', 'idiom',
     '  Mauser: [那些矿井里地震活动频繁，其中多数来自北面的几个区段。]',
     '一句两个「很多」，后一个还接「扇区」；SECTORS 在矿区语境是分区（全库另有「东部区段」），「扇区」是磁盘／雷达用词。保留活动多、多来自北面的事实。'),
    ('CAT:Oabd53fe8c10770b1d1d5', 'ds:P01-015', 'B', 'term',
     '  The0: [哦嗨呀小家伙！是我啦，你友好的小黑客狗。这不，我就想来你这小小的一次性密码本加密频道里露个脸！]',
     '同一场景后文 The0 就是拿「一次性密码本」抖机灵（重复使用表块还能叫 one time pad 吗），女线两版此处均已作「一次性密码本加密频道」；男线「OTP 密码加密频道」既有异常空格，又让后文双关落空。'),
    ('SFWe5978597692502a06b0635b3', 'gemini:P01-009', 'B', 'term',
     '  The0: [哦嗨呀小家伙！是我啦，你友好的小黑客狗。这不，我就想来你这小小的一次性密码本加密频道里露个脸！]',
     '男线 sfw 同句同改，与同一路线的 nsfw 及女线两版一致。'),
    ('CAT:O6eac5c6a11937f84f9e9', 'ds:P01-016', 'B', 'format',
     '  The0: [你就叫我“The0”吧！想着来帮帮你，告诉你一个区域里还剩多少芯片。]',
     '半角直引号在 12px 中文行里露出等宽空隙；女线两版同位都用「“The0”」。The0 仍保留英文写法。'),
    ('SFWe036d684df4d0d260df25273', 'R9M-002', 'B', 'format',
     '  The0: [你就叫我“The0”吧！想着来帮帮你，告诉你一个区域里还剩多少芯片。]',
     '男线 sfw 同句同改，与女线及本路线 nsfw 一致。'),
    ('CAT:O52f7bd5e6d8c15c879ba', 'ds:P01-017', 'B', 'idiom',
     '  The0: [好吧，哇，还真蒙对了……]',
     '「真是运气好猜中了」把 lucky + guess 按英语语序直搬，缺结果连接；「还真蒙对了」接得上随后「可我……正忙着」的心虚收线。'),
    ('CAT:Oe5f5fb755e70d20e5527', 'ds:P01-018', 'C', 'format',
     '  The0: [好吧，哇，这猜得也太准了……]',
     '三个语气词连写「好吧哇」在屏幕上像错字；男线同位已有逗号，只补一个停顿标记。'),
    ('CAT:Oe31d0e581612b4958fcc', 'ds:P01-019', 'B', 'idiom',
     '  The0: [总之，祝黑客——我是说，狩猎愉快！]',
     'HAPPY HACK- 说到一半改口，现译「祝你黑-客快乐」把双字词硬拆开，屏幕上只剩孤立半角连字符，改口笑点失效；女线两版通道已是「祝黑客——我是说，狩猎愉快！」，三处统一。'),
    ('CAT:O3273e9deef4b5665f247', 'gemini:P01-011', 'B', 'format',
     '  The0: [总之，祝黑客——我是说，狩猎愉快！]',
     '同上，datadm 的 GenderSwapped 版同句同改。'),
    ('CAT:Oe35e41270c0fbae9489c', 'gemini:P01-012', 'B', 'format',
     '  The0: [总之，祝黑客——我是说，狩猎愉快！]',
     '同上，datadm 的 Kobo 版同句同改。'),
    ('CAT:Oa619000ee6e9a6568c34', 'ds:P01-020', 'C', 'idiom',
     '  The0: [小狗会刨坑吧？总之，让我看看。扫描中……]',
     '「总之，看看」缺 LET\'S SEE 的主语，读起来像让读者自己看；女线同句作「总之，让我看看」。'),
    ('CAT:O16943a493b2a822eac75', 'gemini:P01-016', 'B', 'format',
     '  The0: [那是——算了，晚点再打给我吧！好，再见！]',
     'THAT\'S- 被打断，现译「那- 算了」用半角连字符加空格，屏幕上成孤立短横；女线同句作「那是——听着」，统一改用全角破折号。'),
    ('CAT:O73c68400be6f22df5289', 'gemini:P01-014', 'B', 'format',
     '  The0: [什、什么？不可能！我的扫描程序是——]',
     '行尾 ASCII 连字符在文本框里显示为孤立半角减号，与同场其它破折号打断写法不统一；语声骤止的意思不变。'),
    ('CAT:O977f2bb4dc4d4e0704e6', 'gemini:P01-015', 'B', 'format',
     '  The0: [什、什么？不可能！我的扫描程序是——]',
     '男线同句同改，两版一致。'),
    ('CAT:Occ4fa40dc5b2b1c83dfe', 'ds:P01-004', 'C', 'format',
     '  * ……SXUXYGAX……',
     '同场另两行都用「……」，只有代码行是半角三点；女线同句已统一。代码本身 SXUXYGAX 与「* 」前缀原样保留。'),
    ('CAT:O383a6c3da53e7b1875f8', 'gemini:P01-013', 'B', 'meaning',
     '  The0: [哦嘿，黏黏！身上粘着芯片吗？]',
     'GOT ANY CHIPS STUCK TO YOU 是「有芯片粘在你身上」，现译「身上有芯片粘着你」把芯片写成主动粘人的活物；女线同句已作「身上粘着芯片吗」。'),
    ('CAT:Of8eca47c17aabf1269ff', 'gemini:P01-017', 'C', 'voice',
     '  The0: [嗨呀科博！你有点吓人，不过你有芯片吗？]',
     '「可有芯片吗」略带古风／方言，The0 是轻快技术宅；女线同位作「不过你有芯片吗」。只换连接词，逗号与称呼不动。'),
]

REJECT = [
    ('ds:P01-003', 'C', 'idiom', 'SC1d1158bdbf9ad2d5', 'CAT:O0eda9438152bf41cf111',
     '「捅出大窟窿」与男线「彻底崩掉」都通顺，元笑点是调试码真把游戏弄崩；C 级统一收益小于改动风险，保留两版各自口吻。'),
    ('ds:P01-021', 'B', 'voice', 'SC11014e83b9fc86dd', 'CAT:O199371b34daed6215054',
     '「黏黏」作为当下形态的临时称呼两版一致，读者不易误当固定名；改为「黏糊糊的小家伙」使该行加长约 60px（12px 实测折行仍在 3 行内），收益不及行宽与节奏代价，保留原译。'),
]

HOLD = [
    ('R9M-003', 'C', 'format', 'SC6e55efe5652d83ff', 'CAT:Of36a02113d3dcec54dec',
     '同一频率 28.250 在四版里写作「在 28.250 呼我」「打 28.250 给我」「打28.250联系我」「打 28.250 找我」，数字两侧空格不统一。属全库排版口径问题，不宜在本批只改一处，待统一规则后另行处理。'),
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
