# docs/workflows —— Cosmobreeder Yiffai 中文补丁工作流文档

本目录说明如何导出译文、审校场景、维护图集、构建与打包补丁。
项目概况与玩家说明见根目录 [README.md](../../README.md)；项目交接与最新状态见 [接续.md](../接续.md)。

## 工作流索引

| 文档 | 覆盖范围 | 何时使用 |
| --- | --- | --- |
| [translation.md](translation.md) | TSV 译文源格式、导出与重建、转义与 U+2028 规范 | 修改任何译文或重新导出语料前 |
| [review.md](review.md) | 术语表 `review/terms.tsv`、`review_tool.py` 检查、同文异译、待办管理 | 校对、术语统一、批量修订、质量核查 |
| [images.md](images.md) | 已落地的 79 个图集区域覆盖与待处理的 4 个变体 | 维护或新增图像本地化 |
| [build-release.md](build-release.md) | `chain_build.py` 全链构建、19 步 CPU 回归、`release_tool.py` 差分打包 | 每次修改后验证与发版 |

## 全局纪律

1. **只改 TSV，不直改归档**：所有文本修改在 `tl_work/chunks/*.tsv`（或 `review/sheet_*.tsv`）完成，`payload/` 永远由 `tl_tool.py build` 重建生成。
2. **批量修改先 dry-run**：`review_tool.py terms` 与 `apply` 默认 dry-run，核对后再 `--apply` / `--write`。
3. **译文改动走全链**：执行 `python tl_work/chain_build.py --apply`，核对构建、CPU 回归和明文读回。
4. **实机与 CPU 分开报告**：CPU 回归不替代游戏安装、启动、GPU/CRT 渲染与存档读写验证；严禁擅自写入用户真实游戏目录或读取真实存档。
