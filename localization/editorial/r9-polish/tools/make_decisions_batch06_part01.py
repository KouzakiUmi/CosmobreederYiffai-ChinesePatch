"""Write the r9 batch-06-part01 decision table.

The DS route ran as two agents over half the reader each, so its findings are
loaded from two files. Row ids come from those findings, never typed here.
"""
from pathlib import Path
import json

ROOT = Path(__file__).resolve().parents[4]
BASE = ROOT / 'localization/editorial/r9-polish/batch-06-part01'
ORDER = json.loads((BASE / 'orders/batch-06-part01.json').read_text('utf8'))
ROWS = {r['row_id']: (s['scene_id'], r) for s in ORDER['scenes'] for r in s['rows']}


def load(*paths):
    out = {}
    for p in paths:
        for line in Path(p).read_text('utf8').splitlines():
            if not line.strip():
                continue
            f = json.loads(line)
            out[f['finding_id']] = f
    return out


ROUTE = {
    'gemini': load(BASE / 'gemini' / 'findings.jsonl'),
    'ds': load(BASE / 'ds' / 'findings.jsonl'),
}

# 全库取证：小狗崽 40／小狗狗 14；P.A.W. 带点 126/135；PUPLOCK 仅此一处且词典无条目

PLAN = [
    # —— A：按键名被汉化 ——
    ('gemini', 'P06a-104', 'apply',
     '`UP+ATTACK` 是按键名，硬约束要求原样保留；本行把 ATTACK 译成「攻击」并给两端加双引号，而同批其它行、全库多数行都作 UP+ATTACK。只改按键这一处，句子其余部分不动。'),

    # —— B：术语（词典依据） ——
    ('gemini', 'P06a-103', 'apply',
     'KOBO 旧译「狗头人」残留。全库 99 处作「科博德」，batch-02 已把同 root 四处改为「科博德」，本行是同类残留。'),
    ('ds', 'P06a-S2-101', 'reject',
     '与本表 gemini:P06a-103 同一行同一处（狗头人→科博德）已落地。本条另主张把「小狗狗」改「小狗崽」，但这两句是雄猫对不同道具的招呼语，全库「小狗崽」40 处、「小狗狗」14 处本就并存，不是同一词条的两种写法，改它属于风格偏好，不作术语修正。'),
    ('ds', 'P06a-S2-104', 'reject',
     '与本表 gemini:P06a-103 同一行同一处（狗头人→科博德），两路同报，已按 gemini 条落地。'),

    # —— B：语义（原文方向被译反） ——
    ('ds', 'P06a-S2-103', 'apply',
     '原文 IT\'D COMMAND TOP LECT 说的是这奶酪**能卖出**顶级价，现译「那可得花一大笔 LECT 才能买到」把卖价说成买价，方向反了。男线同句另一场（SC1ab56d6909194ab4，CAT:O6030524ddeff17e10ddb）已作「肯定能卖一大笔 LECT」，此处与之对齐。'),

    # —— C：结构 ——
    ('ds', 'P06a-S1-102', 'apply',
     '终端设备名 `P.A.W.` 带句点；全库 126/135 带点，本批多处也带点，此行漏了。只补一个点。'),
    ('ds', 'P06a-S2-102', 'reject',
     '主张把「一个白热的光点」改成「白得发烫的光点」。WHITE HOT 在此是扫描仪显示上的白炽点，「白热」是既有译法且读得通；改后把物理描述换成触觉比喻，属风格偏好。'),
    ('ds', 'P06a-S2-105', 'apply',
     '本行是完整独立陈述而句末无标点；下一行「吃完这么大一块……」是另起一句（英文 AFTER GORGING ON THAT... 亦另起），不补会把两句黏成一句。'),
    ('ds', 'P06a-S2-106', 'apply',
     '「……严重违禁品」句末缺标点，直接接下一行「这是黑市生物加密货币」，读起来像一句没说完的话被掐断；补句号恢复「定罪→解释是什么」两步递进。'),
    # —— 上半段其余 18 条补齐 ——
    ('ds', 'P06a-S1-106', 'apply',
     '原文 UP TO THE LEVEL DISPLAYED ON THEM 的 ON THEM 指门；现译「门卡上标着等级」把等级挪到卡上，与上一行「带着卡走向能量门」的流程对不上。与 batch-06-part02 的 ds:P06b-119 是同一处缺陷的男版。'),
    ('ds', 'P06a-S1-117', 'apply',
     '词典条目名是「小圆盾」（BUCKLER → 小圆盾）；现译「能量圆盾」把条目名里的「小」丢了。只补一个字。'),
    ('ds', 'P06a-S1-103', 'apply',
     '「漂亮的精灵新头冠」把形容词安在「精灵」上，读起来像买了一顶「精灵」；原文是 NEW ELF HEADDRESS，新的是头冠。调换语序即可。'),
    ('ds', 'P06a-S1-116', 'apply',
     '本作把可解谜的古代造物统一作「遗物」（正文 5 处）；「造物」4 处是另一种写法，且「造物」在中文里偏指造物主所造之物，与本义（拾得的古物）有偏差。'),
    ('ds', 'P06a-S1-118', 'apply',
     '原文 THE REST OF MY UNIFORM 指这一身制服的其余部分；现译「我的其他制服」变成了另外几套制服，与「没跟它放在一起」对不上。'),
    ('ds', 'P06a-S1-122', 'apply',
     '原文 SOME OF YOUR FELLOW AGENTS（你之前的几位同僚特工）；现译「你之前的一些特工」读成「你以前有过的特工」，把所属关系说反了。'),
    ('ds', 'P06a-S2-109', 'apply',
     '原文 OH NO 在此不是惊呼而是转折否认：上一句问「有什么问题吗」，本句答「哦，没事！它就是看着好好吃」。现译「哦，不！」变成惊叫，与后半句接不上。'),
    ('ds', 'P06a-S1-101', 'apply',
     '「只有一个办法能知道」是英语 ONLY ONE WAY TO FIND OUT 的直搬；中文里 FIND OUT 在这里是「弄清楚／试了才知道」，改「弄清楚」更顺，句意不变。'),
    ('ds', 'P06a-S1-104', 'apply',
     '行尾的 `"不"` 用了半角双引号，全批中文引号一律用全角；只换引号，不动措辞。'),
    ('ds', 'P06a-S1-107', 'apply', '本行是完整独立陈述而句末无标点；下一行换说话人。'),
    ('ds', 'P06a-S1-108', 'apply', '本行是完整句子，下一行换说话人，缺句末标点。'),
    ('ds', 'P06a-S1-109', 'apply', '整句到此为止而缺句号。'),
    ('ds', 'P06a-S1-110', 'apply', '女版同句同改。'),
    ('ds', 'P06a-S1-111', 'apply', '整句到此为止而缺句号。'),
    ('ds', 'P06a-S1-112', 'apply',
     '本行是未完分句的收尾（「更专注一些，」），但下一行是新句子而非续句，中文用逗号会与下一行黏连。'),
    ('ds', 'P06a-S1-113', 'apply', '整句到此为止而缺句号。'),
    ('ds', 'P06a-S1-114', 'apply', '本行是完整句子，缺句末标点。'),
    ('ds', 'P06a-S1-119', 'apply', '整句到此为止而缺句号。'),
    ('ds', 'P06a-S1-120', 'apply',
     '「要是你有一只很喜欢你的生物，就可以抚摸它们」单复数不一致（一只→它们）；改成「抚摸它」即可，同时把「有一只」压成「有只」与 gemini 版同批行一致。'),
    ('ds', 'P06a-S1-121', 'apply', '「嘿————，」破折号后多一个逗号，全批同类处不带逗号。'),
    ('ds', 'P06a-S1-105', 'reject',
     '主张把「船件」改成「飞船零件」。全库「船件」4 处、「飞船零件」0 处；「船件」是本作既有说法且读得通，改成词组反而更长。属风格偏好，不作修正。'),
    ('ds', 'P06a-S2-108', 'reject',
     '主张把「小狗」改成「小狗崽」。原文此处是 THAT TOO, PUP，PUP 在全库作「小狗」120 处、「小狗崽」33 处，两者都是既有译法；本行紧接瓦片身体那段调侃，「小狗」并无不妥。属风格偏好。'),
    ('ds', 'P06a-S2-107', 'reject',
     '与本表 gemini:P06a-104 同一行同一处（“UP”+“攻击”→UP+ATTACK），两路同报、改法逐字相同，取 gemini 条落地。'),
    ('gemini', 'P06a-101', 'reject',
     '主张把 PUPLOCK 音译成「帕普洛克船长」。全库仅此一处、词典无条目；PUPLOCK 是 pup（小狗）＋ Captain Harlock 的双关，音译会把 pup 那层丢掉，而那是笑点本身。已转为留置 R9M-901，与本批改动一并等待创译裁决。'),
    ('ds', 'P06a-S1-115', 'reject',
     '与本表 gemini:P06a-102 同一行同一处（狗头人→科博德），两路同报，取 gemini 条落地。'),
    ('gemini', 'P06a-102', 'apply',
     'KOBO 旧译「狗头人」残留，同 P06a-103；本行原文 KOBOLD 与上一处 KOBO 是同一词，一并改为「科博德」。'),
]

