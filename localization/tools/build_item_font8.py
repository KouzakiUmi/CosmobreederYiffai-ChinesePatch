"""Shipping variant: --audit-existing validates existing classic8 without writes.

The local Chinese-only ItemFont8 patch consumes that existing role, creates no
font/texture and packages no new assets. This does not newly certify its source
TTF identity. --source-zip/--output and --validate are OPTIONAL RESEARCH-ONLY
native BDF comparison tooling, not a shipping font replacement. That pinned
2026.10.16 source is real8, never a relabelled/scaled default10 bitmap.
"""
from __future__ import annotations
import argparse
from hashlib import sha256
from io import BytesIO
import json
from pathlib import Path
import re
import zipfile
from PIL import Image
from layout_fonts import parse_fnt

ROOT = Path(__file__).resolve().parents[2]
SOURCE_URL = "https://github.com/TakWolf/fusion-pixel-font/releases/download/2026.10.16/fusion-pixel-font-8px-monospaced-bdf-v2026.10.16.zip"
SOURCE_ZIP_SHA256 = "a090b06a7275a9f392c9f19d780cc9336275e57c79d3b6a4e54a3716032fdf64"
SOURCE_ENTRY = "fusion-pixel-8px-monospaced-zh_hans.bdf"
SOURCE_BDF_SHA256 = "44a2d82b3dd782b505fa2297f10d8fd65499f9476d47b0331a22a133419b0ec3"
ROLE = "item8"
ASSET_INVENTORY = ("item8.fnt", "item8.png", "item8.manifest.json", "item8.coverage.json", "OFL.txt", "NOTICE.txt")


def require(value, message):
    if not value:
        raise ValueError(message)


def digest(data):
    return sha256(data).hexdigest()


def rows(path):
    return [json.loads(line) for line in path.read_text(encoding="utf-8").splitlines() if line.strip()]


def corpus():
    """SH appends .name/.desc/numbered .desc to XK's item key; SM -> Tc consumes it.

    Conservative superset: every non-ui/non-nav dictionary .name key, every
    corresponding .descN, all equip/consumable keys (including no-name fallbacks),
    noItemDesc, plus dynamic decimal suffix/upgrade '+' and fallback punctuation.
    Include source, translation AND draft so deployment selection cannot hide chars.
    """
    loc = ROOT / "localization"
    resources = {r["logical_path"]: r for r in rows(loc / "catalog/resources.jsonl")}
    dictionary_resource = resources["datav/dictionary.json"]
    scripts_resource = resources["datay/scripts_pack.json"]
    dictionary = json.loads((loc / dictionary_resource["blob_path"]).read_text(encoding="utf-8"))
    scripts = json.loads((loc / scripts_resource["blob_path"]).read_text(encoding="utf-8"))
    dictionary.update(scripts.get("patchDictionary", {}))
    keys = {k[:-5] for k in dictionary if k.endswith(".name") and not k.startswith(("ui.", "navmap."))}
    keys.update(scripts["equipInfo"])
    keys.update(scripts["consumableInfo"])
    selected = {k for k in dictionary if any(k == item + ".name" or re.fullmatch(re.escape(item) + r"\.desc\d*", k) for item in keys)}
    selected.add("ui.items.noItemDesc")
    occurrences = [r for r in rows(loc / "catalog/occurrences.jsonl") if r.get("json_key") in selected]
    units = {r["id"]: r for r in rows(loc / "catalog/units.jsonl")}
    translations = {r["id"]: r for r in rows(loc / "translations/zh-CN.jsonl")}
    records = [{"key": k, "kind": "dictionary-source", "text": dictionary[k]} for k in sorted(selected) if k in dictionary]
    for occurrence in occurrences:
        uid = occurrence["unit_id"]
        records.append({"key": occurrence["json_key"], "kind": "catalog-source", "unit_id": uid, "text": units[uid]["source"]})
        for kind in ("translation", "draft"):
            text = translations.get(uid, {}).get(kind)
            if text:
                records.append({"key": occurrence["json_key"], "kind": kind, "unit_id": uid, "text": text})
    records.append({"key": "$dynamic", "kind": "runtime-format", "text": "+? 0123456789" + "".join(sorted(keys))})
    ids = {ord(c) for r in records for c in r["text"] if c not in "|\r\n\t"}
    require(len(keys) >= 100 and len(records) >= 250, "item corpus unexpectedly incomplete")
    evidence = []
    for path in (loc / "catalog/resources.jsonl", loc / dictionary_resource["blob_path"], loc / scripts_resource["blob_path"],
                 loc / "catalog/units.jsonl", loc / "catalog/occurrences.jsonl", loc / "translations/zh-CN.jsonl"):
        evidence.append({"path": path.relative_to(ROOT).as_posix(), "sha256": digest(path.read_bytes())})
    return {"item_keys": sorted(keys), "dictionary_keys": sorted(selected), "records": records,
            "required_ids": sorted(ids), "sources": evidence,
            "consumer": "SH: XK item key + .name/.descN; SL -> SM -> Tc; Le equipment '+' retained"}


