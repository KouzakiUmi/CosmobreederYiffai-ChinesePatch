# batch-15 独立复核

24 条里 **15 条采纳、9 条驳回、0 条存疑**。九条驳回都不是结构问题：拟改相对现文都只换了命中词，行首前缀、行尾、`|` 与方括号未动。驳回原因是少数写法并不是清单所写的那个词：五条 `电击器` 实际是未终裁的 LIGHTTAZER，四条 `宇航服` 的英文是普通 space suit／spacesuit，不是 COSMOSUIT。

核对范围：`orders/batch-15.json` 与 `review/decisions.tsv` 的 24 个 `row_id` 一一对应；`orders/batch-15.hits.json` 的命中词代入现文后与 `final_zh` 逐字相同。英文对照 `localization/catalog/units.jsonl`，以及 batch-08／09 工单里带 `source` 的同句。未读候选归档明文。

裁决理由里反复出现的「同一句在 jar 与 patch.pak 各有一份，两份都改」对只出现一侧的行不成立：另一侧已不含该少数写法，所以没进本批。这不改变下表对已列出那一侧的判定。

| row_id | 现文 | 拟改 | 判定 | 理由 |
| --- | --- | --- | --- | --- |
| `P15:cosmobreeder-multi.jar:datadf/1:487` | `  * 想当太空海盗吗？你需要的只是这把官方海盗光电击器！` | `  * 想当太空海盗吗？你需要的只是这把官方海盗光电击枪！` | 驳回 | 英文是 Official Pirate Lighttazer，不是 TAZER。`电击器` 只是 `光电击器` 的子串；LIGHTTAZER 中文名未终裁，不能改成另一套未定写法。 |
| `P15:cosmobreeder-multi.jar:datadf/1:1504` | `  * 太空行走最糟的，就是得穿宇航服。` | `  * 太空行走最糟的，就是得穿宇宙服。` | 驳回 | 英文是 a space suit（AreaE_Macsen1.Talk.mags），不是 COSMOSUIT。改成「宇宙服」会把泛称坐实成装备专名。 |
| `P15:cosmobreeder-multi.jar:datadf/1:2292` | `  Yiffany: [它在说：“按 SELECT 选择你的超能力，然后同时按下 UP+攻击，激活你选定的能力！”]` | `  Yiffany: [它在说：“按 SELECT 选择你的超能力，然后同时按下 UP+ATTACK，激活你选定的能力！”]` | 采纳 | 英文是 BY PRESSING UP+ATTACK。玩家可见，但原文是英文键名，不是中文原文；只换键名。 |
| `P15:cosmobreeder-multi.jar:datadf/1:2444` | `  Yiffany: [当然！只要我没选中什么花哨能力，就可以按 UP+攻击 射出钩子，然后在天花板上荡过去！]` | `  Yiffany: [当然！只要我没选中什么花哨能力，就可以按 UP+ATTACK 射出钩子，然后在天花板上荡过去！]` | 采纳 | 英文是 PRESS UP+ATTACK TO LAUNCH A HOOK。同上，只换键名。 |
| `P15:cosmobreeder-multi.jar:datadf/1:2447` | `  Tomcat: [就————是这样，只要没选中你那些古怪能力，按 UP+攻击，就能轻松荡过那段缺口。]` | `  Tomcat: [就————是这样，只要没选中你那些古怪能力，按 UP+ATTACK，就能轻松荡过那段缺口。]` | 采纳 | 英文是 JUST PRESS UP+ATTACK。拉长音与句意不动。 |
| `P15:cosmobreeder-multi.jar:datadf/1:4287` | `  Tomcat: [就————是这样，只要没选中你那些古怪能力，再按 UP+攻击，你就能轻松荡过任何缺口。]` | `  Tomcat: [就————是这样，只要没选中你那些古怪能力，再按 UP+ATTACK，你就能轻松荡过任何缺口。]` | 采纳 | 同上一句的另一处复述，英文仍是 UP+ATTACK。 |
| `P15:cosmobreeder-multi.jar:datadm/1:471` | `  * 想当太空海盗吗？你只需要这把官方海盗光电击器！` | `  * 想当太空海盗吗？你只需要这把官方海盗光电击枪！` | 驳回 | 与 datadf L487 同句，英文仍是 Official Pirate Lighttazer。子串替换不能当 TAZER 统一。 |
| `P15:cosmobreeder-multi.jar:datadm/1:621` | `  * 也许你用电击器打一下，就能扰乱它……？` | `  * 也许你用电击枪打一下，就能扰乱它……？` | 采纳 | 英文是 disrupt it with a tazer strike，是独立的 tazer，不是 LIGHTTAZER。 |
| `P15:cosmobreeder-multi.jar:datadm/1:1502` | `  * 太空行走最糟的，就是得穿宇航服。` | `  * 太空行走最糟的，就是得穿宇宙服。` | 驳回 | 与 datadf 太空行走句同文，英文是 a space suit，不是 COSMOSUIT。 |
| `P15:cosmobreeder-multi.jar:datadm/1:4317` | `  Yiffai: [当然！只要没选什么花哨的能力，我就可以按 UP+攻击 射出钩子，挂在天花板上荡来荡去！]` | `  Yiffai: [当然！只要没选什么花哨的能力，我就可以按 UP+ATTACK 射出钩子，挂在天花板上荡来荡去！]` | 采纳 | 男线同句，英文是 UP+ATTACK。只换键名。 |
| `P15:cosmobreeder-multi.jar:datadm/1:4823` | `  * 你好，伊吠。你不认识我，不过我偷偷窥探了你的卫星通讯。` | `  * 你好，伊吠。你不认识我，不过我偷偷窥探了你的卫星链路。` | 采纳 | 英文是 snooped your satlink。part04 已把名词定为「卫星链路」；本行只换名词。 |
| `P15:cosmobreeder-multi.jar:datadm/1:4825` | `  * 很简单：把你在外头找到的那些高级芯片带给我，我就替你破解门锁！这不是双赢嘛！` | `  * 很简单：把你在外头找到的那些花哨芯片带给我，我就替你破解门锁！这不是双赢嘛！` | 采纳 | 英文是 fancy chips。part04 驳回的是改成「高级」，不是维持「高级」。只换这一个词，不重开整句口径。 |
| `P15:cosmobreeder-multi.jar:vsn/167:6` | `text: 要是给我把好点的电击器，而不是这套弱得可怜的见习装备，我大概一击就能放倒你。` | `text: 要是给我把好点的电击枪，而不是这套弱得可怜的见习装备，我大概一击就能放倒你。` | 采纳 | 英文是 a better tazer。`text: ` 前缀未动。 |
| `P15:cosmobreeder-multi.jar:vsn/47:17` | `text: 瞧瞧，这是什么……我的光刃电击器！` | `text: 瞧瞧，这是什么……我的光刃电击枪！` | 驳回 | 英文是 my lighttazer。改成「光刃电击枪」仍是未终裁的 LIGHTTAZER 写法，不是 TAZER→电击枪。 |
| `P15:cosmobreeder-multi.jar:vsn/53:7` | `text: 我能成为最精锐的特工之一，可不是靠乱挥电击器！` | `text: 我能成为最精锐的特工之一，可不是靠乱挥电击枪！` | 采纳 | 英文是 sloppy tazer-play。句中「特工」已是多数写法，不必再动。 |
| `P15:patch.pak:datadf/1:487` | `  * 想当太空海盗吗？你需要的只是这把官方海盗光电击器！` | `  * 想当太空海盗吗？你需要的只是这把官方海盗光电击枪！` | 驳回 | jar 侧同句。英文仍是 Official Pirate Lighttazer。 |
| `P15:patch.pak:datadf/1:1483` | `    * 不穿宇航服就往外跑，你胆子可真大！` | `    * 不穿宇宙服就往外跑，你胆子可真大！` | 采纳 | 英文虽写 spacesuit，但这句在 `!inCosmoSuit()` 分支里；part03 已把男线姊妹句改成「宇宙服」。四个空格前缀保留。不能拿这条给其余宇航服开绿灯。 |
| `P15:patch.pak:datadf/1:1502` | `  * 太空行走最糟的，就是得穿宇航服。` | `  * 太空行走最糟的，就是得穿宇宙服。` | 驳回 | 与 jar 侧太空行走句同文，英文是 a space suit。没有 `inCosmoSuit()` 条件。 |
| `P15:patch.pak:datadm/1:470` | `  * 想当太空海盗吗？你只需要这把官方海盗光电击器！` | `  * 想当太空海盗吗？你只需要这把官方海盗光电击枪！` | 驳回 | jar L471 的 pak 侧同句，英文仍是 Official Pirate Lighttazer。 |
| `P15:patch.pak:datadm/1:1342` | `  * 用不着你的电击器了！接下来交给我！` | `  * 用不着你的电击枪了！接下来交给我！` | 采纳 | 英文是 your tazer。part02 把它改成了少数写法；本批是独立清理台账，回退成立。 |
| `P15:patch.pak:datadm/1:4970` | `  * 你好，伊吠。你不认识我，不过我偷偷窥探了你的卫星通讯。` | `  * 你好，伊吠。你不认识我，不过我偷偷窥探了你的卫星链路。` | 采纳 | jar L4823 的 pak 侧。英文是 satlink，只换名词。 |
| `P15:patch.pak:datadm/1:4972` | `  * 很简单：把你在外头找到的那些高级芯片带给我，我就替你破解门锁！这不是双赢嘛！` | `  * 很简单：把你在外头找到的那些花哨芯片带给我，我就替你破解门锁！这不是双赢嘛！` | 采纳 | jar L4825 的 pak 侧。英文是 fancy chips，只换词。 |
| `P15:patch.pak:vsn/59:7` | `text: 我连宇航服都刚穿惯，就摊上这烂摊子。` | `text: 我连宇宙服都刚穿惯，就摊上这烂摊子。` | 驳回 | 英文是 wearing a spacesuit。没有 cosmosuit 条件，不能改成装备专名。 |
| `P15:patch.pak:datav/1:ui.data.m_AgentM02.desc` | `强势的上位猫探员，\|迎战来犯之敌！` | `强势的上位猫特工，\|迎战来犯之敌！` | 采纳 | 这句英文是 TOP CAT，没有 agent；`探员` 是卡面多出来的职衔，不是专名。同库 `m_AgentM05` 的 TOP AGENT 已作「上位特工」。竖线保留。 |

## 漏掉的同类残留

没有能坐实的、本批扫描范围内漏收的同类行。

查过的三处：

1. `units.jsonl` 里 `DOWN+ATTACK` 有两句英文（女线 `datadf` `AreaB_Macsen1.Talk.digging`、男线 `datadm` 同场）。口径表写了 `DOWN+攻击`→`DOWN+ATTACK`，但 `batch-15.hits.json` 零命中。batch-09-part01／part04 已经把当时见到的两侧改成 `DOWN+ATTACK`。未读候选归档明文，不能证明 candidate43 里还留着第三种写法。
2. `狗头人`、`吠叫者` 也在口径表里，hits 同样为零。`LEFTOVERS.md` 里 pak 侧 8 处「狗头人」是 candidate35 前后的旧计数；本次扫描覆盖 `datadf/1`、`datadm/1`、`vsn/*`、`datav/1`，零命中说明这四个 root 的 candidate43 文本里已经扫不到这两个词。未把旧台账当成仍在的漏项。
3. 太空行走句的英文（`units.jsonl`：having to wear a space suit）和海盗商店句的英文（Official Pirate Lighttazer）都在 order 内，不是漏行；它们是被收进来、但不该按多数写法改的反例，已在上表驳回。
