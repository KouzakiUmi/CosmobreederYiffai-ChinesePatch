"""Write the r9 batch-04 decision table.

Every row id below was read back from the batch order, not typed from memory:
a wrong id would silently bind a repair to the wrong physical line.
"""
from pathlib import Path
import json

ROOT = Path(__file__).resolve().parents[4]
BASE = ROOT / 'localization/editorial/r9-polish/batch-04'
ORDER = json.loads((BASE / 'orders/batch-04.json').read_text('utf8'))
ROWS = {r['row_id']: (s['scene_id'], r) for s in ORDER['scenes'] for r in s['rows']}

# Row ids resolved by searching the order for the current text, then verified.
APPLY = [
    # —— A：地名分裂
    ('CAT:O552d526566426cfb09a7', 'ds:P04-001', 'A', 'term',
     '  Mauser: [你已经进入艾斯卡姆尔！矮人的家园！]',
     'AYSKAMMR 在导航图、图鉴卡、麦森台词与同 root 另一份拷贝里都作「艾斯卡姆尔」，只有这行写成「艾斯坎默」。同一地区不能两个名字。'),
    # —— A：无线电收线被译成离场
    ('CAT:O0c4ed02a9a1bf4c8922c', 'ds:P04-002', 'A', 'meaning',
     '  Yiffai: 我……我很抱歉……伊、伊吠……完毕！',
     'Y-YIFFAI OUT! 是无线电断线；「先走了」把收线写成离场动作，人并没有走。batch-03 已把另两场同句改成「通话完毕」，此处按同一口径收线。'),
    # —— A：句子不成立
    ('SFWce6e6170cacb490fc0ff0ebd', 'ds:P04-003', 'A', 'format',
     '  Bossu: [我们不能冒险让你再次被击落……或者更糟。]',
     '「甚至出更糟的事」缺谓语，读不成句；OR WORSE 是并列的「或者更糟」。风险判断与「再次被击落」的条件不动。'),
    # —— A：按键名被汉化
    ('CAT:O5e4eb683155190dd7050', 'gemini:P04-005', 'A', 'gameplay',
     '  Yiffany: [说什么要"SELECT"波形，然后再用“UP & ATTACK”发动能力，好把障碍物挪开……]',
     '原文是 UP & ATTACK 键名，现译「UP & 攻击」把键名一半汉化；只还原键名，句意与省略号不动。'),
    ('CAT:O40193b545ac070b573e2', 'gemini:P04-006', 'A', 'gameplay',
     '  Yiffany: [它在说：“按 SELECT 选择你的超能力，然后同时按下 UP+ATTACK，激活你选定的能力！”]',
     '同一组教学里另一处键名也统一；这句是「声音」的指令转述，键名必须与实际按键一致。'),
    # —— A：源码残留双引号
    ('CAT:Of5810f2e97164e8b7a18', 'gemini:P04-011', 'A', 'format',
     '  Yiffai: [呃——，这个嘛……]',
     '源文以 `..."]` 结尾（作者引号未闭合），现译照抄留下孤立右引号；只删这个残留，不改措辞。'),
    ('SFW3d32f8a28c3f230c479e5517', 'gemini:P04-012', 'A', 'format',
     '  Yiffai: [呃——，这个嘛……]',
     '女 SFW 同文同句，一并删掉残留右引号。'),
    # —— 术语：干员 → 特工
    ('CAT:Of3b574a35d8096437f00', 'gemini:P04-001', 'B', 'term',
     '  Mauser: [……呼叫特工伊吠！请回答！]',
     '全库 agent 处 431 处作「特工」，「干员」仅 12 处散见；R2 已明确不把现用「特工」批量改掉。本批 4 处「干员」是少数派，归位到「特工」。'),
    ('SFWaa18c075537d157fccf4f83f', 'gemini:P04-002', 'B', 'term',
     '  Mauser: [……呼叫特工伊吠！请回答！]',
     '男线 SFW 同句同改，与 NSFW 一致。'),
    # —— 术语：电台 → 无线电
    ('CAT:O3e5e25ee5a75819994b1', 'gemini:P04-008', 'B', 'term',
     '  Mauser: [……如果你还挥着台 PPP 无线电到处叫人，我不觉得这套伪装会有多好用。]',
     '本作通讯设备全库 42 处作「无线电」，只有本批这两处写「电台」；只换名词并补间隔。'),
    ('CAT:Oa7308118fad528f5f568', 'gemini:P04-009', 'B', 'term',
     '  Mauser: [……你挥着台 PPP 无线电到处叫人，不觉得这样可能会暴露身份吗？]',
     '另一份拷贝同改，两版措辞保持一致。'),
    # —— 口吻：不把 liaison 说成官职
    ('CAT:O2e9427e1ca032962fa33', 'gemini:P04-003', 'B', 'voice',
     '  Mauser: [别在意！我是你这次出击的主要联络人]',
     '「主联络官」把 liaison 职责说成军衔／官职，参照明确规定不作军衔；同 root 另一份拷贝已作「主要联络员」。'),
    # —— 口吻：损友调侃不萌化
    ('CAT:Occ36c36d2b0aa020f33a', 'gemini:P04-007', 'B', 'relationship',
     '  Tomcat: [行吧姑娘，你去找几块老旧易碎的砖块，试试那条反重力裙子，这边这只快晕过去的老鼠就交给我吧。]',
     '「鼠鼠」把损友外号读成网络萌化叠词，参照明确禁止；Tomcat 是在挖苦同事，用「老鼠」保持调侃力度。'),
    # —— 口吻：呼叫而非拨号
    ('CAT:O465792bc2c9866c8797b', 'gemini:P04-010', 'B', 'voice',
     '  Mauser: [你该呼叫雄猫！她才是装备专家。]',
     '原文是建议对方去联络装备专家；「该打给」像座机拨号。补主语并用通讯语境动词。'),
    # —— 习语：big boy pants
    ('CAT:Obfbe9a4bdd9340fca56d', 'gemini:P04-017', 'B', 'idiom',
     '  Tomcat: [就是啊，小狗崽，拿出大人样穿上裤子，稳着点来。]',
     'put on your big boy pants 是「拿出大人样」，现译「穿大人的裤子」把比喻说成动作；调整后仍接得住后文丢裤子的笑点。'),
    # —— 术语：仓储站 → 仓库（全库 49 处作仓库，仅此 1 处作仓储站）
    ('CAT:O221a9c23356a19a9799e', 'ds:P04-008', 'B', 'term',
     '  Mauser: [报告显示，这里曾经有许多仓库，但如今只剩这一个了。]',
     'DEPOT 在全库 49 处作「仓库」，此处「仓储站」是唯一异写；只换名词，数量与位置不动。'),
    # —— 术语：COSMO 套件 → 宇宙套件（与 Cosmobreeder 系列构词一致）
    ('CAT:O9a641edef3adc4f62a71', 'ds:P04-010', 'B', 'term',
     '  Mauser: [你没带吗？每个标准宇宙套件里都有一把铲子！]',
     'COSMO KIT 是标准装备名，全库其余语料作「宇宙服／宇宙靴／宇宙盔」同一构词；「COSMO套件」把半截英文留在句中。'),
    # —— 口吻：不把卡壳切在词中间
    ('CAT:O93fa12dc32fc9eb16c0d', 'ds:P04-021', 'B', 'voice',
     '  Mauser: [什、什么？你这话什么意思……？]',
     '「意、意思」把卡壳切在词中间，读起来像错字；原文卡壳在句首 W-WHAT，句尾不再重复卡壳。'),
    # —— 语气：敷衍的重心
    ('CAT:O33729688ce4ddcf7c35b', 'ds:P04-019', 'B', 'voice',
     '  Mauser: [什、什么？可我的研究写着……]',
     '「明明写着」多了一层争辩语气；原文是愣住后拿资料反驳，保留卡壳与省略号，去掉额外强调词。'),
]

