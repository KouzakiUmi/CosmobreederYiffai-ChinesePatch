# Cosmobreeder Yiffai 简体中文补丁

**《Cosmobreeder Yiffai》的非营利性简体中文汉化补丁，仅面向 PC（Steam）版。**

![Status](https://img.shields.io/badge/Status-Alpha-orange?style=flat-square)
![Platform](https://img.shields.io/badge/Platform-Windows-blue?style=flat-square)
![Engine](https://img.shields.io/badge/Engine-Java%2017%20%2B%20libGDX-blueviolet?style=flat-square)
![License](https://img.shields.io/badge/License-CC%20BY--NC--SA%204.0-lightgrey?style=flat-square)

> **By KouzakiUmi (呜咪 / 神前海)**

---

**项目说明**：本补丁覆盖开场、剧情字幕、无线电、Continue 窄栏、道具与结局报告，并为每类场景单独适配 12px / 10px / classic8 像素字体与换行宽度。发行物是**依赖原文件的二进制差分**（`CBDELTA1-COPY-XOR`），不携带完整替换 JAR/PAK、游戏图片音频、原游戏 JRE 或存档。

| 项目 | 说明 |
| --- | --- |
| 适用游戏 | Cosmobreeder Yiffai `1.0.5_full`（Windows），原版 SFW（JAR）或官方 NSFW 补丁（JAR+PAK） |
| 游戏引擎 | Java 17 + libGDX（混淆于 `PRG/*`），Scala 3 / FMOD / Steamworks4J |
| 基线校验 | `cosmobreeder-multi.jar` sha256 `cd37e445...`；可选 `patch.pak` `2f9da7d4...` |
| 当前预发行版 | [alpha0.4-scene-audit](https://github.com/KouzakiUmi/CosmobreederYiffai-ChinesePatch/releases/tag/alpha0.4-scene-audit) |
| 运行要求 | Windows 独立 EXE 无需 Python；Python 运行版需要 Python 3.12 |
| 校对范围 | 九份可编辑译文共 16,545 条，按场景、角色路线与分支对读；修订 13,417 条 |

从[预发行页](https://github.com/KouzakiUmi/CosmobreederYiffai-ChinesePatch/releases/tag/alpha0.4-scene-audit)下载 Windows 安装器或 Python 备用包。已通过 19 步 CPU 回归、113 项资源明文读回和安装器负载检查；游戏内显示与安装卸载仍待实机验证。

---

## 📁 目录结构

```text
CosmobreederYiffai-ChinesePatch/
├── originals/          # [本地] 原版 JAR/PAK（gitignored）
├── deps/               # [本地] JDK17 / JRE / r27 底座 / 开源字体源码（gitignored）
├── payload/            # [本地] 目标归档与 19 步回归报告（gitignored）
├── dist/               # [本地] 发行差分安装包 EXE / ZIP（gitignored）
├── src/
│   ├── cosmobreeder_patch/   # 安装器、CBDELTA1 差分、GUI 与 Steam 探测
│   └── java/                 # Java 8 运行时排版适配器与 ASM 字节码补丁
├── assets/images/      # 79 组 UI 图集局部覆盖及白名单遮罩
├── tools/
│   ├── tl_tool.py      # 导出(export) / 构建(build) / 状态(status) / 回验(verify-readback)
│   ├── review_tool.py  # 统计(stats) / 扫描(scan) / 术语(terms) / 查重(dedupe) / 审校表(export/apply)
│   ├── patch_tool.py   # 安装 / 还原 / 校验 / 查找游戏目录统一入口
│   ├── release_tool.py # 差分包 EXE / ZIP 构建器
│   └── lib/            # Salsa20 加解密、字体/图像生成等底层库
├── tl_work/
│   ├── chain_build.py  # TSV 校验 → 构建 → 19 步 CPU 回归 → 明文读回 → 同步封签
│   ├── chunks/         # [导出生成] dialogue/ vsn/ ui/ 可编辑 TSV 分块（唯一文本源）
│   └── archive/        # [本地] 历史审校材料；旧版本可从 Git 历史查阅
├── review/
│   ├── terms.tsv       # 7 列统一术语规则表
│   ├── worklist.md     # 待办与实机已知缺陷清单
│   ├── scene-context-changes.jsonl # 公开校对索引（不含原文列）
│   └── findings.md     # [本地] review_tool.py scan 扫描报告
├── tests/
│   ├── release/        # 安装器与差分协议单元测试
│   └── run_cpu_regression.py # 19 步 JVM CPU 回归
└── docs/
    ├── workflows/      # 翻译、校对、图像、构建发版四条标准工作流
    ├── reference/      # 容器规则、渲染研究与历史技术报告
    ├── release-notes/  # alpha0.1 / alpha0.2 / alpha0.3 发行说明
    └── 接续.md         # 维护与恢复交接指南
```

---

## ⚙️ 快速恢复与日常工作流（维护者）

```cmd
:: 1. 首次恢复时从 originals/ 和现有目标导出可编辑 TSV
python tools\tl_tool.py export --target payload

:: 2. 校对与质量检查
python tools\review_tool.py scan
python tools\review_tool.py terms
python tools\review_tool.py dedupe

:: 3. 改完译文后构建，执行 19 步 CPU 回归和明文读回
python tl_work\chain_build.py --apply

:: 4. 跑通发布单测并生成差分安装包
python -m unittest discover -s tests/release -v
python tools\release_tool.py --source originals --target payload --output dist\alpha0.4-scene-audit-local --label alpha0.4-scene-audit --exe
```

详细操作规范见 [工作流文档索引](docs/workflows/README.md) 与 [交接说明](docs/接续.md)。新检出的仓库需准备本地原版、已还原的译文归档及构建依赖；[导出与复核方法](docs/workflows/translation.md#核对全量场景校对版)说明如何检查导出的译文是否与发行版一致。

---

## ⚠️ 版权与许可

- 原作《Cosmobreeder Yiffai》及其代码、美术、音频、剧情与原版位图字体权利归原权利人所有；本项目与原作者无隶属或背书关系。
- 仓库与发行物不含任何完整游戏归档、原游戏 JRE 或存档。
- **字体**：新增中文字体贡献来自 [Fusion Pixel Font](https://github.com/TakWolf/fusion-pixel-font) 2026.10.16（**SIL OFL 1.1**），完整许可文本见 [licenses/](licenses/)、[NOTICE](NOTICE) 与 [THIRD_PARTY_NOTICES.md](THIRD_PARTY_NOTICES.md)。
- **许可证**：[CC BY-NC-SA 4.0](https://creativecommons.org/licenses/by-nc-sa/4.0/deed.zh-hans)（全文见 [LICENSE](LICENSE)）。
