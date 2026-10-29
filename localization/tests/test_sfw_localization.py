"""SFW candidates only: original archive reads and in-memory outputs, no installation."""
from collections import Counter
import copy
import json
import re
from pathlib import Path
import sys
import unittest

ROOT = Path(__file__).resolve().parents[2]
sys.path.insert(0, str(ROOT / 'localization/tools'))
import sfw_localization as sfw

DATA = ROOT / 'localization/optimization/r28/sfw'


def fixture(data=b'<A>\r\n  * Press SELECT 2 times: @Name @Name <p> [_]\r\ndo unchanged\r\n', logical='datadf/all.ds'):
    manifest = {'archive_sha256': 'a' * 64}
    resource = {'logical_path': logical, 'archive_entry': 'datadf/1' if logical.endswith('.ds') else 'vsn/123', 'resource_sha256': sfw.digest(data)}
    rows = [sfw.make_record(manifest, resource, parsed) for parsed in sfw.parse_resource(logical, data)]
    for row in rows:
        row.update(status='candidate', translation='按SELECT 2次：@Name @Name <p> [_]')
    return data, resource, rows


def plan(data, resource, rows, **kwargs):
    return sfw.candidate_replacements(archive=sfw.ARCHIVE, archive_sha256='a' * 64,
        logical_path=resource['logical_path'], archive_entry=resource['archive_entry'],
        original_bytes=data, records=rows, **kwargs)


