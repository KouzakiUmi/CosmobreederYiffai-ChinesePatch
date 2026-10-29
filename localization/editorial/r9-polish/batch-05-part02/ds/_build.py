# -*- coding: utf-8 -*-
"""Build ds/findings.jsonl + ds/coverage.jsonl for batch-05-part02, with checks."""
import importlib.util
import json
import re
from collections import Counter

BASE = 'localization/editorial/r9-polish/batch-05-part02'
OUT = BASE + '/ds'
spec = importlib.util.spec_from_file_location('pl', 'localization/tools/preview-layout.py')
pl = importlib.util.module_from_spec(spec)
spec.loader.exec_module(pl)
HEAD, CHARS, _ = pl.load_font('localization/runtime/bbc2-12px.fnt',
                             'localization/runtime/bbc2-cjk-12.png')

PREFIX = re.compile(r'^(\s*(?:\*\s?)?(?:[^<>{}#*\s][^:]{0,40}:)?\s?)')


def wraps(text, box):
    return len(pl.layout(text, CHARS, box))


def missing(text):
    return sorted({c for c in text if ord(c) not in CHARS})


order = json.load(open(BASE + '/orders/batch-05-part02.json', encoding='utf-8'))
rows = {r['row_id']: (s['scene_id'], r) for s in order['scenes'] for r in s['rows']}
scene_rows = {s['scene_id']: [r['row_id'] for r in s['rows']] for s in order['scenes']}

F = []


def cur_of(rid):
    return rows[rid][1]['current']


def add(n, rid_list, sev, cat, src, prop, reason, refs, status='proposal', note=''):
    sid = rows[rid_list[0]][0]
    F.append({
        'finding_id': 'P05b-%03d' % n,
        'scene_id': sid,
        'row_ids': rid_list,
        'severity': sev,
        'category': cat,
        'source_quote': src,
        'current_quote': cur_of(rid_list[0]),
        'proposed_zh': prop,
        'reason': reason,
        'reference_keys': refs,
        'status': status,
        'note': note,
    })


def tail(prop):
    return '实测 240px／224px 折行 %d／%d。' % (wraps(prop, 240), wraps(prop, 224))


DICT = '§四.11 出处：datav/dictionary.json 条目'

# --- 101 Bullfrog over-limit -------------------------------------------------
add(101, ['CAT:Od65baabc30d343ed6f34'], 'B', 'format',
    '[THERE ARE REPORTS THAT A "HOPPER" THAT ABSORBS ENOUGH] / '
    '[PSYCHIC ENERGY WILL TURN INTO A "BULLFROG"] / '
    '[CAPABLE OF SHOOTING BUBBLES AT TARGETS FROM AFAR OR EVEN] / '
    '[DEALING DAMAGE WITH THEIR NEW, ELONGATED TONGUE.]',
    '  Bossu: [有报道称，「跳跃者」吸够灵能就会变成「牛蛙」，能从远处朝目标喷吐泡泡，还会用新长出的修长舌头造成伤害。]',
    '§四之二指定行：240px 下已折成 4 行，超出每页 3 行。四句英文被并进一条物理行，必须压回 3 行且不得丢条件。'
    '只删冗余虚词（「只要吸收了足够的」→「吸够」、「甚至还能用」→「还会用」），'
    '「有报道称」这一情报来源限定词、「跳跃者」「牛蛙」两个已定术语、喷吐泡泡与舌头伤人两项能力全部保留。',
    ['§四之二', 'Bossu 非全知口吻（有报道称…）', DICT + ' HOPPER = 跳跃者／BULLFROG = 牛蛙'],
    note=tail('  Bossu: [有报道称，「跳跃者」吸够灵能就会变成「牛蛙」，能从远处朝目标喷吐泡泡，还会用新长出的修长舌头造成伤害。]')
    + '三句尾行 CAT:O4c25f9d49140cc183abe／CAT:O032ba0052eed4753cde8／CAT:Oce8fc0c7699db70a09bf 的 current 为空，属既有合句尾行，不单独改。')

