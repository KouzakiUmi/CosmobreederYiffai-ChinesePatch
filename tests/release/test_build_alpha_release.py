"""Original build entry regressions, synthetic inputs only; no EXE/game/install."""
from pathlib import Path
import importlib.util,json,tempfile,unittest,zipfile
ROOT=Path(__file__).resolve().parents[2]
spec=importlib.util.spec_from_file_location('alpha_builder',ROOT/'tools/build_alpha_release.py')
b=importlib.util.module_from_spec(spec);spec.loader.exec_module(b)

class OriginalBuilderTests(unittest.TestCase):
 def setUp(self):
  self.tmp=tempfile.TemporaryDirectory();self.base=Path(self.tmp.name);self.target=self.base/'r28-test';self.target.mkdir()
  for n in b.NAMES:(self.target/n).write_bytes(('synthetic:'+n).encode())
  self.info={'version':'r28-full-opt-candidate','status':'integrated_candidate_not_real_clip_CRT_input_acceptance','full_component_set':True,'archives':{n:{'sha256':b.sha(self.target/n)} for n in b.NAMES}}
  self.manifest=self.target/'build-manifest.json';self.manifest.write_text(json.dumps(self.info),encoding='utf8')
  self.accept={'status':'passed_cpu_and_independent_review_not_real_clip_CRT_input','archives':{n:b.sha(self.target/n) for n in b.NAMES},'build_manifest_sha256':b.sha(self.manifest)}
  self.acceptance=self.target/'acceptance.json';self.save()
 def save(self):self.acceptance.write_text(json.dumps(self.accept),encoding='utf8')
 def tearDown(self):self.tmp.cleanup()
 def test_legacy_baseline_remains_legacy(self):
  legacy=self.base/'r27-story12-shaderfix-test5';legacy.mkdir()
  self.assertEqual(b.target_identity(legacy),({'baseline':legacy.name},None))
 def test_accepted_r28_uses_actual_target_name(self):
  identity,record=b.target_identity(self.target)
  self.assertEqual(identity['baseline'],'r28-test');self.assertTrue(identity['candidate']);self.assertEqual(record,self.acceptance)
 def test_missing_acceptance_rejected(self):
  self.acceptance.unlink()
  with self.assertRaisesRegex(ValueError,'验收'):b.target_identity(self.target)
 def test_wrong_target_bytes_rejected(self):
  (self.target/b.NAMES[0]).write_bytes(b'changed')
  with self.assertRaisesRegex(ValueError,'SHA'):b.target_identity(self.target)
 def test_failed_acceptance_rejected(self):
  self.accept['status']='failed';self.save()
  with self.assertRaisesRegex(ValueError,'验收'):b.target_identity(self.target)
 def test_modified_build_manifest_rejected(self):
  self.manifest.write_text(json.dumps(self.info)+' ',encoding='utf8')
  with self.assertRaisesRegex(ValueError,'验收'):b.target_identity(self.target)
 def test_native8_complete_text_only(self):
  with zipfile.ZipFile(self.target/b.NAMES[0],'w') as z:
   for n in ['OFL8.txt','NOTICE.txt','LICENSES8/boutique-bitmap-7x7/OFL.txt','LICENSES8/galmuri/LICENSE.txt','LICENSES8/misaki/misaki.txt','LICENSES8/miseki-bitmap/LICENSE.txt']:z.writestr('r28-font/'+n,'许可・\n'+n)
   z.writestr('r28-font/not-for-distribution.png',b'not a license')
  result=b.native_font_notices(self.target)
  self.assertEqual(len(result),6);self.assertTrue(all(n.endswith('.txt') for n in result));self.assertTrue(all(v.decode('utf8').startswith('许可・') for v in result.values()))
 def test_native8_missing_component_rejected(self):
  with zipfile.ZipFile(self.target/b.NAMES[0],'w') as z:z.writestr('r28-font/OFL8.txt','license')
  with self.assertRaises(KeyError):b.native_font_notices(self.target)
 def test_original_exe_name_source_and_isolated_utf8_build(self):
  out=self.base/'new';args=b.exe_command(out/'payload',out/'licenses',[ROOT/'LICENSE'],out)
  self.assertEqual(args[args.index('--name')+1],'CosmobreederYiffai-alpha0.1-setup')
  self.assertEqual(args[args.index('--python-option')+1],'X utf8')
  self.assertEqual(args[-1],str(ROOT/'src/cosmobreeder_patch/__main__.py'))
  self.assertTrue(Path(args[args.index('--workpath')+1]).is_relative_to(out))
  self.assertNotIn('--uac-admin',args)

if __name__=='__main__':unittest.main(verbosity=2)
