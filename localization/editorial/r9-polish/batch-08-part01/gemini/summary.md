# batch-08-part01 精校总结报告（Gemini 路）

## 一、输入与审校概况

- **工单文件**：`localization/editorial/r9-polish/batch-08-part01/orders/batch-08-part01.reader.md`
- **读取行数**：完整读取 1892 行，严格按每 200 行分段读取并即时增量审校，**全量读完，无截断**。
- **场景覆盖**：工单全部 15 场，涵盖 452 个 ROW 行，全部完成精校审查。
  - **女线**（7 场）：
    1. `SCb0c2a122f1065c8d`（`vsn/f_AgentF07/script.vsn`，44 rows）
    2. `SC8c2a5c414a297776`（`vsn/f_AgentFZ2/script.vsn`，22 rows）
    3. `SCa2fb98b0f0ceefb5`（`vsn/f_AgentFZ6/script.vsn`，22 rows）
    4. `SC952e581f7322b50b`（`vsn/f_ClassicBigbold/script.vsn`，65 rows）
    5. `SC7f00fdd5a5b7a70e`（`vsn/f_ClassicBigboldV2/script.vsn`，29 rows）
    6. `SC282bb2757cee4a43`（`vsn/f_ClassicBossRedbull/script.vsn`，20 rows）
    7. `SC95b360ac069218fb`（`vsn/f_ClassicPigobinV3/script.vsn`，16 rows）
  - **男线**（8 场）：
    8. `SC8c5795a6717ff892`（`vsn/m_AgentM01/script.vsn`，36 rows）
    9. `SCfabc28c6d25f68c7`（`vsn/m_AgentM0B/script.vsn`，26 rows）
    10. `SC4ae7f053796af024`（`vsn/m_AgentMZ1/script.vsn`，27 rows）
    11. `SC3ce221bd4584b3f6`（`vsn/m_AgentMZ3/script.vsn`，19 rows）
    12. `SC78be6b2b2431f3c9`（`vsn/m_AgentMZ5/script.vsn`，19 rows）
    13. `SC247abe9c6c0216e1`（`vsn/m_ClassicEnelye/script.vsn`，14 rows）
    14. `SC2cc5a8a8d22d1336`（`vsn/m_ClassicStarkillV3/script.vsn`，17 rows）
    15. `SC7c9d71ffa59dae21`（`vsn/m_ClassicWerepup/script.vsn`，76 rows）

---

## 二、发现总数与分布

共记录 **21 条** 独立发现，编号为 `P08-0101` ～ `P08-0121`。

### 1. 分级统计
- **A 级**（误义、漏义、逻辑或结构破坏）：0 条
- **B 级**（半角连字符代替破折号等结构缺陷）：1 条（`P08-0107`）
- **C 级**（行尾多余半角空格）：20 条（`P08-0101`～`P08-0106`、`P08-0108`～`P08-0121`）
- **needs_evidence**：0 条

### 2. 发现分布列表

