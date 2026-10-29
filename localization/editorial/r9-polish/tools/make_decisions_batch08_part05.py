"""Write the r9 batch-08-part05 decision table.

Both routes ran the full part this time and converged on the same five rows --
council, Elves, Cosmohelm, Cosmosuit and a half-width ellipsis -- so the table
takes the first route's wording there and records the other's as duplicates.
Trailing spaces are swept from the unit sources, as in the previous two parts.
"""
from pathlib import Path
import json

ROOT = Path(__file__).resolve().parents[4]
BASE = ROOT / 'localization/editorial/r9-polish/batch-08-part05'
ORDER = json.loads((BASE / 'orders/batch-08-part05.json').read_text('utf8'))
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

GEM = [
    ('P08-0501', '本行作「理事会」，同一场另两行与全库口径都是「议会」（Fenfen council）。'),
    ('P08-0502', 'Elves 整词未译。全库一律作「精灵」，男线同型对白也作「精灵」。'),
    ('P08-0503', '同一场里 council 前文作「议会」，本行却作「Fenfen理事会」；男线同句作「Fenfen议会」。'),
    ('P08-0504', 'Cosmohelm 整词未译；词典 `CosmoHead.desc` 作「宇宙头盔」，另一处雄猫对白同。'),
    ('P08-0505', 'Cosmosuit 整词未译，词典 `SpecialZentaiSuit` 条目名即「宇宙服」；同时行末半角三点改全角省略号。'),
]

DS = [
    ('P08-S5-101', '同一场把 wrestle／tussling／wrestling 分别译成「摔跤」与「扭打」，指同一件事却两个词；本行改「扭打」。'),
    ('P08-S5-102', '原文 manhood 是绕开的说法，现译「鸡巴」把它直白化；而同一场另一行 thick cock 才是原文直白处。委婉被升格会把这两处的强弱对比压平。'),
    ('P08-S5-104', '同一行里前半用「它们」指那批怪物，后半改口「他们」，指称不一致。'),
    ('P08-S5-113', '本场 alien creature／aliens 有「外星生物」与「异星生物」两套说法，指同一批东西。'),
    ('P08-S5-121', '原文 beat him off 说的是把人打退，现译加了「用手」这个原文没有的细节。'),
]

DUP = [
    ('P08-S5-112', 'gemini:P08-0501', '同一行同一处（理事会／议会），取另一条。'),
    ('P08-S5-117', 'gemini:P08-0502', '同一行同一处（Elves），取另一条。'),
    ('P08-S5-118', 'gemini:P08-0503', '同一行同一处（Fenfen理事会），取另一条。'),
    ('P08-S5-125', 'gemini:P08-0504', '同一行同一处（Cosmohelm），取另一条。'),
    ('P08-S5-126', 'gemini:P08-0505', '同一行同一处（Cosmosuit）；另一条把词与行末标点一起处理。'),
    ('P08-S5-127', 'gemini:P08-0505', '同一行同一处（行末半角三点）；另一条已一并处理。'),
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

    for route, items in (('gemini', GEM), ('ds', DS)):
        for fid, reason in items:
            f = ROUTE[route][fid]
            final = f.get('proposed_zh') or ''
            if not final:
                raise SystemExit('apply without text: %s:%s' % (route, fid))
            emit(route + ':' + fid, route, f.get('severity', ''), f.get('category', ''),
                 f['row_ids'][0], 'apply', final, reason)

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

    # Account for every trailing-space finding the other route filed: each is
    # either the row just swept or a genuine mirror.
    for fid, f in ROUTE['ds'].items():
        if f.get('category') != 'format' or ('ds:' + fid) in seen:
            continue
        rid = f['row_ids'][0]
        if rid in taken:
            reason = '与本表 %s 同一行同一处（行尾空格），取先落地的条目。' % taken[rid]
        else:
            reason = 'REJECT：本行英文原行行尾本身带空格，中文的行尾空格是排版镜像，不删。'
        emit('ds:' + fid, 'ds', f.get('severity', ''), 'format', rid, 'reject', '', reason)

    (BASE / 'review/decisions.tsv').write_text('\n'.join(lines) + '\n', encoding='utf8')
    a = sum(1 for l in lines[1:] if l.split('\t')[6] == 'apply')
    print(json.dumps({'decisions': len(lines) - 1, 'apply': a,
                      'reject': sum(1 for l in lines[1:] if l.split('\t')[6] == 'reject')}, ensure_ascii=False))


if __name__ == '__main__':
    main()
