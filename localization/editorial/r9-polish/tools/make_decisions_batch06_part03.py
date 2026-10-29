"""Write the r9 batch-06-part03 decision table.

PLAN takes its text from the route's own findings file. Where a row was
proposed by both routes, one entry applies and the other records which won.
"""
from pathlib import Path
import json

ROOT = Path(__file__).resolve().parents[4]
BASE = ROOT / 'localization/editorial/r9-polish/batch-06-part03'
ORDER = json.loads((BASE / 'orders/batch-06-part03.json').read_text('utf8'))
ROWS = {r['row_id']: (s['scene_id'], r) for s in ORDER['scenes'] for r in s['rows']}


def load(route):
    out = {}
    p = BASE / route / 'findings.jsonl'
    if not p.exists():
        return out
    for line in p.read_text('utf8').splitlines():
        if not line.strip():
            continue
        f = json.loads(line)
        out[f['finding_id']] = f
    return out


ROUTE = {'gemini': load('gemini'), 'ds': load('ds')}

# 全库取证：挥爪 26 / 挥击 2（词典 SWIPER→挥爪）；造物 4 / 遗物 5；
# P.A.W. 带点 126/135；通话完毕 33 / 通话结束 17（既有分布，不强行统一）

APPLY = [
    # —— A：按键名被汉化 ——
    ('gemini', 'P06c-107', '`UP+ATTACK` 是按键名，本行译成「UP+攻击」；同 root 另有行仍作 UP+ATTACK，玩家会照着找不到键。只改按键，句子其余不动。'),
    ('gemini', 'P06c-117', '`DOWN`／`JUMP` 是按键名，本行译成「"下"+"跳跃"」；同时该行前缀有两个空格（`Tomcat:  [`），一并收成一个。'),
    ('ds', 'P06c-S2-107', 'REJECT：与本表 gemini:P06c-117 同一行同一处（DOWN+JUMP 汉化），两路同报，取 gemini 条落地；该条同时处理前缀双空格。'),

    # —— A：术语 ——
    ('gemini', 'P06c-115', 'KOBO 旧译「狗头人」残留；全库 99 处作「科博德」，batch-02 已改同 root 四处。'),
    ('ds', 'P06c-S2-103', 'REJECT：与本表 gemini:P06c-115 同一行同一处，两路同报，取 gemini 条落地。'),
    ('ds', 'P06c-S2-105', 'SWIPER 词典条目名是「挥爪」（正文 26 处）；「挥击」只 2 处，是自造写法。'),

    # —— A：语义 ——
    ('gemini', 'P06c-114', '原文 I RAN INTO THIS **GLOWING** ORB 的 GLOWING 被整个漏掉。下一行紧接说「它发光的样子」，不补这层读者会跟不上。'),
    ('gemini', 'P06c-102', '「你现在还是不偶尔吃点软食吧？」把否定与频度副词直搬，中文读成逻辑颠倒。原文 STILL DON’T DIP INTO SOFT FOOD 是「还是不去沾点软食」，改后反问才成立。'),
    ('gemini', 'P06c-124', '原文 them 指的是机库里关着的那些怪物，前面用「它们」；现译「他们」把非人对象写成人类第三人称。'),
    ('ds', 'P06c-S2-104', '原文 SOME OF YOUR FELLOW AGENTS（你之前的几位同僚特工）；现译「你之前的一些特工」读成「你以前有过的特工」，所属关系反了。与 batch-06-part01 的 ds:P06a-S1-122 是同一句的两版。'),
    ('ds', 'P06c-S2-124', '原文连「波苏」带「我」都说情报不足；现译「波苏都没多少情报，我也补充不了多少」把主语关系读成递进否定，与后半「也许都藏起来了？」的猜测语气接不上。'),

    # —— A：拒绝（方向判错 / 已裁项） ——
    ('gemini', 'P06c-108', 'REJECT：本条主张 THEM 指门卡，改成「凭这张门卡，同级或更低级的门都能打开」。同 root 另两处、batch-06-part01／part02／part04 已据 ON THEM 判为门上所标等级，且上一行明说「拿着一张走进能量门」。现译「门上所标数字」是对的，不改。'),

    # —— B：结构（行尾空格 / 破折号 / 结巴 / 句末标点） ——
    ('gemini', 'P06c-101', '被打断处用半角连字符，12px 渲染成孤立小横；全批其它打断处一律用全角破折号。'),
    ('gemini', 'P06c-118', '同上一处：半角连字符改破折号。'),
    ('gemini', 'P06c-119', '同上一处。'),
    ('gemini', 'P06c-126', '结巴处「好-好吃」的半角连字符改顿号，与本作其它结巴写法一致。'),
    ('ds', 'P06c-S2-118', 'REJECT：与本表 gemini:P06c-126 同一行同一处，取 gemini 条落地。'),
    ('gemini', 'P06c-103', '行尾残留一个半角空格。'),
    ('gemini', 'P06c-104', '行尾残留一个半角空格。'),
    ('gemini', 'P06c-109', '行尾残留一个半角空格。'),
    ('gemini', 'P06c-111', '行尾残留一个半角空格。'),
    ('gemini', 'P06c-121', '行尾残留一个半角空格。'),
    ('gemini', 'P06c-125', '行尾残留一个半角空格。'),
    ('gemini', 'P06c-130', '行尾残留两个半角空格。'),
    ('ds', 'P06c-S2-101', 'REJECT：与本表 gemini:P06c-109 同一行同一处（行尾空格），两路同报，取 gemini 条落地。'),
    ('ds', 'P06c-S2-128', 'REJECT：与本表 gemini:P06c-130 同一行同一处（行尾两空格），取 gemini 条落地。'),
    ('ds', 'P06c-S2-112', 'REJECT：与本表 gemini:P06c-121 同一行同一处（行尾空格），取 gemini 条落地。'),
    ('ds', 'P06c-S2-108', 'REJECT：与本表 gemini:P06c-118 同一行同一处（半角连字符），取 gemini 条落地。'),
    ('ds', 'P06c-S2-109', 'REJECT：与本表 gemini:P06c-119 同一行同一处，取 gemini 条落地。'),
    ('gemini', 'P06c-105', '本行是完整句子而句末无标点，下一行换说话人。'),
    ('gemini', 'P06c-106', '反问的「哦是吗」缺问号，读者分不出是陈述还是反诘。'),
    ('gemini', 'P06c-127', '感叹句「我的天哪」缺标点。'),
    ('gemini', 'P06c-132', '句末是疑问分句而缺问号。'),
    ('gemini', 'P06c-122', '本行与下一行是同一句的两段（准是上次出击的人落下的……／那些怪物），中文缺承接省略号会把两句黏成一句。'),

    # —— B：其余 ——
    ('gemini', 'P06c-110', '行首「不、不是那种」的顿号处夹了半角空格。'),
    ('gemini', 'P06c-116', '同上一处，女版。'),
    ('gemini', 'P06c-128', '前缀有两个空格（`Tomcat:  [`），全批只此一处与 P06c-117 两处，收成一个。'),
    ('ds', 'P06c-S2-120', 'REJECT：与本表 gemini:P06c-128 同一行同一处（前缀双空格），两路同报，取 gemini 条落地。'),
    ('gemini', 'P06c-129', '「他说自己接触到了自己从来不知道的某一面」两个「自己」指同一个人，读成自我接触；原文是接触到自身未知的一面。'),
    ('ds', 'P06c-S2-121', 'REJECT：与本表 gemini:P06c-129 同一行，两路同报；gemini 条只改重复指代，改动更小，取之。'),
    ('gemini', 'P06c-131', '「生命体征又出现一次飙升」是英语 A SPIKE 的直搬；中文说「又飙升了一次」更顺。'),
    ('ds', 'P06c-S2-119', '「它似乎每当我把它放到装备附近就会有反应」把 WHENEVER 从句嵌在「似乎」后面，中文读起来断气；调成「似乎每当我……，它就会有反应」。'),
    ('ds', 'P06c-S2-106', '「我不太懂你在说什……」的省略号落在「什」字后，读者会以为是「说什么」缺字；补完整。'),
    ('ds', 'P06c-S2-111', '本作把可解谜的古代造物统一作「遗物」（正文 5 处对「造物」4 处），且「造物」在中文里偏指造物主所造之物。'),
    ('ds', 'P06c-S2-110', '同批 OUT 公式本行作「通话结束」，而全库「通话完毕」33 处对「通话结束」17 处；本行与同场其它 OUT 行不一致，按多数归位。'),
    ('ds', 'P06c-S2-123', '同上一处，男版对应行。'),
    ('ds', 'P06c-S2-126', '本行是完整句子而句末无标点，下一行另起。'),
    ('ds', 'P06c-S2-127', '同上，句末缺标点。'),
    ('ds', 'P06c-S2-117', '「锋利得必要时完全能当武器。」句尾用句号但整句是被打断的补充说明，按同批写法改为省略号。'),

    ('ds', 'P06c-S2-102', 'REJECT：与本表 gemini:P06c-114 同一行同一处（GLOWING 漏译），两路同报，取 gemini 条的措辞落地。'),
    ('ds', 'P06c-S2-122', '同批 OUT 公式本行作「通话结束」；与本表 ds:P06c-S2-110 同一类，按「通话完毕」的多数写法归位。'),
    ('gemini', 'P06c-113', 'REJECT：与本表 gemini:P06c-109 同一行同一处（行尾空格），重复引用，已按那条落地。'),
    ('gemini', 'P06c-123', 'REJECT：与本表 gemini:P06c-121 同一行同一处（行尾空格），重复引用。'),
    ('gemini', 'P06c-112', '行尾残留一个半角空格。'),
    ('gemini', 'P06c-120', '本行是未完分句的收尾，下一行接着说完；中文缺省略号承接。'),

    # —— 驳回：风格偏好或依据不足 ——
    ('ds', 'P06c-S2-113', 'REJECT：主张改「兄 弟 ……」。原文 D U D E . . . 逐字加空格、末尾接省略点，「兄 弟 ……」正是这条排版的镜像；part04 的 gemini:P06d-106 也独立判为不改。'),
    ('ds', 'P06c-S2-125', 'REJECT：主张改上一行「老兄。兄弟。给我。」的断句。原文 DUDE. BRO. GIMME. 本就是三个独立短句，现译与之逐句对应，无结构缺陷。'),
    ('ds', 'P06c-S2-114', 'REJECT：主张改「蝌蚪出了名地滑溜……似乎还可能恢复」的连词。该行是两条英文合句后的尾句，语气连贯可读，改它属润色。'),
    ('ds', 'P06c-S2-115', 'REJECT：主张把「兽装」改成别的写法。全库「兽装」仅此 1 处，但它是本作既有译法且读得通；改成自造新词没有依据。'),
    ('ds', 'P06c-S2-116', 'REJECT：与上一条同族，针对「装扮用的」提法；无库内依据，属润色。'),
]

