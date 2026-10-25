"""Regression for R26's real red-channel shader/transparent-white font failure."""
import hashlib
from io import BytesIO
from pathlib import Path
import sys
import unittest
import zipfile
from PIL import Image

ROOT=Path(__file__).resolve().parents[2]
sys.path.insert(0,str(ROOT/'localization/tools'))
import build_story_font12 as producer
from layout_fonts import parse_fnt


class StoryShaderTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.manifest,cls.files=producer.build_story_font12_assets(ROOT/'localization/work/story-font12/font12.zip')
        cls.font=parse_fnt(cls.files['story12.fnt'].decode('utf8'))
        cls.fixed=Image.open(BytesIO(cls.files['bbc2-shared-story12.png'])).convert('RGBA')
        with zipfile.ZipFile(ROOT/'localization/builds/r26-story12-test4/cosmobreeder-multi.jar') as jar:
            cls.broken=Image.open(BytesIO(jar.read('story12/bbc2-shared-story12.png'))).convert('RGBA')
            cls.shaders={name:jar.read(name) for name in ['shaders/vsn_term_shade.frag','shaders/cosmo_term_shade.frag']}

    @classmethod
    def cell(cls,image,code):
        g=cls.font.glyphs[code]
        return image.crop((g['x'],g['y'],g['x']+g['width'],g['y']+g['height']))

    def test_real_shaders_use_red_without_alpha_mask(self):
        expected={'shaders/vsn_term_shade.frag':'c58575de99d069aa6cfa10755e2fd222d67d78078958e99596d2907b761d45d5',
                  'shaders/cosmo_term_shade.frag':'0bbebcce2f3d76c2645e529fcd199fb3bea6b1205c2132665fd688c87c2fbeec'}
        for name,data in self.shaders.items():
            self.assertEqual(hashlib.sha256(data).hexdigest(),expected[name])
            self.assertIn(b'base_color.r > 0',data)
            self.assertNotIn(b'base_color.a >',data)

    def test_reproduce_released_r26_solid_middle_glyph(self):
        pixels=list(self.cell(self.broken,ord('中')).getdata())
        self.assertEqual(sum(a>0 for r,g,b,a in pixels),37)
        self.assertEqual(sum(r>0 for r,g,b,a in pixels),144)
        self.assertEqual(sum(r>0 and a==0 for r,g,b,a in pixels),107)

    def test_fixed_native_glyph_masks_match_real_shader_all_2312(self):
        count=0
        for code,g in self.font.glyphs.items():
            if g['y']<256:continue
            pixels=list(self.cell(self.fixed,code).getdata())
            self.assertTrue(all((r>0)==(a>0) for r,g,b,a in pixels),hex(code))
            self.assertTrue(all(p in ((0,0,0,0),(255,255,255,255)) for p in pixels),hex(code))
            count+=1
        self.assertEqual(count,2312)
        pixels=list(self.cell(self.fixed,ord('中')).getdata())
        self.assertEqual(sum(r>0 for r,g,b,a in pixels),37)

    def test_ink_and_metrics_unchanged_only_transparent_rgb_corrected(self):
        self.assertEqual(hashlib.sha256(self.files['story12.fnt']).hexdigest(),'972d49918484e3e5521a7da58dbe94f6c6c604e4f486844b75f5b3be87fa2546')
        self.assertEqual(self.fixed.getchannel('A').tobytes(),self.broken.getchannel('A').tobytes())
        self.assertEqual(self.fixed.crop((0,0,2048,256)).tobytes(),self.broken.crop((0,0,2048,256)).tobytes())
        self.assertEqual(hashlib.sha256(self.files['bbc2-shared-story12.png']).hexdigest(),producer.PNG_SHA256)


if __name__=='__main__':unittest.main()
