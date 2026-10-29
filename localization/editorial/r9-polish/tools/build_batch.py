"""Build one r9-polish batch order from the candidate-bound corpus snapshot.

Read-only over the snapshot; writes only under r9-polish/batch-NN/orders.
Every row keeps its review_row_id / physical line / source, so a later proposal
can be bound back to the same node without re-reading the archive.
"""
from pathlib import Path
from hashlib import sha256
import argparse
import json

ROOT = Path(__file__).resolve().parents[4]
SNAP_DEFAULT = ROOT / 'localization/editorial/r1/corpus/snapshot-03'
SNAPSHOTS = {'snapshot-02': ROOT / 'localization/editorial/r1/corpus/snapshot-02',
             'snapshot-03': SNAP_DEFAULT}
OUT_ROOT = ROOT / 'localization/editorial/r9-polish'

# Priority batches from the R1 rewrite plan, section eight.
# Each entry also records the dialogue roots excluded from the batch (e.g. a
# single root that is large enough to deserve its own batch).
BATCHES = {
    'batch-01': ('开场与第一区无线电教学',
                 ['The0', 'Area0_Macsen1', 'Area0_Macsen2', 'Area0_MacsenBar',
                  'Area0_Prison1', 'MauserHints_AreaA']),
    'batch-02': ('雄猫支援线（核心人物往来之一）', ['Tomcat']),
    'batch-03': ('波苏指挥线（核心人物往来之二）', ['Bossu']),
    # The next priority in the plan is support-side lore and gameplay text, which
    # is dominated by two very large roots. They are split so each batch stays
    # readable in full: Mauser's item/equipment lines, then the codex.
    'batch-04': ('毛鼠支援线与装备说明（装备与情报）', ['Mauser']),
    'batch-05': ('图鉴与首领资料（图鉴与装备）', ['BossuDex']),
    'batch-06': ('雄猫道具与商店线（道具说明）', ['TomcatItems']),
    'batch-07': ('结局与开场演出（结局与平行版本）',
             ['vsn/f_EndingBad/script', 'vsn/f_EndingGood/script',
             'vsn/f_EndingIntoShmup/script', 'vsn/f_GameOverArea0/script',
             'vsn/f_GameOverAreaA/script', 'vsn/f_GameOverAreaB/script',
             'vsn/f_GameOverAreaC/script', 'vsn/f_GameOverAreaE/script',
             'vsn/f_GameStart/script', 'vsn/m_EndingBad/script',
             'vsn/m_EndingGood/script', 'vsn/m_EndingIntoShmup/script',
             'vsn/m_GameOverArea0/script', 'vsn/m_GameOverAreaA/script',
             'vsn/m_GameOverAreaB/script', 'vsn/m_GameOverAreaC/script',
             'vsn/m_GameOverAreaE/script', 'vsn/m_GameStart/script'], ['vsn']),
             'batch-08': ('VSN 剧情场景脚本（结局与平行版本）',
             ['vsn/ClassicPreTitle/script', 'vsn/f_AgentF01/script',
             'vsn/f_AgentF02/script', 'vsn/f_AgentF03/script',
             'vsn/f_AgentF04/script', 'vsn/f_AgentF05/script',
             'vsn/f_AgentF06/script', 'vsn/f_AgentF07/script',
             'vsn/f_AgentF08/script', 'vsn/f_AgentF0B/script',
             'vsn/f_AgentFZ1/script', 'vsn/f_AgentFZ2/script',
             'vsn/f_AgentFZ3/script', 'vsn/f_AgentFZ4/script',
             'vsn/f_AgentFZ5/script', 'vsn/f_AgentFZ6/script',
             'vsn/f_ClassicBigbold/script', 'vsn/f_ClassicBigboldV2/script',
             'vsn/f_ClassicBossRedbull/script', 'vsn/f_ClassicEnelye/script',
             'vsn/f_ClassicPigobinV3/script', 'vsn/f_ClassicSqueakerBoss/script',
             'vsn/f_ClassicStarkillV3/script', 'vsn/f_ClassicWerehund/script',
             'vsn/f_ClassicWerepup/script', 'vsn/m_AgentM01/script',
             'vsn/m_AgentM02/script', 'vsn/m_AgentM03/script',
             'vsn/m_AgentM04/script', 'vsn/m_AgentM05/script',
             'vsn/m_AgentM06/script', 'vsn/m_AgentM07/script',
             'vsn/m_AgentM08/script', 'vsn/m_AgentM0B/script',
             'vsn/m_AgentMZ1/script', 'vsn/m_AgentMZ2/script',
             'vsn/m_AgentMZ3/script', 'vsn/m_AgentMZ4/script',
             'vsn/m_AgentMZ5/script', 'vsn/m_AgentMZ6/script',
             'vsn/m_ClassicBigbold/script', 'vsn/m_ClassicBigboldV2/script',
             'vsn/m_ClassicBossRedbull/script', 'vsn/m_ClassicEnelye/script',
             'vsn/m_ClassicPigobinV3/script', 'vsn/m_ClassicSqueakerBoss/script',
             'vsn/m_ClassicStarkillV3/script', 'vsn/m_ClassicWerehund/script',
             'vsn/m_ClassicWerepup/script'], ['vsn']),
             'batch-09': ('区域场景与条件分支（关卡救援与分支）',
             ['AreaA_Cellar', 'AreaA_Macsen1', 'AreaA_Macsen2', 'AreaA_Prison1',
             'AreaA_Prison2', 'AreaA_Prison3', 'AreaB_Macsen1', 'AreaB_Macsen2',
             'AreaB_MacsenBar', 'AreaB_Prison1', 'AreaB_Prison2', 'AreaB_Slaver2',
             'AreaC_Macsen1', 'AreaC_MacsenDark', 'AreaC_Prison1', 'AreaC_Prison2',
             'AreaC_Prison3', 'AreaC_Slaver1', 'AreaE_Macsen1', 'AreaH_Cellar',
             'AreaH_MacsenBar', 'AreaH_MacsenBreeding', 'AreaH_MacsenMechanic',
             'AreaH_Ship', 'AreaX_Upgrade', 'Fenfen_Shared', 'Gitgud',
             'Hacker_Shared', 'Macsen_Shared', 'Prison_Shared', 'Proto_Fenfen',
             'Proto_PrisonKey', 'Proto_PrisonTazer', 'Queen', 'Test_Hacker1',
             'Test_Prison1', 'Test_Slaver1']),
             'batch-10': ('界面与系统文本（UI 与其他）',
             ['ui', '/patchDictionary/navmap', 'input', 'navmap', 'save',
             'MauserHints', 'MauserHints_Area0', 'MauserHints_AreaB',
             'MauserHints_AreaC', 'MauserHints_AreaE', 'MauserHints_AreaH'], ['ui']),
             'batch-11': ('其余零散条目（风格与文笔）',
             ['/missionLog/female/0/header', '/missionLog/female/0/locationName',
             '/missionLog/female/0/subject', '/missionLog/female/0/text',
             '/missionLog/female/1/header', '/missionLog/female/1/locationName',
             '/missionLog/female/1/subject', '/missionLog/female/1/text',
             '/missionLog/female/10/header', '/missionLog/female/10/locationName',
             '/missionLog/female/10/subject', '/missionLog/female/10/text',
             '/missionLog/female/11/header', '/missionLog/female/11/locationName',
             '/missionLog/female/11/subject', '/missionLog/female/11/text',
             '/missionLog/female/12/header', '/missionLog/female/12/locationName',
             '/missionLog/female/12/subject', '/missionLog/female/12/text',
             '/missionLog/female/13/header', '/missionLog/female/13/locationName',
             '/missionLog/female/13/subject', '/missionLog/female/13/text',
             '/missionLog/female/14/header', '/missionLog/female/14/locationName',
             '/missionLog/female/14/subject', '/missionLog/female/14/text',
             '/missionLog/female/15/header', '/missionLog/female/15/locationName',
             '/missionLog/female/15/subject', '/missionLog/female/15/text',
             '/missionLog/female/16/header', '/missionLog/female/16/locationName',
             '/missionLog/female/16/subject', '/missionLog/female/16/text',
             '/missionLog/female/17/header', '/missionLog/female/17/locationName',
             '/missionLog/female/17/subject', '/missionLog/female/17/text',
             '/missionLog/female/18/header', '/missionLog/female/18/locationName',
             '/missionLog/female/18/subject', '/missionLog/female/18/text',
             '/missionLog/female/19/header', '/missionLog/female/19/locationName',
             '/missionLog/female/19/subject', '/missionLog/female/19/text',
             '/missionLog/female/2/header', '/missionLog/female/2/locationName',
             '/missionLog/female/2/subject', '/missionLog/female/2/text',
             '/missionLog/female/3/header', '/missionLog/female/3/locationName',
             '/missionLog/female/3/subject', '/missionLog/female/3/text',
             '/missionLog/female/4/header', '/missionLog/female/4/locationName',
             '/missionLog/female/4/subject', '/missionLog/female/4/text',
             '/missionLog/female/5/header', '/missionLog/female/5/locationName',
             '/missionLog/female/5/subject', '/missionLog/female/5/text',
             '/missionLog/female/6/header', '/missionLog/female/6/locationName',
             '/missionLog/female/6/subject', '/missionLog/female/6/text',
             '/missionLog/female/7/header', '/missionLog/female/7/locationName',
             '/missionLog/female/7/subject', '/missionLog/female/7/text',
             '/missionLog/female/8/header', '/missionLog/female/8/locationName',
             '/missionLog/female/8/subject', '/missionLog/female/8/text',
             '/missionLog/female/9/header', '/missionLog/female/9/locationName',
             '/missionLog/female/9/subject', '/missionLog/female/9/text',
             '/missionLog/male/0/header', '/missionLog/male/0/locationName',
             '/missionLog/male/0/subject', '/missionLog/male/0/text',
             '/missionLog/male/1/header', '/missionLog/male/1/locationName',
             '/missionLog/male/1/subject', '/missionLog/male/1/text',
             '/missionLog/male/10/header', '/missionLog/male/10/locationName',
             '/missionLog/male/10/subject', '/missionLog/male/10/text',
             '/missionLog/male/11/header', '/missionLog/male/11/locationName',
             '/missionLog/male/11/subject', '/missionLog/male/11/text',
             '/missionLog/male/12/header', '/missionLog/male/12/locationName',
             '/missionLog/male/12/subject', '/missionLog/male/12/text',
             '/missionLog/male/13/header', '/missionLog/male/13/locationName',
             '/missionLog/male/13/subject', '/missionLog/male/13/text',
             '/missionLog/male/14/header', '/missionLog/male/14/locationName',
             '/missionLog/male/14/subject', '/missionLog/male/14/text',
             '/missionLog/male/15/header', '/missionLog/male/15/locationName',
             '/missionLog/male/15/subject', '/missionLog/male/15/text',
             '/missionLog/male/16/header', '/missionLog/male/16/locationName',
             '/missionLog/male/16/subject', '/missionLog/male/16/text',
             '/missionLog/male/17/header', '/missionLog/male/17/locationName',
             '/missionLog/male/17/subject', '/missionLog/male/17/text',
             '/missionLog/male/18/header', '/missionLog/male/18/locationName',
             '/missionLog/male/18/subject', '/missionLog/male/18/text',
             '/missionLog/male/19/header', '/missionLog/male/19/locationName',
             '/missionLog/male/19/subject', '/missionLog/male/19/text',
             '/missionLog/male/2/header', '/missionLog/male/2/locationName',
             '/missionLog/male/2/subject', '/missionLog/male/2/text',
             '/missionLog/male/3/header', '/missionLog/male/3/locationName',
             '/missionLog/male/3/subject', '/missionLog/male/3/text',
             '/missionLog/male/4/header', '/missionLog/male/4/locationName',
             '/missionLog/male/4/subject', '/missionLog/male/4/text',
             '/missionLog/male/5/header', '/missionLog/male/5/locationName',
             '/missionLog/male/5/subject', '/missionLog/male/5/text',
             '/missionLog/male/6/header', '/missionLog/male/6/locationName',
             '/missionLog/male/6/subject', '/missionLog/male/6/text',
             '/missionLog/male/7/header', '/missionLog/male/7/locationName',
             '/missionLog/male/7/subject', '/missionLog/male/7/text',
             '/missionLog/male/8/header', '/missionLog/male/8/locationName',
             '/missionLog/male/8/subject', '/missionLog/male/8/text',
             '/missionLog/male/9/header', '/missionLog/male/9/locationName',
             '/missionLog/male/9/subject', '/missionLog/male/9/text',
             '/shops/female/Area0_Macsen1/products/2/displayName',
             '/shops/male/Area0_Macsen1/products/2/displayName', 'AnomalyAlpha',
             'AnomalyBeta', 'AnomalyGamma', 'AnomalyOmicron', 'AttackElixir',
             'BarLectReward', 'Bomb', 'CheatGiveAll', 'ClassicArcher',
             'ClassicBarker', 'ClassicBat', 'ClassicBigbold', 'ClassicBigboldEnemy',
             'ClassicBigboldV2', 'ClassicBlocker', 'ClassicBossPigobinGhostAdd',
             'ClassicBossPigobinTriforce', 'ClassicBossRedbull',
             'ClassicBossRedbullFire', 'ClassicBossRedbullSecond',
             'ClassicBugFlier', 'ClassicBugLarva', 'ClassicBugSpiker',
             'ClassicBulber', 'ClassicBullfrog', 'ClassicBumper', 'ClassicBumperC',
             'ClassicBumperPlus', 'ClassicCannonCeiling', 'ClassicCannonCeilingC',
             'ClassicCannonFloor', 'ClassicCannonFloorC', 'ClassicCannonWall',
             'ClassicCannonWallC', 'ClassicCeilingTurret', 'ClassicCrawly',
             'ClassicCrusher', 'ClassicDragonV2Hand', 'ClassicDragonV2HandPhase2',
             'ClassicDragonV2Phase1', 'ClassicDragonV2Phase2',
             'ClassicDragonV2Phase3', 'ClassicDragonV2Phase3Fenfen',
             'ClassicDragonV2Phase3Head', 'ClassicDriller', 'ClassicDwarf',
             'ClassicDwarfAdd', 'ClassicDwarfThrower', 'ClassicElf',
             'ClassicEnelye', 'ClassicEnelyeBulb', 'ClassicEnelyeMoon',
             'ClassicEnelyeSpiritFire', 'ClassicFenfen', 'ClassicFire',
             'ClassicFlamer', 'ClassicFlappy', 'ClassicFlyDrone', 'ClassicFlybomb',
             'ClassicGhoster', 'ClassicGoatboss', 'ClassicGoatbossHead',
             'ClassicHopper', 'ClassicIvyball', 'ClassicIvyshoot',
             'ClassicJellyfish', 'ClassicKingbold', 'ClassicKingboldFire',
             'ClassicKobold', 'ClassicMine', 'ClassicMineCeiling',
             'ClassicMineCeilingZero', 'ClassicMineWall', 'ClassicMineWallZero',
             'ClassicMineZero', 'ClassicOmegoblin', 'ClassicOmegothrower',
             'ClassicOrber', 'ClassicQueenCrystalSpiritFire', 'ClassicQueenHead',
             'ClassicQueenLarva', 'ClassicQueenShadow', 'ClassicQueenSpaceGhost',
             'ClassicSalamanderPriest', 'ClassicSalamanderknight',
             'ClassicShieldGenerator', 'ClassicSlime', 'ClassicSpaceBugFlier',
             'ClassicSpaceHead', 'ClassicSpiderbot', 'ClassicSpikeball',
             'ClassicSpikebot', 'ClassicSqueaker', 'ClassicSqueakerBoss',
             'ClassicStarkillV1', 'ClassicStarkillV2Female',
             'ClassicStarkillV2Male', 'ClassicStarkillV3Female',
             'ClassicStarkillV3Fire', 'ClassicStarkillV3Male', 'ClassicSwiper',
             'ClassicTentacle', 'ClassicThorner', 'ClassicTribulb', 'ClassicViner',
             'ClassicWerehund', 'ClassicWerepup', 'ClassicWyvern',
             'ClassicXCannonCeiling', 'ClassicXCannonFloor', 'ClassicXCannonWall',
             'ClassicXeno', 'CosmoBody', 'CosmoCardBarker', 'CosmoCardBigbold',
             'CosmoCardDragon', 'CosmoCardDwarf', 'CosmoCardElf', 'CosmoCardEnelye',
             'CosmoCardKobold', 'CosmoCardOmegobin', 'CosmoCardPigobin',
             'CosmoCardRedbull', 'CosmoCardSqueaker', 'CosmoCardStarkill',
             'CosmoCardSwiper', 'CosmoCardWerehund', 'CosmoCardWerepup',
             'CosmoCardWyvern', 'CosmoHead', 'DataDisk', 'DefeatHints',
             'DefenseElixir', 'DoggyBody', 'DoggyHead', 'ElfBody', 'ElfHead',
             'FakeDrumstick', 'FakeMeat', 'FakeMilk', 'FakeTea', 'GasMask',
             'IceCola', 'JudoBody', 'JudoHead', 'Key', 'KoboBody', 'KoboHead',
             'Lect', 'LuckyBody', 'LuckyBodyNotUpgraded', 'LuckyHead',
             'LuckyHeadNotUpgraded', 'Luckybody', 'Pickaxe', 'PirateBody',
             'PirateHead', 'Powerpak', 'PsyBottle', 'PsyCoffee', 'PsyCrystal',
             'PsyCrystalBig', 'PsyJuice', 'PsySyrup', 'PsyTea', 'PsyUp', 'PsyWine',
             'Rock', 'ShipGun', 'ShipRadar', 'ShipShield', 'ShipTurbo',
             'SlimePotion', 'SpecialAnklet', 'SpecialBrace', 'SpecialBuckler',
             'SpecialCosmoID', 'SpecialFap', 'SpecialFeather', 'SpecialFlippers',
             'SpecialGeiger', 'SpecialHighBoots', 'SpecialHookshot',
             'SpecialKeycard0', 'SpecialKeycard1', 'SpecialKeycard2',
             'SpecialKeycard3', 'SpecialKeycard4', 'SpecialLabel',
             'SpecialLeftmark', 'SpecialLotion', 'SpecialNecklace',
             'SpecialPowermark', 'SpecialPsycards', 'SpecialRadio',
             'SpecialRightmark', 'SpecialShoes', 'SpecialTorch', 'SpecialWhistle',
             'SpecialZentaiSuit', 'Starkill', 'StatCheese', 'StatCherry',
             'StatCream', 'StatFishtaco', 'StatFortune', 'StatMelon', 'StatNut',
             'StatOctopus', 'StatPepper', 'StatPretzel', 'StatSpirit',
             'StatTadpole', 'Statcoin', 'Static', 'TazerAttuned',
             'TazerAttunedNotUpgraded', 'TazerCombat', 'TazerKobo', 'TazerPirate',
             'TazerRapier', 'TazerTomahawk', 'TazerTrainee', 'TazerTrainer',
             'ThrowKnife', 'ThrownC4', 'TribalBody', 'TribalHead', 'UpgradeChip',
             'VitBone', 'VitDrumstick', 'VitHam', 'VitMeat', 'VitSkull', 'Vitamin',
             'ZenerCircle', 'ZenerCross', 'ZenerSquare', 'ZenerStar',
             'ZenerTriangle', 'ZenerWaves', 'area']),
}


