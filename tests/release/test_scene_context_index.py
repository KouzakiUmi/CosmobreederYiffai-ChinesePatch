"""The public audit index contains translations and digests, not source rows."""
import json
from pathlib import Path
import sys
import tempfile
import unittest

sys.path.insert(0, str(Path(__file__).resolve().parents[2] / 'tools'))
from scene_context_index import check_fingerprint, export_index, fingerprint, public_target, verify_index  # noqa: E402


class SceneContextIndexTests(unittest.TestCase):
    def setUp(self):
        self.temp = tempfile.TemporaryDirectory()
        self.addCleanup(self.temp.cleanup)
        self.index = Path(self.temp.name) / 'index.jsonl'
        self.before = self.rows('旧译', '旧代码')
        self.after = self.rows('新译', 'UNTRANSLATED')

    @staticmethod
    def rows(text, code):
        return {
            'X': ('ui/fixture.tsv', ['X', 'fixture.jar', 'datav/1', 'menu', 'Sample line', text]),
            'Y': ('ui/fixture.tsv', ['Y', 'fixture.jar', 'datav/1', 'code', 'UNTRANSLATED', code]),
        }

    def test_chinese_only_and_hash_only_targets(self):
        self.assertEqual(export_index(self.index, self.after, self.before), 2)
        text = self.index.read_text(encoding='utf-8')
        records = [json.loads(line) for line in text.splitlines()]
        self.assertEqual(records[0]['target'], '新译')
        self.assertNotIn('target', records[1])
        self.assertNotIn('Sample line', text)
        self.assertNotIn('UNTRANSLATED', text)
        self.assertEqual(verify_index(self.index, self.after, self.before), 2)

    def test_verification_rejects_missing_change_against_baseline(self):
        export_index(self.index, self.after, self.before)
        first = self.index.read_text(encoding='utf-8').splitlines()[0]
        self.index.write_text(first + '\n', encoding='utf-8')
        with self.assertRaisesRegex(ValueError, '范围'):
            verify_index(self.index, self.after, self.before)

    def test_export_rejects_changed_source_column(self):
        self.after['X'][1][-2] = 'Different sample'
        with self.assertRaisesRegex(ValueError, '保护列'):
            export_index(self.index, self.after, self.before)
        self.assertFalse(self.index.exists())

    def test_public_target_excludes_source_embedded_in_translation(self):
        self.assertEqual(public_target(['Sample line', 'Sample line 中文']), {})

    def test_fingerprint_detects_truncation_and_nonindexed_changes(self):
        count = export_index(self.index, self.after, self.before)
        pins = self.index.with_suffix('.json')
        pins.write_text(json.dumps(fingerprint(self.index, self.after, count)), encoding='utf-8')
        check_fingerprint(self.index, pins, self.after, count)
        stale_rows = dict(self.after)
        stale_rows['unindexed'] = ('ui/file.tsv', ['unindexed', 'x'])
        with self.assertRaisesRegex(ValueError, '完整译文'):
            check_fingerprint(self.index, pins, stale_rows, count)
        first = self.index.read_text(encoding='utf-8').splitlines()[0]
        self.index.write_text(first + '\n', encoding='utf-8')
        with self.assertRaisesRegex(ValueError, '公开索引'):
            check_fingerprint(self.index, pins, self.after, 1)
