"""Reject malformed or missing TSV text without touching real game data."""
import json
from pathlib import Path
import sys
import tempfile
import unittest

sys.path.insert(0, str(Path(__file__).resolve().parents[2] / 'tools'))
from tl_tool import TAG_ARCHIVE, _sha, escape_tsv, reconstruct_text_entries  # noqa: E402


class TextReconstructionTests(unittest.TestCase):
    def setUp(self):
        local = tempfile.TemporaryDirectory()
        self.addCleanup(local.cleanup)
        self.root = Path(local.name)
        self.entries = {}
        for tag, archive in TAG_ARCHIVE.items():
            for family in ('datadf', 'datadm'):
                entry = family + '/1'
                self.add_template(tag, entry, '<Intro>\n  * Hello\n')
                row = [f'{tag}-{family}', archive, entry, 'Intro', '2', '  * ', 'Hello', '你好']
                self.chunk('dialogue', tag, family, [row])
            self.add_template(tag, 'vsn/5', 'text: Hello\n')
            self.add_template(tag, 'vsn/11', 'text: Again\n')
            self.chunk('vsn', tag, 'vsn', [
                [f'{tag}-vsn-a', archive, 'vsn/5', 'Intro', '1', 'text: ', 'Hello', '你好'],
                [f'{tag}-vsn-b', archive, 'vsn/11', 'Followup', '1', 'text: ', 'Again', '再见'],
            ])
            self.add_template(tag, 'datav/1', '{"one":"Hello","two":"Again"}\n')
            self.chunk('ui', tag, 'datav', [
                [f'{tag}-ui-a', archive, 'datav/1', 'one', 'Hello', '你好'],
                [f'{tag}-ui-b', archive, 'datav/1', 'two', 'Again', '再见'],
            ])
        self.add_template('jar', 'datay/1', '{"patchDictionary":{"label":"Hello"},"count":3}\n')
        self.chunk('ui', 'jar', 'datay', [
            ['jar-overlay', TAG_ARCHIVE['jar'], 'datay/1', '/patchDictionary/label', 'Hello', '你好'],
        ])
        (self.root / 'template/manifest.json').write_text(json.dumps({'entries': self.entries}), encoding='utf-8')

    def add_template(self, tag, name, content):
        path = self.root / 'template' / tag / name
        path.parent.mkdir(parents=True, exist_ok=True)
        data = content.encode('utf-8')
        path.write_bytes(data)
        self.entries[f'{tag}/{name}'] = {'sha256': _sha(data)}

    def chunk(self, kind, tag, name, rows):
        path = self.root / 'chunks' / kind / f'{tag}_{name}.tsv'
        path.parent.mkdir(parents=True, exist_ok=True)
        path.write_text(''.join('\t'.join(map(escape_tsv, row)) + '\n' for row in rows), encoding='utf-8')

    def test_complete_data_with_dialogue_soft_break(self):
        path = self.root / 'chunks/dialogue/jar_datadf.tsv'
        path.write_text(path.read_text(encoding='utf-8').replace('你好', '你⏎好'), encoding='utf-8')
        archives, _ = reconstruct_text_entries(self.root)
        self.assertEqual(sum(map(len, archives.values())), 11)
        self.assertIn('你│好'.encode(), archives[TAG_ARCHIVE['jar']]['datadf/1'])

    def test_escaped_script_newline_is_rejected(self):
        path = self.root / 'chunks/dialogue/jar_datadf.tsv'
        path.write_text(path.read_text(encoding='utf-8').replace('你好', escape_tsv('普通台词\nFAKE: 第二行')), encoding='utf-8')
        with self.assertRaisesRegex(ValueError, '新的脚本行或控制字符'):
            reconstruct_text_entries(self.root)

    def test_missing_chunk_is_rejected(self):
        path = self.root / 'chunks/dialogue/jar_datadf.tsv'
        path.rename(path.with_suffix('.hidden'))
        with self.assertRaisesRegex(ValueError, '缺少分块'):
            reconstruct_text_entries(self.root)

    def test_missing_vsn_resource_is_rejected(self):
        path = self.root / 'chunks/vsn/jar_vsn.tsv'
        path.write_text(path.read_text(encoding='utf-8').splitlines()[0] + '\n', encoding='utf-8')
        with self.assertRaisesRegex(ValueError, '脚本定位范围'):
            reconstruct_text_entries(self.root)

    def test_missing_ui_key_is_rejected(self):
        path = self.root / 'chunks/ui/jar_datav.tsv'
        path.write_text(path.read_text(encoding='utf-8').splitlines()[0] + '\n', encoding='utf-8')
        with self.assertRaisesRegex(ValueError, '界面键集合'):
            reconstruct_text_entries(self.root)
