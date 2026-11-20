"""Regression: all.ds (datadf/1 & datadm/1) soft-break encoding.

The game's PRG.afF (Scala FastParse CubeDSParser) rejects U+2028 with a
Parsed.Failure, which breaks ALL dialogue (raw keys shown). tl_tool.py build now
writes the parser-safe sentinel U+2502 instead of U+2028 into datadf/1 & datadm/1,
and DialogueWrap.story()/radio() restore U+2028 before layout. This test pins the
built payload to that contract and proves the encoding is a lossless, reversible
soft-break transform relative to the TSV source.
"""
import sys
import unittest
import zipfile
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
sys.path.insert(0, str(ROOT / "tools"))
sys.path.insert(0, str(ROOT / "tools" / "lib"))

from codec import decrypt_file  # noqa: E402

SOFT_BREAK = "\u2028"
SOFT_BREAK_VIS = "\u23CE"
SENTINEL = "\u2502"
ARCHIVES = ("cosmobreeder-multi.jar", "patch.pak")
DS_ENTRIES = ("datadf/1", "datadm/1")


def _payload() -> Path:
    return ROOT / "payload"


def _tsv_soft_break_counts() -> dict:
    """arch/entry -> number of authoring soft breaks recorded in the TSV chunks."""
    from tl_tool import _read_tsv, unescape_tsv, SOFT_BREAK as TB
    counts = {}
    for tsv in sorted((ROOT / "tl_work" / "chunks" / "dialogue").glob("*.tsv")):
        for parts in _read_tsv(tsv, 8):
            _seq, arch, entry, _scene, _line, _prefix, _src, tgt_s = parts
            if not entry.startswith(DS_ENTRIES):
                continue
            counts[(arch, entry)] = counts.get((arch, entry), 0) + unescape_tsv(tgt_s).count(TB)
    return counts


class DsSoftBreakTests(unittest.TestCase):
    def setUp(self):
        self.payload = _payload()
        if not (self.payload / "cosmobreeder-multi.jar").is_file():
            self.skipTest("payload not built")

    def test_constant_matches_runtime(self):
        # Guard: the build-side sentinel and the runtime decoder must be the same char.
        from tl_tool import DS_SOFT_BREAK_SENTINEL
        self.assertEqual(DS_SOFT_BREAK_SENTINEL, SENTINEL)
        wrap = (ROOT / "src" / "java" / "runtime" / "PRG" / "DialogueWrap.java").read_text("utf-8")
        self.assertIn("\\u2502", wrap)

    def test_no_parser_rejected_breaks_and_reversible(self):
        expected = _tsv_soft_break_counts()
        checked_entries = 0
        for archive in ARCHIVES:
            with zipfile.ZipFile(self.payload / archive) as z:
                for entry in DS_ENTRIES:
                    raw = decrypt_file(z.read(entry)).decode("utf-8")
                    # (a) No character that PRG.afF rejects.
                    for bad in (SOFT_BREAK, "\u2029", "\u0085"):
                        self.assertNotIn(bad, raw, f"{archive} {entry} still contains U+{ord(bad):04X}")
                    # (b) Sentinel is the ONLY soft-break carrier.
                    self.assertNotIn(SOFT_BREAK_VIS, raw, f"{archive} {entry} leaked literal {SOFT_BREAK_VIS}")
                    sentinel_count = raw.count(SENTINEL)
                    self.assertEqual(
                        sentinel_count,
                        expected.get((archive, entry), 0),
                        f"{archive} {entry} sentinel count != TSV soft-break count",
                    )
                    # (c) Reversible: restoring sentinel -> U+2028 recovers exactly the
                    #     authoring breaks and leaves no sentinel behind.
                    decoded = raw.replace(SENTINEL, SOFT_BREAK)
                    self.assertNotIn(SENTINEL, decoded, f"{archive} {entry} decode left sentinel")
                    self.assertEqual(
                        decoded.count(SOFT_BREAK), sentinel_count,
                        f"{archive} {entry} decode did not restore every soft break",
                    )
                    checked_entries += 1
        self.assertEqual(checked_entries, len(ARCHIVES) * len(DS_ENTRIES))

    def test_reconstruct_matches_payload(self):
        # verify-readback equivalence for the two all.ds entries.
        import tl_tool
        expected_entries, _ = tl_tool.reconstruct_text_entries(ROOT / "tl_work")
        for archive in ARCHIVES:
            with zipfile.ZipFile(self.payload / archive) as z:
                for entry in DS_ENTRIES:
                    want = expected_entries[archive].get(entry)
                    if want is None:
                        continue
                    got = decrypt_file(z.read(entry))
                    self.assertEqual(got, want, f"{archive} {entry} payload != TSV reconstruction")


if __name__ == "__main__":
    unittest.main()
