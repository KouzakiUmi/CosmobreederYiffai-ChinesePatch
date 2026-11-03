"""Write the batch-15 order: the residual term/键名 spellings left behind.

Every row here sits inside a scene an earlier batch already polished, so this is
not a new coverage batch — it is the cleanup pass the LEFTOVERS ledger has been
promising since R9 batch-09. The rows are selected by spelling, not by root: the
scan in `VARIANTS` finds the minority form, and each hit becomes one decision with
the majority form as the replacement.

The order keeps whole scenes (not bare rows) so the ledger builder sees the same
row context the earlier batches did.
"""
from pathlib import Path
from hashlib import sha256
import json
import sys

R9 = Path(__file__).resolve().parents[1]
ROOT = R9.parents[2]
SNAP = ROOT / 'localization/editorial/r1/corpus/snapshot-03'
OUT = R9 / 'batch-15/orders'

# minority spelling -> (replacement, rationale)
VARIANTS = {
    '狗头人': ('科博德', 'kobold 在库内作「科博德」99 处、「狗头人」10 处'),
    '吠叫者': ('吠犬', 'BARKER 在库内作「吠犬」40 处、「吠叫者」1 处'),
    '探员': ('特工', 'agent 在库内作「特工」471 处、「探员」3 处'),
    '宇航服': ('宇宙服', 'COSMOSUIT 在库内作「宇宙服」19 处、「宇航服」9 处'),
    '电击器': ('电击枪', 'TAZER 在库内作「电击枪」92 处、「电击器」10 处，其中一处是早前批次反向改出来的'),
    'UP+攻击': ('UP+ATTACK', '按键名一律保留英文（R9 batch-01 已裁决）'),
    'DOWN+攻击': ('DOWN+ATTACK', '按键名一律保留英文（R9 batch-01 已裁决）'),
    '高级芯片': ('花哨芯片', 'FANCY CHIPS 在库内作「花哨芯片」3 处、「高级芯片」1 处'),
    '卫星通讯': ('卫星链路', 'SATLINK 在库内作「卫星链路」3 处、「卫星通讯」1 处'),
}


def live_text(candidate, row, mode, root):
    """The base candidate's current text for this row.

    The cleanup batch cannot quote `snapshot-03`: earlier batches already edited
    some of these very rows, so the order has to describe the archive the ledger
    will apply against, or `build_ledger` reports baseline drift.
    """
    import r9_targets
    archive, entry, kind, loc_name, locator = target_of_live(row, mode, candidate, root)
    state, digest = r9_targets.resource_state(candidate, archive, entry, kind)
    return r9_targets.old_text(state, kind, locator, row), archive, entry, digest


def target_of_live(row, mode, candidate, root):
    import r9_targets
    # `target_of` expects the order's row shape, where the id is `row_id`.
    proxy = dict(row, row_id=row.get('review_row_id') or row.get('occurrence_id'))
    return r9_targets.target_of(proxy, mode, candidate, root)


def main():
    import argparse
    ap = argparse.ArgumentParser()
    ap.add_argument('--base', required=True, help='candidate directory name under localization/builds')
    a = ap.parse_args()
    candidate = ROOT / 'localization/builds' / a.base
    scenes = json.loads((SNAP / 'scenes.json').read_text('utf8'))
    hits = {}
    for scene in scenes:
        rows = []
        for row in scene['rows']:
            current = row.get('current_line') or ''
            for bad in VARIANTS:
                if bad in current:
                    rows.append(row)
                    hits.setdefault(bad, []).append((scene['root'], row.get('line')))
                    break
        if rows:
            scene['_hits'] = rows
            scene['_live'] = {}
            # Every row of the scene needs the live text, not just the hits: the
            # ledger builder compares the whole batch against its base.
            for row in scene['rows']:
                row_id = row.get('review_row_id') or row.get('occurrence_id')
                text, archive, entry, digest = live_text(candidate, row, scene['mode'], scene['root'])
                scene['_live'][row_id] = (text, archive, entry, digest)
    picked = [s for s in scenes if s.get('_hits')]
    picked.sort(key=lambda s: (s['root'], s['logical_path'], s['scene_id']))

    out = {
        'schema': 'r9-batch-order/v1',
        'batch': 'batch-15',
        'batch_group': 'batch-15',
        'part': 1,
        'parts': 1,
        'title': '术语与按键名残留清理（前批遗留的少数写法）',
        'roots': sorted({s['root'].split('.')[0] for s in picked}),
        'corpus_snapshot': 'snapshot-03',
        'current_zh_baseline_candidate': 'candidate13',
        'corpus_manifest_sha256': '',
        'corpus_status': 'snapshot-03',
        'current_zh_baseline': 'snapshot-03',
        'scenes': [],
    }
    for scene in picked:
        out['scenes'].append({
            'scene_id': scene['scene_id'],
            'mode': scene['mode'],
            'logical_path': scene['logical_path'],
            'root': scene['root'],
            'header_line': scene.get('source_header_line'),
            'controls': scene.get('controls') or [],
            'rows': [{
                'row_id': row.get('review_row_id') or row.get('occurrence_id'),
                'line': row.get('line'),
                'speaker': row.get('speaker') or '',
                'variant': row.get('variant') or '',
                'current_kind': row.get('current_kind'),
                'archive_entry': scene['_live'][row.get('review_row_id') or row.get('occurrence_id')][2]
                if row.get('review_row_id') or row.get('occurrence_id') in scene['_live']
                else row.get('archive_entry'),
                'source': row.get('source') or '',
                'current': scene['_live'][row.get('review_row_id') or row.get('occurrence_id')][0]
                if (row.get('review_row_id') or row.get('occurrence_id')) in scene['_live']
                else (row.get('current_line') or ''),
            } for row in scene['rows']],
        })

    OUT.mkdir(parents=True, exist_ok=True)
    (OUT / 'batch-15.json').write_text(json.dumps(out, ensure_ascii=False, indent=1) + '\n', encoding='utf8')
    total = sum(len(s['rows']) for s in picked)
    print('scenes %d | rows %d | hits %d' % (len(picked), total, sum(len(v) for v in hits.values())))
    for bad, places in sorted(hits.items(), key=lambda kv: -len(kv[1])):
        print('  %-8s -> %-10s %2d  %s' % (bad, VARIANTS[bad][0], len(places),
                                           '; '.join('%s:%s' % p for p in places[:3])))


if __name__ == '__main__':
    main()