# --- 102 Spikebot over-limit -------------------------------------------------
add(102, ['CAT:O829863279bb55814844e'], 'B', 'format',
    '[THE LITTLE WHEELED DRONES WERE ONCE USED TO FERRY] / '
    '[ORE AND TOOLS IN THE MINES, BUT THESE UNITS HAVE BEEN] / '
    '[MODDED WITH CRUDE SPIKES AND INTRUDER- SEEKING LOGIC.]',
    '  Bossu: [这些轮式小无人机曾用来运送矿井里的矿石和工具，但已被改装，加上了简陋尖刺和搜寻入侵者的逻辑。]',
    '§四之二指定行：240px 下已折成 4 行。原译把「经过了改装」拖到句末，与前半句「已被加上…逻辑」重复表达同一个 MODDED，'
    '先删重复再用「已被改装，加上了…」一次收束；「曾用来运送」「矿井里的矿石和工具」「简陋尖刺」「搜寻入侵者的逻辑」四项信息全保留。',
    ['§四之二', '术语：无人机／巷道运输（同场男线同句对照）', DICT + '（本句无物种名）'],
    note=tail('  Bossu: [这些轮式小无人机曾用来运送矿井里的矿石和工具，但已被改装，加上了简陋尖刺和搜寻入侵者的逻辑。]')
    + '男线同句 CAT:O9df35108fe2d4ae2dd0e 实测 240px 为 3 行、224px 为 4 行，未列入 §四之二，故本路不擅自改动，仅在 summary 记录。')

# --- 103 LITERALLY dropped ---------------------------------------------------
add(103, ['SFWa39a9d33f4a69ccb44eca74d'], 'B', 'meaning',
    "[THEY'RE LITERALLY IMPOSSIBLE TO DESTROY!]",
    '  Bossu: [它们从字面上说就不可能被摧毁！]',
    '下一行 Yiffany 的追问正是「字面意思？你是说……比喻而已，对吧？」，她咬的就是 LITERALLY 这个词。'
    '现译「根本就不可能被摧毁」把 LITERALLY 抹成普通语气副词，问句失去所指，「拆词抬杠」的笑点整段断掉。补回「从字面上说」，否定与可能性判断不动。',
    ['§三 第五步 倒查英文', '笑点依赖原句用词对应（LITERALLY／FIGURATIVELY）'],
    note=tail('  Bossu: [它们从字面上说就不可能被摧毁！]')
    + '紧随的 SFW9a29178f939c22ba584b7ba6「字面意思？你是说……比喻而已，对吧？」已正确，不需改动。')

# --- 104 / 105 MAY 升格为断言 ------------------------------------------------
add(104, ['CAT:Odcf4e4e895a30ca6a957'], 'B', 'meaning',
    '[THE ELVES OF SCEAFYA MAY ALL BE FEMALE]',
    '  Bossu: [斯凯菲亚的精灵也许全是雌性，却并非个个都能长生不死。]',
    '英文是 MAY ALL BE FEMALE（也许全是雌性），Bossu 依手上情报给出的推测；现译「虽说全是雌性」把推测说成既定事实，'
    '同时把转折 BUT 改成了让步。同 root 的 sfw 场 SFW3ab6eac16bdc3fa6a06204be 已译作「也许全是雌性」，本批内已有正确写法，按同一口径补回 MAY。',
    [DICT + '（ELF 无独立条目，取本批内同句对照）', '§四.11 出处：同 root 另一场 SFW3ab6eac16bdc3fa6a06204be',
     'Bossu 非全知：seems／may 不得升格为断言'],
    note=tail('  Bossu: [斯凯菲亚的精灵也许全是雌性，却并非个个都能长生不死。]')
    + '男线同句见 P05b-105（CAT:Oa299621be2e312a2d893），按 §四.10 分别处理。')

add(105, ['CAT:Oa299621be2e312a2d893'], 'B', 'meaning',
    '[THE ELVES OF SCEAFYA MAY ALL BE FEMALE]',
    '  Bossu: [斯凯菲亚的精灵也许全是雌性，却并不个个长生不老。]',
    '与 P05b-104 同因：MAY ALL BE FEMALE 被译成「虽说全是雌性」的让步断言。男线按 §四.10 独立处理，'
    '句尾「并不个个长生不老」与女线写法不同但各自成立，对齐与否不影响判点，本条只改前半句的推测语气。',
    ['§四.11 出处：同 root 另一场 SFW3ab6eac16bdc3fa6a06204be', '§四.10 男女线分别处理',
     'Bossu 非全知：may 不得升格为断言'],
    note=tail('  Bossu: [斯凯菲亚的精灵也许全是雌性，却并不个个长生不老。]') + '女线同句见 P05b-104。')

