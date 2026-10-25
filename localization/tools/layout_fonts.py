"""Build/validate an isolated compact10 candidate; never register or replace classic.

API: build_compact_font(new_output_dir) -> manifest dict.
read_fnt(path)/parse_fnt(text) -> BitmapFont; validate_fnt(font, png, added_ids=())
checks structural/pixel invariants; validate_compact_font(output_dir) additionally
checks the manifest, local source identities, original metrics and copied pixels.

Only the existing default10 bitmap is copied (no rendering, scaling or download).
The existing license metadata describes its upstream 12px font, not a separately
verified 10px TTF. That metadata/notice is retained verbatim, not relabelled.
"""
from __future__ import annotations

from dataclasses import dataclass
from hashlib import sha256
from io import BytesIO
import json
from pathlib import Path
import re
from typing import Iterable
import zipfile

from PIL import Image

ROOT = Path(__file__).resolve().parents[2]
RUNTIME = ROOT / "localization/runtime"
ORIGINAL_JAR = ROOT / "backup/cosmobreeder-multi.jar"
PAGE_SIZE = 2048
CLASSIC_WIDTH = 512
ROLE = "compact10"
MANIFEST_FILENAME = "compact10.manifest.json"
GLYPH_FIELDS = (
    "id", "x", "y", "width", "height", "xoffset", "yoffset",
    "xadvance", "page", "chnl",
)
_ATTR = re.compile(r'(\w+)=("[^"\r\n]*"|[^\s]+)')


class FontValidationError(ValueError):
    """A font pair or its provenance failed a fail-closed candidate gate."""


@dataclass
class BitmapFont:
    info: dict
    common: dict
    pages: dict[int, str]
    glyphs: dict[int, dict[str, int]]
    kernings: tuple[dict[str, int], ...]
    char_lines: dict[int, str]


def _require(condition: bool, message: str) -> None:
    if not condition:
        raise FontValidationError(message)


def _attrs(body: str) -> dict:
    result = {}
    end = 0
    for match in _ATTR.finditer(body):
        _require(not body[end:match.start()].strip(), "malformed FNT attributes")
        key, value = match.groups()
        _require(key not in result, f"duplicate FNT attribute: {key}")
        if value.startswith('"'):
            value = value[1:-1]
        elif re.fullmatch(r"-?\d+", value):
            value = int(value)
        result[key] = value
        end = match.end()
    _require(not body[end:].strip(), "malformed FNT attributes")
    return result


def _integers(attrs: dict, fields: Iterable[str], label: str) -> None:
    for key in fields:
        _require(type(attrs.get(key)) is int, f"{label}: missing/integer field {key}")


def parse_fnt(text: str) -> BitmapFont:
    """Parse text BMFont without silently accepting duplicate IDs/counts/sections.

    This deliberately supports only the single-page unpacked channel-0 contract
    used by the project's candidate inputs; it is not a general BMFont loader.
    """
    info = common = None
    pages, glyphs, char_lines = {}, {}, {}
    counts = {}
    kernings = []
    seen_kerning_pairs = set()
    for raw in text.splitlines():
        line = raw.strip()
        if not line:
            continue
        tag, sep, body = line.partition(" ")
        _require(bool(sep), f"malformed FNT line: {line!r}")
        attrs = _attrs(body)
        if tag == "info":
            _require(info is None and common is None, "duplicate/out-of-order info")
            _integers(attrs, ("size",), "info")
            info = attrs
        elif tag == "common":
            _require(info is not None and common is None and not pages,
                     "duplicate/out-of-order common")
            _integers(attrs, ("lineHeight", "base", "scaleW", "scaleH", "pages", "packed"),
                      "common")
            common = attrs
        elif tag == "page":
            _require(common is not None and "chars" not in counts, "out-of-order page")
            _integers(attrs, ("id",), "page")
            page_id = attrs["id"]
            _require(page_id not in pages, f"duplicate page id: {page_id}")
            _require(isinstance(attrs.get("file"), str) and bool(attrs["file"]),
                     "page: missing file")
            pages[page_id] = attrs["file"]
        elif tag in ("chars", "kernings"):
            _require(tag not in counts, f"duplicate {tag} count")
            _integers(attrs, ("count",), tag)
            _require(attrs["count"] >= 0, f"negative {tag} count")
            if tag == "chars":
                _require(bool(pages) and "kernings" not in counts, "out-of-order chars")
            else:
                _require("chars" in counts, "kernings before chars")
            counts[tag] = attrs["count"]
        elif tag == "char":
            _require("chars" in counts and "kernings" not in counts,
                     "char outside chars section")
            _integers(attrs, GLYPH_FIELDS, "char")
            _require(set(attrs) == set(GLYPH_FIELDS), "unsupported glyph attributes")
            cid = attrs["id"]
            _require(cid not in glyphs, f"duplicate glyph id: {cid}")
            glyphs[cid] = attrs
            char_lines[cid] = raw
        elif tag == "kerning":
            _require("kernings" in counts, "kerning outside kernings section")
            _integers(attrs, ("first", "second", "amount"), "kerning")
            pair = (attrs["first"], attrs["second"])
            _require(pair not in seen_kerning_pairs, "duplicate kerning pair")
            seen_kerning_pairs.add(pair)
            kernings.append(attrs)
        else:
            raise FontValidationError(f"unsupported FNT section: {tag}")
    _require(info is not None and common is not None and "chars" in counts,
             "missing required FNT section")
    _require(counts["chars"] == len(glyphs), "chars count mismatch")
    _require(counts.get("kernings", 0) == len(kernings), "kernings count mismatch")
    font = BitmapFont(info, common, pages, glyphs, tuple(kernings), char_lines)
    _validate_structure(font)
    return font