SELF = [
    ('R9M-906', 'A', 'gameplay', 'SCb28ad558d39b8510', 'CAT:O8e8cd9a7820dc9fdc872',
     '  Tomcat: [你能打开等级不超过门上所标数字的门！]',
     '本行译文正确，登记为「已一致，不改」：THEM 指门，与同 root 男线、batch-06 前三个 part 的同一句一致。本批与 part04 各有一次提案要把等级挪回卡上，均驳回，此处记明理由是防止后续批次再翻。'),
]

HOLD = [
    ('R9M-907', 'B', 'term', 'SCb28ad558d39b8510', 'CAT:O8e8cd9a7820dc9fdc872',
     '门卡这一句在五个 root 里出现六次，其中三处已统一为「门上所标等级／数字」，两处仍是别的写法。全库统一需跨 root 一次改完，本批只锁定本批范围内的写法，其余登记待后续批次。'),
]


def main():
    lines = ['finding_id\troute\tseverity\tcategory\tscene_id\trow_id\tdecision\tfinal_zh\treason']
    seen = set()

    def emit(key, route, sev, cat, rid, decision, final, reason):
        if rid not in ROWS:
            raise SystemExit('unknown row %s from %s' % (rid, key))
        if key in seen:
            raise SystemExit('planned twice: ' + key)
        seen.add(key)
        scene_id, row = ROWS[rid]
        if decision == 'apply':
            if not (row['current'] or '').strip():
                raise SystemExit('blank line target ' + rid)
            if row['current'] == final:
                raise SystemExit('no-op ' + rid)
        lines.append('\t'.join((key, route, sev, cat, scene_id, rid, decision, final, reason)))

    for route, fid, reason in APPLY:
        if fid not in ROUTE[route]:
            raise SystemExit('no such finding: %s:%s' % (route, fid))
        f = ROUTE[route][fid]
        decision = 'reject' if reason.startswith('REJECT') else 'apply'
        final = '' if decision == 'reject' else (f.get('proposed_zh') or '')
        if decision == 'apply' and not final:
            raise SystemExit('apply without text: %s:%s' % (route, fid))
        emit(route + ':' + fid, route, f.get('severity', ''), f.get('category', ''),
             f['row_ids'][0], decision, final, reason)

    for fid, sev, cat, scene_id, rid, final, reason in SELF:
        key = fid
        # SELF rows that only annotate are recorded as holds, not rewrites
        rid_rows = ROWS.get(rid)
        if rid_rows and rid_rows[1]['current'] == final:
            lines.append('\t'.join((key, 'R9M', sev, cat, scene_id, rid, 'hold', '', reason)))
        else:
            emit(key, 'R9M', sev, cat, rid, 'apply', final, reason)

    for fid, sev, cat, scene_id, rid, reason in HOLD:
        emit(fid, 'R9M', sev, cat, rid, 'hold', '', reason)

    (BASE / 'review/decisions.tsv').write_text('\n'.join(lines) + '\n', encoding='utf8')
    applies = sum(1 for r, f, reason in APPLY if not reason.startswith('REJECT'))
    rejects = sum(1 for r, f, reason in APPLY if reason.startswith('REJECT'))
    print(json.dumps({'decisions': len(lines) - 1, 'apply': applies,
                      'reject': rejects, 'hold': len(HOLD) + 1}, ensure_ascii=False))


if __name__ == '__main__':
    main()
