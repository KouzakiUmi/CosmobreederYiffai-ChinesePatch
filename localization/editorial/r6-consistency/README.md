# R6：层一致性与术语回改

**处理 R4 遗留的 4 项可解问题 + 2 类结构问题，共 23 个来源锁定操作。** 已并入 candidate11，17 步 CPU 回归全部 exit 0。

本轮性质是**纠错**，不是新创作：其中两项是对我自己前两轮判断的修正。

## 五件事

| 类别 | 内容 | 操作 |
| --- | --- | --- |
| A 内证改译 | P01-034／P05-015 `SENSOR DARK` → “传感器探测不到的悬浮球” | 4 |
| B 术语回改 | P04-031／P10-035 `Bumper` 由“弹板／撞击兽”改为“弹跳机” | 10 |
| C 术语统一 | P04-024 道具名“训练者”→“驯兽” | 2 |
| D 最小改译 | P10-032 三重否定 → “我也不是没有胃口。” | 1 |
| E 层一致性 | R4 只落了 patch 层的 4 个键补 jar 同值；男线 Werepup 描述统一 | 6 |

## A. `SENSOR DARK`：同组场景自证

同一功能（Zener 球拾取）的其它球体对话里，译文自己写的是“总部探测不到的球体”“近场数据里完全看不到的”，且紧接一句“没有数据，我们就只能相信你的直觉了”。所以该词是“传感器探不到”，不是“暗色”。现译“暗色传感球”既孤立，也把修饰语落在了错误的名词上。

## B. `Bumper`：前两轮都判错

图鉴原文（`BossuDex.ClassicBumper`）：

> 那些**不停上下弹跳的机器**似乎是某种**巡逻机器人**，目前出了故障。

R1 术语提案 T018 对 `Bumper` 的暂名是“弹跳巡逻机”，并明确约束“机器不译成兽”。据此：

- 初翻“弹板”把它当成了弹球台机关；
- R4 的“撞击兽”既与“弹跳”不符，又违反“机器不译成兽”，还把 SFW 层“撞击机器人”与 NSFW 层“撞击兽”拆成两种说法；
- 本轮统一为“弹跳机”，popup 三键与四句对白一起改。

## C. 道具名与对白不一致

对白从头到尾说“驯兽电击枪”，术语表也已裁“驯兽／见习”，但道具名仍是“训练者”（读起来像个人）。改为“驯兽”。商店的“训练者 - 持证／训练者提供报酬”属持证训练者义，按术语分译保留未动。

## D. 三重否定

原文 `It's not as if I'm not without an appetite` 在自夸段落，随后一句是“我的力量和体格，可不是在弥补我男性方面其他地方的不足！”——语意是“我有胃口”。原译照字面搬成三重否定读不通，改为“当然，我也不是没有胃口。”，保留双重否定的语气。

## E. 两层归档不一致（结构问题）

从 R2 起，改文按 occurrence 记录的归档落笔；`patch.pak` 覆盖 jar 同键，因此 **R4 的 8 个字典键只改了 patch 层**，没装 NSFW 补丁档的玩家读 jar 层会看到旧文。本轮把可对齐的 4 个键补到 jar：

| 键 | 修正前 jar | 现两层同值 |
| --- | --- | --- |
| `SpecialFap.ElfBuff.desc` | 精灵闲置时\|回复精神力 | 精灵加成\|闲置时回复精神力 |
| `StatPretzel.desc` | 新鲜出炉的\|扭结面包 | 硬结打卷\|育得正好 |
| `ui.breeding.Kobold.affinity.max` | 科博德蜷起身子，\|享受着你的陪伴。\|… | 科博德蜷在你身边，\|惬意地享受着你的陪伴。\|… |
| `ui.data.f_ClassicWerepup.desc` | 给了小狗一记重击后，\|又和他交上了朋友！ | 击败小狼崽之后，\|回忆涌上心头，又迟疑起来。 |

顺带发现同一句 `Werepup` 描述此前有**三种译法**（jar 女、jar 男、pak 男），本轮一并统一；`ui.data.m_AgentM02.desc` 在 jar 层不存在，无需处理。

未动的两处既有差异已确认是有意设计：`navmap.shop_trainer` 的“训练者”是持证训练者义；`CosmoCardWerepup.desc.Back` 的 jar 空卡背对应 SFW 层不展示该段内容。

## 仍留置（3 条）

| 编号 | 原因 |
| --- | --- |
| P08-022 | `[HEART IS NOT TOUCH CROSS]` 的“接触”是否等于“相邻”取决于谜题判定，缺规则证据 |
| P01-035 | `MAGs` 无对应物品，物品表里没有任何 MAG 类商品，纯语境猜 |
| P03-033 | 角色卡正面是 13 个定长槽位，六行合并稿需字体容器实测后才能落 |

## 边界

未安装、未启动游戏、未访问存档、未做真实 GPU/CRT/输入验收。未生成 `acceptance.json`。

## 文件

- [逐条处置](reports/consistency-01/decisions.tsv) · [构建与回归](reports/consistency-01/BUILD.md) · [候选复核](review/candidate11-review.json)
- 台账：[editorial-r6-consistency-repairs.jsonl](../../translations/editorial-r6-consistency-repairs.jsonl)
- 工具：[build_consistency.py](tools/build_consistency.py) · [verify_consistency.py](tools/verify_consistency.py)
