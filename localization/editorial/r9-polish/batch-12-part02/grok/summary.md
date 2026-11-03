# batch-12-part02 精校摘要（第二路）

## 输入与覆盖

- 工单正文：`localization/editorial/r9-polish/batch-12-part02/orders/batch-12-part02.reader.md`，1013 行。
- 结构化数据：同目录 `batch-12-part02.json`。口径：`ORDER.md`、`reference-excerpt.md`。
- 实际读完 158 场，`coverage.jsonl` 158 行，`scene_id` 不重复，与工单场景一一对应。ROW 219 行，与工单 JSON 行数一致。`read_status` 全部为 `read_full`。
- 分段边界上的 `ClassicBarker`、sfw `PsySyrup` 在下一段补全后再记覆盖，没有半场落盘。

## 发现分布

共 11 条，全部 `status=proposal`。无 C，无 `needs_evidence`。

| 严重度 | 条数 | finding_id |
| --- | --- | --- |
| A | 5 | P12-X207、P12-X208、P12-X209、P12-X210、P12-X211 |
| B | 6 | P12-X201～P12-X206 |
| C | 0 | — |
| needs_evidence | 0 | — |

覆盖结果：`issues_found` 16 场，`retain` 142 场。

### 按 root

- **A／meaning**
  - `ClassicKingbold`：`KINGBOLD`→「胆王」把 BOLD 读成胆大。提案「大壮兽王」。依据是词典 `BIGBOLD`→「大壮兽」（part01 `CAT:Ob5ef84e4b12bfd979d15`）与任务头「击败大壮兽」（part03 `CAT:Oa424abe291aebc51b005`）。键名不改。
  - `StatPretzel`：`BAKED FRESH` 被译成「育得正好」。提案「扭结面包|新鲜出炉」。短名「椒盐卷」不动。
  - `SpecialNecklace`：`FENFEN T`→「翻译项链」漏了专名，并写入键名里的「项链」。提案「Fenfen译」。Fenfen 不改成芬芬；描述行不动。part03 同值 `CAT:Oc6746404d822070b9956` 一并列入。
- **A／gameplay**
  - `SpecialRadio`：`SELECT` 译成「选择」。提案「按 (SELECT)|进行通讯」。part01 sfw 同句已留 SELECT（`SFW9c8e090c508293aaaf7d3076`）。
  - `SpecialShoes`：nsfw 把 `DOWN+JUMP` 译成「下+跳跃」。提案与本批 sfw 同文「空中按DOWN+JUMP|使出俯冲踢！」。`SHOES`→「鞋子」两侧已一致，不改。
- **B／term**
  - `/missionLog/female/6/header`：`ACQUIRED ANOMALY ALPHA`→「已获取异常体 ALPHA」。女线 4 条「已获取异常体」、男线 4 条「已获得异常」，持平。全批 `ACQUIRED` 任务头里「获得」14 条。提案「获得异常 ALPHA」。拉丁字母不改成词典「阿尔法」。
- **B／format**（只删英文 source 没有的行尾，占位正文不润色）
  - 短 lorem 五场带三空格加行尾换行：女线/4、/7 text，男线/2、/5、/8 text（P12-X201）。女线/9 text 只有三空格（P12-X202）。判据是 `units.jsonl` 的 `source`（女 `Ue731848430007098930b`、男 `U9bb19863f47c9f910721`），不是 `occurrences.trailing_ws`。
  - `Line 1|Line 2…` 女线/1、男线/1 text：段数一致，只多一个行尾换行（P12-X203）。
  - 女线/11 `Stub: Tomcat bio` 多一个行尾换行（P12-X204）。用词「待补：雄猫简介」成立。
  - 男线/13 实文多一个行尾换行（P12-X205）。正文跟随英文，不改。

## 高风险段

