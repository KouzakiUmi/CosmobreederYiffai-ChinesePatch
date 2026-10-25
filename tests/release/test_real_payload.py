"""Explicit opt-in integration: only fresh fixtures, never the original installation."""
import os
from pathlib import Path
import shutil
import sys
import tempfile
import unittest
from unittest.mock import patch
ROOT = Path(__file__).resolve().parents[2]
sys.path.insert(0, str(ROOT / 'src'))
from cosmobreeder_patch import installer as i
from cosmobreeder_patch.delta import sha

@unittest.skipUnless(os.environ.get('CB_REAL_DELTA_TEST') == '1', 'opt in with CB_REAL_DELTA_TEST=1')
class RealPayloadTests(unittest.TestCase):
    def test_real_both_variants(self):
        payload = ROOT / 'dist/alpha0.1/payload'
        m = i.verify(payload)
        base = ROOT / '.local/release-audit/delta-release'
        base.mkdir(parents=True, exist_ok=True)
        for nsfw in (False, True):
            with self.subTest(nsfw=nsfw), tempfile.TemporaryDirectory(dir=base) as tmp:
                game = Path(tmp)
                names = i.NAMES if nsfw else i.NAMES[:1]
                for n in names: shutil.copyfile(ROOT / 'backup' / n, game / n)
                (game / 'save-sentinel').write_bytes(b'NOT ACCESSED BY INSTALLER')
                with patch.object(i, 'running_guard'):
                    i.install(game, payload)
                    for n in names: self.assertEqual(sha(game / n), m['files'][n]['target_sha256'])
                    i.uninstall(game, payload)
                for n in names: self.assertEqual(sha(game / n), m['files'][n]['source_sha256'])
                self.assertEqual((game / 'save-sentinel').read_bytes(), b'NOT ACCESSED BY INSTALLER')
                self.assertEqual({p.name for p in game.iterdir()}, set(names) | {'save-sentinel'})

@unittest.skipUnless(os.environ.get('CB_EXE_DELTA_TEST') == '1', 'opt in with CB_EXE_DELTA_TEST=1')
class FrozenInstallerTests(unittest.TestCase):
    def test_frozen_both_variants(self):
        import subprocess
        exe = ROOT / 'dist/alpha0.1/CosmobreederYiffai-alpha0.1-setup.exe'
        base = ROOT / '.local/release-audit/delta-release'
        base.mkdir(parents=True, exist_ok=True)
        m = i.verify(ROOT / 'dist/alpha0.1/payload')
        def run(*args):
            result = subprocess.run([str(exe), *map(str, args)], capture_output=True)
            self.assertEqual(result.returncode, 0, repr(result.stderr))
            return result.stdout
        self.assertIn(b'verified', run('--verify-payload'))
        license_output = run('--licenses')
        for name in (b'fonts/OFL.txt', b'fonts/LICENSES/galmuri/LICENSE.txt', b'runtime/Python-LICENSE.txt', b'SIL OPEN FONT LICENSE'):
            self.assertIn(name, license_output)
        for nsfw in (False, True):
            with self.subTest(nsfw=nsfw), tempfile.TemporaryDirectory(dir=base) as tmp:
                game = Path(tmp)
                names = i.NAMES if nsfw else i.NAMES[:1]
                for n in names: shutil.copyfile(ROOT / 'backup' / n, game / n)
                (game / 'save-sentinel').write_bytes(b'UNCHANGED')
                self.assertIn(b'nsfw' if nsfw else b'vanilla', run('--game-dir', game, '--check'))
                run('--game-dir', game, '--install')
                for n in names: self.assertEqual(sha(game / n), m['files'][n]['target_sha256'])
                run('--game-dir', game, '--uninstall')
                for n in names: self.assertEqual(sha(game / n), m['files'][n]['source_sha256'])
                self.assertEqual((game / 'save-sentinel').read_bytes(), b'UNCHANGED')
                self.assertEqual({p.name for p in game.iterdir()}, set(names) | {'save-sentinel'})

@unittest.skipUnless(os.environ.get('CB_GUI_DELTA_TEST') == '1', 'opt in with CB_GUI_DELTA_TEST=1')
class GuiSmokeTests(unittest.TestCase):
    def test_gui_and_nested_license_viewer(self):
        import tkinter as tk
        from cosmobreeder_patch.__main__ import main
        def smoke(root):
            try:
                root.update()
                buttons = [w for w in root.winfo_children() if isinstance(w, tk.Button)]
                self.assertEqual(len(buttons), 5)
                buttons[-1].invoke()
                root.update()
                window = [w for w in root.winfo_children() if isinstance(w, tk.Toplevel)][0]
                text = [w for w in window.winfo_children() if isinstance(w, tk.Text)][0].get('1.0', 'end')
                self.assertIn('fonts/LICENSES/galmuri/LICENSE.txt', text)
                self.assertIn('SIL OPEN FONT LICENSE', text)
            finally:
                root.destroy()
        with patch.object(sys, 'argv', ['installer']), patch.object(sys, '_MEIPASS', str(ROOT / 'dist/alpha0.1'), create=True), patch.object(tk.Tk, 'mainloop', smoke):
            main()

if __name__ == '__main__': unittest.main()
