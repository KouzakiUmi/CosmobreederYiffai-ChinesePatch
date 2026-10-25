"""Real SFW source-version regressions; no JVM/game or install/save access."""
from pathlib import Path
import copy
import json
import sys
import unittest
import zipfile
sys.path.insert(0,str(Path(__file__).resolve().parents[1]/'tools'))
from projectlib import PROJECT
from codec import decrypt_file
import dialogue_sfw


class SfwDialogueTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.records=[json.loads(x) for x in (PROJECT/'tests/fixtures/dialogue-joins-initial.jsonl').read_text('utf8').splitlines()]
        with zipfile.ZipFile(PROJECT.parent/'backup/cosmobreeder-multi.jar') as a,zipfile.ZipFile(PROJECT/'builds/final-8146-r21-images/cosmobreeder-multi.jar') as b:
            cls.original=decrypt_file(a.read('datadf/1'));cls.localized=decrypt_file(b.read('datadf/1'))

    def test_real_sfw_root_matching_does_not_reuse_pak_lines(self):
        result,report=dialogue_sfw.rewrite_sfw('datadf/all.ds',self.original,self.localized,self.records)
        group=next(g for g in report['groups'] if g['join_id']=='DJ007')
        self.assertEqual(group['actual_sfw_lines'],[2010,2011])
        self.assertNotEqual(group['actual_sfw_lines'],[2011,2012])
        lines=result.decode('utf8').splitlines()
        self.assertIn('频率27.850',lines[2009])
        self.assertEqual(lines[2010],'')
        # This SFW text says OUR SATELLITE, not SATELLITE R18: do not force the PAK join.
        self.assertTrue(any(s['join_id']=='DJ006' and s['matches']==0 for s in report['skipped']))
        self.assertGreater(report['translated_by_exact_root_prefix_source'],0)
        self.assertGreaterEqual(report['applied_groups'],5)
        before=self.localized.decode('utf8').splitlines(keepends=True);after=result.decode('utf8').splitlines(keepends=True)
        self.assertEqual(len(before),len(after))
        self.assertEqual([dialogue_sfw.split_line(x)[1] for x in before],[dialogue_sfw.split_line(x)[1] for x in after])

    def test_additional_source_comment_shifts_real_match_not_targeting_old_line(self):
        result,report=dialogue_sfw.rewrite_sfw('datadf/all.ds',b'// private source-version fixture\n'+self.original,b'// private source-version fixture\n'+self.localized,self.records)
        group=next(g for g in report['groups'] if g['join_id']=='DJ007')
        self.assertEqual(group['actual_sfw_lines'],[2011,2012])
        self.assertTrue(result.startswith(b'// private source-version fixture\n'))

    def test_source_wording_difference_is_reported_not_wrongly_joined(self):
        record=next(r for r in self.records if r['join_id']=='DJ007')
        # Change both source/localized data only inside this private fixture.
        original=self.original.replace(b'IF YOU COME ACROSS ANY NEW CREATURES, FEEL FREE TO',b'IF YOU COME ACROSS A DIFFERENT SOURCE VERSION',1)
        self.assertNotEqual(original,self.original)
        _,report=dialogue_sfw.rewrite_sfw('datadf/all.ds',original,self.localized,[record])
        self.assertEqual(report['applied_groups'],0)
        self.assertEqual(report['skipped'][0]['join_id'],'DJ007')

    def test_non_dialogue_control_drift_rejected(self):
        changed=self.localized.replace(b'<Area0_Macsen1.Hello>',b'<Area0_Macsen1.BadHeader>',1)
        self.assertNotEqual(changed,self.localized)
        with self.assertRaisesRegex(ValueError,'control/header'):
            dialogue_sfw.rewrite_sfw('datadf/all.ds',self.original,changed,self.records)

    def test_tampered_merged_text_cannot_skip_canonical_validation(self):
        records=copy.deepcopy(self.records);records[0]['merged_translation']='篡改文本'
        with self.assertRaises(ValueError):dialogue_sfw.rewrite_sfw('datadf/all.ds',self.original,self.localized,records)

    def test_ambiguous_original_source_group_is_not_applied_twice(self):
        record=next(r for r in self.records if r['join_id']=='DJ007')
        source=self.original.decode('utf8').splitlines(keepends=True);localized=self.localized.decode('utf8').splitlines(keepends=True)
        duplicate=''.join(source[2009:2011]);loc_duplicate=''.join(localized[2009:2011])
        source.insert(2011,duplicate);localized.insert(2011,loc_duplicate)
        _,report=dialogue_sfw.rewrite_sfw('datadf/all.ds',''.join(source).encode(),''.join(localized).encode(),[record])
        self.assertEqual(report['applied_groups'],0)
        self.assertEqual(report['skipped'][0]['matches'],2)


if __name__=='__main__':unittest.main()
