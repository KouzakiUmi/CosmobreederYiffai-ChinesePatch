"""Write the r9 batch-06-part02 decision table.

Row ids are taken from each route's own findings file, so no id is typed from
memory here: a decision names (route, finding_id), and the row it lands on is
whatever that finding actually pointed at.
"""
from pathlib import Path
import json

ROOT = Path(__file__).resolve().parents[4]
BASE = ROOT / 'localization/editorial/r9-polish/batch-06-part02'
ORDER = json.loads((BASE / 'orders/batch-06-part02.json').read_text('utf8'))
ROWS = {r['row_id']: (s['scene_id'], r) for s in ORDER['scenes'] for r in s['rows']}


def load(route):
    out = {}
    for line in (BASE / route / 'findings.jsonl').read_text('utf8').splitlines():
        if not line.strip():
            continue
        f = json.loads(line)
        out[f['finding_id']] = f
    return out


ROUTE = {'gemini': load('gemini'), 'ds': load('ds')}

PLAN = [
    ('ds', 'P06b-101', 'apply',
     '工单四之二点名超限：原译 56 字实测 4 行。取 DS 版——Gemini 版把「如果你有一只很喜欢你的生物」的条件从句并成「抚摸亲近你的生物」，条件被压扁。保留场衰减棱镜技术名、抚摸充能的条件、效果因生物而异三项。240px／224px 均 3 行。'),
    ('ds', 'P06b-102', 'apply',
     '工单四之二点名超限：原译 68 字实测 4 行。取 DS 版——Gemini 版删掉「光是握着它，我就能想象」的第一人称与「海盗」，叙述视角被压成旁白。保留握持带出的想象、海盗身份、想要就夺、来粗的调侃四层。240px／224px 均 3 行。'),
    ('ds', 'P06b-103', 'apply',
     '工单四之二点名超限：原译 54 字实测 4 行。取 DS 版——Gemini 版去掉按键原有引号并删「特工」，按键标记的引号位置不该动。保留报告来源、战斗时机、两段按键与相应能力。240px／224px 均 3 行。'),
    ('ds', 'P06b-116', 'apply',
     'UP+ATTACK 是按键名，硬约束要求原样保留；本行把 ATTACK 译成「攻击」，而同场上一行已作 UP+ATTACK。全库另有 3 处同类，不在本批范围，见 R9M-801。'),
    ('ds', 'P06b-113', 'apply',
     '词典条目名是「钩爪」（正文 5 处），同场下一行也作「射出钩子」；「钩锁」只有 2 处，是生成时引入的偏差。'),
    ('ds', 'P06b-115', 'apply',
     '词典条目名是「超能护腕」（正文 6 处）；「助推护腕」4 处是另一套自造写法。下一行说的是宇宙育种者制服的标准配备，讲的是护腕本身而不是助推。'),
    ('ds', 'P06b-114', 'apply',
     'KOBO 旧译「狗头人」残留。全库 99 处作「科博德」，batch-02 已把同 root 四处改为「科博德」，两路本批也都独立报出这一行。本行与 part01、part03 的同类行一并归位。'),
    ('ds', 'P06b-120', 'apply',
     'HEAVY EQUIPMENT 在同 root 另两处作「重型装备」，「重型设备」只此一处；中文里装备与机械分属两义。'),
    ('ds', 'P06b-112', 'apply',
     '终端设备名 P.A.W. 带句点；本批 11 处中 10 处带点，全库 126/135。只补一个点。'),
    ('ds', 'P06b-119', 'apply',
     '原文 UP TO THE LEVEL DISPLAYED ON THEM 的 ON THEM 指门；现译「门卡上标的等级」把等级挪到卡上，与上一行「带着卡走向能量门」的流程对不上。同 root 另一场作「门上所标数字」，此处对齐。'),
    ('ds', 'P06b-121', 'apply',
     '原文 A SEEMINGLY ENDLESS SUPPLY 的 supply 指镐的供应，不是力气；现译「有用不完的力气」把 supply 换成 strength，下一行「以你的臂力，一柄镐只能扔一次」就失去对照——正因为镐子管够才轮得到谈臂力。'),
    ('ds', 'P06b-118', 'apply',
     '「把你喝醉了扔出去」结构读不通（把＋小句＋动词）；原文 TOSSING YOUR DRUNK ASS OUT 的 drunk 修饰的是人。改「你这醉鬼」，粗鲁口气不变。'),
    ('ds', 'P06b-117', 'apply',
     '「小时候还是幼犬时」同义重复；「吞嚼咬玩具」三个动词粘连，且小时候／幼犬时时间概念也重复。压成「当幼犬时吞咬胶玩具」，去重但保留自嘲。'),
    ('ds', 'P06b-109', 'apply',
     '被截断处用半角短横，12px 渲染成一个孤立小横；全批其它被打断处一律用全角破折号。'),
    ('ds', 'P06b-110', 'apply',
     '结巴处的半角连字符「好-好吃」在中文里应作顿号，与本作其它结巴写法（「这、这些」「那、那个」）一致。'),
    ('ds', 'P06b-111', 'apply',
     '同上一处：结巴的「行-行吧」改顿号。'),
    ('gemini', 'P06b-111', 'reject',
     '与本表 ds:P06b-105 同一行同一处（行尾空格），两路同报，取 DS 条落地。'),
    ('gemini', 'P06b-112', 'reject',
     '与本表 ds:P06b-106 同一行同一处（行尾空格），取 DS 条落地。'),
    ('gemini', 'P06b-113', 'reject',
     '与本表 ds:P06b-107 同一行同一处（行尾空格），取 DS 条落地。'),
    ('gemini', 'P06b-119', 'reject',
     '与本表 ds:P06b-108 同一行同一处（行尾空格），取 DS 条落地。'),
    ('ds', 'P06b-104', 'apply', '行尾残留一个半角空格。'),
    ('ds', 'P06b-105', 'apply', '行尾残留一个半角空格。'),
    ('ds', 'P06b-106', 'apply', '行尾残留一个半角空格。'),
    ('ds', 'P06b-107', 'apply', '行尾残留一个半角空格。'),
    ('ds', 'P06b-108', 'apply', '行尾残留两个半角空格。'),
    ('gemini', 'P06b-101', 'apply', '本行是完整句子，下一行换说话人，中文缺句末标点。'),
    ('gemini', 'P06b-103', 'apply', '整句到此为止而缺句号。'),
    ('gemini', 'P06b-104', 'apply', '本行是完整句子，缺句末标点。'),
    ('gemini', 'P06b-106', 'apply', '本行是完整句子，缺句末标点。'),
    ('gemini', 'P06b-107', 'apply', '女版同句同改。'),
    ('gemini', 'P06b-108', 'apply', '整句到此为止而缺句号。'),
    ('gemini', 'P06b-115', 'apply', '整句到此为止而缺句号。'),
    ('gemini', 'P06b-116', 'apply', '整句到此为止而缺句号。'),
    ('gemini', 'P06b-118', 'apply', '本行是未完分句，下一行接着说完，中文缺逗号承接。只补逗号，不动措辞。'),
    ('gemini', 'P06b-102', 'reject',
     '与本表 ds:P06b-109 同一行同一处（半角短横改破折号），已按行落地。'),
    ('gemini', 'P06b-114', 'reject',
     '与本表 ds:P06b-114 同一行同一处（狗头人→科博德），两路独立得出同一结论，取 DS 的措辞落地。'),
    ('gemini', 'P06b-105', 'reject',
     '与本表 ds:P06b-105 同一行（KoboHead 那行的行尾空格），已由 DS 条落地；本条不另立操作。'),
    ('gemini', 'P06b-110', 'reject',
     '与本表 ds:P06b-116 同一行同一处（UP+攻击→UP+ATTACK），已按行落地。'),
    ('gemini', 'P06b-109', 'reject',
     '与本表 ds:P06b-101 同一处超限压缩；Gemini 版把条件从句压扁，取 DS 版。'),
    ('gemini', 'P06b-117', 'reject',
     '与本表 ds:P06b-102 同一处超限压缩；Gemini 版删掉第一人称与「海盗」，取 DS 版。'),
    ('gemini', 'P06b-120', 'reject',
     '与本表 ds:P06b-103 同一处超限压缩；Gemini 版去掉按键引号并删「特工」，取 DS 版。'),
]

