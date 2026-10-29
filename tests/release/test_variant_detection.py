"""Release contract: source-verified SFW/official NSFW, not filename guessing."""
import unittest
import test_delta_release as fixtures
from cosmobreeder_patch import installer as engine


def load_tests(loader, tests, pattern):
    return unittest.TestSuite(VariantDetectionTests(name) for name in VariantDetectionTests.__dict__ if name.startswith('test_'))


class VariantDetectionTests(fixtures.ReleaseTests):
    def test_original_sfw_is_read_only(self):
        self.populate(nsfw=False)
        before = self.snapshot()
        self.assertEqual(engine.detect(self.game, engine.verify(self.payload)), 'vanilla')
        self.assertEqual(before, self.snapshot())

    def test_official_nsfw_is_read_only(self):
        self.populate(nsfw=True)
        before = self.snapshot()
        self.assertEqual(engine.detect(self.game, engine.verify(self.payload)), 'nsfw')
        self.assertEqual(before, self.snapshot())

    def test_arbitrary_pak_is_not_official_nsfw(self):
        self.populate()
        (self.game / engine.NAMES[1]).write_bytes(b'not the official patch')
        before = self.snapshot()
        with self.assertRaises(ValueError):
            engine.detect(self.game, engine.verify(self.payload))
        self.assertEqual(before, self.snapshot())

    def test_unknown_jar_refused_with_or_without_pak(self):
        self.populate()
        (self.game / engine.NAMES[0]).write_bytes(b'old localization or unknown version')
        for nsfw in (True, False):
            if not nsfw:
                (self.game / engine.NAMES[1]).unlink()
            before = self.snapshot()
            with self.assertRaises(ValueError):
                engine.install(self.game, self.payload)
            self.assertEqual(before, self.snapshot())


if __name__ == '__main__':
    unittest.main()
