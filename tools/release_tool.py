# -*- coding: utf-8 -*-
"""差分发行包构建器：originals/ -> payload/ -> delta/ZIP/EXE + SHA256SUMS。

从原工具 tools/build_alpha_release.py 迁移而来，默认路径对齐 WoC 结构：
  --source originals   --target payload   --output dist/alpha0.X
保留原安装器源码、GUI 与 alpha0.1 备份还原状态协议。不安装也不启动游戏。
"""
from __future__ import annotations

import argparse
import json
import os
from pathlib import Path
import re
import shutil
import subprocess
import sys
import zipfile

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "src"))
sys.path.insert(0, str(ROOT / "tools" / "lib"))
from cosmobreeder_patch.delta import apply, build, sha  # noqa: E402
from cosmobreeder_patch.installer import NAMES, verify  # noqa: E402
from acceptance_checks import ACCEPTANCE_STATUS, LEGACY_ACCEPTANCE_STATUS, validate_cpu_result  # noqa: E402
from output_paths import workspace_output  # noqa: E402

LEGACY_BASELINE = 'r27-story12-shaderfix-test5'
LEGACY_TARGET_PINS = {
    'cosmobreeder-multi.jar': 'dc6b0cedc3a3b2f6f51941a2cef449d33ec87d314ee64ea63495c3ffdebd06be',
    'patch.pak': 'd2e21deeb85d74e981770b247625ee7ceb7ed39ae566305c1833c2c3d97b54d5',
}


def target_identity(target: Path):
    """验证目标归档已通过 CPU 回归与封签验收。"""
    manifest = target / "build-manifest.json"
    info = json.loads(manifest.read_text("utf-8")) if manifest.is_file() else {}
    actual = {n: sha(target / n) for n in NAMES}
    if info.get("version") != "r28-full-opt-candidate" and actual == LEGACY_TARGET_PINS:
        return {"baseline": LEGACY_BASELINE}, None
    acceptance = target / "acceptance.json"
    if not acceptance.is_file():
        raise ValueError("目标缺少已通过的验收记录 acceptance.json")
    record = json.loads(acceptance.read_text("utf-8"))
    if (
        not manifest.is_file()
        or record.get("status") not in {ACCEPTANCE_STATUS, LEGACY_ACCEPTANCE_STATUS}
        or record.get("archives") != actual
        or record.get("build_manifest_sha256") != sha(manifest)
        or info.get("full_component_set") is not True
        or info.get("version") != "r28-full-opt-candidate"
        or info.get("status") != "integrated_candidate_not_real_clip_CRT_input_acceptance"
        or any(info.get("archives", {}).get(n, {}).get("sha256") != actual[n] for n in NAMES)
    ):
        raise ValueError("验收状态或目标 SHA 不匹配")
    results_path = target / 'test-results/results.json'
    if not results_path.is_file() or record.get('cpu_regression', {}).get('results_sha256') != sha(results_path):
        raise ValueError('验收封签的 CPU 回归指纹不匹配')
    validate_cpu_result(json.loads(results_path.read_bytes()), actual[NAMES[0]])
    return {
        "baseline": target.name,
        "build_id": target.name,
        "candidate": True,
        "integration_baseline": LEGACY_BASELINE,
    }, acceptance


def native_font_notices(target: Path):
    """从已验收目标读取完整许可文本（不复制字体二进制）。"""
    sources = {"OFL8.txt": "OFL.txt", "NOTICE.txt": "NOTICE.txt"}
    components = (
        "boutique-bitmap-7x7/OFL.txt",
        "galmuri/LICENSE.txt",
        "misaki/misaki.txt",
        "miseki-bitmap/LICENSE.txt",
    )
    sources.update({"LICENSES8/" + n: "LICENSES/" + n for n in components})
    result = {}
    with zipfile.ZipFile(target / NAMES[0]) as z:
        for source, dest in sources.items():
            data = z.read("r28-font/" + source)
            data.decode("utf-8")
            result["fonts/native8/" + dest] = data
    return result


def exe_command(payload: Path, licenses: Path, notices: list[Path], output: Path, label: str = "alpha0.1"):
    work = output.resolve() / "build"
    notice_args = [arg for notice in notices for arg in ("--add-data", str(notice.resolve()) + ":.")]
    return [
        sys.executable, "-m", "PyInstaller", "--noconfirm", "--onefile", "--noupx",
        "--python-option", "X utf8", "--hide-console", "hide-early", *notice_args,
        "--name", "CosmobreederYiffai-" + label + "-setup",
        "--paths", str(ROOT / "src"),
        "--add-data", str(payload.resolve()) + ":payload",
        "--add-data", str(licenses.resolve()) + ":licenses",
        "--distpath", str(output.resolve()),
        "--workpath", str(work / "work"),
        "--specpath", str(work / "spec"),
        str(ROOT / "src/cosmobreeder_patch/__main__.py"),
    ]


