# -*- coding: utf-8 -*-
"""Cosmobreeder Yiffai 中文补丁：翻译校对与质量检查工具（纯标准库，Python 3.12+）。

用法：
  python tools/review_tool.py stats              # 查看分块统计
  python tools/review_tool.py scan               # 规则扫描 -> review/findings.md + review/candidates.tsv
  python tools/review_tool.py terms [--apply]    # 对照 review/terms.tsv 检查/统一术语
  python tools/review_tool.py dedupe             # 查同文异译（含 SFW/NSFW 与词典/overlay 差异）
  python tools/review_tool.py export             # 导出校对工作表 -> review/sheet_*.tsv
  python tools/review_tool.py apply [--write]    # 把 review/sheet_*.tsv 的 revised 列写回 chunks
"""
from __future__ import annotations

import argparse
import collections
from pathlib import Path
import re
import shutil
import subprocess
import sys
import time

ROOT = Path(__file__).resolve().parents[1]
LIB = ROOT / "tools" / "lib"
sys.path.insert(0, str(LIB))

from editorial_repairs import _markers  # noqa: E402

TL_DEFAULT = ROOT / "tl_work"
REVIEW_DIR = ROOT / "review"
TERMS_PATH = REVIEW_DIR / "terms.tsv"

SOFT_BREAK = "\u2028"
SOFT_BREAK_VIS = "⏎"
HAN_RE = re.compile(r"[\u3400-\u9fff]")
ENG_WORD_RE = re.compile(r"[A-Za-z]{4,}")
HALF_PUNCT_RE = re.compile(r"[,;:!?]")
LINE_HEAD_BAD = set("，。！？；：、）】》」』”’,.!?;:)]}")
# 已知合法保留的英文词（不记为英文残留）
ALLOWED_ENGLISH = {
    "Cosmobreeder", "Yiffai", "Traeh", "The0", "Static", "Boss", "Area",
    "Select", "Start", "Enter", "Shift", "Ctrl", "Space", "Zener", "Neon",
    "Tutor", "Tutorial", "System", "Menu", "Radio", "HardFox", "VSN",
    "TEST", "INFO", "OK", "HP", "MP", "SP", "XP", "LVL", "MAX", "MIN",
    "GAME", "OVER", "LOAD", "SAVE", "EXIT", "BACK", "NEXT", "DATA", "CHIP",
    "STEAM", "ACHIEVEMENT", "BIGBOLD1", "BIGBOLD2", "NO_VALUE",
}


def escape_tsv(s: str) -> str:
    return (
        s.replace("\\", "\\\\")
        .replace("\t", "\\t")
        .replace("\r", "\\r")
        .replace("\n", "\\n")
        .replace(SOFT_BREAK, SOFT_BREAK_VIS)
    )


def unescape_tsv(s: str) -> str:
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


def iter_rows(tl_dir: Path):
    chunks = tl_dir / "chunks"
    for folder, cols in (("dialogue", 8), ("vsn", 8), ("ui", 6)):
        d = chunks / folder
        if not d.is_dir():
            continue
        for p in sorted(d.glob("*.tsv")):
            lines = p.read_text(encoding="utf-8-sig").splitlines()
            for idx, raw in enumerate(lines):
                if not raw.strip() or raw.startswith("#"):
                    continue
                parts = raw.split("\t")
                if len(parts) != cols:
                    continue
                if folder in ("dialogue", "vsn"):
                    yield {
                        "kind": folder,
                        "path": p,
                        "chunk": p.name,
                        "line_idx": idx,
                        "seq": parts[0],
                        "archive": parts[1],
                        "entry": parts[2],
                        "scene": parts[3],
                        "line": parts[4],
                        "prefix": unescape_tsv(parts[5]),
                        "src": unescape_tsv(parts[6]),
                        "tgt": unescape_tsv(parts[7]),
                        "raw_tgt": parts[7],
                        "parts": parts,
                    }
                else:
                    yield {
                        "kind": folder,
                        "path": p,
                        "chunk": p.name,
                        "line_idx": idx,
                        "seq": parts[0],
                        "archive": parts[1],
                        "entry": parts[2],
                        "scene": parts[3],
                        "line": parts[3],
                        "prefix": "",
                        "src": unescape_tsv(parts[4]),
                        "tgt": unescape_tsv(parts[5]),
                        "raw_tgt": parts[5],
                        "parts": parts,
                    }


