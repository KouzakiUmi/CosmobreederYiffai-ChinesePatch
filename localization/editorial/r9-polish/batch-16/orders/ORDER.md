# batch-16 清理工单：专名统一 FENFEN（1／1）

本批与 batch-15 同类：不是新覆盖，是把库内已经定下来的专名补到还没跟上的三处。

## 一、依据

`FENFEN` 在库内已有中文写法「芬芬」，共 3 处：

- 词典条目 `ClassicFenfen`（`FENFEN` → `芬芬`）
- Starkill 卡面：`Traeh, a former Fenfen Elder` → 「Traeh曾是|芬芬长老」
- Dragon 卡面：`Fenfen Elder Sevaw` → 「芬芬长老 Sevaw」

仍然保留拉丁的三处，以及一处误译：

| 位置 | 现文 | 英文 | 处理 |
| --- | --- | --- | --- |
| `datadf/1` 3032 | 「关于 FENFEN 服装散落各处的报告」 | `REPORTS OF FENFEN OUTFITS` | `FENFEN` → `芬芬` |
| `datav/1`（jar）`SpecialNecklace` | 「翻译项链」 | `FENFEN T` | `翻译项链` → `芬芬 T` |
| `datav/1`（pak）同上 | 同上 | 同上 | 同上 |

## 二、判据

1. 专名统一按库内多数写法，不新造译名。
2. `T` 保留：英文是 `FENFEN T`，`T` 是型号／系列后缀，没有证据说明它指什么，不擅自展开。
3. 词典键名（`SpecialNecklace`、`ClassicFenfen`）是内部键，不改、不提案。
4. 同一值在 jar 与 patch.pak 各一份，两份都改。

## 三、产出

- `orders/batch-16.json`：3 行（1 行对白 + 2 个 JSON 值）。
- `review/decisions.tsv`：3 条裁决，全部 apply。

## 四、本批不可外推

只处理 FENFEN。其余专名（LIGHTTAZER、STARSUIT）与跨面命名问题见 [LEFTOVERS](../LEFTOVERS.md)。
