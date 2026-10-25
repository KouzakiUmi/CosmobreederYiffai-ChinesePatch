import json
import os
from pathlib import Path
import sys
import tempfile
import unittest
from unittest.mock import patch

ROOT = Path(__file__).resolve().parents[2]
sys.path.insert(0, str(ROOT / 'src'))
from cosmobreeder_patch import installer as i
from cosmobreeder_patch.delta import build, apply, sha

class ReleaseTests(unittest.TestCase):
    def setUp(self):
        base = ROOT / '.local/release-audit/delta-release'
        base.mkdir(parents=True, exist_ok=True)
        self.tmp = tempfile.TemporaryDirectory(dir=base)
        self.root = Path(self.tmp.name)
        self.payload = self.root / 'payload'
        self.payload.mkdir()
        self.game = self.root / 'game'
        self.game.mkdir()
        self.m = {'version': 'alpha0.1', 'files': {}}
        self.sources = {}
        self.targets = {}
        for idx, n in enumerate(i.NAMES):
            source = bytes(range(256)) * 600 + bytes([idx]) * 1000
            target = source[:65536] + b'changed' + source[65543:] + b'new data'
            self.sources[n], self.targets[n] = source, target
            s, t = self.root / ('source' + str(idx)), self.root / ('target' + str(idx))
            s.write_bytes(source)
            t.write_bytes(target)
            e = build(s, t, self.payload / (n + '.cbd'))
            e['delta'] = n + '.cbd'
            self.m['files'][n] = e
        (self.payload / 'manifest.json').write_text(json.dumps(self.m), 'utf-8')
        self.guard = patch.object(i, 'running_guard')
        self.guard.start()
    def tearDown(self):
        self.guard.stop()
        self.tmp.cleanup()
    def populate(self, nsfw=True):
        for n in i.NAMES if nsfw else i.NAMES[:1]:
            (self.game / n).write_bytes(self.sources[n])
        saves = self.game / 'saves'
        saves.mkdir()
        (saves / 'untouched').write_bytes(b'USER SAVE')
    def snapshot(self):
        return {str(p.relative_to(self.game)): p.read_bytes() for p in self.game.rglob('*') if p.is_file()}
    def test_both_variants_exact_output_repeat_and_restore(self):
        for nsfw in (False, True):
            with self.subTest(nsfw=nsfw):
                self.populate(nsfw)
                before = self.snapshot()
                self.assertEqual(i.install(self.game, self.payload), 'nsfw' if nsfw else 'vanilla')
                for n in i.NAMES if nsfw else i.NAMES[:1]:
                    self.assertEqual((self.game / n).read_bytes(), self.targets[n])
                with self.assertRaises(ValueError):
                    i.install(self.game, self.payload)
                i.uninstall(self.game, self.payload)
                self.assertEqual(before, self.snapshot())
                for p in (self.game / 'saves').iterdir(): p.unlink()
                (self.game / 'saves').rmdir()
                for n in i.NAMES:
                    if (self.game / n).exists(): (self.game / n).unlink()
    def test_unknown_no_write(self):
        self.populate()
        (self.game / i.NAMES[1]).write_bytes(b'unknown')
        before = self.snapshot()
        with self.assertRaises(ValueError): i.install(self.game, self.payload)
        self.assertEqual(before, self.snapshot())
    def test_corrupt_delta_no_partial_install(self):
        self.populate()
        p = self.payload / (i.NAMES[1] + '.cbd')
        p.write_bytes(p.read_bytes()[:-1] + b'!')
        before = self.snapshot()
        with self.assertRaises(ValueError): i.install(self.game, self.payload)
        self.assertEqual(before, self.snapshot())
    def test_corrupt_output_even_with_updated_delta_sha(self):
        self.populate()
        self.m['files'][i.NAMES[1]]['target_sha256'] = '0' * 64
        (self.payload / 'manifest.json').write_text(json.dumps(self.m), 'utf-8')
        before = self.snapshot()
        with self.assertRaises(ValueError): i.install(self.game, self.payload)
        self.assertEqual(before, self.snapshot())
    def test_replace_exception_rolls_back(self):
        self.populate()
        before = self.snapshot()
        replace = os.replace
        calls = []
        def fail_second(s, d):
            calls.append(1)
            if len(calls) == 2: raise OSError('injected')
            return replace(s, d)
        with patch.object(i.os, 'replace', side_effect=fail_second):
            with self.assertRaises(OSError): i.install(self.game, self.payload)
        self.assertEqual(before, self.snapshot())
    def test_bad_backup_refused(self):
        self.populate()
        i.install(self.game, self.payload)
        (self.game / i.BACKUP / i.NAMES[0]).write_bytes(b'bad')
        before = self.snapshot()
        with self.assertRaises(ValueError): i.uninstall(self.game, self.payload)
        self.assertEqual(before, self.snapshot())
    def test_interrupted_transaction_recovery(self):
        self.populate()
        before = self.snapshot()
        i.install(self.game, self.payload)
        (self.game / i.STATE).unlink()
        (self.game / i.NAMES[1]).write_bytes(self.sources[i.NAMES[1]])
        i.uninstall(self.game, self.payload)
        self.assertEqual(before, self.snapshot())
    def test_old_backup_refused(self):
        self.populate()
        (self.game / i.BACKUP).mkdir()
        before = self.snapshot()
        with self.assertRaises(ValueError): i.install(self.game, self.payload)
        self.assertEqual(before, self.snapshot())
    def test_running_game_refused(self):
        self.populate()
        before = self.snapshot()
        with patch.object(i, 'running_guard', side_effect=ValueError('running')):
            with self.assertRaises(ValueError): i.install(self.game, self.payload)
        self.assertEqual(before, self.snapshot())
    def test_unknown_backup_file_preserved(self):
        self.populate()
        i.install(self.game, self.payload)
        (self.game / i.BACKUP / 'user-file').write_bytes(b'preserve')
        before = self.snapshot()
        with self.assertRaises(ValueError): i.uninstall(self.game, self.payload)
        self.assertEqual(before, self.snapshot())
    def test_replace_then_interrupt_rolls_back(self):
        self.populate()
        before = self.snapshot()
        replace = os.replace
        def interrupt_after(s, d):
            replace(s, d)
            raise KeyboardInterrupt()
        with patch.object(i.os, 'replace', side_effect=interrupt_after):
            with self.assertRaises(KeyboardInterrupt): i.install(self.game, self.payload)
        self.assertEqual(before, self.snapshot())
    def test_malformed_delta_with_matching_sha_refused(self):
        self.populate()
        n = i.NAMES[1]
        p = self.payload / (n + '.cbd')
        p.write_bytes(b'CBDELTA1C' + b'\xff' * 12 + b'E')
        self.m['files'][n]['delta_sha256'] = sha(p)
        (self.payload / 'manifest.json').write_text(json.dumps(self.m), 'utf-8')
        before = self.snapshot()
        with self.assertRaises(ValueError): i.install(self.game, self.payload)
        self.assertEqual(before, self.snapshot())
    def test_saves_not_even_opened(self):
        import builtins
        import io
        self.populate()
        before = self.snapshot()
        original_open, original_io_open = builtins.open, io.open
        saves = (self.game / 'saves').absolute()
        def guarded(original):
            def call(file, *a, **kw):
                if isinstance(file, (str, bytes, os.PathLike)) and not isinstance(file, bytes):
                    if Path(file).absolute().is_relative_to(saves):
                        raise AssertionError('save file accessed')
                return original(file, *a, **kw)
            return call
        with patch.object(builtins, 'open', guarded(original_open)), patch.object(io, 'open', guarded(original_io_open)):
            i.detect(self.game, i.verify(self.payload))
            i.install(self.game, self.payload)
            i.uninstall(self.game, self.payload)
        self.assertEqual(before, self.snapshot())
    def test_verify_never_accesses_game(self):
        with patch.object(i, 'context', side_effect=AssertionError('game accessed')):
            i.verify(self.payload)

if __name__ == '__main__': unittest.main()