# --- 106 女线残留英文 mine ------------------------------------------------
add(106, ['CAT:O2efd47e2bce33a316b21'], 'B', 'meaning',
    '[INDEED, IT APPEARS THE MINES OF TUTONE HAVE BEEN MINED.]',
    '  Bossu: [听见了。看来图托恩的矿，都"认了主"。]',
    '女线把 mine 这个词原样留在中文句里（本行「都埋了mine」、下一行「我说的是mine炸了」），是全批唯一残留未译英文实词的对话行，'
    '玩家读到中英混排且句中不可解。R5 P08-013 已就同一段英文裁决改成「认主／炸毛」结构并在男线落地'
    '（CAT:O211d32bcfc1ea166f9a9「确实，看来图托恩的矿，都"认了主"。」、CAT:O8ffba486b4343ce835c7「认了主的东西，会自己炸毛。」），女线漏并。'
    '本行按已裁决口径补齐，双关枢纽不改。',
    ['R5 P08-013 已裁决（localization/translations/editorial-r5-creative-repairs.jsonl R5-0001～R5-0008）',
     '§四.11 出处：同 root 男线场 CAT:O211d32bcfc1ea166f9a9'],
    status='proposal',
    note=tail('  Bossu: [听见了。看来图托恩的矿，都"认了主"。]')
    + '同场第二行 CAT:O19a64d3545f4e849130e（「我说的是mine炸了。」）建议同步作 `  Bossu: [认了主的东西，会自己炸毛。]`。'
    '若主代理认定女线必须保留英文 mine 的字面双关，则本条应转 needs_evidence。')

# --- 107 SPIKERS -------------------------------------------------------------
add(107, ['CAT:Oc2b7948077102e9eef2f'], 'B', 'term',
    '[THOSE SILVERY SPIKED ROBOS ARE CALLED "SPIKERS"]',
    '  Bossu: [那些银色的带刺机器人叫做「刺虫」。]',
    '游戏内词典条目名 SPIKER = 刺虫（同表 SPIKEBOT=刺机器人、DRILLER=钻探者、BLOCKER=阻挡者），'
    '玩家在图鉴里看到「刺虫」，正文这行却留全大写英文 SPIKERS，Bossu 第一次报名号的台词与词典对不上。'
    '本行同时缺句末句号（全批 302 条非空行绝大多数以「。」收尾），一并补上。',
    [DICT + ' SPIKER = 刺虫', '§四.4 保护标记（[ ] 原样保留）', '§四.11 术语改动须给出处'],
    note=tail('  Bossu: [那些银色的带刺机器人叫做「刺虫」。]'))

# --- 108 Blocker -------------------------------------------------------------
add(108, ['CAT:O850e5e85f7d25926e88d'], 'B', 'term',
    '[AHH, THAT SEEMS TO BE A SMALLER VERSION OF THE BLOCKER]',
    '  Bossu: [啊，那似乎是「阻挡者」的缩小版。]',
    'BLOCKER 在 datav/dictionary.json 的条目名是「阻挡者」，本行留英文 Blocker。'
    '本批其他场次对已命名物种一律用中文引号写法（SC5c5f5477be1d2b03 的「幽灵者」、SCa365f4cac4cbee44 的「光球」、SC8284617482e0142b 的「球茎怪」），'
    '写法不统一；同时缺句末句号。',
    [DICT + ' BLOCKER = 阻挡者', '同批写法：SC5c5f5477be1d2b03「幽灵者」／SCa365f4cac4cbee44「光球」', '§四.4 保护标记'],
    note=tail('  Bossu: [啊，那似乎是「阻挡者」的缩小版。]'))

# --- 109 / 110 DRILLER -------------------------------------------------------
add(109, ['CAT:O92e36425c795c5a40b5f'], 'B', 'term',
    "[AS A NANOMECHANICAL ROBOT, THE 'DRILLER' UNITS WILL] / "
    "[CONTINUOUSLY REPAIR THEMSELVES. THEY'LL BURROW TIRELESSLY.]",
    '  Bossu: [作为一种纳米机械体，那些「钻探者」单元会持续自我修复，还会不知疲倦地钻掘。]',
    "datav/dictionary.json 的条目名 DRILLER = 钻探者，正文却把单元名写成带单引号的全大写英文 'DRILLER'。"
    '原文的单引号只是给新名号加标记，不属于 §四.4 的保护标记；本批其他名号（跳跃者／幽灵者／光球／球茎怪）都用「」。'
    '两句英文并为一句，保证压在原 3 行内。',
    [DICT + ' DRILLER = 钻探者', '§四.4 保护标记（单引号不在列）', '§四.10 男女线分别处理'],
    note=tail('  Bossu: [作为一种纳米机械体，那些「钻探者」单元会持续自我修复，还会不知疲倦地钻掘。]')
    + '同场第二行 CAT:O4afe981d246566c2effd（「的确，特工。DRILLER单元只在预定范围内活动，不会越界。」）'
      '建议同步作 `  Bossu: [的确，特工。「钻探者」单元只在预定范围内活动，不会越界。]`（实测 2／2 行）。')

