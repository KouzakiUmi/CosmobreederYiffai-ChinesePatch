"""Write the r9 batch-07-part02 decision table.

Both routes worked the same twelve ending scenes and landed on the same rows
often enough that the table resolves overlaps by row rather than by hand: the
Gemini entry is applied first and the DS entry for the same row is recorded as
rejected-because-duplicate, which keeps every route finding accounted for.
"""
from pathlib import Path
import json

ROOT = Path(__file__).resolve().parents[4]
BASE = ROOT / 'localization/editorial/r9-polish/batch-07-part02'
ORDER = json.loads((BASE / 'orders/batch-07-part02.json').read_text('utf8'))
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

# Route findings in the order they should be tried. Text comes from the
# route's own proposed_zh; the reason here is why the change is justified.
ORDER_APPLY = [
    ('gemini', 'P07-202', '清嗓打断处用半角连字符；中文破折号是全角双线，12px 下一个单横会被读成符号残留。'),
    ('gemini', 'P07-207', '男线同型位置同改。'),
    ('gemini', 'P07-204', '惊叹句首用单字短破折号「—」，全批其它被打断处都是「——」，统一。'),
    ('gemini', 'P07-209', '改口处（wake up faste- I mean）用单字短破折号，同前统一为「——」。'),
    ('gemini', 'P07-203',
     '「连把我锁起来都懒得」把 bother 直搬成句末「懒得」，中文缺宾语读不成句；原文 didn\'t even bother chaining me up。'),
    ('ds', 'P07-S2-104',
     'HECKING 是刻意弱化的脏话，现译升格成「他妈的」；同一批 heck 系另外 4 处都作「到底／搞什么／坏了」。按原文强度收回去。'),
    ('ds', 'P07-S2-110',
     '「像当飞机杯那样用」两个动词叠着不成词；且否定被逗号甩到句尾，「不*好玩*」读成对前文的追加否认，与 Not that it wasn\'t 的双重否定不合。'),
    ('ds', 'P07-S2-113',
     'a little ruffer 是「还颠一点」；现译「颠得厉害」把程度抬高了，与原文的轻描淡写不符。'),
    ('ds', 'P07-S2-114',
     'grrrrl 是拉长的低吼写法，现译「姑娘」抹平了；本作既有的拉长处理用破折号（如「还——是说」），沿用。'),
]

# Findings rejected on evidence or because another entry already took the row.
REJECT = [
    ('gemini', 'P07-201', 'REJECT：与本表 ds:P07-S2-101 同一行同一处（行尾空格），取 DS 条落地。'),
]


def main():
    lines = ['finding_id\troute\tseverity\tcategory\tscene_id\trow_id\tdecision\tfinal_zh\treason']
    seen = set()
    taken = {}

    def emit(key, route, sev, cat, rid, decision, final, reason):
        if rid not in ROWS:
            raise SystemExit('unknown row %s from %s' % (rid, key))
        if key in seen:
            raise SystemExit('planned twice: ' + key)
        if decision == 'apply' and rid in taken:
            raise SystemExit('row already applied by %s: %s' % (taken[rid], rid))
        seen.add(key)
        scene_id, row = ROWS[rid]
        if decision == 'apply':
            if not (row['current'] or '').strip():
                raise SystemExit('blank line target ' + rid)
            if row['current'] == final:
                raise SystemExit('no-op ' + rid)
            taken[rid] = key
        lines.append('\t'.join((key, route, sev, cat, scene_id, rid, decision, final, reason)))

    # Trailing-space family: only where the English line does not end in a space
    # of its own -- otherwise the space mirrors the source and stays.
    for fid, f in ROUTE['gemini'].items():
        if f.get('category') != 'format' or fid in ('P07-201', 'P07-202', 'P07-204', 'P07-207', 'P07-209'):
            continue
        rid = f['row_ids'][0]
        row = ROWS[rid][1]
        if (row['source'] or '') != (row['source'] or '').rstrip():
            raise SystemExit('source also ends in a space: ' + rid)
        emit('gemini:' + fid, 'gemini', 'C', 'format', rid, 'apply',
             (row['current'] or '').rstrip(),
             '译文行尾多一个半角空格，英文原行行尾没有；该空格参与行宽测量。只删空格。')
    for fid, f in ROUTE['ds'].items():
        if f.get('category') != 'format':
            continue
        rid = f['row_ids'][0]
        row = ROWS[rid][1]
        if (row['source'] or '') != (row['source'] or '').rstrip():
            raise SystemExit('source also ends in a space: ' + rid)
        if rid in taken:
            emit('ds:' + fid, 'ds', 'C', 'format', rid, 'reject', '',
                 '与本表 %s 同一行同一处（行尾空格），两路同报，取先落地的条目。' % taken[rid])
            continue
        emit('ds:' + fid, 'ds', 'C', 'format', rid, 'apply',
             (row['current'] or '').rstrip(),
             '译文行尾多出半角空格，英文原行行尾没有。只删空格。')

    for route, fid, reason in ORDER_APPLY:
        if fid not in ROUTE[route]:
            raise SystemExit('no such finding: %s:%s' % (route, fid))
        f = ROUTE[route][fid]
        final = f.get('proposed_zh') or ''
        if not final:
            raise SystemExit('apply without text: %s:%s' % (route, fid))
        emit(route + ':' + fid, route, f.get('severity', ''), f.get('category', ''),
             f['row_ids'][0], 'apply', final, reason)

    for route, fid, reason in REJECT:
        f = ROUTE[route][fid]
        emit(route + ':' + fid, route, f.get('severity', ''), f.get('category', ''),
             f['row_ids'][0], 'reject', '', reason)

    (BASE / 'review/decisions.tsv').write_text('\n'.join(lines) + '\n', encoding='utf8')
    applies = sum(1 for l in lines[1:] if l.split('\t')[6] == 'apply')
    print(json.dumps({'decisions': len(lines) - 1, 'apply': applies,
                      'reject': len(lines) - 1 - applies}, ensure_ascii=False))


if __name__ == '__main__':
    main()
