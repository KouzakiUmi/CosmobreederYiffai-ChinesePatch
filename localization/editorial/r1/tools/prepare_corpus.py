"""Read-only editorial snapshot of source, ledger and currently shipped Chinese.

No source/translation/resource writes. Outputs only a NEW directory under r1/corpus.
Grouping uses script entries and intact VSN files, not isolated translation units.
"""
from pathlib import Path
from collections import defaultdict, Counter
from hashlib import sha256
import argparse
import json
import re
import sys
import zipfile

ROOT = Path(__file__).resolve().parents[4]
LOC = ROOT / 'localization'
sys.path.insert(0, str(LOC / 'tools'))
from codec import decrypt_file
from projectlib import pointer_get


def hashed(data):
    return sha256(data).hexdigest()


def load(path):
    return [json.loads(line) for line in path.read_text('utf8').splitlines() if line.strip()]


def output(path, value):
    path.write_text(json.dumps(value, ensure_ascii=False, indent=2) + '\n', encoding='utf8')


def main():
    p = argparse.ArgumentParser(description=__doc__)
    p.add_argument('--candidate', type=Path, required=True)
    p.add_argument('--output', type=Path, required=True)
    p.add_argument('--packets', type=int, default=10)
    a = p.parse_args()
    candidate = a.candidate.resolve()
    out = a.output.resolve()
    allowed = (LOC / 'editorial/r1/corpus').resolve()
    if out.exists() or not out.is_relative_to(allowed) or out == allowed:
        raise ValueError('NEW r1/corpus child only')
    units = {r['id']: r for r in load(LOC / 'catalog/units.jsonl')}
    occurrences = load(LOC / 'catalog/occurrences.jsonl')
    translations = {r['id']: r for r in load(LOC / 'translations/zh-CN.jsonl')}
    resources = {r['logical_path']: r for r in load(LOC / 'catalog/resources.jsonl')}
    sfw = sum((load(LOC / ('optimization/r28/sfw/ledger-' + kind + '.jsonl'))
               for kind in ('ds', 'vsn', 'ui')), [])
    source_pins = {}
    pinpaths = [LOC / 'catalog' / name for name in ('units.jsonl', 'occurrences.jsonl', 'resources.jsonl')]
    pinpaths += [LOC / 'translations/zh-CN.jsonl', candidate / 'build-manifest.json']
    pinpaths += [LOC / ('optimization/r28/sfw/ledger-' + kind + '.jsonl') for kind in ('ds', 'vsn', 'ui')]
    for path in pinpaths:
        source_pins[path.relative_to(ROOT).as_posix()] = hashed(path.read_bytes())
    archives = {}
    for mode in ('sfw', 'nsfw'):
        name = 'cosmobreeder-multi.jar' if mode == 'sfw' else 'patch.pak'
        original = ROOT / 'backup' / name
        current = candidate / name
        archives[mode] = (zipfile.ZipFile(original), zipfile.ZipFile(current))
        for path in (original, current):
            source_pins[path.relative_to(ROOT).as_posix()] = hashed(path.read_bytes())
    cache = {}
    def lines(mode, entry):
        key = (mode, entry)
        if key not in cache:
            z0, z1 = archives[mode]
            before, after = (decrypt_file(z.read(entry)).decode('utf8') for z in (z0, z1))
            if len(before.splitlines()) != len(after.splitlines()):
                raise ValueError('Physical line mapping drift: ' + str(key))
            cache[key] = (before.splitlines(), after.splitlines())
        return cache[key]
    dictionaries = {}
    def dictionary(mode, entry):
        key=(mode,entry)
        if key not in dictionaries:
            dictionaries[key]=tuple(json.loads(decrypt_file(z.read(entry))) for z in archives[mode])
        return dictionaries[key]
    groups = {}
    row_ids = set()
    def group(mode, kind, logical, root, header_line=None):
        key = (mode, kind, logical, root, header_line)
        if key not in groups:
            identity = hashed(json.dumps(key, ensure_ascii=False).encode())[:16]
            groups[key] = {'scene_id': 'SC' + identity, 'mode': mode, 'kind': kind,
                           'logical_path': logical, 'root': root, 'source_header_line':header_line,
                           'rows': [], 'controls': []}
        return groups[key]
    def add(g, row):
        if row['review_row_id'] in row_ids:
            raise ValueError('Duplicate review row identity')
        row_ids.add(row['review_row_id']); g['rows'].append(row)
    for o in occurrences:
        u = units[o['unit_id']]; t = translations[u['id']]
        kind = u['category']; logical = o.get('logical_path',o.get('image_path',o['location'].split('#')[0]))
        root = o.get('entry', '') if kind == 'dialogue' else logical if kind == 'vsn' else ''
        if kind == 'ui':
            root = o.get('json_key',o.get('json_pointer','')).rsplit('.', 1)[0]
        if kind in ('code', 'image'):
            root = logical
        header_line=None
        if kind=='dialogue':
            before,_=lines('nsfw',o['archive_entry'])
            header_line=next((i+1 for i in range(o['line']-2,-1,-1) if before[i].strip()=='<'+root+'>'),None)
            if header_line is None:raise ValueError('Missing source header')
        g = group('nsfw' if kind in ('dialogue', 'vsn', 'ui') else 'catalog', kind, logical, root,header_line)
        row = {'review_row_id': 'CAT:' + o['occurrence_id'], 'unit_id': u['id'],
               'occurrence_id': o['occurrence_id'], 'source': u['source'],
               'source_sha256': u['source_sha256'], 'speaker': o.get('speaker', ''),
               'variant': u.get('variant', ''), 'location': o['location'],
               'prefix': o.get('prefix', ''), 'line': o.get('line'),
               'ledger_zh': t.get('translation') or t.get('draft') or '', 'ledger_status': t['status'],
               'current_line': None, 'current_kind': 'usage_unverified' if kind == 'code' else 'requires_image_review' if kind == 'image' else 'physical_line'}
        if kind in ('dialogue', 'vsn'):
            entry = o['archive_entry']
            # Catalog captures effective PAK sources; shared JAR-only entries retain their original provider.
            before, after = lines('nsfw', entry)
            row['current_line'] = after[o['line'] - 1]
            if u['source'] not in before[o['line'] - 1]:
                raise ValueError('Catalog source line mismatch: ' + o['occurrence_id'])
            row['archive_entry'] = entry
        elif kind == 'ui':
            provider='sfw' if o['archive']=='jar' else 'nsfw'
            original,current=dictionary(provider,o['archive_entry'])
            key=o.get('json_key'); pointer=o.get('json_pointer')
            oldvalue=original[key] if key is not None else pointer_get(original,pointer)
            newvalue=current[key] if key is not None else pointer_get(current,pointer)
            expected=o.get('leading_ws','') + u['source'] + o.get('trailing_ws','')
            if oldvalue != expected:
                raise ValueError('Dictionary identity drift: ' + str(key or pointer))
            row['current_line'] = newvalue
            row['current_kind'] = 'dictionary_value' if key is not None else 'nested_json_value_runtime_usage_check'
            row['json_key'] = key; row['json_pointer']=pointer; row['source_archive_provider']=o['archive']
        add(g, row)
    for r in sfw:
        kind = {'ds': 'dialogue', 'vsn': 'vsn', 'ui': 'ui'}[r['kind']]
        logical = r['logical_path']; root = r.get('root', '')
        if kind == 'vsn': root = logical
        if kind == 'ui': root = r.get('key', r.get('json_key', root)).rsplit('.', 1)[0]
        header_line=None
        if kind=='dialogue':
            before,_=lines('sfw',r['archive_entry']);n=r['source_line_evidence']
            header_line=next((i+1 for i in range(n-2,-1,-1) if before[i].strip()=='<'+root+'>'),None)
            if header_line is None:raise ValueError('Missing SFW source header')
        g = group('sfw', kind, logical, root,header_line)
        row = {'review_row_id': r['id'], 'unit_id': r.get('provenance', {}).get('unit_id'),
               'occurrence_id': r.get('provenance', {}).get('occurrence_id'),
               'source': r['raw_source'], 'source_sha256': r['raw_source_sha256'],
               'speaker': r.get('role', ''), 'variant': 'sfw', 'prefix': r.get('prefix', ''),
               'line': r.get('source_line_evidence'), 'location': logical + '#' + root + ':' + str(r.get('source_line_evidence', '')),
               'ledger_zh': r.get('translation', ''), 'ledger_status': r['status'],
               'archive_entry': r['archive_entry'], 'current_kind': 'physical_line'}
        if kind in ('dialogue', 'vsn'):
            before, after = lines('sfw', r['archive_entry'])
            n = r['source_line_evidence']; row['current_line'] = after[n - 1]
            if r['raw_source'] not in before[n - 1]:
                raise ValueError('SFW source line mismatch: ' + r['id'])
        else:
            key = r.get('key', r.get('json_key', r.get('root')))
            if key is None: raise ValueError('Missing SFW UI key')
            original,current=dictionary('sfw',r['archive_entry'])
            if original[key] != r['raw_source']: raise ValueError('SFW UI source mismatch')
            row['current_line'] = current[key]; row['current_kind'] = 'dictionary_value'; row['json_key'] = key
        add(g, row)
    # Capture every non-text control inside each DS entry / VSN file, including includes and conditionals.
    for g in groups.values():
        if g['kind'] not in ('dialogue', 'vsn'): continue
        mode = g['mode']; entry = g['rows'][0]['archive_entry']; before, after = lines(mode, entry)
        text_lines = {r['line'] for r in g['rows']}
        if g['kind'] == 'vsn':
            start, stop = 0, len(before)
        else:
            header = '<' + g['root'] + '>'
            starts = [i for i, value in enumerate(before) if value.strip() == header]
            start = g['source_header_line']-1
            if start not in starts:raise ValueError('Scene header identity drift')
            g['header_occurrence_index']=starts.index(start)
            stop = next((i for i in range(start + 1, len(before)) if re.match(r'^\s*<[^>]+>\s*$', before[i])), len(before))
        g['source_range'] = [start + 1, stop]
        g['controls'] = [{'line': i + 1, 'source': before[i], 'current': after[i]}
                         for i in range(start, stop) if i + 1 not in text_lines and before[i].strip()]
        for r in g['rows']:
            r['merged_or_blank_current'] = not bool(r['current_line'].strip())
    scenes = list(groups.values())
    for g in scenes:
        g['rows'].sort(key=lambda r: (r.get('line') or 0, r['review_row_id']))
    # Deduplicate only entire source+current scenes across edition aliases, never individual fragments.
    # Variant and logical path stay in the key: two protagonists are not collapsed together.
    canonical = {}; merged = []
    for g in scenes:
        signature = json.dumps([g['kind'], g['logical_path'], g['root'],g.get('header_occurrence_index'),
                                [(r['source'], r['prefix'], r['current_line']) for r in g['rows']],
                                [(r['source'], r['current']) for r in g['controls']]], ensure_ascii=False)
        key = hashed(signature.encode())
        alias = {'scene_id': g['scene_id'], 'mode': g['mode'],
                 'rows': [{k: r.get(k) for k in ('review_row_id', 'unit_id', 'occurrence_id', 'line', 'location')}
                          for r in g['rows']]}
        if key in canonical and canonical[key]['mode'] != g['mode']:
            canonical[key]['aliases'].append(alias)
        else:
            g['aliases'] = [alias]; canonical[key] = g; merged.append(g)
    # Semantic scene boundaries are intact. Balance by actual source/current text size.
    packets = [[] for _ in range(a.packets)]; weights = [0] * a.packets
    for g in sorted(merged, key=lambda g: sum(len(r['source']) + len(r['current_line'] or '') for r in g['rows']), reverse=True):
        i = min(range(a.packets), key=lambda n: weights[n])
        packets[i].append(g); weights[i] += sum(len(r['source']) + len(r['current_line'] or '') for r in g['rows'])
    out.mkdir(parents=True)
    (out / 'packets').mkdir()
    output(out / 'scenes.json', merged)
    receipts = []
    for i, pack in enumerate(packets, 1):
        pack.sort(key=lambda g: (g['kind'], g['logical_path'], g['root']))
        name = 'packet-%02d' % i
        output(out / 'packets' / (name + '.json'), pack)
        md = ['# ' + name, '', '逐场景通读；current是最终归档，ledger仅追溯。合句后空行不等于漏译。', '']
        for g in pack:
            md += ['## ' + g['scene_id'] + ' | ' + g['mode'] + ' | ' + g['logical_path'] + ' | ' + g['root'],
                   'ALIASES ' + json.dumps([{'mode': x['mode'], 'scene_id': x['scene_id']} for x in g['aliases']], ensure_ascii=False)]
            sequence = [(r.get('line') or 0, 'TEXT', r) for r in g['rows']]
            sequence += [(r['line'], 'CONTROL', r) for r in g['controls']]
            for _, kind, r in sorted(sequence, key=lambda x: x[0]):
                if kind == 'CONTROL':
                    md.append('CONTROL L%d %s' % (r['line'], r['source']))
                else:
                    md.append('ROW ' + json.dumps({k: r.get(k) for k in ('review_row_id', 'unit_id', 'occurrence_id', 'line', 'speaker', 'variant', 'source', 'current_line', 'ledger_zh', 'current_kind')}, ensure_ascii=False))
            md.append('')
        path = out / 'packets' / (name + '.md')
        path.write_text('\n'.join(md) + '\n', encoding='utf8')
        receipts.append({'packet': name, 'scene_ids': [g['scene_id'] for g in pack],
                         'scenes': len(pack), 'canonical_rows': sum(len(g['rows']) for g in pack),
                         'all_alias_rows': sum(len(x['rows']) for g in pack for x in g['aliases']),
                         'text_characters': weights[i - 1], 'markdown_lines': len(md), 'sha256': hashed(path.read_bytes())})
    covered_catalog = {r['unit_id'] for g in merged for x in g['aliases'] for r in x['rows'] if r.get('unit_id') in units}
    if covered_catalog != set(units): raise ValueError('Incomplete catalog coverage')
    output(out / 'manifest.json', {'schema': 'cosmo-editorial-corpus/v1', 'status': 'prepared_not_semantically_reviewed',
           'source_sha256': source_pins, 'catalog_units': len(units), 'catalog_occurrences': len(occurrences),
           'sfw_source_rows': len(sfw), 'all_source_rows': len(row_ids), 'canonical_scenes': len(merged),
           'canonical_rows': sum(len(g['rows']) for g in merged), 'covered_catalog_units': len(covered_catalog),
           'categories': dict(Counter(u['category'] for u in units.values())), 'packets': receipts,
           'notes': ['SFW/NSFW aliases deduplicated only for identical full scenes and identical controls/current text.',
                     'Script row position is an evidence anchor, not permission to translate fragments independently.',
                     'Code/image records are inventory only until player-facing usage/artwork is verified.',
                     'Catalog narrator metadata is not proof that every VSN line is narration. Read staging controls.',
                     'Empty current physical rows may be consumed by prior sentence joins; assess scene totals.']})
    for before, after in archives.values(): before.close(); after.close()
    print(json.dumps({'output': str(out.relative_to(ROOT)), 'source_rows': len(row_ids),
                      'scenes': len(merged), 'packets': receipts}, ensure_ascii=False, indent=2))


if __name__ == '__main__':
    main()
