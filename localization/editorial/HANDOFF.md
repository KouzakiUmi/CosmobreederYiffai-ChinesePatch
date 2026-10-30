# 交接说明

本文记录到本次暂停时刻的实际状态、未完成事项与恢复方式。**未安装、未启动游戏、未访问存档、未做真实 GPU/CRT/输入验收。**

## 一、已完成

| 轮次 | 内容 | 产物 |
| --- | --- | --- |
| R1 | 全文粗校（339 发现） | [r1](r1/README.md) |
| R2 | 339 条逐条修复（291 应用／45 留置／3 驳回） | [r2](r2/README.md) |
| R3 | 36 项人名终裁 | [r3-names](r3-names/README.md) |
| R4 | 45 条留置全部定性，13 操作用 | [r4-pending](r4-pending/README.md) |
| R5 | 5 条创译 | [r5-creative](r5-creative/README.md) |
| R6 | 层一致性与术语回改（Bumper→弹跳机等） | [r6-consistency](r6-consistency/README.md) |
| R7 | 用运行代码＋渲染判定剩余条目 | [r7-render](r7-render/README.md) |
| R8 | 谜题提示改“相邻”，补字形 | [r8-puzzle](r8-puzzle/README.md) |
| R9 | 全正文精校二十批（双路：Gemini 3.8 Flash 自适应 + DS(OD)），551 处落地 | [r9-polish](r9-polish/README.md) |

当前候选链：candidate8（R3）→ 9（R4）→ 10（R5）→ 11（R6）→ 12（R8）→ 13（R9 batch-01）→ 14（+batch-03）→ 15（+batch-02）→ 16（+batch-04）→ 17（+05-part01）→ 18（+05-part03）→ 19（+05-part02）→ 20（+06-part02）→ 21（+06-part01）→ 23（+06-part04）→ 24（+06-part03）→ 25（+07-part01）→ 26（+07-part02）→ 27（+08-part01）→ 28（+08-part02）→ 29（+08-part03）→ 30（+08-part04）→ 31（+08-part05）→ 32（+09-part01）→ **33（+09-part02，最新）**。

- candidate33：15 个组件，四步编译 exit 0，55 类，`status` 为 `integrated_candidate_not_real_clip_CRT_input_acceptance`；manifest 记 `installed: false`、`real_clip_CRT_input_verified: false`。
- 候选 13～33 均跑完 **17 步 CPU 回归，全部 exit 0**（`passed_cpu_only_not_real_clip_CRT_input`）；`candidate33/results.json` 记 `game_started: false`、`user_save_accessed: false`。
- 各轮候选**均未生成 `acceptance.json`**：正式封签需绑定与本次归档 SHA 一致的上游资源／字体／方法复核，字体已多轮变化，旧复核记录无法套用。

## 二、遗留

| 项 | 状态 |
| --- | --- |
| P01-035 `MAGs` | 唯一仍未决的留置项。已证：该句只在 NSFW 版存在（SFW 版整句不同）、全库无 MAG 物品、无弹药系统，现译“弹匣”无据；但“杂志”与“磁靴”两解均无法证实。batch-09-part01 又遇到一次同词，仍无新证据 |
| 全正文系统精校 | **进行中**：R9 二十批已落地（1,293 场／9,170 行，约 43.3%）；batch-09 其余两个 part、batch-10、batch-11 未做，见下节 |
| 全库口径待终裁 | `LIGHTTAZER` 命名（光能电击刃／光电击枪／光电击器／轻型电击枪多种并存）、失真字幕处理方式、`COMMAND CENTER`（总部／指挥中心）、`PUPLOCK`（pup＋Harlock 双关） |
| `STARSUIT` 与 `Cosmosuit` 是否同一件 | 词典 `CosmoBody.name` 是 STARSUIT＝「星装」，而多处已落地作「宇宙服」；batch-09 两批均只记录未改 |
| candidate33 封签 | 未做 |

## 三、进行中：全正文系统精校（双路，路由已定）

模型与路由已在 batch-01 实际跑通；用户指定双路精校并禁用 ACP：

| 路 | 路由 | 档位 | 说明 |
| --- | --- | --- | --- |
| A | `gemini/gemini-3.8-flash` | `tiered`（自适应） | 非 ACP 入口；`antigravity-acp` 按用户要求禁用 |
| B | `opendesign-corouter-plan/deepseek-v4.1-flash` | `high` | OpenDesign 套餐路由（DS(OD)） |

