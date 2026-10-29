# R9：全正文系统精校（第 1 轮）

本轮把 R1 粗校／R2 修复之后的**全文系统精校**真正开跑：对照英文重写中文，而不是只挑错词。方法口径沿用 [R1 中文重写方案](../r1/TRANSLATION_PLAN.md)，落地沿用来源锁定台账与候选构建链。

## 一、输入基线

| 项 | 值 |
| --- | --- |
| 快照 | 基线候选 | 场次／行 | 用途 |
| --- | --- | --- | --- |
| `snapshot-01` | candidate4 | 2,966／13,400 | 已过期，R1 使用 |
| `snapshot-02` | `r8-puzzle-candidate12` | 2,968／13,406 | batch-01 |
| `snapshot-03` | `r9-polish-candidate13` | 2,989／13,494 | batch-02 起 |

快照均用 `r1/tools/prepare_corpus.py --candidate <build> --output <snapshot>` 生成，状态 `prepared_not_semantically_reviewed`；`current` 是对应候选的实际显示行，不是初翻草稿。批次工单用 `tools/build_batch.py <batch> --snapshot <name>` 生成，工单里记录套用的快照与基线候选。

## 二、双路设置（按用户指派，不使用 ACP）

| 路 | 路由 | 档位 | 说明 |
| --- | --- | --- | --- |
| A | `gemini/gemini-3.8-flash` | `tiered`（自适应） | 非 ACP 入口；`antigravity-acp` 在本轮禁用 |
| B | `opendesign-corouter-plan/deepseek-v4.1-flash` | `high` | OpenDesign 套餐路由（DS(OD)） |

两路拿到完全相同的工单与参照，独立出提案、互不通信；主代理负责交叉核验、裁决与台账。

## 三、批次

批次优先级按 [TRANSLATION_PLAN](../r1/TRANSLATION_PLAN.md) 第八节。

| 批次 | 范围 | 场次 | 行数 | 字符 | 状态 |
| --- | --- | --- | --- | --- | --- |
| batch-01 | `The0`、`Area0_Macsen1/2/Bar`、`Area0_Prison1`、`MauserHints_AreaA` | 137 | 358 | 23,277 | 已并入 candidate13 |
| batch-02 | `Tomcat` | 56 | 566 | 36,041 | 已并入 candidate15 |
| batch-03 | `Bossu` | 53 | 437 | 29,033 | 已并入 candidate14 |
| batch-04 | `Mauser` | 81 | 871 | 58,922 | 已并入 candidate16 |
| batch-05 | `BossuDex`（图鉴） | 149 | 1,253 | 83,198 | 分 3 个 part，依次并入 candidate17／19／18 |
| batch-06 | `TomcatItems`（道具） | 260 | 1,753 | 117,974 | 分 4 个 part，待开 |

每批工单在 `batch-NN/orders/`：`ORDER.md`（规范）· `batch-NN.reader.md`（正文）· `batch-NN.json`（结构化）· `reference-excerpt.md`（本批人物与术语摘录，按批重写）。

## 四、工单硬约束（摘要）

- `proposed_zh` 是完整物理行，前缀、缩进、方括号、`@DerekChipReport`、`<3`、数字与频率原样保留。
- 不增删物理行；跨行重分配只写 `note`，由主代理裁决。
- 剧情框 240px／12px 字，单行正文建议 ≤ 约 20 个全角字。
- `current` 为空的 ROW 是既有合句尾行，不报漏译，也不能直接填充（台账拒收空→非空）。
- 已裁决项（R3 人名、R6 术语、R8 谜题提示）不得重提。
- 提案不得让任何行由 ≤3 行折行变成 >3 行；反向也成立：既有 >3 行的合句行，本批应借机压回 3 行（batch-02 的 3 处 4 折行即此例）。

## 四之二、两路裁决的经验

三批下来，两路的可靠性差异不在发现数量，而在**方向**：

- 术语类提案里，「把少数写法改成多数写法」两路都可靠；「把多数写法改成术语提案里的写法」需要先有全库终裁，否则只会多出一种写法（`LIGHTTAZER`）。
- 已经 R2 裁决过的语用点（`torch` 英美异称、`agent` 取「特工」）会被后到的模型反复重提。裁决时以既有裁决为准，并要求提案带新证据才重开。
- 两路各自的「误判为 A」集中在把解释性改写当成误译；A 级只认能指到具体英文词、否定、数量、施受或结构的那种。

