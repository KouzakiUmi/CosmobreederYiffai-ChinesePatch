"""Write the r9 batch-09-part02 decision table."""
from pathlib import Path
import json

ROOT = Path(__file__).resolve().parents[4]
BASE = ROOT / 'localization/editorial/r9-polish/batch-09-part02'
ORDER = json.loads((BASE / 'orders/batch-09-part02.json').read_text('utf8'))
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

APPLY = [
    ('gemini', 'P09-0201', 'hookshot 词典条目名是「钩爪」。两路同报。'),
    ('gemini', 'P09-0202', 'DEPOT B 的既定中文名是「仓库B」。两路同报。'),
    ('gemini', 'P09-0203', '道具描述模板里英文名没译全；同一模板的上一件已作「[镐子描述]」。两路同报。'),
    ('gemini', 'P09-0204', '「并且你也许会感到某种力量流经你」把 and you might feel... 逐词搬下来，中文不成话；女线同一句是自然写法。'),
    ('ds', 'P09-S2-102', '「没开发《宇宙育种者伊吠》苦」把 not nearly as hard as 的比较标记丢了，读成「没开发游戏很苦」，意思反了。'),
    ('ds', 'P09-S2-106', '同一件武器在本场作「电击枪」，与已定的「驯兽／见习电击枪」系列不一致，且原文是 tazer 不是 gun。'),
    ('ds', 'P09-S2-107', '同一句里 senior top agent 译成「资深上位特工」，而男线另一版作「资深精英」；本行改与已定口径一致。'),
    ('ds', 'P09-S2-108', 'spacesuit 在本场受 `inCosmoSuit()` 限定，应为已定的「宇宙服」。'),
    ('ds', 'P09-S2-109', 'meat／meet 的双关在「我们还会再见」里没了；改用既能听成见面又能听成肉的说法。'),
    ('ds', 'P09-S2-111', 'psychic 在本作是「超能力者」，不是「通灵者」。'),
    ('ds', 'P09-S2-112', 'repair bay 本场另作「维修区」，同一处设施两个名字；统一为「修理舱」。'),
    ('ds', 'P09-S2-114', '「就像他那样做的」缺中心语，读不成句；原文指照他那个样子办。'),
]

DUP = [
    ('P09-S2-104', 'gemini:P09-0201', '同一行同一处（钩索／钩爪），取另一条。'),
    ('P09-S2-113', 'gemini:P09-0203', '同一行同一处（ThrowKnife），取另一条。'),
    ('P09-S2-110', 'gemini:P09-0202', '同一行同一处（B号仓库／仓库B），两路同报，取另一条。'),
]

# STARSUIT stays a hold; both routes agree to record it without proposing.
HOLD = []


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

    for route, fid, reason in APPLY:
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