def write_row(path: Path, line_idx: int, parts: list[str]):
    lines = path.read_text(encoding="utf-8-sig").splitlines()
    lines[line_idx] = "\t".join(parts)
    path.write_text("\n".join(lines) + "\n", encoding="utf-8-sig", newline="\n")


def load_terms(path: Path) -> list[dict]:
    if not path.is_file():
        return []
    rules = []
    for raw in path.read_text(encoding="utf-8-sig").splitlines():
        if not raw.strip() or raw.startswith("#"):
            continue
        parts = raw.split("\t")
        if len(parts) < 5:
            continue
        while len(parts) < 7:
            parts.append("")
        rules.append({
            "en": parts[0].strip(),
            "cn": parts[1].strip(),
            "variants": [v.strip() for v in parts[2].split("|") if v.strip()],
            "protect": [p.strip() for p in parts[3].split("|") if p.strip()],
            "mode": parts[4].strip() or "phrase",
            "exclude_en": [e.strip() for e in parts[5].split("|") if e.strip()],
            "note": parts[6].strip(),
        })
    return rules


def _mask_tokens(s: str) -> str:
    s = re.sub(r"@[A-Za-z][A-Za-z0-9_]*", " ", s)
    s = re.sub(r"\$\{[^{}]+\}", " ", s)
    s = re.sub(r"\{[^{}\r\n]+\}", " ", s)
    s = re.sub(r"</?[A-Za-z][^<>\r\n]*>", " ", s)
    return s


# ---------------------------------------------------------------------------
# Commands
# ---------------------------------------------------------------------------

def cmd_stats(args):
    rows = list(iter_rows(args.tl_dir))
    by_chunk = collections.OrderedDict()
    for r in rows:
        c = by_chunk.setdefault(f"{r['kind']}/{r['chunk']}", {"total": 0, "zh": 0, "same": 0, "empty": 0, "breaks": 0})
        c["total"] += 1
        if r["tgt"] == "" or r["tgt"].startswith("__RAW__:"):
            c["empty"] += 1
        elif r["tgt"] == r["src"]:
            c["same"] += 1
        else:
            c["zh"] += 1
        c["breaks"] += r["tgt"].count(SOFT_BREAK)
    for k, c in by_chunk.items():
        print(f"{k:28s} total={c['total']:5d}  zh={c['zh']:5d}  same={c['same']:4d}  empty={c['empty']:4d}  breaks={c['breaks']:4d}")