add(110, ['SFW5fe97bce50fdf703794c4a44'], 'B', 'term',
    "[AS A NANOMECHANICAL ROBOT, THE 'DRILLER' UNITS WILL] / "
    "[CONTINUOUSLY REPAIR THEMSELVES. THEY'LL BURROW TIRELESSLY.]",
    '  Bossu: [作为一种纳米机械体，那些「钻探者」单元会持续自我修复，还会不知疲倦地钻掘。]',
    '与 P05b-109 同因，属 sfw 场的同型行：' + "'DRILLER'" + ' 应作「钻探者」（词典条目 DRILLER = 钻探者）。'
    '两版按 §四.10 分开处理，措辞各自成立，不机械复制。',
    [DICT + ' DRILLER = 钻探者', '§四.10 男女线分别处理'],
    note=tail('  Bossu: [作为一种纳米机械体，那些「钻探者」单元会持续自我修复，还会不知疲倦地钻掘。]')
    + '同场第二行 SFW96fcd436dc8d303fb470be4f（「的确，特工。DRILLER单元只会在它们预定的边界之内运作。」）'
      '建议同步作 `  Bossu: [的确，特工。「钻探者」单元只会在它们预定的边界之内运作。]`（实测 2／2 行）。')

# --- 111 FENFEN --------------------------------------------------------------
add(111, ['SFW58fcacb717e1d3c1e0d0f53b'], 'C', 'term',
    '[REPORTS OF FENFEN OUTFITS STREWN ABOUT ARE ALL WE HAVE.]',
    '  Bossu: [我们只有那些关于 Fenfen 服装散落各处的报告。]',
    '同一场 SFW47326ffeaf3685647efb274d 已写作「机械复制品——Fenfen。」，本行却是全大写带半角空格的 FENFEN；'
    'datav/dictionary.json 的条目名是 FENFEN → Fenfen，男女线其余正文也一律用 Fenfen。'
    '同一场两种写法会让人误以为是两个不同对象，统一为 Fenfen。',
    [DICT + ' FENFEN = Fenfen', '同场 SFW47326ffeaf3685647efb274d', '§四.11 术语改动须给出处'],
    note=tail('  Bossu: [我们只有那些关于 Fenfen 服装散落各处的报告。]'))

# --- 112 lect 小写 -----------------------------------------------------------
add(112, ['SFW9d77dbbdc02ceee322e5d387'], 'C', 'term',
    '[THOSE LIZARDS ARE A SLY BUNCH, KNOWN FOR PIRACY AND SLAVING]',
    '  Bossu: [那些蜥蜴狡猾得很，干海盗和贩奴的勾当出了名，凡是最后能捞到LECT的事，他们都干！]',
    '货币名在本行写作小写并夹两个半角空格的 " lect "，是全批孤例：男线同型句 CAT:O5b4ba87c47509c238e8d 写作「赚到LECT的营生」，'
    'datav/dictionary.json 条目名为 LECT，语料中大写 LECT 共 33 处、小写 lect 仅 8 处。'
    '中文句内夹半角空格且小写，读起来中途断气。',
    [DICT + ' LECT = LECT', '§四.10 跨版本：男线 CAT:O5b4ba87c47509c238e8d（SCdd1003a024a00fd3）'],
    note=tail('  Bossu: [那些蜥蜴狡猾得很，干海盗和贩奴的勾当出了名，凡是最后能捞到LECT的事，他们都干！]'))

# --- 113 半角空格 -----------------------------------------------------------
add(113, ['SFWe2912d7e0113891885a0b1eb'], 'C', 'format',
    "[BOSSU HERE, WHAT'S THE PROBLEM, AGENT?]",
    '  Bossu: [波苏在此，出什么问题了，特工？]',
    '「波苏 在此」中间夹一个半角空格，是排版残留而非停顿标记：本批无线电套语别处都连写'
    '（同批 CAT:Oe221133b4ddccf9c0f90「波苏，请求立即更新当前情况」）。删空格即可，语序与语气不动。',
    ['§四.4 结构：中文句内不留半角空格', '无线电套语写法'],
    note=tail('  Bossu: [波苏在此，出什么问题了，特工？]'))

# --- 114 半角连字符当破折号 ---------------------------------------------------
add(114, ['CAT:Oafa2c8f4181a40861975'], 'C', 'format',
    '[YEAH! IT WAS IN THE MINES, BUT-]',
    '  Yiffai: [对啊！那是在矿坑里，但是——]',
    '原行用半角连字符表示被打断的长破折号；本批同一功能一律用「——」'
    '（同场 CAT:O58d4ef1a57096949cd79「埋了雷——谁碰炸谁」、CAT:O03f10b4c9a480da72ec7「我说——」），'
    '半角连字符在 12px 字库里只占 8px 宽，视觉上缩成小横点，与被截断的语气不匹配。',
    ['§四.7 被打断按功能区分，不能抹平', '§四.4 结构：行尾破折号保持被截断的形态'],
    note=tail('  Yiffai: [对啊！那是在矿坑里，但是——]') + '女线同句 CAT:Oa4ea38656770a5ce786f 用「可——」，已合规。')