def read_fnt(path: str | Path) -> BitmapFont:
    return parse_fnt(Path(path).read_text(encoding="utf-8"))


def _validate_structure(font: BitmapFont) -> None:
    common = font.common
    _require(common["pages"] == 1 and set(font.pages) == {0}, "expected one page id=0")
    _require(common["packed"] == 0, "packed channels are unsupported")
    _require(common["scaleW"] > 0 and common["scaleH"] > 0, "invalid page dimensions")
    _require(common["lineHeight"] > 0, "invalid lineHeight")
    for cid, glyph in font.glyphs.items():
        _integers(glyph, GLYPH_FIELDS, "char")
        _require(cid == glyph["id"], "glyph dictionary key/id mismatch")
        _require(0 <= cid <= 0x10FFFF and not 0xD800 <= cid <= 0xDFFF,
                 f"invalid Unicode glyph id: {cid}")
        _require(glyph["page"] == 0, f"glyph {cid}: invalid page")
        _require(glyph["chnl"] == 0, f"glyph {cid}: unsupported channel")
        _require(glyph["x"] >= 0 and glyph["y"] >= 0 and glyph["width"] >= 0
                 and glyph["height"] >= 0, f"glyph {cid}: negative PNG bounds")
        _require(glyph["x"] + glyph["width"] <= common["scaleW"]
                 and glyph["y"] + glyph["height"] <= common["scaleH"],
                 f"glyph {cid}: outside PNG bounds")
    for kerning in font.kernings:
        _require(kerning["first"] in font.glyphs and kerning["second"] in font.glyphs,
                 "kerning references missing glyph")


def _box(glyph: dict) -> tuple[int, int, int, int]:
    return (glyph["x"], glyph["y"], glyph["x"] + glyph["width"],
            glyph["y"] + glyph["height"])


def _rgba(data: bytes) -> Image.Image:
    with Image.open(BytesIO(data)) as image:
        _require(image.format == "PNG", "font page must be PNG")
        _require(image.mode == "RGBA", "font page must have RGBA channels")
        return image.copy()


def validate_fnt(font: BitmapFont, png: str | Path | Image.Image,
                 *, added_ids: Iterable[int] = ()) -> dict:
    """Check count (at parse), page/channel/bounds and EVERY added visible glyph.

    Added visible glyphs must be alpha-nonempty and advance >=10; whitespace is
    exempt. Source-provenance/pixel equality and non-overlap are checked by the
    stronger validate_compact_font gate below.
    """
    _validate_structure(font)
    image = png if isinstance(png, Image.Image) else _rgba(Path(png).read_bytes())
    _require(image.mode == "RGBA", "font page must have RGBA channels")
    _require(image.size == (font.common["scaleW"], font.common["scaleH"]),
             "PNG dimensions do not match FNT")
    added = set(added_ids)
    _require(added <= font.glyphs.keys(), "missing added glyph ids")
    for cid in sorted(added):
        if chr(cid).isspace():
            continue
        glyph = font.glyphs[cid]
        _require(glyph["xadvance"] >= 10, f"glyph {cid}: Chinese advance below 10")
        _require(glyph["width"] > 0 and glyph["height"] > 0,
                 f"glyph {cid}: empty visible glyph bounds")
        _require(image.crop(_box(glyph)).getchannel("A").getbbox() is not None,
                 f"glyph {cid}: empty visible glyph alpha")
    return {"glyph_count": len(font.glyphs), "added_glyph_count": len(added),
            "page_size": list(image.size)}


