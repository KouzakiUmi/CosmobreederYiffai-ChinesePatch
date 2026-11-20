# -*- coding: utf-8 -*-
"""Cosmobreeder Yiffai 简体中文补丁：导出 / 构建 / 状态 / 读回核验统一工具。

对齐 WoC-ChinesePatch 工作流：
  tl_work/
    template/              冻结的原版明文骨架（由 export 生成，不手改）
    chunks/
      dialogue/*.tsv       对白脚本（jar_datadf, jar_datadm, pak_datadf, pak_datadm）
      vsn/*.tsv            演出字幕脚本（jar_vsn, pak_vsn）
      ui/*.tsv             字典与任务日志（jar_datav, pak_datav, jar_datay）

常用命令：
  python tools/tl_tool.py export [--target <build_dir>] [--force]
  python tools/tl_tool.py build  [--output payload]
  python tools/tl_tool.py status
  python tools/tl_tool.py verify-readback [--target payload]
"""
from __future__ import annotations

import argparse
from hashlib import sha256
from io import BytesIO
import json
import os
from pathlib import Path
import re
import shutil
import subprocess
import sys
import zipfile

from PIL import Image

ROOT = Path(__file__).resolve().parents[1]
LIB = ROOT / "tools" / "lib"
sys.path.insert(0, str(LIB))

from codec import decrypt_file, encrypt_file  # noqa: E402
from editorial_repairs import _json_tokens, _line_role, _safe_string, EditorialRepairError  # noqa: E402
from output_paths import check_outputs, workspace_output  # noqa: E402
from projectlib import parse_atlas  # noqa: E402
import optimized_fonts  # noqa: E402
import optimized_images  # noqa: E402

ARCHIVES = ("cosmobreeder-multi.jar", "patch.pak")
ARCHIVE_TAG = {"cosmobreeder-multi.jar": "jar", "patch.pak": "pak"}
TAG_ARCHIVE = {tag: name for name, tag in ARCHIVE_TAG.items()}
CHUNK_NAMES = {
    'dialogue': {f'{tag}_{kind}.tsv' for tag in TAG_ARCHIVE for kind in ('datadf', 'datadm')},
    'vsn': {f'{tag}_vsn.tsv' for tag in TAG_ARCHIVE},
    'ui': {'jar_datav.tsv', 'jar_datay.tsv', 'pak_datav.tsv'},
}
EXPORTS = [
    "--add-exports", "java.base/jdk.internal.org.objectweb.asm=ALL-UNNAMED",
    "--add-exports", "java.base/jdk.internal.org.objectweb.asm.tree=ALL-UNNAMED",
]
LICENSE8 = (
    "boutique-bitmap-7x7/OFL.txt",
    "galmuri/LICENSE.txt",
    "misaki/misaki.txt",
    "miseki-bitmap/LICENSE.txt",
)

SOFT_BREAK = "\u2028"
SOFT_BREAK_VIS = "⏎"
# datadf/1 and datadm/1 are the plaintext of all.ds, parsed at runtime by PRG.afF
# (the Scala FastParse CubeDSParser). Its dialogue rule rejects U+2028 with a
# Parsed.Failure. We keep U+2028 as the authoring soft-break in the TSV source but
# encode it to this parser-safe sentinel on disk; DialogueWrap.story()/radio()
# restore U+2028 before layout. U+2502 (BOX DRAWINGS LIGHT VERTICAL) is accepted by
# the real dialogue rule, does not occur in any current text, and is never rendered
# because it is decoded before layout.
DS_SOFT_BREAK_SENTINEL = "\u2502"
RUNTIME_MARKERS = re.compile(
    r'@[A-Za-z][A-Za-z0-9_]*|\$\{[^{}]+\}|\{[^{}\r\n]+\}'
    r'|%(?:[1-9]\d*\$)?(?:[-+#0]*\d*(?:\.\d+)?)?[sdifouxXeEgGc](?![A-Za-z])|</>|\|'
)


def check_runtime_markers(seq: str, source: str, target: str) -> None:
    if RUNTIME_MARKERS.findall(source) != RUNTIME_MARKERS.findall(target):
        raise ValueError(f'{seq}: 运行时占位符或分隔符发生变化')


def check_target_value(seq: str, source: str, target: str, kind: str) -> None:
    try:
        _safe_string(target, json_value=kind == 'ui', line_row=kind == 'dialogue')
    except EditorialRepairError as error:
        raise ValueError(f'{seq}: 译文不能加入新的脚本行或控制字符') from error
    check_runtime_markers(seq, source, target)
    if kind == 'ui' and re.findall(r'[|\r\n]', source) != re.findall(r'[|\r\n]', target):
        raise ValueError(f'{seq}: 界面分段和换行的顺序发生变化')


def _sha(data: bytes) -> str:
    return sha256(data).hexdigest()


def _file_sha(path: Path) -> str:
    return _sha(path.read_bytes())


def escape_tsv(s: str) -> str:
    """Lossless single-line TSV cell encoding."""
    return (
        s.replace("\\", "\\\\")
        .replace("\t", "\\t")
        .replace("\r", "\\r")
        .replace("\n", "\\n")
        .replace(SOFT_BREAK, SOFT_BREAK_VIS)
    )


def unescape_tsv(s: str) -> str:
    """Exact inverse of escape_tsv."""
    out = []
    i = 0
    n = len(s)
    while i < n:
        ch = s[i]
        if ch == SOFT_BREAK_VIS:
            out.append(SOFT_BREAK)
            i += 1
        elif ch == "\\" and i + 1 < n:
            nxt = s[i + 1]
            if nxt == "\\":
                out.append("\\")
                i += 2
            elif nxt == "t":
                out.append("\t")
                i += 2
            elif nxt == "r":
                out.append("\r")
                i += 2
            elif nxt == "n":
                out.append("\n")
                i += 2
            else:
                out.append(ch)
                i += 1
        else:
            out.append(ch)
            i += 1
    return "".join(out)


