# batch-15 清理工单：术语与按键名残留（1／1）

本批**不是新覆盖**：它不是「还没人读过的场次」，而是 R9 前三十批留下的少数写法。清单由 `tools/scan_residual_archive.py` 直接扫描 `candidate43` 的两个归档得到——因为同一句在 `cosmobreeder-multi.jar` 与 `patch.pak` 里各有一份，而快照只记录每 unit 的一行显示值，前批改了 jar 侧就把 pak 侧姊妹行留在了旧译上。

## 一、判据

每条只有一个动作：把少数写法换成多数写法。方向由库内频次定，不由偏好定：

| 少数写法 | 多数写法 | 频次 |
| --- | --- | --- |
| 狗头人 | 科博德 | 10 : 99 |
| 吠叫者 | 吠犬 | 1 : 40 |
| 探员 | 特工 | 3 : 471 |
| 宇航服 | 宇宙服 | 9 : 19 |
| 电击器 | 电击枪 | 10 : 92 |
| UP+攻击 | UP+ATTACK | 5 : 按键名一律保留英文（R9 batch-01 裁决） |
| DOWN+攻击 | DOWN+ATTACK | 2 : 同上 |
| 高级芯片 | 花哨芯片 | 1 : 3 |
| 卫星通讯 | 卫星链路 | 1 : 3 |

## 二、硬约束

1. 只换词：行首前缀（`  * `、`    Mauser: `、`text: `）、行尾、`|`、`[]`、`@DerekChipReport`、数字与按键名结构一律不动。
2. 同一句在 jar 与 pak 各一份，**两份都要改**；只改一份等于没改。
3. 不改词以外的措辞、不顺手润色、不合并行。
4. 频次接近时（如 9 : 19）仍按多数统一，但理由要写明频次；不能凭语感改。
5. 本批没有第二路逐行精校：清单是机械扫描 + 主代理裁决，另有一路独立复核（`batch-15/grok-review.md`）判断每处是否该改。

## 三、产出

- `localization/editorial/r9-polish/batch-15/orders/batch-15.json`：24 行待改（含 `current` 与 `archive_entry`）。
- `localization/editorial/r9-polish/batch-15/orders/batch-15.hits.json`：每行命中的少数写法。
- `localization/editorial/r9-polish/batch-15/review/decisions.tsv`：逐行裁决（采纳 24、驳回 0）。

## 四、本批不可外推

扫描只覆盖 `datadf/1`、`datadm/1`、`vsn/*`、`datav/1` 里的这九组写法。别的不一致（跨面命名、未终裁专名）见 [LEFTOVERS](../LEFTOVERS.md)，不在本批。
