# batch-02（雄猫支援线）双路精校报告（Gemini 路）

## 一、工单输入与执行基线

- **工单输入**：
  - 正文文件：`localization/editorial/r9-polish/batch-02/orders/batch-02.reader.md`（共 1873 行）
  - 结构化数据：`localization/editorial/r9-polish/batch-02/orders/batch-02.json`（共 6581 行，56 场，566 物理行）
  - 参照基准：`reference-excerpt.md`（雄猫多面语域、称呼矩阵、术语表、容器折行限制）
- **阅读与覆盖**：
  - 实际读完场景数：**56 场**（全覆盖，无截断，无抽样）。
  - 覆盖统计：**36 场** 发现待改进判点（`issues_found`），**20 场** 语义口吻准确予以保留（`retain`）。
  - 合句尾行处理：本批共有 118 个 `current` 为空的 ROW，严格确认为既有合句尾行，未报漏译，未做填充。

---

## 二、发现总数与分级分布

本次精校共产出 **63 条** 独立判点提案：
- **A 类（严重误译/玩法损坏/结构破坏）**：**3 条**
- **B 类（术语漂移/称谓统一/翻译腔/语域口吻）**：**60 条**
- **C 类（纯节奏文笔打磨）**：**0 条**（无强理由不凑数）
- **needs_evidence（存疑留证）**：**0 条**（上下文与触发机制清晰）

### 按 Root 场景分布统计

| Root 场景分类 | 场次数 | 发现总数 | A 类 | B 类 | C 类 |
| :--- | :---: | :---: | :---: | :---: | :---: |
| `Tomcat.Area0_First_CosmoCard noselect` | 4 | 3 | 0 | 3 | 0 |
| `Tomcat.Area0_map16_a noselect noamendfreq` | 4 | 2 | 0 | 2 | 0 |
| `Tomcat.AreaA_map42_a noselect` | 3 | 3 | 0 | 3 | 0 |
| `Tomcat.AreaB_map03_a noselect` | 2 | 1 | 0 | 1 | 0 |
| `Tomcat.AreaC_map45_a noselect` | 2 | 4 | 2 | 2 | 0 |
| `Tomcat.AreaC_map56_a noselect noamendfreq` | 4 | 0 | 0 | 0 | 0 |
| `Tomcat.AreaC_map64_b noselect` | 3 | 12 | 0 | 12 | 0 |
| `Tomcat.AreaH_map02_a noselect` | 4 | 11 | 0 | 11 | 0 |
| `Tomcat.AreaX_fenfen_rescued noselect` | 2 | 4 | 0 | 4 | 0 |
| `Tomcat.Feral noselect noamendfreq` | 3 | 4 | 0 | 4 | 0 |
| `Tomcat.FeralPickup noselect noamendfreq` | 3 | 0 | 0 | 0 | 0 |
| `Tomcat.GenderSwapped noselect noamendfreq` | 2 | 2 | 0 | 2 | 0 |
| `Tomcat.GenderSwappedPickup noselect noamendfreq` | 2 | 2 | 0 | 2 | 0 |
| `Tomcat.Kobo noselect noamendfreq` | 4 | 5 | 1 | 4 | 0 |
| `Tomcat.KoboPickup noselect noamendfreq` | 4 | 6 | 0 | 6 | 0 |
| `Tomcat.NoteFrequency noselect` | 2 | 0 | 0 | 0 | 0 |
| `Tomcat.Slime noselect noamendfreq` | 3 | 4 | 0 | 4 | 0 |
| `Tomcat.SlimePickup noselect noamendfreq` | 3 | 0 | 0 | 0 | 0 |
| `Tomcat.TestA` | 2 | 0 | 0 | 0 | 0 |
| **合计** | **56** | **63** | **3** | **60** | **0** |

---

## 三、高风险连续段与核心判点分析

### 1. 道具与英美口语双关破损（A 类重灾区）
- **场景**：`SCbef498a71645cdb4`（`AreaC_map45_a`，男线）
- **问题**：主角手持电子手电筒（Tomcat 前一句明确指出读数乱套），波苏作为老派英式军官用英式英语词汇 `torch`（手电筒）代指（`A FLICKERING TORCH AND SUDDEN COLD SWEATS...`），年轻的 Yiffai 习惯美式英语，对此产生困惑并反问（`...DID YOU JUST CALL MY FLASHLIGHT A "TORCH"?`）。现译竟直译为古代「火把」（“火把忽明忽暗……” / “你刚把我的手电筒叫作‘火把’？”）。这不仅违背高科技科幻探险设定，且彻底摧毁了英美用词差异与长官古板用语的戏谑互动。
- **裁决方案**：波苏行改为老派规范的「手提电筒忽明忽暗……」，Yiffai 吐槽行相应调整为「……你刚才管我的手电筒叫“手提电筒”？」，与女线「照明电筒」的设定遥相呼应，修复前后逻辑与语用闭环（`P02-012`, `P02-013`）。