def _split_lines_lf(text: str) -> list[str]:
    """Split strictly on LF (never on U+2028!) while remembering trailing CR."""
    return text.split("\n")


def _strip_cr(line: str) -> tuple[str, str]:
    if line.endswith("\r"):
        return line[:-1], "\r"
    return line, ""


def _vsn_scene_map(z: zipfile.ZipFile) -> dict[str, str]:
    """Map 'vsn/<N>' -> logical scene name (e.g. 'Area0/Intro')."""
    if "vsn/0" not in z.namelist():
        return {}
    index = json.loads(decrypt_file(z.read("vsn/0")))
    out = {}
    for logical, idx in index.items():
        if isinstance(logical, str) and logical.endswith("/script.vsn"):
            scene = logical.strip("/").rsplit("/", 1)[0]
            out[f"vsn/{idx}"] = scene
    return out


def _is_vsn_script_entry(name: str) -> bool:
    if not name.startswith("vsn/"):
        return False
    tail = name.split("/", 1)[1]
    if not tail.isdigit():
        return False
    idx = int(tail)
    return idx > 0 and (idx - 5) % 6 == 0


def _is_translatable_datay_pointer(ptr: str) -> bool:
    if ptr.startswith("/patchDictionary/"):
        return True
    if ptr.startswith("/missionLog/"):
        leaf = ptr.rsplit("/", 1)[-1]
        return leaf in ("header", "locationName", "subject", "text")
    if ptr.startswith("/shops/"):
        leaf = ptr.rsplit("/", 1)[-1]
        return leaf == "displayName"
    return False


def _pointer_str(path_tuple: tuple[str, ...]) -> str:
    return "/" + "/".join(p.replace("~", "~0").replace("/", "~1") for p in path_tuple)


def _is_ui_field(entry: str, path: tuple[str, ...], value: object) -> bool:
    if not isinstance(value, str):
        return False
    return bool(value) if entry == 'datav/1' else _is_translatable_datay_pointer(_pointer_str(path))


def _write_tsv(path: Path, header_comment: str, columns: list[str], rows: list[list[str]]):
    path.parent.mkdir(parents=True, exist_ok=True)
    lines = [f"# {header_comment}", "# " + "\t".join(columns)]
    for r in rows:
        lines.append("\t".join(r))
    path.write_text("\n".join(lines) + "\n", encoding="utf-8-sig", newline="\n")


def _read_tsv(path: Path, expected_cols: int) -> list[list[str]]:
    rows = []
    for lineno, raw in enumerate(path.read_text(encoding="utf-8-sig").splitlines(), 1):
        if not raw.strip() or raw.startswith("#"):
            continue
        parts = raw.split("\t")
        if len(parts) != expected_cols:
            raise ValueError(f"{path}:{lineno}: 期望 {expected_cols} 列，实际 {len(parts)} 列")
        rows.append(parts)
    return rows


# ---------------------------------------------------------------------------
# Export
# ---------------------------------------------------------------------------

