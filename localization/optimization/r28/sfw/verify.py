"""Reproduce in-memory candidate/834-join evidence; writes only this SFW directory."""
from collections import Counter
import io
import json
import re
from pathlib import Path
import sys
import unittest

HERE = Path(__file__).resolve().parent
ROOT = HERE.parents[3]
sys.path.insert(0, str(ROOT / 'localization/tools'))
import sfw_localization as sfw
import dialogue_joins


def save(name, obj):
    path = HERE / name
    assert path.resolve().is_relative_to(HERE)
    path.write_text(json.dumps(obj, ensure_ascii=False, indent=2) + '\n', encoding='utf-8')


def join_source_review(manifest, payloads, ledger):
    suggestions_path = ROOT / 'localization/optimization/r28/vsn/source-join-suggestions.json'
    suggestions = json.loads(suggestions_path.read_text(encoding='utf-8'))
    resources = {r['logical_path']: r for r in manifest['resources']}
    review = []
    by_id = {(r['logical_path'], r['root'], r['prefix'], r['raw_source_sha256'], r['source_ordinal']): r['id'] for r in ledger}
    for suggestion in suggestions:
        logical = 'vsn/' + suggestion['scene'] + '/script.vsn'
        expected = suggestion['ordered_source_en']
        result = {'canonical_operation_id': suggestion['canonical_operation_id'], 'logical_path': logical,
                  'status': 'source_absent_or_changed', 'applied': False}
        if logical in payloads and all(sfw.text_digest(s) == h for s, h in zip(expected, suggestion['ordered_source_sha256'])):
            parsed = sfw.parse_resource(logical, payloads[logical])
            candidates = []
            for i in range(len(parsed) - len(expected) + 1):
                group = parsed[i:i+len(expected)]
                if (all(r['prefix'] == suggestion['prefix'] == 'text: ' for r in group)
                    and [r['raw_source'] for r in group] == expected
                    and [r['line'] for r in group] == list(range(group[0]['line'], group[0]['line']+len(group)))):
                    candidates.append(group)
            if len(candidates) == 1:
                group = candidates[0]
                result.update({'status': 'unique_whole_source_match_review_only',
                    'archive': sfw.ARCHIVE, 'archive_sha256': manifest['archive_sha256'],
                    'archive_entry': resources[logical]['archive_entry'],
                    'resource_sha256': resources[logical]['resource_sha256'],
                    'prefix': suggestion['prefix'],
                    'inputs': [{'source_line_evidence': r['line'], 'source': r['raw_source'],
                                'raw_source_sha256': r['raw_source_sha256'],
                                'ledger_id': by_id[(logical, r['root'], r['prefix'], r['raw_source_sha256'], r['source_ordinal'])]} for r in group],
                    'candidate_zh_CN': suggestion['candidate_zh_CN'],
                    'review_notes': ['No PAK line number used. Own JAR source and adjacent text-only physical commands matched exactly.',
                                     'Not applied: full stage/actor/timing and reduction of click count still require SFW-specific review.']})
            elif len(candidates) > 1:
                result['status'] = 'ambiguous_whole_source_match'
        review.append(result)
    return {'schema': 'sfw-vsn-join-source-review/v1', 'suggestions_sha256': sfw.digest(suggestions_path.read_bytes()),
            'counts': dict(Counter(r['status'] for r in review)), 'source_scan_applied_groups': 0,
            'final_application_ledger': 'vsn-joins.jsonl', 'operations': review}


