"""Isolated, read-only-source tests for exact frozen r27 PAK DS polish."""
import copy
import json
from pathlib import Path
import re
import sys
import unittest
from unittest.mock import patch
import zipfile

HERE=Path(__file__).resolve().parent
LOC=HERE.parents[3]
sys.path.insert(0,str(HERE));sys.path.insert(0,str(LOC/'tools'))
import ds_polish as ds
from codec import decrypt_file


class DsPolishTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.manifest,cls.ops=ds.load_data()
        cls.reviews=[json.loads(row) for row in (HERE/'review-ledger.jsonl').read_text('utf8').splitlines()]
        with zipfile.ZipFile(LOC/'builds/r27-story12-shaderfix-test5/patch.pak') as z:
            cls.sources={p:decrypt_file(z.read(pin['archive_entry'])) for p,pin in cls.manifest['resources'].items()}

    def test_all_sixteen_exact_revisions_preserve_every_other_byte(self):
        count=0
        for path,data in self.sources.items():
            result,report=ds.rewrite_ds_polish(path,data)
            old,new=ds.split(data),ds.split(result)
            ops=[o for o in self.ops if o['logical_path']==path]
            changed={o['line'] for o in ops}
            self.assertEqual(len(old),len(new))
            for n,(a,b) in enumerate(zip(old,new),1):
                self.assertEqual(ds.body_eol(a)[1],ds.body_eol(b)[1])
                if n not in changed:self.assertEqual(a,b)
            for op in ops:self.assertEqual(ds.body_eol(new[op['line']-1])[0].decode('utf8'),op['output_line'])
            self.assertEqual(report['applied_revisions'],len(ops))
            self.assertEqual(report['removed_text_nodes'],0)
            self.assertEqual(report['control_or_timing_changes'],0)
            count+=report['applied_revisions']
        self.assertEqual(count,16)
        self.assertEqual(sum(o['logical_path']=='datadf/all.ds' for o in self.ops),3)

    def test_all_21_unit_risks_have_explicit_review_and_real_stutters_stay(self):
        units=[r for r in self.reviews if r['kind']=='unit-cjk-word-hyphen']
        self.assertEqual(len(units),21)
        self.assertEqual(sum(r['decision']=='revised' for r in units),7)
        self.assertEqual(sum(r['decision']=='retained' for r in units),14)
        for r in units:
            self.assertTrue(r['reason']);self.assertTrue(r['source_case']['unit']['source'])
            if r['decision']=='retained':
                for item in r['source_case']['occurrences']:
                    o=item['occurrence'];p=o['logical_path'];n=item['effective_line']
                    out,_=ds.rewrite_ds_polish(p,self.sources[p])
                    self.assertEqual(ds.split(out)[n-1],ds.split(self.sources[p])[n-1])

    def test_merged_hyphens_reviewed_without_touching_model_or_interruptions(self):
        rows=[r for r in self.reviews if r['kind']=='merged-ascii-hyphen']
        self.assertEqual(len(rows),17)
        self.assertEqual(sum(r['decision']=='revised' for r in rows),11)
        self.assertEqual(sum(r['decision']=='retained' for r in rows),6)
        model=next(r for r in rows if r['case_id']=='DM04')
        self.assertEqual(model['classification'],'model-identifier')
        self.assertIn('3P-X69',model['source_case']['join']['merged_translation'])
        for r in rows:
            if r['decision']=='retained':
                j=r['source_case']['join'];p=j['logical_path'];n=j['physical_lines'][0]
                out,_=ds.rewrite_ds_polish(p,self.sources[p])
                self.assertEqual(ds.split(out)[n-1],ds.split(self.sources[p])[n-1])

    def test_five_missing_skips_are_not_falsely_all_word_cutoffs(self):
        rows=json.loads((HERE/'derived-skips.json').read_text('utf8'))
        self.assertEqual(len(rows),5)
        self.assertIn('不是词中断',rows[0]['reason'])
        self.assertIn('后续猜测',rows[4]['reason'])
        for row in rows:
            edge=row['source_case']['edge'];p=edge['logical_path']
            result,_=ds.rewrite_ds_polish(p,self.sources[p]);old,new=ds.split(self.sources[p]),ds.split(result)
            for n in edge['lines']:self.assertEqual(old[n-1],new[n-1])
            self.assertEqual(row['decision'],'retained');self.assertTrue(row['reason'])

    def test_semantic_and_punctuation_samples(self):
        byid={o['operation_id']:o for o in self.ops}
        self.assertIn('功能完好的休息区',byid['DSP-datadf-2582']['replacement'])
        self.assertIn('功能完好的休息区',byid['DSP-datadm-2603']['replacement'])
        for n in (4623,4637,4651,4665,4679,4693):
            self.assertIn('目前所处区域',byid['DSP-datadm-'+str(n)]['replacement'])
        last=byid['DSP-datadm-4789']['replacement']
        self.assertTrue(last.endswith('。'));self.assertIn('造成的伤害',last);self.assertNotIn('-',last)
        self.assertIn('——以及此地供给的能量——',byid['DSP-datadf-1919']['replacement'])

    def test_text_edit_spans_markers_occurrences_and_sources_conserved(self):
        for row in self.ops:
            self.assertEqual(''.join(e['before'] for e in row['text_edits']),row['old_text'])
            self.assertEqual(''.join(e['after'] for e in row['text_edits']),row['replacement'])
            self.assertEqual(ds.markers(row['old_text']),ds.markers(row['replacement']))
            self.assertNotRegex(row['replacement'],r'[\x00-\x1f\u2028\u2029]|<p>|\|')
            for i in row['inputs']:
                self.assertTrue(i['occurrence_id']);self.assertTrue(i['raw_payload_sha256'])
                self.assertEqual(ds.sha(i['source_en'].encode('utf8')),i['source_sha256'])

    def test_headers_prefixes_blank_join_rows_and_control_tokens_unchanged(self):
        for p,data in self.sources.items():
            out,_=ds.rewrite_ds_polish(p,data)
            old,new=ds.split(data),ds.split(out)
            revised={o['line'] for o in self.ops if o['logical_path']==p}
            for n,a in enumerate(old,1):
                if n not in revised:self.assertEqual(a,new[n-1])
            for token in (b'@DerekChipReport',b'do {',b'noselect',b'noamendfreq',b'<',b'>'):
                self.assertEqual(data.count(token),out.count(token))

    def test_wrong_archive_source_variant_repeat_or_eol_fails_closed(self):
        f=self.sources['datadf/all.ds'];m=self.sources['datadm/all.ds']
        for p,b,archive in [('datadf/all.ds',f,'cosmobreeder-multi.jar'),('datadf/all.ds',m,'patch.pak'),
                            ('datadm/all.ds',f,'patch.pak'),('unknown',f,'patch.pak'),
                            ('datadf/all.ds',f+b' ','patch.pak'),('datadf/all.ds',f.replace(b'\n',b'\r\n'),'patch.pak')]:
            with self.assertRaises(ds.DsPolishValidationError):ds.rewrite_ds_polish(p,b,archive)
        out,_=ds.rewrite_ds_polish('datadf/all.ds',f)
        with self.assertRaises(ds.DsPolishValidationError):ds.rewrite_ds_polish('datadf/all.ds',out)

    def test_late_invalid_record_is_atomic_and_rejects_header_prefix_injection(self):
        path='datadm/all.ds';saved=self.sources[path]
        changes=[('full_header','<Other>'),('prefix','do {'),('input_line','wrong'),
                 ('replacement','插入\n  do {bad}'),('source_resource_sha256','0'*64)]
        for key,value in changes:
            ops=copy.deepcopy(self.ops);target=[o for o in ops if o['logical_path']==path][-1];target[key]=value
            with patch.object(ds,'load_data',return_value=(self.manifest,ops)):
                with self.assertRaises(ds.DsPolishValidationError):ds.rewrite_ds_polish(path,saved)
            self.assertEqual(saved,self.sources[path])

    def test_all_required_glyphs_available_in_frozen_10_and_12_fonts(self):
        chars=set(''.join(o['replacement'] for o in self.ops))
        with zipfile.ZipFile(LOC/'builds/r27-story12-shaderfix-test5/cosmobreeder-multi.jar') as z:
            for font in ('bbc2.fnt','story12.fnt'):
                ids=set(map(int,re.findall(rb'char id=(\d+)',z.read(font))))
                self.assertFalse({ord(c) for c in chars}-ids,font)
        self.assertEqual(ds.sha((HERE/'required_chars.txt').read_bytes()),self.manifest['required_chars_sha256'])

    def test_canonical_join_ledger_hash_is_unmodified(self):
        data=(LOC/'translations/dialogue-joins.jsonl').read_bytes()
        self.assertEqual(ds.sha(data),self.manifest['canonical_join_ledger_sha256'])
        self.assertEqual(len(data.splitlines()),956)

if __name__=='__main__':unittest.main()