# --- 115～121 句末句号 -------------------------------------------------------
PUNCT = [
    (115, 'SFW61ed973476ffe97340e5e182', '  Bossu: [小心那些四处巡逻的带刺无人机。]',
     '[WATCH OUT FOR THOSE PRICKLY DRONES PATHING AROUND]',
     '本行是一条独立陈述句（下一行 EN 另起一句「THEY\'RE LITERALLY IMPOSSIBLE…」），现译结尾无句号。'),
    (116, 'CAT:O66f75236f0ade5bd8183', '  Bossu: [它应该也一样对物理伤害免疫。]',
     '[IT SHOULD JUST AS IMPERVIOUS TO PHY- SICAL DAMAGE]',
     '本行是从句合并后的独立陈述句，结尾无句号；同场其余三行（CAT:O850e5e85f7d25926e88d 之外的 CAT:O39ec02146a0b8eed0da8）都以「。」收尾。'),
    (117, 'CAT:Oc1e29058d884edf3ce2e', '  Bossu: [干掉它，但别被围住，才能活下来。]',
     '[TAKE IT DOWN WITH- OUT BEING BOXED IN, IN ORDER TO SURVIVE]',
     '本场最后一行、独立祈使句，结尾无句号；同批同类祈使句（如 SC3fd869c6a2937dd3「尽量避开就好。」）都带句号。'),
    (118, 'CAT:O07cc193f119910e57da1', '  Yiffai: [我不记得简报里提到过这个区域。]',
     "[I DON'T REMEMBER SEEING THIS AREA IN THE BRIEFING]",
     '本行结尾无句号；男线同型句 CAT:O9f345ddefcefdc2e1260 是同一个漏标点，两版同因。'),
    (119, 'CAT:O9f345ddefcefdc2e1260', '  Yiffai: [我不记得简报里提到过这个区域。]',
     "[I DON'T REMEMBER SEEING THIS AREA IN THE BRIEFING]",
     '与 P05b-118 同因，属另一场的同型行（本批 ClassicXCannonWall 与 ClassicXCannonFloor 两场重复同一段台词）。'),
    (120, 'CAT:O9ff19728e3075adbd1c4', '  Bossu: [你可以靠近它们，让它们自爆，也可以打它们，让它们爆炸。你选吧。]',
     '[YOU CAN EITHER GET NEAR THEM SO THAT THEY DESTRUCT]',
     '本行结尾「你选吧」后无句号，而同批同段台词在 SC862403c68f1d4607／SC2314258606729cd4 已写作「你自己选。」，三处只有这里漏标点。'),
    (121, 'CAT:O2072f53beec326800614', '  Bossu: [要是你遇见近视的棕毛小动物，那些小家伙叫作「吱吱怪」。]',
     '[IF YOU COME ACROSS ANY NEAR-SIGHTED BROWN FUR CRITTERS]',
     '本行是给新物种报名的完整句，结尾无句号；同批报名句（SC88fb3f2b7b4acd86「暂且叫它们「幽灵者」吧。」）都带句号。'),
]
for n, rid, prop, src, why in PUNCT:
    add(n, [rid], 'C', 'format', src, prop,
        '正文结尾缺句末句号。' + why + '补一个句号，不改任何语义、条件与语气。',
        ['§四.2 只替换正文，行首前缀与行尾「]」原样保留', '全批句末标点一致性'],
        note=tail(prop))

# --- 122 行尾半角空格 --------------------------------------------------------
add(122, ['SFWf25c39e15833ca1e59294c34'], 'C', 'format',
    '[EITHER WAY, BE CAREFUL, AGENT!]',
    '  Bossu: [不管怎样，小心点，特工！]',
    '行尾「]」之后还带两个半角空格，全批仅此一处（另一处 SFWf5e2d63876c039cc8f63fe79 在别的场次）。'
    '渲染上看不见，但破坏了「行尾即「]」」这一约定，按行比对的脚本会把它算成差异；男线同型行 CAT:O8ffba486b4343ce835c7 无尾空格。',
    ['§四.2 结构：行尾形态一致', '全批行尾一致性'],
    note=tail('  Bossu: [不管怎样，小心点，特工！]')
    + '英文 source 同样以两个空格结尾，说明残留来自原文件；本条只清渲染残留，不动句子。'
      '若主代理坚持 §四.2「行尾原样保留」从严解释，本条可仅记录不改。')