class CandidateContractTests(unittest.TestCase):
    def test_preserve_control_prefix_eol_and_complete_target(self):
        data, resource, rows = fixture()
        result = sfw.render_candidate(data, plan(data, resource, rows))
        self.assertEqual(result.decode(), '<A>\r\n  * 按SELECT 2次：@Name @Name <p> [_]\r\ndo unchanged\r\n')
        self.assertTrue(result.endswith(b'do unchanged\r\n'))

    def test_duplicate_replacement_identity_fails(self):
        data, resource, rows = fixture()
        with self.assertRaisesRegex(ValueError, 'duplicate'):
            plan(data, resource, rows + rows)

    def test_incomplete_ledger_fails_closed(self):
        data, resource, rows = fixture()
        with self.assertRaisesRegex(ValueError, 'incomplete'):
            plan(data, resource, [])

    def test_source_drift_fails_closed_even_same_length(self):
        data, resource, rows = fixture()
        with self.assertRaisesRegex(ValueError, 'identity drift'):
            plan(data.replace(b'2 times', b'3 times'), resource, rows)

    def test_source_line_evidence_is_not_a_pak_locator(self):
        data, resource, rows = fixture()
        rows[0]['source_line_evidence'] = 999999
        self.assertTrue(plan(data, resource, rows))

    def test_raw_source_digest_tampering_fails(self):
        data, resource, rows = fixture()
        rows[0]['raw_source'] += 'x'
        with self.assertRaisesRegex(ValueError, 'raw source'):
            plan(data, resource, rows)

    def test_prefix_and_role_are_immutable(self):
        data, resource, rows = fixture()
        rows[0]['prefix'] = 'OTHER: '
        with self.assertRaises(ValueError): plan(data, resource, rows)

    def test_resource_gender_variant_isolation(self):
        data, resource, rows = fixture()
        resource['logical_path'] = 'datadm/all.ds'
        with self.assertRaisesRegex(ValueError, 'logical_path'):
            plan(data, resource, rows)

    def test_pak_cannot_be_accepted_as_jar(self):
        data, resource, rows = fixture()
        with self.assertRaisesRegex(ValueError, 'SFW JAR'):
            sfw.candidate_replacements(archive='patch.pak', archive_sha256='a'*64,
                logical_path=resource['logical_path'], archive_entry=resource['archive_entry'],
                original_bytes=data, records=rows)

    def test_repeated_placeholders_are_multisets(self):
        with self.assertRaisesRegex(ValueError, 'multiset'):
            sfw.validate_target('@Name @Name', '@Name @Other')
        with self.assertRaisesRegex(ValueError, 'multiset'):
            sfw.validate_target('@Name @Name', '@Name')

    def test_full_tags_not_just_tag_count(self):
        with self.assertRaisesRegex(ValueError, 'multiset'):
            sfw.validate_target('first<p>second', '前半<br>后半')
        sfw.validate_target('DWARF <FAUNA>', '矮人 <动物>')

    def test_preserve_numbers_key_combinations_and_literal_keys(self):
        for original, target in [('Press SELECT!', '按选择！'), ('UP+ATTACK', 'UP+攻击'), ('100% 2', '100% 两')]:
            with self.subTest(source=original), self.assertRaises(ValueError):
                sfw.validate_target(original, target)
        sfw.validate_target('SELECT A PROGRAM', '选择程序')
        sfw.validate_target('KEYCARD3', '门卡3')

    def test_identifier_codes_preserved(self):
        with self.assertRaises(ValueError): sfw.validate_target('R18 40N', '卫星18 北纬40')
        sfw.validate_target('R18 40N', 'R18卫星40N')

    def test_whole_sentence_glyph_coverage_includes_last_character(self):
        sfw.validate_target('Hello', '你好。', {ord(c) for c in '你好。'})
        with self.assertRaisesRegex(ValueError, 'glyph coverage'):
            sfw.validate_target('Hello', '你好。', {ord(c) for c in '你好'})

    def test_unicode_line_separator_injection_rejected(self):
        for sep in ('\x85', '\u2028', '\u2029'):
            with self.subTest(separator=repr(sep)), self.assertRaisesRegex(ValueError, 'line separator'):
                sfw.validate_target('Hello', '你' + sep + '好')

    def test_no_empty_translation_completion(self):
        data, resource, rows = fixture()
        rows[0]['translation'] = ''
        with self.assertRaisesRegex(ValueError, 'empty translation'):
            plan(data, resource, rows)

    def test_ambiguous_duplicates_need_explicit_multiplicity(self):
        data, resource, rows = fixture(b'<A>\n * Hello\n * Hello\n')
        for row in rows: row['translation'] = '你好'
        self.assertEqual(len(plan(data, resource, rows)), 2)
        rows[0]['source_multiplicity'] = 1
        with self.assertRaisesRegex(ValueError, 'multiplicity'):
            plan(data, resource, rows)

    def test_pattern_dual_representation_opt_in_and_identity(self):
        data, resource, rows = fixture(b'lang(Fox): Hello\n', 'vsn/m_scene/script.vsn')
        rows[0]['translation'] = '你好'
        self.assertEqual(plan(data, resource, rows), [])
        r = plan(data, resource, rows, allow_pattern_candidates=True)[0]
        self.assertEqual(r.role, 'Fox')
        self.assertEqual(r.symbol_source, 'Hello')
        rows[0]['symbol_source'] = 'different'
        with self.assertRaisesRegex(ValueError, 'pattern source'):
            plan(data, resource, rows, allow_pattern_candidates=True)

    def test_dictionary_only_value_tokens_change(self):
        data = b'{"key": "Hello", "keep": "ID-2"}\r\n'
        _, resource, rows = fixture(data, 'datav/dictionary.json')
        rows[0]['translation'] = '你好'
        rows[1].update(status='preserved', translation='ID-2')
        result = sfw.render_candidate(data, plan(data, resource, rows))
        self.assertEqual(result.decode(), '{"key": "你好", "keep": "ID-2"}\r\n')

    def test_dictionary_duplicate_key_rejected(self):
        with self.assertRaisesRegex(ValueError, 'duplicate'):
            sfw.parse_resource('datav/dictionary.json', b'{"key":"first","key":"second"}')

    def test_candidate_span_drift_and_overlap_rejected(self):
        data, resource, rows = fixture()
        replacements = plan(data, resource, rows)
        with self.assertRaises(ValueError): sfw.render_candidate(data, replacements * 2)
        with self.assertRaises(ValueError): sfw.render_candidate(data.replace(b'2 times', b'3 times'), replacements)


class RealSfwDataTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.manifest, cls.rows = sfw.load_ledger(DATA)
        cls.actual, cls.payloads = sfw.inventory_archive(ROOT / 'backup/cosmobreeder-multi.jar')
        cls.vsn_joins = [json.loads(line) for line in (DATA / 'vsn-joins.jsonl').read_text(encoding='utf-8').splitlines()]
        cls.polish = [json.loads(line) for line in (DATA / 'ds-polish.jsonl').read_text(encoding='utf-8').splitlines()]
        import dialogue_joins
        cls.unpolished, cls.unpolished_report = sfw.rebuild_candidate_entries(ROOT / 'backup/cosmobreeder-multi.jar', DATA,
                canonical_join_records=dialogue_joins.load_records(), allow_pattern_candidates=True, enable_ds_polish=False)

    def test_all_original_routes_identity_and_counts(self):
        self.assertEqual(self.actual['archive_sha256'], self.manifest['archive_sha256'])
        self.assertEqual(self.actual['resources'], self.manifest['resources'])
        self.assertEqual(len(self.payloads), 42)
        self.assertEqual(Counter(row['kind'] for row in self.rows), {'ds': 5471, 'ui': 871, 'vsn': 792})
        self.assertTrue(all(row['variant'] == 'sfw' and row['archive'] == sfw.ARCHIVE for row in self.rows))

    def test_all_candidates_complete_target_character_qa(self):
        required = json.loads((DATA / 'required_chars.json').read_text(encoding='utf-8'))
        glyphs = set(required['codepoints'])
        for row in self.rows:
            if row['status'] in ('candidate', 'reused_candidate'):
                with self.subTest(id=row['id']): sfw.validate_target(row['raw_source'], row['translation'], glyphs)

    def test_independent_gap_has_real_translations_not_empty_completion(self):
        coverage = json.loads((DATA / 'coverage.json').read_text(encoding='utf-8'))
        self.assertEqual(coverage['audit_460_ds_gap']['located_records'], 460)
        self.assertEqual(coverage['audit_460_ds_gap']['status'].get('needs_translation', 0), 0)
        self.assertTrue(all(row['translation'] for row in self.rows if row['status'] in ('candidate', 'reused_candidate')))

    def test_real_candidate_rebuild_and_sfw_pak_card_back_isolation(self):
        entries, report = sfw.rebuild_candidate_entries(ROOT / 'backup/cosmobreeder-multi.jar', DATA)
        self.assertEqual(len(entries), 42)
        resource = next(r for r in self.actual['resources'] if r['logical_path'] == 'datav/dictionary.json')
        ui = json.loads(entries[resource['archive_entry']])
        original_ui = json.loads(self.payloads['datav/dictionary.json'])
        self.assertEqual(ui['ui.card.CosmoCardBarker.desc.Back'], original_ui['ui.card.CosmoCardBarker.desc.Back'])
        self.assertTrue(ui['ui.card.CosmoCardBarker.desc.Back'].endswith('\n'))
        self.assertEqual(ui['ui.item.dataview'], '回忆')
        self.assertEqual(report['writes'], 0)
        self.assertEqual(sum(len(r['pattern_withheld']) for r in report['resources']), 272)

    def test_19_sfw_vsn_joins_preserve_all_controls_eols_and_last_lines(self):
        entries, report = sfw.rebuild_candidate_entries(ROOT / 'backup/cosmobreeder-multi.jar', DATA, allow_pattern_candidates=True)
        self.assertEqual(report['sfw_vsn_applied_groups'], 19)
        self.assertEqual(report['sfw_vsn_click_reduction'], 19)
        self.assertEqual(report['sfw_vsn_retained_groups'], 0)
        for resource in self.actual['resources']:
            path = resource['logical_path']
            if not path.endswith('.vsn'): continue
            before = self.payloads[path]; after = entries[resource['archive_entry']]
            b_lines = before.decode().splitlines(keepends=True)
            a_lines = after.decode().splitlines(keepends=True)
            with self.subTest(path=path):
                self.assertEqual(len(b_lines), len(a_lines))
                self.assertEqual([sfw._line_parts(x)[1] for x in b_lines], [sfw._line_parts(x)[1] for x in a_lines])
                self.assertEqual(sfw._vsn_controls(before), sfw._vsn_controls(after))
                if not sfw.VSN_TEXT.match(sfw._line_parts(b_lines[-1])[0]):
                    self.assertEqual(b_lines[-1], a_lines[-1])
                else:
                    last = sfw.parse_resource(path, before)[-1]
                    row = next(r for r in self.rows if r['logical_path'] == path and r['root'] == last['root']
                               and r['prefix'] == last['prefix'] and r['raw_source_sha256'] == last['raw_source_sha256']
                               and r['source_ordinal'] == last['source_ordinal'])
                    target = row['translation'] if row['status'] in ('candidate', 'reused_candidate') else row['raw_source']
                    self.assertEqual(a_lines[-1], row['prefix'] + target + sfw._line_parts(b_lines[-1])[1])
                b_roles = [(p['line'], p['prefix']) for p in sfw.parse_resource(path, before) if not p['prefix'].startswith('text:')]
                a_roles = [(p['line'], p['prefix']) for p in sfw.parse_resource(path, after) if not p['prefix'].startswith('text:')]
                self.assertEqual(b_roles, a_roles)

    def _vsn_join_fixture(self):
        join = copy.deepcopy(self.vsn_joins[0])
        path = join['logical_path']; original = self.payloads[path]
        rows = [r for r in self.rows if r['logical_path'] == path]
        resource = next(r for r in self.actual['resources'] if r['logical_path'] == path)
        replacements = sfw.candidate_replacements(archive=sfw.ARCHIVE, archive_sha256=self.actual['archive_sha256'],
            logical_path=path, archive_entry=resource['archive_entry'], original_bytes=original, records=rows,
            allow_pattern_candidates=True)
        return join, path, original, sfw.render_candidate(original, replacements), rows

    def test_vsn_join_duplicate_overlap_fails_closed(self):
        join, path, original, localized, rows = self._vsn_join_fixture()
        with self.assertRaisesRegex(ValueError, 'duplicate'):
            sfw.apply_vsn_joins(path, original, localized, rows, [join, join])

    def test_vsn_join_stage_and_auto_role_drift_fail_closed(self):
        join, path, original, localized, rows = self._vsn_join_fixture()
        with self.assertRaisesRegex(ValueError, 'staging'):
            sfw.apply_vsn_joins(path, original, localized.replace(b'rewind!', b'rewind?', 1), rows, [join])
        join['prefix'] = 'auto(1.0): '
        with self.assertRaisesRegex(ValueError, 'identity/prefix'):
            sfw.apply_vsn_joins(path, original, localized, rows, [join])

    def test_vsn_join_input_target_and_context_drift_fail_closed(self):
        join, path, original, localized, rows = self._vsn_join_fixture()
        join['inputs'][0]['input_translation_sha256'] = '0'*64
        with self.assertRaisesRegex(ValueError, 'input candidate drift'):
            sfw.apply_vsn_joins(path, original, localized, rows, [join])
        join, path, original, localized, rows = self._vsn_join_fixture()
        join['context_before'] = []
        with self.assertRaisesRegex(ValueError, 'stage context'):
            sfw.apply_vsn_joins(path, original, localized, rows, [join])

    def _polish_fixture(self, index=0):
        operation = copy.deepcopy(self.polish[index]); path = operation['logical_path']
        rows = [r for r in self.rows if r['logical_path'] == path]
        resource_report = next(r for r in self.unpolished_report['resources'] if r['logical_path'] == path)
        return operation, path, self.payloads[path], self.unpolished[operation['archive_entry']], rows, resource_report['canonical_join_report']

    def test_all_16_ds_polish_use_own_source_and_preserve_structure(self):
        import dialogue_joins
        entries, report = sfw.rebuild_candidate_entries(ROOT / 'backup/cosmobreeder-multi.jar', DATA,
                canonical_join_records=dialogue_joins.load_records(), allow_pattern_candidates=True)
        self.assertEqual(report['sfw_ds_polish_applied_operations'], 16)
        changed = 0
        for entry in ('datadf/1', 'datadm/1'):
            old = self.unpolished[entry].decode().splitlines(keepends=True)
            new = entries[entry].decode().splitlines(keepends=True)
            self.assertEqual(len(old), len(new))
            self.assertEqual([sfw._line_parts(s)[1] for s in old], [sfw._line_parts(s)[1] for s in new])
            changed += sum(a != b for a, b in zip(old, new))
        self.assertEqual(changed, 16)
        self.assertEqual(sum(r.get('canonical_join_report', {}).get('applied_groups', 0) for r in report['resources']), 834)

    def test_ds_polish_old_chinese_match_is_not_sufficient(self):
        operation, path, original, localized, rows, joins = self._polish_fixture()
        operation['source_inputs'][0]['raw_source'] = 'different English source'
        with self.assertRaisesRegex(ValueError, 'raw English'):
            sfw.apply_ds_polish(path, original, localized, rows, [operation], canonical_join_report=joins)

    def test_ds_polish_requires_actually_applied_own_join(self):
        operation, path, original, localized, rows, joins = self._polish_fixture()
        joins = copy.deepcopy(joins); joins['groups'] = []
        with self.assertRaisesRegex(ValueError, 'was not applied'):
            sfw.apply_ds_polish(path, original, localized, rows, [operation], canonical_join_report=joins)

    def test_ds_polish_duplicate_and_replay_are_rejected(self):
        operation, path, original, localized, rows, joins = self._polish_fixture()
        with self.assertRaisesRegex(ValueError, 'duplicate'):
            sfw.apply_ds_polish(path, original, localized, rows, [operation, operation], canonical_join_report=joins)
        result, _ = sfw.apply_ds_polish(path, original, localized, rows, [operation], canonical_join_report=joins)
        with self.assertRaisesRegex(ValueError, 'old Chinese'):
            sfw.apply_ds_polish(path, original, result, rows, [operation], canonical_join_report=joins)

    def test_intentional_corruption_preserved_and_proper_names_context_translated(self):
        corruption = [r for r in self.rows if any('intentional-corruption/source-preserved' in n for n in r['review_notes'])]
        self.assertEqual(len(corruption), 4)
        self.assertTrue(all(r['status'] == 'preserved' and r['translation'] == r['raw_source'] for r in corruption))
        self.assertFalse(any(r['status'] == 'needs_review' for r in self.rows))
        pup = next(r for r in self.rows if 'CAPTAIN PUPLOCK' in r['raw_source'])
        self.assertEqual(pup['status'], 'candidate'); self.assertIn('PUPLOCK', pup['translation'])
        dragon = next(r for r in self.rows if r['root'] == 'ui.card.CosmoCardDragon.desc.Front')
        self.assertEqual(dragon['status'], 'candidate'); self.assertIn('艾斯卡姆尔', dragon['translation']); self.assertIn('Sevaw', dragon['translation'])
        fragments = [r for r in self.rows if 'AND THEN YOU CAN TELL ME ABOUT THE BIG TEN...' in r['raw_source']]
        self.assertEqual(len(fragments), 2)
        self.assertTrue(all('BIG TEN...' in r['translation'] and '大触' not in r['translation'] for r in fragments))

    def test_all_60_ending_fields_fit_actual_classic8_32_cell_limit(self):
        font = ROOT / 'localization/optimization/r28/integration/tests/final-01/fonts/classic.fnt'
        metrics = {int(k): int(v) for k, v in re.findall(r'^char id=(\d+)\s+.*?xadvance=(-?\d+)', font.read_text(encoding='utf-8'), re.M)}
        values = {r['root']: r['translation'] if r['status'] in ('candidate', 'reused_candidate') else r['raw_source']
                  for r in self.rows if r['kind'] == 'ui'}
        report = sfw.validate_ending_fields(values, metrics)
        self.assertEqual(report['field_count'], 60)
        self.assertEqual(report['nonempty_fields'], 29)
        self.assertLessEqual(report['maximum_columns'], 32)
        self.assertLessEqual(report['maximum_width_px'], 256)
        self.assertEqual(values['ui.end.cr6'], '   FMOD STUDIO，由 FIRELIGHT 开发   ')
        old_values = dict(values); old_values['ui.end.cr6'] = '    FMOD STUDIO，由 FIRELIGHT 开发    '
        with self.assertRaisesRegex(ValueError, '32 columns/256px'):
            sfw.validate_ending_fields(old_values, metrics)

    def test_cosmetic_credit_padding_exception_cannot_change_other_fields(self):
        rows = copy.deepcopy([r for r in self.rows if r['kind'] == 'ui'])
        other = next(r for r in rows if r['root'] == 'ui.end.cr1')
        other.update(status='candidate', translation=other['raw_source'].strip())
        other['cosmetic_padding'] = {'source_left': 4, 'source_right': 4, 'target_left': 3, 'target_right': 3}
        with self.assertRaisesRegex(ValueError, 'edge whitespace'):
            sfw.candidate_replacements(archive=sfw.ARCHIVE, archive_sha256=self.actual['archive_sha256'],
                logical_path='datav/dictionary.json', archive_entry='datav/1',
                original_bytes=self.payloads['datav/dictionary.json'], records=rows)

    def test_existing_834_joins_and_new_unmatched_candidates_survive(self):
        import dialogue_joins
        records = dialogue_joins.load_records()
        entries, report = sfw.rebuild_candidate_entries(ROOT / 'backup/cosmobreeder-multi.jar', DATA,
                canonical_join_records=records, allow_pattern_candidates=True)
        self.assertEqual(sum(r.get('canonical_join_report', {}).get('applied_groups', 0) for r in report['resources']), 834)
        self.assertEqual(sum(len(r.get('canonical_join_report', {}).get('skipped', [])) for r in report['resources']), 122)
        female = entries['datadf/1'].decode('utf-8').splitlines()
        self.assertEqual(female[253], '  * 咦，一只狗？')
        self.assertIn('UP+ATTACK', '\n'.join(female))
        self.assertEqual(len(female), len(self.payloads['datadf/all.ds'].decode('utf-8').splitlines()))


if __name__ == '__main__': unittest.main()
