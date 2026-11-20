# -*- coding: utf-8 -*-
"""19 步 JVM CPU 回归测试（不启动游戏、不调用 GL、不访问存档）。

用法：
  python tests/run_cpu_regression.py [--candidate payload] [--output payload/test-results]
"""
from __future__ import annotations

import argparse
import hashlib
import json
import os
from pathlib import Path
import re
import shutil
import subprocess
import sys
import zipfile

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "tools" / "lib"))

from build_story_font12 import wide  # noqa: E402
from codec import decrypt_file  # noqa: E402
from output_paths import check_outputs, workspace_output  # noqa: E402
from pattern_ink import export as export_pattern_ink  # noqa: E402

JDK = ROOT / "deps" / "jdk17" / "bin"
JRE = ROOT / "deps" / "jre" / "bin" / "java.exe"
EXPORTS = [
    "--add-exports", "java.base/jdk.internal.org.objectweb.asm=ALL-UNNAMED",
    "--add-exports", "java.base/jdk.internal.org.objectweb.asm.tree=ALL-UNNAMED",
]
TEST_NAMES = [
    "PixelLayoutTest",
    "DialogueGridTest",
    "DialogueWrapTest",
    "ContinueWrapTest",
    "SubtitleLayoutTest",
    "PatternSymbolsTest",
]


