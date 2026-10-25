"""Identity/atomic merge gates; all fixtures are private project-local copies."""
from pathlib import Path
import io
import json
import sys
import tempfile
import unittest
import zipfile
sys.path.insert(0, str(Path(__file__).resolve().parents[1] / 'tools'))
from projectlib import PROJECT
from layout_bundle import read_layout_bundle, apply_layout_bundle, sha
from package import grow_font, replace_utf8
from classfile import load
sys.path.insert(0, str(PROJECT.parent / 'research'))
import research_patch as rp


class LayoutBundleTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.original = PROJECT.parent / 'backup/cosmobreeder-multi.jar'
        baseline = json.loads((PROJECT/'layout/baseline.json').read_text(encoding='utf-8'))
        cls.original_classes = {n+'.class': digest for n,digest in baseline['target_classes'].items()}
        cls.patched_classes = {}
        with zipfile.ZipFile(cls.original) as source:
            for entry in cls.original_classes:
                raw = source.read(entry)
                # Valid metadata-only fixture: preserve every existing pool index
                # and bytecode, append one unused UTF8 entry (some obfuscated
                # classes have no SourceFile attribute to edit).
                end, count = rp.cp_end(raw); pool = rp.Pool(count)
                pool.utf('layout-bundle-fixture')
                cls.patched_classes[entry] = raw[:8] + rp.u2(pool.count) + raw[10:end] + pool.bytes() + raw[end:]
            cls.target = cls.patched_classes['PRG/Yg.class']
            cls.other = source.read('PRG/Yq$b.class')
            cls.base_replacements = grow_font(source)
        for name in ('PRG/LayoutBridge', 'PRG/VsnLayout', 'PRG/SaveMenuLayout',
                     'PRG/ItemMenuLayout', 'cosmoloc/layout/FontAccess', 'cosmoloc/layout/PixelLayout'):
            minimal = rp.JVMClass(name); minimal.default_constructor()
            cls.patched_classes[name+'.class'] = minimal.bytes()
        cls.work = PROJECT / 'work/layout-bundle-tests'
        cls.work.mkdir(parents=True, exist_ok=True)

    def setUp(self):
        self.temp = tempfile.TemporaryDirectory(dir=self.work)
        self.root = Path(self.temp.name).resolve()
        self.assertTrue(self.root.is_relative_to(self.work.resolve()))
        self.addCleanup(self.temp.cleanup)
        (self.root/'classes/PRG').mkdir(parents=True)
        (self.root/'classes/PRG/Yg.class').write_bytes(self.target)
        (self.root/'fonts').mkdir()
        self.manifest = {'schema_version': 1, 'baseline_revision': 2, 'game_version': '1.0.5_full',
                         'status': 'candidate_not_accepted', 'runtime_activation': 'explicit_candidate_profiles_only',
                         'components': ['vsn-opening', 'save-single-card', 'item-selected-detail'],
                         'original_classes': self.original_classes.copy(),
                         'classes': {}, 'font_bindings': {}, 'sealed_resources': {}}
        for entry, raw in self.patched_classes.items():
            path = self.root/'classes'/entry
            path.parent.mkdir(parents=True, exist_ok=True); path.write_bytes(raw)
            self.manifest['classes'][entry] = {'path': 'classes/'+entry, 'sha256': sha(raw)}
        self.replacements = self.base_replacements.copy()
        for role, fnt, png in [('default', 'bbc2.fnt', 'bbc2-cjk-10.png'),
                               ('classic', 'classic.fnt', 'classic-cjk.png')]:
            fnt_raw = (PROJECT/'runtime'/fnt).read_bytes()
            png_raw = (PROJECT/'runtime'/png).read_bytes()
            (self.root/'fonts'/fnt).write_bytes(fnt_raw)
            (self.root/'fonts'/png).write_bytes(png_raw)
            self.replacements[fnt] = fnt_raw
            self.manifest['font_bindings'][role] = {'fnt_entry': fnt, 'fnt_sha256': sha(fnt_raw),
                                                     'runtime_png': png, 'png_sha256': sha(png_raw)}
            self.manifest['sealed_resources']['fonts/'+fnt] = sha(fnt_raw)
            self.manifest['sealed_resources']['fonts/'+png] = sha(png_raw)
        self.save()

    def save(self):
        (self.root/'layout-manifest.json').write_text(json.dumps(self.manifest), encoding='utf-8')

    def reject_apply(self, code=None):
        before = self.replacements.copy()
        with zipfile.ZipFile(self.original) as source:
            with self.assertRaises((ValueError, KeyError, OSError)):
                apply_layout_bundle(source, self.replacements, self.root, code)
        self.assertEqual(before, self.replacements, 'failed gate must not partially update caller table')

    def test_valid_bundle_and_actual_atlas_merge(self):
        doc, identity = read_layout_bundle(self.root)
        self.assertEqual(identity, sha((self.root/'layout-manifest.json').read_bytes()))
        with zipfile.ZipFile(self.original) as source:
            summary = apply_layout_bundle(source, self.replacements, self.root)
        self.assertFalse(summary['visual_acceptance'])
        self.assertEqual(self.replacements['PRG/Yg.class'], self.target)

    def test_consumer_identity_must_match_prepared_plan(self):
        before = self.replacements.copy()
        with zipfile.ZipFile(self.original) as source:
            with self.assertRaisesRegex(ValueError, 'changed after packaging plan'):
                apply_layout_bundle(source, self.replacements, self.root, expected_manifest_sha256='0'*64)
        self.assertEqual(before, self.replacements)

    def test_second_class_read_is_reverified_before_mutation(self):
        import layout_bundle
        from unittest.mock import patch
        safe = layout_bundle._safe_file
        calls = [0]
        owner = self
        class ChangingRead:
            def read_bytes(self):
                calls[0] += 1
                return owner.target if calls[0] == 1 else owner.other
        def changed(root, relative):
            path = safe(root, relative)
            return ChangingRead() if relative == 'classes/PRG/Yg.class' else path
        with patch.object(layout_bundle, '_safe_file', side_effect=changed):
            self.reject_apply()
        self.assertEqual(calls[0], 2)

    def test_missing_component_metadata_is_atomic(self):
        del self.manifest['components']; self.save(); self.reject_apply()

    def test_stale_baseline_revision_is_rejected(self):
        self.manifest['baseline_revision'] = 1; self.save(); self.reject_apply()

    def test_missing_activation_metadata_is_atomic(self):
        del self.manifest['runtime_activation']; self.save(); self.reject_apply()

    def test_target_identity_change_is_atomic(self):
        self.manifest['original_classes']['PRG/Yg.class'] = '0'*64; self.save()
        self.reject_apply()

    def test_previous_class_replacement_is_not_overwritten(self):
        self.replacements['PRG/Yg.class'] = b'earlier patch'
        self.reject_apply()

    def test_cp_pool_overlap_is_rejected(self):
        self.reject_apply({'PRG/Yg.class': {12: 'replacement'}})

    def test_missing_target_spec(self):
        self.manifest['classes'].clear(); self.save(); self.reject_apply()

    def test_class_sha_mismatch(self):
        (self.root/'classes/PRG/Yg.class').write_bytes(self.target+b'tampered')
        self.reject_apply()

    def test_class_internal_identity_mismatch(self):
        (self.root/'classes/PRG/Yg.class').write_bytes(self.other)
        self.manifest['classes']['PRG/Yg.class']['sha256'] = sha(self.other); self.save()
        self.reject_apply()

    def test_runtime_major_too_new_even_with_updated_hash(self):
        raw = self.target[:6] + (61).to_bytes(2, 'big') + self.target[8:]
        (self.root/'classes/PRG/Yg.class').write_bytes(raw)
        self.manifest['classes']['PRG/Yg.class']['sha256'] = sha(raw); self.save()
        self.reject_apply()

    def test_unsafe_bundle_relative_path(self):
        self.manifest['classes']['PRG/Yg.class']['path'] = '../Yg.class'; self.save()
        self.reject_apply()

    def test_sealed_resource_tamper(self):
        (self.root/'fonts/classic.fnt').write_bytes(b'wrong')
        self.reject_apply()

    def test_synchronized_removal_of_one_target_is_rejected(self):
        del self.manifest['classes']['PRG/LX.class']
        del self.manifest['original_classes']['PRG/LX.class']
        self.save(); self.reject_apply()

    def test_required_helper_cannot_be_omitted(self):
        del self.manifest['classes']['PRG/LayoutBridge.class']; self.save(); self.reject_apply()

    def test_missing_descriptor_only_helper_dependency(self):
        entry = 'cosmoloc/layout/PixelLayout.class'
        minimal = rp.JVMClass('cosmoloc/layout/PixelLayout'); minimal.default_constructor()
        minimal.field(1, 'missing', 'Lcosmoloc/layout/UnbundledHelper;')
        raw = minimal.bytes(); (self.root/'classes'/entry).write_bytes(raw)
        self.manifest['classes'][entry]['sha256'] = sha(raw); self.save(); self.reject_apply()

    def test_unpatched_target_cannot_be_declared_complete(self):
        with zipfile.ZipFile(self.original) as source: raw = source.read('PRG/Yg.class')
        (self.root/'classes/PRG/Yg.class').write_bytes(raw)
        self.manifest['classes']['PRG/Yg.class']['sha256'] = sha(raw); self.save(); self.reject_apply()

    def test_wrong_atlas_page_name_is_rejected(self):
        from codec import decrypt_file, encrypt_file
        with zipfile.ZipFile(self.original) as source: index = json.loads(decrypt_file(source.read('dataq/0')))
        key = 'dataq/'+str(index['/sprites.atlas'])
        text = decrypt_file(self.replacements[key]).decode('utf-8')
        self.replacements[key] = encrypt_file(text.replace('sprites.png', 'missing.png', 1).encode('utf-8'), bytes(32), bytes(8))
        self.reject_apply()

    def test_wrong_atlas_page_size_is_rejected(self):
        from codec import decrypt_file, encrypt_file
        with zipfile.ZipFile(self.original) as source: index = json.loads(decrypt_file(source.read('dataq/0')))
        key = 'dataq/'+str(index['/sprites.atlas'])
        text = decrypt_file(self.replacements[key]).decode('utf-8')
        self.assertIn('size: 4096, 6144', text)
        self.replacements[key] = encrypt_file(text.replace('size: 4096, 6144', 'size: 1, 1', 1).encode('utf-8'), bytes(32), bytes(8))
        self.reject_apply()

    def test_missing_font_pair(self):
        del self.manifest['font_bindings']['classic']; self.save(); self.reject_apply()

    def test_font_role_substitution(self):
        self.manifest['font_bindings']['default']['runtime_png'] = 'bbc2-cjk-8.png'; self.save()
        self.reject_apply()

    def test_unsealed_font_image(self):
        del self.manifest['sealed_resources']['fonts/bbc2-cjk-10.png']; self.save()
        self.reject_apply()

    def test_selected_fnt_mismatch(self):
        self.replacements['bbc2.fnt'] = b'8px font'; self.reject_apply()

    def test_actual_original_8px_atlas_cannot_pass_as_10px(self):
        self.replacements = {k:v for k,v in self.replacements.items() if k in ('bbc2.fnt', 'classic.fnt')}
        self.reject_apply()

    def test_helper_collision_in_original_archive(self):
        (self.root/'classes/PRG/Yq$b.class').write_bytes(self.other)
        self.manifest['classes']['PRG/Yq$b.class'] = {'path': 'classes/PRG/Yq$b.class', 'sha256': sha(self.other)}
        self.save(); self.reject_apply()

    def test_rejects_false_visual_acceptance_claim(self):
        self.manifest['status'] = 'accepted'; self.save(); self.reject_apply()


if __name__ == '__main__':
    unittest.main(verbosity=2)