def hashed(data):
    return sha256(data).hexdigest()


def main():
    p = argparse.ArgumentParser(description=__doc__)
    p.add_argument('batch', choices=sorted(BATCHES))
    p.add_argument('--snapshot', default='snapshot-03', choices=sorted(SNAPSHOTS))
    p.add_argument('--part', type=int, default=1, help='1-based part when the batch is split')
    p.add_argument('--parts', type=int, default=1, help='split the batch into this many parts')
    a = p.parse_args()
    SNAP = SNAPSHOTS[a.snapshot]
    entry = BATCHES[a.batch]
    title, root_list = entry[0], entry[1]
    # 'dialogue' unless the batch says otherwise: the ending/VSN and interface
    # batches are stored under other kinds, and filtering them to dialogue
    # silently yields an empty batch.
    kinds = set(entry[2]) if len(entry) > 2 else {'dialogue'}
    roots = set(root_list)
    scenes = json.loads((SNAP / 'scenes.json').read_text('utf8'))
    picked = [s for s in scenes if s['kind'] in kinds and s['root'].split('.')[0] in roots]
    if not picked:
        raise ValueError('empty batch')
    if a.parts < 1 or not 1 <= a.part <= a.parts:
        raise ValueError('part must be within 1..parts')
    if a.parts > 1:
        # Split on scene boundaries, balanced by source+current text size, so a
        # part never breaks a scene in half.
        def weight(scene):
            return sum(len(r['source']) + len(r['current_line'] or '') for r in scene['rows'])
        buckets = [[] for _ in range(a.parts)]
        loads = [0] * a.parts
        for scene in sorted(picked, key=weight, reverse=True):
            i = min(range(a.parts), key=lambda n: loads[n])
            buckets[i].append(scene)
            loads[i] += weight(scene)
        picked = sorted(buckets[a.part - 1], key=lambda s: (s['root'], s['mode'], s['scene_id']))
        if not picked:
            raise ValueError('empty part')
    order_rows = []
    for s in sorted(picked, key=lambda s: (s['root'], s['mode'], s['scene_id'])):
        order_rows.append({
            'scene_id': s['scene_id'], 'mode': s['mode'], 'logical_path': s['logical_path'],
            'root': s['root'], 'header_line': s['source_header_line'],
            'controls': s['controls'],
            'rows': [{'row_id': r['review_row_id'], 'line': r['line'], 'speaker': r['speaker'],
                      'variant': r['variant'], 'current_kind': r['current_kind'],
                      'archive_entry': r.get('archive_entry'),
                      'source': r['source'], 'current': r['current_line']} for r in s['rows']],
        })
    manifest = json.loads((SNAP / 'manifest.json').read_text('utf8'))
    order = {
        'schema': 'cosmo-r9-polish-order/v1',
        'batch': a.batch if a.parts == 1 else '%s-part%02d' % (a.batch, a.part),
        'batch_group': a.batch,
        'part': a.part if a.parts > 1 else None,
        'parts': a.parts if a.parts > 1 else None,
        'title': title if a.parts == 1 else '%s（第 %d／%d 部分）' % (title, a.part, a.parts),
        'roots': sorted(roots),
        'corpus_snapshot': SNAP.relative_to(ROOT).as_posix(),
        'current_zh_baseline_candidate': 'localization/builds/' + ('r9-polish-candidate13' if a.snapshot == 'snapshot-03' else 'r8-puzzle-candidate12'),
        'corpus_manifest_sha256': hashed((SNAP / 'manifest.json').read_bytes()),
        'corpus_status': manifest['status'],
        'current_zh_baseline': 'localization/builds/r8-puzzle-candidate12',
        'scenes': order_rows,
    }
    name = order['batch']
    out = OUT_ROOT / name / 'orders'
    out.mkdir(parents=True, exist_ok=True)
    (out / (name + '.json')).write_text(
        json.dumps(order, ensure_ascii=False, indent=1) + '\n', encoding='utf8')
    lines = ['# %s 精校工单：%s' % (name, order['title']), '',
             '英文与当前中文都按整场连读；`current` 是 candidate13 的实际显示行。',
             'ROW 行的 `line` 是归档物理行号，`row_id` 是稳定节点；CONTROL 是脚本控制行，不改。', '']
    for s in order_rows:
        lines.append('## %s | %s | %s | %s' % (s['scene_id'], s['mode'], s['logical_path'], s['root']))
        seq = [(c['line'], 'CONTROL', c) for c in s['controls']]
        seq += [(r['line'] or 0, 'ROW', r) for r in s['rows']]
        for line_no, kind, item in sorted(seq, key=lambda x: x[0]):
            if kind == 'CONTROL':
                lines.append('CONTROL L%d  %s' % (line_no, item['source']))
            else:
                lines.append('ROW %s L%d %s %s' % (item['row_id'], item['line'] or 0,
                                                   item['speaker'] or '-', item['current_kind']))
                lines.append('  EN: ' + item['source'])
                lines.append('  ZH: ' + (item['current'] if item['current'] is not None else '<none>'))
        lines.append('')
    (out / (name + '.reader.md')).write_text('\n'.join(lines) + '\n', encoding='utf8')
    total = sum(len(s['rows']) for s in order_rows)
    chars = sum(len(r['source']) + len(r['current'] or '') for s in order_rows for r in s['rows'])
    print(json.dumps({'batch': name, 'scenes': len(order_rows), 'rows': total,
                      'chars': chars, 'roots': sorted(roots),
                      'json': str((out / (name + '.json')).relative_to(ROOT)),
                      'reader': str((out / (name + '.reader.md')).relative_to(ROOT))},
                     ensure_ascii=False, indent=1))


if __name__ == '__main__':
    main()