| 编号 | 场景 ID | 归属脚本 Root | 涉及 row_id | 级别 | 类别 | 简述 |
| :--- | :--- | :--- | :--- | :---: | :---: | :--- |
| **P08-0101** | `SC8c2a5c414a297776` | `vsn/f_AgentFZ2/script.vsn` | `CAT:O64c282165c424cfd7ad6` | C | format | 英文原行行尾无空格，中文行尾有多余半角空格，去除尾部空格。 |
| **P08-0102** | `SC8c2a5c414a297776` | `vsn/f_AgentFZ2/script.vsn` | `CAT:O6f28a94c58171b7bfbb9` | C | format | 英文原行行尾无空格，中文行尾有多余半角空格，去除尾部空格。 |
| **P08-0103** | `SC8c2a5c414a297776` | `vsn/f_AgentFZ2/script.vsn` | `CAT:O80cd7e8b0c722b0f54f5` | C | format | 英文原行行尾无空格，中文行尾有多余半角空格，去除尾部空格。 |
| **P08-0104** | `SCa2fb98b0f0ceefb5` | `vsn/f_AgentFZ6/script.vsn` | `CAT:O9e90b42855f36967e9cc` | C | format | 英文原行行尾无空格，中文行尾有多余半角空格，去除尾部空格。 |
| **P08-0105** | `SC952e581f7322b50b` | `vsn/f_ClassicBigbold/script.vsn` | `CAT:O8b06b381dcca78bdcf6b` | C | format | 英文原行行尾无空格，中文行尾有多余半角空格，去除尾部空格。 |
| **P08-0106** | `SC952e581f7322b50b` | `vsn/f_ClassicBigbold/script.vsn` | `CAT:Oa45c6925ff1a0001d990` | C | format | 英文原行行尾无空格，中文行尾有多余半角空格，去除尾部空格。 |
| **P08-0107** | `SC952e581f7322b50b` | `vsn/f_ClassicBigbold/script.vsn` | `CAT:O742b26cc4aac1a43957b` | B | format | 句首使用半角连字符`-`代替破折号`——`（`text: -嘿……`），承接上一行被打断的破折号`一颠一颠——`，提案替换为`text: ——嘿……`。 |
| **P08-0108** | `SC952e581f7322b50b` | `vsn/f_ClassicBigbold/script.vsn` | `CAT:O514067886c6e23c449ee` | C | format | 英文原行行尾无空格，中文行尾有多余半角空格，去除尾部空格。 |
| **P08-0109** | `SC952e581f7322b50b` | `vsn/f_ClassicBigbold/script.vsn` | `CAT:O5c57d92ae486389c8276` | C | format | 英文原行行尾无空格，中文行尾有多余半角空格，去除尾部空格。 |
| **P08-0110** | `SC282bb2757cee4a43` | `vsn/f_ClassicBossRedbull/script.vsn` | `CAT:O58ea8fab5d27028c6ea1` | C | format | 英文原行行尾无空格，中文行尾有多余半角空格，去除尾部空格。 |
| **P08-0111** | `SC282bb2757cee4a43` | `vsn/f_ClassicBossRedbull/script.vsn` | `CAT:Od7d0f60b2e5c70c50ab9` | C | format | 英文原行行尾无空格，中文行尾有多余半角空格，去除尾部空格。 |
| **P08-0112** | `SCfabc28c6d25f68c7` | `vsn/m_AgentM0B/script.vsn` | `CAT:O435d2cb71b9696ba050f` | C | format | 英文原行行尾无空格，中文行尾有多余半角空格，去除尾部空格。 |
| **P08-0113** | `SCfabc28c6d25f68c7` | `vsn/m_AgentM0B/script.vsn` | `CAT:Oec35cbbfb6a6c3d697e7` | C | format | 英文原行行尾无空格，中文行尾有多余半角空格，去除尾部空格。 |
| **P08-0114** | `SC4ae7f053796af024` | `vsn/m_AgentMZ1/script.vsn` | `CAT:Oadd5dcb043a4d98e0531` | C | format | 英文原行行尾无空格，中文行尾有多余半角空格，去除尾部空格。 |
| **P08-0115** | `SC2cc5a8a8d22d1336` | `vsn/m_ClassicStarkillV3/script.vsn` | `CAT:O8412a0ae707b31ef48f2` | C | format | 英文原行行尾无空格，中文行尾有多余半角空格，去除尾部空格。 |
| **P08-0116** | `SC2cc5a8a8d22d1336` | `vsn/m_ClassicStarkillV3/script.vsn` | `CAT:O04703be7e3b9c5d54f0d` | C | format | 英文原行行尾无空格，中文行尾有多余半角空格，去除尾部空格。 |
| **P08-0117** | `SC7c9d71ffa59dae21` | `vsn/m_ClassicWerepup/script.vsn` | `CAT:O90dfd048506baae0450b` | C | format | 英文原行行尾无空格，中文行尾有多余半角空格，去除尾部空格。 |
| **P08-0118** | `SC7c9d71ffa59dae21` | `vsn/m_ClassicWerepup/script.vsn` | `CAT:O177e051e89610b838894` | C | format | 英文原行行尾无空格，中文行尾有多余两个半角空格，去除尾部空格。 |
| **P08-0119** | `SC7c9d71ffa59dae21` | `vsn/m_ClassicWerepup/script.vsn` | `CAT:O10aaf3d11e2bff3fc672` | C | format | 英文原行行尾无空格，中文行尾有多余半角空格，去除尾部空格。 |
| **P08-0120** | `SC7c9d71ffa59dae21` | `vsn/m_ClassicWerepup/script.vsn` | `CAT:O50a025787aae226b4044` | C | format | 英文原行行尾无空格，中文行尾有多余半角空格，去除尾部空格。 |
| **P08-0121** | `SC7c9d71ffa59dae21` | `vsn/m_ClassicWerepup/script.vsn` | `CAT:O587351ffd85884b92f1c` | C | format | 英文原行行尾无空格，中文行尾有多余半角空格，去除尾部空格。 |

---

## 三、场次判定结果（保留场次说明）

本批 15 场中，**7 场**判定为全场保留（`retain`），**8 场**判定为发现结构缺陷（`issues_found`）：

1. **`SCb0c2a122f1065c8d`（女线特工自述，`f_AgentF07`，44 行）**：**retain**
   - 特工自述口吻活泼俏皮，合句自然，无残留英文、行尾空格或术语问题。全场保留。