REJECT = [
    # 参照摘录写错导致的整组提案：「脚环」才是道具名与多数写法
    ('gemini:P04-013', 'B', 'term', 'SC2bb5df69804fef2f', 'CAT:O73fda3f8e160fd4f32a6',
     '两路都主张把「反重力脚环」改「反重力踝环」，依据是我在参照摘录里把 anti-grav anklet 写成「踝环」。核对后：UI 道具名就是「脚环」，正文 7 处「反重力脚环」+12 处「脚环」，「踝环」只有 5 处——多数派是「脚环」。已修正参照摘录，此处驳回。'),
    ('gemini:P04-014', 'B', 'term', 'SCb714b8ec1b957c4e', 'CAT:Ob9524d26104bc0456aae',
     '同上，方向相反，驳回。'),
    ('gemini:P04-015', 'B', 'term', 'SC581aac8836b915da', 'SFW2fb5fe9d099481d20c013deb',
     '同上，方向相反，驳回。'),
    ('gemini:P04-016', 'B', 'term', 'SC568f82ccb29b4fa0', 'SFW613c659a0ca5ce2d987283b7',
     '同上，方向相反，驳回。'),
    ('ds:P04-005', 'B', 'term', 'SC2bb5df69804fef2f', 'CAT:O73fda3f8e160fd4f32a6',
     '同 gemini:P04-013，驳回。'),
    ('ds:P04-006', 'B', 'term', 'SC701bdd2f929e1031', 'CAT:O2e9427e1ca032962fa33',
     '本行已在 gemini:P04-003 按「联络人」处理；DS 的方向一致，重复条目不另立。'),
    ('ds:P04-007', 'B', 'term', 'SC55c4a209986bb4f7', 'CAT:O2c7062e3dd39a403386a',
     '「芝士球」与另一处的「小奶酪球」是同一外号 CHEESEBALL 的两种叫法；改成「奶酪球」只是把其中一处换掉，仍会两存。外号属称呼口径，不单点改。'),
    ('ds:P04-009', 'B', 'term', 'SCe5d8ed9267f0f4c4c7a5e', 'CAT:Oa6cc1ec27c9bc959d259',
     '「通话结束」与「通话完毕」在全库本来就是多数并存（33 对 17）；本行不改，避免在单批制造新的不一致。'),
    ('ds:P04-011', 'B', 'voice', 'SC55c4a209986bb4f7', 'CAT:Occ36c36d2b0aa020f33a',
     '与 gemini:P04-007 同位置；已采纳 gemini 的改法，不重复计数。'),
    ('ds:P04-013', 'B', 'relationship', 'SC55c4a209986bb4f7', 'CAT:Oc4410cc1434bfd3877c8',
     '「狗狗翘臀」比原文多出性化成分，但这是全库尺度问题，且该行本身是 Tomcat 的荤玩笑；不在单批收紧。'),
    ('ds:P04-014', 'B', 'relationship', 'SCb6a7d5d9e0c1f2a3b4c5d', 'CAT:O3afdccc791e26827d676',
     'DEAR 译「亲爱的」被读成恋人关系。该词更像老派招呼，但改成别的说法会牵动多处同类招呼，留待称呼口径一并定。'),
    ('ds:P04-020', 'B', 'voice', 'SC8bbefad7d6e7d322', 'CAT:Of3d8eac24c3a65588c13',
     '女线用半角连字符写结巴（不-不是）与全批顿号写法冲突。统一会牵动全库所有结巴行，须先定「卡壳标记」口径；本批不动。'),
    ('ds:P04-027', 'B', 'gameplay', 'SCc84763bc1dd8de7b', 'CAT:O40193b545ac070b573e2',
     '与 gemini:P04-006 同位置；已作为 A 级采纳，不重复计数。'),
    ('ds:P04-028', 'B', 'format', 'SC8bbefad7d6e7d322', 'CAT:O5e4eb683155190dd7050',
     '与 gemini:P04-005 同位置；已作为 A 级采纳，不重复计数。'),
]