def cmd_export(args):
    orig_dir = (ROOT / args.originals).resolve()
    tgt_dir = (ROOT / args.target).resolve()
    tl_dir = workspace_output(ROOT, args.tl_dir, exact=('tl_work',), parents=('build',))
    if tl_dir != ROOT / 'tl_work' and tl_dir.exists():
        raise FileExistsError('隔离导出需要新的 build/ 子目录')
    if any(p.is_relative_to(tl_dir) or tl_dir.is_relative_to(p) for p in (orig_dir, tgt_dir)):
        raise ValueError('导出目录不能与原版或目标归档目录重叠')

    for a in ARCHIVES:
        if not (orig_dir / a).is_file():
            raise FileNotFoundError(f"缺少原版归档: {orig_dir / a}")
        if not (tgt_dir / a).is_file():
            raise FileNotFoundError(f"缺少目标归档: {tgt_dir / a}")

    chunks_dir = tl_dir / "chunks"
    tpl_dir = tl_dir / "template"
    check_outputs(tl_dir, ('chunks', 'template'))
    if (chunks_dir.exists() or tpl_dir.exists()) and not args.force:
        raise FileExistsError("tl_work/chunks 或 template 已存在；如需重导出请加 --force")

    if chunks_dir.exists():
        shutil.rmtree(chunks_dir)
    if tpl_dir.exists():
        shutil.rmtree(tpl_dir)

    tpl_meta = {"originals": {}, "target": {}, "entries": {}}

    for arch in ARCHIVES:
        tag = ARCHIVE_TAG[arch]
        tpl_meta["originals"][arch] = _file_sha(orig_dir / arch)
        tpl_meta["target"][arch] = _file_sha(tgt_dir / arch)

        with zipfile.ZipFile(orig_dir / arch) as z_orig, zipfile.ZipFile(tgt_dir / arch) as z_tgt:
            vsn_scenes = _vsn_scene_map(z_orig)

            # 1) Dialogue: datadf/1, datadm/1
            for entry in ("datadf/1", "datadm/1"):
                raw_orig = decrypt_file(z_orig.read(entry))
                raw_tgt = decrypt_file(z_tgt.read(entry))
                tpl_path = tpl_dir / tag / entry
                tpl_path.parent.mkdir(parents=True, exist_ok=True)
                tpl_path.write_bytes(raw_orig)
                tpl_meta["entries"][f"{tag}/{entry}"] = {"sha256": _sha(raw_orig), "bytes": len(raw_orig)}

                lines_orig = _split_lines_lf(raw_orig.decode("utf-8"))
                lines_tgt = _split_lines_lf(raw_tgt.decode("utf-8"))
                if len(lines_orig) != len(lines_tgt):
                    raise ValueError(f"{arch} {entry} 行数不一致: {len(lines_orig)} vs {len(lines_tgt)}")

                rows = []
                cur_scene = ""
                seq_prefix = f"{tag.upper()}-{'DF' if entry.startswith('datadf') else 'DM'}"
                seq_num = 0
                for lineno, (lo, lt) in enumerate(zip(lines_orig, lines_tgt), 1):
                    co, _ = _strip_cr(lo)
                    ct, _ = _strip_cr(lt)
                    stripped = co.strip()
                    if stripped.startswith("<") and stripped.endswith(">") and len(stripped) > 2:
                        cur_scene = stripped[1:-1]
                        continue
                    role = _line_role(co, "ds")
                    if role is None:
                        if co != ct:
                            raise ValueError(f"{arch} {entry}:{lineno} 非台词行发生改动: {co!r} -> {ct!r}")
                        continue
                    prefix, src_body = role
                    if ct == "":
                        tgt_body = ""
                    elif ct.strip() == "":
                        tgt_body = "__RAW__:" + ct
                    else:
                        role_t = _line_role(ct, "ds")
                        if role_t is None or role_t[0] != prefix:
                            raise ValueError(f"{arch} {entry}:{lineno} 目标前缀漂移: {prefix!r} vs {ct!r}")
                        tgt_body = role_t[1]
                        if entry.startswith(("datadf/", "datadm/")):
                            # Reverse of the build-time soft-break encoding so a re-export
                            # round-trips the on-disk sentinel back to the U+2028 authoring mark.
                            tgt_body = tgt_body.replace(DS_SOFT_BREAK_SENTINEL, SOFT_BREAK)
                    seq_num += 1
                    rows.append([
                        f"{seq_prefix}-{seq_num:04d}",
                        arch,
                        entry,
                        cur_scene,
                        str(lineno),
                        escape_tsv(prefix),
                        escape_tsv(src_body),
                        escape_tsv(tgt_body),
                    ])

                out_tsv = chunks_dir / "dialogue" / f"{tag}_{entry.split('/')[0]}.tsv"
                _write_tsv(
                    out_tsv,
                    f"{arch} {entry} 对白分块（只改最后一列 target；软断行 U+2028 记作 {SOFT_BREAK_VIS}；空 target 表示合句空尾行）",
                    ["seq", "archive", "entry", "scene", "line", "prefix", "source", "target"],
                    rows,
                )

            # 2) VSN scripts
            vsn_rows = []
            vsn_seq = 0
            vsn_entries = sorted(
                [n for n in z_orig.namelist() if _is_vsn_script_entry(n)],
                key=lambda x: int(x.split("/")[1]),
            )
            for entry in vsn_entries:
                raw_orig = decrypt_file(z_orig.read(entry))
                raw_tgt = decrypt_file(z_tgt.read(entry))
                tpl_path = tpl_dir / tag / entry
                tpl_path.parent.mkdir(parents=True, exist_ok=True)
                tpl_path.write_bytes(raw_orig)
                tpl_meta["entries"][f"{tag}/{entry}"] = {"sha256": _sha(raw_orig), "bytes": len(raw_orig)}

                lines_orig = _split_lines_lf(raw_orig.decode("utf-8"))
                lines_tgt = _split_lines_lf(raw_tgt.decode("utf-8"))
                if len(lines_orig) != len(lines_tgt):
                    raise ValueError(f"{arch} {entry} 行数不一致")
                scene = vsn_scenes.get(entry, entry)
                for lineno, (lo, lt) in enumerate(zip(lines_orig, lines_tgt), 1):
                    co, _ = _strip_cr(lo)
                    ct, _ = _strip_cr(lt)
                    role = _line_role(co, "vsn")
                    if role is None:
                        if co != ct:
                            raise ValueError(f"{arch} {entry}:{lineno} 非字幕行发生改动: {co!r} -> {ct!r}")
                        continue
                    prefix, src_body = role
                    if ct == "":
                        tgt_body = ""
                    elif ct.strip() == "":
                        tgt_body = "__RAW__:" + ct
                    else:
                        role_t = _line_role(ct, "vsn")
                        if role_t is None or role_t[0] != prefix:
                            raise ValueError(f"{arch} {entry}:{lineno} VSN前缀漂移: {prefix!r} vs {ct!r}")
                        tgt_body = role_t[1]
                    vsn_seq += 1
                    vsn_rows.append([
                        f"{tag.upper()}-VSN-{vsn_seq:04d}",
                        arch,
                        entry,
                        scene,
                        str(lineno),
                        escape_tsv(prefix),
                        escape_tsv(src_body),
                        escape_tsv(tgt_body),
                    ])

            _write_tsv(
                chunks_dir / "vsn" / f"{tag}_vsn.tsv",
                f"{arch} VSN 演出字幕分块（只改最后一列 target；注意 VSN 词法不接受 {SOFT_BREAK_VIS}）",
                ["seq", "archive", "entry", "scene", "line", "prefix", "source", "target"],
                vsn_rows,
            )

            # 3) UI: datav/1 (both) and datay/1 (jar only)
            for entry in ("datav/1", "datay/1"):
                if entry not in z_orig.namelist():
                    continue
                raw_orig = decrypt_file(z_orig.read(entry))
                raw_tgt = decrypt_file(z_tgt.read(entry))
                tpl_path = tpl_dir / tag / entry
                tpl_path.parent.mkdir(parents=True, exist_ok=True)
                tpl_path.write_bytes(raw_orig)
                tpl_meta["entries"][f"{tag}/{entry}"] = {"sha256": _sha(raw_orig), "bytes": len(raw_orig)}

                tok_orig = _json_tokens(raw_orig.decode("utf-8"))
                tok_tgt = _json_tokens(raw_tgt.decode("utf-8"))
                if set(tok_orig) != set(tok_tgt):
                    raise ValueError(f"{arch} {entry} JSON 结构键集合漂移")

                ui_rows = []
                seq_num = 0
                seq_tag = "DV" if entry.startswith("datav") else "DY"
                for path_tuple, (_, _, val_o) in tok_orig.items():
                    val_t = tok_tgt[path_tuple][2]
                    if not _is_ui_field(entry, path_tuple, val_o):
                        if val_o != val_t:
                            raise ValueError(f'{arch} {entry}: 受保护的界面字段改变：{path_tuple}')
                        continue
                    key_str = path_tuple[0] if entry == 'datav/1' else _pointer_str(path_tuple)
                    seq_num += 1
                    ui_rows.append([
                        f"{tag.upper()}-{seq_tag}-{seq_num:04d}",
                        arch,
                        entry,
                        key_str,
                        escape_tsv(val_o),
                        escape_tsv(val_t),
                    ])

                _write_tsv(
                    chunks_dir / "ui" / f"{tag}_{entry.split('/')[0]}.tsv",
                    f"{arch} {entry} 界面与词典分块（只改最后一列 target；保留原 \\n 分段与尾换行）",
                    ["seq", "archive", "entry", "key", "source", "target"],
                    ui_rows,
                )

    (tpl_dir / "manifest.json").write_text(
        json.dumps(tpl_meta, ensure_ascii=False, indent=2) + "\n", encoding="utf-8"
    )
    print(f"Export OK -> {chunks_dir.relative_to(ROOT)}")


