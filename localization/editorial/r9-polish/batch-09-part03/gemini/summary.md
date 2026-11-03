# batch-09-part03 精校总结报告（gemini 路线）

## 一、输入文件与实读统计

- **工单正文**：`localization/editorial/r9-polish/batch-09-part03/orders/batch-09-part03.reader.md`（共 1,991 行物理行）
- **结构化数据**：`localization/editorial/r9-polish/batch-09-part03/orders/batch-09-part03.json`
- **参照依据**：`localization/editorial/r9-polish/batch-09-part03/orders/reference-excerpt.md`、`ORDER.md`
- **实读场数**：229 场（SCe4a5c703d204367e ～ SC7a8997bd2b051f31，覆盖率 100%）
- **实读物理 ROW 行数**：399 行
- **读取状态**：全部 229 场均为 `read_full`，无 `partial` 或 `not_read`。

## 二、发现总数与分级分布

- **发现总数**：19 条（编号段：`P09-0301` ～ `P09-0319`）
- **等级分布**：
  - **A 级（误义/漏义/玩法误导）**：0 条
  - **B 级（语用/称呼/术语一致性）**：4 条
  - **C 级（文笔/排版格式/无源空格清除）**：15 条
  - **needs_evidence（原文存疑/需证据）**：0 条

### 按 Root 归组统计

| Root 组别 | 场景数 | 发现数 | 涉及编号与详情 |
| :--- | :--- | :--- | :--- |
| `AreaA_Cellar` | 3 | 0 | 全保留（retain） |
| `AreaA_Macsen1` | 5 | 1 | P09-0301 (C: 行尾多余空格) |
| `AreaA_Macsen2` | 7 | 2 | P09-0302, P09-0303 (C: 行尾多余空格) |
| `AreaA_Prison1` | 11 | 2 | P09-0304, P09-0305 (C: 行尾多余空格) |
| `AreaA_Prison2` | 13 | 0 | 全保留（retain） |
| `AreaA_Prison3` | 13 | 1 | P09-0306 (B: Barkers 规范为“吠犬”) |
| `AreaB_Macsen1` | 3 | 0 | 全保留（retain） |
| `AreaB_Macsen2` | 3 | 0 | 全保留（retain） |
| `AreaB_MacsenBar` | 2 | 0 | 全保留（retain） |
| `AreaB_Prison1` | 7 | 1 | P09-0307 (B: kobolds 规范为“科博德”) |
| `AreaB_Prison2` | 10 | 0 | 全保留（retain） |
| `AreaB_Slaver2` | 11 | 0 | 全保留（retain） |
| `AreaC_Macsen1` | 3 | 0 | 全保留（retain） |
| `AreaC_MacsenDark` | 4 | 1 | P09-0308 (B: hookshot 规范为“钩爪”) |
| `AreaC_Prison1` | 7 | 0 | 全保留（retain） |
| `AreaC_Prison2` | 15 | 1 | P09-0309 (C: 行尾多余空格) |
| `AreaC_Prison3` | 7 | 1 | P09-0310 (C: 行尾多余空格) |
| `AreaC_Slaver1` | 11 | 1 | P09-0311 (C: 行尾多余空格) |
| `AreaE_Macsen1` | 6 | 3 | P09-0312, P09-0313, P09-0314 (C: 行尾多余空格) |
| `AreaH_Cellar` | 7 | 3 | P09-0315 (B: agent 规范为“特工”); P09-0316, P09-0317 (C: 行尾空格) |
| `AreaH_MacsenBar` | 4 | 0 | 全保留（retain） |
| `AreaH_MacsenBreeding` | 3 | 0 | 全保留（retain） |
| `AreaH_MacsenMechanic` | 1 | 0 | 全保留（retain） |
| `AreaX_Upgrade` | 10 | 2 | P09-0318, P09-0319 (C: 行尾多余空格) |
| `Fenfen_Shared` | 1 | 0 | 全保留（retain） |
| `Gitgud` | 2 | 0 | 全保留（retain） |
| `Hacker_Shared` | 8 | 0 | 全保留（retain） |
| `Macsen_Shared` | 6 | 0 | 全保留（retain） |
| `Prison_Shared` | 1 | 0 | 全保留（retain） |
| `Proto_*` (Fenfen/Key/Tazer) | 19 | 0 | 全保留（retain） |
| `Test_*` (Hacker/Prison/Slaver) | 26 | 0 | 全保留（retain） |
| **合计** | **229** | **19** | **B级 4 条，C级 15 条** |

