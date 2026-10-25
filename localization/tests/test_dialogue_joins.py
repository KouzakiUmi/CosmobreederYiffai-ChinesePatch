"""Isolated DS join regressions: no JVM/game, canonical or install writes.

Run: PYTHONDONTWRITEBYTECODE=1 python -m unittest discover -s localization/tests
     -p test_dialogue_joins.py -v
"""
import copy
import json
from pathlib import Path
import sys
import unittest
from unittest.mock import patch
import zipfile

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / 'tools'))
import dialogue_joins as joins
from codec import decrypt_file
from projectlib import PROJECT, current_translations, digest, load_occurrences, load_units, source_hash


class DialogueJoinTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.active_records = joins.load_records()
        cls.records = [json.loads(line) for line in (PROJECT / 'tests/fixtures/dialogue-joins-initial.jsonl').read_text('utf8').splitlines()]
        cls.occurrences = load_occurrences()
        cls.units = {u['id']: u for u in load_units()}
        cls.translations = current_translations()
        cls.originals = {}
        cls.localized = {}
        with zipfile.ZipFile(PROJECT / 'builds/final-8146-r21/patch.pak') as archive:
            for path, entry in [('datadf/all.ds', 'datadf/1'), ('datadm/all.ds', 'datadm/1')]:
                cls.originals[path] = (PROJECT.parent / 'extract/patch' / path).read_bytes()
                cls.localized[path] = decrypt_file(archive.read(entry))

    def apply(self, records=None, localized=None, original=None, path='datadf/all.ds'):
        return joins.apply_joins(path, self.originals[path] if original is None else original,
                                 self.localized[path] if localized is None else localized,
                                 records=self.records if records is None else records)

    def rejects(self, records=None, localized=None, original=None, message=None):
        saved = self.localized['datadf/all.ds']
        with self.assertRaisesRegex(joins.JoinValidationError, message or '.'):
            self.apply(records, localized, original)
        self.assertEqual(saved, self.localized['datadf/all.ds'])

    def test_11_real_groups_apply_individually(self):
        self.assertEqual(len(self.records), 11)
        for record in self.records:
            with self.subTest(join=record['join_id']):
                path = record['logical_path']
                result, report = self.apply([record], path=path)
                before, after = joins._split(self.localized[path]), joins._split(result)
                self.assertEqual(len(before), len(after))
                first = record['inputs'][0]
                occurrence = next(o for o in self.occurrences if o['occurrence_id'] == first['occurrence_id'])
                expected = record['prefix'] + occurrence['leading_ws'] + record['merged_translation'] + occurrence['trailing_ws']
                self.assertEqual(joins._body_eol(after[first['line'] - 1])[0].decode('utf8'), expected)
                for number in record['physical_lines'][1:]:
                    self.assertEqual(after[number - 1], joins._body_eol(before[number - 1])[1])
                for number, (a, b) in enumerate(zip(before, after), 1):
                    self.assertEqual(joins._body_eol(a)[1], joins._body_eol(b)[1])
                    if number not in record['physical_lines']:
                        self.assertEqual(a, b)
                self.assertEqual(report['applied_groups'], 1)
                self.assertEqual(len(report['occurrence_mapping']), len(record['inputs']))

    def test_initial_golden_groups_and_byte_preservation(self):
        total_groups = total_removed = 0
        for path in self.originals:
            result, report = self.apply(path=path)
            selected = [r for r in self.records if r['logical_path'] == path]
            changed_lines = {n for r in selected for n in r['physical_lines']}
            old, new = joins._split(self.localized[path]), joins._split(result)
            self.assertEqual([joins._body_eol(x)[1] for x in old], [joins._body_eol(x)[1] for x in new])
            self.assertEqual([x for i, x in enumerate(old, 1) if i not in changed_lines],
                             [x for i, x in enumerate(new, 1) if i not in changed_lines])
            self.assertEqual(report['input_sha256'], digest(self.localized[path]))
            self.assertEqual(report['output_sha256'], digest(result))
            total_groups += report['applied_groups']
            total_removed += report['removed_text_nodes']
        self.assertEqual((total_groups, total_removed), (11, 13))

    def test_active_956_full_source_groups_apply_without_unrelated_changes(self):
        self.assertEqual(len(self.active_records), 956)
        self.assertEqual(len({r['join_id'] for r in self.active_records}), 956)
        active_members={i['occurrence_id'] for r in self.active_records for i in r['inputs']}
        self.assertTrue({i['occurrence_id'] for r in self.records for i in r['inputs']}.issubset(active_members))
        groups = removed = 0
        for path in self.originals:
            result,report=joins.apply_joins(path,self.originals[path],self.localized[path])
            selected=[r for r in self.active_records if r['logical_path']==path]
            changed={n for r in selected for n in r['physical_lines']}
            before,after=joins._split(self.localized[path]),joins._split(result)
            self.assertEqual(len(before),len(after))
            for number,(old,new) in enumerate(zip(before,after),1):
                self.assertEqual(joins._body_eol(old)[1],joins._body_eol(new)[1])
                if number not in changed:self.assertEqual(old,new)
            for r in selected:
                occurrence=next(o for o in self.occurrences if o['occurrence_id']==r['inputs'][0]['occurrence_id'])
                expected=r['prefix']+occurrence['leading_ws']+r['merged_translation']+occurrence['trailing_ws']
                self.assertEqual(joins._body_eol(after[r['physical_lines'][0]-1])[0].decode('utf8'),expected)
                for n in r['physical_lines'][1:]:self.assertEqual(after[n-1],joins._body_eol(before[n-1])[1])
            groups+=report['applied_groups'];removed+=report['removed_text_nodes']
        self.assertEqual((groups,removed),(956,1098))
        initial_dm=next(r for r in self.records if r['join_id']=='DJ002')['inputs'][0]['occurrence_id']
        dm=next(r for r in self.active_records if any(i['occurrence_id']==initial_dm for i in r['inputs']))
        self.assertNotIn('不太再穿',dm['merged_translation'])
        self.assertEqual(dm['merged_translation'].count('大概'),1)

    def test_actual_mauser_transmission_station_both_resource_variants(self):
        for path in self.originals:
            record=next(r for r in self.active_records if r['logical_path']==path and r['root']=='Mauser.Area0_map13_b' and '传输站' in r['merged_translation'])
            self.assertEqual(len(record['inputs']),3)
            self.assertEqual(record['actor'],'Mauser')
            result,report=joins.apply_joins(path,self.originals[path],self.localized[path],records=[record])
            lines=result.decode('utf8').splitlines()
            self.assertIn('传输站',lines[record['physical_lines'][0]-1])
            self.assertNotIn('传输]',lines[record['physical_lines'][0]-1])
            self.assertTrue(all(lines[n-1]=='' for n in record['physical_lines'][1:]))
            self.assertEqual(report['removed_text_nodes'],2)

    def test_bracket_delta_is_group_scoped(self):
        result, report = self.apply()
        old, new = self.localized['datadf/all.ds'].decode('utf8'), result.decode('utf8')
        delta = sum(r['expected_marker_delta']['open_square'] for r in self.records if r['logical_path'] == 'datadf/all.ds')
        self.assertEqual(new.count('[') - old.count('['), delta)
        self.assertEqual(new.count(']') - old.count(']'), delta)
        self.assertEqual(delta, -5)
        for record in self.records:
            if not record['coalesce_outer_brackets']:
                self.assertEqual(record['expected_marker_delta'], {'open_square': 0, 'close_square': 0})

    def test_shared_unit_test_hacker_fixture_never_joins(self):
        target = next(r for r in self.records if r['join_id'] == 'DJ010')
        reuse = next(o for o in self.occurrences if o.get('logical_path') == 'datadf/all.ds' and o.get('line') == 5178)
        self.assertEqual(reuse['unit_id'], target['inputs'][0]['unit_id'])
        self.assertNotIn(reuse['occurrence_id'], {i['occurrence_id'] for r in self.records for i in r['inputs']})
        result, report = self.apply()
        old, new = joins._split(self.localized['datadf/all.ds']), joins._split(result)
        self.assertEqual(old[5174:5179], new[5174:5179])
        self.assertEqual(next(o for o in self.occurrences if o.get('logical_path') == 'datadf/all.ds' and o.get('line') == 5179)['unit_id'], 'De00a2698259bf50d9d66')
        self.assertNotIn(reuse['occurrence_id'], {m['occurrence_id'] for m in report['occurrence_mapping']})

    def test_actual_yiffany_actor_and_next_tomcat_unchanged(self):
        record = next(r for r in self.records if r['join_id'] == 'DJ011')
        self.assertEqual((record['root'], record['actor']), ('Mauser.AreaE_map23', 'Yiffany'))
        new, _ = self.apply([record])
        self.assertEqual(joins._split(new)[2558], joins._split(self.localized['datadf/all.ds'])[2558])
        self.assertIn(b'Tomcat:', joins._split(new)[2558])

    def test_merged_semantics_reordered_not_mechanical(self):
        records = {r['join_id']: r for r in self.records}
        self.assertEqual(records['DJ002']['merged_translation'].count('大概'), 1)
        self.assertTrue(records['DJ003']['merged_translation'].endswith('吗？'))
        self.assertIn('一直在把你的近场数据传回总部', records['DJ006']['merged_translation'])
        self.assertEqual(records['DJ008']['merged_translation'], '[震源在你的东边，但看起来你的西边有一座旧传输站！]')
        self.assertIn('27.850', records['DJ007']['merged_translation'])

    def test_truthful_origin_no_approval_or_old_generation_claim(self):
        for r in self.records:
            self.assertEqual(r['status'], 'candidate_user_requested')
            self.assertFalse(r['origin']['independent_qa_approval'])
            self.assertEqual(r['origin']['authorization'], 'user_requested_sentence_join')
            self.assertNotIn('usage_approved', r)
            self.assertNotIn('reviewer', r)
            self.assertNotIn('model', r)
            self.assertNotIn('runtime_key', r)

    def test_no_records_and_unrelated_resource_noop(self):
        result, report = self.apply([])
        self.assertEqual(result, self.localized['datadf/all.ds'])
        self.assertEqual(report['applied_groups'], 0)
        result, report = joins.apply_joins('unrelated.ds', b'original', b'localized')
        self.assertEqual(result, b'localized')
        self.assertEqual(report['applied_groups'], 0)

    def test_source_resource_and_ledger_sha_drift_rejected(self):
        self.rejects(original=self.originals['datadf/all.ds'] + b' ', message='SourceSHA')
        records = copy.deepcopy(self.records)
        records[0]['source_resource_sha256'] = '0' * 64
        self.rejects(records, message='SourceSHA')

    def test_input_translation_and_hash_drift_rejected(self):
        for key, value in [('input_translation', '变动中文'), ('input_translation_sha256', '0' * 64),
                           ('source_sha256', '0' * 64), ('unit_id', 'Dmissing'), ('occurrence_id', 'Omissing')]:
            with self.subTest(key=key):
                records = copy.deepcopy(self.records)
                records[0]['inputs'][0][key] = value
                self.rejects(records)
        records = copy.deepcopy(self.records)
        records[0]['merged_translation_sha256'] = '0' * 64
        self.rejects(records, message='Merged translation SHA')

    def test_current_draft_table_drift_rejected_without_writes(self):
        changed = copy.deepcopy(self.translations)
        changed[self.records[0]['inputs'][0]['unit_id']]['draft'] += '改变'
        with patch.object(joins, 'current_translations', return_value=changed):
            self.rejects(message='Draft/input SHA')

    def test_occurrence_table_drift_rejected(self):
        changed = copy.deepcopy(self.occurrences)
        next(o for o in changed if o['occurrence_id'] == self.records[0]['inputs'][0]['occurrence_id'])['prefix'] = '  Other/Smile: '
        with patch.object(joins, 'load_occurrences', return_value=changed):
            self.rejects(message='Occurrence location/unit/prefix')

    def test_ledger_order_overlap_and_gaps_rejected(self):
        for mutate in [lambda r: r['inputs'].reverse(),
                       lambda r: r['physical_lines'].reverse(),
                       lambda r: r['inputs'][1].update(line=129)]:
            records = copy.deepcopy(self.records)
            mutate(records[0])
            self.rejects(records, message='Nonconsecutive/reordered')
        records = copy.deepcopy(self.records)
        duplicate = copy.deepcopy(records[0])
        duplicate['join_id'] = 'different-id'
        records.append(duplicate)
        self.rejects(records, message='Overlapping')

    def test_ledger_actor_expression_root_flags_branch_rejected(self):
        for key, value in [('prefix', '  Other/Smile: '), ('actor', 'Other'), ('root', 'Other.Root'),
                           ('full_header', '<Area0_Macsen2.DoggyHead noselect>'), ('header_line', 123),
                           ('branch_evidence', {})]:
            with self.subTest(key=key):
                records = copy.deepcopy(self.records)
                records[0][key] = value
                self.rejects(records)

    def test_localized_actor_expression_event_text_drift_rejected(self):
        old = self.localized['datadf/all.ds']
        lines = joins._split(old)
        for line, body in [(126, '  Other: 不同角色'), (126, '  */Smile: 表情改变'),
                           (127, '  event { changed }'), (126, '  * 英文输入改变'),
                           (864, '  } else { changed'), (1935, '  if { changed } {'),
                           (1967, '<Tomcat.Area0_map16_a noselect>')]:
            with self.subTest(line=line):
                changed = lines[:]
                changed[line - 1] = body.encode('utf8') + joins._body_eol(lines[line - 1])[1]
                self.rejects(localized=b''.join(changed))
        self.assertEqual(old, self.localized['datadf/all.ds'])

    def test_localized_line_count_and_eol_drift_rejected(self):
        self.rejects(localized=self.localized['datadf/all.ds'] + b'\n\n', message='line count')
        self.rejects(localized=self.localized['datadf/all.ds'] + b'\n', message='EOL drift')
        lines = joins._split(self.localized['datadf/all.ds'])
        body, eol = joins._body_eol(lines[125])
        lines[125] = body + (b'\n' if eol == b'\r\n' else b'\r\n')
        self.rejects(localized=b''.join(lines), message='EOL drift')

    def test_all_preflight_atomic_last_record_failure(self):
        records = copy.deepcopy(self.records)
        records[-1]['inputs'][-1]['input_translation_sha256'] = '0' * 64
        self.rejects(records, message='Draft/input SHA')
        result, _ = self.apply()
        self.assertNotEqual(result, self.localized['datadf/all.ds'])
        self.rejects(localized=result, message='Localized CJK input/prefix')

    def test_bracket_tampering_and_delimiter_injection_rejected(self):
        for key, value in [('coalesce_outer_brackets', False),
                           ('expected_marker_delta', {'open_square': 0, 'close_square': 0})]:
            record = copy.deepcopy(next(r for r in self.records if r['join_id'] == 'DJ006'))
            record[key] = value
            self.rejects([record])
        for text in ['[错误[嵌套]正文]', '[缺右括号', '[加入@ZoneName变量]', '中文|分段', '中文<p>分段', '中文\n换行']:
            record = copy.deepcopy(next(r for r in self.records if r['join_id'] == 'DJ006'))
            record['merged_translation'] = text
            record['merged_translation_sha256'] = source_hash(text)
            self.rejects([record])

    def test_all_other_markers_and_placeholder_multisets_conserved(self):
        normal = {'coalesce_outer_brackets': False, 'expected_marker_delta': {'open_square': 0, 'close_square': 0}}
        joins._validate_markers(normal, ['@ZoneName__<b>', '@ZoneName'],
                                ['@ZoneName__<b>中文', '@ZoneName中文'], '@ZoneName__<b>中文@ZoneName中文')
        for merged in ['@ZoneName__<i>中文@ZoneName中文', '@ZoneName_<b>中文@ZoneName中文', '@ZoneName__<b>中文',
                       '@ZoneName__<b>中文@BOYPC中文']:
            with self.subTest(merged=merged), self.assertRaises(joins.JoinValidationError):
                joins._validate_markers(normal, ['@ZoneName__<b>', '@ZoneName'],
                                        ['@ZoneName__<b>中文', '@ZoneName中文'], merged)
        bracket = {'coalesce_outer_brackets': True, 'expected_marker_delta': {'open_square': -1, 'close_square': -1}}
        with self.assertRaises(joins.JoinValidationError):
            joins._validate_markers(bracket, ['[@ZoneName]', '[x]'], ['[@ZoneName中文]', '[中文]'], '[@ZoneName中文中文]')

    def test_synthetic_mixed_eols_and_no_final_eol_preserved(self):
        # Explicit synthetic source fixture: hash substitution is confined to mocks,
        # never used for the production ledger/canonical bytes.
        path = 'datadf/all.ds'
        old, localized = [], []
        a, b = joins._split(self.originals[path]), joins._split(self.localized[path])
        for index, (x, y) in enumerate(zip(a, b)):
            eol = b'' if index == len(a) - 1 else (b'\r\n' if index % 2 else b'\n')
            old.append(joins._body_eol(x)[0] + eol)
            localized.append(joins._body_eol(y)[0] + eol)
        original, localized = b''.join(old), b''.join(localized)
        records = copy.deepcopy([r for r in self.records if r['logical_path'] == path])
        for r in records:
            r['source_resource_sha256'] = digest(original)
        real_read = joins.read_jsonl
        def fixture_resources(p):
            rows = copy.deepcopy(real_read(p))
            if Path(p).name == 'resources.jsonl':
                next(r for r in rows if r['logical_path'] == path)['sha256'] = digest(original)
            return rows
        with patch.object(joins, 'read_jsonl', side_effect=fixture_resources):
            result, _ = self.apply(records, localized=localized, original=original)
        self.assertEqual([joins._body_eol(x)[1] for x in joins._split(result)],
                         [joins._body_eol(x)[1] for x in joins._split(localized)])
        self.assertFalse(result.endswith((b'\n', b'\r')))

    def test_build_record_reuses_all_11_preflight_policies_without_persistence(self):
        ledger = joins.LEDGER.read_bytes()
        for expected in self.records:
            with self.subTest(join=expected['join_id']):
                candidate = joins.build_record([i['occurrence_id'] for i in expected['inputs']],
                                                expected['merged_translation'], 'Explicit fixture review',
                                                agent='unit-test-caller')
                for key in expected:
                    if key not in ('join_id', 'origin'):
                        self.assertEqual(candidate[key], expected[key], key)
                self.assertEqual(candidate['origin']['agent'], 'unit-test-caller')
                self.assertEqual(candidate['status'], 'candidate_user_requested')
        self.assertEqual(ledger, joins.LEDGER.read_bytes())
        self.assertEqual(self.translations, current_translations())

    def test_build_record_rejects_order_actor_branch_marker_and_unknown_ids(self):
        by_line = {o['line']: o['occurrence_id'] for o in self.occurrences
                   if o.get('logical_path') == 'datadf/all.ds' and o['category'] == 'dialogue'}
        for ids, merged in [([by_line[127], by_line[126]], '反序中文'),
                            ([by_line[2558], by_line[2559]], '[跨角色中文]'),
                            ([by_line[863], by_line[865]], '跨else中文'),
                            ([by_line[1972], by_line[1973]], '丢方括号中文'),
                            ([by_line[126], by_line[126]], '重复中文'),
                            (['Omissing', by_line[126]], '未知中文')]:
            with self.subTest(ids=ids), self.assertRaises(joins.JoinValidationError):
                joins.build_record(ids, merged, 'Negative fixture')

    def test_candidate_audit_is_not_approval(self):
        ledger_before = joins.LEDGER.read_bytes()
        result = joins.scan_candidates()
        self.assertGreater(result['pair_count'], 11)
        for group in result['groups']:
            numbers = group['physical_lines']
            self.assertEqual(numbers, list(range(numbers[0], numbers[-1] + 1)))
            self.assertEqual(group['status'], 'unreviewed_audit_only')
            rows = [o for o in self.occurrences if o.get('logical_path') == group['logical_path'] and o.get('line') in numbers]
            self.assertEqual(len({o['prefix'] for o in rows}), 1)
            self.assertEqual(len({o['entry'] for o in rows}), 1)
        self.assertEqual(ledger_before, joins.LEDGER.read_bytes())


if __name__ == '__main__':
    unittest.main()
