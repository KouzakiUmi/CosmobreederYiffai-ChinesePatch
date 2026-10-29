"""生成 R4 留置项裁决表与来源锁定台账（锚定 candidate8）。

输入：R2 PENDING.md 的 45 条 defer + evidence/runtime-evidence.json。
输出：
  reports/pending-01/decisions.tsv
  reports/pending-01/SUMMARY.md
  ../../translations/editorial-r4-pending-repairs.jsonl  （仅 apply 项）
不写归档、不改正式译文库、不构建候选。
"""
import csv
import json
import sys
import zipfile
from collections import Counter
from hashlib import sha256
from pathlib import Path

ROOT = Path(__file__).resolve().parents[4]
LOC = ROOT / 'localization'
R4 = LOC / 'editorial' / 'r4-pending'
sys.path.insert(0, str(LOC / 'tools'))
from codec import decrypt_file  # noqa: E402

PENDING = LOC / 'editorial' / 'r2' / 'reports' / 'repair-01' / 'PENDING.md'
CAND = LOC / 'builds' / 'r28-character-names-candidate8'

# finding_id -> (disposition, evidence_class, reason, action)
DECISIONS = {
    'P01-032': ('style_rule', 'no_voice_proven',
                '失真广播残片；FMOD 事件库无语音对白，原音证据不存在。',
                '保留拉丁残片形态，不补全句。'),
    'P01-034': ('defer', 'source_anomaly',
                'SENSOR DARK 原文异常搭配，文本内证不足以唯一确定。',
                '维持现译，保留异质感。'),
    'P01-035': ('defer', 'insufficient_evidence',
                'MAGs 缩写未展开，物件身份无直接证据。',
                '保留类别风险，不按常识替换。'),
    'P02-009': ('defer', 'creative_pending',
                '纳米机→anal 中文音桥未建立，机械近音会生造性词。',
                '待专项创译，整组重写并试读。'),
    'P02-029': ('close_no_change', 'covered_by_r3',
                'Enelye 已由 R3 终裁为恩莉耶；目标行 4 处（NAME-0369/0398/0741/0790）已应用。',
                '不改文，结案。'),
    'P02-032': ('style_rule', 'no_voice_proven',
                'TR...MIS...ATE 未知失真残片，无语音可核。',
                '按残片保形，不扩写。'),
    'P02-033': ('close_upstream', 'source_defect',
                '源确为 YIFFAI、speaker 为 Yiffany 且有 MAM；中文跟源正确。',
                '结案为上游源疑点。'),
    'P03-015': ('close_no_change', 'source_grammar',
                '门卡教学三行齐全，THEM 先行词是 DOORS，现译正确。',
                '不改文，结案。'),
    'P03-026': ('style_rule', 'no_voice_proven',
                'GEAR TO / NOT GIVE 句法残缺，无原音。',
                '按残片保形。'),
    'P03-033': ('defer', 'layout_pending',
                '高阶女士卡片含真实换行留白，六行改写未经 16 格容器实测。',
                '待字体容器实测后改写。'),
    'P04-006': ('close_upstream', 'source_defect',
                'MAUSER ORDERS IN 与说话人关系无演出证据。',
                '结案为上游源疑点。'),
    'P04-007': ('close_upstream', 'source_defect',
                'NSFW 女线源称 YIFFAI，中文跟源正确。',
                '结案为上游源疑点。'),
    'P04-024': ('defer', 'term_follow',
                'Trainer Tazer 短名与 TRAINER 商店义分开；术语表已裁决驯兽/见习口径。',
                '跟随术语表，短名不再另造；本条转术语跟随。'),
    'P04-025': ('style_rule', 'no_voice_proven',
                'SAVE IT 宾语与残词不可确定。',
                '按残片保形。'),
    'P04-031': ('apply', 'enemy_table',
                'Bumper 在 enemyData 敌人表中；UI 弹板错误，对话撞击兽正确。',
                'UI 三个 popup 键改撞击兽。'),
    'P05-015': ('defer', 'source_anomaly',
                'sensor dark 语法异常，与 P01-034 同源。',
                '维持现译。'),
    'P05-020': ('defer', 'creative_pending',
                'COME IN 与 I HOPE NOT 成组成人接梗，须整组重建。',
                '待专项创译；中文“进来了？”可保歧义。'),
    'P05-034': ('apply', 'dictionary_key',
                'ACQUIRED ZENER WAVES 是 missionLog header；波浪不符波形概念。',
                '男女线各一条改获得泽纳波。'),
    'P05-035': ('apply', 'runtime_proven',
                'OLD JUNK 是 shops/male/Aread0_Macsen1/products/2 的 displayName，CosmoBody 制装的伪装展示名。',
                '改旧杂货。'),
    'P05-036': ('close_upstream', 'source_defect',
                'male 路径源称 Yiffany/her，中文跟源正确。',
                '结案为上游源疑点。'),
    'P05-037': ('apply', 'term_ledger',
                'Exile 已终裁流放地并全区统用，仅 datadf 男线漏字。',
                '补为流放地东北。'),
    'P06-004': ('close_upstream', 'source_defect',
                'MAUSER ORDERS IN 与 P04-006 同类。',
                '结案为上游源疑点。'),
    'P06-009': ('close_no_change', 'source_grammar',
                '门卡 THEM 指 DOORS，现译正确。',
                '不改文，结案。'),
    'P06-020': ('close_no_change', 'covered_by_r3',
                'Enelye 已终裁恩莉耶；字典 ui.card.CosmoCardEnelye.name 已是恩莉耶 <阿尔法>，对白 12 处已统一。',
                '不改文，结案。'),
    'P06-021': ('apply', 'runtime_proven',
                'OLD JUNK 女线 displayName 同 P05-035。',
                '改旧杂货，与男线一致。'),
    'P07-017': ('apply', 'official_patch',
                '官方 patch 把 TWISTED BREAD 改为 HARD KNOTTED|BRED，刻意荤双关；StatPepper 同调。',
                '译出双关，不改成面包或培育语。'),
    'P07-018': ('apply', 'runtime_proven',
                'ui.breeding.Kobold.affinity.max 是宠物笼亲和度实显文本。',
                '改写为蜷在身边享受陪伴。'),
    'P07-019': ('apply', 'runtime_proven',
                'ui.data.f_ClassicWerepup.desc 实存于 patch 层图鉴。',
                '语序顺正为击败后回忆涌上。'),
    'P07-020': ('apply', 'runtime_proven',
                'ui.data.m_AgentM02.desc 实存于 patch 层图鉴。',
                '改为强势上位猫探员迎战。'),
    'P07-025': ('defer', 'creative_pending',
                'beat off 双关尚无自然中文。',
                '维持现稿待精校。'),
    'P07-028': ('style_rule', 'no_voice_proven',
                'SAVE IT 残片与 P04-025 同源。',
                '按残片保形。'),
    'P08-013': ('defer', 'creative_pending',
                'mine/mined/mines 多义无法靠词面堆叠恢复。',
                '整组专项创译后再落。'),
    'P08-022': ('defer', 'mechanic_unverified',
                'touch 是否等于相邻未核界面判定。',
                '保留不接触现译。'),
    'P09-031': ('apply', 'dictionary_key',
                'SpecialFap.ElfBuff.desc 是道具说明实显文本。',
                '补为精灵加成|闲置时回复精神力。'),
    'P09-035': ('close_upstream', 'source_defect',
                'female 路径源 his/Yiffai，中文跟源正确。',
                '结案为上游源疑点。'),
    'P10-007': ('style_rule', 'no_voice_proven', '男线失真残片与 P01-032 同类。', '按残片保形。'),
    'P10-008': ('style_rule', 'no_voice_proven', '女线失真残片与 P01-032 同类。', '按残片保形。'),
    'P10-009': ('style_rule', 'no_voice_proven', 'GEAR TO 残片与 P03-026 同类。', '按残片保形。'),
    'P10-011': ('defer', 'creative_pending',
                'take it / Just like he did 施受未核。',
                '待创译，明确施受后再改。'),
    'P10-017': ('close_no_change', 'source_grammar', '门卡 THEM 指 DOORS，现译正确。', '不改文，结案。'),
    'P10-018': ('close_no_change', 'source_grammar', '门卡 THEM 指 DOORS，现译正确。', '不改文，结案。'),
    'P10-028': ('close_no_change', 'already_applied',
                'candidate8 已改为“矮人嘟囔着抱怨住处，|却还是冲你|粗犷地笑了笑。”，gruff smile 生硬已解。',
                '不改文，结案。'),
    'P10-030': ('close_no_change', 'runtime_proven',
                'ui.end.BadEnding l6/l7/l8 按键号递增绘制即特蕾还在外面那里……，无错乱。',
                '不改文，结案。'),
    'P10-032': ('defer', 'source_anomaly',
                '原文多重否定异常，上下文不能证明作者意图。',
                '整条留置。'),
    'P10-035': ('defer', 'term_follow',
                'BumperPlus 在 enemyData 已证实；Bumper 裁决撞击兽，Plus 变体待专名规律。',
                '跟随术语表，Plus 另定。'),
}

