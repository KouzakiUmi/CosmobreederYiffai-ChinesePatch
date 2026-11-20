# -*- coding: utf-8 -*-
"""Cosmobreeder Yiffai 中文补丁安装器统一入口（包装 src/cosmobreeder_patch）。

用法：
  python tools/patch_tool.py gui --payload <PATH>         # 启动图形界面
  python tools/patch_tool.py find                         # 自动查找 Steam / 附近游戏目录
  python tools/patch_tool.py check --payload <PATH> --game-dir <PATH>
  python tools/patch_tool.py install --payload <PATH> --game-dir <PATH>
  python tools/patch_tool.py uninstall --payload <PATH> --game-dir <PATH>
  python tools/patch_tool.py verify --payload <PATH>      # 只读校验差分负载
  python tools/patch_tool.py licenses                     # 输出全部第三方许可文本
"""
from __future__ import annotations

import argparse
import json
from pathlib import Path
import sys

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "src"))

from cosmobreeder_patch import __main__ as entry  # noqa: E402
from cosmobreeder_patch.discovery import find_game  # noqa: E402


def main():
    p = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    sub = p.add_subparsers(dest="cmd", required=True)

    gui = sub.add_parser("gui", help="启动图形安装器")
    gui.add_argument("--payload", required=True)
    sub.add_parser("find", help="自动查找可能的游戏目录")

    for name in ("check", "install", "uninstall"):
        sp = sub.add_parser(name)
        sp.add_argument("--game-dir", required=True)
        sp.add_argument("--payload", required=True)

    pv = sub.add_parser("verify", help="校验差分负载")
    pv.add_argument("--payload", required=True)

    sub.add_parser("licenses", help="显示第三方许可")

    args = p.parse_args()
    if args.cmd == "gui":
        sys.argv = ["patch_tool", "--payload", args.payload]
        entry.main()
    elif args.cmd == "find":
        cands = find_game()
        print(json.dumps([str(c) for c in cands], ensure_ascii=False, indent=2))
    elif args.cmd == "verify":
        sys.argv = ["patch_tool", "--payload", args.payload, "--verify-payload"]
        entry.main()
    elif args.cmd == "licenses":
        sys.argv = ["patch_tool", "--licenses"]
        entry.main()
    else:
        sys.argv = ["patch_tool", "--payload", args.payload, "--game-dir", args.game_dir, f"--{args.cmd}"]
        entry.main()


if __name__ == "__main__":
    main()