def parse_bdf(data):
    text = data.decode("utf-8")
    require('\nSIZE 8 75 75\n' in text and '\nPIXEL_SIZE 8\n' in text and '\nFONTBOUNDINGBOX 8 8 0 -1\n' in text,
            "not the pinned native 8px BDF")
    glyphs = {}
    for block in text.split("STARTCHAR ")[1:]:
        lines = block.splitlines()
        cp = int(next(l for l in lines if l.startswith("ENCODING ")).split()[1])
        if not 0 <= cp <= 65535 or 0xD800 <= cp <= 0xDFFF:
            continue
        dw = list(map(int, next(l for l in lines if l.startswith("DWIDTH ")).split()[1:]))
        w, h, xo, yo = map(int, next(l for l in lines if l.startswith("BBX ")).split()[1:])
        require(0 <= w <= 8 and 0 <= h <= 8 and 0 < dw[0] <= 8 and dw[1] == 0,
                f"native glyph exceeds 8px contract: U+{cp:04X}")
        bitmap = lines[lines.index("BITMAP") + 1:lines.index("ENDCHAR")]
        require(len(bitmap) == h and cp not in glyphs, "BDF duplicate/count mismatch")
        pixels = Image.new("RGBA", (w, h), (255, 255, 255, 0))
        for y, value in enumerate(bitmap):
            bits = int(value, 16)
            nbits = len(value) * 4
            for x in range(w):
                if bits & (1 << (nbits - 1 - x)):
                    pixels.putpixel((x, y), (255, 255, 255, 255))
        glyphs[cp] = (w, h, xo, 7 - yo - h, dw[0], pixels)
    require(len(glyphs) > 20000, "incomplete native BDF")
    return glyphs


def shared_source():
    runtime = ROOT / "localization/runtime"
    fnt = (runtime / "bbc2-10px.fnt").read_bytes()
    png = (runtime / "bbc2-cjk-10.png").read_bytes()
    font = parse_fnt(fnt.decode("utf-8"))
    image = Image.open(BytesIO(png)).convert("RGBA")
    require(image.size == (2048, 2048), "shared default10 page dimensions")
    require(max(g["y"] + g["height"] for g in font.glyphs.values()) <= 256,
            "default10 overlaps item8 reserved strip")
    require(image.crop((0, 256, 2048, 512)).getchannel("A").getbbox() is None,
            "shared page item8 strip is not empty")
    return fnt, png, image