## 四之三、主代理补的发现

三批共补 21 条 `R9M-*`（batch-01 3 条、batch-02 2 条、batch-03 16 条），绝大多数是「同文的姊妹行」：工单要求每条发现只挂本场 row，同文异场的位置只能写进 note，落台账时按 row 逐条展开。批量落库后再回读归档核对，是发现这类遗漏的唯一可靠办法。

## 四之四、参照摘录写错会让两路一致地错

batch-04 里两路都要求把「反重力脚环」改成「反重力踝环」，提案质量很高：行数齐、理由足、覆盖 4 个 row。但方向是反的——UI 道具名就是「脚环」，正文也是「脚环」多。

根源是我在 `reference-excerpt.md` 里把 `anti-grav anklet` 定为「反重力踝环」。两路照做，交叉核对也发现不了，因为**两路错得一样**。

教训：参照摘录里的每一条术语都要先回查全库用法与 UI 名，再写进工单；写错比不写危害更大，它会把两路的一致性变成一致错。

## 五、流程与产物

1. `tools/build_batch.py <batch> --snapshot <snap>` 生成批次工单（可复现，带 corpus manifest SHA 与基线候选）。
2. 两路各自写 `batch-NN/gemini|ds/{findings,coverage}.jsonl` 与 `summary.md`。
3. `tools/verify_batch.py <batch>` 做结构核验（覆盖、row 归属、前缀与标记守恒）并输出 worksheet；`tools/measure_width.py <batch>` 用真实 12px 字形表实测折行。
4. 主代理逐条核验后写 `batch-NN/review/decisions.tsv`；`tools/build_ledger.py <batch>` 生成该批来源锁定台账并 dry-run，`tools/verify_round.py <batch>` 出 gate。
5. 在 `localization/optimization/r28/r9polish/component.json` 的 `batches` 数组登记该批（台账／gate／decisions 三项），再构建候选与跑 17 步回归。

## 五之二、五批合计

| 项 | -01 | -02 | -03 | -04 | 05-part01 | 05-part02 | 05-part03 | 合计 |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 场次／行 | 137／358 | 56／566 | 53／437 | 81／871 | 49／419 | 50／419 | 50／415 | 476／3,485 |
| 两路发现 | 18＋22 | 63＋71 | 44＋38 | 22＋39 | 13＋33 | 28＋23 | 20＋27 | 461 |
| 裁决 | 35 | 38 | 35 | 40 | 56 | 55 | 56 | 315 |
| 　采纳 | 32 | 24 | 28 | 19 | 41 | 26 | 36 | **206** |
| 　驳回 | 2 | 11 | 5 | 14 | 11 | 27 | 18 | 88 |
| 　留置 | 1 | 3 | 2 | 7 | 4 | 2 | 2 | 21 |
| 主代理补 | 3 | 2 | 16 | 1 | 6 | 4 | 1 | 33 |

驳回率从 batch-01 的 6% 升到 batch-02 的 29%、batch-04 的 35%，batch-05 三个 part 分别为 20%、49%、32%。驳回变多不等于审校变差：part02／part03 的驳回里有一大半是两路同报同一行、只取一路措辞，这类在早期批次里根本没被计数。真正判错的类型仍在变少。

## 五之三、batch-05-part01 的两个教训

**一、参照摘录里的术语表是最高危的一行。** part01 摘录把 Squeaker／Spiker／Driller 写成「吱吱兽／刺甲机／钻掘机」，Gemini 老老实实按表执行，DS 没有照表而是去查游戏内名，才躲过去。语料实测 `datav/dictionary.json` 的条目名是「吱吱怪／刺虫／钻探者」（SQUEAKER 同源 16 处、FLAMER 作「喷火者」），三个「规范译名」在库里零出现。真正需要的不是「更聪明的模型」，而是**摘录里的每条术语都必须带出处行号**——没有出处的术语表等于把错了的常识写成规则。

