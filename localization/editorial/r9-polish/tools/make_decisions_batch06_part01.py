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
    ('ds', 'P06a-S1-101', 'reject',
     '主张把「卡片正面还是哪儿」改成「还是什么」。原句「是正面还是哪儿」在中文里是可读的口语选择问句，改后反而更生硬；属风格偏好，不作修正。'),
    ('ds', 'P06a-S2-102', 'reject',
     '主张把「一个白热的光点」改成「白得发烫的光点」。WHITE HOT 在此是扫描仪显示上的白炽点，「白热」是既有译法且读得通；改后把物理描述换成触觉比喻，属风格偏好。'),
    ('ds', 'P06a-S2-105', 'apply',
     '本行是完整独立陈述而句末无标点；下一行「吃完这么大一块……」是另起一句（英文 AFTER GORGING ON THAT... 亦另起），不补会把两句黏成一句。'),
    ('ds', 'P06a-S2-106', 'apply',
     '「……严重违禁品」句末缺标点，直接接下一行「这是黑市生物加密货币」，读起来像一句没说完的话被掐断；补句号恢复「定罪→解释是什么」两步递进。'),
    ('ds', 'P06a-S2-107', 'apply',
     '同一个 OMEGA 词素在库内两种写法：词典条目名作「欧米茄」（欧米茄哥布林，词典 13 处），协议名却作「欧米伽」（仅 3 处）。全库「欧米茄」22 处对「欧米伽」3 处。按条目名与多数写法定为「欧米茄」。'),
    ('gemini', 'P06a-101', 'reject',
     '主张把 PUPLOCK 音译成「帕普洛克船长」。全库仅此一处、词典无条目；PUPLOCK 是 pup（小狗）＋ Captain Harlock 的双关，音译会把 pup 那层丢掉，而那是笑点本身。已转为留置 R9M-901，与本批改动一并等待创译裁决。'),
    ('gemini', 'P06a-102', 'apply',
     'KOBO 旧译「狗头人」残留，同 P06a-103；本行原文 KOBOLD 与上一处 KOBO 是同一词，一并改为「科博德」。'),
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

    for fid, sev, cat, scene_id, rid, reason in HOLD:
        if rid not in ROWS:
            raise SystemExit('unknown row ' + rid)
        lines.append('\t'.join((fid, 'R9M', sev, cat, scene_id, rid, 'hold', '', reason)))

    (BASE / 'review/decisions.tsv').write_text('\n'.join(lines) + '\n', encoding='utf8')
    print(json.dumps({'decisions': len(lines) - 1,
                      'apply': sum(1 for p in PLAN if p[2] == 'apply'),
                      'reject': sum(1 for p in PLAN if p[2] == 'reject'),
                      'hold': len(HOLD)}, ensure_ascii=False))


if __name__ == '__main__':
    main()
