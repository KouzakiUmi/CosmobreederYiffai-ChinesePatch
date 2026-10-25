"""Synthetic-only installer tests; all generated files stay in the owned work tree."""
import argparse
from contextlib import redirect_stdout
import hashlib
import importlib.util
import io
import json
from pathlib import Path
import sys
import tempfile
import unittest
from unittest.mock import patch

PROJECT = Path(__file__).resolve().parents[1]
WORK = PROJECT / 'work/layout-test-installer-unit'
NAMES = ('cosmobreeder-multi.jar', 'patch.pak')
ORIGINAL = dict(zip(NAMES, (b'original jar', b'original pak')))
R21 = dict(zip(NAMES, (b'r21 jar', b'r21 pak')))
PAYLOAD = dict(zip(NAMES, (b'layout test jar', b'layout test pak')))


def digest(data):
    return hashlib.sha256(data).hexdigest()


def load_module(name, path):
    spec = importlib.util.spec_from_file_location(name, path)
    module = importlib.util.module_from_spec(spec)
    sys.modules[name] = module
    spec.loader.exec_module(module)
    return module


class LayoutTestInstallerTests(unittest.TestCase):
    def setUp(self):
        WORK.mkdir(parents=True, exist_ok=True)
        self.root = Path(tempfile.mkdtemp(prefix='case-', dir=WORK)).resolve()
        self.assertTrue(self.root.is_relative_to(WORK.resolve()))
        self.prepared = self.root / 'prepared'
        self.prepared.mkdir()
        self.game = self.root / 'synthetic-game'
        self.game.mkdir()
        source = (PROJECT / 'packaging/patch_tool.py').read_text(encoding='utf-8')
        source = source.replace('BACKUP_DIRNAME = "_汉化补丁备份"', 'BACKUP_DIRNAME = "_中文排版测试备份"')
        source = source.replace('STATE_NAME = "install-state.json"', 'STATE_NAME = "layout-test-install-state.json"')
        source = source.replace('if cur == e["sha256"]:\n            warnings.append',
                                'if cur == e["sha256"] and cur != e["original"]["sha256"]:\n            warnings.append')
        (self.prepared / 'base_patch_tool.py').write_text(source, encoding='utf-8')
        wrapper = (PROJECT / 'packaging/layout_test_backend.py').read_text(encoding='utf-8')
        (self.prepared / 'patch_tool.py').write_text(wrapper, encoding='utf-8')
        payload = self.prepared / 'payload'
        payload.mkdir()
        for name, data in PAYLOAD.items():
            (payload / name).write_bytes(data)
        self.manifest = {'name': 'isolated layout test', 'version': 'layout-test-1',
                         'built': '2026-10-25', 'status': 'layout_test_not_accepted',
                         'activation': {'layout': True}, 'variants': {}}
        for tag, contents in [('original', ORIGINAL), ('r21', R21)]:
            self.manifest['variants'][tag] = {
                'label': tag, 'available': True,
                'detect': {p: {'sha256': digest(contents[p])} for p in NAMES},
                'files': [{'path': p, 'payload': p, 'sha256': digest(PAYLOAD[p]),
                           'original': {'sha256': digest(contents[p])}} for p in NAMES]}
        self.save_manifest()
        self.seed_game(ORIGINAL)
        self.sentinels = {'install-state.json': b'old official state\x00\xff',
                          'sav/slot1.sav': b'private save\x00\x01',
                          'options.json': b'user options\xff',
                          '_汉化补丁备份/cosmobreeder-multi.jar': b'old official jar backup',
                          '_汉化补丁备份/patch.pak': b'old official pak backup',
                          '_汉化补丁备份/sentinel': b'never change'}
        for name, data in self.sentinels.items():
            p = self.game / name
            p.parent.mkdir(parents=True, exist_ok=True)
            p.write_bytes(data)
        previous = {name: sys.modules.get(name) for name in ('base_patch_tool', 'patch_tool')}
        def restore_modules():
            for name, module in previous.items():
                if module is None:
                    sys.modules.pop(name, None)
                else:
                    sys.modules[name] = module
        self.addCleanup(restore_modules)
        self.base = load_module('base_patch_tool', self.prepared / 'base_patch_tool.py')
        self.tool = load_module('patch_tool', self.prepared / 'patch_tool.py')
        self.args = argparse.Namespace(game_dir=str(self.game), force=False, backup_dir=None)
        self.addCleanup(self.check_sentinels)

    def save_manifest(self):
        (self.prepared / 'manifest.json').write_text(json.dumps(self.manifest), encoding='utf-8')

    def seed_game(self, contents):
        for name, data in contents.items():
            (self.game / name).write_bytes(data)

    def snapshot(self):
        return {str(p.relative_to(self.game)): p.read_bytes() for p in self.game.rglob('*') if p.is_file()}

    def check_sentinels(self):
        for name, data in self.sentinels.items():
            self.assertEqual((self.game / name).read_bytes(), data, name)

    def call(self, function):
        with redirect_stdout(io.StringIO()):
            return function(self.args)

    def assert_refused_without_writes(self, function):
        before = self.snapshot()
        with self.assertRaises((ValueError, SystemExit, OSError)):
            self.call(function)
        self.assertEqual(self.snapshot(), before)

    def test_unchanged_pak_is_not_a_duplicate_install(self):
        source = dict(R21, **{'patch.pak': PAYLOAD['patch.pak']})
        self.seed_game(source)
        variant = self.manifest['variants']['r21']
        variant['detect']['patch.pak']['sha256'] = digest(PAYLOAD['patch.pak'])
        variant['files'][1]['original']['sha256'] = digest(PAYLOAD['patch.pak'])
        self.save_manifest()
        self.assertEqual(self.call(self.tool.cmd_install), 0)
        self.assertEqual(self.call(self.tool.cmd_uninstall), 0)
        for name,data in source.items(): self.assertEqual((self.game/name).read_bytes(), data)

    def test_failure_before_game_write_never_rewrites_untouched_files(self):
        before = self.snapshot()
        opened = []
        original_open = io.open
        def watch(path, mode='r', *args, **kwargs):
            if 'w' in mode: opened.append(str(path))
            return original_open(path, mode, *args, **kwargs)
        with patch.object(self.base.shutil, 'copy2', side_effect=OSError('backup disk fixture failure')), \
                patch.object(self.base.io, 'open', side_effect=watch):
            with self.assertRaises(OSError): self.call(self.tool.cmd_install)
        self.assertEqual(self.snapshot(), before)
        self.assertEqual(opened, [])

    def test_original_and_r21_install_check_uninstall(self):
        for source in (ORIGINAL, R21):
            with self.subTest(source=source):
                self.seed_game(source)
                # Existing same-hash backups are legal; avoid deleting any fixture data.
                bdir = self.game / self.tool.BACKUP_DIRNAME
                bdir.mkdir(exist_ok=True)
                for name, data in source.items():
                    (bdir / name).write_bytes(data)
                self.assertEqual(self.call(self.tool.cmd_install), 0)
                for name in NAMES:
                    self.assertEqual((self.game / name).read_bytes(), PAYLOAD[name])
                self.assertEqual(self.call(self.tool.cmd_check), 0)
                self.assertEqual(self.call(self.tool.cmd_uninstall), 0)
                for name in NAMES:
                    self.assertEqual((self.game / name).read_bytes(), source[name])
                self.assertFalse((self.game / self.tool.STATE_NAME).exists())
                self.check_sentinels()

    def test_verify_payload_is_read_only_without_game_discovery(self):
        before = self.snapshot()
        with patch.object(self.base, 'find_game', side_effect=AssertionError('discovery forbidden')), \
             patch.object(self.base, 'resolve_game', side_effect=AssertionError('game read forbidden')), \
             patch.object(self.base, 'read_state', side_effect=AssertionError('state read forbidden')), \
             patch.object(self.base, 'write_state', side_effect=AssertionError('write forbidden')):
            result = self.tool.verify_payload()
        self.assertEqual(result['sha256'], {p: digest(PAYLOAD[p]) for p in NAMES})
        self.assertEqual(result['files'], result['sha256'])
        self.assertEqual(result['version'], self.manifest['version'])
        self.assertEqual(result['activation'], {'layout': True})
        self.assertEqual(result['status'], self.manifest['status'])
        self.assertIs(result['game_started'], False)
        self.assertIs(result['installed'], False)
        self.assertEqual(self.snapshot(), before)

    def test_frozen_payload_root_uses_existing_meipass_mechanism(self):
        extracted = self.root / 'extracted'
        extracted.mkdir()
        (extracted / 'manifest.json').write_bytes((self.prepared / 'manifest.json').read_bytes())
        (extracted / 'payload').mkdir()
        for p in NAMES:
            (extracted / 'payload' / p).write_bytes(PAYLOAD[p])
        with patch.object(sys, '_MEIPASS', str(extracted), create=True):
            base = load_module('base_patch_tool', self.prepared / 'base_patch_tool.py')
            wrapper = load_module('patch_tool', self.prepared / 'patch_tool.py')
        self.assertEqual(base.ROOT, str(extracted))
        self.assertEqual(wrapper.verify_payload()['status'], self.manifest['status'])
        self.assertIs(wrapper.find_game, base.find_game)
        self.assertIs(wrapper.check_game_dir, base.check_game_dir)

    def test_payload_corruption_refuses_without_writes(self):
        (self.prepared / 'payload/patch.pak').write_bytes(b'corrupt')
        self.assert_refused_without_writes(self.tool.cmd_install)
        with self.assertRaisesRegex(ValueError, '损坏'):
            self.tool.verify_payload()

    def test_unknown_game_version_refuses_without_writes(self):
        (self.game / 'patch.pak').write_bytes(b'unknown')
        self.assert_refused_without_writes(self.tool.cmd_install)

    def test_force_and_custom_backup_refused_for_install_and_uninstall(self):
        for function in (self.tool.cmd_install, self.tool.cmd_uninstall):
            for attr, value in [('force', True), ('backup_dir', str(self.root / 'foreign'))]:
                with self.subTest(command=function.__name__, attr=attr):
                    with patch.object(self.args, attr, value):
                        self.assert_refused_without_writes(function)
        self.assertFalse((self.root / 'foreign').exists())

    def test_main_dispatches_to_wrapper(self):
        before = self.snapshot()
        with patch.object(sys, 'argv', ['patch_tool.py', 'install', '--force', '--game-dir', str(self.game)]):
            with self.assertRaisesRegex(ValueError, '禁止'):
                self.tool.main()
        self.assertEqual(self.snapshot(), before)
        self.assertIs(self.base.cmd_install, self.tool.cmd_install)
        self.assertIs(self.base.cmd_uninstall, self.tool.cmd_uninstall)

    def test_path_drift_is_refused_without_writes(self):
        mutations = [('path', '../outside.jar'), ('path', '/absolute.jar'),
                     ('path', 'other.jar'), ('payload', '../patch.pak'),
                     ('payload', 'sub/patch.pak'), ('payload', 'C:\\patch.pak')]
        entry = self.manifest['variants']['original']['files'][0]
        for key, value in mutations:
            with self.subTest(key=key, value=value):
                old = entry[key]
                entry[key] = value
                self.save_manifest()
                self.assert_refused_without_writes(self.tool.cmd_install)
                entry[key] = old
        self.manifest['variants']['original']['detect']['../other'] = {'absent': True}
        self.save_manifest()
        self.assert_refused_without_writes(self.tool.cmd_install)

    def test_existing_incorrect_test_backup_refused(self):
        bdir = self.game / self.tool.BACKUP_DIRNAME
        bdir.mkdir()
        (bdir / NAMES[0]).write_bytes(b'foreign backup')
        self.assert_refused_without_writes(self.tool.cmd_install)

    def test_any_existing_test_state_even_malformed_refuses(self):
        for data in (b'{broken', b'{}', b'null'):
            (self.game / self.tool.STATE_NAME).write_bytes(data)
            self.assert_refused_without_writes(self.tool.cmd_install)

    def test_second_payload_partial_write_rolls_back_all_files_and_new_backups(self):
        before = self.snapshot()
        original_copy = self.base.shutil.copy2
        def fail_second(src, dst, *args, **kwargs):
            if Path(src).parent == self.prepared / 'payload' and Path(src).name == 'patch.pak':
                Path(dst).write_bytes(b'partially overwritten pak')
                raise PermissionError('injected second write')
            return original_copy(src, dst, *args, **kwargs)
        with patch.object(self.base.shutil, 'copy2', side_effect=fail_second):
            with self.assertRaises(SystemExit):
                self.call(self.tool.cmd_install)
        self.assertEqual(self.snapshot(), before)
        self.assertFalse((self.game / self.tool.BACKUP_DIRNAME).exists())

    def test_state_write_failure_rolls_back_and_preserves_existing_test_backups(self):
        bdir = self.game / self.tool.BACKUP_DIRNAME
        bdir.mkdir()
        for name, data in ORIGINAL.items():
            (bdir / name).write_bytes(data)
        (bdir / 'sentinel').write_bytes(b'old test backup user data')
        before = self.snapshot()
        def fail_state(game, state):
            (Path(game) / self.tool.STATE_NAME).write_bytes(b'partial state')
            raise OSError('injected state write failure')
        with patch.object(self.base, 'write_state', side_effect=fail_state):
            with self.assertRaisesRegex(OSError, 'injected state'):
                self.call(self.tool.cmd_install)
        self.assertEqual(self.snapshot(), before)

    def test_rollback_failure_is_explicit_not_success(self):
        original_open = self.tool.io.open
        def fail_restore(path, mode='r', *args, **kwargs):
            if Path(path) == self.game / NAMES[0] and mode == 'wb':
                raise OSError('injected rollback failure')
            return original_open(path, mode, *args, **kwargs)
        with patch.object(self.base, 'write_state', side_effect=OSError('install failure')), \
             patch.object(self.tool.io, 'open', side_effect=fail_restore):
            with self.assertRaisesRegex(RuntimeError, 'rollback 失败'):
                self.call(self.tool.cmd_install)

    def test_uninstall_preserves_user_modified_files_and_returns_skip(self):
        self.assertEqual(self.call(self.tool.cmd_install), 0)
        (self.game / NAMES[0]).write_bytes(b'user post-install change')
        self.assertEqual(self.call(self.tool.cmd_uninstall), 1)
        self.assertEqual((self.game / NAMES[0]).read_bytes(), b'user post-install change')
        self.assertEqual((self.game / NAMES[1]).read_bytes(), ORIGINAL[NAMES[1]])
        self.assertTrue((self.game / self.tool.STATE_NAME).exists())

    def test_uninstall_preserves_switch_to_another_known_source(self):
        self.seed_game(R21)
        self.assertEqual(self.call(self.tool.cmd_install), 0)
        state=json.loads((self.game/self.tool.STATE_NAME).read_text('utf8'))
        self.assertEqual(state['source_sha256'], {p:digest(v) for p,v in R21.items()})
        (self.game/NAMES[0]).write_bytes(ORIGINAL[NAMES[0]])
        self.assertEqual(self.call(self.tool.cmd_uninstall), 1)
        self.assertEqual((self.game/NAMES[0]).read_bytes(), ORIGINAL[NAMES[0]])
        self.assertEqual((self.game/NAMES[1]).read_bytes(), R21[NAMES[1]])
        self.assertTrue((self.game/self.tool.STATE_NAME).exists())

    def test_other_known_backup_version_cannot_replace_exact_source(self):
        self.assertEqual(self.call(self.tool.cmd_install), 0)
        (self.game/self.tool.BACKUP_DIRNAME/NAMES[0]).write_bytes(R21[NAMES[0]])
        self.assert_refused_without_writes(self.tool.cmd_uninstall)

    def test_uninstall_missing_backup_returns_skip_and_retains_state(self):
        self.assertEqual(self.call(self.tool.cmd_install), 0)
        # Rename only this freshly-created private backup after checking the absolute targets.
        source = (self.game / self.tool.BACKUP_DIRNAME / NAMES[0]).resolve()
        target = source.with_name('private-hidden-backup.jar')
        self.assertTrue(source.is_relative_to(self.root))
        self.assertTrue(target.is_relative_to(self.root))
        source.rename(target)
        self.assertEqual(self.call(self.tool.cmd_uninstall), 1)
        self.assertTrue((self.game / self.tool.STATE_NAME).exists())

    def test_uninstall_refuses_foreign_backup_or_foreign_state(self):
        self.assertEqual(self.call(self.tool.cmd_install), 0)
        (self.game / self.tool.BACKUP_DIRNAME / NAMES[0]).write_bytes(b'foreign backup')
        self.assert_refused_without_writes(self.tool.cmd_uninstall)
        (self.game / self.tool.BACKUP_DIRNAME / NAMES[0]).write_bytes(ORIGINAL[NAMES[0]])
        sp = self.game / self.tool.STATE_NAME
        state = json.loads(sp.read_text(encoding='utf-8'))
        for field, value in [('version', 'foreign'), ('patch', 'foreign'),
                             ('backup_dir', str(self.root)), ('files', ['../foreign'])]:
            changed = dict(state, **{field: value})
            sp.write_text(json.dumps(changed), encoding='utf-8')
            self.assert_refused_without_writes(self.tool.cmd_uninstall)
        sp.write_text('{}', encoding='utf-8')
        self.assert_refused_without_writes(self.tool.cmd_uninstall)

    def test_uninstall_without_test_state_does_not_restore_test_backups(self):
        bdir = self.game / self.tool.BACKUP_DIRNAME
        bdir.mkdir()
        for name, data in ORIGINAL.items():
            (bdir / name).write_bytes(data)
        self.assert_refused_without_writes(self.tool.cmd_uninstall)

    def test_uninstall_preserves_nonzero_backend_result(self):
        self.assertEqual(self.call(self.tool.cmd_install), 0)
        with patch.object(self.tool, '_uninstall', return_value=7):
            self.assertEqual(self.call(self.tool.cmd_uninstall), 7)


if __name__ == '__main__':
    unittest.main(verbosity=2)
