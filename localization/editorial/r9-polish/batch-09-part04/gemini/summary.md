# batch-09-part04 独立精校总结报告（路线：gemini）

## 一、工单与覆盖概况

- **工单正文**：`localization/editorial/r9-polish/batch-09-part04/orders/batch-09-part04.reader.md`（共 1,950 物理行）。
- **同源结构化数据**：`localization/editorial/r9-polish/batch-09-part04/orders/batch-09-part04.json`（共 228 场、398 行物理 ROW）。
- **覆盖统计**：实际完整读完 228 场，覆盖率 100%（`read_status: read_full` 228 场，无遗漏、无跳过、无重复 scene_id）。
- **产物位置**：
  - `localization/editorial/r9-polish/batch-09-part04/gemini/coverage.jsonl`
  - `localization/editorial/r9-polish/batch-09-part04/gemini/findings.jsonl`
  - `localization/editorial/r9-polish/batch-09-part04/gemini/summary.md`

---

## 二、发现总数及分级／归组分布

- **发现总数**：9 条
- **分级分布**：
  - **A 级（玩法硬约束）**：1 条
  - **B 级（术语／已裁决项统一）**：3 条
  - **C 级（行尾空格格式缺陷）**：5 条
  - **needs_evidence**：0 条
- **按 Root 归组清单**：
  1. `AreaA_Prison1`：1 条（C 级 1 条，P09-0401）
  2. `AreaA_Prison3`：1 条（B 级 1 条，P09-0402）
  3. `AreaB_Macsen1`：1 条（A 级 1 条，P09-0403）
  4. `AreaC_Prison1`：1 条（C 级 1 条，P09-0404）
  5. `AreaC_MacsenDark`：1 条（B 级 1 条，P09-0405）
  6. `AreaH_Cellar`：1 条（B 级 1 条，P09-0406）
  7. `AreaE_Macsen1`：3 条（C 级 3 条，P09-0407、P09-0408、P09-0409）

---

## 三、高风险连续段审校分析

1. **合句尾行与断点审校**：
   - 如 `AreaB_MacsenBar.Talk.main`（SFW46d5c882c95a6161d155409c / SFW0fb32b20f6ae7a6ba347309c）、`AreaH_Cellar.Talk.food`（CAT:O8a454fb14be4e625215b / CAT:O0ce93419dcb65fad68c9 等）、`AreaC_MacsenDark.DarkNoPurchase` 等场景中存在首行长句合并、次行物理留空的既有结构。经逐段连读，合并后的首行意思连贯完整，无硬粘语病，尾行保留为空，未误报漏译。
2. **玩法按键硬约束**：
   - 在 `AreaB_Macsen1.Talk.digging`（`SC261c757407969621`）中，当前译文将 `DOWN+ATTACK` 汉化成了 `DOWN+攻击`。按 reference-excerpt 第三节及 ORDER 硬约束，按键名不改，提出 A 级提案 P09-0403 恢复为 `DOWN+ATTACK`。
3. **行尾空格镜像核查**：
   - 严格以 `localization/catalog/units.jsonl` 中的英文原文 `source` 为准逐行查验。
   - SFW 版本的 `SC16c88d04e6435719` 英文原行末尾自带半角空格，中文末尾带空格属于排版镜像，判定合格保留；
   - NSFW 版本的 `SC58e6139ca98d3a1d`（CAT:O5646682bc67cfdf29f8c、CAT:Ofeca87bcb892b8bd239e）以及 `SCb810ac30e6045f70`、`SC937701d5b4d26497`、`SCe1411891da18e1a5` 英文原行均无空格，中文多出尾随空格，确认为格式缺陷，提提案去除。

---

## 四、男女两版不一致清单

1. **`AreaH_Cellar.Talk.food` 探员 vs 特工**：
   - 女线 `SC7e74bd0d0fa2d0ea`（CAT:Oe6e54de8abdcdade680d）：译为“你们这种特工”，符合 R2 裁决；
   - 男线 `SCcb0a76aad6da4b24`（SFW1358957567e6edf09b099433）：原译为“你们这种探员”，残留旧译。提出 P09-0406 纠正为“特工”。
2. **`AreaB_Macsen2.Talk.macsenmoneycode1` 语气差异**：
   - 女线 `SCc3ad59fdff3438ca`：`钱都拿了，还不快滚，小混混？`
   - 男线 `SCd0245ca0662e436c`：`接下来你怎么不走人呢，啊，小混混？`
   - 判定：两处表述均通顺且贴合麦森被洗劫后的抓狂语气，保留差异。
3. **`Test_Hacker1.Meeting` 原文人名**：
   - 女线测试场景 `SC4740dd505f30d827`（`datadf/all.ds`）中，英文原文为 `Greetings, Yiffai.`（男主名）。译文忠实对应，未做私自臆测修改。

---

## 五、未覆盖项与本工单不能证明的事项

1. **未终裁术语**：
   - 如 `LIGHTTAZER`（光电击枪 / 激光电击枪）按 ORDER 口径不提案修改，维持当前文本不变。
2. **实机渲染与折行**：
   - 本工单提案均保持单行在 20 个汉字左右（或与当前物理行长一致），未引入超长单行；最终视觉折行与剧情框（240px）适配需结合实机测试验证。