# --- 123 ACTUAL_HINTS needs_evidence ----------------------------------------
add(123, ['SFW4aa9c46be1d5e96310fb577e'], 'needs_evidence', 'source_uncertainty',
    '[I REMEMBER WHEN I GOT ACTUAL_HINTS FROM THIS LINE...]',
    None,
    '英文原文把 ACTUAL_HINTS 写成全大写下划线令牌，语义是「我记得以前这条线也能给我真正的提示……」：'
    '它描述的是一条本该给出玩法提示的文本行，更像开发期占位符或注释被当成台词发布了。'
    '现译「以前这条线还能给点真正_有用的提示……」把令牌意译成「真正_有用的提示」，读起来像角色在抱怨界面，'
    '但保留了下划线形态，无法判断该保留结构还是彻底改写。同源三处写法完全一致，宜由主代理一并裁决。',
    ['§三 needs_evidence：原文自相矛盾／疑似占位符', 'R9 batch-05-part01 同类判定 P05-121', '§四.4 保护标记（本行无可保护标记）'],
    status='needs_evidence',
    note='同源三处：SC862403c68f1d4607／SFW4aa9c46be1d5e96310fb577e、SCc39f2393aa7808ee／CAT:O552f8ae2a529ef475b11、'
         'SC2314258606729cd4／SFW261aef93fcef8705b7378ffc。三行 current 完全一致，本路不擅改。')

# --- validate ---------------------------------------------------------------
problems = []
seen = set()
for f in F:
    fid = f['finding_id']
    if fid in seen:
        problems.append('dup ' + fid)
    seen.add(fid)
    sid = f['scene_id']
    for rid in f['row_ids']:
        if rid not in rows:
            problems.append('%s unknown row %s' % (fid, rid))
        elif rows[rid][0] != sid:
            problems.append('%s cross-scene %s' % (fid, rid))
    cur = cur_of(f['row_ids'][0])
    if f['current_quote'] != cur:
        problems.append('%s current_quote mismatch' % fid)
    src = f['source_quote'] or ''
    en = rows[f['row_ids'][0]][1]['source']
    for piece in [p.strip() for p in src.split(' / ')]:
        if piece not in en:
            problems.append('%s source piece not in EN: %r' % (fid, piece))
    prop = f['proposed_zh']
    if prop:
        if PREFIX.match(cur).group(1) != PREFIX.match(prop).group(1):
            problems.append('%s prefix drift %r vs %r' % (fid, PREFIX.match(cur).group(1), PREFIX.match(prop).group(1)))
        for box in (240, 224):
            if wraps(prop, box) > 3:
                problems.append('%s wraps %d=%d' % (fid, box, wraps(prop, box)))
        if missing(prop):
            problems.append('%s missing glyphs %s' % (fid, missing(prop)))
        if prop.count('[') != cur.count('[') or prop.count(']') != cur.count(']'):
            problems.append('%s bracket drift' % fid)

print('PROBLEMS:', problems if problems else 'none')
print('findings:', len(F), 'sev:', dict(Counter(x['severity'] for x in F)),
      'cat:', dict(Counter(x['category'] for x in F)))
if problems:
    raise SystemExit(1)

with open(OUT + '/findings.jsonl', 'w', encoding='utf-8', newline='\n') as fh:
    for f in F:
        fh.write(json.dumps(f, ensure_ascii=False) + '\n')

# --- coverage ---------------------------------------------------------------
by_scene = {}
for f in F:
    by_scene.setdefault(f['scene_id'], []).append(f['finding_id'])

