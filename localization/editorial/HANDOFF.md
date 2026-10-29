# 交接说明

按当前安排暂停；本文记录到暂停时刻为止的实际状态、未完成事项与恢复方式。**未安装、未启动游戏、未访问存档、未做真实 GPU/CRT/输入验收。**

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
| R9 | 全正文精校 batch-01～04 与 batch-05 全部三个 part（双路：Gemini 3.8 Flash 自适应 + DS(OD)），206 处落地 | [r9-polish](r9-polish/README.md) |

当前候选链：candidate8（R3）→ 9（R4）→ 10（R5）→ 11（R6）→ 12（R8）→ 13（R9 batch-01）→ 14（+batch-03）→ 15（+batch-02）→ 16（+batch-04）→ 17（+05-part01）→ 18（+05-part03）→ **19（+05-part02，最新）**。

- candidate12：13 个组件，四步编译 exit 0，55 类。
- candidate13～19：15 个组件（新增 `r9polish`），四步编译 exit 0，55 类；**17 步 CPU 回归全部 exit 0**。
- 候选 8–19 均跑完 **17 步 CPU 回归，全部 exit 0**（`passed_cpu_only_not_real_clip_CRT_input`）。
- 各轮候选**均未生成 `acceptance.json`**：正式封签需绑定与本次归档 SHA 一致的上游资源/字体/方法复核，字体已多轮变化，旧复核记录无法套用。

## 二、遗留

| 项 | 状态 |
| --- | --- |
| P01-035 `MAGs` | 唯一仍未决的留置项。已证：该句只在 NSFW 版存在（SFW 版整句不同）、全库无 MAG 物品、无弹药系统，现译“弹匣”无据；但“杂志”与“磁靴”两解均无法证实 |
| 全正文系统精校 | **进行中**：R9 batch-01～04 与 batch-05 三个 part 已落地（476 场／3,485 行，约 15.9%）；batch-06 的 4 个 part 工单已就绪，见下节 |
| 全库口径待终裁 | `LIGHTTAZER` 命名（光能电击刃／光电击枪／轻型电击枪三种）、失真字幕处理方式、`COMMAND CENTER`（总部／指挥中心） |
| candidate19 封签 | 未做 |

## 三、进行中：全正文系统精校（双路，路由已定）

模型与路由已在 batch-01 实际跑通；用户指定双路精校并禁用 ACP：

| 路 | 路由 | 档位 | 说明 |
| --- | --- | --- | --- |
| A | `gemini/gemini-3.8-flash` | `tiered`（自适应） | 非 ACP 入口；`antigravity-acp` 按用户要求禁用 |
| B | `opendesign-corouter-plan/deepseek-v4.1-flash` | `high` | OpenDesign 套餐路由（DS(OD)）；旧记录里「没有 opendesign provider」已过时 |

已落地七批：

| 批次 | 范围 | 场次／行 | 两路发现 | 裁决 | 台账 |
| --- | --- | --- | --- | --- | --- |
| batch-01 | 开场与第一区无线电教学 | 137／358 | 18 / 22 | 35（apply 32／reject 2／hold 1） | 32 个操作，并入 candidate13 |
| batch-03 | 波苏指挥线 | 53／437 | 44 / 38 | 35（apply 28／reject 5／hold 2） | 28 个操作，并入 candidate14 |
| batch-02 | 雄猫支援线 | 56／566 | 63 / 71 | 38（apply 24／reject 11／hold 3） | 24 个操作，并入 candidate15 |
| batch-04 | 毛鼠支援线与装备说明 | 81／871 | 22 / 39 | 40（apply 19／reject 14／hold 7） | 19 个操作，并入 candidate16 |
| batch-05-part01 | 图鉴与首领资料（part 1／3） | 49／419 | 13 / 33 | 56（apply 41／reject 11／hold 4） | 41 个操作，并入 candidate17 |
| batch-05-part03 | 图鉴与首领资料（part 3／3） | 50／415 | 20 / 27 | 56（apply 36／reject 18／hold 2） | 36 个操作，并入 candidate18 |
| batch-05-part02 | 图鉴与首领资料（part 2／3） | 50／419 | 28 / 23 | 55（apply 26／reject 27／hold 2） | 26 个操作，并入 candidate19 |