# ---------------------------------------------------------------------------
# Reconstruct text entries from tl_work/chunks + tl_work/template
# ---------------------------------------------------------------------------

def _chunk_files(directory: Path, folder: str) -> list[Path]:
    paths = sorted((directory / folder).glob('*.tsv'))
    names = {path.name for path in paths}
    if names != CHUNK_NAMES[folder]:
        raise ValueError(f'{folder}: 缺少分块 {sorted(CHUNK_NAMES[folder] - names)}；额外分块 {sorted(names - CHUNK_NAMES[folder])}')
    return paths


def reconstruct_text_entries(tl_dir: Path) -> tuple[dict[str, dict[str, bytes]], list[str]]:
    tpl_dir = tl_dir / "template"
    chunks_dir = tl_dir / "chunks"
    if not (tpl_dir / "manifest.json").is_file():
        raise FileNotFoundError("缺少 tl_work/template/manifest.json，请先执行 tl_tool.py export")

    tpl_meta = json.loads((tpl_dir / "manifest.json").read_text("utf-8"))
    template_entries = {tuple(name.split('/', 1)) for name in tpl_meta['entries']}
    template_ui = {(TAG_ARCHIVE[tag], entry) for tag, entry in template_entries if entry in ('datav/1', 'datay/1')}
    template_scripts = {(TAG_ARCHIVE[tag], entry) for tag, entry in template_entries if entry not in ('datav/1', 'datay/1')}
    out_entries: dict[str, dict[str, bytes]] = {a: {} for a in ARCHIVES}
    all_texts: list[str] = []

    def load_tpl(arch: str, entry: str) -> bytes:
        tag = ARCHIVE_TAG[arch]
        p = tpl_dir / tag / entry
        data = p.read_bytes()
        expected = tpl_meta["entries"][f"{tag}/{entry}"]["sha256"]
        if _sha(data) != expected:
            raise ValueError(f"Template SHA 漂移: {tag}/{entry}")
        return data

    # 1) Line-based entries (dialogue + vsn)
    seen_ids = set()
    line_edits: dict[tuple[str, str], dict[int, tuple[str, str, str, str, str]]] = {}
    for folder, cols in (("dialogue", 8), ("vsn", 8)):
        for tsv in _chunk_files(chunks_dir, folder):
            tag, file_role = tsv.stem.split('_', 1)
            for parts in _read_tsv(tsv, cols):
                seq, arch, entry, scene, lineno_s, prefix_s, src_s, tgt_s = parts
                lineno = int(lineno_s)
                prefix = unescape_tsv(prefix_s)
                source = unescape_tsv(src_s)
                tgt = unescape_tsv(tgt_s)
                allowed = entry == file_role + '/1' if folder == 'dialogue' else _is_vsn_script_entry(entry)
                positions = line_edits.setdefault((arch, entry), {})
                if not allowed or arch != TAG_ARCHIVE[tag] or seq in seen_ids or lineno <= 0 or lineno in positions:
                    raise ValueError(f'{seq}: 禁用或重复的脚本定位')
                seen_ids.add(seq)
                if tgt.startswith('__RAW__:') and (arch, entry, lineno, tgt) != ('patch.pak', 'vsn/251', 94, '__RAW__: '):
                    raise ValueError(f'{seq}: 未登记的原样脚本行')
                check_target_value(seq, source, tgt, folder)
                positions[lineno] = (seq, scene, prefix, source, tgt)

    if line_edits.keys() - template_scripts:
        raise ValueError('TSV 指向冻结模板中没有的脚本')
    for arch, entry in sorted(template_scripts):
        edits = line_edits.get((arch, entry), {})
        raw = load_tpl(arch, entry)
        lines = _split_lines_lf(raw.decode("utf-8"))
        family = 'vsn' if entry.startswith('vsn/') else 'ds'
        scene = ''
        protected = {}
        for lineno, raw_line in enumerate(lines, 1):
            text, _ = _strip_cr(raw_line)
            name = text.strip()
            if family == 'ds' and name.startswith('<') and name.endswith('>') and len(name) > 2:
                scene = name[1:-1]
                continue
            role = _line_role(text, family)
            if role is not None:
                protected[lineno] = (scene, role)
        if edits.keys() != protected.keys():
            raise ValueError(f'{arch} {entry}: 脚本定位范围与冻结模板不同')
        for lineno, (seq, row_scene, prefix, source, tgt) in edits.items():
            original_scene, original_role = protected[lineno]
            if (family == 'ds' and row_scene != original_scene) or original_role != (prefix, source):
                raise ValueError(f'{seq}: 场景、说话人或原文列与冻结模板不一致')
            _, cr = _strip_cr(lines[lineno - 1])
            if tgt == "":
                lines[lineno - 1] = cr
            elif tgt.startswith("__RAW__:"):
                lines[lineno - 1] = tgt[8:] + cr
            else:
                written = tgt
                if entry.startswith(("datadf/", "datadm/")):
                    # Encode the soft break to a character PRG.afF accepts so all.ds
                    # loads; font coverage still sees the original U+2028 (skipped by
                    # optimized_fonts) because all_texts keeps tgt unchanged.
                    if DS_SOFT_BREAK_SENTINEL in tgt:
                        raise ValueError(
                            f"{seq}: target already contains the datadf/datadm soft-break sentinel U+2502"
                        )
                    written = tgt.replace(SOFT_BREAK, DS_SOFT_BREAK_SENTINEL)
                lines[lineno - 1] = prefix + written + cr
                all_texts.append(tgt)
        rebuilt = "\n".join(lines).encode("utf-8")
        if rebuilt != raw:
            out_entries[arch][entry] = rebuilt

    # 2) JSON-based entries (datav/1, datay/1)
    json_edits: dict[tuple[str, str], dict[tuple[str, ...], tuple[str, str, str]]] = {}
    for tsv in _chunk_files(chunks_dir, 'ui'):
        tag, file_role = tsv.stem.split('_', 1)
        for parts in _read_tsv(tsv, 6):
            seq, arch, entry, key_s, src_s, tgt_s = parts
            source = unescape_tsv(src_s)
            tgt = unescape_tsv(tgt_s)
            if seq in seen_ids or arch != TAG_ARCHIVE[tag] or entry != file_role + '/1':
                raise ValueError(f'{seq}: 禁用或重复的界面定位')
            seen_ids.add(seq)
            check_target_value(seq, source, tgt, 'ui')
            if entry.startswith("datav"):
                path_tuple = (key_s,)
            else:
                if not key_s.startswith("/"):
                    raise ValueError(f"{seq}: 无效 JSON 指针 {key_s!r}")
                path_tuple = tuple(p.replace("~1", "/").replace("~0", "~") for p in key_s[1:].split("/"))
            fields = json_edits.setdefault((arch, entry), {})
            if path_tuple in fields:
                raise ValueError(f'{seq}: 重复的界面键')
            fields[path_tuple] = (seq, source, tgt)

    if json_edits.keys() - template_ui:
        raise ValueError('TSV 指向冻结模板中没有的界面资源')
    for arch, entry in sorted(template_ui):
        edits = json_edits.get((arch, entry), {})
        raw = load_tpl(arch, entry)
        text = raw.decode("utf-8")
        tokens = _json_tokens(text)
        expected = {path for path, (_, _, value) in tokens.items() if _is_ui_field(entry, path, value)}
        if edits.keys() != expected:
            raise ValueError(f'{arch} {entry}: 界面键集合与冻结模板不一致')
        splices = []
        for path_tuple, (seq, source, new_val) in edits.items():
            if path_tuple not in tokens:
                raise ValueError(f"{arch} {entry} 缺少 JSON 键 {path_tuple}")
            start, end, old_val = tokens[path_tuple]
            if old_val != source:
                raise ValueError(f'{seq}: 界面原文列与冻结模板不一致')
            all_texts.append(new_val)
            if new_val != old_val:
                encoded = json.dumps(new_val, ensure_ascii=False)
                splices.append((start, end, encoded))
        if splices:
            splices.sort(key=lambda x: x[0], reverse=True)
            buf = text
            for start, end, encoded in splices:
                buf = buf[:start] + encoded + buf[end:]
            rebuilt = buf.encode("utf-8")
            json.loads(rebuilt.decode("utf-8"))  # validate well-formedness
            out_entries[arch][entry] = rebuilt

    return out_entries, all_texts