已落地二十批：

| 批次 | 范围 | 场次／行 | 两路发现 | 裁决 | 台账 |
| --- | --- | --- | --- | --- | --- |
| batch-01 | 开场与第一区无线电教学 | 137／358 | 18 / 22 | 35（apply 32／reject 2／hold 1） | 32 个操作，并入 candidate13 |
| batch-03 | 波苏指挥线 | 53／437 | 44 / 38 | 35（apply 28／reject 5／hold 2） | 28 个操作，并入 candidate14 |
| batch-02 | 雄猫支援线 | 56／566 | 63 / 71 | 38（apply 24／reject 11／hold 3） | 24 个操作，并入 candidate15 |
| batch-04 | 毛鼠支援线与装备说明 | 81／871 | 22 / 39 | 40（apply 19／reject 14／hold 7） | 19 个操作，并入 candidate16 |
| batch-05-part01 | 图鉴与首领资料（1／3） | 49／419 | 13 / 33 | 56（apply 41／reject 11／hold 4） | 41 个操作，并入 candidate17 |
| batch-05-part03 | 图鉴与首领资料（3／3） | 50／415 | 20 / 27 | 56（apply 36／reject 18／hold 2） | 36 个操作，并入 candidate18 |
| batch-05-part02 | 图鉴与首领资料（2／3） | 50／419 | 28 / 23 | 55（apply 26／reject 27／hold 2） | 26 个操作，并入 candidate19 |
| batch-06-part01 | 雄猫道具线（1／4） | 65／434 | 4 / 31 | 38（apply 28／reject 8／hold 2） | 28 个操作，并入 candidate21 |
| batch-06-part02 | 雄猫道具线（2／4） | 65／441 | 28 / 23 | 43（apply 30／reject 11／hold 2） | 30 个操作，并入 candidate20 |
| batch-06-part03 | 雄猫道具线（3／4） | 65／437 | 32 / 28 | 62（apply 41／reject 19／hold 2） | 41 个操作，并入 candidate24 |
| batch-06-part04 | 雄猫道具线（4／4） | 65／441 | 9 / 24 | 35（apply 20／reject 14／hold 1） | 20 个操作，并入 candidate23 |
| batch-07-part01 | 结局与开场演出（1／2） | 11／385 | 3 / 33 | 38（apply 32／reject 4／hold 2） | 32 个操作，并入 candidate25 |
| batch-07-part02 | 结局与开场演出（2／2） | 12／391 | 12 / 18 | 30（apply 23／reject 7） | 23 个操作，并入 candidate26 |
| batch-08-part01 | VSN 场景脚本（1／5） | 15／452 | 21 / 29 | 53（apply 24／reject 26／hold 3） | 24 个操作，并入 candidate27 |
| batch-08-part02 | VSN 场景脚本（2／5） | 16／470 | 1 / 26 | 28（apply 25／reject 2／hold 1） | 25 个操作，并入 candidate28 |
| batch-08-part03 | VSN 场景脚本（3／5） | 15／483 | 0 / 8 | 25（apply 24／hold 1） | 24 个操作，并入 candidate29 |
| batch-08-part04 | VSN 场景脚本（4／5） | 16／502 | 2 / 7 | 36（apply 32／reject 3／hold 1） | 32 个操作，并入 candidate30 |
| batch-08-part05 | VSN 场景脚本（5／5） | 16／449 | 5 / 28 | 50（apply 27／reject 23） | 27 个操作，并入 candidate31 |
| batch-09-part01 | 区域场景与条件分支（1／4） | 228／402 | 11 / 24 | 47（apply 24／reject 23） | 24 个操作，并入 candidate32 |
| batch-09-part02 | 区域场景与条件分支（2／4） | 228／398 | 4 / 14 | 21（apply 15／reject 6） | 15 个操作，并入 candidate33 |

**尚未出工单的部分**：batch-09-part03、part04（各约 399 行，工单已生成、可直接派单）；batch-10 界面与系统（295 场／1,159 行，需拆约 3 个 part）；batch-11 零散条目（109 场／505 行）。批次定义均已在 `tools/build_batch.py` 的 `BATCHES` 里，`reader.md` 与 `.json` 由 `build_batch.py` 生成，`ORDER.md` 与 `reference-excerpt.md` 需按批手写（模板取最近一批的 `orders/`）。