def charset_sha256(ids: Iterable[int]) -> str:
    """Hash sorted unique Unicode scalar IDs, each encoded as uint32 big endian."""
    return sha256(b"".join(cid.to_bytes(4, "big") for cid in sorted(set(ids)))).hexdigest()


def _identity(path: Path, data: bytes) -> dict:
    return {"path": path.relative_to(ROOT).as_posix(), "sha256": sha256(data).hexdigest()}


def _load_sources() -> dict:
    # Read each source once; all identities refer to precisely these snapshots.
    jar_data = ORIGINAL_JAR.read_bytes()
    with zipfile.ZipFile(BytesIO(jar_data)) as archive:
        _require(archive.namelist().count("classic.fnt") == 1,
                 "original JAR classic.fnt entry must be unique")
        classic_data = archive.read("classic.fnt")
    names = ("bbc2-10px.fnt", "bbc2-cjk-10.png", "classic-cjk.png",
             "font-license-metadata.json", "LICENSE-FusionPixel-OFL.txt", "NOTICE.txt")
    data = {name: (RUNTIME / name).read_bytes() for name in names}
    classic = parse_fnt(classic_data.decode("utf-8"))
    default = parse_fnt(data["bbc2-10px.fnt"].decode("utf-8"))
    classic_page = _rgba(data["classic-cjk.png"])
    default_page = _rgba(data["bbc2-cjk-10.png"])
    _require(len(classic.glyphs) == 193, "original classic must contain 193 glyphs")
    _require((classic.common["scaleW"], classic.common["scaleH"]) == (512, 512),
             "original classic page identity is not 512x512")
    _require(not classic.kernings, "unexpected original classic kernings")
    _require(classic_page.size == (PAGE_SIZE, PAGE_SIZE), "invalid classic source PNG size")
    _require(default.info["size"] == 10 and default.common["lineHeight"] == 14
             and default.common["base"] == 8, "default10 metrics identity mismatch")
    _require(default_page.size == (PAGE_SIZE, PAGE_SIZE), "invalid default10 PNG size")
    added = sorted(default.glyphs.keys() - classic.glyphs.keys())
    _require(bool(added), "default10 has no added glyphs")
    _require(all(cid > 127 for cid in added), "unexpected added ASCII glyph")
    validate_fnt(default, default_page, added_ids=added)
    validate_fnt(classic, classic_page.crop((0, 0, 512, 512)))
    # This is an existing bitmap-source contract, not a font-size label check.
    _require(all((default.glyphs[cid]["width"], default.glyphs[cid]["height"]) == (10, 10)
                 for cid in added if not chr(cid).isspace()),
             "default10 visible glyphs must retain real 10x10 source cells")
    metadata = json.loads(data["font-license-metadata.json"].decode("utf-8"))
    _require(metadata.get("bitmap_derivative_included") is True
             and metadata.get("full_license_text_bundled") is True,
             "missing bitmap/license metadata")
    _require(any("SIL Open Font License" in value
                 for value in metadata.get("name_table", {}).get("13", [])),
             "missing OFL metadata")
    _require(b"SIL OPEN FONT LICENSE Version 1.1" in data["LICENSE-FusionPixel-OFL.txt"],
             "missing full OFL license text")
    identities = {name: _identity(RUNTIME / name, value) for name, value in data.items()}
    identities["original_jar"] = _identity(ORIGINAL_JAR, jar_data)
    identities["original_classic_fnt"] = {
        "archive": ORIGINAL_JAR.relative_to(ROOT).as_posix(), "entry": "classic.fnt",
        "sha256": sha256(classic_data).hexdigest(), "glyph_count": 193,
    }
    return {"classic": classic, "default": default, "classic_page": classic_page,
            "default_page": default_page, "added": added, "data": data,
            "identities": identities, "metadata": metadata}


