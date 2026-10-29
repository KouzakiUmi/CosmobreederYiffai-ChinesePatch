"""Frozen PAK VSN join regressions. No canonical/archive/install writes."""
import copy
import json
from pathlib import Path
import sys
import unittest
import zipfile

LOC = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(LOC / 'tools'))
import vsn_joins as vsn
from codec import decrypt_file


class VsnJoinTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.manifest, cls.records = vsn._load()
        cls.pins = cls.manifest['resources']
        cls.before, cls.original = {}, {}
        resources = {r['logical_path']: r for r in (json.loads(row) for row in (LOC / 'catalog/resources.jsonl').read_text('utf8').splitlines())}
        with zipfile.ZipFile(LOC / 'builds/r27-story12-shaderfix-test5/patch.pak') as z:
            assert vsn.sha(Path(z.filename).read_bytes()) == cls.manifest['frozen_archive_sha256']
            for p, pin in cls.pins.items():
                cls.before[p] = decrypt_file(z.read(pin['archive_entry']))
                cls.original[p] = (LOC / resources[p]['blob_path']).read_bytes()
        cls.reviews = [json.loads(row) for row in (vsn.DATA / 'review-ledger.jsonl').read_text('utf8').splitlines()]

    def test_all_67_files_and_300_explicit_groups(self):
        groups = removed = 0
        for path, data in self.before.items():
            with self.subTest(path=path):
                result, report = vsn.apply_joins(path, self.original[path], data)
                self.assertEqual(vsn.rewrite_vsn(path, data)[0], result)
                old, new = vsn._split(data), vsn._split(result)
                selected = [r for r in self.records if r['logical_path'] == path]
                changed = {n for r in selected for n in r['physical_lines']}
                self.assertEqual(len(old), len(new))
                for n, (a,b) in enumerate(zip(old,new), 1):
                    self.assertEqual(vsn._body_eol(a)[1], vsn._body_eol(b)[1])
                    if n not in changed: self.assertEqual(a,b)
                for r in selected:
                    nums = r['physical_lines']
                    self.assertEqual(vsn._body_eol(new[nums[0]-1])[0].decode('utf8'), 'text: '+r['replacement'])
                    for n in nums[1:]: self.assertEqual(new[n-1], vsn._body_eol(old[n-1])[1] or b' ')
                groups += report['applied_groups']; removed += report['removed_text_nodes']
                self.assertEqual(report['automatic_delay_delta_seconds'], 0)
                self.assertEqual(report['input_sha256'], vsn.sha(data))
                self.assertEqual(report['output_sha256'], vsn.sha(result))
        self.assertEqual((len(self.before),groups,removed),(67,300,324))

    def test_review_edges_form_an_exact_disjoint_partition(self):
        candidate = json.loads((LOC.parent / 'docs/font-layout-audit-20261025/text-review/results/vsn-merge-candidates.json').read_text('utf8'))
        expected = {(c['logical_path'],tuple(c['lines'])) for c in candidate['candidates']}
        accepted, retained = set(), set()
        for row in self.reviews:
            self.assertTrue(row['reviewed_context'])
            self.assertTrue(row['inputs'])
            self.assertFalse(row['origin']['independent_qa_approval'])
            for join in row['joins']:
                ns = join['physical_lines']
                accepted.update((row['logical_path'],(a,b)) for a,b in zip(ns,ns[1:]))
            for skip in row['skipped_edges']:
                self.assertTrue(skip['reason'].strip())
                retained.add((row['logical_path'],tuple(skip['lines'])))
        self.assertEqual(len(self.reviews),391)
        self.assertEqual((len(accepted),len(retained)),(324,97))
        self.assertFalse(accepted & retained)
        self.assertEqual(accepted | retained,expected)
        self.assertEqual(sum(len(r['skipped_edges']) for r in self.reviews if r['inputs'][0]['prefix'].startswith('lang(')),72)

    def test_source_and_occurrence_identity_chain(self):
        for r in self.records:
            for item in r['inputs']:
                self.assertEqual(vsn.sha(item['source_en'].encode('utf8')), item['source_sha256'])
                self.assertEqual(vsn.sha(item['input_line'].encode('utf8')),item['input_line_sha256'])
                self.assertTrue(item['occurrence_id']); self.assertTrue(item['raw_payload_sha256'])
                self.assertEqual(item['prefix'],'text: ')
            self.assertEqual(r['control_evidence']['intervening_controls'],[])

    def test_control_auto_and_glyph_roles_remain_byte_identical(self):
        for path,data in self.before.items():
            result,_=vsn.rewrite_vsn(path,data)
            old,new=vsn._split(data),vsn._split(result)
            controls=[i for i,x in enumerate(old) if not vsn.TEXT.match(vsn._body_eol(x)[0].decode('utf8'))]
            self.assertEqual([old[i] for i in controls],[new[i] for i in controls])
            protected=[i for i,x in enumerate(old) if x.startswith((b'lang(',b'auto('))]
            self.assertEqual([old[i] for i in protected],[new[i] for i in protected])

    def test_four_untranslated_continuations_are_identified_and_consumed_once(self):
        four=json.loads((vsn.DATA/'continuation-translations.json').read_text('utf8'))
        self.assertEqual(len(four),4)
        for t in four:
            self.assertEqual(t['status'],'candidate_user_requested')
            self.assertTrue(t['canonical_translation_unchanged'])
            self.assertRegex(t['candidate_zh_CN'],r'[\u3400-\u9fff]')
            used=[r for r in self.records if any(i['occurrence_id']==t['occurrence_id'] for i in r['inputs'])]
            self.assertEqual(len(used),1)
            self.assertEqual(used[0]['operation_id'],t['applied_in_join'])
            out,report=vsn.rewrite_vsn(t['logical_path'],self.before[t['logical_path']])
            self.assertNotIn(t['source_en'],out.decode('utf8'))
            self.assertEqual(sum(m['occurrence_id']==t['occurrence_id'] for m in report['occurrence_mapping']),1)

    def test_semantic_edits_not_fragment_concatenation(self):
        rs={r['review_group_id']:r for r in self.records}
        self.assertEqual(rs['VG002']['replacement'].count('眼前'),1)
        self.assertEqual(rs['VG010']['replacement'].count('那些'),1)
        self.assertEqual(rs['VG150']['replacement'].count('越来越'),1)
        self.assertIn('满十八岁才准实操训练',rs['VG338']['replacement'])
        self.assertIn('二十一岁的成年男人',rs['VG337']['replacement'])
        self.assertNotIn('on that other',rs['VG141']['replacement'])
        self.assertEqual(rs['VG031']['physical_lines'],[69,70])
        self.assertNotIn('VG043',rs)

    def test_reviewed_text_and_markup_conservation_with_explicit_edit_spans(self):
        for r in self.records:
            text=''.join(i['input_line'][6:].strip() for i in r['inputs'])
            edits=r['text_edit_evidence']
            self.assertEqual(''.join(e['before'] for e in edits),text)
            self.assertEqual(''.join(e['after'] for e in edits),r['replacement'])
            self.assertEqual(vsn._markers(text),vsn._markers(r['replacement']))
            self.assertNotRegex(r['replacement'],r'[\r\n\x00-\x1f\u2028\u2029]|<p>|\|')

    def test_explicit_noop_still_checks_exact_source(self):
        path=self.records[0]['logical_path']; data=self.before[path]
        self.assertEqual(vsn.rewrite_vsn(path,data,records=[])[0],data)
        with self.assertRaises(vsn.VsnJoinValidationError): vsn.rewrite_vsn(path,data+b' ',records=[])

    def test_atomic_rejection_on_late_record_drift_duplicate_or_injection(self):
        path=max(self.before,key=lambda p:sum(r['logical_path']==p for r in self.records))
        selected=[r for r in self.records if r['logical_path']==path]
        mutations=[]
        for key,value in [('replacement','注入\ncut(0.06): Black'),('physical_lines',[1,2]),('archive','cosmobreeder-multi.jar'),('input_resource_sha256','0'*64),('source_resource_sha256','0'*64)]:
            rows=copy.deepcopy(selected); rows[-1][key]=value; mutations.append(rows)
        rows=copy.deepcopy(selected);rows[-1]['inputs'][0]['occurrence_id']='fake';mutations.append(rows)
        mutations.append(selected+[selected[-1]])
        for rows in mutations:
            saved=self.before[path]
            with self.assertRaises(vsn.VsnJoinValidationError):vsn.rewrite_vsn(path,saved,records=rows)
            self.assertEqual(saved,self.before[path])

    def test_resource_or_control_drift_and_wrong_english_fail_closed(self):
        r=self.records[0];p=r['logical_path'];data=self.before[p]
        for mutated in (data+b'\n',data.replace(b'rewind!',b'sync!',1),data.replace(b'\n',b'\r\n'),self.original[p]):
            with self.assertRaises(vsn.VsnJoinValidationError):vsn.rewrite_vsn(p,mutated)
        with self.assertRaises(vsn.VsnJoinValidationError):vsn.apply_joins(p,self.original[p]+b' ',data)
        with self.assertRaises(vsn.VsnJoinValidationError):vsn.rewrite_vsn('vsn/not-pinned/script.vsn',data)

    def test_every_sfw_shared_resource_rejected_even_same_physical_line(self):
        with zipfile.ZipFile(LOC/'builds/r27-story12-shaderfix-test5/cosmobreeder-multi.jar') as z:
            index=json.loads(decrypt_file(z.read('vsn/0')))
            for logical,entry in index.items():
                if not logical.endswith('/script.vsn'):continue
                path='vsn/'+logical.strip('/').split('/')[-2]+'/script.vsn'
                data=decrypt_file(z.read('vsn/'+str(entry)))
                with self.assertRaisesRegex(vsn.VsnJoinValidationError,'Archive identity'):vsn.rewrite_vsn(path,data,archive='cosmobreeder-multi.jar')
                if vsn.sha(data)!=self.pins[path]['r27_plaintext_sha256']:
                    with self.assertRaises(vsn.VsnJoinValidationError):vsn.rewrite_vsn(path,data)

    def test_all_reviewed_output_glyphs_exist_in_frozen_story12(self):
        import re
        with zipfile.ZipFile(LOC/'builds/r27-story12-shaderfix-test5/cosmobreeder-multi.jar') as z:
            ids=set(map(int,re.findall(rb'char id=(\d+)',z.read('story12.fnt'))))
        chars=set(''.join(r['replacement'] for r in self.records))
        self.assertFalse({ord(c) for c in chars}-ids)
        self.assertEqual(vsn.sha((vsn.DATA/'required_chars.txt').read_bytes()),self.manifest['required_chars_sha256'])

    def test_physical_eol_split_preserves_non_line_unicode_and_missing_eof(self):
        for data in (b'',b'a',b'a\n',b'a\r\nb\rc\n', 'text: 字\u2028字\u2029\f尾'.encode('utf8')):
            self.assertEqual(b''.join(vsn._split(data)),data)

if __name__=='__main__': unittest.main()
