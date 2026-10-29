# batch-07-part01 精校总结报告（Gemini 路）

## 一、输入与审校概况

- **工单文件**：`localization/editorial/r9-polish/batch-07-part01/orders/batch-07-part01.reader.md`
- **读取行数**：完整读取 1535 行，按每 200 行分段读取并即时跟进，**全量读完，无截断**。
- **场景覆盖**：工单全部 11 场，涵盖 385 个 ROW 行，全部完成精校审查。
  - 女线（SFW/NSFW）：5 场（`vsn/f_EndingBad/script.vsn`、`vsn/f_EndingGood/script.vsn`、`vsn/f_GameOverArea0/script.vsn`、`vsn/f_GameOverAreaA/script.vsn`、`vsn/f_GameStart/script.vsn`）
  - 男线（SFW/NSFW）：6 场（`vsn/m_EndingBad/script.vsn`、`vsn/m_EndingGood/script.vsn`、`vsn/m_GameOverArea0/script.vsn`、`vsn/m_GameOverAreaC/script.vsn`、`vsn/m_GameOverAreaE/script.vsn`、`vsn/m_GameStart/script.vsn`）

---

## 二、发现总数与分布

共记录 **3 条** 独立发现，编号为 `P07-101` ～ `P07-103`。

### 1. 分级统计
- **A 级**（误义、漏义、逻辑或结构破坏）：0 条
- **B 级**（语境衔接、格式规范、角色术语不一致、跨版本同型台词不一致）：3 条
- **C 级**（纯文笔润色）：0 条
- **needs_evidence**：0 条

### 2. 发现分布列表

| 编号 | 场景 ID | 归属脚本 Root | 涉及 row_id | 级别 | 类别 | 简述 |
| :--- | :--- | :--- | :--- | :---: | :---: | :--- |
| **P07-101** | `SCa2d5d1f6d5944926` | `vsn/f_EndingGood/script.vsn` | `CAT:O9b102edb47da0d82ef05` | B | format | 原文为 `-Ahem...`，当前中文作 `text: -嗯哼……`，句首残留半角连字符，提案改为全角破折号 `text: ——嗯哼……`。 |
| **P07-102** | `SCc9710272ec73d1ea` | `vsn/m_EndingGood/script.vsn` | `CAT:O18305b5ce35391c77571` | B | format | 男线同型位置同样出现 `text: -嗯哼……`，与 P07-101 同型，提案改为全角破折号 `text: ——嗯哼……`。 |
| **P07-103** | `SCa2d5d1f6d5944926` | `vsn/f_EndingGood/script.vsn` | `CAT:O7d47a8f4843f68747af5` | B | continuity | 女线好结局波苏报告署名残留未译英文 `text: [PPP以拥有这两位特工为荣。]                      -SIGNED, BOSSU`；男线同型已译为 `——署名：波苏`，提案将女线对齐为 `text: [PPP以拥有这两位特工为荣。]                      ——署名：波苏`。 |

---

## 三、场次判定结果（保留场次说明）

本批 11 场中，**9 场**判定为全场保留（`retain`），**2 场**判定为发现问题（`issues_found`）：

1. **`SC05c3dd2092871dea`（女线坏结局，`f_EndingBad`）**：**retain**
   - 13 行全通顺，Traeh、图托恩（Tutone）术语规范，追逐失败自责情绪传神。
2. **`SCa2d5d1f6d5944926`（女线好结局，`f_EndingGood`）**：**issues_found**
   - 34 行。发现波苏打断清嗓的半角连字符（P07-101）及末尾波苏署名未汉化残留（P07-103），其余对白通顺、姐弟互动生动，其余行保留。
3. **`SC9ddff3d06e1707d8`（女线区域0战败演出，`f_GameOverArea0`）**：**retain**
   - 53 行。合句断点自然，色气对白语用还原度高，长合句未超折行安全阈值，全场保留。
4. **`SCa4f1ced2b88fd910`（女线区域A战败演出，`f_GameOverAreaA`）**：**retain**
   - 59 行。史莱姆战斗及剥心魔（Mind Flayer）战败报告分明，编者注客观准确，全场保留。
