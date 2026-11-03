# R9 遗留项台账（滚动记录）

在 R9 已落地批次与当前批次之间发现的、**不属于任何已定义批次**的一致性问题，以及本轮发现并被推翻的反向改动。记录在此，等全批次落地后统一处理；不擅自扩大批次范围。

计数口径：以 `snapshot-03`（候选 candidate13 基线）的中文显示行为准，再扣掉本轮 batch-09-part03／part04 已落地的操作；`candidate35` 之后的真实数字需重新扫描确认。

## 一、术语分叉残留

| 词条 | 主流写法 | 残留写法与位置 | 本轮变化 |
| --- | --- | --- | --- |
| kobold | 科博德（99） | 狗头人 8 处：`Tomcat.Kobo`、`Tomcat.KoboPickup`、`TomcatItems.StatCream`、`TomcatItems.SpecialLeftmark`／`SpecialRightmark` 的 **patch.pak 侧副本** | batch-02／06 只改了 jar 侧同名行；本轮 part03（`AreaB_Prison1`）、part04（`AreaA_Prison3`）各改 1 处，10 → 8 |
| BARKER | 吠犬（40） | 吠叫者：0 | part03 改掉唯一一处（`AreaA_Prison3.GoodbyeDog`） |
| agent | 特工（471） | 探员：`ui.data.m_AgentM02`「强势的上位猫探员」1 处（batch-10 范围内）；`AreaH_Cellar.Talk.food` 两侧各 1 处已由 part03／part04 改掉 | 3 → 1 |
| Cosmosuit | 宇宙服（19） | 宇航服 7 处 | part03、part04 各改 1 处（9 → 7） |
| tazer | 电击枪（92） | 电击器 10 处，其中 `patch.pak datadm/1` L1342 是 **batch-09-part02 反向改出来的**（本轮 part04 改了另一处，仍留这一处） | 需在清理批次里回退 |
| 按键名 | `UP+ATTACK`／`DOWN+ATTACK` | `UP+攻击` 5 处、`DOWN+攻击` 1 处（`AreaB_Macsen1.Talk.digging` 的另一侧；`Tomcat`、`TomcatItems`、`Mauser` 一带） | part04 改掉 1 处（7 → 6）；R9 batch-01 已定按键名原样保留 |
| fancy chips | 花哨芯片（3 个平行变体） | 高级芯片 1 处（`Hacker_Shared.Meeting` 的另一侧） | part04 驳回了「改成高级」的提案，整句口径待终裁 |
| satlink | 卫星链路（3 个平行变体） | 卫星通讯 1 处 | part04 只改了动词，名词未统一 |
| 大壮兽资料卡 | sfw 侧作「大壮兽1／大壮兽2」（各 2 处） | nsfw 侧仍是裸 ID `BIGBOLD1`／`BIGBOLD2`（各 2 处） | batch-10-part01 未改：改名会让 `BIGBOLD1` 这一标记 token 消失，`editorial_repairs` 按标记漂移整批拒绝；要改须由引擎层放行 |

**教训**：同一句在 jar 与 pak 两侧各有一份（HANDOFF 第五节已记），改一侧不会影响另一侧；R9 早期批次改了 jar 侧就以为改完了，pak 侧副本因此留存旧译。后续批次要按 `occurrence_id` 查同文姊妹行，两侧一起改。

## 二、待办

1. pak 侧 `Tomcat*`／`TomcatItems*` 的 8 处 `狗头人`、6 处按键名中文化、7 处 `宇航服`、9 处 `电击器`：不在任何已定义批次内，需要单独的清理批次。
2. batch-10-part03 的 `CosmoCardEnelye.desc` 是多行 JSON 值，行尾空格无法写进行式裁决表，本批按 `reject` 记录下来，交由清理批次改用其他写入方式处理。
3. 界面卡面（`ui.card.*.desc`）的值尾多出一个换行符而英文源没有（batch-10-part01 的 8 行全部如此）：引擎对 JSON 值强制换行计数不变，台账改不了，属构建层／引擎层问题。
4. `patch.pak datadm/1` L1342 的回退（`电击器`→`电击枪`）要有独立台账，不能借某批的正文改动顺手改。
5. 其余术语分叉（`LIGHTTAZER` 命名、`STARSUIT`／`Cosmosuit` 是否同一件、`FENFEN` 中文名、`花哨芯片` 整句口径）仍未终裁，见 [HANDOFF](../HANDOFF.md) 第二节。