# 主代理自持的改动：路由的 findings 里没有对应条目（DS 的一段结果在一次并发重写中丢了
# 这条，但决定已经做出且已随 candidate21 落地），这里直接固定旧值与新值，保证重跑
# build_ledger 时台账稳定。
SELF = [
    ('R9M-903', 'A', 'term', 'SCe1a779c61c9843af', 'CAT:O5235f0bf107f29edd815',
     '  Mauser: [放轻松，执行绝密欧米茄协议任务的特工有权动用手头的一切手段，就算这些手段……通常不合法也一样。]',
     '同一个 OMEGA 词素在库内两种写法：词典条目名作「欧米茄」（欧米茄哥布林，词典 13 处），协议名却作「欧米伽」（仅 3 处）。全库「欧米茄」22 处对「欧米伽」3 处。按条目名与多数写法定为「欧米茄」。'),
]

HOLD = [
    ('R9M-901', 'B', 'term', 'SCcf94f585c1e0205e', 'SFWfbb3a40e26235475f2eb0739',
     '`PUPLOCK` 全库仅此一处，词典无条目。它是 pup（小狗）＋ Captain Harlock（宇宙海盗哈洛克）的双关，Gemini 主张音译「帕普洛克船长」，但音译会把 pup 这一层丢掉，而这一层正是笑点；保留英文又违反「正文不残留英文实词」。需与 LIGHTTAZER 一并做创译裁决，本批不改动。'),
    ('R9M-902', 'B', 'gameplay', 'SCde8682ffd4c1a8db', 'CAT:O48ed0e32b742e8e4575a',
     'UP+ATTACK 被译成「UP+攻击」，全库共 5 处（含本批已改的 1 处与 batch-06-part02 已改的 1 处）。其余分布在各区 root，不在本批范围，登记待后续批次一并归位。'),
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

    for fid, sev, cat, scene_id, rid, final, reason in SELF:
        if rid not in ROWS:
            raise SystemExit('unknown row ' + rid)
        scene_id, row = ROWS[rid]
        if row['current'] == final:
            raise SystemExit('no-op ' + rid)
        lines.append('	'.join((fid, 'R9M', sev, cat, scene_id, rid, 'apply', final, reason)))

    for fid, sev, cat, scene_id, rid, reason in HOLD:
        if rid not in ROWS:
            raise SystemExit('unknown row ' + rid)
        lines.append('\t'.join((fid, 'R9M', sev, cat, scene_id, rid, 'hold', '', reason)))

    (BASE / 'review/decisions.tsv').write_text('\n'.join(lines) + '\n', encoding='utf8')
    print(json.dumps({'decisions': len(lines) - 1,
                      'apply': sum(1 for p in PLAN if p[2] == 'apply') + len(SELF),
                      'reject': sum(1 for p in PLAN if p[2] == 'reject'),
                      'hold': len(HOLD)}, ensure_ascii=False))


if __name__ == '__main__':
    main()
