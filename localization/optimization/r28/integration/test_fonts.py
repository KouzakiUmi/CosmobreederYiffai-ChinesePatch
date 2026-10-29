"""CPU-only tests for supplemental font assets; all inputs read-only."""
from pathlib import Path
from io import BytesIO
import hashlib, json, sys, unittest, zipfile
ROOT=Path(__file__).resolve().parents[4]
sys.path.insert(0,str(ROOT/'localization/tools'))
import optimized_fonts as fonts
from layout_fonts import parse_fnt
from PIL import Image

class SupplementalFontTest(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.jar=ROOT/'localization/builds/r27-story12-shaderfix-test5/cosmobreeder-multi.jar'
        with zipfile.ZipFile(cls.jar) as z:
            cls.old={n:z.read(n) for n in ['bbc2.fnt','classic.fnt','story12.fnt']}
        cls.existing=fonts.build_assets(cls.jar,['中文 ABC……'])
        # These rare but normal BMP Chinese glyphs deliberately are not in r27.
        cls.expanded=fonts.build_assets(cls.jar,['中文 ABC……喆龘'])
    def test_existing_fnt_bytes_are_exact(self):
        self.assertEqual(self.existing['fnts'],self.old)
        self.assertTrue(all(not r['added_ids'] for r in self.existing['manifest']['roles'].values()))
    def test_expanded_coverage_and_original_metrics(self):
        for filename,raw in self.expanded['fnts'].items():
            before=parse_fnt(self.old[filename].decode('utf8'));after=parse_fnt(raw.decode('utf8'))
            self.assertTrue({ord('喆'),ord('龘')}<=set(after.glyphs))
            self.assertTrue(all(after.glyphs[cp]==g for cp,g in before.glyphs.items()))
    def test_new_cells_shader_channels(self):
        pages={k:Image.open(BytesIO(v)).convert('RGBA') for k,v in self.expanded['png_regions'].items()}
        for row in self.expanded['manifest']['added_rectangles']:
            image=pages[row['region']].crop(tuple(row['box']))
            self.assertEqual(image.getchannel('R').tobytes(),image.getchannel('A').tobytes())
            self.assertIsNotNone(image.getchannel('A').getbbox())
    def test_new_size_and_spacing_are_not_faked(self):
        for row in self.expanded['manifest']['roles'].values():
            font=parse_fnt(self.expanded['fnts'][row['fnt']].decode('utf8'))
            for cp in row['added_ids']:
                g=font.glyphs[cp];self.assertEqual(g['width'],row['glyph_size']);self.assertEqual(g['xadvance'],row['glyph_size'])
    def test_unicode_scope_is_explicit(self):
        with self.assertRaises(ValueError):fonts.required_ids(['\U0001f600'])
        with self.assertRaises(ValueError):fonts.required_ids(['\u200d\x00'])
        self.assertTrue({ord('A'),ord('a')}<=fonts.required_ids(['a']))
    def test_duplicate_replacement_rejected(self):
        sample=parse_fnt(self.old['bbc2.fnt'].decode('utf8')).glyphs[ord('中')]
        with self.assertRaises(ValueError):fonts.append_fnt(self.old['bbc2.fnt'],{ord('中'):sample})

if __name__=='__main__':unittest.main(verbosity=2)