---

## 三、4 项 B 级术语修正提案详情

1. **`P09-0306` (AreaA_Prison3.GoodbyeDog / SCac5b9f5097efca6e / CAT:O865697caa77a7b551eed)**
   - 英文原文：`Seeya girl! Watch out for the Barkers!`
   - 当前中文：`  * 回见啦，姑娘！小心那些吠叫者！`
   - 提案修改：`  * 回见啦，姑娘！小心那些吠犬！`
   - 依据出处：`reference-excerpt.md` 第三节术语表明文规定 `BARKER -> 吠犬`。同项目已落地台账 `editorial-r9-batch-08-part01-repairs.jsonl` 第 10 行（`那些吠犬老冲我尾巴来`）及 `editorial-r9-batch-07-part02-repairs.jsonl` 第 22 行（`一只橙毛吠犬`）均已统一落地为“吠犬”。
2. **`P09-0307` (AreaB_Prison1.TalkBeforeRescue.bopped / SC86572c4386d4b135 / SFWa831055d27dc24243cba3eb1)**
   - 英文原文：`Some big kobolds locked me up in here.`
   - 当前中文：`  * 几个大块头狗头人把我关在这里了。`
   - 提案修改：`  * 几个大块头科博德把我关在这里了。`
   - 依据出处：`reference-excerpt.md` 第三节术语表及第五节已落地裁决（`Kobo＝科博德`）。前期台账 `editorial-r9-batch-02-repairs.jsonl`（L3/4/10/11）及 `editorial-r9-batch-06-part01-repairs.jsonl`（L1/4）均已系统性纠正旧译“狗头人”为“科博德”。
3. **`P09-0308` (AreaC_MacsenDark.Talk.dark / SC1d9a1c61cec5875e / SFW267f2fc596449b95d0209b5e)**
   - 英文原文：`First somewan stole my hookshot so I have to walk around on these tiny legs...`
   - 当前中文：`    * 先是有人偷了我的钩索，害我只能靠这两条小短腿走路……`
   - 提案修改：`    * 先是有人偷了我的钩爪，害我只能靠这两条小短腿走路……`
   - 依据出处：`reference-excerpt.md` 第三节术语表明文规定 `HOOKSHOT -> 钩爪`。同 batch 前序台账 `editorial-r9-batch-09-part01-repairs.jsonl` 第 16 行（SC0bffef4b72d95f38）与 `editorial-r9-batch-09-part02-repairs.jsonl` 第 5 行（SC534b27bb191911f5）均已将同句“钩索”统一纠正为“钩爪”。
4. **`P09-0315` (AreaH_Cellar.Talk.food / SCf3cb45071658dd85 / CAT:Oa77aae8b9823089a86a1)**
   - 英文原文：`It's been so long since I saw another one of you agent sorts here that I haven't even kept the stocks up!`
   - 当前中文：`    * 我好久没在这儿见到你们这种探员了，连存货都没顾上补！`
   - 提案修改：`    * 我好久没在这儿见到你们这种特工了，连存货都没顾上补！`
   - 依据出处：R2 核心裁决与 `reference-excerpt.md` 第三节及第五节明文规定 `agent＝特工`，不得使用旧译“探员”。同场女线 SFW 版本（SC57698af9183051b1 / SFWf36a73288b6064869cf953a0）已正确使用“特工”，此处统一纠偏。

---

## 四、高风险连续段（问答错位、合句断点、无线电套语）

本批包含多处跨行物理换行的既有合句（尾行 `current` 为空字符串）。逐一审校确认：
1. **`AreaB_MacsenBar.Talk.main` (SC17cc2156161f94a5)**：
   L867 承载前半句与后半句合并（`之前还来过一个跟你一样的太空伙计，嘴里嘀咕着说把武器落在这儿正北边了！ `），L868 为空。英文原文行尾有空格，中文行尾空格为合法镜像，按规范不报。接续 L869 的 R8 谜题提示措辞准确，保留原样。
2. **`AreaC_MacsenDark.DarkNoPurchase` (SCfd4ab3dc2ab0c65b)**：
   L1202 承接合句（“……但我每次一动，好像都会踩到什——嗷呜！”），L1203 为空，标点与语气拟声词衔接自然。
