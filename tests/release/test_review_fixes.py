import json
import os
from pathlib import Path
import subprocess
import sys
import unittest
from unittest.mock import patch
import test_delta_release as fixtures
from cosmobreeder_patch import installer as i
from cosmobreeder_patch import delta
from cosmobreeder_patch.__main__ import license_text

def load_tests(loader, standard_tests, pattern):
    return unittest.TestSuite(ReviewFixTests(name) for name in ReviewFixTests.__dict__ if name.startswith('test_'))

class ReviewFixTests(fixtures.ReleaseTests):
    def test_manifest_bounds_and_types(self):
        self.populate()
        original = json.loads(json.dumps(self.m))
        for field in ('source_size', 'target_size', 'delta_size'):
            for bad in (True, False, 0, -1, 1.5, '100', None, 2**63, delta.MAX_FILE + 1):
                with self.subTest(field=field, value=bad):
                    m = json.loads(json.dumps(original))
                    m['files'][i.NAMES[0]][field] = bad
                    (self.payload / 'manifest.json').write_text(json.dumps(m), 'utf-8')
                    before = self.snapshot()
                    with self.assertRaises(ValueError): i.install(self.game, self.payload)
                    self.assertEqual(before, self.snapshot())
        (self.payload / 'manifest.json').write_text(json.dumps(original), 'utf-8')
        with patch.object(i, 'MAX_TOTAL', 1):
            with self.assertRaises(ValueError): i.manifest(self.payload)

    def test_delta_operation_limit(self):
        n = i.NAMES[0]
        p = self.payload / (n + '.cbd')
        p.write_bytes(b'CBDELTA1' + (b'C' + (0).to_bytes(8, 'big') + (1).to_bytes(4, 'big')) * 3 + b'E')
        e = dict(self.m['files'][n], delta_size=p.stat().st_size, delta_sha256=delta.sha(p))
        with patch.object(delta, 'MAX_OPS', 1):
            with self.assertRaisesRegex(ValueError, '指令数'):
                delta.apply(self.root / 'source0', p, self.root / 'out', e)

    def test_persistence_before_replace_and_cleanup(self):
        self.populate()
        sync_copy = i.sync_copy
        replace = os.replace
        synced = set()
        fsync = os.fsync
        sync_events = []
        def sync(fd):
            fsync(fd)
            sync_events.append(fd)
        def copy(s, d):
            count = len(sync_events)
            sync_copy(s, d)
            self.assertGreater(len(sync_events), count)
            synced.add(str(d))
        def replace_checked(s, d):
            if str(s).endswith(('.new', '.restore')) and Path(s).name != 'state.new':
                self.assertIn(str(s), synced)
            return replace(s, d)
        with patch.object(i.os, 'fsync', side_effect=sync), patch.object(i, 'sync_copy', side_effect=copy), patch.object(i.os, 'replace', side_effect=replace_checked):
            i.install(self.game, self.payload)
            i.uninstall(self.game, self.payload)

    def test_uninstall_interruption_retains_backups_and_retries(self):
        self.populate()
        before = self.snapshot()
        i.install(self.game, self.payload)
        replace = os.replace
        count = []
        def interrupted(s, d):
            count.append(1)
            if len(count) == 2: raise KeyboardInterrupt()
            return replace(s, d)
        with patch.object(i.os, 'replace', side_effect=interrupted):
            with self.assertRaises(KeyboardInterrupt): i.uninstall(self.game, self.payload)
        for n in i.NAMES:
            self.assertEqual(delta.sha(self.game / i.BACKUP / n), self.m['files'][n]['source_sha256'])
        self.assertTrue((self.game / i.STATE).is_file())
        i.uninstall(self.game, self.payload)
        self.assertEqual(before, self.snapshot())

    def test_restore_bad_result_keeps_backup(self):
        self.populate()
        i.install(self.game, self.payload)
        sync_file = i.sync_file
        def corrupt(path):
            sync_file(path)
            Path(path).write_bytes(b'unknown external modification')
        with patch.object(i, 'sync_file', side_effect=corrupt):
            with self.assertRaises(ValueError): i.uninstall(self.game, self.payload)
        self.assertTrue((self.game / i.BACKUP / i.NAMES[0]).is_file())
        before = self.snapshot()
        with self.assertRaises(ValueError): i.uninstall(self.game, self.payload)
        self.assertEqual(before, self.snapshot())

    def test_process_guard_real_parser(self):
        # Restore the real function hidden by the fixture's safety mock.
        self.guard.stop()
        if os.name != 'nt': self.skipTest('Windows tasklist parser')
        for name in (b'java.exe', b'JAVAw.EXE', b'Cosmobreeder.exe'):
            with patch.object(i.subprocess, 'run', return_value=subprocess.CompletedProcess([], 0, b'"' + name + b'","123"\r\n')):
                with self.assertRaises(ValueError): i.running_guard()
        with patch.object(i.subprocess, 'run', return_value=subprocess.CompletedProcess([], 0, b'"notjava.exe","123"\r\n')):
            i.running_guard()

    def test_path_link_refused(self):
        target = self.root / 'link-target'
        target.write_bytes(b'untouched')
        link = self.game / i.NAMES[0]
        try: link.symlink_to(target)
        except OSError: self.skipTest('OS does not grant symlink creation')
        with self.assertRaises(ValueError): i.context(self.game)
        self.assertEqual(target.read_bytes(), b'untouched')

    def test_source_licenses_and_symlink_refusal(self):
        text = license_text()
        self.assertIn('fonts/LICENSES/galmuri/LICENSE.txt', text)
        self.assertIn('SIL OPEN FONT LICENSE', text)
        base = self.root / 'bundle'
        base.mkdir()
        for n in ('LICENSE', 'NOTICE', 'THIRD_PARTY_NOTICES.md'): (base / n).write_text('text', 'utf-8')
        (base / 'licenses').mkdir()
        try: (base / 'licenses' / 'linked.txt').symlink_to(self.root / 'source0')
        except OSError: self.skipTest('OS does not grant symlink creation')
        with patch.object(sys, '_MEIPASS', str(base), create=True):
            with self.assertRaisesRegex(ValueError, '链接'): license_text()
