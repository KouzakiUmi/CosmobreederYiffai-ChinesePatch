# R9 精校遗留项台账（滚动记录）

在 R9 已落地批次与当前批次之间发现的、**不属于任何已定义批次**的一致性问题。记录在此，等全批次落地后统一处理；不擅自扩大批次范围。

## 一、术语分叉残留（库内计数取 `snapshot-03`）

| 词条 | 主流写法（条数） | 残留写法（条数） | 残留位置 | 现状 |
| --- | --- | --- | --- | --- |
| kobold | 科博德（99） | 狗头人（10） | `Tomcat.Kobo`、`Tomcat.KoboPickup`、`TomcatItems.StatCream`、`TomcatItems.SpecialLeftmark/Rightmark` 的 **patch.pak 侧副本**，以及 `AreaA_Prison3`、`AreaB_Prison1` | batch-02／06 只改了 jar（`cosmobreeder-multi.jar`）侧同名行，pak 侧副本未改；`AreaA_Prison3`／`AreaB_Prison1` 落在 batch-09-part03／part04 范围内，本批处理 |
| agent | 特工（471） | 探员（3） | `AreaH_Cellar.Talk.food`（两版侧各一）、另一处见下 | batch-09-part03／part04 范围内各改一处 |
| BARKER | 吠犬（40） | 吠叫者（1） | `AreaA_Prison3.GoodbyeDog` | batch-09-part03 处理 |
| cosmo fellas | 太空伙计（4） | 宇宙来的家伙（2） | `AreaB_MacsenBar` 一带 | batch-09-part03 处理一处，其余待核 |
| Cosmosuit | 宇宙服（19） | 宇航服（9） | 多处 | batch-02 已改 jar 侧一处，batch-09-part03／part04 各改一处 |

**教训**：同一句在 jar 与 pak 两侧各有一份（HANDOFF 第五节已记），改一侧不会影响另一侧；R9 早期批次改了 jar 侧就以为改完了，pak 侧副本因此留存旧译。后续批次要按 `occurrence_id` 查同文姊妹行，两侧一起改。

## 二、待办

- pak 侧 `Tomcat*`／`TomcatItems*` 的 8 处 `狗头人`：不在任何已定义批次内，需要单独的清理批次。
- 其余术语分叉（`LIGHTTAZER` 命名、`STARSUIT`／`Cosmosuit` 是否同一件、`FENFEN` 中文名）仍未终裁，见 [HANDOFF](../HANDOFF.md) 第二节。
