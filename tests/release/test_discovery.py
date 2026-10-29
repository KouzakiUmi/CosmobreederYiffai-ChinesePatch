import sys
from pathlib import Path
import tempfile
import unittest
from unittest.mock import patch

sys.path.insert(0, str(Path(__file__).resolve().parents[2] / 'src'))
from cosmobreeder_patch import discovery


class DiscoveryTests(unittest.TestCase):
    def setUp(self):
        self.tmp = tempfile.TemporaryDirectory()
        self.root = Path(self.tmp.name).resolve()
        self.steamapps = self.root / 'Steam' / 'steamapps'
        self.common = self.steamapps / 'common'
        self.common.mkdir(parents=True)

    def tearDown(self):
        self.tmp.cleanup()

    def game(self, name, pak=False):
        path = self.common / name
        path.mkdir()
        (path / 'cosmobreeder-multi.jar').write_bytes(b'discovery hint only')
        if pak:
            (path / 'patch.pak').write_bytes(b'not assumed official')
        return path

    def find(self, nearby=()):
        with patch.object(discovery, '_steam_roots', return_value=[self.steamapps]), patch.object(discovery, '_nearby_dirs', return_value=list(nearby)):
            return discovery.find_game()

    def test_finds_sfw_and_nsfw_without_modifying(self):
        sfw = self.game('Cosmobreeder Yiffai')
        nsfw = self.game('Yiffai other copy', pak=True)
        before = {p: p.read_bytes() for p in self.root.rglob('*') if p.is_file()}
        self.assertEqual(set(self.find()), {sfw, nsfw})
        self.assertEqual(before, {p: p.read_bytes() for p in self.root.rglob('*') if p.is_file()})

    def test_ignores_wrong_name_missing_jar_and_nested_game(self):
        self.game('Unrelated game')
        empty = self.common / 'Cosmobreeder empty'
        empty.mkdir()
        (empty / 'nested').mkdir()
        (empty / 'nested' / 'cosmobreeder-multi.jar').write_bytes(b'no recursive scan')
        self.assertEqual(self.find(), [])

    def test_nearby_and_steam_candidates_deduplicated(self):
        game = self.game('Cosmobreeder')
        self.assertEqual(self.find([game, game]), [game])

    def test_non_steam_nearby_game(self):
        game = self.root / 'Portable game'
        game.mkdir()
        (game / 'cosmobreeder-multi.jar').write_bytes(b'portable')
        self.assertEqual(self.find([game]), [game])

    def test_secondary_library_vdf_and_duplicate(self):
        library = self.root / 'Secondary Library'
        escaped = str(library).replace('\\', '\\\\')
        (self.steamapps / 'libraryfolders.vdf').write_text('"libraryfolders" { "1" { "path" "' + escaped + '" } }', encoding='utf-8')
        self.assertEqual(discovery._library_roots([self.steamapps, self.steamapps]), [self.steamapps, library / 'steamapps'])

    def test_missing_library_configuration(self):
        self.assertEqual(discovery._library_roots([self.steamapps]), [self.steamapps])

    def test_frozen_executable_not_meipass(self):
        exe = self.root / 'Installer' / 'setup.exe'
        with patch.object(sys, 'frozen', True, create=True), patch.object(sys, 'executable', str(exe)), patch.object(sys, '_MEIPASS', str(self.root / 'unpacked'), create=True):
            paths = discovery._nearby_dirs()
        self.assertIn(exe.parent, paths)
        self.assertIn(exe.parent.parent, paths)
        self.assertNotIn(self.root / 'unpacked', paths)


if __name__ == '__main__':
    unittest.main()