1. 按键名：`SpecialRadio` 的 SELECT、`SpecialShoes` 的 DOWN+JUMP。照现译操作会对不上键帽。part01 `SpecialBrace` 的 nsfw 也把 `DOWN+JUMP` 译成「下+跳跃」（`CAT:O68dead41d2c6239e8c09`），是另一句，未并入本条替换。
2. `ClassicKingbold`：敌人短名会指错物种。
3. `StatPretzel`：食物说明读成培育。
4. `SpecialNecklace`：物品短名不再指向 Fenfen。
5. 男线/13 任务日志是本批唯一实文，行尾多一空行；女／男 `ACQUIRED ANOMALY` 模板也不一致。

无线电套语、问答错位、合句断点：本批没有对话场。`|` 段数没有被提案改动。

## 男女两版与两侧

本批男／女任务日志里，地名与字段名一致，不单列提案：泽罗尼亚、艾斯卡姆尔、仓库B、总部、任务、活体样本、击败狼犬、获得泽纳图形、获得战斗电击枪。

不一致：

- `ACQUIRED ANOMALY {字母}`：女线「已获取异常体」，男线「已获得异常」。本批只有女线 ALPHA 一行，男线四行在 part01／part03，row_id 已写入 P12-X206。
- 男线/13 英文本身写 Yiffany（还有笔误 `ger ship`）。译文作伊吠妮，是跟随原文，不是把伊吠译错。不提案改名。
- `ClassicStarkillV2Male` 的值是 `YIFFANY?`，`ClassicStarkillV3Female` 的值是 `YIFFAI`。译文跟随值，不按键名里的 Male／Female 对调。

sfw／nsfw：FakeMeat、PirateBody、PsySyrup、VitDrumstick、KOBOSUIT、STARHELM、OMEGOBIN、CANNON、卡牌编号等同文。真正分叉是 `SpecialShoes` 的按键名。`SpecialFap.OmegobinBuff` 英文行尾一格空格，中文「幸运 」是镜像，不删。

## 明确不提案

- 键名（`ClassicBarker`、`Bomb`、`SpecialHookshot` 一类）不改。
- Zener 形状词条名：`STAR`→「星星」、`WAVES`→「波浪」未改。R4 写 ZenerWaves＝泽纳波、波形不用波浪；派单把形状词条名列为未终裁，故只记录张力，不提案。任务头里的「泽纳波／星形／十字／方形／三角形」沿用现译。
- `FENFEN` 不改芬芬，也不把描述里的 Fenfen 改掉。
- `LIGHTTAZER`、`STARSUIT`、Traeh／Sevaw／Erauqs、引号体例：本批没有可改的终裁项，未动。
- `LIVEWARE`→「活体样本」是用户已决定的任务主题名，不重提。
- `LECT`、`500 LECT`、`UP+ATK` 一类按键以外的已裁决保留项，维持原样。
- 占位样例（`Line 1|…`、lorem、`Stub:`、`Test Werepup`）只处理行尾，不润色。
- `RAPER`→「强奸者」跟随值的性化拼写；描述「细剑」承担刺剑义。不改回细剑，也不新造双关。
- `FERAL-SIZED|SHIPPING LABEL.` 本批与 part03 都是「兽形尺寸的|货运标签。」。参照摘录写 feral＝野兽，与这两条语料冲突。两条彼此一致，不单改一侧。

## 未覆盖与本工单不能证明的东西

- 未启动游戏，未量像素宽。短标签只按英文字符长作上限；全角双宽是否顶格，工单不能证明。`欧米茄哥布林`、`双足飞龙` 等已落地且两侧同文的写法没有为了变短而改。
- 行尾换行是否在实机多出一空行，只凭快照 `current_line` 与 `units.jsonl` source 的换行数差，没有运行时证据。
- 男线日志里的 Yiffany、`ger`，以及 Starkill 键名性别与显示名对调，是原文事实。工单不能证明作者本意是不是写错分支。
- Zener 形状词条的终裁名、Fenfen 的中文名、`FERAL` 在全库是「野兽」还是「兽形」占多数：本工单的两条货运标签不足以终裁。
- 未改归档、未写台账、未跑构建。其它 part 的行只作对照，提案的 `proposed_zh` 只替换本批对应行。
