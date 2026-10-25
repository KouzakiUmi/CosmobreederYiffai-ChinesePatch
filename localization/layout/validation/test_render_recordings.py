"""Small CPU replay contract tests; no game init, window or filesystem writes."""
from pathlib import Path
import sys
import unittest
from PIL import Image
sys.path.insert(0, str(Path(__file__).resolve().parent))
from render_recordings import composite_checked, replay_scenario, sprite


class RecordingReplayTests(unittest.TestCase):
    def setUp(self):
        self.font = Image.new('RGBA',(4,2),(255,255,255,255))
        self.sheet = Image.new('RGBA',(4,4),(0,0,255,255))

    def text(self, x, y=0):
        return {'kind':'text','text':'A','font':'default','original_methods':['test.fixture'],
                'quads':[{'codepoint':65,'srcX':0,'srcY':0,'width':2,'height':1,'x':x,'screenTop':y}]}

    def scenario(self, calls):
        return {'id':'fixture','prototype':True,'status':'PASS','calls':calls}

    def replay(self, calls):
        return replay_scenario(self.scenario(calls),4,4,{},self.sheet,self.font)

    def test_exact_one_pixel_ink_overlap(self):
        image,report=self.replay([self.text(0),self.text(1)])
        self.assertEqual(report['text_overlap_pixels'],1)
        self.assertEqual(report['text_glyphs'],2)
        self.assertFalse(report['parent_clip_verified'])
        self.assertEqual(image.getpixel((0,0)),(255,255,255,255))

    def test_expected_rejection_is_not_reported_as_a_pass(self):
        scenario=self.scenario([]);scenario.update(status='EXPECTED_REJECTION',expected_error='overflow',error='overflow')
        image,report=replay_scenario(scenario,4,4,{},self.sheet,self.font)
        self.assertEqual(report['text_overlap_pixels'],0)
        self.assertEqual(report['scenario_status'],'EXPECTED_REJECTION')
        self.assertEqual(report['expected_error'],'overflow')

    def test_nonoverlap_and_touching_edges(self):
        image,report=self.replay([self.text(0),self.text(2)])
        self.assertEqual(report['text_overlap_pixels'],0)
        self.assertEqual(report['canvas_clip_events'],[])

    def test_transparent_padding_is_not_ink_overlap(self):
        self.font.putpixel((0,0),(255,255,255,0))
        image,report=self.replay([self.text(0),self.text(1)])
        self.assertEqual(report['text_overlap_pixels'],0)

    def test_clipped_glyph_is_reported_not_silently_accepted(self):
        image,report=self.replay([self.text(-1)])
        self.assertEqual(len(report['canvas_clip_events']),1)
        self.assertEqual(image.getpixel((0,0)),(255,255,255,255))

    def test_invalid_source_or_font_domain_fails(self):
        call=self.text(0);call['quads'][0]['srcX']=4
        with self.assertRaises(ValueError):self.replay([call])
        call=self.text(0);call['font']='classic'
        with self.assertRaises(ValueError):self.replay([call])
        with self.assertRaises(ValueError):self.replay([{'kind':'unknown'}])

    def test_fractional_pixel_coordinates_are_not_rounded(self):
        with self.assertRaises(ValueError):self.replay([self.text(0.5)])

    def test_sprite_trim_preserves_original_anchor(self):
        regions={'icon':[{'xy':[0,0],'size':[2,2],'orig':[4,4],'offset':[1,1],'rotation':0,'index':-1}]}
        image=sprite('icon',regions,self.sheet)
        self.assertEqual(image.size,(4,4))
        self.assertEqual(image.getpixel((1,1)),(0,0,255,255))
        self.assertEqual(image.getpixel((0,0))[3],0)
        regions['icon'][0]['rotation']=90
        with self.assertRaises(ValueError):sprite('icon',regions,self.sheet)

    def test_image_y_up_projection_and_scaling(self):
        regions={'fill':[{'xy':[0,0],'size':[1,1],'orig':[1,1],'offset':[0,0],'rotation':0,'index':-1}]}
        image,report=replay_scenario(self.scenario([{'kind':'rect','name':'fill','x':1,'y':1,'width':2,'height':1}]),
                                    4,4,regions,self.sheet,self.font)
        self.assertEqual(image.getpixel((1,2)),(0,0,255,255))
        self.assertEqual(image.getpixel((1,1)),(0,0,0,255))
        self.assertFalse(report['crt_verified'])


if __name__=='__main__':
    unittest.main(verbosity=2)
