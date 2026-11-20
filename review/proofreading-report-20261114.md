# 全量上下文校对报告（2026-11-14）

针对“单句过于孤立、缺乏上下文语气与连贯性”的问题，按 `scene` 连续场景分组对全库 9 个 TSV 分块进行了全量通读校对与跨档位一致性对齐。

## 一、校对范围与修改统计

| 工作包 | 覆盖范围 | 原文行数 | 采纳修改 | 说明 |
| --- | --- | ---: | ---: | --- |
| 包 1 | `pak_vsn` 前半（开场、F01–F08、FZ1–FZ6、Classic*） | 1,224 | 46 | 顺畅语气、修复口癖/长老文风、清光击枪残留 |
| 包 2 | `pak_vsn` 后半 + `jar_vsn` 差异 | 1,419 | 42 | 统一开场航电、修残句与“俺”口癖、清光击枪 |
| 包 3 | `pak_datadf` 前半（区域商店/救援/BossuDex 前半） | 1,449 | 54 | 补齐对话承接、修 `⏎` 行首标点与旧人名“伊法伊” |
| 包 4 | `pak_datadf` 后半（BossuDex 后半/TomcatItems/DefeatHints） | 1,445 | 45 | 润色无线电吐槽节奏、清“光电击枪/反重力踝环” |
| 包 5 | `pak_datadm` 前半 | 1,456 | 28 | 男线口气顺接、统一 `ClassicMine*` 双关、清“伊法” |
| 包 6 | `pak_datadm` 后半 | 1,456 | 89 | 拆词断行清理、人称/性别指代、清“光电击枪/踝环” |
| 包 7 | UI 词典、卡面、图鉴、成就与任务日志 | 1,292 | 52 | 卡面 16 列超宽收束、背景故事连贯化、芬芬/通讯统一 |
| 包 8 | SFW（`jar`）独有/差异对白 | 1,308 | 152 | SFW 专属语境润色、区分 `space suit` 太空服、清残留 |
| 自动同步 + 扫描收尾 | 同源 `(scene, prefix, source)` 同步到 `jar` + 剩余 6 条扫描修复 | — | 289 | 含 283 条 `pak→jar` 自动同步、4 条 `lighttazer`、2 条 `⏎` 标点 |

- **合计采纳**：**797 处正文修订**（`rejected: 0`）。

## 二、同步清理的质量指标

- `term:anti-grav anklet`（反重力踝环 → 反重力脚环）：4 → **0**
- `term:lighttazer`（光电击枪/轻型电击枪 → 光击枪）：32 → **0**
- `explicit_line_head_punct`（显式 `⏎` 后接禁止行首标点）：14 → **0**
- `m_GameStart`（`等不及批准` → `没法等批准`）：SFW/NSFW 双档位已落地
- 旧人名残留（`伊法伊` / `伊法……伊` / `Fenfen`）：已清零

## 三、构建与验证结果

- `python tl_work/chain_build.py --apply`：全链 exit 0（`compile-runtime` / `compile-tools` / `patch-targets` / `verify-final-classes`、**17 步独立 JVM CPU 回归全 exit 0**、`tl_tool.py verify-readback` 校验 113 个加密资源 0 差异）。
- `python -m unittest discover -s tests/release -v`：42 passed, 5 opt-in skipped；`CB_REAL_DELTA_TEST=1` 真实差分夹具安装/卸载回归通过。
- 实机安装与游戏内全场景显示（含 `alpha0.4-font-test` / `alpha0.4` 的 `story12` 对齐效果）待用户实机确认。
