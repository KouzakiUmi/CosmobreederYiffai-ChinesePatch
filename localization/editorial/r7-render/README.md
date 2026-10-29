# R7：从运行代码与真实场景判定剩余三条

对 R4/R6 后仍留置的 3 条，**先用候选归档里的运行代码确定真实容器与数据来源，再用真实位图字体按该容器渲染场景**，而不是孤立渲染一句话。

## 代码给出的容器真相

| 容器 | 代码位置 | 实测规则 |
| --- | --- | --- |
| 角色卡正文 | [SceneText.java](../../../layout/src/PRG/SceneText.java) `cardFormat`/`cardDraw` → `PRG/Jm` | **16 列 × 128px**，行数上限 **15**（`NT=15`，背面 `NU=11`）；某行超 128px 或总行数超限即抛异常 |
| 数据书条目 | `SceneText.dataBlock` → `PRG/Kc` | **224px**，最多 **3 行**，超过抛 "Data book exceeds three reachable 224px rows" |
| 剧情对话 | `DialogueGrid` + `StoryFont12` | 12px、**240px** 折行、每页 **3 行** |

顺带纠正 R7 上一版的误判：剧情对话并不是“超过 240px 抛异常”，240px 是**折行宽度**，真正的硬断言只针对已经排好的定长行（卡面、数据书、结局报告）。

## 判定一：P03-033 角色卡 —— 结案不改

- 代码：卡面 16 列 × 128px、≤15 行。
- 现译 11 行、每行 3–6 字（最宽 48px），远在限内；R1 合并稿 6 行（最宽 72px）也合法。
- 查全部 16 张卡：**正面一律 11 行**。合并成 6 行只会让这一张短于同类。

![卡面现译](out/card_before.png) ![卡面合并稿](out/card_after.png)

结论：保留 11 行结构，**结案**。

## 判定二：P01-035 `MAGs` —— 仍留置，但“弹匣”可判为无据

代码与数据侧的发现：

1. `Talk.mags` 在**两种内容版里是两段不同台词**：SFW 版第二句是 `It gets my fur all mussed up!`（中文：弄得我的毛全乱了！），只有 **NSFW 版**才有这句 `there's extra MAGs in the back here if you need them!`。
2. 全库检索 `MAG`／`magazine`／`magnet`：除这一句外只剩 `MAGNETOSHEATH` 环境文字。
3. `equipInfo`／`consumableInfo` 里**没有任何靴类、磁力类、弹匣类物品**；Macsen 在 E 区只卖 `SpecialGeiger` 一件货。
4. 游戏没有弹药系统，`弹匣` 没有任何机制支撑。

![E 区商人对话场景（按 240px 折行、每页 3 行）](out/scene_macsen_dialogue.png)

所以这是一句纯玩笑、且只存在于 NSFW 版。两种可解释读法：`杂志`（后屋的成人刊物，更贴合 NSFW 版替换掉这句的行为）或 `磁靴`（太空行走用）。两者都无实证，**维持留置**，但可以确定现译“弹匣”是无据的。

## 判定三：P08-022 谜题提示 —— 线索已齐，建议改为“不相邻”

代码侧：`ui.data.{f,m}_AgentFZ{1..6}.desc` 是**六条一组的“脑中回响”**，走 `dataBlock`（224px、3 行上限），同一组在男女两版内容一致。六条全文：

| 部分 | 原文 | 现译 |
| --- | --- | --- |
| 1 | `STAR BETWEEN CROSS &SQUARE` | 星星在十字与方块之间 |
| 2 | `TRIANGLE COMES FIRST` | 三角排在最前 |
| 3 | `WAVES FOLLOWED BY CROSS` | 波浪之后是十字 |
| 4 | `CIRCLE IS AFTER TRIANGLE` | 圆圈在三角之后 |
| 5 | `HEART IS NOT TOUCH CROSS` | **心不接触十字** |
| 6 | `SQUARE IS NOT LAST` | 方块不是最后 |

六条里五条都在描述**先后与位置**（之间／最前／之后／不是最后），第 5 条是唯一的例外用词。同族约束下，`TOUCH` 指的就是**序列或格位上的相邻**，不是物理接触；中文写成“不接触”既不合族群，也会被读成“不能碰”。

![六条提示同屏](out/scene_fenfen_data.png)

另外代码里搜不到任何 adjacency／neighbour／touch 的谜题判定实现（`AdjacentScope`、`NearestNeighbour` 是引擎通用件），所以无法从判定逻辑反推；但“相邻”是这组约束唯一自洽的读法。

成本：`邻`(U+90BB) 不在 story12／classic 字库，改则需新增一个字形（同 R4 补「惬」那样触发字体与 pin 类重写）。宽度没问题（88px → 100px，仍 1 行）。

## 边界

只做代码取证与渲染模拟；未改任何归档、译文或台账；未安装、未启动游戏。渲染使用 candidate11 的字体与真实容器宽度，未复现背景美术与对话框边框。