batch-06 的 4 个 part（`TomcatItems`，各约 65 场／435 行），工单、参照摘录与分段均已生成，可直接派单。

组件 `r9polish` 按 `batch-01 → batch-03 → batch-02 → batch-04 → batch-05-part01 → batch-05-part03 → batch-05-part02` 顺序应用，每批 gate 绑定它之前的构建，串行校验整资源 SHA。已知超限行已压回 3 行：batch-02 三处、batch-05-part01 两处、part02 两处、part03 一处。

**参照摘录的术语表已改为带出处。** part01 的摘录曾把 Squeaker／Spiker／Driller 写成「吱吱兽／刺甲机／钻掘机」，而 `datav/dictionary.json` 的条目名是「吱吱怪／刺虫／钻探者」，三个错写法在库里零出现；一路照表执行、一路没照表，才暴露出冲突。三份摘录现已全部改为引用词典条目名，工单第 11 条要求任何术语改动必须给出依据所在行。

Grok 复查本轮未用（用户要求双路）；`xai-oauth/grok-4.6`、`grok-4.7` 仍可用于后续独立复核。

## 四、后续批次的建议做法

1. **分块**：用 `r9-polish/tools/build_batch.py` 按批次生成工单，取 [TRANSLATION_PLAN](r1/TRANSLATION_PLAN.md) 第八节的下一优先级（核心人物往来 → 关卡救援 → 图鉴与装备 → 结局），每批约 300–400 行，先跑通再扩量。
2. **工单内容**：整段原文＋候选当前中文＋参照摘录＋容器限制＋七步重写法；复制 `r9-polish/batch-01/orders/` 的 ORDER 与 reference-excerpt 口径。
3. **产出**：两路各自 findings/coverage/summary；`verify_batch.py` 核结构并出 worksheet；主代理写 `decisions.tsv`，`build_ledger.py` 出账并 dry-run，`verify_round.py` 出 gate。
4. **落地**：台账并入 `r9polish` 组件（台账文件追加、gate 重新生成），在 [build_candidate.py](../optimization/r28/integration/build_candidate.py) 走既有组件块，再构建候选与跑 17 步回归。
5. **容器限制（已实测，直接引用即可）**：卡面 16 列 × 128px、≤15 行；数据书 224px、≤3 行；剧情 12px、240px 折行、每页 3 行；超限均抛异常。`r9-polish/tools/measure_width.py` 可用真实 12px 字形表测折行。

## 五、关键事实（避免重复踩坑）

- **原版基线**以 `localization/sources/archives.json` 为准，`backup/` 存着对应副本；**已打补丁的游戏目录不是英文源**（其 `datav/1` 解密即中文）。
- 归档内资源为无扩展名编号条目，用 [codec.py](../tools/codec.py)（Salsa20）解密；`patch.pak` 覆盖 jar 同键，`datay` 只在 jar，**改字典要两层同改**（R6 的教训）。
- 游戏**无语音对白**（FMOD 全为 Music/SFX），失真广播是文本风格装置，不存在可等的原音。
- 改文一律写来源锁定台账（`localization/translations/*-repairs.jsonl`），由 [editorial_repairs.py](../tools/editorial_repairs.py) 校验；任一 SHA 或旧值漂移整批拒绝。
- 归档条目字节常因**随机重加密**而整体不同，比较内容必须解密后比明文。

## 六、未验证项（勿当作已通过）

安装、启动、存档、真实 GPU/CRT、输入/IME、完整场景层次、全图可达性均未验证；CPU 回归与静态复核不等于实机验收。
