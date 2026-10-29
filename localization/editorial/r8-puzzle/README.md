# R8：谜题提示改为“相邻”

处置 [R4](../r4-pending/reports/pending-01/decisions.tsv) 遗留的 P08-022。共 4 个来源锁定操作，已并入 candidate12，17 步 CPU 回归全部 exit 0。

## 依据

[R7](../r7-render/README.md) 把六条“脑中回响”同屏取证后，判断依据已从单句变成整族约束：

| 部分 | 原文 | 现译 |
| --- | --- | --- |
| 1 | `STAR BETWEEN CROSS &SQUARE` | 星星在十字与方块之间 |
| 2 | `TRIANGLE COMES FIRST` | 三角排在最前 |
| 3 | `WAVES FOLLOWED BY CROSS` | 波浪之后是十字 |
| 4 | `CIRCLE IS AFTER TRIANGLE` | 圆圈在三角之后 |
| 5 | `HEART IS NOT TOUCH CROSS` | **→ 心形与十字不相邻** |
| 6 | `SQUARE IS NOT LAST` | 方块不是最后 |

六条里五条描述先后与位置，`TOUCH` 在序列／格位语境下只能指相邻；“不接触”不合族群，也会被读成“不能碰”。

代码侧同时确认容器：`SceneText.dataBlock` 走 224px、最多 3 行；新文仍为 1 行 112px，不越界。

## 改动

| 归档 | 键 | 旧 | 新 |
| --- | --- | --- | --- |
| 两个归档各 2 处 | `ui.data.f_AgentFZ5.desc`、`ui.data.m_AgentMZ5.desc` | `…$[心不接触十字]` | `…$[心形与十字不相邻]` |

`邻`(U+90BB) 原本不在字库，本轮由构建的字符需求自动补入 story12 与 classic，触发字体与字体 pin 类重写（与 R4 补「惬」同机制）。

## 结果

- candidate12：13 个组件，四步编译 exit 0，55 类；文本差异仅 `datav/1` 两个归档各 2 键。
- 独立复核 14 项断言 PASS，含 `邻` 在两套字库中的存在性、差异集合、CPU 结果绑定。
- 渲染确认：六条提示同屏，第 5 条完整显示“心形与十字不相邻”。

![应用后的六条提示](../r7-render/out/scene_fenfen_after.png)

## 边界

未安装、未启动游戏、未访问存档、未做真实 GPU/CRT/输入验收；未生成 `acceptance.json`。

## 文件

- [处置表](reports/puzzle-01/decisions.tsv) · [构建与回归](reports/puzzle-01/BUILD.md) · [候选复核](review/candidate12-review.json)
- 台账：[editorial-r8-puzzle-repairs.jsonl](../../translations/editorial-r8-puzzle-repairs.jsonl)
- 工具：[build_puzzle.py](tools/build_puzzle.py) · [verify_puzzle.py](tools/verify_puzzle.py)
