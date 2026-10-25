# -*- coding: utf-8 -*-
"""把已构建好的包准备成可打包的形态：payload/ + manifest.json。

    python localization/packaging/prepare.py --build builds/final-8146-r11-images

只做两件事：
  1. 把 jar / pak 复制进 packaging/payload/
  2. 按 patch_tool 期望的格式写 manifest.json（含原版哈希，用于安装前校验版本）

不调 PyInstaller，打包另跑：pyinstaller CosmobreederYiffaiCN.spec
"""
import argparse
import hashlib
import io
import json
import os
import shutil
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
LOC = os.path.dirname(HERE)

VERSION = "1.0"
BUILT = "2026-10-24"


def sha256(path):
    h = hashlib.sha256()
    with open(path, "rb") as f:
        for chunk in iter(lambda: f.read(1 << 20), b""):
            h.update(chunk)
    return h.hexdigest()


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--build", required=True, help="builds/ 下的包目录，含 jar 与 pak")
    ap.add_argument("--version", default=VERSION)
    a = ap.parse_args()

    build = os.path.abspath(a.build)
    if not os.path.isdir(build):
        sys.exit("找不到构建目录：%s" % build)

    pm_path = os.path.join(build, "package-manifest.json")
    if not os.path.isfile(pm_path):
        sys.exit("构建目录里没有 package-manifest.json，无法确认原版哈希")
    pm = json.load(io.open(pm_path, encoding="utf-8"))

    originals = {o["tag"]: o for o in pm["originals"]}
    archives = {x["archive"]: x for x in pm["archives"]}

    payload = os.path.join(HERE, "payload")
    os.makedirs(payload, exist_ok=True)

    files = []
    mapping = [("cosmobreeder-multi.jar", "jar"), ("patch.pak", "patch")]
    for name, tag in mapping:
        src = os.path.join(build, name)
        if not os.path.isfile(src):
            sys.exit("构建目录缺少 %s" % name)
        dst = os.path.join(payload, name)
        shutil.copy2(src, dst)
        h, size = sha256(dst), os.path.getsize(dst)
        expect = archives.get(name, {}).get("sha256")
        if expect and h != expect:
            sys.exit("%s 复制后哈希与 package-manifest 不一致" % name)
        orig = originals[tag]
        files.append({
            "path": name,
            "payload": name,
            "sha256": h,
            "size": size,
            "original": {"sha256": orig["sha256"], "size": orig["bytes"]},
        })
        print("  %-26s %8.1f MB  已复制" % (name, size / 1048576.0))

    jar_e, pak_e = files[0], files[1]
    man = {
        "name": "Cosmobreeder Yiffai 简体中文补丁",
        "game": "Cosmobreeder Yiffai (Steam)",
        "version": a.version,
        "built": BUILT,
        "variants": {
            "nsfw": {
                "label": "NSFW 版（游戏里已装官方 patch.pak）",
                "detect": {"patch.pak": {"sha256": pak_e["original"]["sha256"]}},
                "available": True,
                "files": [jar_e, pak_e],
            },
            "vanilla": {
                "label": "本体版（游戏里没有 patch.pak）",
                "detect": {"patch.pak": {"absent": True}},
                "available": True,
                "files": [jar_e],
            },
        },
        "notes": [
            "官方本体和官方 NSFW 补丁都叫 patch.pak，安装器按文件在不在、哈希对不对自动选版本。",
            "jar 里同时含两种版本需要的文本，装了 patch.pak 的走 pak，没装的走 jar。",
            "只修改 cosmobreeder-multi.jar（以及 NSFW 版下的 patch.pak）。",
            "安装前会把原版备份到游戏目录下的 _汉化补丁备份\，卸载时还原。",
            "不写注册表，不动存档。",
        ],
    }
    out = os.path.join(HERE, "manifest.json")
    with io.open(out, "w", encoding="utf-8") as f:
        json.dump(man, f, ensure_ascii=False, indent=1)
    print("wrote", out)
    print("payload 合计 %.1f MB" % (sum(x["size"] for x in files) / 1048576.0))
    return 0


if __name__ == "__main__":
    sys.exit(main())