def main():
    p = argparse.ArgumentParser(description=__doc__)
    p.add_argument("--candidate", type=Path, default=Path("payload"))
    p.add_argument("--output", type=Path, default=Path("payload/test-results"))
    p.add_argument("--diagnostic-continue", action="store_true")
    a = p.parse_args()

    candidate = (ROOT / a.candidate).resolve() if not a.candidate.is_absolute() else a.candidate.resolve()
    out = workspace_output(ROOT, a.output, parents=('payload', 'build'))
    if candidate == out or candidate.is_relative_to(out):
        raise ValueError('回归输出不能覆盖候选归档')
    if not (candidate / "build-manifest.json").is_file():
        raise ValueError(f"缺少 build-manifest.json: {candidate}")

    if out.exists():
        if out != ROOT / 'payload/test-results':
            raise FileExistsError('隔离回归需要新的输出子目录')
        check_outputs(out, ('.cpu-regression-output', 'results.json'))
        marker = out / '.cpu-regression-output'
        if not marker.is_file():
            previous = json.loads((out / 'results.json').read_text('utf-8'))
            if 'candidate_sha256' not in previous or not isinstance(previous.get('steps'), list):
                raise ValueError('回归输出目录不是以前的回归产物')
        shutil.rmtree(out)

    out.mkdir(parents=True)
    (out / '.cpu-regression-output').touch(exist_ok=False)
    for name in ("classes", "tools", "fonts", "vsn", "logs"):
        (out / name).mkdir()

    jar = candidate / "cosmobreeder-multi.jar"
    base = ROOT / "deps" / "r27-base" / "cosmobreeder-multi.jar"
    result = {
        "status": "running_cpu_only",
        "candidate_sha256": hashlib.sha256(jar.read_bytes()).hexdigest(),
        "steps": [],
        "game_started": False,
        "user_save_accessed": False,
    }

    def save():
        (out / "results.json").write_text(json.dumps(result, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")

    def run_step(name: str, args: list[str | Path]):
        r = subprocess.run([str(x) for x in args], cwd=ROOT, stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
        (out / "logs" / f"{name}.log").write_bytes(r.stdout)
        result["steps"].append({"name": name, "exit_code": r.returncode})
        save()
        print(f"  [{name}] exit {r.returncode}", flush=True)
        if r.returncode != 0:
            result["status"] = "failed_cpu_only"
            save()
            if not a.diagnostic_continue or name in ("compile-tests", "compact-inputs", "compact-compile"):
                raise RuntimeError(f"测试步骤失败，请查看 {out / 'logs' / (name + '.log')}")

    with zipfile.ZipFile(jar) as z:
        extended = {"PRG/CompactFields.class", "PRG/SceneText.class"} <= set(z.namelist())
        radio = "PRG/RadioLabels.class" in z.namelist()
        for name in ("bbc2.fnt", "classic.fnt", "story12.fnt", "dingbats.fnt"):
            (out / "fonts" / name).write_bytes(z.read(name))
        (out / "fonts" / "bbc2-10px.fnt").write_bytes(z.read("bbc2.fnt"))

    vsn = []
    census = {"commands": 0, "han_commands": 0, "han": 0}
    for archive, variant in (("cosmobreeder-multi.jar", "sfw"), ("patch.pak", "nsfw")):
        with zipfile.ZipFile(candidate / archive) as z:
            (out / f"dictionary-{variant}.json").write_bytes(decrypt_file(z.read("datav/1")))
            for dentry in ("datadf/1", "datadm/1"):
                (out / f"ds-{variant}-{dentry.split('/')[0]}.txt").write_bytes(decrypt_file(z.read(dentry)))
            index = json.loads(decrypt_file(z.read("vsn/0")))
            for logical, value in sorted(index.items()):
                if not logical.endswith("/script.vsn"):
                    continue
                scene = logical.strip("/").split("/")[-2]
                raw = decrypt_file(z.read("vsn/" + str(value)))
                path = out / "vsn" / f"{variant}-{scene}.txt"
                path.write_bytes(raw)
                vsn.append(f"{variant}\t{scene}\t{path}")
                for line in raw.decode("utf-8").splitlines():
                    m = re.match(r"^lang\((Fox|HardFox)\):\s?(.*)$", line)
                    if m:
                        census["commands"] += 1
                        cnt = sum(0x3400 <= ord(c) <= 0x9FFF for c in m[2])
                        census["han"] += cnt
                        census["han_commands"] += bool(cnt)

    (out / "vsn.tsv").write_text("\n".join(vsn) + "\n", encoding="utf-8")
    (out / "pattern-census.properties").write_text(
        "".join(f"{k}={v}\n" for k, v in census.items()), encoding="utf-8"
    )
    result["independent_pattern_census"] = census
    result["actual_archive_script_inputs"] = len(vsn)
    save()

    result["pattern_ink"] = export_pattern_ink(jar, base, out)
    save()

    java_dir = ROOT / "tests" / "java"
    sources = [java_dir / f"{name}.java" for name in TEST_NAMES] + [java_dir / "CoreRegression.java"]
    if extended:
        sources.extend(java_dir / f"{name}.java" for name in ("SceneTextTest", "EndingReportLayoutTest", "StoryFont12Test"))
        sources.append(java_dir / "BridgePatch.java")
        sources.append(java_dir / "ShopTextTest.java")
        sources.append(java_dir / "DsParseTest.java")
    if radio:
        sources.append(java_dir / "RadioLabelsTest.java")

    snapshot_sources = list(sources)
    if extended:
        snapshot_sources.extend([
            java_dir / "CpuEvidence.java",
            java_dir / "CompactFieldsCpuTest.java",
            java_dir / "compact" / "prepare_inputs.py",
            java_dir / "compact" / "render_compact.py",
        ])
    result["test_source_sha256"] = {
        str(p.relative_to(ROOT)).replace("\\", "/"): hashlib.sha256(p.read_bytes()).hexdigest()
        for p in snapshot_sources
    }
    save()

    cp = os.pathsep.join([str(jar), str(candidate / "tools")])
    run_step("compile-tests", [JDK / "javac.exe", *EXPORTS, "-encoding", "UTF-8", "-cp", cp, "-d", out / "classes", *sources])
    vm = [JRE, "-Dfile.encoding=UTF-8", "-Xverify:all", *EXPORTS, "-cp", os.pathsep.join([str(jar), str(out / "classes"), str(candidate / "tools")])]

    if radio:
        run_step("radio-labels", [*vm, "RadioLabelsTest", base, jar, out / "fonts/classic.fnt"])
    run_step("core-regression", [*vm, "CoreRegression", base])
    run_step("pixel-layout", [*vm, "PixelLayoutTest"])
    run_step("dialogue-grid", [*vm, "DialogueGridTest"])
    run_step("dialogue-wrap", [*vm, "DialogueWrapTest", out / "fonts/bbc2.fnt", java_dir / "fixtures/joined.tsv"])
    run_step("continue", [*vm, "ContinueWrapTest", out / "fonts/bbc2.fnt"])
    run_step("subtitle", [*vm, "SubtitleLayoutTest", out / "fonts/bbc2.fnt", out / "vsn.tsv", "--pattern-symbols", out / "pattern-ink.properties"])
    run_step("pattern", [*vm, "PatternSymbolsTest", out / "vsn.tsv", out / "fonts/dingbats.fnt", out / "fonts/story12.fnt", out / "fonts/bbc2.fnt", out / "pattern-census.properties"])

    if extended:
        run_step("ending-sfw", [*vm, "EndingReportLayoutTest", out / "fonts/classic.fnt", out / "dictionary-sfw.json"])
        run_step("ending-nsfw", [*vm, "EndingReportLayoutTest", out / "fonts/classic.fnt", out / "dictionary-nsfw.json"])
        scene_vm = [
            JRE, "-Dfile.encoding=UTF-8",
            f"-Dscenes.report={out / 'breeding-corpus.json'}",
            "-Xverify:all", *EXPORTS, "-cp",
            os.pathsep.join([str(out / "classes"), str(jar), str(candidate / "tools")]),
        ]
        run_step("scenes", [*scene_vm, "SceneTextTest", "--candidate", jar, out / "fonts", out / "dictionary-sfw.json", out / "dictionary-nsfw.json"])
        build = json.loads((candidate / "build-manifest.json").read_text("utf-8"))
        native_count = 2312 + sum(wide(cp_val) for cp_val in build["font_manifest"]["roles"]["story12"]["added_ids"])
        run_step("story12-lifecycle", [*vm, "StoryFont12Test", "--cpu", out / "fonts", str(native_count)])

        run_step("shop-text", [*vm, "ShopTextTest", base, jar])
        run_step("ds-parse", [*vm, "DsParseTest", jar,
            out / "ds-sfw-datadf.txt", out / "ds-sfw-datadm.txt",
            out / "ds-nsfw-datadf.txt", out / "ds-nsfw-datadm.txt"])

        compact = out / "compact"
        compact.mkdir()
        (compact / "classes").mkdir()
        compact_root = java_dir / "compact"
        run_step("compact-inputs", [sys.executable, "-B", compact_root / "prepare_inputs.py", "--pak-json", out / "dictionary-nsfw.json", "--jar-json", out / "dictionary-sfw.json", "--output-dir", compact])
        compact_sources = [java_dir / "CpuEvidence.java", java_dir / "CompactFieldsCpuTest.java"]
        run_step("compact-compile", [JDK / "javac.exe", "-encoding", "UTF-8", "-source", "8", "-target", "8", "-cp", jar, "-d", compact / "classes", *compact_sources])
        run_step("compact-cpu", [JRE, "-Dfile.encoding=UTF-8", "-Xverify:all", "-cp", os.pathsep.join([str(jar), str(compact / "classes")]), "PRG.CompactFieldsCpuTest", jar, jar, compact])
        run_step("compact-pixels", [sys.executable, "-B", compact_root / "render_compact.py", jar, "--output-dir", compact])

    result["test_sources_unchanged_after_run"] = all(
        hashlib.sha256((ROOT / n).read_bytes()).hexdigest() == h
        for n, h in result["test_source_sha256"].items()
    )
    if not result["test_sources_unchanged_after_run"]:
        raise RuntimeError("测试源码在运行期间发生变化")
    if any(step["exit_code"] for step in result["steps"]):
        result["status"] = "failed_cpu_only"
        save()
        raise RuntimeError("存在失败的测试步骤，请检查 results.json")
    result["status"] = "passed_cpu_only_not_real_clip_CRT_input"
    save()
    print(f"CPU Regression OK ({len(result['steps'])} steps) -> {out.relative_to(ROOT)}")


if __name__ == "__main__":
    main()