# apply：finding -> 具体节点规格（archive, entry, kind, locator, new）
APPLY_SPECS = {
    'P04-031': [
        ('patch.pak', 'datav/1', 'json', {'json_key': 'ClassicBumper.popup'}, '撞击兽'),
        ('patch.pak', 'datav/1', 'json', {'json_key': 'ClassicBumperC.popup'}, '撞击兽'),
        ('patch.pak', 'datav/1', 'json', {'json_key': 'ClassicBumperPlus.popup'}, '撞击兽'),
    ],
    'P09-031': [
        ('patch.pak', 'datav/1', 'json',
         {'json_key': 'SpecialFap.ElfBuff.desc'}, '精灵加成|闲置时回复精神力'),
    ],
    'P07-017': [
        ('patch.pak', 'datav/1', 'json',
         {'json_key': 'StatPretzel.desc'}, '硬结打卷|育得正好'),
    ],
    'P07-018': [
        ('patch.pak', 'datav/1', 'json',
         {'json_key': 'ui.breeding.Kobold.affinity.max'},
         '科博德蜷在你身边，|惬意地享受着你的陪伴。|真是个好宠物！'),
    ],
    'P07-019': [
        ('patch.pak', 'datav/1', 'json',
         {'json_key': 'ui.data.f_ClassicWerepup.desc'},
         '击败小狼崽之后，|回忆涌上心头，又迟疑起来。'),
    ],
    'P07-020': [
        ('patch.pak', 'datav/1', 'json',
         {'json_key': 'ui.data.m_AgentM02.desc'},
         '强势的上位猫探员，|迎战来犯之敌！'),
    ],
    'P05-035': [
        ('cosmobreeder-multi.jar', 'datay/1', 'json',
         {'json_pointer': '/shops/male/Area0_Macsen1/products/2/displayName'}, '旧杂货'),
    ],
    'P06-021': [
        ('cosmobreeder-multi.jar', 'datay/1', 'json',
         {'json_pointer': '/shops/female/Area0_Macsen1/products/2/displayName'}, '旧杂货'),
    ],
    'P05-034': [
        ('cosmobreeder-multi.jar', 'datay/1', 'json',
         {'json_pointer': '/missionLog/male/2/header'}, '获得泽纳波'),
        ('cosmobreeder-multi.jar', 'datay/1', 'json',
         {'json_pointer': '/missionLog/female/2/header'}, '获得泽纳波'),
    ],
    'P05-037': [
        # datadf 男线一行；定位按原文行匹配
        ('cosmobreeder-multi.jar', 'datadf/1', 'line', {'source_line': '流放东北'},
         '你在流放地东北发现的那座宝库，看起来确实很重要。'),
    ],
}


