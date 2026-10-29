"""Write the r9 batch-06-part04 decision table.

PLAN entries are (route, finding_id, decision, reason) and take their text from
the route's own findings file. SELF entries are (finding_id, severity, category,
row_id, final_zh, reason) for corrections I decided myself, where either the
route's draft was inadequate or the row needed more than the route proposed.
"""
from pathlib import Path
import json

ROOT = Path(__file__).resolve().parents[4]
BASE = ROOT / 'localization/editorial/r9-polish/batch-06-part04'
ORDER = json.loads((BASE / 'orders/batch-06-part04.json').read_text('utf8'))
ROWS = {r['row_id']: (s['scene_id'], r) for s in ORDER['scenes'] for r in s['rows']}


def load(route):
    p = BASE / route / 'findings.jsonl'
    out = {}
    if not p.exists():
        return out
    for line in p.read_text('utf8').splitlines():
        if not line.strip():
            continue
        f = json.loads(line)
        out[f['finding_id']] = f
    return out


ROUTE = {'gemini': load('gemini'), 'ds': load('ds')}

# 词典：BUCKLER→小圆盾；P.A.W. 带点 126/135；OMEGA 词素＝欧米茄（词典 13 处，全库 22:3）

PLAN = [
    ('gemini', 'P06d-103', 'apply',
     '工单四之二点名超限：原译 55 字实测 4 行。保留场衰减棱镜技术名、生物好感条件、抚摸充能、效果因生物而异四项，只压虚词与重复指代。240px／224px 均 3 行。'),
    ('gemini', 'P06d-107', 'apply',
     '工单四之二点名超限：原译 57 字实测 4 行。保留影响生物的加密币、严重违法、绝密欧米茄协议、你自己定夺四项条件与语气，只压连接词。顺带把协议名的少数写法「欧米伽」并入库内标准「欧米茄」（词典条目名 13 处、全库 22 对 3）。240px／224px 均 3 行。'),
    ('gemini', 'P06d-108', 'apply',
     '女版同句同改，与上一条同一处压缩与同一术语修正。240px／224px 均 3 行。'),
    ('gemini', 'P06d-105', 'apply',
     'DOWN 与 JUMP 是按键名，硬约束要求原样保留；本行译成「"下"+"跳跃"」，玩家照着按不到键。同 root 与全库另 7 处 JUMP 都保留英文。'),
    ('gemini', 'P06d-102', 'apply',
     '被打断处用半角连字符，12px 渲染成一个孤立小横；全批其它被打断处一律用全角破折号。'),
    ('gemini', 'P06d-101', 'reject',
     '主张把「看起来 S、S……」改成「看起来可、可爱……」。该行原文是 LOOK S-S...，首字母重复对应的是 S 打头的词；男线同句（CAT:Oc82fdcb15e39e8e56ef3）已定译「看着性、性感……」。本条是按上一句 CUTE 反推的，与源文首字母不符，不改。'),
    ('gemini', 'P06d-104', 'reject',
     '方向相反：本条主张 THEM 指门卡，改成「卡上所标数字」。同 root 男线（part01 的 CAT:Ocf5d1daf6e7846490b5f、part02 的 CAT:Oc91c83e4cdc8b678f7ca）已据 ON THEM 判为门上所标等级，且上一行明说「带着卡走向能量门」。本行现译「门上所标数字」是对的，不改。'),
    ('gemini', 'P06d-106', 'reject',
     '主张把「兄 弟 ……」改成「老——兄……」。原文是 D U D E . . .，逐字加空格、末尾接省略点；译文「兄 弟 ……」正是对这条排版的镜像还原，改掉反而不忠实。DS 路在 part03 独立判为不报，两路一致。'),
    ('gemini', 'P06d-109', 'reject',
     '按键名确实被译成「“上”+“攻击”」，本条成立；但该行在 224px 下原本就折成 4 行，只换按键仍会超限。改由 R9M-905 一并处理按键与行宽。'),
]

SELF = [
    ('R9M-905', 'A', 'gameplay', 'SC25645bfd72c28ab1', 'CAT:O1b37c6453c9c87c3f4d8',
     '  Tomcat: [报告说，战斗中特工能用“SELECT”选能力，再同时按“UP”+“ATTACK”使出。]',
     '按键名被译成「“上”+“攻击”」，须恢复英文；同时该行在 224px 下原本就折成 4 行（240px 是 3 行），是既有超限行，一并压回。保留「报告说」的传闻限定、战斗时机、两段按键三项，只压连接词。两档实测均 3 行。'),
]

HOLD = [
    ('R9M-904', 'B', 'format', 'SCc4c2b7eda0f9ae23', 'SFW611fa16540e8dfd8f4e9db01',
     '本行与男线 CAT:Oc82fdcb15e39e8e56ef3 同句，但源文两版上一句用词不同（女版 CUTE、男版 SEXY），而本句两版都写 LOOK S-S...。按源文字面应与男线一致作「性、性感」，但女版上文说「可爱」，字面与内容自相矛盾。这是源文内部不一致，需与 CROSS 体例一并裁决，本批不改。'),
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

    for route, fid, decision, reason in PLAN:
        if fid not in ROUTE[route]:
            raise SystemExit('no such finding: %s:%s' % (route, fid))
        f = ROUTE[route][fid]
        final = ''
        if decision == 'apply':
            final = f.get('proposed_zh') or ''
            if not final:
                raise SystemExit('apply without text: %s:%s' % (route, fid))
        emit(route + ':' + fid, route, f.get('severity', ''), f.get('category', ''),
             f['row_ids'][0], decision, final, reason)

    for fid, sev, cat, scene_id, rid, final, reason in SELF:
        emit(fid, 'R9M', sev, cat, rid, 'apply', final, reason)

    for fid, sev, cat, scene_id, rid, reason in HOLD:
        emit(fid, 'R9M', sev, cat, rid, 'hold', '', reason)

    (BASE / 'review/decisions.tsv').write_text('\n'.join(lines) + '\n', encoding='utf8')
    print(json.dumps({'decisions': len(lines) - 1,
                      'apply': sum(1 for p in PLAN if p[2] == 'apply') + len(SELF),
                      'reject': sum(1 for p in PLAN if p[2] == 'reject'),
                      'hold': len(HOLD)}, ensure_ascii=False))


if __name__ == '__main__':
    main()