def main():
    log = io.StringIO()
    suite = unittest.defaultTestLoader.discover(str(ROOT / 'localization/tests'), pattern='test_sfw_localization.py')
    result = unittest.TextTestRunner(stream=log, verbosity=2).run(suite)
    (HERE / 'tests.log').write_text(log.getvalue(), encoding='utf-8')
    if not result.wasSuccessful():
        print(log.getvalue()); return 1
    manifest, ledger = sfw.load_ledger(HERE)
    actual, payloads = sfw.inventory_archive(ROOT / 'backup/cosmobreeder-multi.jar')
    entries, rebuild = sfw.rebuild_candidate_entries(ROOT / 'backup/cosmobreeder-multi.jar', HERE,
                        canonical_join_records=dialogue_joins.load_records(), allow_pattern_candidates=True)
    save('rebuild-report.json', rebuild)
    font_path = ROOT / 'localization/optimization/r28/integration/tests/final-01/fonts/classic.fnt'
    font_raw = font_path.read_bytes()
    metrics = {int(k): int(v) for k, v in re.findall(r'^char id=(\d+)\s+.*?xadvance=(-?\d+)', font_raw.decode('utf-8'), re.M)}
    ending_report = sfw.validate_ending_fields(json.loads(entries['datav/1']), metrics)
    ending_report.update({'font_source': font_path.relative_to(ROOT).as_posix(), 'font_sha256': sfw.digest(font_raw),
                          'note': 'Actual final-01 classic8 advances, all 60 fields; no glyph/width/column-limit relaxation.'})
    save('ending-field-layout.json', ending_report)
    save('vsn-join-source-review.json', join_source_review(actual, payloads, ledger))
    unresolved = [r for r in ledger if r['status'] in ('needs_review', 'needs_translation')]
    intentional = [r for r in ledger if any('intentional-corruption/source-preserved' in note for note in r['review_notes'])]
    save('remaining-review.json', {'schema': 'sfw-remaining-review/v1', 'records': unresolved,
                                 'intentional_corruption_source_preserved': intentional,
                                 'note': 'No unresolved candidates. Four intentionally corrupted broadcasts remain original Latin fragments, not counted as complete Chinese. Proper names retain source spelling or existing project glossary evidence.'})
    canonical_prefixes = {r['prefix'] for r in [json.loads(x) for x in (ROOT / 'localization/catalog/occurrences.jsonl').read_text(encoding='utf-8').splitlines()] if r['category'] == 'dialogue'}
    foreign = sorted({r['prefix'] for r in ledger if r['kind'] == 'ds'} - canonical_prefixes)
    final_text = []
    for resource in actual['resources']:
        final_text.extend(sfw.parse_resource(resource['logical_path'], entries[resource['archive_entry']]))
    required = json.loads((HERE / 'required_chars.json').read_text(encoding='utf-8'))
    report = {'schema': 'sfw-verification/v1', 'tests_run': result.testsRun, 'tests_passed': result.wasSuccessful(),
              'required_characters': len(required['codepoints']),
              'ending_fields': ending_report['field_count'], 'ending_nonempty_fields': ending_report['nonempty_fields'],
              'ending_maximum_columns': ending_report['maximum_columns'], 'ending_maximum_width_px': ending_report['maximum_width_px'],
              'final_text_records': dict(Counter(r['kind'] for r in final_text)),
              'final_text_containing_Han': dict(Counter(r['kind'] for r in final_text if any('\u3400' <= c <= '\u9fff' for c in r['raw_source']))),
              'original_archive_sha256': manifest['archive_sha256'], 'in_memory_output_entries': len(entries),
              'applied_canonical_joins': sum(r.get('canonical_join_report', {}).get('applied_groups', 0) for r in rebuild['resources']),
              'skipped_canonical_joins': sum(len(r.get('canonical_join_report', {}).get('skipped', [])) for r in rebuild['resources']),
              'sfw_only_dialogue_prefixes_not_recognized_by_canonical_rewriter': foreign,
              'remaining_review_records': len(unresolved), 'remaining_unique_sources': len({r['review_key'] for r in unresolved}),
              'applied_sfw_vsn_joins': rebuild['sfw_vsn_applied_groups'],
              'sfw_vsn_click_reduction': rebuild['sfw_vsn_click_reduction'],
              'sfw_vsn_auto_or_lang_joins': 0,
              'applied_sfw_ds_polish_operations': rebuild['sfw_ds_polish_applied_operations'],
              'intentional_corruption_source_preserved_not_full_Chinese': len(intentional),
              'output_entry_plaintext_sha256': {name: sfw.digest(data) for name, data in entries.items()},
              'archive_writes': 0, 'game_execution': False, 'font_runtime_acceptance': 'not performed'}
    save('verification.json', report)
    print(json.dumps(report, ensure_ascii=False, indent=2))
    return 0

if __name__ == '__main__': raise SystemExit(main())
