"""Write the r9 batch-09-part01 decision table."""
from pathlib import Path
import json

ROOT = Path(__file__).resolve().parents[4]
BASE = ROOT / 'localization/editorial/r9-polish/batch-09-part01'
ORDER = json.loads((BASE / 'orders/batch-09-part01.json').read_text('utf8'))
ROWS = {r['row_id']: (s['scene_id'], r) for s in ORDER['scenes'] for r in s['rows']}


def load(route):
    out = {}
    p = BASE / route / 'findings.jsonl'
    if p.exists():
        for line in p.read_text('utf8').splitlines():
            if line.strip():
                f = json.loads(line)
                out[f['finding_id']] = f
    return out


ROUTE = {'gemini': load('gemini'), 'ds': load('ds')}

# The nine LECT findings all rest on "this currency is always upper case". The
# English varies by line -- lower case here, title case there -- and the Chinese
# mirrors it, so the shape of the word is not a defect. Rejected as a family.
LECT = ['P09-0101', 'P09-0102', 'P09-0104', 'P09-0105', 'P09-0107', 'P09-0108',
        'P09-0109', 'P09-0110', 'P09-0111']

APPLY = [
    ('gemini', 'P09-0103',
     '按键名被汉化成「DOWN+攻击」，玩家实机上找不到这个键；同批 UP+ATTACK／DOWN+JUMP／SELECT 都原样保留。两路同报。'),
    ('gemini', 'P09-0106', 'hookshot 词典条目名是「钩爪」。两路同报。'),
    ('ds', 'P09-S-113', '宇航服与 R9 已定的 Cosmosuit＝宇宙服 不一致；本作触发条件就是 inCosmoSuit()。'),
    ('ds', 'P09-S-114', '同上一处，另一行。'),
    ('ds', 'P09-S-117', 'PSY 是「精神力」，同批另一行已作「精神力」；「超能力者」对应的是 Esper。'),
    ('ds', 'P09-S-119', '同句前半已作「驯兽电击枪」，后半却作「学员电击枪」；词典 TazerTrainee.name 是「见习」。'),
    ('ds', 'P09-S-122', 'Cosmosuit＝宇宙服；「星际服」是第三种写法。'),
    ('ds', 'P09-S-115', 'tiger 这里是打气的昵称，不是军衔；「猛将」与本线的见习生／菜鸟撞车。'),
    ('ds', 'P09-S-116', '「恢复精神」与 PSY＝精神力 撞车；同批 VitMeat／VitHam 都用「活力」。'),
    ('ds', 'P09-S-118', '导航图条目 DEPOT B 的既定中文名是「仓库B」，batch-04 毛鼠无线电同。'),
    ('ds', 'P09-S-123', '「锁铐」不是规范写法；同批对同一个词用「镣铐」。'),
    ('ds', 'P09-S-124', '测试串里英文名没译全；词典 ThrowKnife.name 是「小刀」。'),
]

DUP = [
    ('P09-S-104', 'gemini:P09-0103', '同一行同一处（DOWN+攻击），取另一条。'),
    ('P09-S-107', 'gemini:P09-0106', '同一行同一处（钩索／钩爪），取另一条。'),
]

HOLD = [
    ('R9M-1501', 'B', 'term', 'SC0bffef4b72d95f38', 'CAT:Off',
     '冲突待裁：词典 `CosmoBody.name` 的词条写作 STARSUIT，条目名是「星装」；而 R9 已在多处把 Cosmosuit 统一为「宇宙服」。两者是否同一件装备、以哪个为准，需要先定。'),
]


def main():
    lines = ['finding_id\troute\tseverity\tcategory\tscene_id\trow_id\tdecision\tfinal_zh\treason']
    seen, taken = set(), {}

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
            taken[rid] = key
        lines.append('\t'.join((key, route, sev, cat, scene_id, rid, decision, final, reason)))

    for route, items in (('gemini', APPLY), ('ds', APPLY)):
        for r, fid, reason in items:
            if r != route:
                continue
            f = ROUTE[route][fid]
            final = f.get('proposed_zh') or ''
            if not final:
                raise SystemExit('apply without text: %s:%s' % (route, fid))
            emit(route + ':' + fid, route, f.get('severity', ''), f.get('category', ''),
                 f['row_ids'][0], 'apply', final, reason)

    for fid in LECT:
        f = ROUTE['gemini'][fid]
        emit('gemini:' + fid, 'gemini', 'B', 'term', f['row_ids'][0], 'reject', '',
             'REJECT：英文原文这一行的货币名本身大小写就不统一（有的行是 lect，有的是 Lect），中文大小写是照源的，不是缺陷。要求一律改大写会与原文分叉。')

    for fid, dup, reason in DUP:
        f = ROUTE['ds'][fid]
        emit('ds:' + fid, 'ds', f.get('severity', ''), f.get('category', ''),
             f['row_ids'][0], 'reject', '', reason)

    occ, units = {}, {}
    for line in (ROOT / 'localization/catalog/occurrences.jsonl').read_text('utf8').splitlines():
        d = json.loads(line)
        occ[d['occurrence_id']] = d['unit_id']
    for line in (ROOT / 'localization/catalog/units.jsonl').read_text('utf8').splitlines():
        d = json.loads(line)
        units[d['id']] = d['source']
    for rid, (scene_id, row) in ROWS.items():
        cur = row['current'] or ''
        if cur == cur.rstrip() or rid in taken:
            continue
        uid = occ.get(rid.replace('CAT:', ''))
        src = units.get(uid) if uid else None
        if src is None:
            src = row['source'] or ''
        if src != src.rstrip():
            continue
        emit('R9M-' + rid, 'R9M', 'C', 'format', rid, 'apply', cur.rstrip(),
             '中文行尾多出半角空格，英文原文行尾没有（按 unit 原文核对）。只删空格。')

    for fid, f in ROUTE['ds'].items():
        if f.get('category') != 'format' or ('ds:' + fid) in seen:
            continue
        rid = f['row_ids'][0]
        key = taken.get(rid)
        reason = ('与本表 %s 同一行同一处（行尾空格），取先落地的条目。' % key) if key else \
                 'REJECT：本行英文原行行尾本身带空格，中文的行尾空格是排版镜像。'
        emit('ds:' + fid, 'ds', f.get('severity', ''), 'format', rid, 'reject', '', reason)

    (BASE / 'review/decisions.tsv').write_text('\n'.join(lines) + '\n', encoding='utf8')
    a = sum(1 for l in lines[1:] if l.split('\t')[6] == 'apply')
    print(json.dumps({'decisions': len(lines) - 1, 'apply': a,
                      'reject': sum(1 for l in lines[1:] if l.split('\t')[6] == 'reject')}, ensure_ascii=False))


if __name__ == '__main__':
    main()
