"""Write the r9 batch-09-part03 decision table.

Structure follows the earlier batches: apply the semantically verified findings
first (so a finding that also strips a stray trailing space keeps both edits in
one operation), then emit the mechanical R9M-* trailing-space rows for every
remaining row whose Chinese line ends in whitespace the English source lacks.
Every route finding must end up applied, held or rejected -- the script fails
instead of silently dropping one.
"""
from pathlib import Path
import json

ROOT = Path(__file__).resolve().parents[4]
BATCH = 'batch-09-part03'
BASE = ROOT / 'localization/editorial/r9-polish' / BATCH
ORDER = json.loads((BASE / 'orders' / (BATCH + '.json')).read_text('utf8'))
ROWS = {r['row_id']: (s['scene_id'], s) for s in ORDER['scenes'] for r in s['rows']}


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

# (route, finding_id, reason). Verified against the corpus by the main agent.
APPLY = [
    ('gemini', 'P09-0306',
     'BARKER 的词典条目名是「吠犬」（库内 40 处）；「吠叫者」全库仅此 1 处。两路同报。'),
    ('gemini', 'P09-0307',
     'kobold 的既有中文名是「科博德」（词典条目名、库内 99 处）；「狗头人」是旧译，属同一物种两种叫法。两路同报。'),
    ('gemini', 'P09-0315',
     'agent＝特工是 R2 裁决；库内 471 处作「特工」，「探员」仅 3 处。两路同报。'),
    ('gemini', 'P09-0308',
     'hookshot 的词典条目名是「钩爪」；batch-09-part02 已按同一口径改过 pak 侧同句，本行是 jar 侧副本。'),
    ('ds', 'P09-0309',
     '上一行已用「哎呀」译 Gee，本行英文换了感叹词 Why，现译连着两行「哎呀」抹平了麦森的换气；「那身行头」把指代接回上一句的道服。'),
    ('ds', 'P09-0304',
     '合句后「救了一大批他们」把代词挂在数量短语之后，中文不成句；上一行已点明救的是特工，删「他们」不丢信息。'),
    ('ds', 'P09-0305',
     '「把……你吞多深」把「把」的宾语拆到省略号两侧，中文「把」字句不能这样断开；并回后成句，挑逗语气不变。'),
    ('ds', 'P09-0306',
     '触发条件是 `!inCosmoSuit()`，指 Cosmosuit 这件装备，R9 已定「宇宙服」；同时删掉中文行尾多出的半角空格。'),
    ('ds', 'P09-0307',
     '同一俚称 cosmo fellas 库内 4 处作「太空伙计」，本行「宇宙来的家伙」是分叉写法，且易与宇宙服／宇宙头盔的物品名混读。'),
    ('ds', 'P09-0308',
     '本行已把下一物理行并进来，而英文该行行尾没有省略号；现译补的「……」与下一行开头的「……」连读成双省略号。'),
]

# Findings that are recorded but must not be applied. Reason is filled in when
# the entry is auto-rejected for a row that another decision already owns.
MANUAL_REJECT = {}


def main():
    lines = ['finding_id\troute\tseverity\tcategory\tscene_id\trow_id\tdecision\tfinal_zh\treason']
    seen, taken = set(), {}

    def emit(key, route, sev, cat, rid, decision, final, reason):
        if rid not in ROWS:
            raise SystemExit('unknown row %s from %s' % (rid, key))
        if key in seen:
            raise SystemExit('planned twice: ' + key)
        seen.add(key)
        scene_id, _scene = ROWS[rid]
        if decision == 'apply':
            row = _scene['rows'] and next(r for r in _scene['rows'] if r['row_id'] == rid)
            if not (row.get('current') or '').strip():
                raise SystemExit('blank line target ' + rid)
            if row['current'] == final:
                raise SystemExit('no-op ' + rid)
            if rid in taken:
                raise SystemExit('row already owned by %s: %s' % (taken[rid], rid))
            taken[rid] = key
        lines.append('\t'.join((key, route, sev, cat, scene_id, rid, decision, final, reason)))

    for route, fid, reason in APPLY:
        f = ROUTE[route].get(fid)
        if f is None:
            raise SystemExit('missing finding %s:%s' % (route, fid))
        final = f.get('proposed_zh') or ''
        if not final:
            raise SystemExit('apply without text: %s:%s' % (route, fid))
        emit(route + ':' + fid, route, f.get('severity', ''), f.get('category', ''),
             f['row_ids'][0], 'apply', final, reason)

    # Mechanical trailing-space check, verified against the English source.
    occ, units = {}, {}
    for line in (ROOT / 'localization/catalog/occurrences.jsonl').read_text('utf8').splitlines():
        d = json.loads(line)
        occ[d['occurrence_id']] = d['unit_id']
    for line in (ROOT / 'localization/catalog/units.jsonl').read_text('utf8').splitlines():
        d = json.loads(line)
        units[d['id']] = d['source']
    for rid, (scene_id, scene) in ROWS.items():
        row = next(r for r in scene['rows'] if r['row_id'] == rid)
        cur = row.get('current') or ''
        if cur == cur.rstrip() or rid in taken:
            continue
        uid = occ.get(rid.replace('CAT:', ''))
        src = units.get(uid) if uid else None
        if src is None:
            src = row.get('source') or ''
        if src != src.rstrip():
            continue
        emit('R9M-' + rid, 'R9M', 'C', 'format', rid, 'apply', cur.rstrip(),
             '中文行尾多出半角空格，英文原文行尾没有（按 unit 原文核对）。只删空格。')

    # Anything the routes proposed that is not already owned by a decision.
    leftover = []
    for route, findings in ROUTE.items():
        for fid, f in findings.items():
            key = route + ':' + fid
            if key in seen:
                continue
            rid = f['row_ids'][0]
            if rid in taken:
                emit(key, route, f.get('severity', ''), f.get('category', ''), rid, 'reject', '',
                     '与 %s 同一行同一处，取先落地的条目。' % taken[rid])
            elif key in MANUAL_REJECT:
                emit(key, route, f.get('severity', ''), f.get('category', ''), rid, 'reject', '',
                     MANUAL_REJECT[key])
            else:
                leftover.append(key)
    if leftover:
        raise SystemExit('unhandled route findings: ' + ', '.join(leftover))

    (BASE / 'review').mkdir(parents=True, exist_ok=True)
    (BASE / 'review/decisions.tsv').write_text('\n'.join(lines) + '\n', encoding='utf8')
    counts = {}
    for row in lines[1:]:
        decision = row.split('\t')[6]
        counts[decision] = counts.get(decision, 0) + 1
    print(json.dumps({'decisions': len(lines) - 1, **counts}, ensure_ascii=False))


if __name__ == '__main__':
    main()
