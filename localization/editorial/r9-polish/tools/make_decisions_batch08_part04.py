"""Write the r9 batch-08-part04 decision table.

The second route reached all sixteen scenes; the first only managed the first
eight before terminating, and two re-dispatches of the other half also died
without writing anything, so scenes nine through sixteen are single-route.

Two of the route findings are corrected here rather than taken as given, both
because an earlier batch already settled the wording: the same "they did as
Traeh commanded" line was fixed in the jar copy in part 1 and reads
"DUTY_PLACEHOLDER", so the patch-pak copy takes that same wording; and a
proposal to render feral as one variant would undo the term part 3 chose.
"""
from pathlib import Path
import json

ROOT = Path(__file__).resolve().parents[4]
BASE = ROOT / 'localization/editorial/r9-polish/batch-08-part04'
ORDER = json.loads((BASE / 'orders/batch-08-part04.json').read_text('utf8'))
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


ROUTE = {'ds': load('ds'), 'gemini-s1': load('gemini-s1'), 'gemini': load('gemini')}


def main():
    lines = ['finding_id\troute\tseverity\tcategory\tscene_id\trow_id\tdecision\tfinal_zh\treason']
    seen = set()
    taken = {}

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

    def from_route(route, fid, reason, override=None):
        f = ROUTE[route][fid]
        final = override if override is not None else (f.get('proposed_zh') or '')
        if not final:
            raise SystemExit('apply without text: %s:%s' % (route, fid))
        emit(route + ':' + fid, route, f.get('severity', ''), f.get('category', ''),
             f['row_ids'][0], 'apply', final, reason)

    # council, reported by both routes for the same row; the first half's
    # version wins because it is the one that also cites the neighbouring lines.
    from_route('gemini-s1', 'P08-04A01',
               '本行作「理事会」，而同一场另两行与全库口径都是「议会」（Fenfen council）。两路同报。')
    d101 = ROUTE['ds']['P08-S4-101']
    emit('ds:P08-S4-101', 'ds', 'B', 'term', d101['row_ids'][0], 'reject', '',
         '与本表 gemini-s1:P08-04A01 同一行同一处（理事会／议会），两路同报，取另一条落地。')

    from_route('gemini-s1', 'P08-04A02',
               '条件从句「也许……若能更快应对」与下一行「就本可以阻止……」是同一句，本行末尾缺承接逗号。')

    from_route('ds', 'P08-S4-104',
               '「争着早点出任、任务了」把 get sent on a mission 拆成了两个不成立的词，「出任」不接「任务」。')

    from_route('ds', 'P08-S4-105',
               'nubs 在本行作「肉突」，同一场另一行与前面批次已定的写法都是「凸粒」。')

    from_route('ds', 'P08-S4-106',
               'bulbus glandis 在本行作「龟头球」，同一场另有「肉结」「结」两种写法；batch-08-part03 落地的是「肉结」。统一为「肉结」。')

    # Same sentence as part 1, but that fix landed in the jar copy while this
    # row is the patch-pak copy that overrides it -- so it needs the same fix.
    from_route('ds', 'P08-S4-103',
               '与前一批同一句（They did as Traeh commanded）。前批落在 jar 一侧，本行是 pak 一侧的同句拷贝，「其」同样没有先行词。按前批已定的措辞改为「它」。',
               override='lang(Fox): Traeh吩咐什么，它便做什么！')

    d107 = ROUTE['ds']['P08-S4-107']
    emit('ds:P08-S4-107', 'ds', 'B', 'term', d107['row_ids'][0], 'reject', '',
         'REJECT：主张把「变成野兽了」改成「变成兽形了」，理由是同一句在 part03 已落地。但 part03 落地的是「野兽」不是「兽形」——那条改的正是「野性兽人」→「野兽」。本行已是「野兽」，与 part03 一致，改了反而分叉。')

    # Trailing spaces whose English source has none, by unit source.
    occ, units = {}, {}
    for line in (ROOT / 'localization/catalog/occurrences.jsonl').read_text('utf8').splitlines():
        d = json.loads(line)
        occ[d['occurrence_id']] = d['unit_id']
    for line in (ROOT / 'localization/catalog/units.jsonl').read_text('utf8').splitlines():
        d = json.loads(line)
        units[d['id']] = d['source']
    swept = 0
    for rid, (scene_id, row) in ROWS.items():
        cur = row['current'] or ''
        if cur == cur.rstrip() or rid in taken:
            continue
        uid = occ.get(rid.replace('CAT:', ''))
        src = units.get(uid) if uid else None
        if src is None:
            # Jar-side rows carry no catalog occurrence; their order-file
            # source does preserve the original trailing whitespace.
            src = row['source'] or ''
        if src != src.rstrip():
            continue
        emit('R9M-' + rid, 'R9M', 'C', 'format', rid, 'apply', cur.rstrip(),
             '中文行尾多出半角空格，英文原文行尾没有（按 catalog 的 unit 原文核对）。只删空格。')
        swept += 1

    d102 = ROUTE['ds']['P08-S4-102']
    emit('ds:P08-S4-102', 'ds', 'B', 'term', d102['row_ids'][0], 'reject', '',
         '同场 lighttazer 三种写法并存，主张统一为「光电击枪」。但该武器中文名未终裁，选边等于替全局定名。本批不改，见 R9M-1401。')
    emit('R9M-1401', 'R9M', 'B', 'term', d102['row_ids'][0], 'hold', '',
         'DS 报本行 lighttazer 作「光刃电击器」，同场与另几批作「光电击枪」，主张同场统一。但 LIGHTTAZER 的中文名至今未终裁、库内三种写法并存，选任何一种都等于替全局定名。本批不改。')

    (BASE / 'review/decisions.tsv').write_text('\n'.join(lines) + '\n', encoding='utf8')
    a = sum(1 for l in lines[1:] if l.split('\t')[6] == 'apply')
    print(json.dumps({'decisions': len(lines) - 1, 'apply': a,
                      'reject': sum(1 for l in lines[1:] if l.split('\t')[6] == 'reject'),
                      'hold': 1}, ensure_ascii=False))


if __name__ == '__main__':
    main()
