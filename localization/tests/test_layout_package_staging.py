"""Exercise the explicit package hook and inject failure after the first archive.
No production translations or installation paths are used/written.
"""
from contextlib import redirect_stdout
import io
import json
from pathlib import Path
import sys
import tempfile
import unittest
from unittest.mock import patch
import uuid
import zipfile
sys.path.insert(0, str(Path(__file__).resolve().parents[1]/'tools'))
import package as package_tool
from projectlib import PROJECT, digest


class LayoutPackageStagingTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.bundle = PROJECT/'builds/layout-r22-candidate-v2/layout-bundle'
        if not cls.bundle.is_dir(): raise unittest.SkipTest('Build the isolated r22 layout candidate first')
        cls.archives = package_tool.read_json(PROJECT/'sources/archives.json')
        for entry in cls.archives:
            entry['path'] = str(PROJECT.parent/'backup'/Path(entry['path']).name)
            if digest(Path(entry['path']).read_bytes()) != entry['sha256']:
                raise AssertionError('Fixture original identity mismatch')
        cls.original_read = staticmethod(package_tool.read_json)

    def setUp(self):
        self.parent = tempfile.TemporaryDirectory(dir=PROJECT/'builds')
        self.path = Path(self.parent.name).resolve()
        self.assertTrue(self.path.is_relative_to((PROJECT/'builds').resolve()))
        self.addCleanup(self.parent.cleanup)

    def execute(self, output, grow):
        def local_read(path):
            if Path(path).name == 'archives.json': return [dict(row) for row in self.archives]
            return self.original_read(path)
        args = ['package.py', '--write', '--output', str(output), '--layout-bundle', str(self.bundle)]
        # Only the translation production stages are stubbed; real archive, font,
        # class bundle, identity merge, ZIP integrity and publish code execute.
        with patch.object(package_tool, 'read_json', side_effect=local_read), \
             patch.object(package_tool, 'selected_translations', return_value={}), \
             patch.object(package_tool, 'approved_overrides', return_value={}), \
             patch.object(package_tool, 'render_resources', return_value={}), \
             patch.object(package_tool, 'patch_jar_dialogue', return_value={}), \
             patch.object(package_tool, 'code_changes', return_value={}), \
             patch.object(package_tool, 'grow_font', side_effect=grow), \
             patch.object(sys, 'argv', args), redirect_stdout(io.StringIO()):
            package_tool.main()

    def test_success_publishes_both_archives_with_consumed_bundle_identity(self):
        real = package_tool.grow_font
        output = self.path/'success'
        self.execute(output, real)
        manifest = json.loads((output/'package-manifest.json').read_text(encoding='utf-8'))
        self.assertEqual(len(manifest['archives']), 2)
        identity = digest((self.bundle/'layout-manifest.json').read_bytes())
        self.assertEqual(manifest['plan']['layout_bundle']['manifest_sha256'], identity)
        for record in manifest['archives']:
            path = output/record['archive']
            self.assertEqual(digest(path.read_bytes()), record['sha256'])
            with zipfile.ZipFile(path) as archive: self.assertIsNone(archive.testzip())
        self.assertFalse(manifest['plan']['source_installation_write'])

    def test_second_archive_failure_does_not_publish_first_archive(self):
        real = package_tool.grow_font
        calls = [0]
        def fail_second(source):
            calls[0] += 1
            if calls[0] == 2: raise RuntimeError('injected second archive failure')
            return real(source)
        output = self.path/'must-not-exist'
        with self.assertRaisesRegex(RuntimeError, 'injected second archive failure'):
            self.execute(output, fail_second)
        self.assertEqual(calls[0], 2)
        self.assertFalse(output.exists(), 'first JAR must remain in private staging, not final output')
        for record in self.archives:
            self.assertEqual(digest(Path(record['path']).read_bytes()), record['sha256'])


if __name__ == '__main__':
    unittest.main(verbosity=2)
