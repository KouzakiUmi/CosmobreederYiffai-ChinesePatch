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
}


def hashed(data):
    return sha256(data).hexdigest()


def main():
    p = argparse.ArgumentParser(description=__doc__)
    p.add_argument('batch', choices=sorted(BATCHES))
    p.add_argument('--snapshot', default='snapshot-03', choices=sorted(SNAPSHOTS))
    a = p.parse_args()
    SNAP = SNAPSHOTS[a.snapshot]
    title, root_list = BATCHES[a.batch]
    roots = set(root_list)
    scenes = json.loads((SNAP / 'scenes.json').read_text('utf8'))
    picked = [s for s in scenes if s['kind'] == 'dialogue' and s['root'].split('.')[0] in roots]
    if not picked:
        raise ValueError('empty batch')
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
        'batch': a.batch,
        'title': title,
        'roots': sorted(roots),
        'corpus_snapshot': SNAP.relative_to(ROOT).as_posix(),
        'current_zh_baseline_candidate': 'localization/builds/' + ('r9-polish-candidate13' if a.snapshot == 'snapshot-03' else 'r8-puzzle-candidate12'),
        'corpus_manifest_sha256': hashed((SNAP / 'manifest.json').read_bytes()),
        'corpus_status': manifest['status'],
        'current_zh_baseline': 'localization/builds/r8-puzzle-candidate12',
        'scenes': order_rows,
    }
    out = OUT_ROOT / a.batch / 'orders'
    out.mkdir(parents=True, exist_ok=True)
    (out / (a.batch + '.json')).write_text(
        json.dumps(order, ensure_ascii=False, indent=1) + '\n', encoding='utf8')
    lines = ['# %s 精校工单：%s' % (a.batch, title), '',
             '英文与当前中文都按整场连读；`current` 是 candidate12 的实际显示行。',
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
    (out / (a.batch + '.reader.md')).write_text('\n'.join(lines) + '\n', encoding='utf8')
    total = sum(len(s['rows']) for s in order_rows)
    chars = sum(len(r['source']) + len(r['current'] or '') for s in order_rows for r in s['rows'])
    print(json.dumps({'batch': a.batch, 'scenes': len(order_rows), 'rows': total,
                      'chars': chars, 'roots': sorted(roots),
                      'json': str((out / (a.batch + '.json')).relative_to(ROOT)),
                      'reader': str((out / (a.batch + '.reader.md')).relative_to(ROOT))},
                     ensure_ascii=False, indent=1))


if __name__ == '__main__':
    main()
