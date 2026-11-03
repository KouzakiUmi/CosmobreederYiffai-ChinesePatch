"""Write the r9 batch-09-part04 decision table.

Applies the verified findings first, then the mechanical R9M-* trailing-space
rows for the remaining rows. Two findings are decided against the routes:
`fancy chips` keeps the majority form (3 of 4 parallel variants), and one apply
reuses the wording already landed for the same sentence in batch-09-part02 so
the two archive sides stay identical.
"""
from pathlib import Path
import json

ROOT = Path(__file__).resolve().parents[4]
BATCH = 'batch-09-part04'
BASE = ROOT / 'localization/editorial/r9-polish' / BATCH
ORDER = json.loads((BASE / 'orders' / (BATCH + '.json')).read_text('utf8'))
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

# route, finding_id, reason, and optional overrides for the applied text/severity.
APPLY = [
    ('ds', 'P09-0402',
     '按键名属受保护的玩法标记，R9 batch-01 已定「UP+ATTACK 原样保留」；英文源行本来就是 DOWN+ATTACK。'
     '两路同报。级别按 format 记，不改玩法语义。', None, 'B'),
    ('ds', 'P09-0401',
     'kobold 的词典条目名是「科博德」（库内 99 处）；「狗头人」是另一套奇幻译名，读者会当成两种怪。两路同报。'),
    ('ds', 'P09-0407',
     '道具名按词典条目 SpecialHookshot 的中文名「钩爪」（库内 6 处）；「钩索」是早期草稿批注的写法，'
     'batch-09-part02 已按条目名改过 pak 侧同句。两路同报。'),
    ('ds', 'P09-0408',
     'agent＝特工是 R2 裁决；同句的 datadf 版已作「特工」，「探员」全库仅 3 处。两路同报。'),
    ('ds', 'P09-0403',
     '「没开发《宇宙育种者伊吠》苦」缺谓语中心、不成句；本行沿用 batch-09-part02 对同一句已落地并复核过的措辞，'
     '让 jar／pak 两侧读起来一致。', '  * 可没开发《宇宙育种者伊吠》那么苦，不过也挺累人！', None),
    ('ds', 'P09-0404',
     '原句是赶人（Why don\'t you take off next）；现译把 next 硬挂成时间状语又接「你怎么不走人呢」，句子立不起来。'
     'datadf 版同句作「还不快滚」，可见意思本身清楚，只有这一版硬直译。'),
    ('ds', 'P09-0405',
     '这名俘虏被锁在牢里（同段索要钥匙、说「把我关在这里」），free me 是「放我出去」；「放开我」指松开抓握，与场景不符。'),
    ('ds', 'P09-0406',
     '上一行是「几个当地人卑鄙地偷袭」，指代对象是人，用「它们」把施事者错指成非人；同段 sfw 版即作「他们」。'),
    ('ds', 'P09-0409',
     'tazer 在本作以「电击枪」为主（库内 92 处对「电击器」10 处），「驯兽／见习电击枪」系列也作此写法。'),
    ('ds', 'P09-0410',
     '原意是门已开、劝主角去找别的待救者；现译「去找其他人救」最自然的读法是「找人来救我」，意思反了。'),
    ('ds', 'P09-0411',
     '「在……击中时」缺被动标记，主语变成光击枪自己；补一个「被」即可，不改 LIGHTTAZER 的命名（该名仍未终裁）。'),
    ('ds', 'P09-0413',
     '「有点偷看了」把程度副词与完成态硬拼；四个平行变体里三处都作「卫星链路」，因此只改动词、不动名词。'),
]

MANUAL_REJECT = {
    'ds:P09-0412':
        '「fancy chips」在四个平行变体里三处作「花哨芯片」、一处作「高级芯片」；只改其中一处会让同一句的分叉变多，'
        '而「fancy＝花哨」本身是可辩护的直译。整句口径待全库终裁，本批不动。',
}


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
            if not (row.get('current') or '').strip():
                raise SystemExit('blank line target ' + rid)
            if row['current'] == final:
                raise SystemExit('no-op ' + rid)
            if rid in taken:
                raise SystemExit('row already owned by %s: %s' % (taken[rid], rid))
            taken[rid] = key
        lines.append('\t'.join((key, route, sev, cat, scene_id, rid, decision, final, reason)))

    for entry in APPLY:
        route, fid, reason = entry[0], entry[1], entry[2]
        final_override = entry[3] if len(entry) > 3 else None
        sev_override = entry[4] if len(entry) > 4 else None
        if (route + ':' + fid) in MANUAL_REJECT:
            continue
        f = ROUTE[route].get(fid)
        if f is None:
            raise SystemExit('missing finding %s:%s' % (route, fid))
        final = final_override if final_override is not None else (f.get('proposed_zh') or '')
        if not final:
            raise SystemExit('apply without text: %s:%s' % (route, fid))
        emit(route + ':' + fid, route, sev_override or f.get('severity', ''), f.get('category', ''),
             f['row_ids'][0], 'apply', final, reason)

    occ, units = {}, {}
    for line in (ROOT / 'localization/catalog/occurrences.jsonl').read_text('utf8').splitlines():
        d = json.loads(line)
        occ[d['occurrence_id']] = d['unit_id']
    for line in (ROOT / 'localization/catalog/units.jsonl').read_text('utf8').splitlines():
        d = json.loads(line)
        units[d['id']] = d['source']
    for rid, (scene_id, row) in ROWS.items():
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

    leftover = []
    for route, findings in ROUTE.items():
        for fid, f in findings.items():
            key = route + ':' + fid
            if key in seen:
                continue
            rid = f['row_ids'][0]
            if key in MANUAL_REJECT:
                emit(key, route, f.get('severity', ''), f.get('category', ''), rid, 'reject', '',
                     MANUAL_REJECT[key])
            elif rid in taken:
                emit(key, route, f.get('severity', ''), f.get('category', ''), rid, 'reject', '',
                     '与 %s 同一行同一处，取先落地的条目。' % taken[rid])
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