### 2. 核心武器与规程条例误译（A 类）
- **场景**：`SC29cb42777b41829b`（`Kobo`，男线）
- **问题**：Yiffai 在查阅规程时说道 `HMM, VEHICU...? NO, THREE-*TWO*. LIGHTTAZER CARE...?`。现译将核心近战武器设定 `lighttazer`（光能电击刃）误翻为「轻型电击枪」，且规程词首截断 `VEHICU...?` 裸留大写英文未做本地化。
- **裁决方案**：改为「嗯，载具……？不，是 3-*2*。光能电击刃保养……？」，严格纠正武器术语为「光能电击刃」，并将条例查阅自然本地化（`P02-050`）。

### 3. 操作指令同一场景内冲突（B 类）
- **场景**：`SCb09c7c6e85e32642` & `SC88ac39742501fe56`（`AreaC_map64_b`，抓钩说明）
- **问题**：前文 Yiffai 刚刚复述了按键操作 `UP+ATTACK`，Tomcat 紧接着讲操作时却被翻成了 `上+攻击`。同一场内按键命名中英文杂糅，不符合按键名称统一保留原样的规范。
- **裁决方案**：Tomcat 行统一修改为英文按键名称 `UP+ATTACK`，保持全场按键指示一致（`P02-021`, `P02-025`）。

### 4. 职衔称谓全局性漂移（B 类主体）
- **全工单排查**：在原版对话中，波苏、毛鼠、雄猫及主角均大量使用 `Agent` / `Agent Y`。在历史译本中，存在大量残留的「特工」（如“Y特工”、“外勤特工”、“说明，特工”、“特工，你不是收集者？”等共计 35+ 处）。根据全局统一规范，调查局体系职衔全篇统一定为「探员」，本批次将所有残留的「特工」全部修正为「探员」，恢复官方职衔的严肃性与一致性。

---

## 四、男女两版（datadf vs datadm）不一致清单

1. **装备名词本地化遗漏**：
   - 在 `AreaA_map42_a` 中，女线及男线毛鼠台词均已汉化为「马克 IV 宇宙靴」，而男线 Tomcat 独有台词 `CAT:Oc62eb4fc6f3b74b075bf` 却裸留了英文 `Mark IV Cosmoboots`。已在男线补齐汉化（`P02-007`）。
2. **意识投射叙述生硬度差异**：
   - 在 `AreaX_fenfen_rescued`（救出芬芬）中，男线译作「对方不知怎么把图像直接传进了我脑子里」，自然通顺；女线却被直译为「他送了……送进了我的脑子」，机翻感极强。本次对女线进行了同等质量的修润（`P02-038`, `P02-039`）。
3. **Kobo 伪装称谓分裂**：
   - 女线与男线、SFW 与 NSFW 之间分别出现了「科博德套装」、「狗头人装」、「科博德群」与「狗头人」。依据术语表，全线统一规范为「科博」与「科博套件」。
4. **武器译名漂移**：
   - 最后一击收容怪物的 `trainer tazer`，在女线 SFW 中被译为「训练电击器」，在其余场次被译为「驯兽电击枪」。男女全线统一修正为设定术语「驯兽电击刃」。

---

## 五、未覆盖项与本工单不能证明的事项

1. **无线电失真杂音的真实字形**：
   - 在 `AreaC_map56_a` 中，Tomcat 的无线电受到强烈干扰（如 `..UP... T... AKE... ...ITCH!`）。英文原意为失真断句（WAKE UP... TAKE... BITCH!），女线保留了英文字母断片，男线 NSFW 译为拟声词，男线 SFW 译为断续短语。因无法取得 FMOD 缺失的语音事实（本游戏文本即全部音频风格），本精校对这些失真断片予以保留，不主观脑补重构。
2. **文本框物理渲染边界**：
   - 本批提案的所有替换物理行均已在字数上严格控制（普遍在 15~40 字之间，最长未超过原版既有的 59 字极限），未打破行数与前缀结构；实际游戏内 240px 折行情况需在后续构建中由 `measure_width.py` 自动化检测通过。

---

## 六、交付物清单

1. `localization/editorial/r9-polish/batch-02/gemini/findings.jsonl`（63 行）
2. `localization/editorial/r9-polish/batch-02/gemini/coverage.jsonl`（56 行）
3. `localization/editorial/r9-polish/batch-02/gemini/summary.md`
