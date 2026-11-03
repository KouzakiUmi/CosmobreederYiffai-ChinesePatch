# batch-12-part03 精校小结（grok，第二路）

## 覆盖

- 工单正文：`localization/editorial/r9-polish/batch-12-part03/orders/batch-12-part03.reader.md`，1009 行。
- 结构化数据：`orders/batch-12-part03.json`，158 场、218 行。
- 实际读完：158 场，`read_status` 全部为 `read_full`。`coverage.jsonl` 158 行，scene_id 与工单顺序一致、不重复。
- 未覆盖：无。

## 发现分布

共 7 条，全部为提案。A 0，B 7，C 0，needs_evidence 0。

| finding | root | 级别 | 类别 |
| --- | --- | --- | --- |
| P12-0301 | `/missionLog/male/6/header`（同改 male/7、male/9） | B | term |
| P12-0302 | `/missionLog/male/7/header`（同改 male/6、male/9） | B | term |
| P12-0303 | `LuckyBodyNotUpgraded`（nsfw／sfw 两行） | B | term |
| P12-0304 | `SpecialHookshot` | B | gameplay |
| P12-0305 | `SpecialNecklace`（nsfw／sfw 名称行） | B | meaning |
| P12-0306 | `StatFortune` | B | meaning |
| P12-0307 | `StatFishtaco` | B | meaning |

`coverage.jsonl` 里 `issues_found` 9 场：异常 header 3 场同时挂 0301 与 0302；LuckyBodyNotUpgraded 两侧 2 场挂 0303；其余 4 场各挂一条。retain 149 场。

## 高风险连续段

1. 男线异常 header（male/6 ALPHA、male/7 BETA、male/9 OMICRON）是同一家族的连续缺口：名词缺「体」，等级名留拉丁。两条判点分开，不要合成一句再审。女线 female/6 不在本批，改完男线后它会变成唯一的「已获取异常体 ALPHA」。
2. 钩爪用法行是控制提示。sfw 已保留 `UP+ATK`，本批 nsfw 译成了「上+攻击」。只改本批这一行。
3. 任务日志 `text` 里的 Line N 与 lorem 占位，结构已对过 `|` 段数和连字符断行，行尾与英文 raw 载荷一致，全部 retain。没有问答错位，也没有无线电套语。

## 男女两版

本批任务日志男女同文的地名和栏名没有分叉：泽罗尼亚、艾斯卡姆尔、斯凯菲亚、仓库B、总部、任务、活体样本、击败大壮兽、击败狼崽。

真正的男女 header 分叉不在「同一英文两种中文」的地名上，而在异常 header：

| 英文 | 女线快照 | 男线本批 |
| --- | --- | --- |
| ACQUIRED ANOMALY ALPHA | female/6「已获取异常体 ALPHA」（不在本批，CAT:O8e693539f4176a2c26f8） | 「已获得异常 ALPHA」 |
| ACQUIRED ANOMALY BETA／OMICRON | 女线快照原为「已获取异常体 …」；台账 R9-0003／R9-0006 已改成「已获得异常体 贝塔／奥密克戎」 | 仍是「已获得异常 BETA／OMICRON」 |

P12-0301 只补「体」，P12-0302 只改等级名。同时采纳时三行应为「已获得异常体 阿尔法／贝塔／奥密克戎」，等级名前留一空格，对齐已落地的 R9-0009。动词保持男线的「已获得」，不抄女线快照里的「已获取」，也不收成 Zener header 的「获得」。

`ClassicStarkillV2Female` 的值是 `YIFFAI?`，译「伊吠？」。英文不是 YIFFANY，不改成伊吠妮。

`TazerTrainee`、`StatPepper` 的男女／两侧描述英文本身不同（VIRGIN／NEW，JUST FOR YOU／BUT ADDICTIVE），不是漏译，不互抄。

## 两侧（sfw／nsfw）

- 已提案：`GET A FEELING|SO COMPLICATED`（P12-0303）、`UP+ATK WITHOUT|PSY ABILITY ON`（P12-0304）、`FENFEN T`（P12-0305，两侧同误）。
- 未提案：`FENFEN` 一侧 Fenfen、一侧芬芬。中文名未终裁，不互改。
- 抽过同英文的条目（卡牌、加农炮、钩爪、科博服、头冠、三角帽、咖啡、哨子、调谐、见习、旧杂货、制式配发）两侧一致，retain。

## 对过但不提案

- 行尾空格：有 occurrence 的行用 `units.jsonl` 的 `source` 加 raw 载荷哈希核对；无 occurrence 的 SFW 行用工单 JSON 的 `source`。中文行尾与英文 raw 一致的镜像不删。`occurrences.jsonl` 的 `trailing_ws` 未当作判据。
- Zener 形状词：任务日志「圆形／方形／波」与词典 `ZenerCircle`＝圆圈。形状词条名未终裁，不提案。
- `STARSUIT`＝星装、`Traeh-XE`、引号体例：未终裁，不提案。本批没有 LIGHTTAZER、Sevaw、Erauqs 的值要改。
- `TORCH`＝手电筒。摘录写 R2「手电」，语料和两侧词典都是手电筒。按工单以语料为准，不改；冲突记在这里。
- `PSY` 恢复行作「精神力」。摘录「精神水晶」与台词里的「精神力水晶」冲突，本批值不是 PSY CRYSTAL，不改。
- `HARD KNOTTED|BRED` 保持食物读法。不改用「肉结」，避免把双关收成加性化。
- 内部键（`ClassicBulber` 一类，以及本批的 `area`、`SpecialHookshot` 等 root）不改。

## 本工单不能证明的东西

- 任何提案的像素宽、卡面是否折行、实机是否装得下。字符数都未超过对应英文；没写「行宽待实测」。
- 女线 female/6 和词典 sfw 侧不在本批的行，只在 note 里点了 row_id，不能由本工单直接改。
- 占位 lorem／Line N 的开发用途之外，玩家会不会看到这些行。
- 已落地台账 R9-0003／0004／0006／0009 是否已经打进当前可玩构建。判据用的是台账新值和词典条目名，不是本批快照里的旧行。
