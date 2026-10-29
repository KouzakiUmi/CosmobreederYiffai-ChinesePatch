"""Write the r9 batch-08-part02 decision table.

One route returned a single finding and the other twenty-six, which is the
widest split in the round so far; both landed on the same untranslated
equipment name, so that one is taken from the route that cited the dictionary.
"""
from pathlib import Path
import json

ROOT = Path(__file__).resolve().parents[4]
BASE = ROOT / 'localization/editorial/r9-polish/batch-08-part02'
ORDER = json.loads((BASE / 'orders/batch-08-part02.json').read_text('utf8'))
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

APPLY = [
    ('gemini', 'P08-0201',
     'Cosmohelm 整词未译。词典 `CosmoHead.desc` 作「宇宙头盔」，另一处雄猫对白也作「宇宙头盔」；两路同报。'),
    ('ds', 'P08-S2-108',
     '「我当时可上了大新闻」不成话：「上新闻」不能带宾语。与 batch-08-part01 的 ds:P08-S-112 是同一句在另一场的拷贝。'),
    ('ds', 'P08-S2-116',
     '原文 takin\' one Omegobin after another 的 take 在这里是「受、挨」；现译「吃下」把欧米茄哥布林写成了食物，施受关系错。'),
    ('ds', 'P08-S2-121',
     'Fenfen council 同型男线三句与词典 `CosmoCardStarkill.desc` 均作「议会」；本行「理事会」是孤例。'),
    ('ds', 'P08-S2-123',
     'strike out 是「出手／先动手」；现译「反击」把它读成还手，而原文说的是没人敢先动。'),
    ('ds', 'P08-S2-125',
     '同一场前文已作「议会」，本行却作「议员」，指称同一批人却用了不同词。'),
    ('ds', 'P08-S2-126',
     '囚禁 Traeh 的那座建筑，全库「囚牢」6 处、「牢笼」1 处；且女线同句作「囚牢」。'),
]

REJECT = [
    ('ds', 'P08-S2-109',
     'REJECT：主张把「光电击枪」改成「轻型电击枪」。说法本身有道理（light 指重量，不是光），但 LIGHTTAZER 的中文名至今未终裁、库内并存三种写法，改名要连动全部含该武器的行与词典条目名。本批不动，见 R9M-1201。'),
    ('ds', 'P08-S2-111',
     'REJECT：与本表 gemini:P08-0201 同一行同一处（Cosmohelm），两路同报，取 gemini 条的措辞落地。'),
]

HOLD = [
    ('R9M-1201', 'B', 'term', 'SC6c92dcf306eb4565', 'CAT:O472effdb44387dbb2253',
     'DS 报「光电击枪」应为「轻型电击枪」，依据是 light 指重量。但 LIGHTTAZER 的中文名至今未终裁，库内三种写法并存，此前已定「不要单点改」，改名要连动全部含该武器的行与词典条目名，本批不改。'),
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

    for route, fid, reason in APPLY:
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

    for fid, sev, cat, scene_id, rid, reason in HOLD:
        emit(fid, 'R9M', sev, cat, rid, 'hold', '', reason)

    for route in ('gemini', 'ds'):
        for fid, f in ROUTE[route].items():
            if f.get('category') != 'format':
                continue
            rid = f['row_ids'][0]
            row = ROWS[rid][1]
            if (row['source'] or '') != (row['source'] or '').rstrip():
                raise SystemExit('source also ends in a space: ' + rid)
            if rid in taken:
                emit(route + ':' + fid, route, 'C', 'format', rid, 'reject', '',
                     '与本表 %s 同一行同一处（行尾空格），取先落地的条目。' % taken[rid])
                continue
            emit(route + ':' + fid, route, 'C', 'format', rid, 'apply',
                 (row['current'] or '').rstrip(),
                 '译文行尾多出半角空格，英文原行行尾没有；该空格参与行宽测量。只删空格。')

    (BASE / 'review/decisions.tsv').write_text('\n'.join(lines) + '\n', encoding='utf8')
    applies = sum(1 for l in lines[1:] if l.split('\t')[6] == 'apply')
    print(json.dumps({'decisions': len(lines) - 1, 'apply': applies,
                      'reject': sum(1 for l in lines[1:] if l.split('\t')[6] == 'reject'),
                      'hold': len(HOLD)}, ensure_ascii=False))


if __name__ == '__main__':
    main()
