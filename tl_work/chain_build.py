# -*- coding: utf-8 -*-
"""一键全链构建与核验（对齐 WoC tl_work/chain_build.py）：
  1) 检查 TSV 结构与占位符守恒（tl_work/chunks/*.tsv）
  2) build -> payload/（重建加密文本、动态字库、图片覆盖、Java 补丁）
  3) 19 步 CPU 回归测试（tests/run_cpu_regression.py）
  4) 明文读回核验（tl_tool.py verify-readback）
  5) 封签 payload/acceptance.json 并同步根 manifest.json

用法：
  python tl_work/chain_build.py            # dry-run：仅校验 TSV 与展示状态
  python tl_work/chain_build.py --apply    # 全链执行
"""
from __future__ import annotations

import hashlib
import json
from pathlib import Path
import subprocess
import sys

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / 'tools' / 'lib'))
from acceptance_checks import ACCEPTANCE_STATUS, validate_cpu_result  # noqa: E402
from output_paths import check_outputs, workspace_output  # noqa: E402

APPLY = "--apply" in sys.argv
NAMES = ("cosmobreeder-multi.jar", "patch.pak")


def _sha(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def run(cmd: list[str | Path]) -> int:
    print("$", " ".join(str(c) for c in cmd), flush=True)
    p = subprocess.run([str(c) for c in cmd], cwd=ROOT)
    return p.returncode


def seal_acceptance(payload_dir: Path) -> dict:
    check_outputs(payload_dir, ('acceptance.json',))
    manifest_path = payload_dir / "build-manifest.json"
    results_path = payload_dir / "test-results" / "results.json"
    build_info = json.loads(manifest_path.read_text("utf-8"))
    results_info = json.loads(results_path.read_text("utf-8"))

    if build_info.get("status") != "integrated_candidate_not_real_clip_CRT_input_acceptance":
        raise ValueError("build-manifest 状态未达标")
    archives = {n: _sha(payload_dir / n) for n in NAMES}
    validate_cpu_result(results_info, archives[NAMES[0]])
    if any(build_info.get('archives', {}).get(n, {}).get('sha256') != h for n, h in archives.items()):
        raise ValueError('候选归档与构建清单不匹配')
    acceptance = {
        "status": ACCEPTANCE_STATUS,
        "candidate": payload_dir.name,
        "source_mode": "tsv_chunks",
        "archives": archives,
        "build_manifest_sha256": _sha(manifest_path),
        "cpu_regression": {
            "steps": len(results_info["steps"]),
            "status": results_info["status"],
            "results_sha256": _sha(results_path),
        },
        "not_verified": [
            "游戏安装",
            "游戏启动",
            "GPU/CRT/裁剪渲染",
            "存档读写",
            "4 张位图的本地化",
        ],
        "game_started": False,
        "user_save_accessed": False,
    }
    (payload_dir / "acceptance.json").write_text(
        json.dumps(acceptance, ensure_ascii=False, indent=2) + "\n", encoding="utf-8"
    )
    return acceptance


def sync_root_manifest(payload_dir: Path, acceptance: dict):
    check_outputs(ROOT, ('manifest.json',))
    root_manifest = ROOT / "manifest.json"
    current = {}
    if root_manifest.is_file():
        current = json.loads(root_manifest.read_text("utf-8"))
    data = {
        "project": "CosmobreederYiffai-ChinesePatch",
        "version": current.get("version", "alpha0.3"),
        "installer_protocol": "alpha0.1",
        "game_version": "1.0.5_full",
        "payload_dir": "payload",
        "archives": {
            n: {
                "sha256": acceptance["archives"][n],
                "bytes": (payload_dir / n).stat().st_size,
            }
            for n in NAMES
        },
        "acceptance_status": acceptance["status"],
        "cpu_regression_steps": acceptance["cpu_regression"]["steps"],
        "notes": current.get("notes", []),
    }
    root_manifest.write_text(json.dumps(data, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")


def main() -> int:
    print("== 1) 检查 TSV 译文源与规则扫描 ==")
    rc = run([sys.executable, "tools/tl_tool.py", "status"])
    if rc != 0:
        return rc
    rc = run([sys.executable, "tools/review_tool.py", "scan"])
    if rc != 0:
        return rc

    if not APPLY:
        print("\n(dry-run 到此为止；如需完整构建与回归: python tl_work/chain_build.py --apply)")
        return 0

    print("\n== 2) build -> payload/ ==")
    rc = run([sys.executable, "tools/tl_tool.py", "build", "--output", "payload"])
    if rc != 0:
        return rc

    print("\n== 3) CPU 回归 ==")
    rc = run([sys.executable, "tests/run_cpu_regression.py", "--candidate", "payload", "--output", "payload/test-results"])
    if rc != 0:
        return rc

    print("\n== 4) 明文读回核验 ==")
    rc = run([sys.executable, "tools/tl_tool.py", "verify-readback", "--target", "payload"])
    if rc != 0:
        return rc

    print("\n== 5) 封签 acceptance.json 与同步 manifest.json ==")
    payload_dir = workspace_output(ROOT, 'payload', exact=('payload',))
    acceptance = seal_acceptance(payload_dir)
    sync_root_manifest(payload_dir, acceptance)
    print("== 全链完成: OK ==")
    return 0


if __name__ == "__main__":
    sys.exit(main())
