"""Write the r9 batch-08-part01 decision table.

Two families dominate and both are resolved by row rather than by hand:
the trailing-space rows, where the two routes filed overlapping lists, and the
six-plus-six Fox speech that differs between the female and male lines without
either version being wrong.
"""
from pathlib import Path
import json

ROOT = Path(__file__).resolve().parents[4]
BASE = ROOT / 'localization/editorial/r9-polish/batch-08-part01'
ORDER = json.loads((BASE / 'orders/batch-08-part01.json').read_text('utf8'))
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
    ('ds', 'P08-S-112',
     '「我当时可上了大新闻」不成话：「上新闻」不能带「我」作宾语。原文 it was big news。'),
    ('ds', 'P08-S-116',
     '原文 barkers kept goin\' for my tail 说的是尾巴；现译改成「屁股」并把性意味加进来，是尺度加码，同一场后文仍作「啃咬我的毛」。改回尾巴。'),
    ('ds', 'P08-S-120',
     '「纵然或许强大」两个让步副词叠在一起；原文 Powerful though ... may have been 只一层让步。'),
    ('ds', 'P08-S-121',
     '「Traeh吩咐什么，其便做什么」的「其」在此没有先行词，读者会当成另一个人；原文 They did as Traeh commanded 的 They 指前面的那些存在。'),
    ('ds', 'P08-S-126',
     '「被挨操」把被动标记「被」和「挨」叠用，中文不成词；原文 how amazing it felt to be used。'),
]

REJECT = [
    ('gemini', 'P08-0107',
     'REJECT：主张把「-嘿……」改成「——嘿……」。原文这两行是跨行断词（上一行 "like mine o-"，本行 "-hey..."），行首那个连字符就是原文的断词符，属排版镜像，不能改成破折号。'),
    ('ds', 'P08-S-101',
     'REJECT：主张把「让心神向内」改成「将心神转向内在」，理由是缺中心动词。但「让」就是这句的动词，「让心神向内，去见证……」读得通；且女线六个 root（f_AgentFZ1～FZ6）全部是这一句，男线六个（m_AgentMZ1～MZ6）全部是「将心神转向内在」，两边各自内部一致。只改其中两行会打破女线的一致性。Gemini 路独立判为保留。'),
    ('ds', 'P08-S-106',
     'REJECT：与 P08-S-101 同一句的女线另一场，理由同上。'),
    ('ds', 'P08-S-104',
     'REJECT：主张在「挡不住那些陡然壮了胆的生灵」句末补逗号。下一行「连我们求饶的呼声也得不到半点回应。」是独立的完整句（自带主语与谓语），不是这一行的续写；补逗号反而会把两句粘成一句。'),
    ('ds', 'P08-S-109',
     'REJECT：主张删掉本行两个「唔」。这一段说话人醉着，原文靠 s→sh 的发音滑移（shleep／thish／exshtra）表达，同场下一行已用「窝」承接；本行的「唔」是同一装置的另一种拼法。删掉会把这段的醉态抹平。整场怎么拼另见 R9M-1102。'),
    ('ds', 'P08-S-115',
     'REJECT：主张在「或许，你想上一堂关于“力量”的课」句末补逗号。下一行「再由你背给我听，如何？」同样是独立句，中文两行各自成立，不需要承接逗号。'),
]

HOLD = [
    ('R9M-1101', 'C', 'term', 'SC7c9d71ffa59dae21', 'CAT:O818d47ead285c8c06d70',
     'DS 报「虚拟科博」与词典条目「科博德」不一致，但同时说明词典里另有以「科博」为词干的条目名（KoboBody→科博服、TazerKobo→科博爪），无法证明此处必须扩写。要不要把「科博」单列为可独立使用的短词干，牵涉全部带 Kobo 的条目，本批不改。'),
    ('R9M-1102', 'C', 'voice', 'SC952e581f7322b50b', 'CAT:O84f686512d3b01c2de7d',
     'DS 报本行两个「唔」是多余填充，主张删掉。但这一段说话人是醉着的，原文用 s→sh 的发音滑移表达（shleep／thish／exshtra），同场下一行已用「窝」来承接这个滑移；本行的「唔」很可能也是同一装置。要定这件事得先定整场的醉话怎么拼，跨多行，本批不动。'),
    ('R9M-1103', 'C', 'continuity', 'SC282bb2757cee4a43', 'CAT:O28b8eaa2c872c0193aab',
     '女线 Fox 六场与男线 Fox 六场是同一段台词的两个版本，措辞系统性不同（「让心神向内」对「将心神转向内在」、「那些往事」对「往事」）。两路都判各自内部一致。是否要把男女线拉平属全局口径，本批不动。'),
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

# Content findings first: one of them also removes a trailing space, and it
    # should own that row rather than colliding with the format sweep.
    for route, fid, reason in APPLY:
        if fid not in ROUTE[route]:
            raise SystemExit('no such finding: %s:%s' % (route, fid))
        f = ROUTE[route][fid]
        final = f.get('proposed_zh') or ''
        if not final:
            raise SystemExit('apply without text: %s:%s' % (route, fid))
        emit(route + ':' + fid, route, f.get('severity', ''), f.get('category', ''),
             f['row_ids'][0], 'apply', final, reason)

    skipped = {'P08-0107'}
    for route in ('gemini', 'ds'):
        for fid, f in ROUTE[route].items():
            if f.get('category') != 'format' or fid in skipped:
                continue
            rid = f['row_ids'][0]
            row = ROWS[rid][1]
            if (row['source'] or '') != (row['source'] or '').rstrip():
                raise SystemExit('source also ends in a space: ' + rid)
            if rid in taken:
                emit(route + ':' + fid, route, 'C', 'format', rid, 'reject', '',
                     '与本表 %s 同一行同一处（行尾空格），两路同报，取先落地的条目。' % taken[rid])
                continue
            emit(route + ':' + fid, route, 'C', 'format', rid, 'apply',
                 (row['current'] or '').rstrip(),
                 '译文行尾多出半角空格，英文原行行尾没有；该空格参与行宽测量。只删空格。')

    for route, fid, reason in REJECT:
        f = ROUTE[route][fid]
        emit(route + ':' + fid, route, f.get('severity', ''), f.get('category', ''),
             f['row_ids'][0], 'reject', '', reason)

    for fid, sev, cat, scene_id, rid, reason in HOLD:
        emit(fid, 'R9M', sev, cat, rid, 'hold', '', reason)

    (BASE / 'review/decisions.tsv').write_text('\n'.join(lines) + '\n', encoding='utf8')
    applies = sum(1 for l in lines[1:] if l.split('\t')[6] == 'apply')
    print(json.dumps({'decisions': len(lines) - 1, 'apply': applies,
                      'reject': len(lines) - 1 - applies - len(HOLD),
                      'hold': len(HOLD)}, ensure_ascii=False))


if __name__ == '__main__':
    main()
