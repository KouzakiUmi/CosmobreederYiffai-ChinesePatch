"""Write the r9 batch-07-part01 decision table.

The DS route filed twenty of the same defect (a half-width space at the end of
the Chinese line where the English has none), so the table treats them as one
family and applies them uniformly. Two rows where the English also ends in a
space are left alone: there the space mirrors the source.
"""
from pathlib import Path
import json

ROOT = Path(__file__).resolve().parents[4]
BASE = ROOT / 'localization/editorial/r9-polish/batch-07-part01'
ORDER = json.loads((BASE / 'orders/batch-07-part01.json').read_text('utf8'))
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

TRAILING = [
    'P07-S-101', 'P07-S-103', 'P07-S-104', 'P07-S-107', 'P07-S-110', 'P07-S-111',
    'P07-S-113', 'P07-S-115', 'P07-S-117', 'P07-S-118', 'P07-S-123', 'P07-S-124',
    'P07-S-125', 'P07-S-126', 'P07-S-127', 'P07-S-128', 'P07-S-129', 'P07-S-130',
    'P07-S-131', 'P07-S-132',
]

APPLY = [
    ('gemini', 'P07-101', '清嗓打断处用半角连字符，12px 下是一个孤立小横；全批其它打断处一律用全角破折号。'),
    ('gemini', 'P07-102', '男线同型位置同改。'),
    ('gemini', 'P07-103',
     '女线终报署名整段残留 `-SIGNED, BOSSU`，男线同句已作「——署名：波苏」。全库「署名：波苏」2 处、`SIGNED, BOSSU` 0 处。按男线对齐。'),
    ('ds', 'P07-S-105', '上屏报告块整句缺句末标点；同批其它上屏行带标点。'),
    ('ds', 'P07-S-112',
     'Not quite that low! 的 low 说的是高度；现译「别那么下面」把方位名词当谓语，中文不成句。改「别那么低」。'),
    ('ds', 'P07-S-121', '「醒来」与「一醒来」同句重复，改「一睁眼」去掉重复，动作不变。'),
    ('ds', 'P07-S-133',
     '「一颗绕行星运行的小行星」里「行星」会被读成小行星自己，指代含混；原文 a small asteroid orbiting the planet，女线同句作「绕该星球运行」。'),
    ('ds', 'P07-S-106',
     '合句时把 under my tail 塞进了「等着干」的宾语位，读成「等着干我尾巴底下」，语序不成立。改稿字数与现译相同，行数不变。'),
    ('ds', 'P07-S-119',
     'end-of-capture report 是「被俘结案报告」；现译「获释后的被俘经历报告」凭空加了「已经获释」这个前提，而下一块描写她仍被套着拘束具。'),
    ('ds', 'P07-S-120',
     '...little... 修饰的是后面的 nap；现译「……稍微……」接不上前一行「这段短短的」与下一行「……睡觉」。'),
    ('ds', 'P07-S-122',
     'almost disappointed 的 almost 被抹掉，译成「我还真有点失望」；下一行「差点就是了，直到……」就失去了它否定的对象。'),
    ('ds', 'P07-S-108',
     '同一段里「另一处难受要解决」与「更大的才能解决」两个「解决」撞车，且前者是 take care of（处理）；改「要处理／才行」。'),
]

REJECT = [
    ('ds', 'P07-S-102', '同位语加破折号属排版取舍。原句读得通，且原文本就是全大写呼喊体；改它属风格偏好。'),
    ('ds', 'P07-S-116', '同上一处，男线对应行。'),
    ('ds', 'P07-S-109', '「……再来一次……！」改「……又一次……！」是措辞偏好，两句意思相同，不作修正。'),
    ('ds', 'P07-S-114',
     '主张在「便会被安置进触手床中」句末补逗号。该行是一条完整的方括号陈述（原文 ...nestled into a tentacle bed 到此结束），补逗号反而让它看起来没说完。'),
]

HOLD = [
    ('R9M-1001', 'C', 'term', 'SC42b1851d50303cc3', 'CAT:Oa84ecf30c030b934b0a0',
     'DS 报「恩莉耶大人」与词典条目名「高阶女士」不一致。但这一行是上屏宣称号，男女两线写法相同，改动要连动两条线并牵涉称号体例，本批不改。'),
    ('R9M-1002', 'C', 'continuity', 'SC42b1851d50303cc3', 'CAT:O89be2c7fce59af929339',
     '「她们难道不知道……」按女线同场「她那帮轻浮跟班」判定敌方为女性，代词成立；男线上下文不足以独立确认。登记为已核不动。'),
]


def main():
    lines = ['finding_id\troute\tseverity\tcategory\tscene_id\trow_id\tdecision\tfinal_zh\treason']
    seen = set()

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
        lines.append('\t'.join((key, route, sev, cat, scene_id, rid, decision, final, reason)))

    for fid in TRAILING:
        f = ROUTE['ds'][fid]
        rid = f['row_ids'][0]
        row = ROWS[rid][1]
        if (row['source'] or '') != (row['source'] or '').rstrip():
            raise SystemExit('source also ends in a space, must not strip: ' + rid)
        emit('ds:' + fid, 'ds', 'C', 'format', rid, 'apply',
             (row['current'] or '').rstrip(),
             '译文行尾多一个半角空格，而英文原行没有；该空格会参与行宽测量。原文行尾本身带空格的 2 行按镜像未动。只删空格。')

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
        if fid not in ROUTE[route]:
            raise SystemExit('no such finding: %s:%s' % (route, fid))
        f = ROUTE[route][fid]
        emit(route + ':' + fid, route, f.get('severity', ''), f.get('category', ''),
             f['row_ids'][0], 'reject', '', reason)

    for fid, sev, cat, scene_id, rid, reason in HOLD:
        emit(fid, 'R9M', sev, cat, rid, 'hold', '', reason)

    (BASE / 'review/decisions.tsv').write_text('\n'.join(lines) + '\n', encoding='utf8')
    print(json.dumps({'decisions': len(lines) - 1, 'apply': len(TRAILING) + len(APPLY),
                      'reject': len(REJECT), 'hold': len(HOLD)}, ensure_ascii=False))


if __name__ == '__main__':
    main()
