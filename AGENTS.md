# 项目维护入口

《Cosmobreeder Yiffai》简体中文补丁（本地仓库，结构对齐 `WoC-ChinesePatch`）。目标是让 Steam 版游戏的剧情、无线电、UI、道具与结局能连续读成通顺中文，同时不改动玩法条件、施受关系、信息揭示顺序与保护字段。

## 目录结构（WoC 对齐版）

| 目录/文件 | 角色 | Git |
| --- | --- | --- |
| `originals/` | 原版游戏文件（`cosmobreeder-multi.jar`、`patch.pak`、`archives.json`） | 忽略 |
| `deps/` | 外部依赖与冻结底座（`jdk17/`、`jre/`、`r27-base/`、`fonts/`） | 忽略 |
| `payload/` | 构建产物与 19 步回归结果（`cosmobreeder-multi.jar`、`patch.pak`、`acceptance.json`） | 忽略 |
| `dist/` | 差分安装器发行包（`alpha0.3/` 等） | 忽略 |
| `src/` | 安装器包（`cosmobreeder_patch/`）与 Java 运行时/字节码补丁源码（`java/`） | 追踪 |
| `assets/` | 79 组图集覆盖片与白名单掩码；原版参考切片仅本地保存 | 覆盖片、遮罩和清单追踪 |
| `tools/` | 统一命令行工具：`tl_tool.py`、`review_tool.py`、`patch_tool.py`、`release_tool.py` 及 `lib/` | 追踪 |
| `tl_work/` | `chain_build.py` 构建入口；`chunks/` 与 `template/` 为本地导出，历史双语台账保留在本地及旧提交 | 构建入口追踪 |
| `review/` | 术语、人物、覆盖范围和不含原文列的公开校对索引 | 规则、清单和公开索引追踪；扫描与历史双语材料忽略 |
| `tests/` | 发布单测 `tests/release/` 与 19 步 JVM 回归 `tests/run_cpu_regression.py` | 追踪 |
| `docs/` | 工作流 `workflows/`、技术参考 `reference/`、发版说明 `release-notes/`、交接 `接续.md` | 追踪 |
| `manifest.json` | 当前构建身份与校验清单 | 追踪 |

## 核心工作流（4 条命令复现）

```cmd
python tools\tl_tool.py export --target payload           :: 1) 首次准备本地译文分块与模板
python tools\review_tool.py scan                         :: 2) 规则预筛 -> review/findings.md（另支持 stats/terms/dedupe/export/apply）
python tl_work\chain_build.py --apply                    :: 3) 构建 + 19 步 CPU 回归 + 明文读回 + 封签
python tools\release_tool.py --label alpha0.4-scene-audit --output dist\alpha0.4-scene-audit-local --exe
```

## 维护约定与安全边界

- **只改 TSV，不直改归档**：文本修改在 `tl_work/chunks/*.tsv` 或 `review/sheet_*.tsv` 完成，由 `tl_work/chain_build.py --apply` 重建并验证 `payload/`。
- **不擅自安装或启动游戏**：脚本与构建严格隔离，不写入 Steam 真实游戏目录、不启动游戏、不访问用户存档；实机验证由用户执行。
- **本机 Python 入口**：构建、回归与打包一律使用系统 Python 3.12（避免 DSH 沙箱内捆绑 Python 写盘权限受限）。
- **依赖方向**：全链入口编排 `tools/` 和测试；工具调用 `tools/lib/` 与安装器，底层不反向依赖 CLI。Java 运行时适配器与字节码 patcher 分开，唯一组件清单为 `src/java/config/components.json`。
- **容器与规则关键事实**：
  - 故事框走 `StoryFont12`（240px / 12px 字，每页 3 行；非宽字符 `yoffset` 已相对原版下移 `+4` 对齐汉字基线）；无线电与 `<TomcatItems.*>` / `<BossuDex.*>` 物品说明走 `DialogueWrap.radio`（150px / `bbc2` 10px 字，每行 15 汉字）。
  - `vsn/` 演出脚本词法不接受 `U+2028`（`⏎`），软断行只允许用于 `dialogue/`。
  - 全量校对与工作区验收见[场景审查台账](review/scene-context-audit.md)；剩余实机检查见[待办清单](review/worklist.md)。

## 索引

- 工作流总览：[docs/workflows/README.md](docs/workflows/README.md)（[翻译](docs/workflows/translation.md) · [校对](docs/workflows/review.md) · [图像](docs/workflows/images.md) · [构建发布](docs/workflows/build-release.md)）
- 交接与状态：[docs/接续.md](docs/接续.md) · [review/worklist.md](review/worklist.md)
- 发行说明：[alpha0.3](docs/release-notes/alpha0.3.md) · [alpha0.2](docs/release-notes/alpha0.2.md) · [alpha0.1](docs/release-notes/alpha0.1.md)