3. **`AreaC_MacsenDark.Talk.dress` (SCe338b7546a4c96ff)**：
   L1230 承接“听说它们靠某种纳米机器，能防止脚下的方块崩塌……”，L1231 为空，接下行魔法感叹，逻辑紧凑。
4. **`AreaE_Macsen1.SpecialGeiger` (SCa77905dd8a62d2c1 / SC457bf0e86885490a)**：
   L1492 承接雷达探测与导航地图标记功能，L1493 为空，合句通顺。
5. **`AreaH_Cellar.Talk.food` (SCf3cb45071658dd85 / SC57698af9183051b1)**：
   L1583/L1586 合并多行从句，语义完整，无主谓残缺。
6. **`AreaH_MacsenBar` 连续段 (SCad64b28a0cedd27b, SC8cf80b11c314c9d0, SCcc40787614a1caeb)**：
   超能力水晶、特工拯救回扣、Zener 卡牌三角/十字力量设定的合句均完整承接，无破损。
7. **`AreaX_Upgrade` (SC0ad0638f9309545b, SC591eb00fae1bff09, SC5a6089db81efd081)**：
   黑入现实模拟、收集芯片、电网重启的合句均通顺准确。
8. **`Gitgud.Tip4` / `Tip5` (SCf84d3bb202657af6, SCafde0627f237c71b)**：
   提示框火把敲碎掉零钱、电击枪硬直躲避技巧，均保持 R8 裁决措辞。

---

## 五、男女两版不一致清单（跨版本对照）

本批涉及多处女线（`datadf`，Yiffany）与男线（`datadm`，Yiffai）的同型台词比对：
1. **`AreaB_Slaver2.Talk.kobo`**：
   - 女线 (`SC60b2521ed8918dd3` / CAT:O74e8ea2524757a3baa1b / L1062)：`    * 你这科博德，闻起来倒挺讨人喜欢，嘿嘿。你跟哪支船队来的？`
   - 男线 (`SCfd3a35d14d8646de` / CAT:O4c25f65c290e84e68628 / L1067)：`    * 作为科博德，你闻着还挺可爱的，嘿嘿。你跟哪伙船员来的？`
   - **分析**：英文同为 `You smell pretty cute for a kobold, heh-heh. What crew you fly in with?`。两版措辞略有不同（“船队” vs “船员”，“讨人喜欢” vs “可爱”），但均符合各自历史语境且自然通顺，按规范分别保留各自独立版本，不强行抹平。
2. **`AreaH_Cellar.Talk.food`**：
   - 男线 (`SCf3cb45071658dd85` / CAT:Oa77aae8b9823089a86a1 / L1586)：`    * 我好久没在这儿见到你们这种探员了，连存货都没顾上补！`（已提案将“探员”纠正为“特工”）
   - 女线 SFW (`SC57698af9183051b1` / SFWf36a73288b6064869cf953a0 / L1578)：`    * 我已经很久没在这儿见到你们这种特工了，连存货都没顾上补！`
   - **分析**：词义与结构一致，男线修正术语后与女线完全对齐。
3. **`Test_Prison1` 与 `Test_Slaver1` 系列测试场景**：
   - 男女主角在测试监狱场景台词完全镜像对齐（如 `  * [谢谢你，伊吠！]` vs `  * [谢谢你，伊吠妮！]`，`  * [我自由了！]`，`  * 你好！想买点什么？` 等），代词与名字替换准确无误。

---

## 六、未覆盖项与本工单不能证明的事项

1. **按键名手柄映射**：
   `UP+ATTACK`、`DOWN+JUMP` 等按键组合在文本中直接以英文大写呈现，属于程序底层按键定义，未连接手柄进行实机按键映射提示测试。
2. **LIGHTTAZER 最终中文定名**：
   本批文本中出现的“电击枪”、“光电击枪”属于全局未终裁术语。依照 `ORDER.md` 与 `reference-excerpt.md` 第六节硬约束，本路线严守口径，不主动发起提案修改。
3. **引号与空格体例**：
   全角引号（`“”`）与直角引号（`「」`）、拉丁字母与汉字之间的半角空格体例在全项目中处于全局待裁状态，本批不作局部统一。
4. **游戏内剧情框像素级折行表现**：
   本路线严格保障了文本行长度不超标，并在所有提案中完整保留原行首前缀与缩进；但未启动游戏本体进行动态字宽排版渲染实测。
