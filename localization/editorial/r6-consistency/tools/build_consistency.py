"""R6：层一致性与术语回改。

处理四件事：
  A. SENSOR DARK 按同一功能姊妹场景的内证改为“传感器探测不到的悬浮球”
  B. Bumper 回改：图鉴写“上下弹跳的巡逻机器人”，术语约束“机器不译成兽”，
     R4 的“撞击兽”与旧“弹板”都改“弹跳机”；popup 与对白同时统一
  C. TazerTrainer 道具名“训练者”→“驯兽”，与对白和术语表一致
  D. P10-032 三重否定按上下文改成正向最小表述
  E. R4 只落了 patch 层的 datav 改动，补 jar 层同值（R2 起沿用 occurrence 归档落笔，
     patch 覆盖 jar 同键，导致未装补丁档的 jar 层读旧文）

锚定 candidate10；输出台账与处置表，不写归档、不构建。
"""
import csv
import json
import sys
import zipfile
from hashlib import sha256
from pathlib import Path

ROOT = Path(__file__).resolve().parents[4]
LOC = ROOT / 'localization'
R6 = LOC / 'editorial' / 'r6-consistency'
sys.path.insert(0, str(LOC / 'tools'))
from codec import decrypt_file  # noqa: E402

CAND = LOC / 'builds' / 'r5-creative-candidate10'

SENSOR_OLD = '  Tomcat: [让我猜猜：刚碰了一颗悬浮的暗色传感球？]'
SENSOR_NEW = '  Tomcat: [让我猜猜：刚碰了一颗传感器探测不到的悬浮球？]'
BUMPER_NEW = '弹跳机'
PRETZEL = '硬结打卷|育得正好'
ELF = '精灵加成|闲置时回复精神力'
KOBOLD = '科博德蜷在你身边，|惬意地享受着你的陪伴。|真是个好宠物！'
WEREPUP = '击败小狼崽之后，|回忆涌上心头，又迟疑起来。'

# (finding, archive, entry, kind, locator, old, new)
EDITS = [
    # A. SENSOR DARK：jar 两处 + pak 两处
    ('P01-034', 'cosmobreeder-multi.jar', 'datadf/1', 'line', 4368, SENSOR_OLD, SENSOR_NEW),
    ('P01-034', 'cosmobreeder-multi.jar', 'datadf/1', 'line', 4377, SENSOR_OLD, SENSOR_NEW),
    ('P05-015', 'patch.pak', 'datadf/1', 'line', 4523, SENSOR_OLD, SENSOR_NEW),
    ('P05-015', 'patch.pak', 'datadf/1', 'line', 4532, SENSOR_OLD, SENSOR_NEW),

    # B. Bumper：三层 popup ×2 归档 + 4 处对白
    ('P04-031', 'cosmobreeder-multi.jar', 'datav/1', 'json', 'ClassicBumper.popup', '弹板', BUMPER_NEW),
    ('P04-031', 'cosmobreeder-multi.jar', 'datav/1', 'json', 'ClassicBumperPlus.popup', '弹板', BUMPER_NEW),
    ('P04-031', 'cosmobreeder-multi.jar', 'datav/1', 'json', 'ClassicBumperC.popup', '弹板', BUMPER_NEW),
    ('P10-035', 'patch.pak', 'datav/1', 'json', 'ClassicBumper.popup', '撞击兽', BUMPER_NEW),
    ('P10-035', 'patch.pak', 'datav/1', 'json', 'ClassicBumperPlus.popup', '撞击兽', BUMPER_NEW),
    ('P10-035', 'patch.pak', 'datav/1', 'json', 'ClassicBumperC.popup', '撞击兽', BUMPER_NEW),
    ('P04-031', 'cosmobreeder-multi.jar', 'datadf/1', 'line', 3122,
     '  Bossu: [那一区的撞击机器人，装甲似乎比你之前见过的同类更好。]',
     '  Bossu: [那一区的弹跳机，装甲似乎比你之前见过的同类更好。]'),
    ('P04-031', 'cosmobreeder-multi.jar', 'datadm/1', 'line', 3169,
     '  Bossu: [那一区的撞击兽，装甲似乎比你见过的其他撞击兽都要好。]',
     '  Bossu: [那一区的弹跳机，装甲似乎比你见过的其他弹跳机都要好。]'),
    ('P10-035', 'patch.pak', 'datadf/1', 'line', 3167,
     '  Bossu: [那一区的撞击机器人，装甲似乎比你之前见过的同类更好。]',
     '  Bossu: [那一区的弹跳机，装甲似乎比你之前见过的同类更好。]'),
    ('P10-035', 'patch.pak', 'datadm/1', 'line', 3237,
     '  Bossu: [那一区的撞击兽，装甲似乎比你见过的其他撞击兽都要好。]',
     '  Bossu: [那一区的弹跳机，装甲似乎比你见过的其他弹跳机都要好。]'),

    # C. 道具名
    ('P04-024', 'cosmobreeder-multi.jar', 'datav/1', 'json', 'TazerTrainer.name', '训练者', '驯兽'),
    ('P04-024', 'patch.pak', 'datav/1', 'json', 'TazerTrainer.name', '训练者', '驯兽'),

    # D. 三重否定
    ('P10-032', 'patch.pak', 'vsn/239', 'line', 59,
     'text: 当然，并不是说好像我不是没有胃口似的。 ',
     'text: 当然，我也不是没有胃口。 '),

    # E. jar 层补 R4 同值
    ('P09-031', 'cosmobreeder-multi.jar', 'datav/1', 'json', 'SpecialFap.ElfBuff.desc',
     '精灵闲置时|回复精神力', ELF),
    ('P07-017', 'cosmobreeder-multi.jar', 'datav/1', 'json', 'StatPretzel.desc',
     '新鲜出炉的|扭结面包', PRETZEL),
    ('P07-018', 'cosmobreeder-multi.jar', 'datav/1', 'json', 'ui.breeding.Kobold.affinity.max',
     '科博德蜷起身子，|享受着你的陪伴。|真是棒极了的宠物！', KOBOLD),
    ('P07-019', 'cosmobreeder-multi.jar', 'datav/1', 'json', 'ui.data.f_ClassicWerepup.desc',
     '给了小狗一记重击后，|又和他交上了朋友！', WEREPUP),
    # 男线 Werepup 描述此前是第三种译法，一并统一
    ('P07-019', 'cosmobreeder-multi.jar', 'datav/1', 'json', 'ui.data.m_ClassicWerepup.desc',
     '给了小狗一记重击后，|又和他交上了朋友！', WEREPUP),
    ('P07-019', 'patch.pak', 'datav/1', 'json', 'ui.data.m_ClassicWerepup.desc',
     '打败小狼崽后，|追忆往事，又犹豫不决！', WEREPUP),
]

