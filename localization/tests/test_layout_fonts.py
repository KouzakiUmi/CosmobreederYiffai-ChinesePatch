"""unittest gates for the isolated compact10 font pair (no runtime writes).

Run from repository root:
  PYTHONDONTWRITEBYTECODE=1 PYTHONIOENCODING=utf-8 python -B -m unittest discover \
      -s localization/tests -p test_layout_fonts.py -v
All on-disk fixtures live under localization/work/layout-fonts-test/.
"""
from copy import deepcopy
from hashlib import sha256
import json
from pathlib import Path
import re
import shutil
import sys
import tempfile
import unittest
from unittest.mock import patch
import zipfile

from PIL import Image

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "tools"))
import layout_fonts as fonts

TEST_ROOT = fonts.ROOT / "localization/work/layout-fonts-test"


def tiny_font(char=None, *, count=1):
    char = char or "char id=20013 x=0 y=0 width=10 height=10 xoffset=0 yoffset=-1 xadvance=10 page=0 chnl=0"
    return ("info face=\"test\" size=10\n"
            "common lineHeight=14 base=8 scaleW=20 scaleH=20 pages=1 packed=0\n"
            "page id=0 file=\"test.png\"\n"
            f"chars count={count}\n{char}\nkernings count=0\n")


class ParserAndPixelGateTests(unittest.TestCase):
    def test_parses_metrics_without_losing_offsets(self):
        font = fonts.parse_fnt(tiny_font())
        self.assertEqual(font.glyphs[20013]["yoffset"], -1)
        self.assertEqual(font.common["lineHeight"], 14)

    def test_rejects_count_mismatch(self):
        with self.assertRaisesRegex(fonts.FontValidationError, "count mismatch"):
            fonts.parse_fnt(tiny_font(count=2))

    def test_rejects_duplicate_glyph_even_with_matching_count(self):
        text = tiny_font()
        line = next(line for line in text.splitlines() if line.startswith("char "))
        text = text.replace("chars count=1", "chars count=2").replace("kernings count=0", line + "\nkernings count=0")
        with self.assertRaisesRegex(fonts.FontValidationError, "duplicate glyph"):
            fonts.parse_fnt(text)

    def test_rejects_invalid_page_and_channel(self):
        for old, new in (("page=0", "page=1"), ("chnl=0", "chnl=15"),
                         ("packed=0", "packed=1"), ("pages=1", "pages=2")):
            with self.subTest(new=new), self.assertRaises(fonts.FontValidationError):
                fonts.parse_fnt(tiny_font().replace(old, new))

    def test_rejects_duplicate_page_and_attributes(self):
        for text in (tiny_font().replace("chars count=1", 'page id=0 file="other.png"\nchars count=1'),
                     tiny_font().replace("xadvance=10", "xadvance=10 xadvance=10")):
            with self.assertRaisesRegex(fonts.FontValidationError, "duplicate"):
                fonts.parse_fnt(text)

    def test_rejects_out_of_bounds_and_invalid_scalar(self):
        for old, new in (("x=0", "x=-1"), ("y=0", "y=15"),
                         ("width=10", "width=-1"), ("id=20013", "id=55296"),
                         ("id=20013", "id=1114112")):
            with self.subTest(new=new), self.assertRaises(fonts.FontValidationError):
                fonts.parse_fnt(tiny_font().replace(old, new))

    def test_rejects_char_after_kernings(self):
        text = tiny_font().replace("chars count=1\n", "chars count=1\nkernings count=0\n")
        with self.assertRaisesRegex(fonts.FontValidationError, "outside chars"):
            fonts.parse_fnt(text)

    def test_rejects_kerning_count_and_unknown_references(self):
        for text in (tiny_font().replace("kernings count=0", "kernings count=1"),
                     tiny_font().replace("kernings count=0", "kernings count=1\nkerning first=1 second=20013 amount=1")):
            with self.assertRaises(fonts.FontValidationError):
                fonts.parse_fnt(text)

    def test_rejects_missing_and_malformed_sections(self):
        for text in (tiny_font().replace("chars count=1\n", ""),
                     tiny_font().replace("xadvance=10", "xadvance=oops"),
                     tiny_font() + "unexpected value=1\n",
                     tiny_font().replace("xadvance=10", "BROKEN xadvance=10")):
            with self.assertRaises(fonts.FontValidationError):
                fonts.parse_fnt(text)

    def test_png_dimensions_and_alpha_not_rgb_are_checked(self):
        font = fonts.parse_fnt(tiny_font())
        # Transparent white RGB is NOT visible ink; opaque black IS visible.
        for image, message in ((Image.new("RGBA", (19, 20)), "dimensions"),
                               (Image.new("RGBA", (20, 20), (255, 255, 255, 0)), "alpha"),
                               (Image.new("RGB", (20, 20)), "RGBA")):
            with self.subTest(message=message), self.assertRaisesRegex(fonts.FontValidationError, message):
                fonts.validate_fnt(font, image, added_ids=[20013])
        fonts.validate_fnt(font, Image.new("RGBA", (20, 20), (0, 0, 0, 255)), added_ids=[20013])

    def test_visible_advance_and_zero_cell_are_rejected(self):
        image = Image.new("RGBA", (20, 20), (255, 255, 255, 255))
        for old, new in (("xadvance=10", "xadvance=8"), ("width=10", "width=0")):
            with self.subTest(new=new), self.assertRaises(fonts.FontValidationError):
                fonts.validate_fnt(fonts.parse_fnt(tiny_font().replace(old, new)), image,
                                   added_ids=[20013])

    def test_whitespace_is_exempt_from_visible_advance_and_ink(self):
        text = tiny_font().replace("id=20013", "id=12288").replace("width=10", "width=0").replace("height=10", "height=0").replace("xadvance=10", "xadvance=0")
        fonts.validate_fnt(fonts.parse_fnt(text), Image.new("RGBA", (20, 20)), added_ids=[12288])

    def test_charset_hash_has_canonical_encoding(self):
        expected = sha256(b"\x00\x00\x00A\x00\x00N-").hexdigest()
        self.assertEqual(fonts.charset_sha256([20013, 65, 20013]), expected)


class CompactFontTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        TEST_ROOT.mkdir(parents=True, exist_ok=True)
        cls.temporary = tempfile.TemporaryDirectory(prefix="unittest-", dir=TEST_ROOT)
        cls.root = Path(cls.temporary.name)
        cls.baseline = cls.root / "candidate"
        cls.source_hashes = {str(path): sha256(path.read_bytes()).hexdigest()
                             for path in (fonts.ORIGINAL_JAR, *fonts.RUNTIME.iterdir()) if path.is_file()}
        cls.manifest = fonts.build_compact_font(cls.baseline)
        cls.text = (cls.baseline / "compact10.fnt").read_text("utf-8")
        cls.font = fonts.parse_fnt(cls.text)
        cls.sources = fonts._load_sources()

    @classmethod
    def tearDownClass(cls):
        try:
            for name, digest in cls.source_hashes.items():
                if sha256(Path(name).read_bytes()).hexdigest() != digest:
                    raise AssertionError(f"source changed during tests: {name}")
        finally:
            cls.temporary.cleanup()

    def fixture(self):
        output = self.root / self.id().split(".")[-1]
        shutil.copytree(self.baseline, output)
        return output

    def refresh_asset_hash(self, output, kind):
        manifest_path = output / fonts.MANIFEST_FILENAME
        manifest = json.loads(manifest_path.read_text("utf-8"))
        asset = manifest["assets"][kind]
        asset["sha256"] = sha256((output / asset["file"]).read_bytes()).hexdigest()
        manifest_path.write_text(json.dumps(manifest), encoding="utf-8")

    def change_glyph(self, output, cid, **values):
        path = output / "compact10.fnt"
        text = path.read_text("utf-8")
        line = fonts.parse_fnt(text).char_lines[cid]
        changed = line
        for key, value in values.items():
            changed = re.sub(rf"\b{key}=-?\d+", f"{key}={value}", changed)
        path.write_text(text.replace(line, changed), encoding="utf-8")
        self.refresh_asset_hash(output, "fnt")

    def test_build_and_validate_complete_manifest(self):
        self.assertEqual(fonts.validate_compact_font(self.baseline), self.manifest)
        self.assertEqual(self.manifest["charset"]["count"], 2504)
        self.assertEqual(len(self.manifest["charset"]["added_ids"]), 2311)
        self.assertEqual(self.manifest["role"], "compact10")
        self.assertFalse(self.manifest["global_classic_replacement"])
        self.assertFalse(self.manifest["registered_globally"])
        self.assertEqual(self.font.pages, {0: "compact10.png"})
        self.assertEqual(self.font.info["size"], 10)
        self.assertEqual(self.font.common["lineHeight"], 14)
        for asset in self.manifest["assets"].values():
            self.assertEqual(sha256((self.baseline / asset["file"]).read_bytes()).hexdigest(), asset["sha256"])

    def test_all_193_original_records_and_classic_only_latin_unchanged(self):
        original = self.sources["classic"]
        self.assertEqual(len(original.glyphs), 193)
        with zipfile.ZipFile(fonts.ORIGINAL_JAR) as archive:
            self.assertEqual(fonts.parse_fnt(archive.read("classic.fnt").decode()).glyphs, original.glyphs)
        for cid, glyph in original.glyphs.items():
            self.assertEqual(self.font.glyphs[cid], glyph)
            self.assertEqual(self.font.char_lines[cid], original.char_lines[cid])
        classic_only = set(original.glyphs) - set(self.sources["default"].glyphs)
        self.assertTrue(classic_only)
        for cid in classic_only:
            self.assertEqual(self.font.glyphs[cid]["xadvance"], original.glyphs[cid]["xadvance"])
        self.assertIn(ord("é"), classic_only)

    def test_every_pixel_and_added_metric_is_copied_without_rescaling(self):
        with Image.open(self.baseline / "compact10.png") as image:
            strip = (0, 0, 512, 2048)
            self.assertEqual(image.crop(strip).tobytes(), self.sources["classic_page"].crop(strip).tobytes())
            for cid in self.sources["added"]:
                new, old = self.font.glyphs[cid], self.sources["default"].glyphs[cid]
                self.assertGreaterEqual(new["x"], 512)
                for field in fonts.GLYPH_FIELDS:
                    if field not in ("x", "y"):
                        self.assertEqual(new[field], old[field])
                self.assertEqual(image.crop(fonts._box(new)).tobytes(),
                                 self.sources["default_page"].crop(fonts._box(old)).tobytes())
            fonts.validate_fnt(self.font, image, added_ids=self.sources["added"])

    def test_manifest_binds_original_sources_charset_and_license(self):
        manifest = self.manifest
        self.assertEqual(manifest["charset"]["sha256"], fonts.charset_sha256(self.font.glyphs))
        for key, identity in manifest["sources"].items():
            if "path" in identity:
                self.assertEqual(sha256((fonts.ROOT / identity["path"]).read_bytes()).hexdigest(), identity["sha256"])
        for name, digest in manifest["licenses"]["bundled_files"].items():
            self.assertEqual((self.baseline / name).read_bytes(), (fonts.RUNTIME / name).read_bytes())
            self.assertEqual(sha256((self.baseline / name).read_bytes()).hexdigest(), digest)
        self.assertEqual(manifest["licenses"]["metadata"]["source_font_filename"],
                         "fusion-pixel-12px-monospaced-zh_hans.ttf")
        self.assertFalse(manifest["licenses"]["redistribution_clearance_claimed"])

    def test_reproducible_pair_in_two_new_directories(self):
        output = self.root / "second-candidate"
        self.assertEqual(fonts.build_compact_font(output), self.manifest)
        for name in ("compact10.fnt", "compact10.png", fonts.MANIFEST_FILENAME):
            self.assertEqual((output / name).read_bytes(), (self.baseline / name).read_bytes())

    def test_refuses_all_existing_output_paths_without_writes(self):
        empty = self.root / "empty"
        empty.mkdir()
        regular_file = self.root / "file"
        regular_file.write_bytes(b"untouched")
        for path in (self.baseline, empty, regular_file):
            with self.subTest(path=path.name), self.assertRaises(FileExistsError):
                fonts.build_compact_font(path)
        self.assertEqual(list(empty.iterdir()), [])
        self.assertEqual(regular_file.read_bytes(), b"untouched")
        self.assertEqual(fonts.validate_compact_font(self.baseline), self.manifest)

    def test_rejects_unpaired_8px_png(self):
        output = self.fixture()
        (output / "compact10.png").write_bytes((fonts.RUNTIME / "bbc2-cjk-8.png").read_bytes())
        with self.assertRaisesRegex(fonts.FontValidationError, "manifest/hash"):
            fonts.validate_compact_font(output)

    def test_rejects_missing_page_file(self):
        output = self.fixture()
        # Rename is unnecessary: a missing-file fixture uses an uncreated directory.
        missing = output / "missing"
        missing.mkdir()
        (missing / fonts.MANIFEST_FILENAME).write_bytes((output / fonts.MANIFEST_FILENAME).read_bytes())
        (missing / "compact10.fnt").write_bytes((output / "compact10.fnt").read_bytes())
        with self.assertRaises(FileNotFoundError):
            fonts.validate_compact_font(missing)

    def test_rejects_manifest_role_charset_or_provenance_edits(self):
        output = self.fixture()
        path = output / fonts.MANIFEST_FILENAME
        for field in ("role", "charset", "sources", "licenses"):
            manifest = deepcopy(self.manifest)
            manifest[field] = "edited"
            path.write_text(json.dumps(manifest), encoding="utf-8")
            with self.subTest(field=field), self.assertRaisesRegex(fonts.FontValidationError, "manifest/hash"):
                fonts.validate_compact_font(output)

    def test_rejects_bundled_license_tampering(self):
        output = self.fixture()
        (output / "NOTICE.txt").write_text("different notice", encoding="utf-8")
        with self.assertRaisesRegex(fonts.FontValidationError, "license identity"):
            fonts.validate_compact_font(output)

    def test_rejects_changed_local_source_identity(self):
        sources = dict(self.sources)
        sources["identities"] = deepcopy(sources["identities"])
        sources["identities"]["original_jar"]["sha256"] = "0" * 64
        with patch.object(fonts, "_load_sources", return_value=sources):
            with self.assertRaisesRegex(fonts.FontValidationError, "provenance"):
                fonts.validate_compact_font(self.baseline)

    def test_rejects_original_latin_metric_change_even_with_updated_hash(self):
        output = self.fixture()
        self.change_glyph(output, ord("é"), xadvance=10)
        with self.assertRaisesRegex(fonts.FontValidationError, "original classic glyph"):
            fonts.validate_compact_font(output)

    def test_rejects_added_offset_change_even_with_updated_hash(self):
        output = self.fixture()
        self.change_glyph(output, ord("中"), yoffset=1)
        with self.assertRaisesRegex(fonts.FontValidationError, "source metrics"):
            fonts.validate_compact_font(output)

    def test_rejects_added_advance_8_even_with_updated_hash(self):
        output = self.fixture()
        self.change_glyph(output, ord("中"), xadvance=8)
        with self.assertRaisesRegex(fonts.FontValidationError, "advance below 10"):
            fonts.validate_compact_font(output)

    def test_checks_last_glyph_not_only_first_sample(self):
        output = self.fixture()
        cid = self.sources["added"][-1]
        path = output / "compact10.png"
        with Image.open(path) as image:
            changed = image.copy()
        changed.paste((255, 255, 255, 0), fonts._box(self.font.glyphs[cid]))
        changed.save(path)
        self.refresh_asset_hash(output, "png")
        with self.assertRaisesRegex(fonts.FontValidationError, "empty visible glyph alpha"):
            fonts.validate_compact_font(output)

    def test_rejects_added_overlap_even_with_updated_hash(self):
        output = self.fixture()
        first, last = self.sources["added"][0], self.sources["added"][-1]
        glyph = self.font.glyphs[first]
        self.change_glyph(output, last, x=glyph["x"], y=glyph["y"])
        with self.assertRaisesRegex(fonts.FontValidationError, "overlaps another glyph"):
            fonts.validate_compact_font(output)

    def test_rejects_added_glyph_in_reserved_classic_strip(self):
        output = self.fixture()
        self.change_glyph(output, self.sources["added"][0], x=0)
        # The glyph's target area can be empty; either ink or reserved-region gate fails.
        with self.assertRaises(fonts.FontValidationError):
            fonts.validate_compact_font(output)

    def test_rejects_wrong_page_filename_even_with_updated_hash(self):
        output = self.fixture()
        path = output / "compact10.fnt"
        path.write_text(self.text.replace('file="compact10.png"', 'file="../classic.png"'), encoding="utf-8")
        self.refresh_asset_hash(output, "fnt")
        with self.assertRaisesRegex(fonts.FontValidationError, "page filename"):
            fonts.validate_compact_font(output)

    def test_rejects_changed_classic_pixel_even_with_updated_hash(self):
        output = self.fixture()
        path = output / "compact10.png"
        with Image.open(path) as image:
            changed = image.copy()
        changed.putpixel((0, 500), (100, 20, 30, 255))
        changed.save(path)
        self.refresh_asset_hash(output, "png")
        with self.assertRaisesRegex(fonts.FontValidationError, "left strip pixels"):
            fonts.validate_compact_font(output)

    def test_rejects_nonempty_but_wrong_added_pixels_even_with_updated_hash(self):
        output = self.fixture()
        path = output / "compact10.png"
        with Image.open(path) as image:
            changed = image.copy()
        changed.paste((0, 0, 0, 255), fonts._box(self.font.glyphs[ord("中")]))
        changed.save(path)
        self.refresh_asset_hash(output, "png")
        with self.assertRaisesRegex(fonts.FontValidationError, "pixels differ"):
            fonts.validate_compact_font(output)

    def test_no_original_jar_or_runtime_files_written(self):
        for name, digest in self.source_hashes.items():
            self.assertEqual(sha256(Path(name).read_bytes()).hexdigest(), digest)


if __name__ == "__main__":
    unittest.main(verbosity=2)