2. **`SC8c2a5c414a297776`（女线Fenfen支线，`f_AgentFZ2`，22 行）**：**issues_found**
   - 发现 3 处行尾多余半角空格（P08-0101～0103）；其余对白古风端庄、Traeh与图托恩术语准确，其余行保留。
3. **`SCa2fb98b0f0ceefb5`（女线Fenfen支线，`f_AgentFZ6`，22 行）**：**issues_found**
   - 发现 1 处行尾多余半角空格（P08-0104）；心理与灵能设定翻译精确，其余行保留。
4. **`SC952e581f7322b50b`（女线经典大壮兽首领演出，`f_ClassicBigbold`，65 行）**：**issues_found**
   - 发现 1 处半角连字符打断缺陷（P08-0107，`-嘿……` 改为 `——嘿……`）及 4 处行尾多余半角空格（P08-0105、0106、0108、0109）。口含时的口齿不清与色气互动极为地道传神，科博德术语正确，其余行保留。
5. **`SC7f00fdd5a5b7a70e`（女线经典大壮兽SFW演出，`f_ClassicBigboldV2`，29 行）**：**retain**
   - SFW版对白利落风趣，“超能护腕”（hyper bracer）术语与词典完全一致，全场保留。
6. **`SC282bb2757cee4a43`（女线经典红牛首领演出，`f_ClassicBossRedbull`，20 行）**：**issues_found**
   - 发现 2 处行尾多余半角空格（P08-0110～0111）；伊吠妮自报名号与红牛压迫感表现优秀，其余行保留。
7. **`SC95b360ac069218fb`（女线经典Pigobin首领演出，`f_ClassicPigobinV3`，16 行）**：**retain**
   - 英文原文行尾空格被中文镜像保留，不报；古典英文“thou/thee/mine”以“汝/吾/罢”传神对译，全场保留。
8. **`SC8c5795a6717ff892`（男线特工自述，`m_AgentM01`，36 行）**：**retain**
   - 男线特工第一人称抱怨与傲娇情绪丰满，“强奸兰博”（rapebo）、“吠犬”（barkers）、“科博德”（kobolds）、“锁结”（tie）术语与黑话全部地道准确，全场保留。
9. **`SCfabc28c6d25f68c7`（男线特工自述，`m_AgentM0B`，26 行）**：**issues_found**
   - 发现 2 处行尾多余半角空格（P08-0112～0113）；兔特工对白生动，“挥爪”（Swipers）术语准确，男主角伊吠称呼准确，其余行保留。
10. **`SC4ae7f053796af024`（男线Fenfen支线，`m_AgentMZ1`，27 行）**：**issues_found**
    - 发现 1 处行尾多余半角空格（P08-0114）；叙事沉稳宏大，其余行保留。
11. **`SC3ce221bd4584b3f6`（男线Fenfen支线，`m_AgentMZ3`，19 行）**：**retain**
    - 英文原行行尾空格为原版排版镜像，不报；超能力反击战与精灵兵器剧情通畅，全场保留。
12. **`SC78be6b2b2431f3c9`（男线Fenfen支线，`m_AgentMZ5`，19 行）**：**retain**
    - 英文原行行尾多处带空格，中文行尾空格为排版镜像，不报；流星坠落与Traeh水晶监牢剧情通畅，全场保留。
13. **`SC247abe9c6c0216e1`（男线经典恩莉耶演出，`m_ClassicEnelye`，14 行）**：**retain**
    - “恩莉耶”（Enelye）术语与词典完全一致，男特工被强制穿女装的尴尬与抗议口吻精准，全场保留。
14. **`SC2cc5a8a8d22d1336`（男线经典星杀演出，`m_ClassicStarkillV3`，17 行）**：**issues_found**
    - 发现 2 处行尾多余半角空格（P08-0115～0116）；弟弟（伊吠）打醒被心控姐姐（伊吠妮）的姐弟互动极佳，人名规范，其余行保留。
15. **`SC7c9d71ffa59dae21`（男线经典幼犬演出，`m_ClassicWerepup`，76 行）**：**issues_found**
    - 发现 5 处行尾多余半角空格（P08-0117～0121）；男主角自夸21岁成熟特工却陷入VR回忆的傲娇表现十分传神，性喜剧双关“迷了心窍”（dickstracted）本土化优秀，科博德术语一致，其余行保留。

---

## 四、高风险连续段分析