def compose(source, required_ids):
    native = parse_bdf(source)
    ids = set(required_ids) | set(range(32, 127))
    require(ids <= native.keys(), "native8 source does not cover all item glyphs")
    glyphs = {cp: native[cp] for cp in sorted(ids)}
    size = 2048
    _, _, canvas = shared_source()
    lines = ['info face="Cosmo Item Native 8" size=8 bold=0 italic=0 charset="" unicode=1 stretchH=100 smooth=0 aa=1 padding=0,0,0,0 spacing=0,0',
             f'common lineHeight=8 base=7 scaleW={size} scaleH={size} pages=1 packed=0',
             'page id=0 file="item8.png"', f'chars count={len(glyphs)}']
    # 9px cells keep every native BDF pixel and separate neighboring glyphs.
    for index, (cp, value) in enumerate(sorted(glyphs.items())):
        w, h, xo, yo, advance, pixels = value
        x, y = (index % 227) * 9, 256 + (index // 227) * 9
        require(y + h <= 512, "native atlas reserved strip capacity")
        canvas.paste(pixels, (x, y))
        lines.append(f'char id={cp} x={x} y={y} width={w} height={h} xoffset={xo} yoffset={yo} xadvance={advance} page=0 chnl=0')
    lines.append('kernings count=0')
    data = ("\n".join(lines) + "\n").encode("utf-8")
    stream = BytesIO(); canvas.save(stream, format="PNG")
    return data, stream.getvalue()


def validate_pair(fnt_data, png_data, coverage):
    font = parse_fnt(fnt_data.decode("utf-8"))
    require(font.info["size"] == 8 and font.common["lineHeight"] == 8 and font.common["base"] == 7,
            "item8 metrics identity")
    require(font.pages == {0: "item8.png"} and not font.kernings, "item8 page/kerning identity")
    image = Image.open(BytesIO(png_data)); require(image.mode == "RGBA" and image.size == (2048, 2048), "item8 PNG identity")
    old_fnt, old_png, original = shared_source()
    for box in ((0, 0, 2048, 256), (0, 512, 2048, 2048)):
        require(image.crop(box).tobytes() == original.crop(box).tobytes(),
                "shared default10 pixels changed outside item8 strip")
    require(set(image.crop((0, 256, 2048, 512)).getchannel("A").tobytes()) <= {0, 255},
            "native item8 must be unscaled binary pixels")
    missing = set(coverage["required_ids"]) - font.glyphs.keys()
    require(not missing, "native8 missing actual item corpus: " + " ".join(f"U+{c:04X}" for c in sorted(missing)))
    for cp, g in font.glyphs.items():
        require(0 <= g["width"] <= 8 and 0 <= g["height"] <= 8 and 0 < g["xadvance"] <= 8,
                f"item8 glyph contract U+{cp:04X}")
        require(g["xoffset"] >= 0 and g["xoffset"] + g["width"] <= g["xadvance"] and
                g["yoffset"] >= 0 and g["yoffset"] + g["height"] <= 8, "glyph exceeds integer cell")
        if cp in coverage["required_ids"] and not chr(cp).isspace():
            box = (g["x"], g["y"], g["x"] + g["width"], g["y"] + g["height"])
            require(image.crop(box).getchannel("A").getbbox() is not None, f"empty item glyph U+{cp:04X}")
    return font


def build_item_font8(source_zip, output_dir):
    output = Path(output_dir)
    require(not output.exists(), "refuse existing output directory")
    raw = Path(source_zip).read_bytes()
    require(digest(raw) == SOURCE_ZIP_SHA256, "official source ZIP SHA mismatch")
    archive = zipfile.ZipFile(BytesIO(raw))
    source = archive.read(SOURCE_ENTRY)
    if SOURCE_BDF_SHA256:
        require(digest(source) == SOURCE_BDF_SHA256, "source BDF SHA mismatch")
    coverage = corpus()
    fnt, png = compose(source, coverage["required_ids"])
    font = validate_pair(fnt, png, coverage)
    licenses = {name: archive.read(name) for name in archive.namelist() if name == "OFL.txt" or name.startswith("LICENSES/")}
    require(b"SIL OPEN FONT LICENSE Version 1.1" in licenses["OFL.txt"], "full OFL missing")
    notice = ("Cosmo Item Native 8 is a bitmap derivative of Fusion Pixel 8px Mono zh_Hans 2026.10.16.\n"
              "Copyright (c) 2022, TakWolf (https://takwolf.com).\n"
              "SIL Open Font License 1.1; full upstream OFL and component notices are bundled.\n"
              "Upstream: https://github.com/TakWolf/fusion-pixel-font\n"
              "Native BDF pixels copied 1:1; no scaling/rasterization of the existing default10 font.\n").encode("utf-8")
    files = {"item8.fnt": fnt, "item8.png": png, "item8.coverage.json": (json.dumps(coverage, ensure_ascii=False, indent=2) + "\n").encode("utf-8"),
             "NOTICE.txt": notice, **licenses}
    manifest = {"schema": 1, "role": ROLE, "native_pixel_size": 8,
                "source": {"url": SOURCE_URL, "zip_sha256": SOURCE_ZIP_SHA256, "entry": SOURCE_ENTRY, "bdf_sha256": digest(source),
                           "copyright": "Copyright (c) 2022, TakWolf (https://takwolf.com)", "license": "OFL-1.1"},
                "transforms": {"copied_native_bdf_bits": True, "rescaled": False,
                               "shared_default10_texture": True, "default10_glyphs_unchanged": True,
                               "reserved_item8_strip": [0, 256, 2048, 512]},
                "shared_page_sources": {"bbc2-10px.fnt": digest(shared_source()[0]),
                                        "bbc2-cjk-10.png": digest(shared_source()[1])},
                "packaging": {"item8.fnt": "item8/item8.fnt", "item8.png": "replace built bbc2 region pixels only; not a new texture",
                              "bitmap_font_ctor": "arp(apQ.e.b(item8/item8.fnt), Yq.i(bbc2), false)"},
                "glyph_count": len(font.glyphs), "required_item_glyph_count": len(coverage["required_ids"]), "missing_ids": [],
                "inventory": {name: digest(data) for name, data in sorted(files.items())}}
    output.mkdir(parents=True)
    for name, data in files.items():
        path = output / name; path.parent.mkdir(parents=True, exist_ok=True); path.write_bytes(data)
    (output / "item8.manifest.json").write_text(json.dumps(manifest, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    return manifest


def validate_item_font8(output_dir, source_zip=None):
    output = Path(output_dir)
    manifest = json.loads((output / "item8.manifest.json").read_text(encoding="utf-8"))
    require(manifest["source"]["zip_sha256"] == SOURCE_ZIP_SHA256 and manifest["role"] == ROLE, "source/role pin")
    for name, sha in manifest["inventory"].items():
        require(digest((output / name).read_bytes()) == sha, "asset/notice SHA mismatch: " + name)
    coverage = json.loads((output / "item8.coverage.json").read_text(encoding="utf-8"))
    require(coverage == corpus(), "actual item corpus changed; rebuild item8")
    validate_pair((output / "item8.fnt").read_bytes(), (output / "item8.png").read_bytes(), coverage)
    if source_zip is not None:
        raw = Path(source_zip).read_bytes(); require(digest(raw) == SOURCE_ZIP_SHA256, "source zip pin")
        source = zipfile.ZipFile(BytesIO(raw)).read(SOURCE_ENTRY)
        require(digest(source) == manifest["source"]["bdf_sha256"], "BDF pin")
        fnt, png = compose(source, coverage["required_ids"])
        require(fnt == (output / "item8.fnt").read_bytes() and png == (output / "item8.png").read_bytes(), "not exact native BDF pixels")
    return manifest


def audit_existing_classic():
    """Shipping minimal variant: audit existing classic8, create/replace NOTHING.

    Existing metadata pins a 12px mono source; make-classic-cjk.py references an
    external 8px proportional source without a local SHA. This audit proves the
    installed bitmap metrics/pixels/coverage, NOT a newly verified native source.
    Native-BDF build above is research-only, not required or packaged by patch.
    """
    runtime = ROOT / "localization/runtime"
    coverage = corpus()
    fnt_data = (runtime / "classic.fnt").read_bytes()
    png_data = (runtime / "classic-cjk.png").read_bytes()
    require(digest(fnt_data) == "a456bb96b944b2c443868b5ea02d2b458744eb795e161d6835a2d490a67c2510", "existing classic FNT identity")
    font = parse_fnt(fnt_data.decode("utf-8"))
    image = Image.open(BytesIO(png_data)).convert("RGBA")
    require(font.info["size"] == 8 and font.common["lineHeight"] == 8 and font.common["base"] == 8, "existing classic8 metrics")
    require(image.size == (font.common["scaleW"], font.common["scaleH"]), "classic PNG/FNT dimensions")
    missing = sorted(set(coverage["required_ids"]) - font.glyphs.keys())
    require(not missing, "missing existing classic8 item characters: " + str(missing))
    padded_ascii = []
    for cp in coverage["required_ids"]:
        g = font.glyphs[cp]
        require(0 < g["xadvance"] <= 8, f"classic advance exceeds8 U+{cp:04X}")
        if cp > 127:
            require(0 <= g["width"] <= 8 and 0 <= g["height"] <= 8, f"CJK cell exceeds8 U+{cp:04X}")
        box = (g["x"], g["y"], g["x"] + g["width"], g["y"] + g["height"])
        ink = image.crop(box).getchannel("A").getbbox()
        if not chr(cp).isspace():
            require(ink is not None, f"empty actual item glyph U+{cp:04X}")
        if cp <= 127 and (g["width"] > 8 or g["height"] > 8):
            padded_ascii.append(cp)
            require(ink is None or (ink[2] - ink[0] <= 8 and ink[3] - ink[1] <= 8), "padded Latin visible ink exceeds8")
    name_records = [r for r in coverage["records"] if r["key"].endswith(".name")]
    name_widths = [(sum(font.glyphs[ord(c)]["xadvance"] for c in r["text"]), r) for r in name_records]
    require(all(width <= 72 for width, _ in name_widths), "name exceeds original single72px line")
    chinese_descriptions = []
    original_ascii_overflows = []
    for r in coverage["records"]:
        if not (re.search(r"\.desc\d*$", r["key"]) or r["key"] == "ui.items.noItemDesc"):
            continue
        line_count = 0
        for line in r["text"].replace("|", "\n").splitlines() or [""]:
            line_count += 1
            width = 0
            for c in line:
                next_width = font.glyphs[ord(c)]["xadvance"]
                if width + next_width > 112:
                    line_count += 1
                    width = 0
                width += next_width
        if any(0x2e80 <= ord(c) <= 0x9fff for c in r["text"]):
            require(line_count <= 2, "Chinese description exceeds original 112px/two8px lines: " + r["key"])
            chinese_descriptions.append(r)
        elif line_count > 2:
            original_ascii_overflows.append({"key": r["key"], "kind": r["kind"], "lines_if_reflowed": line_count})
    return {"variant": "existing-classic8-local-chinese-only", "new_asset_inventory": [],
            "existing_assets": {name: digest((runtime / name).read_bytes()) for name in
                                ("classic.fnt", "classic-cjk.png", "bbc2-10px.fnt", "bbc2-cjk-10.png", "font-license-metadata.json", "LICENSE-FusionPixel-OFL.txt", "NOTICE.txt")},
            "coverage": coverage, "missing_ids": missing, "required_chars": len(coverage["required_ids"]),
            "all_name_records": len(name_records), "maximum_name_width": max(width for width, _ in name_widths),
            "chinese_description_records": len(chinese_descriptions), "chinese_description_overflow": [],
            "padded_original_ascii_quad_ids": padded_ascii, "padded_ascii_visible_ink_maximum": [8, 8],
            "original_ascii_overflows_not_changed": original_ascii_overflows,
            "source_identity_claim": "Existing bitmap8 verified only; no claim of newly verified native 8px TTF/BDF source.",
            "native_bdf_research_only": {"source_url": SOURCE_URL, "zip_sha256": SOURCE_ZIP_SHA256, "bdf_sha256": SOURCE_BDF_SHA256},
            "game_or_GL_or_save_tested": False}


if __name__ == "__main__":
    p = argparse.ArgumentParser(description=__doc__)
    p.add_argument("--source-zip", type=Path)
    p.add_argument("--output", type=Path)
    p.add_argument("--validate", type=Path)
    p.add_argument("--audit-existing", action="store_true", help="read-only full existing classic8 corpus/PNG/FNT gate (shipping variant)")
    args = p.parse_args()
    if args.audit_existing:
        audit = audit_existing_classic()
        print(json.dumps({k: v for k, v in audit.items() if k != "coverage"}, ensure_ascii=False, indent=2))
        raise SystemExit(0)
    if args.validate:
        result = validate_item_font8(args.validate, args.source_zip)
    else:
        p.error("--source-zip and --output required") if not args.source_zip or not args.output else None
        result = build_item_font8(args.source_zip, args.output)
    print(json.dumps({k: result[k] for k in ("role", "glyph_count", "required_item_glyph_count", "source")}, ensure_ascii=False, indent=2))