def _gather_strings(val) -> list[str]:
    if isinstance(val, str):
        return [val]
    if isinstance(val, dict):
        return [s for v in val.values() for s in _gather_strings(v)]
    if isinstance(val, list):
        return [s for v in val for s in _gather_strings(v)]
    return []


def _seal_entry(data: bytes) -> bytes:
    enc = encrypt_file(data, os.urandom(32), os.urandom(8))
    if decrypt_file(enc) != data:
        raise ValueError("Salsa20 加密回验失败")
    return enc


def _rewrite_zip(source: Path, target: Path, replacements: dict[str, bytes]):
    with zipfile.ZipFile(source) as before, zipfile.ZipFile(target, "w", zipfile.ZIP_DEFLATED, compresslevel=6) as after:
        names = set(before.namelist())
        for info in before.infolist():
            after.writestr(info, replacements.get(info.filename, before.read(info.filename)))
        for name, data in sorted(replacements.items()):
            if name not in names:
                after.writestr(name, data)
    with zipfile.ZipFile(source) as before, zipfile.ZipFile(target) as after:
        if after.testzip() is not None:
            raise ValueError(f"归档 CRC 校验失败: {target}")
        for name in set(before.namelist()) - set(replacements):
            if before.read(name) != after.read(name):
                raise AssertionError(f"非目标条目被修改: {name}")


