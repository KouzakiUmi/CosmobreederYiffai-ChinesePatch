"""Write the r9 batch-08-part03 decision table.

The route that returned findings argued all seventeen trailing spaces in this
part were mirrors of the English and so filed none. That reasoning inverted the
evidence: the catalog field it read describes the Chinese line, not the source.
Checked against the unit sources, the seventeen are real defects and twelve
other rows in this part are genuine mirrors, so the table files the seventeen
itself and leaves the twelve alone.
"""
from pathlib import Path
import json

ROOT = Path(__file__).resolve().parents[4]
BASE = ROOT / 'localization/editorial/r9-polish/batch-08-part03'
ORDER = json.loads((BASE / 'orders/batch-08-part03.json').read_text('utf8'))
ROWS = {r['row_id']: (s['scene_id'], r) for s in ORDER['scenes'] for r in s['rows']}

# Rows whose Chinese line ends in a space the English source does not have.
# Derived from the unit sources, not from the order file.
TRAILING = [
    'CAT:Odbaa97f8ad38565b6b69', 'CAT:O8e573572a049b63ae705', 'CAT:O25aac6350f03509b6cda',
    'CAT:Obd906925198633290848', 'CAT:O84f5f2dfcb5bf121ed89', 'CAT:O199227d31537be4e16d5',
    'CAT:O6118f287fdcc1bb16cc2', 'CAT:Oaa0b230e86c2c0130c4b', 'CAT:O5c6b821881ff928818f2',
    'CAT:Oeea1cdd013e38babc1a9', 'CAT:O8bfc957b822cdda6a0c1', 'CAT:O05c8f168f413e803c55e',
    'CAT:O2a1ce8dd77078b6f7dea', 'CAT:Od5d500b7140ed29eca3a', 'CAT:O7c957ec32840a49ec5bf',
    'CAT:O8b043a339ab65f78a095', 'CAT:Of67ca13006bb8b779840',
]


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


ROUTE = {'ds': load('ds'), 'gemini': load('gemini')}

APPLY = [
    ('ds', 'P08-S3-101',
     '原文 soooooooo much 的拉长被挪到了「太」上，成了「太——谢谢你」，单独一个「太」悬空不成句；拉长该落在「谢谢」上。'),
    ('ds', 'P08-S3-102',
     'feral 在本行被译成「兽人」，「兽人」在中文里读作一个种族；同场另一处作「兽形」。原文指失去理智的野兽状态。'),
    ('ds', 'P08-S3-103',
     '原文 doggy cream 是绕开的说法，现译「狗狗精液」把它直白化了，属加码；工单禁止。改回「狗狗奶油」，与原文的委婉程度一致。'),
    ('ds', 'P08-S3-104',
     '原文 pushing your tail back 是尾巴；现译「把屁股往后迎」换了部位，同场另一行作「粗尾巴」。'),
    ('ds', 'P08-S3-105',
     '「区区在下」是自谦语，与这一句自夸身手高超的语气相反，且同场另一处该角色自称「本人」。原文 yours truly 就是「我」。'),
    ('ds', 'P08-S3-106',
     '原文 doing whatever it is they do 这一层被整个漏掉，只剩「忙活到筋疲力尽」，读者不知道它们在忙什么。'),
    ('ds', 'P08-S3-107',
     '「有些我的装备」是英文语序直搬；中文应作「我有几件装备」。'),
    ('ds', 'P08-S3-108',
     '原文 Here, 是递东西时说「拿着」；现译「好吧」把这句读成了语气词，而下文紧接 take this garbage 与 With shoes in hand，递物动作不能丢。'),
]

HOLD = [
    ('R9M-1301', 'C', 'format', 'SC8cfb083d3c9e5b3a', 'CAT:O7c957ec32840a49ec5bf',
     '本批另有 12 行（`SFW` 编号一侧）中文行尾带空格，经核对英文原行本身也带空格，属排版镜像，不动。这批镜像行与 17 行真缺陷混在同一批里，是本轮两路判断相反的原因。'),
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

    for rid in TRAILING:
        scene_id, row = ROWS[rid]
        if row['current'] == (row['current'] or '').rstrip():
            raise SystemExit('no trailing space to remove: ' + rid)
        if rid in taken:
            # A content finding already rewrote this row and dropped the space.
            continue
        emit('R9M-' + rid, 'R9M', 'C', 'format', rid, 'apply',
             row['current'].rstrip(),
             '中文行尾多出半角空格，英文原文行尾没有（按 catalog 的 unit 原文核对）。该空格参与行宽测量。只删空格。')

    for fid, sev, cat, scene_id, rid, reason in HOLD:
        emit(fid, 'R9M', sev, cat, rid, 'hold', '', reason)

    (BASE / 'review/decisions.tsv').write_text('\n'.join(lines) + '\n', encoding='utf8')
    applies = sum(1 for l in lines[1:] if l.split('\t')[6] == 'apply')
    print(json.dumps({'decisions': len(lines) - 1, 'apply': applies,
                      'hold': len(HOLD)}, ensure_ascii=False))


if __name__ == '__main__':
    main()