组件 `r9polish` 按 `batches` 数组顺序应用，每批 gate 绑定它之前的构建，串行校验整资源 SHA；任一基线漂移会让构建直接失败而不是悄悄覆盖。**应用顺序与批次编号顺序不同**（batch-06 的 part04 在 part03 之前、part02 在 part01 之前），改顺序要同步重建后续所有候选的 gate。

## 四、后续批次的建议做法

1. **分块**：用 `r9-polish/tools/build_batch.py <batch> --parts N --part K` 生成工单，批次定义见 `BATCHES`，优先级见 [TRANSLATION_PLAN](r1/TRANSLATION_PLAN.md) 第八节。
2. **工单内容**：整段原文＋候选当前中文＋参照摘录＋容器限制＋七步重写法。参照摘录的术语表**必须引用 `datav/dictionary.json` 的条目名**，不能凭印象写（batch-05-part01 曾把 Squeaker／Spiker／Driller 写成「吱吱兽／刺甲机／钻掘机」，三个错写法在库里零出现）。
3. **产出**：两路各自 findings／coverage／summary；主代理写 `decisions.tsv`，`build_ledger.py` 出账并 dry-run，`verify_round.py` 出 gate。
4. **落地**：台账登记进 `component.json` 的 `batches`，构建候选，跑 17 步回归，再逐条回验台账明文是否等于新候选里的实际行，最后确认 gate 的 `ledger_sha256`／`decisions_sha256` 与暂存区 blob 一致才提交。
5. **容器限制（已实测，直接引用即可）**：卡面 16 列 × 128px、≤15 行；数据书 224px、≤3 行；剧情 12px、240px 折行、每页 3 行；超限均抛异常。`measure_width.py` 与 `tools/preview-layout.py` 可用真实 12px 字形表测折行。

## 五、关键事实（避免重复踩坑）

- **原版基线**以 `localization/sources/archives.json` 为准，`backup/` 存着对应副本；**已打补丁的游戏目录不是英文源**（其 `datav/1` 解密即中文）。
- 归档内资源为无扩展名编号条目，用 [codec.py](../tools/codec.py)（Salsa20）解密；`patch.pak` 覆盖 jar 同键，`datay` 只在 jar，**改字典要两层同改**（R6 的教训）。
- 游戏**无语音对白**（FMOD 全为 Music/SFX），失真广播是文本风格装置，不存在可等的原音。
- 改文一律写来源锁定台账（`localization/translations/*-repairs.jsonl`），由 [editorial_repairs.py](../tools/editorial_repairs.py) 校验；任一 SHA 或旧值漂移整批拒绝。
- 归档条目字节常因**随机重加密**而整体不同，比较内容必须解密后比明文。
- **同一句会同时存在于 jar 与 pak 两侧**（如 `Traeh吩咐什么，其便做什么`）。改 jar 侧不会影响 pak 侧，因为 pak 覆盖同键；遇到重复句要查两侧。
- **行尾空格的唯一判据是英文原文行尾**。`catalog/occurrences.jsonl` 的 `trailing_ws` 描述的是**中文行**，用它判断会得出「中英一致、都是镜像」的循环结论——batch-08-part03 因此漏报 17 处真缺陷。正确做法：`occurrence_id → unit_id` 查 `catalog/units.jsonl` 的 `source`；`SFW` 编号行没有 occurrence 记录，改用工单 JSON 的 `source` 字段。已落地的 78 处行尾空格改动按此复核过，76 处原文确无空格，2 处无法追溯。
- **大小写、全半角形态也可能是照源镜像**。batch-09-part01 一路报了 9 条「货币名应统一大写」，但英文原文本身逐行 `lect`／`Lect` 不一，中文是镜像，9 条全部驳回。判断形态类问题前先看英文原行。
- **两路一致不等于覆盖**。batch-06-part01 两路产出 4 条与 31 条；batch-08-part02 是 1 条与 26 条。一条改动的正当性来自能否指出它的源行，不来自两个模型都说。
- **路由也会失效**：Gemini 路在 batch-06-part03、batch-08-part02/03/04 多次读完却零落盘或中途终止。重派时把批次拆成独立 reader 文件、明确「边读边写」并给出具体文件路径，成功率明显提高；若仍失败，按单路落地并在提交信息里写明哪几场只有一路。

## 六、未验证项（勿当作已通过）

安装、启动、存档、真实 GPU/CRT、输入/IME、完整场景层次、全图可达性均未验证；CPU 回归与静态复核不等于实机验收。行宽只在字符宽度层估算，未在任何候选上做实机渲染确认。
