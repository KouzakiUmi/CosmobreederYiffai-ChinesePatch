"""Opt-in real Tk button smoke tests with mocked discovery; never scans a game."""
import os
from pathlib import Path
import sys
import unittest
from unittest.mock import patch

sys.path.insert(0, str(Path(__file__).resolve().parents[2] / 'src'))
from cosmobreeder_patch import gui


@unittest.skipUnless(os.environ.get('CB_GUI_DISCOVERY_TEST') == '1', 'opt in with CB_GUI_DISCOVERY_TEST=1')
class DirectoryGuiTests(unittest.TestCase):
    def exercise(self, candidates):
        real_tk = gui.tk.Tk
        observed = {}
        def make_root():
            root = real_tk()
            def widgets(parent):
                for child in parent.winfo_children():
                    yield child
                    yield from widgets(child)
            def click():
                button = next(w for w in widgets(root) if isinstance(w, gui.ttk.Button) and w.cget('text') == '自动查找')
                button.invoke()
                root.after(100, inspect)
            def inspect():
                # Wait for queue-drained UI, not merely worker completion.
                labels = [w for w in widgets(root) if isinstance(w, gui.ttk.Label)]
                statuses = [root.getvar(w.cget('textvariable')) for w in labels if w.cget('textvariable')]
                if any('没自动找到' in str(s) or '源 SHA-256 匹配' in str(s) for s in statuses):
                    observed['status'] = statuses
                    entry = next(w for w in widgets(root) if isinstance(w, gui.ttk.Entry))
                    observed['selected'] = entry.get()
                    root.destroy()
                else:
                    root.after(100, inspect)
            root.after(100, click)
            root.after(5000, root.destroy)
            return root
        with patch.object(gui.tk, 'Tk', side_effect=make_root), patch.object(gui.discovery, 'find_game', return_value=candidates) as find, patch.object(gui.engine, 'verify', return_value={'version': 'alpha0.1'}), patch.object(gui.engine, 'detect', return_value='vanilla') as detect, patch.object(gui.engine, 'install') as install:
            gui.run(Path('unused-payload'), lambda: 'license')
        self.assertIn('status', observed, 'GUI timed out')
        find.assert_called_once()
        install.assert_not_called()
        if candidates:
            self.assertEqual(observed['selected'], str(candidates[0]))
            detect.assert_called_once()
        else:
            self.assertEqual(observed['selected'], '')
            detect.assert_not_called()

    def test_auto_find_selects_and_checks_without_install(self):
        self.exercise([Path('D:/Synthetic Game')])

    def test_not_found_keeps_manual_selection_available(self):
        self.exercise([])