NOTES = {
    'SCbbb3f9743ac83409': 'Barker 场。红毛野犬、吠犬对应词典 BARKER=吠犬，「咿！」的被打断与咬人描写语气成立，合句尾行处理正确。',
    'SCc77858a16e5f3301': 'BigboldEnemy 场。Mauser 插话两行说话人正确，大壮兽数量与路线条件未改；「老大」称呼在本批仅此一处，男线用「波苏」，属人物差异不报。',
    'SC0d0a5f0289b723af': 'BugFlier 场。纳米回收长段信息完整；「纳——诺——什么玩意儿？」按 §四.7 保留结巴式打断。仅报 P05b-113。',
    'SCcf775d50518b2323': 'BugSpiker 场。仅报术语 P05b-107。MECHA FASCIMILE 的「精巧的机械仿制品」与原文错拼 fascimile 语义相符，不改。',
    'SC8284617482e0142b': 'Bulber 场。三行合句正确，「球茎怪」与词典一致，保留。',
    'SCcba3ef8792e37240': 'Bullfrog 场。§四之二超限行，报 P05b-101 并已压回 3 行；尾行「幸运的是…伏击」条件句完整。',
    'SCa7d50e8f2d64a2e7': 'BumperC 场（datadf）。弹跳机术语与 R6 裁决一致，装甲额外伤害条件未改，保留。与 SCf89ffbe39fe88fa1 为同台词男线版，措辞差异属 §四.10 允许范围。',
    'SCf89ffbe39fe88fa1': 'BumperC 场（datadm）。同台词男线版，「其他弹跳机都要好」比女线更贴 THAN THE OTHER BUMPERS，两版均成立，不强行对齐。',
    'SC3fd869c6a2937dd3': 'BumperPlus 场（datadm）。故障巡逻机与「别莽撞」的劝告语气完整，保留。',
    'SC74eacd540a84f4fd': 'BumperPlus 场（datadf）。仅有前四行，无「DON\'T BE SO BRASH」段，属版本差异而非漏译。',
    'SC9acf15ba7fbb4877': 'CannonFloor 场。「两个世纪／不可能吧」问答对位正确，制式装备细节未改，保留。',
    'SCbbbce3c2e89f8789': 'CannonFloorC 场（datadm）。「太——好了」拖音与原文 GREEAAAAAT 功能一致，保留。',
    'SC26dbe5fa7ee9cf03': 'CannonWallC 场（datadf）。与男线同台词，「还嫌麻烦不够多是吧」加深了语气但未改事实，属可接受范围。',
    'SCef111241d8b20356': 'CannonWallC 场（datadm）。「是有更强的加农炮，还是我变弱了」问答对位正确，只是各场重复，不报。',
    'SCcb7d60767094d0c1': 'Driller 场（datadf，nsfw）。报 P05b-109。学院男生那句的性暗示与原意一致，未加减。',
    'SC390bee8a49306aa9': 'Driller 场（datadf，sfw）。报 P05b-110；边界表述「只会在它们预定的边界之内运作」比 nsfw 版更贴 PREDETERMINED，两版各自成立。',
    'SCca127a62c96d9ff5': 'DwarfThrower 场。矮人、赌博、射精三段笑点顺序未变，星号强调保留，保留。',
    'SC1ed8b1131ee2b80b': 'Elf 场（datadf）。报 P05b-104（MAY 升格为断言）。「*长生不死*」星号保留。',
    'SC8a64100509cd1232': 'Elf 场（datadm，nsfw）。报 P05b-105（同因）。',
    'SC3048c12be4e1ae2d': 'Elf 场（datadm，sfw）。本场「也许全是雌性」已正确，作为 P05b-104/105 的出处；但本场把一句英文拆成「几百年过去，」「她们身上凡俗的特征也越来越多。」两行，属既有分句，不改。',
    'SC54121e70d4d54642': 'Fenfen 场。报 P05b-111（FENFEN→Fenfen）。同场 SFW47326ffeaf3685647efb274d 已正确，作为出处。',
    'SC0a53291b68449545': 'Fire 场（2 行合句）。「也许能扑灭…必然会重新燃起」may／invariably 层级保留正确，保留。',
    'SCe892358017ef4806': 'Flybomb 场。泽罗尼亚地名与词典一致；爆炸载荷、远程攻击建议完整，保留。',
    'SC88fb3f2b7b4acd86': 'Ghoster 场（datadf）。报 P05b-122（行尾两空格）。「幽灵者」与词典一致。',
    'SC86ba5caa7762044d': 'Hopper 场。「跳跃者」与词典一致；灵能注入的 seems 保留；「*没*被影响」星号保留。',
    'SC7cb61827f3957704': 'Ivyball 场（单行）。「没有情报，因为你杀不死它」与 NO INFO, BECAUSE YOU CAN\'T KILL IT 对位，保留。',
    'SC5c5f5477be1d2b03': 'Jellyfish 场。非实体水母与灵能幻象的 may／seem 层级保留；「百分百的狗」笑点成立。',
    'SCdd1003a024a00fd3': 'Kobold 场（sfw）。「科博德」为 R9 已裁决术语，不重提；SFWf5e2d63876c039cc8f63fe79 也带行尾两空格，与 P05b-122 同因，已在该条 note 中记录，未重复立案。',
    'SCf85bf54dd38c63d4': 'Kobold 场（sfw，短版）。报 P05b-112（lect → LECT 并去半角空格）。男线同型句 CAT:O5b4ba87c47509c238e8d 作为出处。',
    'SCf220ad115895cc8e': 'MineCeiling 场。报 P05b-106（女线残留英文 mine）。Mauser 揭底句「等于立块牌子」为 R5 已裁决口径，不动。',
    'SCb84957d4bbe46c64': 'MineWall 场（男线）。报 P05b-114（半角连字符）。「认了主／炸毛」为 R5 P08-013 已裁决项，不翻案；行内半角双引号原样保留。',
    'SCc39f2393aa7808ee': 'MineWallZero 场（datadf，nsfw）。报 P05b-123（ACTUAL_HINTS needs_evidence），三处同源之一。其余问答与「我以为你不会拿我开涮」对位正确。',
    'SC862403c68f1d4607': 'MineWallZero 场（datadf，sfw）。报 P05b-123 同类（同源第一处）；本场「你自己选。」标点正确，与 P05b-120 的漏标点形成对照。',
    'SC1bfee9d188c714cf': 'MineZero 场（datadm，nsfw）。报 P05b-120（「你选吧」缺句号）。',
    'SC2314258606729cd4': 'MineZero 场（datadf，sfw）。报 P05b-123 同类（同源第三处）；本场句末标点齐全。',
    'SCcac2a16949d1ed95': 'Omegothrower 场。欧米茄哥布林与词典一致；树冠投掷、投掷后闪避的玩法提示完整，may 保留。',
    'SCa365f4cac4cbee44': 'Orber 场。「光球」与词典一致；触手性暗示分寸与原文相当。EN 有 YOUR TENTACLE 单复数含糊，两版都写「一两根小触手」，不属误义。',
    'SCcca65604ac8d3a29': 'SpaceHead 场。幽灵者对照与灵能扰动 seems 保留；「你一定正接近…源头」的语气强度与原文相符。',
    'SC3a28513b100a3730': 'Spiderbot 场（datadf）。蛛网／粘胶／退休三点与男线用字不同（蛛丝／黏胶／退隐），属 §四.10 允许的版本差异，两版内部各自一致，不立案，仅在 summary 记录。',
    'SCeb6f35bc1c4dc1e8': 'Spiderbot 场（datadm）。同上一场的男线版；「黏胶」与词典写法一致，而女线作「粘胶」，见 summary 跨版本清单。',
    'SCe9f5656bf5b59b65': 'SpikeballZero 场。报 P05b-103（LITERALLY 丢失）与 P05b-115（缺句号）。「超能力者」与词典 ESPER=超能力者一致。',
    'SC3a9d5c967ef75eca': 'Spikebot 场（datadf）。§四之二超限行，报 P05b-102 并已压回 3 行。',
    'SCd60875d2efc81ef1': 'Spikebot 场（datadm）。本场同句在 240px 为 3 行（224px 为 4 行），未列入 §四之二，故不改动，仅记录。',
    'SC9ede255817e3dec1': 'Squeaker 场。报 P05b-121（缺句号）。「吱吱怪」与词典一致。',
    'SC22000b29b74a37c9': 'Tentacle 场。报 P05b-108（Blocker → 「阻挡者」）与 P05b-116（缺句号）。',
    'SC51e58355ec29489c': 'Viner 场。报 P05b-117（缺句号）。四行合句的施受关系（植物围困猎物、其他生物先解决猎物）正确。',
    'SCdb81ad56e11ce1c1': 'XCannonFloor 场（datadm）。报 P05b-118（缺句号）。塑化金属、蜥蜴海盗建基地的两处事实未改。',
    'SC8d856f259bdafc17': 'XCannonWall 场（datadm）。报 P05b-119（缺句号），与 SCdb81ad56e11ce1c1 为重复台词。',
    'SC56e5db567ec62cce': 'Xeno 场（datadm）。「虫卵宿主／子宫破体」的 may 层级保留；「善于趁虚而入」比女线「伺机而动」更解释性，但未加事实，属可接受差异。',
    'SC6b77e7e0f15fd941': 'Xeno 场（datadf）。同台词女线版，「幼体可能会等不及」保留 COULD 的可能性，正确。',
}

order_ids = [s['scene_id'] for s in order['scenes']]
missing_scenes = [s for s in order_ids if s not in NOTES]
extra = [s for s in NOTES if s not in order_ids]
assert not missing_scenes, missing_scenes
assert not extra, extra

with open(OUT + '/coverage.jsonl', 'w', encoding='utf-8', newline='\n') as fh:
    for sid in order_ids:
        fids = by_scene.get(sid, [])
        rec = {
            'scene_id': sid,
            'read_status': 'read_full',
            'row_ids': scene_rows[sid],
            'result': 'needs_evidence' if any(x['status'] == 'needs_evidence' for x in F if x['scene_id'] == sid)
            else ('issues_found' if fids else 'retain'),
            'findings': fids,
            'notes': NOTES[sid],
        }
        fh.write(json.dumps(rec, ensure_ascii=False) + '\n')

print('coverage scenes:', len(order_ids))
print('scenes with findings:', len(by_scene), 'retain scenes:', len(order_ids) - len(by_scene))
print('done')