def cmd_scan(args):
    rows = list(iter_rows(args.tl_dir))
    rules = load_terms(TERMS_PATH)
    findings: dict[str, list[tuple[str, str, str, str]]] = collections.defaultdict(list)

    for r in rows:
        src, tgt = r["src"], r["tgt"]
        if tgt == "" or tgt.startswith("__RAW__:"):
            continue
        loc = f"{r['chunk']}#{r['seq']}"

        # 1) 占位符与引擎标记守恒
        if _markers(src) != _markers(tgt):
            findings["marker_mismatch"].append((loc, r["scene"], src, tgt))

        # 2) 行尾半角空格（原文无而译文有）
        if tgt.endswith(" ") and not src.endswith(" ") and not r["scene"].startswith(("ui.end.", "ui.backers.")):
            findings["trailing_space"].append((loc, r["scene"], src, tgt))

        # 3) 对话/VSN 中疑似未翻译英文整句
        if tgt == src and re.search(r"[A-Za-z]{4,}", src) and not re.fullmatch(r"[\s|*<>A-Z0-9_.\-]+", src):
            if not any(tok in src for tok in ("ui.end", "save.", "input.")):
                findings["untranslated"].append((loc, r["scene"], src, tgt))

        # 4) 汉语夹杂半角标点
        if HAN_RE.search(tgt):
            masked = _mask_tokens(tgt)
            if HALF_PUNCT_RE.search(masked):
                # 排除数字小数/时间冒号/英文缩写
                stripped_num = re.sub(r"\d+[:.,]\d+", "", masked)
                stripped_eng = re.sub(r"[A-Za-z0-9_]+[,;:!?]\s*[A-Za-z0-9_]*", "", stripped_num)
                if HALF_PUNCT_RE.search(stripped_eng):
                    findings["halfwidth_punct"].append((loc, r["scene"], src, tgt))

        # 5) 显式 U+2028 断行后首字是否为禁止行首标点
        if SOFT_BREAK in tgt:
            segs = tgt.split(SOFT_BREAK)
            for seg in segs[1:]:
                if seg and seg[0] in LINE_HEAD_BAD:
                    findings["explicit_line_head_punct"].append((loc, r["scene"], src, tgt))
                    break

        # 6) 术语变体命中
        for rule in rules:
            if not rule["variants"]:
                continue
            if rule["exclude_en"] and any(ex.lower() in src.lower() for ex in rule["exclude_en"]):
                continue
            if rule["mode"] == "word":
                if not re.search(rf"\b{re.escape(rule['en'])}\b", src, re.IGNORECASE):
                    continue
            else:
                if rule["en"].lower() not in src.lower():
                    continue
            check_tgt = tgt
            for prot in rule["protect"]:
                check_tgt = check_tgt.replace(prot, "")
            hit = next((v for v in rule["variants"] if v in check_tgt), None)
            if hit:
                findings[f"term:{rule['en']}"].append((loc, r["scene"], f"[{hit}->{rule['cn']}] {src}", tgt))

    REVIEW_DIR.mkdir(parents=True, exist_ok=True)
    md_lines = [
        "# 规则扫描报告（review_tool.py scan）",
        "",
        f"扫描总行数：{len(rows)}",
        "",
        "| 类别 | 命中数 |",
        "| --- | ---: |",
    ]
    cand_lines = ["# kind\tlocation\tscene\tsource\ttarget"]
    for cat in sorted(findings):
        items = findings[cat]
        md_lines.append(f"| `{cat}` | {len(items)} |")
    md_lines.append("")
    for cat in sorted(findings):
        items = findings[cat]
        md_lines.append(f"## {cat}（{len(items)}）")
        md_lines.append("")
        for loc, scene, src, tgt in items[: args.show]:
            md_lines.append(f"- `{loc}` ({scene})")
            md_lines.append(f"  - EN: `{escape_tsv(src)[:120]}`")
            md_lines.append(f"  - ZH: `{escape_tsv(tgt)[:120]}`")
        if len(items) > args.show:
            md_lines.append(f"- ……其余 {len(items) - args.show} 条见 `review/candidates.tsv`")
        md_lines.append("")
        for loc, scene, src, tgt in items:
            cand_lines.append(f"{cat}\t{loc}\t{scene}\t{escape_tsv(src)}\t{escape_tsv(tgt)}")

    (REVIEW_DIR / "findings.md").write_text("\n".join(md_lines) + "\n", encoding="utf-8")
    (REVIEW_DIR / "candidates.tsv").write_text("\n".join(cand_lines) + "\n", encoding="utf-8-sig", newline="\n")
    for cat in sorted(findings):
        print(f"  {cat:28s}: {len(findings[cat])}")
    print(f"报告已写入 review/findings.md 与 review/candidates.tsv")