**二、`BOSSU HERE` 不是 `roger`。** Gemini 把 `[BOSSU HERE, WHAT'S THE PROBLEM, AGENT?]` 改成「波苏收到」，「收到」对应 roger／copy that，而 HERE 是报明身份。这行真正的问题是译名替换留下的 `波苏 在此`（半角空格）。同类误判还有 `COME IN. BOSSU?`：源文带问号，现译「波苏，我进来了。」把呼叫写成陈述，抹掉了问句，也抹掉了下行波苏拿 come in 开黄腔的支点。

## 六、构建与回归

`r9polish` 组件按 `batches` 数组顺序应用各批台账。每批的 gate 绑定**它应用之前的那一个构建**（batch-01 绑 candidate12、batch-03 绑 candidate13、batch-02 绑 candidate14、batch-04 绑 candidate15、batch-05-part01 绑 candidate16），构建时逐批串行校验整资源 SHA：任何一批的基线漂移都会让构建直接失败，而不是悄悄覆盖。

| 候选 | 组件 | 台账 | 编译 | 17 步回归 |
| --- | --- | --- | --- | --- |
| candidate13 | 15 个（新增 `r9polish`），`full_component_set=true` | batch-01，32 个行级操作 | 四步 exit 0，55 类 | 全部 exit 0 |
| candidate14 | 同上 | batch-01 + batch-03，60 个行级操作 | 四步 exit 0，55 类 | 全部 exit 0 |
| candidate15 | 同上 | batch-01 + batch-03 + batch-02，84 个行级操作 | 四步 exit 0，55 类 | 全部 exit 0 |
| candidate16 | 同上 | 再加 batch-04，共 103 个行级操作 | 四步 exit 0，55 类 | 全部 exit 0 |
| candidate17 | 同上 | 再加 batch-05-part01，共 144 个行级操作 | 四步 exit 0，55 类 | 全部 exit 0 |
| candidate18 | 同上 | 再加 batch-05-part03，共 180 个行级操作 | 四步 exit 0，55 类 | 全部 exit 0 |
| candidate19 | 同上 | 再加 batch-05-part02，共 206 个行级操作 | 四步 exit 0，55 类 | 全部 exit 0 |

candidate13 归档：jar `fb533645…61587`（45,842,131 B）· pak `046158e7…af8ca8`（13,588,668 B）。
candidate15 归档：jar `2ff30bbd…bcb29`（45,842,088 B）· pak `9c2c7377…0ca585`（13,588,593 B），明细见 [`build-manifest.json`](../../builds/r9-polish-candidate15/build-manifest.json)。
candidate16 归档见 [`build-manifest.json`](../../builds/r9-polish-candidate16/build-manifest.json)。
candidate17 归档见 [`build-manifest.json`](../../builds/r9-polish-candidate17/build-manifest.json)。

构建入口仍是 [`build_candidate.py`](../../optimization/r28/integration/build_candidate.py) 与 [`test_candidate.py`](../../optimization/r28/integration/test_candidate.py)；未生成 `acceptance.json`（字体与资源复核未重新封签）。

## 七、边界

- 已落地 batch-01～04 与 batch-05 全部三个 part（476 场／3,485 行），约占全库 2,989 场的 15.9%；**batch-06 与各区零散 root 未精校，「第 1 轮」不因此视为完成**。
- 三项全库口径问题已留置待终裁：`LIGHTTAZER` 命名、失真字幕处理方式、`COMMAND CENTER`（总部／指挥中心）。
- 引号体例（`“”` 与 `「」` 并存）也仍待终裁：各批只在行内保持原体例，未做全局统一，累计约 110 对 `“”` 对 39 对 `「」`。
- `FENFEN` 的中文条目名未定：词典 SFW 版作「芬芬」、NSFW 版作「Fenfen」，正文 124 处作 Fenfen。目前只统一英文写法，未新造中文名。
- 不覆盖任何历史证据；未安装、未启动游戏、未访问存档；未生成 `acceptance.json`。
- CPU 回归与静态复核不等于实机验收：男线 `DragonHint` 既有 4 行折行（240px／12px 实测）是否翻页或溢出，仍需实机确认。
- 台账中的应用项只证明「更准、更连得上」，不证明全篇语义终审通过。
- 后续批次按 [TRANSLATION_PLAN](../r1/TRANSLATION_PLAN.md) 第八节顺序推进，每批沿用同一双路与裁决流程；`R9M-003`（频率数字两侧空格）待全库排版口径统一后单独处理。
