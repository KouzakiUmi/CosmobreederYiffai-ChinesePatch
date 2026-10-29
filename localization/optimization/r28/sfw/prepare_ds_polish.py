"""Independently relocate DS polish by JAR source IDs, never PAK line positions."""
from collections import Counter
import json
from pathlib import Path
import sys

HERE = Path(__file__).resolve().parent
ROOT = HERE.parents[3]
sys.path.insert(0, str(ROOT / 'localization/tools'))
import sfw_localization as sfw
import dialogue_joins


def main():
    manifest, ledger = sfw.load_ledger(HERE)
    actual, payloads = sfw.inventory_archive(ROOT / 'backup/cosmobreeder-multi.jar')
    kwargs = {'canonical_join_records': dialogue_joins.load_records(), 'allow_pattern_candidates': True}
    # On subsequent rebuilds inspect the unpolished pipeline, not its own output.
    if hasattr(sfw, 'apply_ds_polish'): kwargs['enable_ds_polish'] = False
    entries, report = sfw.rebuild_candidate_entries(ROOT / 'backup/cosmobreeder-multi.jar', HERE, **kwargs)
    suggestions_path = ROOT / 'localization/optimization/r28/vsn/ds-polish/source-polish-suggestions.json'
    metadata_path = suggestions_path.with_name('operations.jsonl')
    suggestions = json.loads(suggestions_path.read_text(encoding='utf-8'))
    # Only logical resource and canonical join identifier are consumed from the
    # other component; its line/header_line fields are deliberately not copied.
    metadata = {r['operation_id']: r for r in [json.loads(x) for x in metadata_path.read_text(encoding='utf-8').splitlines()]}
    resources = {r['logical_path']: r for r in actual['resources']}
    report_by_path = {r['logical_path']: r for r in report['resources']}
    by_identity = {(r['logical_path'], r['root'], r['prefix'], r['raw_source_sha256'], r['source_ordinal']): r for r in ledger}
    review = []; operations = []
    for suggestion in suggestions:
        meta = metadata[suggestion['canonical_operation_id']]
        path = meta['logical_path']; root = suggestion['canonical_header'][1:-1]
        parsed = sfw.parse_resource(path, payloads[path]); expected = suggestion['source_en']
        result = {'suggestion_id': suggestion['canonical_operation_id'], 'logical_path': path,
                  'root': root, 'status': 'source_absent_or_changed'}
        matches = []
        if len(expected) != len(suggestion['source_sha256']) or any(sfw.text_digest(s) != h for s, h in zip(expected, suggestion['source_sha256'])):
            raise ValueError('suggested source SHA drift')
        for i in range(len(parsed)-len(expected)+1):
            group = parsed[i:i+len(expected)]
            if (all(p['root'] == root and p['prefix'] == suggestion['prefix'] for p in group)
                and [p['raw_source'].strip() for p in group] == expected
                and [p['line'] for p in group] == list(range(group[0]['line'], group[0]['line']+len(group)))):
                matches.append(group)
        if len(matches) != 1:
            if matches: result['status'] = 'nonunique_source'
            review.append(result); continue
        group = matches[0]; numbers = [p['line'] for p in group]
        applied_groups = report_by_path[path].get('canonical_join_report', {}).get('groups', [])
        join_id = meta['canonical_join_id']
        if join_id is not None:
            joined = [g for g in applied_groups if g['join_id'] == join_id and g['actual_sfw_lines'] == numbers]
            if len(joined) != 1:
                result['status'] = 'canonical_join_not_applied_to_this_source'; review.append(result); continue
        elif any(n in g['actual_sfw_lines'] for g in applied_groups for n in numbers):
            result['status'] = 'single_source_consumed_elsewhere'; review.append(result); continue
        output_lines = entries[resources[path]['archive_entry']].decode('utf-8').splitlines(keepends=True)
        body, _ = sfw._line_parts(output_lines[numbers[0]-1]); prefix = group[0]['prefix']
        if not body.startswith(prefix): raise ValueError('SFW prefix drift during polish review')
        old_payload = body[len(prefix):]
        if old_payload.strip() != suggestion['old_zh_CN']:
            result['status'] = 'already_fixed_or_different_candidate'
            result['actual_candidate'] = old_payload; review.append(result); continue
        left = old_payload[:len(old_payload)-len(old_payload.lstrip())]
        right = old_payload[len(old_payload.rstrip()):]
        new_payload = left + suggestion['candidate_zh_CN'] + right
        sfw.validate_target(old_payload, new_payload)
        own = [by_identity[(path, p['root'], p['prefix'], p['raw_source_sha256'], p['source_ordinal'])] for p in group]
        key = [actual['archive_sha256'], path, [r['id'] for r in own], join_id, sfw.text_digest(old_payload)]
        operation = {'schema': 'sfw-ds-polish/v1', 'operation_id': 'SFWDSP' + sfw.text_digest(json.dumps(key, separators=(',', ':')))[:24],
            'archive': sfw.ARCHIVE, 'archive_sha256': actual['archive_sha256'], 'variant': 'sfw',
            'logical_path': path, 'archive_entry': resources[path]['archive_entry'], 'resource_sha256': resources[path]['resource_sha256'],
            'root': root, 'prefix': prefix, 'canonical_join_id': join_id,
            'source_inputs': [{'ledger_id': r['id'], 'raw_source': r['raw_source'], 'raw_source_sha256': r['raw_source_sha256'], 'source_ordinal': r['source_ordinal']} for r in own],
            'old_payload': old_payload, 'old_payload_sha256': sfw.text_digest(old_payload),
            'replacement': new_payload, 'replacement_sha256': sfw.text_digest(new_payload),
            'reason': meta['reason'], 'provenance': {'suggestion_id': suggestion['canonical_operation_id'],
                'method': 'unique-SFW-root-prefix-ordered-source-plus-applied-join-and-exact-old-Chinese', 'human_approved': False}}
        operations.append(operation)
        result.update(status='applicable_exact_source_and_old_candidate', operation_id=operation['operation_id'],
                      actual_sfw_source_lines=numbers, source_ledger_ids=[r['id'] for r in own])
        review.append(result)
    (HERE / 'ds-polish.jsonl').write_text(''.join(json.dumps(r, ensure_ascii=False, separators=(',', ':'))+'\n' for r in operations), encoding='utf-8')
    output = {'schema': 'sfw-ds-polish-review/v1', 'suggestions_sha256': sfw.digest(suggestions_path.read_bytes()),
        'counts': dict(Counter(r['status'] for r in review)), 'operations': review,
        'source_identity': 'original JAR own raw source IDs and actual applied join mapping; PAK line values ignored'}
    (HERE / 'ds-polish-review.json').write_text(json.dumps(output, ensure_ascii=False, indent=2)+'\n', encoding='utf-8')
    print(json.dumps(output, ensure_ascii=False, indent=2))

if __name__ == '__main__': main()
