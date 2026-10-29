"""R5 创译批次：把 R4 的 5 条 creative_pending 落成来源锁定台账。

每组给出：整组新旧文、双关处置说明（保留/部分保留/放弃及理由）。
锚定 candidate9；定位器为物理行号，构建时重新校验旧行与整资源 SHA。
不写归档、不构建。
"""
import csv
import json
import sys
import zipfile
from hashlib import sha256
from pathlib import Path

ROOT = Path(__file__).resolve().parents[4]
LOC = ROOT / 'localization'
R5 = LOC / 'editorial' / 'r5-creative'
sys.path.insert(0, str(LOC / 'tools'))
from codec import decrypt_file  # noqa: E402

CAND = LOC / 'builds' / 'r4-pending-candidate9'

# finding -> 组说明（双关处置）
GROUPS = {
    'P08-013': {
        'status': 'partial_pun_loss',
        'note': ('英文 mine=矿山／mined=采矿或布雷／mines=地雷／mine=我的 四重同形无法在中文单字复现。'
                 '保留结构：Bossu 冷面双关→Yiffai 误以为在讲采矿→Bossu 点出爆炸→Mauser 揭底“这矿是我家的”。'
                 '把枢纽从 mine 换成“认主／炸毛”：Bossu 先抛可疑说法，Yiffai 抓不到重点，爆炸由“认主的东西会自己炸毛”圆回，'
                 '最后由 Mauser 落实占有权。损失：单词层面的三重义不可复制。'),
    },
    'P05-020': {
        'status': 'pun_kept',
        'note': ('COME IN 的无线电呼叫义与“进来”的成人义在中文共用“进来”一词，双关可以保留。'
                 'Yiffai 说“我进来了”既是呼叫应答也可被读成身体动作，Bossu 用“希望你别进来”故意接荤梗后再以“没什么”掩盖。'),
    },
    'P02-009': {
        'status': 'pun_rebuilt',
        'note': ('原文从 nanomechanical 里切出 anal。中文“纳米机械”里没有可切出的荤音节，'
                 '改为在“机械”的“机”上做同音梗（机／鸡），仍属听错长词而抓住一个荤音，'
                 '并保留 Bossu 若无其事继续讲解的节奏。'),
    },
    'P07-025': {
        'status': 'pun_dropped',
        'note': ('beat off 兼“打退”与手淫义。中文“打退”无语义双关，“撸退”是为凑双关生造、读感不成立，'
                 'R2 已判定不可用。本组按自然叙事译为“把他打退”，牺牲双关，不添加原文没有的自我改口。'
                 '荤味由同段“手脚很不老实”“使尽浑身解数”承接，不加新动作。'),
    },
    'P10-011': {
        'status': 'pun_rebuilt',
        'note': ('take it 兼“拿走物品”与“接受插入”。中文用“拿去用”保留物品义，'
                 '“用”在指人时带成人暗示；结尾“就像他当初那样‘用’”保住 Just like he did 的回指与 ;3 语气，不发明具体行为。'),
    },
}

