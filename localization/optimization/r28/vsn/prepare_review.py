"""Reproduce the frozen PAK review packet; writes only this VSN directory."""
from pathlib import Path
from collections import defaultdict
import json
import sys
import zipfile

HERE = Path(__file__).resolve().parent
ROOT = HERE.parents[3]
sys.path.insert(0, str(ROOT / 'localization/tools'))
from codec import decrypt_file
from projectlib import read_jsonl


def prepare():
    loc = ROOT / 'localization'
    audit = json.loads((ROOT / 'docs/font-layout-audit-20261025/text-review/results/vsn-merge-candidates.json').read_text('utf8'))
    occs = {(o['logical_path'], o['line']): o for o in read_jsonl(loc / 'catalog/occurrences.jsonl') if o['category'] == 'vsn'}
    units = {u['id']: u for u in read_jsonl(loc / 'catalog/units.jsonl')}
    trs = {t['id']: t for t in read_jsonl(loc / 'translations/zh-CN.jsonl')}
    resources = {r['logical_path']: r for r in read_jsonl(loc / 'catalog/resources.jsonl')}
    with zipfile.ZipFile(loc / 'builds/r27-story12-shaderfix-test5/patch.pak') as z:
        index = json.loads(decrypt_file(z.read('vsn/0')))
        scripts = {'vsn/' + p.strip('/').split('/')[-2] + '/script.vsn': decrypt_file(z.read('vsn/' + str(e))) for p, e in index.items() if p.endswith('/script.vsn')}
    groups = []
    for c in audit['candidates']:
        path, (a, b) = c['logical_path'], c['lines']
        if groups and groups[-1]['logical_path'] == path and groups[-1]['lines'][-1] == a:
            groups[-1]['lines'].append(b)
            groups[-1]['edges'].append(c)
        else:
            groups.append({'group_id': f'VG{len(groups)+1:03}', 'logical_path': path, 'lines': [a, b], 'prefix': c['prefix'], 'edges': [c]})
    packet = []
    for g in groups:
        p = g['logical_path']
        cn = scripts[p].decode('utf8').splitlines()
        en = (loc / resources[p]['blob_path']).read_text('utf8').splitlines()
        a, b = g['lines'][0], g['lines'][-1]
        lo, hi = a-1, b
        while lo > 0 and not (cn[lo-1].strip() == '' and lo < a-1): lo -= 1
        while hi < len(cn) and cn[hi].strip(): hi += 1
        g['context_lines'] = [{'line': n, 'source': en[n-1], 'localized': cn[n-1]} for n in range(lo+1, hi+1)]
        g['inputs'] = []
        for n in g['lines']:
            o = occs[p, n]; u = units[o['unit_id']]
            g['inputs'].append({'occurrence': o, 'unit': u, 'translation': trs[o['unit_id']]})
        packet.append(f"{g['group_id']} {p} {g['lines']} {g['prefix']}")
        for row in g['context_lines']:
            star = '*' if row['line'] in g['lines'] else ' '
            packet.append(f"{star}{row['line']} {row['source']} || {row['localized']}")
        packet.append('')
    (HERE / 'review-packet.txt').write_text('\n'.join(packet), 'utf8')
    (HERE / 'review-packet.json').write_text(json.dumps(groups, ensure_ascii=False, indent=2), 'utf8')
    print(f'{len(groups)} groups, {sum(len(g["edges"]) for g in groups)} edges')

if __name__ == '__main__': prepare()