def _compose(sources: dict) -> tuple[str, Image.Image]:
    classic, default = sources["classic"], sources["default"]
    canvas = Image.new("RGBA", (PAGE_SIZE, PAGE_SIZE), (0, 0, 0, 0))
    # Keep the ENTIRE left strip, not the old 8px CJK glyphs at x>=512.
    canvas.paste(sources["classic_page"].crop((0, 0, CLASSIC_WIDTH, PAGE_SIZE)), (0, 0))
    info = re.sub(r'face="[^"]*"', 'face="Cosmo Compact 10"',
                  sources["data"]["bbc2-10px.fnt"].decode("utf-8").splitlines()[0])
    info = re.sub(r"\bunicode=\d+", "unicode=1", info)
    lines = [info,
             f"common lineHeight=14 base=8 scaleW={PAGE_SIZE} scaleH={PAGE_SIZE} pages=1 packed=0",
             'page id=0 file="compact10.png"',
             f"chars count={len(classic.glyphs) + len(sources['added'])}"]
    # Raw original char records retain ALL original metrics, even classic-only Latin.
    lines.extend(classic.char_lines[cid] for cid in classic.glyphs)
    x, y, row_height = CLASSIC_WIDTH, 0, 0
    for cid in sources["added"]:
        source = default.glyphs[cid]
        glyph = dict(source)
        width, height = glyph["width"], glyph["height"]
        if x + width > PAGE_SIZE:
            x, y, row_height = CLASSIC_WIDTH, y + row_height + 1, 0
        _require(y + height <= PAGE_SIZE, "compact10 page capacity exceeded")
        glyph.update(x=x, y=y)
        # No mask: retain source RGBA bytes exactly (do not apply alpha twice).
        canvas.paste(sources["default_page"].crop(_box(source)), (x, y))
        lines.append("char " + " ".join(f"{key}={glyph[key]}" for key in GLYPH_FIELDS))
        x += width + 1
        row_height = max(row_height, height)
    lines.append("kernings count=0")
    return "\n".join(lines) + "\n", canvas


def _validate_copies(font: BitmapFont, image: Image.Image, sources: dict) -> None:
    classic, default, added = sources["classic"], sources["default"], sources["added"]
    validate_fnt(font, image, added_ids=added)
    _require(font.info["size"] == 10 and font.info.get("face") == "Cosmo Compact 10"
             and font.common["lineHeight"] == 14 and font.common["base"] == 8,
             "compact10 role/baseline mismatch")
    _require(font.pages == {0: "compact10.png"}, "compact10 page filename mismatch")
    _require(not font.kernings, "unexpected compact10 kernings")
    _require(set(font.glyphs) == set(classic.glyphs) | set(added), "candidate charset mismatch")
    for cid, glyph in classic.glyphs.items():
        _require(font.glyphs[cid] == glyph, f"original classic glyph {cid} metrics changed")
    strip = (0, 0, CLASSIC_WIDTH, PAGE_SIZE)
    _require(image.crop(strip).tobytes() == sources["classic_page"].crop(strip).tobytes(),
             "original classic left strip pixels changed")
    # Occupancy check includes the reserved left strip and every added rectangle.
    occupied: dict[int, list[tuple[int, int]]] = {}
    for cid in added:
        glyph, source = font.glyphs[cid], default.glyphs[cid]
        _require(all(glyph[key] == source[key] for key in GLYPH_FIELDS if key not in ("x", "y")),
                 f"added glyph {cid} source metrics changed")
        _require(glyph["x"] >= CLASSIC_WIDTH, f"added glyph {cid} overlaps classic region")
        left, top, right, bottom = _box(glyph)
        if right > left:
            for row in range(top, bottom):
                intervals = occupied.setdefault(row, [])
                _require(all(right <= a or left >= b for a, b in intervals),
                         f"added glyph {cid} overlaps another glyph")
                intervals.append((left, right))
        _require(image.crop(_box(glyph)).tobytes()
                 == sources["default_page"].crop(_box(source)).tobytes(),
                 f"added glyph {cid} pixels differ from default10")