5. **`SC3c3f4d5a75f1ea83`（女线开场演出，`f_GameStart`）**：**retain**
   - 34 行。磁鞘进入点、波苏无线电、失真信号还原精准，Traeh 入侵与被击坠对白紧凑，全场保留。
6. **`SC5feb59441112a3a5`（男线坏结局，`m_EndingBad`）**：**retain**
   - 13 行。姐弟飞船坏结局对白简练，情绪准确，术语一致，全场保留。
7. **`SCc9710272ec73d1ea`（男线好结局，`m_EndingGood`）**：**issues_found**
   - 34 行。发现波苏打断清嗓的半角连字符（P07-102），波苏署名已正确汉化，其余台词均保留。
8. **`SC394405c5c61c5988`（男线区域0战败演出，`m_GameOverArea0`）**：**retain**
   - 46 行。伊吠以记录报告视角叙述被俘过程，口吻鲜活，合句结构严密，全场保留。
9. **`SC42b1851d50303cc3`（男线区域C战败演出，`m_GameOverAreaC`）**：**retain**
   - 60 行。哥布林村落被俘、斯凯菲亚（Sceafya）精灵与恩莉耶大人（High Lady Enelye）的设定表达准确，术语与词典一致，全场保留。
10. **`SC8fcba06da26bb88f`（男线区域E战败演出，`m_GameOverAreaE`）**：**retain**
    - 7 行。流放地（EXILE）失踪通报体裁庄重，黑暗“女王”寻觅新宿主设定明确，全场保留。
11. **`SC9dd5254e6df8337b`（男线开场演出，`m_GameStart`）**：**retain**
    - 32 行。男线开场无线电套语及遭遇战对白还原度高，伊吠初出茅庐的自信口吻跃然纸上，全场保留。

---

## 四、高风险连续段与焦点分析

1. **无线电失真与断句**：
   - 女线开场 L44 (`SFW983326629084e0dfe18a0bb0`) 与男线开场 L43 (`SFW7d58588a259dba42aff67ad1`) 原文均为 `Just make...sur...ou...on your...oes...or....`，当前译文统一作 `text: 只要确……保……你……多加……小……心……`。还原了信号受干扰的断词状态，既未过度补全也未漏失语义，保留良好。
2. **合句与跨行断点**：
   - 演出文本中存在大量合句（前一行承载合并长句，下一行 current 为空）。经逐行比对，合句均完整表达了对应英文的两行语义，合句尾行保持为空，不报漏译，不提案填补。

---

## 五、男女两版跨版本不一致清单

1. **波苏好结局终报署名（P07-103）**：
   - **英文原文**：`[AND THE PPP IS PROUD TO HAVE THEM AS AGENTS.]                      -SIGNED, BOSSU`
   - **男线**（`SCc9710272ec73d1ea`，`CAT:O014c38c7ec9610db4cad`）：`text: [PPP以拥有他们两位特工为荣。]                      ——署名：波苏`
   - **女线**（`SCa2d5d1f6d5944926`，`CAT:O7d47a8f4843f68747af5`）：`text: [PPP以拥有这两位特工为荣。]                      -SIGNED, BOSSU`
   - **判定**：女线保留了英文大写实词 `SIGNED, BOSSU` 及半角连字符，未译出指挥官“波苏”的中文名，属于明显的跨版本不一致及未译残留，已提案将女线按相同排版规范对齐为中文。

---

## 六、未覆盖项与「本工单不能证明的事」

1. **实机渲染与动态折行**：
   - 容器规格为 240px、12px 字体，安全上限约 20 全角字/行、每页最多 3 行。本报告对长句折行判定基于字符宽度估算（汉字约 12px，全角标点 12px，半角字母约 6-8px）。**未进入游戏实机加载字体排版测试，折行完全依靠估算**。
2. **演出上屏英文大写的统一策略**：
   - 结局与开场中部分全大写英文（如 `STARDATE XXXX:XXXX:XXXX.XX`、`MAGNETOSHEATH ENTRY POINT`、`[SO ENDS THE REPORT ON PLANET TUTONE.]` 等）部分进行了方括号内汉化，部分属于特定界面镜像。本报告仅纠正了角色波苏署名中的未译实词，其余演出标题镜像按规则不报。