# (finding, archive, entry, anchor, old, new)
EDITS = [
    # ---- P08-013 矿／地雷整组（BossuDex.ClassicMineWall，男女内容版各一份）----
    ('P08-013', 'cosmobreeder-multi.jar', 'datadm/1', '看来图托恩的矿山都已经布上了雷',
     '  Bossu: [确实，看来图托恩的矿山都已经布上了雷。]',
     '  Bossu: [确实，看来图托恩的矿，都"认了主"。]'),
    ('P08-013', 'cosmobreeder-multi.jar', 'datadm/1', '是那些矿区传来的爆炸',
     '  Bossu: [是那些矿区传来的爆炸。]',
     '  Bossu: [认了主的东西，会自己炸毛。]'),
    ('P08-013', 'cosmobreeder-multi.jar', 'datadm/1', '好喊一声"这是我的！"',
     '  Mauser: [波苏的意思是，那些老矿工当年在他们自己的矿里埋了地雷，好喊一声"这是我的！"]',
     '  Mauser: [波苏的意思是，那些老矿工在自己矿里埋了雷——谁碰炸谁，好让人记住"这矿是我家的"！]'),
    ('P08-013', 'patch.pak', 'datadm/1', '看来图托恩的矿山都已经布上了雷',
     '  Bossu: [确实，看来图托恩的矿山都已经布上了雷。]',
     '  Bossu: [确实，看来图托恩的矿，都"认了主"。]'),
    ('P08-013', 'patch.pak', 'datadm/1', '是那些矿区传来的爆炸',
     '  Bossu: [是那些矿区传来的爆炸。]',
     '  Bossu: [认了主的东西，会自己炸毛。]'),
    ('P08-013', 'patch.pak', 'datadm/1', '好喊一声"这是我的！"',
     '  Mauser: [波苏的意思是，那些老矿工当年在他们自己的矿里埋了地雷，好喊一声"这是我的！"]',
     '  Mauser: [波苏的意思是，那些老矿工在自己矿里埋了雷——谁碰炸谁，好让人记住"这矿是我家的"！]'),
    # 同一笑点的提示段：去掉台词里的英文 (mine) 注释
    ('P08-013', 'cosmobreeder-multi.jar', 'datadm/1', '在自己的矿井（mine）里埋了地雷（mine）',
     '  Mauser: [波苏是说，老矿工在自己的矿井（mine）里埋了地雷（mine），表示“这是我的（mine）！”]',
     '  Mauser: [波苏是说，老矿工在自己的矿井里埋了地雷，等于立块牌子：“这矿是我家的，谁也别碰！”]'),
    ('P08-013', 'patch.pak', 'datadm/1', '在自己的矿井（mine）里埋了地雷（mine）',
     '  Mauser: [波苏是说，老矿工在自己的矿井（mine）里埋了地雷（mine），表示“这是我的（mine）！”]',
     '  Mauser: [波苏是说，老矿工在自己的矿井里埋了地雷，等于立块牌子：“这矿是我家的，谁也别碰！”]'),

    # ---- P05-020 COME IN / I HOPE NOT 整组 ----
    ('P05-020', 'patch.pak', 'datadm/1', '波苏，我这就进来',
     '  Yiffai: [波苏，我这就进来。]',
     '  Yiffai: [波苏，我进来了。]'),
    ('P05-020', 'patch.pak', 'datadm/1', '希望别，孩子',
     '  Bossu: [希望别，孩子。]',
     '  Bossu: [希望你别进来，孩子。]'),

    # ---- P02-009 纳米机械 / 机·鸡 ----
    ('P02-009', 'patch.pak', 'datadf/1', '什么肛门',
     '  Yiffany: [纳—诺—迈—什么肛门？]',
     '  Yiffany: [纳——米——机……什么鸡？]'),
    ('P02-009', 'patch.pak', 'datadm/1', '什么肛门',
     '  Yiffai: [纳—诺—迈—什么肛门？]',
     '  Yiffai: [纳——米——机……什么鸡？]'),

    # ---- P07-025 beat off ----
    ('P07-025', 'patch.pak', 'vsn/41', '把他撸退',
     'text: ——总之！他手脚很不老实，我只好使尽浑身解数把他撸退！',
     'text: ——总之！他手脚很不老实，我只好使尽浑身解数把他打退！'),

    # ---- P10-011 take it / Just like he did ----
    ('P10-011', 'cosmobreeder-multi.jar', 'datadf/1', '拿走吧！就像他那样做的',
     '  * 这儿这个小色狼不值钱，拿走吧！就像他那样做的 ;3！',
     '  * 这儿这个小色狼不值钱，拿去用吧！就像他当初那样"用" ;3！'),
    ('P10-011', 'cosmobreeder-multi.jar', 'datadm/1', '拿走吧！就像他那样做的',
     '  * 这儿这个小色狼不值钱，拿走吧！就像他那样做的 ;3！',
     '  * 这儿这个小色狼不值钱，拿去用吧！就像他当初那样"用" ;3！'),
    ('P10-011', 'patch.pak', 'datadm/1', '拿走吧！就像他那样做的',
     '  * 这儿这个小色狼不值钱，拿走吧！就像他那样做的 ;3！',
     '  * 这儿这个小色狼不值钱，拿去用吧！就像他当初那样"用" ;3！'),
]


def sha(b):
    return sha256(b).hexdigest()


def main():
    archives = {n: zipfile.ZipFile(CAND / n) for n in ('cosmobreeder-multi.jar', 'patch.pak')}
    acc = json.loads((CAND / 'acceptance.json').read_text('utf-8')) if (CAND / 'acceptance.json').exists() else None
    cache, ledger = {}, []
    for n, (pid, archive, entry, anchor, old, new) in enumerate(EDITS, 1):
        key = (archive, entry)
        if key not in cache:
            cache[key] = decrypt_file(archives[archive].read(entry))
        text = cache[key].decode('utf-8')
        lines = text.splitlines()
        hits = [i for i, line in enumerate(lines) if anchor in line]
        if len(hits) != 1:
            raise SystemExit(f'{pid}: anchor {anchor!r} hit {len(hits)} times in {archive}/{entry}')
        idx = hits[0]
        if lines[idx] != old:
            raise SystemExit(f'{pid}: line {idx+1} mismatch\n  have={lines[idx]!r}\n  want={old!r}')
        ledger.append({
            'op_id': f'R5-{n:04d}',
            'archive': archive,
            'archive_entry': entry,
            'kind': 'line',
            'before_resource_sha256': sha(cache[key]),
            'old': old,
            'new': new,
            'finding_ids': [pid],
            'source_refs': [f'R1:{pid}', 'localization/editorial/r5-creative/reports/creative-01/decisions.tsv'],
            'line': idx + 1,
        })

    out = R5 / 'reports' / 'creative-01'
    out.mkdir(parents=True, exist_ok=True)
    ledger_path = LOC / 'translations' / 'editorial-r5-creative-repairs.jsonl'
    ledger_path.write_text('\n'.join(json.dumps(o, ensure_ascii=False) for o in ledger) + '\n',
                           encoding='utf-8')

    with (out / 'decisions.tsv').open('w', encoding='utf-8', newline='') as f:
        w = csv.writer(f, delimiter='\t', lineterminator='\n')
        w.writerow(['finding_id', 'disposition', 'pun_status', 'ops', 'note'])
        for pid, meta in GROUPS.items():
            w.writerow([pid, 'apply', meta['status'],
                        sum(1 for e in EDITS if e[0] == pid), meta['note']])

    print('ledger ops:', len(ledger), '->', ledger_path.relative_to(ROOT))
    for pid in GROUPS:
        print(' ', pid, GROUPS[pid]['status'], sum(1 for e in EDITS if e[0] == pid), 'ops')


if __name__ == '__main__':
    main()