1. **大量合句与空行结构**：
   本批剧情脚本中存在大量“英文两行或三行、合并为单行中文显示”的合句形式（例如 `SCb0c2a122f1065c8d`、`SC952e581f7322b50b`、`SC8c5795a6717ff892`、`SC7c9d71ffa59dae21` 等）。合句尾行在工单中 `ZH:` 均为空行。经逐句核查：
   - 每一个合句的中文均包含了前后多行英文的完整意义，没有发生信息截断或逻辑缺失；
   - 合句的语序完全自然，没有生硬拼接两个半句导致的病句；
   - 所有合句尾行均严格遵守硬约束，不报漏译、不提案填充。

2. **打断破折号衔接**：
   在 `SC952e581f7322b50b` L84-L85 中，上一行是说话中途被打断（`一颠一颠——`），下一行承接打断清嗓，英文为 `-hey...`。中文当前行误用了半角连字符 `text: -嘿……`，破坏了中文版统一的双破折号打断体例。提案已修复为 `text: ——嘿……`。

3. **专有名词与术语一致性**：
   - 怪物与物种术语：刺虫、钻探者、阻挡者、跳跃者、喷火者、吱吱怪、挥爪（Swiper）、吠犬（Barker）、弹跳机、科博德（Kobold/Kobo）全库统一，未见“狗头人”残留；
   - 装备与货币：光电击枪（Lighttazer）、超能护腕（Hyper Bracer）、门卡（Keycard）、LECT、信用点均准确无误；
   - 角色人名：男线伊吠（Yiffai）、女线伊吠妮（Yiffany）、星杀（Starkill）、恩莉耶（Enelye）、Traeh 全部符合 R3 裁决。

---

## 五、男女两版的不一致清单

本批中包含数场男女两线的同型平行场景（Fenfen 支线狐狸的开场叙事），英文原文完全一致，两版中文在保持内部统一的前提下存在风格微调：

| 英文原文 | 女线中文（`f_AgentFZ2`、`f_AgentFZ6`） | 男线中文（`m_AgentMZ1`、`m_AgentMZ3`、`m_AgentMZ5`） | 涉及 row_id |
| :--- | :--- | :--- | :--- |
| `Oh brave hero, thank you for rescuing me and proving your courage.` | `lang(Fox): 噢，勇敢的英雄，谢谢你救了我，证明了你的勇气。` | `lang(Fox): 勇敢的英雄啊，感谢你救出我，证明了你的勇气。` | 女线：`CAT:Obdf83e8a6bf73e5fd9bd`、`CAT:O10c6eb7d4d59fe0466f3`<br>男线：`CAT:Ob3561ecd5daca9db50ca`、`SFW8c0ad60687c3325bca35a629`、`SFWb9aaed094bfffb76806dfaf9` |
| `Now, place your hands upon mine.` | `lang(Fox): 现在，把你的双手放到我的手上。` | `lang(Fox): 现在，把你的双手放在我的手上。` | 女线：`CAT:O25fe2ab809467a265940`、`CAT:Oeca821a1f1c85d82b828`<br>男线：`CAT:O0472e1e7889a2e6fead6`、`SFW1be59e3b68c4381aa8e2bee2`、`SFWe76240135ab956a2e6bef851` |
| `Turn your mind inward and witness the events that have shaped these lands...` | `lang(Fox): 让心神向内，去见证塑造这片土地的那些往事……` | `lang(Fox): 将心神转向内在，见证塑造这片土地的往事……` | 女线：`CAT:O1a2096ad65aae5100c13`、`CAT:O8f488f5e83b8cba74c3d`<br>男线：`CAT:Odf81a6c9c82a44fc665a`、`SFW6e83853540b4f8f1803b1f01`、`SFW47827c3457a5da4f2778424f` |

**裁决建议**：
两版翻译均准确忠实，且女线内部 2 场完全一致、男线内部 3 场完全一致。这种细微的措辞差异体现了男女线独立的语感流动，符合硬约束第 10 条“女线与男线分别处理，不把一版措辞机械复制到另一版”的原则，**建议维持两版各自现状，不作强制机械拉平**。

---

## 六、未覆盖项与本工单不能证明的事

1. **容器实机折行与渲染宽度**：
   剧情框容器标准为 240px、12px 字体、每页最多 3 行，单行约 20 个全角汉字、整页约 30 全角字为安全阈值。本审校基于静态文本长度与视觉估算判定未超界，但实际字形渲染、字距及动态换行以实机运行为准。
2. **CONTROL 脚本指令**：
   本批次包含的大量 `music:`、`snap:`、`fade:`、`cut:`、`queue:`、`sfxcue:`、`rewind!` 等演出脚本控制行均属于底层演出逻辑，审校过程中未作任何修改或破坏。
3. **未引申外推事项**：
   各特工自述的独特口癖（如大舌头语气词、兔特工语气、幼犬傲娇口吻）均保持各场独立语域，未向其他场次机械外推。