HOLD = [
    ('R9M-801', 'B', 'gameplay', 'SCc7219f770fd727bd', 'CAT:O55642f0cd75514b5487f',
     'UP+ATTACK 被译成「UP+攻击」全库共 5 处；本表已改本批范围内的一处（ds:P06b-116）。另处分布在 Mauser.AreaB_map10、Tomcat.AreaC_map64（两行）与 TomcatItems.SpecialHookshot 的女版，都不在 batch-06 的 root 里，登记待后续批次一并归位，避免只改一半。'),
    ('R9M-802', 'C', 'format', 'SC98f7cfffc1d98d81', 'CAT:Ob2dee70046f920c2187b',
     '全批「“”」与「「」」两套引号并存，属跨 part 格式裁决。本批只在既有点位保留原体例，不做全局统一。'),
]


def main():
    lines = ['finding_id\troute\tseverity\tcategory\tscene_id\trow_id\tdecision\tfinal_zh\treason']
    seen = set()
    for route, fid, decision, reason in PLAN:
        if fid not in ROUTE[route]:
            raise SystemExit('no such finding: %s:%s' % (route, fid))
        key = route + ':' + fid
        if key in seen:
            raise SystemExit('planned twice: ' + key)
        seen.add(key)
        f = ROUTE[route][fid]
        rid = f['row_ids'][0]
        if rid not in ROWS:
            raise SystemExit('unknown row %s from %s' % (rid, key))
        scene_id, row = ROWS[rid]
        final = ''
        if decision == 'apply':
            final = f.get('proposed_zh') or ''
            if not final:
                raise SystemExit('apply without text: ' + key)
            if not (row['current'] or '').strip():
                raise SystemExit('blank line target ' + rid)
            if row['current'] == final:
                raise SystemExit('no-op ' + rid)
        lines.append('\t'.join((key, route, f.get('severity', ''),
                                f.get('category', ''), scene_id, rid,
                                decision, final, reason)))

    for fid, sev, cat, scene_id, rid, reason in HOLD:
        if rid not in ROWS:
            raise SystemExit('unknown row ' + rid)
        lines.append('\t'.join((fid, 'R9M', sev, cat, scene_id, rid, 'hold', '', reason)))

    (BASE / 'review/decisions.tsv').write_text('\n'.join(lines) + '\n', encoding='utf8')
    applies = sum(1 for p in PLAN if p[2] == 'apply')
    rejects = sum(1 for p in PLAN if p[2] == 'reject')
    print(json.dumps({'decisions': len(lines) - 1, 'apply': applies,
                      'reject': rejects, 'hold': len(HOLD)}, ensure_ascii=False))


if __name__ == '__main__':
    main()