def cmd_terms(args):
    rules = load_terms(TERMS_PATH)
    if args.rule:
        rules = [r for r in rules if r["en"].lower() == args.rule.lower()]
    rows = list(iter_rows(args.tl_dir))
    edits = []
    for r in rows:
        if r["tgt"] == "" or r["tgt"].startswith("__RAW__:"):
            continue
        new_tgt = r["tgt"]
        for rule in rules:
            if not rule["variants"]:
                continue
            if rule["exclude_en"] and any(ex.lower() in r["src"].lower() for ex in rule["exclude_en"]):
                continue
            if rule["mode"] == "word":
                if not re.search(rf"\b{re.escape(rule['en'])}\b", r["src"], re.IGNORECASE):
                    continue
            else:
                if rule["en"].lower() not in r["src"].lower():
                    continue
            # 保护段临时替换
            placeholders = {}
            tmp = new_tgt
            for i, prot in enumerate(rule["protect"]):
                token = f"__PROT_{i}__"
                if prot in tmp:
                    placeholders[token] = prot
                    tmp = tmp.replace(prot, token)
            for v in rule["variants"]:
                if v in tmp:
                    tmp = tmp.replace(v, rule["cn"])
            for token, prot in placeholders.items():
                tmp = tmp.replace(token, prot)
            new_tgt = tmp
        if new_tgt != r["tgt"]:
            edits.append((r, new_tgt))

    print(f"术语统一命中: {len(edits)} 行")
    for r, new_tgt in edits[: args.show]:
        print(f"  {r['chunk']}#{r['seq']} ({r['scene']})")
        print(f"    - {escape_tsv(r['tgt'])}")
        print(f"    + {escape_tsv(new_tgt)}")
    if not args.apply or not edits:
        if edits:
            print("(dry-run，加 --apply 才会写回 chunks)")
        return
    stamp = time.strftime("%Y%m%d-%H%M%S")
    bak_dir = REVIEW_DIR / f"backup_chunks_{stamp}"
    bak_dir.mkdir(parents=True, exist_ok=True)
    for r, new_tgt in edits:
        bak_file = bak_dir / r["kind"] / r["chunk"]
        if not bak_file.exists():
            bak_file.parent.mkdir(parents=True, exist_ok=True)
            shutil.copy2(r["path"], bak_file)
        parts = list(r["parts"])
        parts[-1] = escape_tsv(new_tgt)
        write_row(r["path"], r["line_idx"], parts)
    print(f"已写回 {len(edits)} 行，备份 -> {bak_dir.relative_to(ROOT)}")


def cmd_dedupe(args):
    rows = list(iter_rows(args.tl_dir))
    by_src: dict[str, list[dict]] = collections.defaultdict(list)
    for r in rows:
        if r["tgt"] == "" or r["tgt"].startswith("__RAW__:"):
            continue
        by_src[r["src"]].append(r)

    conflicts = []
    for src, group in by_src.items():
        if len(group) < 2 or not re.search(r"[A-Za-z]{3,}", src):
            continue
        # 去掉软断行符比较纯文本口径
        variants = collections.Counter(r["tgt"].replace(SOFT_BREAK, "") for r in group)
        if len(variants) > 1:
            conflicts.append((len(group), src, variants, group))

    conflicts.sort(key=lambda x: -x[0])
    print(f"同文异译条目组: {len(conflicts)}")
    for cnt, src, variants, group in conflicts[: args.show]:
        print(f"  [{cnt}次] EN: {escape_tsv(src)[:90]}")
        for zh, n in variants.most_common():
            locs = ", ".join(f"{r['chunk']}#{r['seq']}" for r in group if r["tgt"].replace(SOFT_BREAK, "") == zh)[:60]
            print(f"    ({n}x) {escape_tsv(zh)[:90]}  [{locs}]")


def cmd_export(args):
    rows = list(iter_rows(args.tl_dir))
    REVIEW_DIR.mkdir(parents=True, exist_ok=True)
    by_chunk: dict[str, list[dict]] = collections.defaultdict(list)
    for r in rows:
        by_chunk[r["chunk"]].append(r)
    for chunk_name, items in sorted(by_chunk.items()):
        out = REVIEW_DIR / f"sheet_{chunk_name}"
        lines = ["# chunk\tseq\tscene\tprefix\tsource\ttarget\trevised\tverdict\tnote"]
        for r in items:
            lines.append("\t".join([
                r["chunk"],
                r["seq"],
                r["scene"],
                escape_tsv(r["prefix"]),
                escape_tsv(r["src"]),
                r["raw_tgt"],
                "",
                "",
                "",
            ]))
        out.write_text("\n".join(lines) + "\n", encoding="utf-8-sig", newline="\n")
    print(f"已导出 {len(by_chunk)} 份校对清单到 review/sheet_*.tsv")