def require_unchanged(pins: dict[Path, str]) -> None:
    for path, expected in pins.items():
        if sha(path) != expected:
            raise ValueError(f'打包输入在构建期间发生变化：{path}')


def main():
    p = argparse.ArgumentParser(description=__doc__)
    p.add_argument("--source", type=Path, default=ROOT / "originals")
    p.add_argument("--target", type=Path, default=ROOT / "payload")
    p.add_argument("--output", type=Path, required=True)
    p.add_argument("--exe", action="store_true")
    p.add_argument("--label", required=True, help="发行产物命名标签")
    a = p.parse_args()

    source_dir = (ROOT / a.source).resolve() if not a.source.is_absolute() else a.source.resolve()
    target_dir = (ROOT / a.target).resolve() if not a.target.is_absolute() else a.target.resolve()
    out_dir = workspace_output(ROOT, a.output, parents=('dist',))
    if source_dir == target_dir:
        raise ValueError('原版与目标归档需要使用不同的输入目录')
    if not re.fullmatch(r'[A-Za-z0-9][A-Za-z0-9._-]{0,63}', a.label):
        raise ValueError('发行标签只能包含字母、数字、点、连字符和下划线')

    if out_dir.exists():
        raise ValueError("输出目录已存在，拒绝覆盖；请指定新的 --output")

    source_pins = {n: sha(source_dir / n) for n in NAMES}
    target_pins = {n: sha(target_dir / n) for n in NAMES}
    target_records = [target_dir / name for name in ('build-manifest.json', 'acceptance.json', 'test-results/results.json')]
    metadata_pins = {p: sha(p) for p in target_records if p.is_file()}
    identity, acceptance = target_identity(target_dir)
    extra_notices = native_font_notices(target_dir) if acceptance else {}
    code_files = sorted((ROOT / "src/cosmobreeder_patch").glob("*.py"))
    code_pins = {f.name: sha(f) for f in code_files}
    notices = [ROOT / name for name in ("LICENSE", "NOTICE", "THIRD_PARTY_NOTICES.md")]
    license_root = ROOT / "licenses"
    required = (
        "fonts/OFL.txt", "fonts/NOTICE.txt",
        "fonts/LICENSES/ark-pixel/OFL.txt",
        "fonts/LICENSES/cubic-11/OFL.txt",
        "fonts/LICENSES/galmuri/LICENSE.txt",
        "runtime/Python-LICENSE.txt",
        "runtime/PyInstaller-COPYING.txt",
        "runtime/Tk-license.terms",
        "runtime/Tcl-license.terms",
    )
    license_files = sorted(p for p in license_root.rglob("*") if p.is_file())
    for notice in notices + [license_root / n for n in required]:
        if not notice.is_file():
            raise ValueError("缺少必要许可证: " + str(notice.relative_to(ROOT)))
    for notice in notices + license_files:
        if notice.is_symlink():
            raise ValueError("许可证不能为链接")
        notice.read_text("utf-8")
    pins = {
        **{source_dir / n: expected for n, expected in source_pins.items()},
        **{target_dir / n: expected for n, expected in target_pins.items()},
        **metadata_pins,
        **{f: code_pins[f.name] for f in code_files},
        **{f: sha(f) for f in notices + license_files},
    }

    payload = out_dir / "payload"
    payload.mkdir(parents=True)
    licenses = out_dir / "licenses"
    shutil.copytree(license_root, licenses)
    for name, data in extra_notices.items():
        dest = licenses / name
        if dest.exists():
            raise ValueError("附加许可不能覆盖既有文件: " + name)
        dest.parent.mkdir(parents=True, exist_ok=True)
        dest.write_bytes(data)
    if acceptance:
        shutil.copyfile(acceptance, out_dir / "acceptance.json")
    for notice in notices:
        shutil.copyfile(notice, out_dir / notice.name)

    m = {"version": "alpha0.1", "prerelease": True, **identity, "format": "CBDELTA1-COPY-XOR", "files": {}}
    report = {
        "builder_entry": "tools/release_tool.py",
        "installer_protocol": "alpha0.1",
        "baseline": identity["baseline"],
        "source_sha256": source_pins,
        "target_sha256": target_pins,
        "installer_source_sha256": code_pins,
        "native_font_notices": sorted(extra_notices),
        "reconstruction": {},
        "checks": [],
        "installed": False,
        "uninstalled": False,
        "game_started": False,
        "user_save_accessed": False,
    }
    for n in NAMES:
        e = build(source_dir / n, target_dir / n, payload / (n + ".cbd"))
        e["delta"] = n + ".cbd"
        m["files"][n] = e
        check = out_dir / (n + ".reconstruction-check")
        apply(source_dir / n, payload / e["delta"], check, e)
        if sha(check) != target_pins[n] or check.read_bytes() != (target_dir / n).read_bytes():
            raise ValueError("差分重建不等于冻结目标: " + n)
        report["reconstruction"][n] = "byte-for-byte-equal"
        check.unlink()

    (payload / "manifest.json").write_text(json.dumps(m, indent=2) + "\n", "utf-8", newline="\n")
    verify(payload)
    report["checks"].append({"name": "original-installer-payload-verification", "exit_code": 0})
    (out_dir / "README.md").write_text(
        f"# Cosmobreeder Yiffai 简体中文补丁（{a.label}）\n\n"
        f"依赖原版游戏文件的差分安装器，内容基线：`{identity['baseline']}`。\n\n"
        "支持 `1.0.5_full` 原版 SFW（仅 JAR）与官方 NSFW 补丁（JAR+PAK）；未知源拒绝修改。\n"
        "EXE 内置 Python，无需另装；Python ZIP 需要 Python 3.12。本构建仅作离线负载校验。\n\n"
        f"```text\nCosmobreederYiffai-{a.label}-setup.exe --verify-payload\n"
        f"CosmobreederYiffai-{a.label}-setup.exe --licenses\n```\n",
        encoding="utf-8",
    )

    zip_path = out_dir / f"CosmobreederYiffai-{a.label}-python.zip"
    with zipfile.ZipFile(zip_path, "w", zipfile.ZIP_DEFLATED) as z:
        for f in code_files:
            z.write(f, "cosmobreeder_patch/" + f.name)
        for f in payload.iterdir():
            z.write(f, "cosmobreeder_patch/payload/" + f.name)
        for f in licenses.rglob("*"):
            if f.is_file():
                z.write(f, "cosmobreeder_patch/licenses/" + f.relative_to(licenses).as_posix())
        for notice in notices:
            z.write(notice, "cosmobreeder_patch/" + notice.name)
        for name in ("README.md", "acceptance.json"):
            if (out_dir / name).is_file():
                z.write(out_dir / name, "cosmobreeder_patch/" + name)

    if a.exe:
        work = out_dir.resolve() / "build"
        (work / "spec").mkdir(parents=True)
        env = dict(os.environ, PYINSTALLER_CONFIG_DIR=str(work / "cache"), PYTHONDONTWRITEBYTECODE="1")
        env.pop("PYTHONPATH", None)
        with open(work / "pyinstaller.log", "wb") as log:
            subprocess.run(exe_command(payload, licenses, notices, out_dir, a.label), cwd=ROOT, env=env, stdout=log, stderr=subprocess.STDOUT, check=True)
        exe = (out_dir / f"CosmobreederYiffai-{a.label}-setup.exe").resolve()
        env["PATH"] = str(Path(os.environ.get("SystemRoot", "C:/Windows")) / "System32")
        for key in ("PYTHONPATH", "PYTHONHOME", "PYTHONUTF8", "PYTHONIOENCODING"):
            env.pop(key, None)
        for action in ("--verify-payload", "--licenses"):
            result = subprocess.run([str(exe), action], cwd=work, env=env, capture_output=True, check=True)
            (work / (action[2:] + ".stdout.txt")).write_bytes(result.stdout)
            (work / (action[2:] + ".stderr.txt")).write_bytes(result.stderr)
            text = result.stdout.decode("utf-8").replace("\r\n", "\n")
            if action == "--verify-payload":
                if json.loads(text) != {"version": "alpha0.1", "status": "verified", "game_started": False}:
                    raise ValueError("EXE 负载验证返回异常")
            else:
                for path in notices + sorted(p for p in licenses.rglob("*") if p.is_file()):
                    key = path.name if path in notices else path.relative_to(out_dir).as_posix()
                    if key not in text or path.read_text("utf-8") not in text:
                        raise ValueError("EXE 许可显示不完整: " + key)
            report["checks"].append({"name": action, "exit_code": result.returncode})
        report["exe_sha256"] = sha(exe)
        report["exe_name"] = exe.name

    require_unchanged(pins)
    if sorted((ROOT / 'src/cosmobreeder_patch').glob('*.py')) != code_files:
        raise ValueError('安装器源码文件范围在构建期间发生变化')
    report.update(status="passed-original-tool-build-no-install", installer_source_unmodified=True)
    (out_dir / "build-report.json").write_text(json.dumps(report, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    lines = [sha(f) + "  " + f.relative_to(out_dir).as_posix() for f in sorted(out_dir.rglob("*")) if f.is_file()]
    (out_dir / "SHA256SUMS").write_text("\n".join(lines) + "\n", "utf-8", newline="\n")
    print(f"Release OK -> {out_dir.relative_to(ROOT)}")


if __name__ == "__main__":
    main()