def _manifest(fnt_data: bytes, png_data: bytes, font: BitmapFont, sources: dict) -> dict:
    original_ids = sorted(sources["classic"].glyphs)
    added = sources["added"]
    return {
        "schema_version": 1, "role": ROLE, "status": "candidate",
        "global_classic_replacement": False, "registered_globally": False,
        "assets": {
            "fnt": {"file": "compact10.fnt", "sha256": sha256(fnt_data).hexdigest()},
            "png": {"file": "compact10.png", "sha256": sha256(png_data).hexdigest()},
        },
        "charset": {"encoding": "sorted-unique-unicode-scalars-u32be",
                    "sha256": charset_sha256(font.glyphs), "count": len(font.glyphs),
                    "ids": sorted(font.glyphs), "original_classic_ids": original_ids,
                    "original_classic_sha256": charset_sha256(original_ids),
                    "added_ids": added, "added_sha256": charset_sha256(added)},
        "metrics": {"cjk_size": 10, "minimum_visible_cjk_advance": 10,
                    "lineHeight": 14, "base": 8, "page_size": [PAGE_SIZE, PAGE_SIZE],
                    "original_classic_metrics": "unchanged",
                    "added_metrics": "default10 unchanged except atlas x/y",
                    "reserved_classic_rect": [0, 0, CLASSIC_WIDTH, PAGE_SIZE]},
        "sources": sources["identities"],
        "licenses": {
            "metadata": sources["metadata"],
            "metadata_scope": "Existing metadata describes upstream 12px font; candidate copies existing default10 bitmap only.",
            "cjk_license": "SIL Open Font License 1.1",
            "bundled_files": {name: sha256(sources["data"][name]).hexdigest() for name in
                              ("font-license-metadata.json", "LICENSE-FusionPixel-OFL.txt", "NOTICE.txt")},
            "original_glyphs": "Original game rightsholders' terms; OFL does not grant rights to original game assets.",
            "redistribution_clearance_claimed": False,
        },
        "transforms": {"rasterized": False, "rescaled": False, "downloaded": False,
                       "copied_existing_default10_glyphs": True},
    }


def build_compact_font(output_dir: str | Path) -> dict:
    """Create compact10.fnt/png + manifest/license files in a NEW directory.

    Existing directories/files/symlinks are refused, including an empty directory.
    No runtime asset, original game resource or global registration is written.
    The returned dict is also saved as compact10.manifest.json, written last.
    """
    output = Path(output_dir)
    if output.exists() or output.is_symlink():
        raise FileExistsError(f"refusing to overwrite output directory: {output}")
    sources = _load_sources()
    text, image = _compose(sources)
    font = parse_fnt(text)
    _validate_copies(font, image, sources)
    fnt_data = text.encode("utf-8")
    buffer = BytesIO()
    image.save(buffer, format="PNG")
    png_data = buffer.getvalue()
    manifest = _manifest(fnt_data, png_data, font, sources)
    output.mkdir(parents=True, exist_ok=False)
    files = {"compact10.fnt": fnt_data, "compact10.png": png_data}
    for name in manifest["licenses"]["bundled_files"]:
        files[name] = sources["data"][name]
    files[MANIFEST_FILENAME] = (json.dumps(manifest, ensure_ascii=False, indent=2) + "\n").encode("utf-8")
    for name, content in files.items():
        with (output / name).open("xb") as stream:
            stream.write(content)
    return manifest


def validate_compact_font(output_dir: str | Path) -> dict:
    """Recheck pair SHA, full manifest, local provenance, ALL metrics and pixels.

    Invoke this gate immediately before consuming the candidate. A mismatched
    source snapshot or a missing/edited license file also invalidates the pair.
    Missing files propagate OSError; invalid fonts/manifests raise ValueError.
    """
    output = Path(output_dir)
    manifest = json.loads((output / MANIFEST_FILENAME).read_text(encoding="utf-8"))
    fnt_data = (output / "compact10.fnt").read_bytes()
    png_data = (output / "compact10.png").read_bytes()
    font = parse_fnt(fnt_data.decode("utf-8"))
    image = _rgba(png_data)
    sources = _load_sources()
    expected = _manifest(fnt_data, png_data, font, sources)
    _require(manifest == expected, "manifest/hash/provenance mismatch")
    for name, digest in expected["licenses"]["bundled_files"].items():
        _require(sha256((output / name).read_bytes()).hexdigest() == digest,
                 f"bundled license identity mismatch: {name}")
    _validate_copies(font, image, sources)
    return manifest