# ---------------------------------------------------------------------------
# Build
# ---------------------------------------------------------------------------

def cmd_build(args):
    tl_dir = (ROOT / args.tl_dir).resolve()
    base_dir = (ROOT / args.base).resolve()
    out_dir = workspace_output(ROOT, args.output, exact=('payload',), parents=('build',))
    if out_dir != ROOT / 'payload' and out_dir.exists():
        raise FileExistsError('隔离构建需要新的 build/ 子目录')
    if any(p.is_relative_to(out_dir) or out_dir.is_relative_to(p) for p in (tl_dir, base_dir)):
        raise ValueError('构建输出不能与输入目录重叠')
    work_dirs = ('classes', 'tools', 'fonts', 'logs', 'staging-src')
    check_outputs(out_dir, work_dirs + ARCHIVES + ('font-manifest.json', 'classes.txt',
                  'target-pins.tsv', 'patch-passes.tsv', 'targets.jar', 'build-manifest.json'))

    jdk = ROOT / "deps" / "jdk17" / "bin"
    jre = ROOT / "deps" / "jre" / "bin" / "java.exe"
    if not (jdk / "javac.exe").is_file() or not jre.is_file():
        raise FileNotFoundError("缺少 deps/jdk17 或 deps/jre 运行环境")

    comp_cfg = json.loads((ROOT / "src/java/config/components.json").read_text("utf-8"))
    base_pins = {
        "cosmobreeder-multi.jar": "dc6b0cedc3a3b2f6f51941a2cef449d33ec87d314ee64ea63495c3ffdebd06be",
        "patch.pak": "d2e21deeb85d74e981770b247625ee7ceb7ed39ae566305c1833c2c3d97b54d5",
    }
    for arch, pin in base_pins.items():
        if _file_sha(base_dir / arch) != pin:
            raise ValueError(f"deps/r27-base/{arch} SHA 不匹配")

    # 1) Reconstruct plaintext entries from TSV chunks
    plain_entries, tsv_texts = reconstruct_text_entries(tl_dir)
    replacements: dict[str, dict[str, bytes]] = {a: {} for a in ARCHIVES}
    for arch, entries in plain_entries.items():
        for entry, raw in entries.items():
            replacements[arch][entry] = _seal_entry(raw)

    # 2) Collect all display characters (TSV texts + datav/1 + component required_chars)
    texts = list(tsv_texts)
    for comp_name in ("radio", "images"):
        chars = comp_cfg.get(comp_name, {}).get("required_chars", [])
        if isinstance(chars, list):
            texts.extend(chars)
        elif isinstance(chars, str):
            texts.append(chars)
    if comp_cfg.get("extra_required_chars"):
        texts.append(comp_cfg["extra_required_chars"])
    for arch in ARCHIVES:
        with zipfile.ZipFile(base_dir / arch) as z:
            raw = plain_entries[arch].get("datav/1") or decrypt_file(z.read("datav/1"))
            texts.extend(_gather_strings(json.loads(raw)))

    # 3) Build fonts + image overrides
    font_assets = optimized_fonts.build_assets(base_dir / "cosmobreeder-multi.jar", texts)

    if out_dir.exists():
        # Keep acceptance and test history; only regenerate the build-owned work dirs.
        for sub in work_dirs:
            if (out_dir / sub).exists():
                shutil.rmtree(out_dir / sub)
    out_dir.mkdir(parents=True, exist_ok=True)
    for sub in work_dirs:
        (out_dir / sub).mkdir(exist_ok=True)

    (out_dir / "font-manifest.json").write_text(
        json.dumps(font_assets["manifest"], ensure_ascii=False, indent=2) + "\n", encoding="utf-8"
    )
    for filename, data in font_assets["fnts"].items():
        (out_dir / "fonts" / filename).write_bytes(data)
    (out_dir / "fonts" / "bbc2-10px.fnt").write_bytes(font_assets["fnts"]["bbc2.fnt"])
    with zipfile.ZipFile(base_dir / "cosmobreeder-multi.jar") as z:
        (out_dir / "fonts" / "dingbats.fnt").write_bytes(z.read("dingbats.fnt"))

    for arch in ARCHIVES:
        with zipfile.ZipFile(base_dir / arch) as z:
            route = json.loads(decrypt_file(z.read("dataq/0")))
            _, regions = parse_atlas(decrypt_file(z.read("dataq/" + str(route["/sprites.atlas"]))).decode("utf-8"))
            page_entry = "dataq/" + str(route["/sprites.png"])
            page = Image.open(BytesIO(decrypt_file(z.read(page_entry)))).convert("RGBA")
            original = page.copy()
            page, _img_rep = optimized_images.apply_overrides(
                page, regions, "jar" if arch.endswith(".jar") else "patch"
            )
            for name, png in font_assets["png_regions"].items():
                role = next(r for r in regions if r["name"] == name)
                new_im = Image.open(BytesIO(png)).convert("RGBA")
                x, y = role["xy"]
                if list(new_im.size) != role["size"] or role["rotation"]:
                    raise ValueError(f"Font overlay geometry mismatch: {name}")
                page.paste(new_im, (x, y))
            if page.tobytes() != original.tobytes():
                b = BytesIO()
                page.save(b, format="PNG")
                replacements[arch][page_entry] = _seal_entry(b.getvalue())
            for filename, data in font_assets["fnts"].items():
                if filename in z.namelist() and z.read(filename) == data:
                    continue
                replacements[arch][filename] = data
            if font_assets["manifest"]["added_rectangles"]:
                for filename, data in font_assets["fnts"].items():
                    replacements[arch]["r28-font/" + filename] = data
                for name, png in font_assets["png_regions"].items():
                    replacements[arch]["r28-font/" + name + ".png"] = png
                replacements[arch]["r28-font/manifest.json"] = json.dumps(
                    font_assets["manifest"], ensure_ascii=False, indent=2
                ).encode("utf-8")
                replacements[arch]["r28-font/OFL8.txt"] = (ROOT / "deps/fonts/OFL.txt").read_bytes()
                for lic_name in LICENSE8:
                    replacements[arch]["r28-font/LICENSES8/" + lic_name] = (
                        ROOT / "deps/fonts/LICENSES" / lic_name
                    ).read_bytes()
                replacements[arch]["r28-font/NOTICE.txt"] = (
                    "Additional glyph contribution: Fusion Pixel Font 2026.10.16, Copyright (c) 2022 TakWolf, SIL OFL 1.1. "
                    "Native12 and native8 source SHA are recorded in manifest.json. New default10 cells are nearest-sampled "
                    "derivatives of native12, not native10. Existing game ASCII/font pixels remain under the original "
                    "rightsholders terms; OFL does not relicense game artwork. Full original font component notices remain "
                    "in the frozen story12/ bundle.\n"
                ).encode("utf-8")

    # 4) Compile Java runtime & patchers + run IncrementalPatchDriver
    manifest = {
        "version": "r28-full-opt-candidate",
        "builder": "tools/tl_tool.py",
        "status": "building",
        "full_component_set": True,
        "base_archives": base_pins,
        "commands": [],
        "game_started": False,
        "user_save_accessed": False,
        "installed": False,
        "real_clip_CRT_input_verified": False,
    }

    def run_step(label: str, argv: list[str | Path]):
        r = subprocess.run([str(x) for x in argv], cwd=ROOT, stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
        (out_dir / "logs" / f"{label}.log").write_bytes(r.stdout)
        manifest["commands"].append({"name": label, "exit_code": r.returncode})
        print(f"  [{label}] exit {r.returncode}", flush=True)
        if r.returncode != 0:
            raise RuntimeError(f"{label} failed; inspect {out_dir / 'logs' / (label + '.log')}")

    font_pins = {
        rec["original_sha256"]: rec["sha256"]
        for rec in font_assets["manifest"]["roles"].values()
        if rec["original_sha256"] != rec["sha256"]
    }
    runtime_src_dir = ROOT / "src/java/runtime"
    pinned_files = {"DialogueWrap.java", "StoryFont12.java", "EndingReportLayout.java"}
    staged_runtime = []
    for java_file in sorted(runtime_src_dir.rglob("*.java")):
        rel = java_file.relative_to(runtime_src_dir)
        text = java_file.read_text("utf-8")
        if java_file.name in pinned_files:
            for old_h, new_h in font_pins.items():
                if old_h in text:
                    text = text.replace(old_h, new_h)
        dst = out_dir / "staging-src" / rel
        dst.parent.mkdir(parents=True, exist_ok=True)
        dst.write_text(text, encoding="utf-8")
        staged_runtime.append(dst)

    run_step(
        "compile-runtime",
        [jdk / "javac.exe", "--release", "8", "-encoding", "UTF-8", "-cp", base_dir / "cosmobreeder-multi.jar", "-d", out_dir / "classes", *staged_runtime],
    )

    patcher_files = sorted((ROOT / "src/java/patchers").glob("*.java"))
    cp_tools = os.pathsep.join([str(out_dir / "classes"), str(base_dir / "cosmobreeder-multi.jar")])
    run_step(
        "compile-tools",
        [jdk / "javac.exe", *EXPORTS, "-encoding", "UTF-8", "-cp", cp_tools, "-d", out_dir / "tools", *patcher_files],
    )

    pins: dict[str, str] = {}
    passes: list[tuple[str, str]] = []
    for comp_name in ("core", "pattern", "compact", "scenes", "radio", "shop"):
        c = comp_cfg[comp_name]
        for cls, pin in c.get("target_pins", {}).items():
            cls = cls.removesuffix(".class")
            if cls in pins and pins[cls] != pin:
                raise ValueError(f"Conflicting target pin: {cls}")
            pins[cls] = pin
        if c.get("patcher_class"):
            passes.append((c["patcher_class"], c.get("patcher_method", "apply")))
        for item in c.get("patchers", []):
            passes.append((item["class"], item.get("method", "apply")))

    pins_tsv = out_dir / "target-pins.tsv"
    passes_tsv = out_dir / "patch-passes.tsv"
    pins_tsv.write_text("".join(f"{k}\t{v}\n" for k, v in sorted(pins.items())), encoding="utf-8")
    passes_tsv.write_text("".join(f"{c}\t{m}\n" for c, m in passes), encoding="utf-8")

    targets_jar = out_dir / "targets.jar"
    if targets_jar.exists():
        targets_jar.unlink()
    tool_cp = os.pathsep.join([str(out_dir / "tools"), str(out_dir / "classes"), str(base_dir / "cosmobreeder-multi.jar")])
    run_step(
        "patch-targets",
        [jdk / "java.exe", *EXPORTS, "-cp", tool_cp, "IncrementalPatchDriver", base_dir / "cosmobreeder-multi.jar", out_dir / "classes", pins_tsv, passes_tsv, targets_jar],
    )

    with zipfile.ZipFile(targets_jar) as z:
        code = {n: z.read(n) for n in z.namelist()}
    for cls_path in (out_dir / "classes").rglob("*.class"):
        name = cls_path.relative_to(out_dir / "classes").as_posix()
        data = cls_path.read_bytes()
        if not name.startswith(("PRG/", "cosmoloc/layout/")) or int.from_bytes(data[6:8], "big") != 52:
            raise ValueError(f"Runtime class scope/version error: {name}")
        if name in code:
            raise ValueError(f"Helper/target ownership collision: {name}")
        code[name] = data

    replacements["cosmobreeder-multi.jar"].update(code)
    for arch in ARCHIVES:
        _rewrite_zip(base_dir / arch, out_dir / arch, replacements[arch])

    classes_txt = out_dir / "classes.txt"
    classes_txt.write_text("\n".join(n[:-6].replace("/", ".") for n in code) + "\n", encoding="utf-8")
    verify_cp = os.pathsep.join([str(out_dir / "cosmobreeder-multi.jar"), str(out_dir / "tools")])
    run_step("verify-final-classes", [jre, "-Dfile.encoding=UTF-8", "-Xverify:all", "-cp", verify_cp, "VerifyLayout", classes_txt])

    manifest["archives"] = {
        a: {
            "sha256": _file_sha(out_dir / a),
            "bytes": (out_dir / a).stat().st_size,
            "changed_entries": sorted(replacements[a]),
        }
        for a in ARCHIVES
    }
    manifest["font_manifest"] = font_assets["manifest"]
    manifest["status"] = "integrated_candidate_not_real_clip_CRT_input_acceptance"
    manifest["class_inventory"] = sorted(code)
    (out_dir / "build-manifest.json").write_text(
        json.dumps(manifest, ensure_ascii=False, indent=2) + "\n", encoding="utf-8"
    )
    print(f"Build OK -> {out_dir.relative_to(ROOT)} ({len(code)} classes)")


# ---------------------------------------------------------------------------
# Status & Readback
# ---------------------------------------------------------------------------

def cmd_status(args):
    tl_dir = (ROOT / args.tl_dir).resolve()
    chunks_dir = tl_dir / "chunks"
    if not chunks_dir.is_dir():
        raise FileNotFoundError(f"找不到 {chunks_dir}，请先运行 tl_tool.py export")

    grand = {"rows": 0, "translated": 0, "untranslated": 0, "merged_empty": 0, "soft_breaks": 0}
    for folder, cols in (("dialogue", 8), ("vsn", 8), ("ui", 6)):
        for p in sorted((chunks_dir / folder).glob("*.tsv")):
            rows = _read_tsv(p, cols)
            c = {"rows": len(rows), "translated": 0, "untranslated": 0, "merged_empty": 0, "soft_breaks": 0}
            for r in rows:
                src, tgt = r[-2], r[-1]
                if tgt == "" and folder in ("dialogue", "vsn"):
                    c["merged_empty"] += 1
                elif tgt == src:
                    c["untranslated"] += 1
                else:
                    c["translated"] += 1
                c["soft_breaks"] += tgt.count(SOFT_BREAK_VIS)
            for k in grand:
                grand[k] += c[k]
            print(
                f"{p.relative_to(chunks_dir).as_posix():26s} "
                f"rows={c['rows']:5d}  zh={c['translated']:5d}  same={c['untranslated']:4d}  "
                f"merged_empty={c['merged_empty']:4d}  breaks={c['soft_breaks']:4d}"
            )
    print("-" * 80)
    print(
        f"{'TOTAL':26s} "
        f"rows={grand['rows']:5d}  zh={grand['translated']:5d}  same={grand['untranslated']:4d}  "
        f"merged_empty={grand['merged_empty']:4d}  breaks={grand['soft_breaks']:4d}"
    )


def cmd_verify_readback(args):
    tl_dir = (ROOT / args.tl_dir).resolve()
    tgt_dir = (ROOT / args.target).resolve()
    expected_entries, _ = reconstruct_text_entries(tl_dir)
    tpl_dir = tl_dir / "template"
    problems = []
    checked = 0

    for arch in ARCHIVES:
        tag = ARCHIVE_TAG[arch]
        with zipfile.ZipFile(tgt_dir / arch) as z:
            for tpl_file in sorted((tpl_dir / tag).rglob("*")):
                if not tpl_file.is_file():
                    continue
                entry = tpl_file.relative_to(tpl_dir / tag).as_posix()
                expected = expected_entries[arch].get(entry, tpl_file.read_bytes())
                actual = decrypt_file(z.read(entry))
                checked += 1
                if actual != expected:
                    problems.append(f"{arch} {entry}: decrypted bytes differ from TSV reconstruction")

    print(json.dumps({"target": str(tgt_dir.relative_to(ROOT)), "entries_checked": checked, "problems": problems}, ensure_ascii=False, indent=2))
    if problems:
        raise SystemExit(1)


def main():
    p = argparse.ArgumentParser(description=__doc__)
    sub = p.add_subparsers(dest="cmd", required=True)

    pe = sub.add_parser("export", help="从原版与已构建目标导出 tl_work/chunks/*.tsv 与 template")
    pe.add_argument("--originals", default="originals")
    pe.add_argument("--target", default="payload")
    pe.add_argument("--tl-dir", default="tl_work")
    pe.add_argument("--force", action="store_true")
    pe.set_defaults(func=cmd_export)

    pb = sub.add_parser("build", help="从 tl_work/chunks/*.tsv + src/java + assets 重建 payload/")
    pb.add_argument("--tl-dir", default="tl_work")
    pb.add_argument("--base", default="deps/r27-base")
    pb.add_argument("--output", default="payload")
    pb.set_defaults(func=cmd_build)

    ps = sub.add_parser("status", help="查看 tl_work/chunks/*.tsv 统计")
    ps.add_argument("--tl-dir", default="tl_work")
    ps.set_defaults(func=cmd_status)

    pv = sub.add_parser("verify-readback", help="核验 payload/ 明文与 tl_work/chunks/*.tsv 完全一致")
    pv.add_argument("--tl-dir", default="tl_work")
    pv.add_argument("--target", default="payload")
    pv.set_defaults(func=cmd_verify_readback)

    args = p.parse_args()
    args.func(args)


if __name__ == "__main__":
    main()