def cmd_apply(args):
    sheets = [Path(args.sheet)] if args.sheet else sorted(REVIEW_DIR.glob("sheet_*.tsv"))
    if not sheets:
        print("未找到 review/sheet_*.tsv")
        return
    index = {(r["chunk"], r["seq"]): r for r in iter_rows(args.tl_dir)}
    changes = []
    for sh in sheets:
        for lineno, raw in enumerate(sh.read_text(encoding="utf-8-sig").splitlines(), 1):
            if not raw.strip() or raw.startswith("#"):
                continue
            parts = raw.split("\t")
            if len(parts) < 7:
                continue
            chunk, seq, _scene, _pfx, _src, old_raw, revised = parts[:7]
            if not revised.strip() or revised == old_raw:
                continue
            r = index.get((chunk, seq))
            if r is None:
                raise ValueError(f"{sh}:{lineno}: 找不到条目 {chunk}#{seq}")
            changes.append((r, revised))
    print(f"待写回修改: {len(changes)} 行")
    for r, revised in changes[: args.show]:
        print(f"  {r['chunk']}#{r['seq']}")
        print(f"    - {r['raw_tgt'][:100]}")
        print(f"    + {revised[:100]}")
    if not args.write or not changes:
        if changes:
            print("(dry-run，加 --write 才会写回 chunks)")
        return
    stamp = time.strftime("%Y%m%d-%H%M%S")
    bak_dir = REVIEW_DIR / f"backup_chunks_{stamp}"
    for r, revised in changes:
        bak_file = bak_dir / r["kind"] / r["chunk"]
        if not bak_file.exists():
            bak_file.parent.mkdir(parents=True, exist_ok=True)
            shutil.copy2(r["path"], bak_file)
        parts = list(r["parts"])
        parts[-1] = revised
        write_row(r["path"], r["line_idx"], parts)
    print(f"已写回 {len(changes)} 行，备份 -> {bak_dir.relative_to(ROOT)}")
    if args.build:
        subprocess.run([sys.executable, str(ROOT / "tl_work/chain_build.py"), "--apply"], cwd=ROOT, check=True)


def main():
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--tl-dir", type=Path, default=TL_DEFAULT)
    sub = ap.add_subparsers(dest="cmd", required=True)

    st = sub.add_parser("stats", help="分块统计")
    st.set_defaults(func=cmd_stats)

    sc = sub.add_parser("scan", help="规则预筛 -> review/findings.md")
    sc.add_argument("--show", type=int, default=8)
    sc.set_defaults(func=cmd_scan)

    tm = sub.add_parser("terms", help="对照 review/terms.tsv 统一术语")
    tm.add_argument("--rule")
    tm.add_argument("--apply", action="store_true")
    tm.add_argument("--show", type=int, default=12)
    tm.set_defaults(func=cmd_terms)

    dd = sub.add_parser("dedupe", help="检查同文异译")
    dd.add_argument("--show", type=int, default=15)
    dd.set_defaults(func=cmd_dedupe)

    ex = sub.add_parser("export", help="导出校对清单 review/sheet_*.tsv")
    ex.set_defaults(func=cmd_export)

    ap_ = sub.add_parser("apply", help="将 sheet_*.tsv 的 revised 写回 chunks")
    ap_.add_argument("--sheet")
    ap_.add_argument("--write", action="store_true")
    ap_.add_argument("--build", action="store_true")
    ap_.add_argument("--show", type=int, default=12)
    ap_.set_defaults(func=cmd_apply)

    args = ap.parse_args()
    args.tl_dir = (ROOT / args.tl_dir).resolve() if not args.tl_dir.is_absolute() else args.tl_dir.resolve()
    args.func(args)


if __name__ == "__main__":
    main()