HOLD = [
    ('ds:P04-015', 'B', 'continuity', 'SC0b2a2d5c9e9c6c62', 'CAT:O55b7df2f3a0708d891e3',
     '「我是唯一在活动的特工？」与 Bossu 后面「仅存的希望」口径相关，但涉及主线叙事信息量，需对照后段剧情确认后再动。'),
    ('ds:P04-029', 'B', 'format', 'SC9db33b8f4dd22532', 'CAT:O24f651d1e290f8fd0b56',
     '本行句末缺标点，但同场后续行是合句尾行；补标点会改变合句节奏，留待与合句策略一并处理。'),
    ('ds:P04-033', 'C', 'voice', 'SCb6a7d5d9e0c1f2a3b4c5d', 'SFWb7fcbdd38e27e729f16b0169',
     '「付赌钱」疑为「付赌注／押注」之误，但这句赌约本身是玩笑，语义把握不足，登记待原文语境复核。'),
    ('ds:P04-037', 'C', 'format', 'SCb6a7d5d9e0c1f2a3b4c5d', 'CAT:Odadb5aa2cc23c4df71ad',
     '「Fenfen」保留英文是否合适属专名口径问题（R3 未裁该名），不在本批单独改。'),
    ('ds:P04-030', 'needs_evidence', 'source_uncertainty', 'SCb6a7d5d9e0c1f2a3b4c5d', 'SFW5f8a5ceb0952154ab8c78294',
     '失真台词在四场里被处理成三种（保留英文残片／译成可读中文／纯拟声）；这是失真字幕的全局口径问题，本批登记不改。'),
    ('ds:P04-031', 'needs_evidence', 'source_uncertainty', 'SCb6a7d5d9e0c1f2a3b4c5d', 'CAT:Ob2ac12ffcf46943bf3fa',
     '原文 `MAUSER ORDERS IN... WHAT?` 本身不成句，且男线缺该行；结构对不齐，须先确认残句性质。'),
    ('gemini:P04-018', 'needs_evidence', 'source_uncertainty', 'SC0b2a2d5c9e9c6c62', 'CAT:O139baccbe4571e62632d',
     '原文 `H-HUH? WHO\'S THIS? YIFFAI?!` 是作者把男线脚本复制到女线留下的笔误（女线是伊吠妮在说话）。这是源文本缺陷，中文照原文写「伊吠？！」不算错译；不按提案改成「伊吠妮」。'),
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
        if row['current'] == new:
            raise SystemExit('no-op ' + rid)
        lines.append('\t'.join((fid, fid.split(':')[0], sev, cat, scene_id, rid, 'apply', new, reason)))
    for fid, sev, cat, scene_id, rid, reason in REJECT:
        lines.append('\t'.join((fid, fid.split(':')[0], sev, cat, scene_id, rid, 'reject', '', reason)))
    for fid, sev, cat, scene_id, rid, reason in HOLD:
        lines.append('\t'.join((fid, fid.split(':')[0], sev, cat, scene_id, rid, 'hold', '', reason)))
    (BASE / 'review/decisions.tsv').write_text('\n'.join(lines) + '\n', encoding='utf8')
    print(json.dumps({'decisions': len(lines) - 1, 'apply': len(APPLY),
                      'reject': len(REJECT), 'hold': len(HOLD)}, ensure_ascii=False))


if __name__ == '__main__':
    main()
