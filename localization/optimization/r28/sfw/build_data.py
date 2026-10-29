"""Reproduce SFW derived data only. Reads original JAR/canonical inputs; no game writes."""
from collections import Counter, defaultdict
import json
from pathlib import Path
import sys

HERE = Path(__file__).resolve().parent
ROOT = HERE.parents[3]
sys.path.insert(0, str(ROOT / 'localization/tools'))
from sfw_localization import inventory_archive, make_record, parse_resource, validate_target, SfwValidationError, text_digest, digest


def readl(path):
    return [json.loads(line) for line in path.read_text(encoding='utf-8-sig').splitlines() if line.strip()]


def dump(path, data):
    assert path.resolve().is_relative_to(HERE)
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(data, ensure_ascii=False, indent=2) + '\n', encoding='utf-8')


def build():
    manifest, payloads = inventory_archive(ROOT / 'backup/cosmobreeder-multi.jar')
    units = {u['id']: u for u in readl(ROOT / 'localization/catalog/units.jsonl')}
    translations = {u['id']: u for u in readl(ROOT / 'localization/translations/zh-CN.jsonl')}
    occurrences = readl(ROOT / 'localization/catalog/occurrences.jsonl')
    inputs = ['localization/catalog/units.jsonl', 'localization/catalog/occurrences.jsonl', 'localization/translations/zh-CN.jsonl', 'localization/review/glossary.csv']
    manifest['reuse_inputs'] = {p: digest((ROOT / p).read_bytes()) for p in inputs}
    by_source = defaultdict(list)
    rooted = defaultdict(list)
    for occurrence in occurrences:
        unit = units[occurrence['unit_id']]
        translation = translations.get(unit['id'], {})
        target = translation.get('draft', '')
        if not target or translation.get('source_sha256') != unit['source_sha256']: continue
        category = {'dialogue': 'ds', 'vsn': 'vsn', 'ui': 'ui'}.get(unit['category'])
        if category is None: continue
        choice = (target, unit['id'], occurrence['occurrence_id'])
        by_source[(category, unit['source'])].append(choice)
        root = occurrence.get('entry') if category == 'ds' else occurrence.get('json_key', '') if category == 'ui' else Path(occurrence.get('logical_path', '')).parent.name
        rooted[(category, occurrence.get('logical_path'), root, occurrence.get('prefix', ''), unit['source'])].append(choice)
    reviewed = {}
    for batch in sorted((HERE / 'translations').glob('*.json')) if (HERE / 'translations').exists() else []:
        data = json.loads(batch.read_text(encoding='utf-8'))
        for key, value in data.items():
            if key in reviewed: raise ValueError('duplicate manual source key: ' + key)
            reviewed[key] = (value, batch.relative_to(HERE).as_posix())
    ledger = []
    for resource in manifest['resources']:
        for source in parse_resource(resource['logical_path'], payloads[resource['logical_path']]):
            row = make_record(manifest, resource, source)
            raw = source['raw_source']
            clean = raw.strip()
            short_key = source['kind'] + ':' + text_digest(clean)[:16]
            row['review_key'] = short_key
            if short_key in reviewed:
                entry, batch = reviewed[short_key]
                if entry['source'] != clean: raise ValueError('manual source hash collision/drift')
                row['translation'] = raw[:len(raw)-len(raw.lstrip())] + entry['translation'] + raw[len(raw.rstrip()):]
                row['status'] = entry.get('status', 'candidate')
                if 'cosmetic_padding' in entry:
                    expected_padding = {'source_left': 4, 'source_right': 4, 'target_left': 3, 'target_right': 3}
                    if row['id'] != 'SFW4ef0d94ee90867f2faa6b2ca' or entry['cosmetic_padding'] != expected_padding or entry['translation'] != 'FMOD STUDIO，由 FIRELIGHT 开发':
                        raise ValueError('unrecognized cosmetic credits padding adjustment')
                    row['translation'] = '   ' + entry['translation'] + '   '
                    row['cosmetic_padding'] = expected_padding
                if row['status'] == 'preserved':
                    if entry['translation'] != clean: raise ValueError('preserved candidate must equal original source')
                    row['translation'] = raw
                row['review_notes'] = entry.get('notes', [])
                row['provenance'] = {'method': 'source-specific-agent-review', 'batch': batch, 'model': 'openai/gpt-6.1-sol', 'human_approved': False}
            else:
                exact = rooted[(source['kind'], resource['logical_path'], source['root'], source['prefix'], clean)]
                choices = exact or by_source[(source['kind'], clean)]
                targets = {c[0] for c in choices}
                if len(targets) == 1:
                    target, uid, oid = choices[0]
                    row['translation'] = raw[:len(raw)-len(raw.lstrip())] + target + raw[len(raw.rstrip()):]
                    row['status'] = 'reused_candidate'
                    row['provenance'] = {'method': 'exact-root-prefix-source' if exact else 'exact-category-source-consensus', 'unit_id': uid, 'occurrence_id': oid, 'human_approved': False}
                elif len(targets) > 1:
                    row['review_notes'].append('exact English source has conflicting existing candidates; not guessed')
            if row['status'] in ('candidate', 'reused_candidate'):
                try: validate_target(raw, row['translation'])
                except SfwValidationError as exc:
                    row['status'] = 'needs_review'
                    row['review_notes'].append(str(exc))
            ledger.append(row)
    manifest['record_count'] = len(ledger)
    joins = []
    contexts_path = HERE / 'vsn-join-contexts.jsonl'
    decisions_path = HERE / 'vsn-join-decisions.json'
    if contexts_path.exists() and decisions_path.exists():
        contexts = readl(contexts_path)
        decisions = json.loads(decisions_path.read_text(encoding='utf-8'))
        by_id = {r['id']: r for r in ledger}
        if set(decisions) != {c['canonical_operation_id'] for c in contexts}: raise ValueError('VSN decisions/context set drift')
        for context in contexts:
            inputs = [by_id[s['ledger_id']] for s in context['inputs']]
            if any(r['logical_path'] != context['logical_path'] or r['prefix'] != 'text: ' or r['role'] for r in inputs): raise ValueError('VSN join context/role drift')
            for r, s in zip(inputs, context['inputs']):
                if r['raw_source'] != s['source'] or r['raw_source_sha256'] != s['raw_source_sha256']: raise ValueError('VSN join raw source drift')
            merged = decisions[context['canonical_operation_id']]
            validate_target(' '.join(r['raw_source'] for r in inputs), merged)
            key = [manifest['archive_sha256'], context['logical_path'], [r['id'] for r in inputs]]
            joins.append({'schema': 'sfw-vsn-joins/v1', 'join_id': 'SFWJ' + text_digest(json.dumps(key, separators=(',', ':')))[:24],
                'status': 'candidate', 'archive': manifest['archive'], 'archive_sha256': manifest['archive_sha256'], 'variant': 'sfw',
                'logical_path': context['logical_path'], 'archive_entry': context['archive_entry'], 'resource_sha256': context['resource_sha256'],
                'prefix': 'text: ', 'inputs': [{'ledger_id': r['id'], 'root': r['root'], 'raw_source': r['raw_source'],
                       'raw_source_sha256': r['raw_source_sha256'], 'source_ordinal': r['source_ordinal'],
                       'input_translation_sha256': text_digest(r['translation'])} for r in inputs],
                'merged_translation': merged, 'merged_translation_sha256': text_digest(merged),
                'context_before': context['context_before'], 'context_after': context['context_after'],
                'review': {'source_suggestion': context['canonical_operation_id'], 'method': 'whole-source-and-SFW-stage-context-reviewed',
                           'agent': 'openai/gpt-6.1-sol', 'human_approved': False,
                           'reason': '同一原JAR演出块内连续两条普通text，单一说话者/叙述者的完整句或紧密承接；无插入控制/auto/lang；显式接受减少一次点按。'},
                'click_reduction': len(inputs)-1})
    (HERE / 'vsn-joins.jsonl').write_text(''.join(json.dumps(r, ensure_ascii=False, separators=(',', ':'))+'\n' for r in joins), encoding='utf-8')
    pending = {}
    for row in ledger:
        if row['status'] in ('needs_translation', 'needs_review'):
            key = row['review_key']
            p = pending.setdefault(key, {'key': key, 'kind': row['kind'], 'source': row['raw_source'].strip(), 'existing_candidate': row['translation'], 'status': row['status'], 'notes': row['review_notes'], 'occurrences': []})
            p['occurrences'].append({'logical_path': row['logical_path'], 'root': row['root'], 'prefix': row['prefix'], 'line': row['source_line_evidence']})
    for kind in ('ds', 'vsn', 'ui'):
        path = HERE / ('ledger-' + kind + '.jsonl')
        path.write_text(''.join(json.dumps(r, ensure_ascii=False, separators=(',', ':'))+'\n' for r in ledger if r['kind'] == kind), encoding='utf-8')
        dump(HERE / ('pending-' + kind + '.json'), [r for r in pending.values() if r['kind'] == kind])
        compact = [{'key': r['key'], 'source': r['source'], 'existing_candidate': r['existing_candidate'], 'roots': sorted({o['root'] for o in r['occurrences']})} for r in pending.values() if r['kind'] == kind]
        (HERE / ('review-' + kind + '.jsonl')).write_text(''.join(json.dumps(r, ensure_ascii=False) + '\n' for r in compact), encoding='utf-8')
    manifest['ledger_sha256'] = {'ledger-' + kind + '.jsonl': digest((HERE / ('ledger-' + kind + '.jsonl')).read_bytes()) for kind in ('ds', 'vsn', 'ui')}
    manifest['ledger_sha256']['vsn-joins.jsonl'] = digest((HERE / 'vsn-joins.jsonl').read_bytes())
    polish_path = HERE / 'ds-polish.jsonl'
    polish = readl(polish_path) if polish_path.exists() else []
    if polish_path.exists(): manifest['ledger_sha256']['ds-polish.jsonl'] = digest(polish_path.read_bytes())
    dump(HERE / 'source-manifest.json', manifest)
    counts = {kind: dict(Counter(r['status'] for r in ledger if r['kind'] == kind)) for kind in ('ds', 'vsn', 'ui')}
    chars = sorted({c for r in ledger if r['status'] in ('candidate', 'reused_candidate') for c in r['translation'] if not c.isspace()} | {c for j in joins for c in j['merged_translation'] if not c.isspace()} | {c for p in polish for c in p['replacement'] if not c.isspace()})
    dump(HERE / 'required_chars.json', {'schema': 'sfw-required-chars/v1', 'characters': ''.join(chars), 'codepoints': [ord(c) for c in chars], 'note': 'Complete target strings, including Fox/HardFox Chinese alternatives; dynamic replacements are separate.'})
    coverage = {'schema': 'sfw-candidate-coverage/v1', 'archive_sha256': manifest['archive_sha256'], 'records': len(ledger), 'per_kind': counts, 'pending_unique': dict(Counter(p['kind'] for p in pending.values())), 'special_roles': dict(Counter(r['role'] for r in ledger if r['role'])), 'candidate_is_not_runtime_acceptance': True}
    audit = json.loads((ROOT / 'docs/font-layout-audit-20261025/text-review/results/sfw-variant-coverage.json').read_text(encoding='utf-8'))
    audit_keys = {(path, r['entry'], r['prefix'], r['source_en']) for path, value in audit['unmatched_dialogue_lines'].items() for r in value['unmatched']}
    gap_rows = [r for r in ledger if (r['logical_path'], r['root'], r['prefix'], r['raw_source']) in audit_keys]
    coverage['audit_460_ds_gap'] = {'located_records': len(gap_rows), 'status': dict(Counter(r['status'] for r in gap_rows)), 'remaining_ids': [r['id'] for r in gap_rows if r['status'] in ('needs_review', 'needs_translation')]}
    coverage['sfw_vsn_joins'] = {'applied_candidate_groups': len(joins), 'retained_review_groups': 0, 'click_reduction': sum(j['click_reduction'] for j in joins), 'unmatched_canonical_suggestions_not_applied': 281}
    coverage['sfw_ds_polish'] = {'candidate_operations': len(polish), 'source': 'own JAR raw source IDs plus applied canonical joins plus exact old Chinese'}
    coverage['intentional_corruption_not_full_Chinese'] = [{'ledger_id': r['id'], 'logical_path': r['logical_path'], 'root': r['root'], 'raw_source': r['raw_source']} for r in ledger if any('intentional-corruption/source-preserved' in note for note in r['review_notes'])]
    coverage['candidate_containing_Han'] = dict(Counter(r['kind'] for r in ledger if r['status'] in ('candidate', 'reused_candidate') and any('\u3400' <= c <= '\u9fff' for c in r['translation'])))
    unchanged = [{'review_key': r['review_key'], 'source': r['raw_source'], 'translation': r['translation'], 'kind': r['kind'], 'root': r['root']} for r in ledger if r['status'] in ('candidate', 'reused_candidate') and not any('\u3400' <= c <= '\u9fff' for c in r['translation'])]
    (HERE / 'non-Han-candidates.jsonl').write_text(''.join(json.dumps(r, ensure_ascii=False) + '\n' for r in unchanged), encoding='utf-8')
    dump(HERE / 'coverage.json', coverage)
    print(json.dumps(coverage, ensure_ascii=False, indent=2))

if __name__ == '__main__': build()
