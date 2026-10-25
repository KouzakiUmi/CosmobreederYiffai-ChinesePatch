"""Verify code-pool and font packaging in memory without output/archive mutation."""
from pathlib import Path
import io
import json
import sys
import unittest
import zipfile
sys.path.insert(0,str(Path(__file__).resolve().parents[1]/'tools'))
from projectlib import PROJECT,read_json,digest,parse_atlas
from package import replace_utf8,grow_font
from codec import decrypt_file
from classfile import load
from PIL import Image


class PackageTests(unittest.TestCase):
    def test_cp_utf8_changes_preserve_bytecode(self):
        jar=next(a for a in read_json(PROJECT/'sources/archives.json') if a['tag']=='jar')
        with zipfile.ZipFile(jar['path']) as z:data=z.read('PRG/IV.class')
        cf=load(data);idx=next(v[1] for i,v in cf.cp.items.items() if v[0]==8 and cf.cp.utf8(v[1])=='PAWSED!')
        changed=replace_utf8(data,{idx:'暂停！'});other=load(changed)
        self.assertEqual(other.cp.utf8(idx),'暂停！')
        self.assertEqual(cf.this_name,other.this_name)
        for old,new in zip(cf.methods,other.methods):self.assertEqual(cf.code_of(old),other.code_of(new))
        with self.assertRaises(ValueError):replace_utf8(data,{65534:'错误'})
        with self.assertRaises(ValueError):replace_utf8(data,{idx:'🙂'})

    def test_both_archive_font_pages_are_coherent(self):
        for archive in read_json(PROJECT/'sources/archives.json'):
            before=digest(Path(archive['path']).read_bytes())
            with zipfile.ZipFile(archive['path']) as z:
                idx=json.loads(decrypt_file(z.read('dataq/0')));changes=grow_font(z)
                atlas=decrypt_file(changes['dataq/'+str(idx['/sprites.atlas'])]).decode('utf8')
                pages,regions=parse_atlas(atlas);self.assertEqual(len(pages),1)
                font=next(r for r in regions if r['name']=='bbc2')
                self.assertEqual(font['xy'],[0,4096]);self.assertEqual(font['size'],[2048,2048])
                with Image.open(io.BytesIO(decrypt_file(changes['dataq/'+str(idx['/sprites.png'])]))) as im:
                    self.assertEqual(im.size,(4096,6144))
                    # The current package explicitly selects the 10px page;
                    # cjkfont.png is the retained 12px research asset, not this pair.
                    with Image.open(PROJECT/'runtime/bbc2-cjk-10.png') as ref:self.assertEqual(im.crop((0,4096,2048,6144)).tobytes(),ref.convert('RGBA').tobytes())
            self.assertEqual(digest(Path(archive['path']).read_bytes()),before)


if __name__=='__main__':
    sys.stdout.reconfigure(encoding='utf8');unittest.main(verbosity=2)