DECISIONS = [
    ('P01-034', 'apply', 'same_feature_cross_reference',
     '同组 Zener 球场景各写“总部探测不到的球体”“近场数据里完全看不到的”，紧跟“没有数据”；暗色义无支撑。'),
    ('P05-015', 'apply', 'same_feature_cross_reference', '与 P01-034 同句，patch 层两处一并统一。'),
    ('P04-031', 'apply', 'dex_description_and_term_constraint',
     '图鉴写“不停上下弹跳的机器/巡逻机器人”，术语提案约束“机器不译成兽”；R4 的撞击兽改弹跳机。'),
    ('P10-035', 'apply', 'dex_description_and_term_constraint', 'BumperPlus 与 Bumper 同为弹跳巡逻机，popup 与对白统一为弹跳机。'),
    ('P04-024', 'apply', 'term_consistency', '道具名“训练者”与对白“驯兽电击枪”和术语表“驯兽/见习”不一致。'),
    ('P10-032', 'apply', 'minimal_positive_reading',
     '上下文在自夸有胃口，三重否定照字面搬读不通；改为“我也不是没有胃口”，保留双重否定的语气。'),
    ('P09-031', 'apply', 'layer_consistency', 'jar 层仍是旧文，补与 patch 层同值。'),
    ('P07-017', 'apply', 'layer_consistency', 'jar 层仍是旧文，补与 patch 层同值。'),
    ('P07-018', 'apply', 'layer_consistency', 'jar 层仍是旧文，补与 patch 层同值。'),
    ('P07-019', 'apply', 'layer_consistency_variant_alignment',
     'f/m 两个变体与 jar/pak 两层共三种译法；统一为 R4 已通过的表述。'),
]


def main():
    archives = {n: zipfile.ZipFile(CAND / n) for n in ('cosmobreeder-multi.jar', 'patch.pak')}
    cache, ledger = {}, []
    for n, (pid, archive, entry, kind, loc, old, new) in enumerate(EDITS, 1):
        key = (archive, entry)
        if key not in cache:
            cache[key] = decrypt_file(archives[archive].read(entry))
        if kind == 'json':
            doc = json.loads(cache[key])
            have = doc[loc]
        else:
            lines = cache[key].decode('utf-8').splitlines()
            have = lines[loc - 1]
        if have != old:
            raise SystemExit(f'{pid}: {archive}/{entry} locator {loc}\n  have={have!r}\n  want={old!r}')
        if old == new:
            raise SystemExit(f'{pid}: no-op')
        rec = {
            'op_id': f'R6-{n:04d}',
            'archive': archive,
            'archive_entry': entry,
            'kind': kind,
            'before_resource_sha256': sha256(cache[key]).hexdigest(),
            'old': old,
            'new': new,
            'finding_ids': [pid],
            'source_refs': [f'R1:{pid}', 'localization/editorial/r6-consistency/reports/consistency-01/decisions.tsv'],
        }
        if kind == 'json':
            rec['pointer'] = '/' + loc
        else:
            rec['line'] = loc
        ledger.append(rec)

    out = R6 / 'reports' / 'consistency-01'
    out.mkdir(parents=True, exist_ok=True)
    ledger_path = LOC / 'translations' / 'editorial-r6-consistency-repairs.jsonl'
    ledger_path.write_text('\n'.join(json.dumps(o, ensure_ascii=False) for o in ledger) + '\n',
                           encoding='utf-8')

    with (out / 'decisions.tsv').open('w', encoding='utf-8', newline='') as f:
        w = csv.writer(f, delimiter='\t', lineterminator='\n')
        w.writerow(['finding_id', 'disposition', 'evidence_class', 'ops', 'reason'])
        for pid, disp, cls, reason in DECISIONS:
            w.writerow([pid, disp, cls, sum(1 for e in EDITS if e[0] == pid), reason])

    print('ledger ops:', len(ledger))
    for pid, *_ in DECISIONS:
        print(' ', pid, sum(1 for e in EDITS if e[0] == pid), 'ops')


if __name__ == '__main__':
    main()
