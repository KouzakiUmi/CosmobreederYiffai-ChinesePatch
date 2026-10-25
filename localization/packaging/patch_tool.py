#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""Cosmobreeder Yiffai 中文汉化补丁 —— 安装/卸载/检查。

    py patch_tool.py install     [--game-dir DIR] [--force] [--backup-dir DIR]
    py patch_tool.py uninstall   [--game-dir DIR] [--force]
    py patch_tool.py check       [--game-dir DIR]
    py patch_tool.py find

设计上的几个取舍（照 Winds of Change / FizRP 汉化补丁的做法）：

1. **备份放在游戏目录里**，不放在补丁目录。补丁包被删了也还能还原。
2. **安装前校验原版哈希**。游戏更新过或已被别的补丁改过时，覆盖会毁掉别人的改动。
3. **卸载前校验当前文件仍是我们装的版本**。用户装完后自己动过，就不还原，免得覆盖。
4. **只动两个文件**：cosmobreeder-multi.jar 和 patch.pak。不写注册表、不动存档。

只用标准库。Windows 上 PATH 里有 py 或 python 即可。
"""
import argparse
import io
import json
import os
import re
import shutil
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
# PyInstaller --onefile 会把 datas 解到 sys._MEIPASS。源码直接跑时用脚本所在目录。
ROOT = getattr(sys, "_MEIPASS", HERE)
MANIFEST = os.path.join(ROOT, "manifest.json")
PAYLOAD = os.path.join(ROOT, "payload")

# 备份目录与状态文件都放在游戏根目录，跟着游戏走
BACKUP_DIRNAME = "_汉化补丁备份"
STATE_NAME = "install-state.json"

GAME_EXE_HINTS = ["Cosmobreeder Yiffai.exe", "cosmobreeder-yiffai.exe"]
# 只有 cosmobreeder-multi.jar 是必须的；patch.pak 是官方 NSFW 补丁，本体版没有它。
REQUIRED = ["cosmobreeder-multi.jar"]


# ------------------------------------------------------------------ 基础工具

def sha256(path):
    import hashlib
    h = hashlib.sha256()
    with open(path, "rb") as f:
        for chunk in iter(lambda: f.read(1 << 20), b""):
            h.update(chunk)
    return h.hexdigest()


def human(n):
    for unit in ("B", "KB", "MB", "GB"):
        if n < 1024 or unit == "GB":
            return "%.1f %s" % (n, unit)
        n /= 1024.0


def load_manifest():
    with io.open(MANIFEST, encoding="utf-8") as f:
        return json.load(f)


def read_state(game):
    p = os.path.join(game, STATE_NAME)
    try:
        with io.open(p, encoding="utf-8") as f:
            return json.load(f), p
    except Exception:
        return {}, p


def write_state(game, state):
    p = os.path.join(game, STATE_NAME)
    with io.open(p, "w", encoding="utf-8") as f:
        json.dump(state, f, ensure_ascii=False, indent=1)
    return p


# ------------------------------------------------------------------ 找游戏目录

def variants_of(man):
    """manifest 支持多版本；只有单版本时退回旧的 files 结构。"""
    if man.get("variants"):
        return man["variants"]
    return {"vanilla": {"label": "本体版", "files": man.get("files", []), "available": True}}


def pick_variant(man, game):
    """按游戏里有没有 patch.pak、以及它的哈希，判断该装哪个版本。

    detect 规则两种写法：
      {"patch.pak": {"sha256": "..."}}   文件存在且哈希匹配
      {"patch.pak": {"absent": True}}    文件不存在

    官方本体和官方 NSFW 补丁都叫 patch.pak，只能这样区分。
    """
    vs = variants_of(man)
    notes = []
    for name, v in vs.items():
        rules = v.get("detect") or {}
        if not rules:
            continue
        ok = True
        detail = []
        for fname, rule in rules.items():
            p = os.path.join(game, fname)
            exists = os.path.isfile(p)
            if rule.get("absent"):
                if exists:
                    ok = False; detail.append("%s 存在" % fname)
            elif not exists:
                ok = False; detail.append("%s 不存在" % fname)
            elif sha256(p) != rule["sha256"]:
                ok = False; detail.append("%s 哈希不符" % fname)
            if not ok:
                break
        if ok:
            return name, v, notes
        notes.append("  %-10s %s（%s）" % (name, v.get("label", ""), "，".join(detail) or "未匹配"))
    return None, None, notes


def all_files_map(man):
    """所有版本里出现过的文件定义，按 path 索引。"""
    out = {}
    for v in variants_of(man).values():
        for e in v.get("files", []):
            out[e["path"]] = e
    return out


def installed_file_defs(man, state):
    """卸载/检查时用安装当时记录的文件列表。"""
    m = all_files_map(man)
    paths = (state or {}).get("files") or []
    defs = [m[p] for p in paths if p in m]
    return defs or list(m.values())


def check_game_dir(path):
    """返回 None 表示没问题，否则返回一句人话说明哪里不对。"""
    if not path or not os.path.isdir(path):
        return "目录不存在"
    for name in REQUIRED:
        if not os.path.isfile(os.path.join(path, name)):
            return "找不到 %s（这里不是游戏根目录）" % name
    return None


def _steam_roots():
    """收集所有可能的 steamapps 目录：常见路径 + libraryfolders.vdf + 注册表。"""
    roots = []
    bases = [
        r"C:\Program Files (x86)\Steam",
        r"C:\Program Files\Steam",
        r"C:\Steam",
        r"C:\SteamLibrary",
        r"D:\Steam",
        r"D:\SteamLibrary",
        r"E:\Steam",
        r"E:\SteamLibrary",
        r"F:\SteamLibrary",
    ]
    for b in bases:
        roots.append(os.path.join(b, "steamapps"))
    # 注册表里 Steam 的真实安装位置
    try:
        import winreg
        for hive, key in ((winreg.HKEY_LOCAL_MACHINE, r"SOFTWARE\WOW6432Node\Valve\Steam"),
                          (winreg.HKEY_LOCAL_MACHINE, r"SOFTWARE\Valve\Steam"),
                          (winreg.HKEY_CURRENT_USER, r"Software\Valve\Steam")):
            try:
                k = winreg.OpenKey(hive, key)
                for value in ("InstallPath", "SteamPath"):
                    try:
                        p = winreg.QueryValueEx(k, value)[0]
                        if p:
                            roots.append(os.path.join(p.replace("/", os.sep), "steamapps"))
                    except OSError:
                        pass
            except OSError:
                pass
    except ImportError:
        pass
    # 每个已知库里可能有 libraryfolders.vdf 指向更多库
    extra = []
    for sa in roots:
        vdf = os.path.join(sa, "libraryfolders.vdf")
        if os.path.isfile(vdf):
            try:
                txt = io.open(vdf, encoding="utf-8", errors="ignore").read()
                for p in re.findall(r'"path"\s+"([^"]+)"', txt):
                    extra.append(os.path.join(p.replace("\\\\", "\\"), "steamapps"))
            except Exception:
                pass
    roots.extend(extra)
    # 去重、保序
    seen, out = set(), []
    for r in roots:
        r = os.path.normpath(r)
        if r.lower() not in seen:
            seen.add(r.lower())
            out.append(r)
    return out


def find_game():
    """返回所有看起来装了这个游戏的目录。"""
    found = []
    # 1) Steam 库
    for sa in _steam_roots():
        common = os.path.join(sa, "common")
        if not os.path.isdir(common):
            continue
        try:
            entries = os.listdir(common)
        except OSError:
            continue
        for name in entries:
            if "cosmobreeder" in name.lower() or "yiffai" in name.lower():
                cand = os.path.join(common, name)
                if not check_game_dir(cand):
                    found.append(cand)
    # 2) 上一级/上两级目录（有人把补丁解压进游戏里，或者游戏不在 Steam 库）
    for up in (os.path.dirname(HERE), os.path.dirname(os.path.dirname(HERE))):
        if up and not check_game_dir(up):
            found.append(up)
    # 去重
    seen, out = set(), []
    for f in found:
        k = os.path.normpath(f).lower()
        if k not in seen:
            seen.add(k)
            out.append(os.path.normpath(f))
    return out


def resolve_game(args, need_state=False):
    if getattr(args, "game_dir", None):
        game = os.path.abspath(args.game_dir)
    else:
        cands = find_game()
        if not cands:
            sys.exit("没自动找到游戏目录。\n"
                     "请把本补丁文件夹放进游戏根目录（含 cosmobreeder-multi.jar 的那一层）\n"
                     "或者手动指定：py patch_tool.py install --game-dir \"D:\\...\\Cosmobreeder Yiffai\"")
        game = cands[0]
        if len(cands) > 1:
            print("找到多个安装，使用第一个：")
            for c in cands:
                print("   -", c)
    err = check_game_dir(game)
    if err:
        sys.exit("游戏目录无效：%s\n   %s" % (game, err))
    print("游戏目录：", game)
    return game


# --------------------------------------------------------------------- 命令

def cmd_find(args):
    cands = find_game()
    if not cands:
        print("没找到。请用 --game-dir 手动指定游戏根目录。")
        return 1
    for c in cands:
        print("找到：", c)
    return 0


def cmd_check(args):
    game = resolve_game(args)
    man = load_manifest()
    state, sp = read_state(game)
    print()
    print("补丁版本：", man["version"], "（构建于 %s）" % man["built"])
    vname, var, notes = pick_variant(man, game)
    if var:
        print("游戏版本：", var.get("label", vname))
    else:
        print("游戏版本：未识别")
        for n in notes:
            print(n)
    print("安装状态：", "已安装" if state else "未安装（或状态文件丢失）")
    if state:
        print("   装于：", state.get("installed_at", "?"))
        print("   备份：", state.get("backup_dir", "?"))
    print()
    print("%-28s %-12s %s" % ("文件", "大小", "状态"))
    print("-" * 62)
    _vname, _var, _ = pick_variant(man, game)
    _defs = installed_file_defs(man, state) if state else (_var or {}).get("files", [])
    for e in _defs:
        p = os.path.join(game, e["path"])
        if not os.path.isfile(p):
            print("%-28s %-12s %s" % (e["path"], "-", "缺失"))
            continue
        h = sha256(p)
        size = os.path.getsize(p)
        if h == e["sha256"]:
            tag = "已是汉化版"
        elif h == e["original"]["sha256"]:
            tag = "原版（未打补丁）"
        else:
            tag = "被改动过（既非原版也非本补丁）"
        print("%-28s %-12s %s" % (e["path"], human(size), tag))
    print()
    return 0


def cmd_install(args):
    game = resolve_game(args)
    man = load_manifest()
    state, sp = read_state(game)
    if state and not args.force:
        sys.exit("这个目录已经装过本补丁了。\n"
                 "要重装请加 --force；要还原请重新运行本程序并点「卸载 / 还原」。")

    vname, var, notes = pick_variant(man, game)
    if not var:
        print()
        print("无法识别这个游戏版本。当前 patch.pak 不属于已知的任何一种：")
        for n in notes:
            print(n)
        sys.exit("\n官方本体和官方 NSFW 补丁都叫 patch.pak，只能靠哈希区分。\n"
                 "如果这是 NSFW 版但本补丁包没带它的汉化，就不能装——否则会把 NSFW 内容覆盖掉。\n"
                 "请确认游戏版本，或使用对应版本的补丁包。")
    if not var.get("available", True):
        sys.exit("识别到「%s」，但本补丁包只带其它版本的汉化，装不了。\n"
                 "请使用对应版本的补丁包。" % var.get("label", vname))
    print("游戏版本：", var.get("label", vname))
    files = var["files"]

    # --- 1. 校验 payload 自己是否完好（包传坏了不能写进游戏）
    for e in files:
        src = os.path.join(PAYLOAD, e["payload"])
        if not os.path.isfile(src):
            sys.exit("补丁包不完整，缺少文件：payload\\%s" % e["payload"])
        if sha256(src) != e["sha256"]:
            sys.exit("补丁包已损坏：payload\\%s 的校验值不对。\n请重新解压一次补丁包。" % e["payload"])

    # --- 2. 校验游戏是不是我们这个版本（防止覆盖别人/更新后的文件）
    warnings = []
    for e in files:
        dst = os.path.join(game, e["path"])
        if not os.path.isfile(dst):
            sys.exit("游戏目录里找不到 %s，无法安装。" % e["path"])
        cur = sha256(dst)
        if cur == e["sha256"]:
            warnings.append("%s 已经是汉化版（重复安装）" % e["path"])
        elif cur != e["original"]["sha256"]:
            warnings.append("%s 和本补丁构建时的原版不一致"
                            "（游戏可能更新过，或已被其他补丁改过）" % e["path"])
    if warnings:
        print()
        print("注意：")
        for w in warnings:
            print("   -", w)
        if not args.force:
            sys.exit("\n为了不覆盖别人的改动，已停止。\n"
                     "确认要继续请加 --force。")
        print("\n已指定 --force，继续。")

    # --- 3. 备份（已备份过的跳过，避免用汉化版覆盖掉真原版）
    bdir = os.path.abspath(args.backup_dir) if getattr(args, "backup_dir", None) \
        else os.path.join(game, BACKUP_DIRNAME)
    os.makedirs(bdir, exist_ok=True)
    backed = []
    for e in files:
        dst = os.path.join(game, e["path"])
        bp = os.path.join(bdir, e["path"])
        if os.path.isfile(bp):
            print("备份已存在，跳过：", e["path"])
            continue
        shutil.copy2(dst, bp)
        backed.append(e["path"])
        print("已备份原版：%s (%s)" % (e["path"], human(os.path.getsize(bp))))

    # --- 4. 写入
    for e in files:
        src = os.path.join(PAYLOAD, e["payload"])
        dst = os.path.join(game, e["path"])
        try:
            shutil.copy2(src, dst)
        except PermissionError:
            sys.exit("\n写入 %s 失败：文件被占用。\n请先完全退出游戏（包括后台的 Steam 云同步），再重试。" % e["path"])
        print("已写入：%s (%s)" % (e["path"], human(os.path.getsize(dst))))

    # --- 5. 记状态
    import datetime
    write_state(game, {
        "patch": man["name"],
        "version": man["version"],
        "installed_at": datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
        "backup_dir": bdir,
        "backed_up": backed,
        "files": [e["path"] for e in files],
        "sha256": {e["path"]: e["sha256"] for e in files},
    })

    print()
    print("安装完成。直接启动游戏就是中文。")
    print("备份在：", bdir)
    print("要还原原版，重新运行本程序并点「卸载 / 还原」。")
    return 0


def cmd_uninstall(args):
    game = resolve_game(args)
    man = load_manifest()
    state, sp = read_state(game)
    if not state and not args.force:
        sys.exit("这个目录没有安装记录，可能本来就没装。\n"
                 "如果确实装过（比如状态文件被删了），加 --force 强制还原。")

    bdir = state.get("backup_dir") or os.path.join(game, BACKUP_DIRNAME)
    if not os.path.isdir(bdir):
        sys.exit("找不到备份目录：%s\n无法还原。可能需要用 Steam 的"
                 "「验证游戏文件完整性」来修复。" % bdir)
    print("备份目录：", bdir)

    restored = skipped = 0
    for e in installed_file_defs(man, state):
        dst = os.path.join(game, e["path"])
        bp = os.path.join(bdir, e["path"])
        if not os.path.isfile(bp):
            print("跳过（没有备份）：", e["path"])
            skipped += 1
            continue
        # 当前文件如果既不是汉化版也不是原版，说明装完后被改过，不覆盖
        if os.path.isfile(dst):
            cur = sha256(dst)
            allowed = {e["sha256"], e["original"]["sha256"], sha256(bp)}
            if cur not in allowed and not args.force:
                print("跳过（装完之后被改动过，不覆盖）：", e["path"])
                skipped += 1
                continue
        try:
            shutil.copy2(bp, dst)
        except PermissionError:
            sys.exit("\n还原 %s 失败：文件被占用。请先完全退出游戏。" % e["path"])
        print("已还原：", e["path"])
        restored += 1

    if restored and not skipped:
        try:
            os.remove(sp)
        except OSError:
            pass
    print()
    print("卸载完成：还原 %d 个文件%s。" % (restored, "，跳过 %d 个" % skipped if skipped else ""))
    if skipped:
        print("跳过的文件请用 Steam「验证游戏文件完整性」修复。")
    return 0


def main():
    ap = argparse.ArgumentParser(
        prog="patch_tool.py",
        description="Cosmobreeder Yiffai 中文汉化补丁 安装/卸载/检查")
    sub = ap.add_subparsers(dest="cmd", required=True)

    def common(p):
        p.add_argument("--game-dir", help="游戏根目录（含 cosmobreeder-multi.jar 的那一层）")
        p.add_argument("--force", action="store_true", help="跳过安全检查")

    common(sub.add_parser("install", help="安装汉化补丁"))
    sub.choices["install"].add_argument("--backup-dir", help="自定义备份位置")
    common(sub.add_parser("uninstall", help="还原成原版"))
    common(sub.add_parser("check", help="查看当前装没装、文件对不对"))
    sub.add_parser("find", help="自动探测游戏装在哪")

    a = ap.parse_args()
    fn = {"install": cmd_install, "uninstall": cmd_uninstall,
          "check": cmd_check, "find": cmd_find}[a.cmd]
    return fn(a)


if __name__ == "__main__":
    try:
        sys.exit(main())
    except KeyboardInterrupt:
        print("\n已取消。")
        sys.exit(130)