def read_jsonl(path):
    return [json.loads(s) for s in path.read_text('utf-8').splitlines() if s.strip()]


def resolve_pointer(doc, ptr):
    cur = doc
    for part in ptr.lstrip('/').split('/'):
        part = part.replace('~1', '/').replace('~0', '~')
        cur = cur[int(part)] if isinstance(cur, list) else cur[part]
    return cur


def line_index(text, needle):
    for i, line in enumerate(text.splitlines(), 1):
        if needle in line:
            return i, line
    raise SystemExit(f'line not found: {needle}')


def main():
    defers = []
    for line in PENDING.read_text('utf-8').splitlines():
        if line.startswith('| P'):
            cells = [c.strip() for c in line.strip().strip('|').split('|')]
            if cells[1] == 'defer':
                defers.append(cells[0])
    if set(defers) != set(DECISIONS):
        raise SystemExit(f'裁决覆盖不符: missing={sorted(set(defers)-set(DECISIONS))} '
                         f'extra={sorted(set(DECISIONS)-set(defers))}')

    archives = {name: zipfile.ZipFile(CAND / name)
                for name in ('cosmobreeder-multi.jar', 'patch.pak')}
    acc = json.loads((CAND / 'acceptance.json').read_text('utf-8'))
    for name, zp in archives.items():
        got = sha256((CAND / name).read_bytes()).hexdigest()
        if got != acc['archives'][name]:
            raise SystemExit(f'candidate8 archive drift: {name}')

    cache = {}

    def raw(archive, entry):
        key = (archive, entry)
        if key not in cache:
            cache[key] = decrypt_file(archives[archive].read(entry))
        return cache[key]

    def resource_sha(archive, entry):
        return sha256(raw(archive, entry)).hexdigest()

    ledger, n = [], 0
    resolved = {}
    for pid, specs in APPLY_SPECS.items():
        for archive, entry, kind, locator, new in specs:
            n += 1
            if kind == 'json':
                doc = json.loads(raw(archive, entry))
                if 'json_key' in locator:
                    old = doc[locator['json_key']]
                    target_ptr = '/' + locator['json_key']
                else:
                    old = resolve_pointer(doc, locator['json_pointer'])
                    target_ptr = locator['json_pointer']
                if not isinstance(old, str):
                    raise SystemExit(f'non-string target {pid} {locator}')
            else:
                text = raw(archive, entry).decode('utf-8', errors='replace')
                idx, line_text = line_index(text, locator['source_line'])
                if '流放东北' not in line_text:
                    raise SystemExit(f'unexpected line for {pid}: {line_text!r}')
                old = line_text
                new = old.replace('流放东北', '流放地东北')
                target_line = idx
            if old == new:
                raise SystemExit(f'no-op target {pid}: {old!r}')
            resolved[f'{pid}:{n}'] = old
            record = {
                'op_id': f'R4-{n:04d}',
                'archive': archive,
                'archive_entry': entry,
                'kind': kind,
                'before_resource_sha256': resource_sha(archive, entry),
                'old': old,
                'new': new,
                'finding_ids': [pid],
                'source_refs': [
                    f'R1:{pid}',
                    'localization/editorial/r4-pending/evidence/runtime-evidence.json',
                ],
            }
            if kind == 'json':
                record['pointer'] = target_ptr
            else:
                record['line'] = target_line
            ledger.append(record)

    out = R4 / 'reports' / 'pending-01'
    out.mkdir(parents=True, exist_ok=True)
    counts = Counter()
    with (out / 'decisions.tsv').open('w', encoding='utf-8', newline='') as f:
        w = csv.writer(f, delimiter='\t', lineterminator='\n')
        w.writerow(['finding_id', 'disposition', 'evidence_class', 'apply_ops', 'reason', 'action'])
        for pid in sorted(DECISIONS):
            disp, cls, reason, action = DECISIONS[pid]
            counts[disp] += 1
            ops = len(APPLY_SPECS.get(pid, []))
            w.writerow([pid, disp, cls, ops, reason, action])

    ledger_path = LOC / 'translations' / 'editorial-r4-pending-repairs.jsonl'
    ledger_path.write_text('\n'.join(json.dumps(o, ensure_ascii=False) for o in ledger) + '\n',
                           encoding='utf-8')

    # 术语表是活表：记录本次变更前后 SHA，便于与 R3 交付记录对照。
    glossary = LOC / 'review' / 'glossary.csv'
    r3_record = LOC / 'editorial' / 'r3-names' / 'reports' / 'delivery-record.json'
    r3_glossary_sha = json.loads(r3_record.read_text('utf-8'))['evidence_sha256'].get(
        'localization/review/glossary.csv')
    glossary_sha = sha256(glossary.read_bytes()).hexdigest()
    glossary_rows = len([l for l in glossary.read_text('utf-8').splitlines() if l.strip()]) - 1

    manifest = {
        'schema': 'cosmo-editorial-r4-decisions/v1',
        'glossary': {
            'path': 'localization/review/glossary.csv',
            'sha256': glossary_sha,
            'sha256_at_r3_delivery': r3_glossary_sha,
            'changed_since_r3': glossary_sha != r3_glossary_sha,
            'term_rows': glossary_rows,
            'added_terms': ['Exile', 'Bumper', 'Trainer / Trainee', 'Zener', 'Pretzel / StatPretzel'],
        },
        'coverage': {'defer_total': len(defers), 'decided': len(DECISIONS)},
        'dispositions': dict(counts),
        'apply_findings': sorted(APPLY_SPECS),
        'apply_ops': len(ledger),
        'ledger': str(ledger_path.relative_to(ROOT)),
        'base_candidate': 'localization/builds/r28-character-names-candidate8',
        'base_archives_sha256': acc['archives'],
    }
    (out / 'manifest.json').write_text(json.dumps(manifest, ensure_ascii=False, indent=2) + '\n',
                                       encoding='utf-8')
    print('dispositions:', dict(counts), 'total', sum(counts.values()))
    print('apply ops:', len(ledger), '->', ledger_path.relative_to(ROOT))
    for op in ledger:
        assert op['old'] != op['new']
    return manifest


if __name__ == '__main__':
    main()
