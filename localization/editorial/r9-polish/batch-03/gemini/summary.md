# batch-03（波苏指挥线）精校总结报告（Gemini 路）

## 一、工单概况与读取覆盖
- **输入工单**：`localization/editorial/r9-polish/batch-03/orders/batch-03.reader.md`（共 1478 行，53 场，437 行物理对白）。
- **结构化参照**：`localization/editorial/r9-polish/batch-03/orders/batch-03.json`。
- **实际读取**：全部 53 场完整逐场通读（`read_full` 53 场，无截断、无抽样）。
- **输出文件**：
  - `localization/editorial/r9-polish/batch-03/gemini/findings.jsonl`（44 条发现）
  - `localization/editorial/r9-polish/batch-03/gemini/coverage.jsonl`（53 场覆盖）
  - `localization/editorial/r9-polish/batch-03/gemini/summary.md`

## 二、发现总数与分级分布
- **发现总数**：44 条
  - **A 类（严重/误义）**：1 条（占 2.3%）
    - `P03-001`：史莱姆状态拟声词 `GOOP` 误意译为形容词/名词「黏糊」，破坏变形拟声语境。
  - **B 类（主体/口吻/术语/跨版本衔接）**：29 条（占 65.9%）
    - 包括：同场无线电/通讯器漂移、特工/干员漂移、规章空格异常、断句截断错位、代词单复数误判（「你们」改「你」）、亲属称谓具体化（男线「你的手足」改「你姐姐」）、无线电结束语误译（「先走了」改「挂了」）等。
  - **C 类（文笔打磨与标点完整性）**：14 条（占 31.8%）
    - 包括：陈述句句末补齐句号、连读分句补齐逗号、同版本口吻统一（根据/依照）。
  - **needs_evidence**：0 条。

### 场景结果分布
- **发现问题场景（issues_found）**：32 场
- **完全保留场景（retain）**：21 场
- **覆盖总场数**：53 场（100% 覆盖）

### 按 Root 归组统计
| Root | 场数 | 发现数 | 主要问题概述 |
| --- | --- | --- | --- |
| `Bossu.Area0_StarkillHint noselect` | 3 | 3 | 句末标点补齐（泽罗尼亚后漏句号） |
| `Bossu.Area0_map10_a noselect noamendfreq` | 4 | 2 | 女线「好女孩」机翻腔优化为「好姑娘」；男线 SFW「乖」过度幼化优化为「好小子」 |
| `Bossu.Area0_map18_a noselect` | 4 | 3 | 男线句末标点遗漏补齐（生物数据、装备后漏句号） |
| `Bossu.Area0_map26_a noselect` | 4 | 7 | 「干员」漂移回「特工」；人名（潘科、塞塔特尼）夹带多余空格；SFW 连续句断句生硬截断修复 |
| `Bossu.Area0_map68_b noselect` | 2 | 2 | 句末标点遗漏补齐（为自己骄傲后漏句号） |
| `Bossu.AreaBTransportal2_a noselect` | 3 | 4 | 行尾残留半角空格；男线「传送到实心地表里」修正为「传进实体里」（对齐女线风险规程） |
| `Bossu.AreaE_map26 noselect` | 2 | 2 | 女线定语歧义重构（弟弟被黑暗能量侵蚀）；男线抽象书面词「你的手足」对齐亲属关系为「你姐姐」 |
| `Bossu.AreaH_map01_a noselect` | 2 | 3 | 货币 `LECT` 按规范修正为 `Lect`；「一个犬科，它」优化为「一名犬科，他」；男线结束语统一为「结束通话」 |
| `Bossu.CapturedPet` | 4 | 1 | 男线 SFW 分句行末遗漏逗号补齐 |
| `Bossu.Feral noselect noamendfreq` | 2 | 1 | PPP 两侧多余半角空格清除 |
| `Bossu.FeralPickup noselect noamendfreq` | 2 | 2 | 女线同场「通讯器」与「无线电」前后漂移统一；句末漏句号补齐 |
| `Bossu.GenderSwapped noselect noamendfreq` | 2 | 1 | 男线无线电下线语「先走了」修正为「挂了」 |
| `Bossu.GenderSwappedPickup noselect noamendfreq` | 2 | 1 | 男线无线电下线语「先走了」修正为「挂了」 |
| `Bossu.Kobo noselect noamendfreq` | 2 | 0 | 2场均完整表达Bossu护短与大笑，折行实测合格，全保留（retain） |
| `Bossu.KoboPickup noselect noamendfreq` | 4 | 4 | 对单人无线电通话误用复数「你们」修正为单数「你」/「打过来」 |
| `Bossu.NoteFrequency noselect` | 2 | 0 | 2场频率原样保留，自然流畅，全保留（retain） |
| `Bossu.Slime noselect noamendfreq` | 2 | 3 | A类 GOOP 误译「黏糊」修正为拟声「咕叽……？」；PPP空格规范；条例引用统一「根据」 |
| `Bossu.SlimePickup noselect noamendfreq` | 2 | 2 | 女线同场「通讯器」与「无线电」前后漂移统一；句末漏句号补齐 |
| `Bossu.TestA` | 2 | 0 | 2场测试通讯准确清晰，全保留（retain） |
| `Bossu.TransitionAreaEAirlock1 noselect` | 3 | 1 | 女线 NSFW「偷偷穿走」对齐男线与 SFW 版「偷偷拿走」并补逗号 |
| **合计** | **53** | **44** | |

## 三、高风险连续段审查
1. **救援特工数据联动段（`Bossu.Area0_map26_a`）**：
   - 现行译文中在男线 NSFW（SCa9fb8a0543b4e2eb）中连续将 AGENT / AGENT DATA 译作「干员 / 干员数据」，而在 SFW 版中同一说话人 Bossu 第一句称「顶尖干员」，下一句即变为「其他特工来说也是个好兆头」，同场术语严重割裂。精校统一回「特工」，维护了全局基线术语一致。
   - SFW 男线（SC5d1f63ab15b52fb9）中，L2032 与 L2033 原文跨行将「ALWAYS GLAD TO SEE AN AGENT SAFE AND SOUND, THAT BODES / WELL FOR THE OTHER AGENTS」生硬切断为「……总让人欣慰，这对 / 其他特工来说也是个好兆头。」精校将「这对」归入第二行句首，消除断头残句。
2. **传送门风险规程段（`Bossu.AreaBTransportal2_a`）**：
   - 男线将「porting into a solid surface」译作「传送到实心地表里」，忽略了地表为外部表面的物理常识与传进岩石/实体内部的致死风险；女线已译为「传进实体里」。精校将男线对齐为「传进实体里」，准确传达地形移位与实体嵌合的致命风险规程。
3. **黑暗能量侵蚀房间揭示段（`Bossu.AreaE_map26`）**：
   - 原文为「WHERE YOUR SIBLING WAS OVERTAKEN BY DARK ENERGY」，女线现行语序「你快到你弟弟被黑暗能量控制的那间房间了」造成定语修饰歧义，易误解为黑暗能量控制了房间；男线现行「你的手足」过于文绉绉。精校均做分句重构，女线为「你快接近那间房间了，你弟弟就是在那儿被黑暗能量侵蚀的」，男线为「你快接近那间房间了，你姐姐就是在那儿被黑暗能量吞噬的」，双线亲属关系清晰对称。

## 四、男女双版不一致清单与裁决建议
| 场景类型 | 女线 (datadf) 现状 | 男线 (datadm) 现状 | 精校裁决方案 |
| --- | --- | --- | --- |
| `CapturedPet` (SFW) | Mauser:「是啊，你跟这些当地生物越亲近，」（带逗号） | Mauser:「是啊，你越跟本地动物亲近」（漏逗号） | 男线补齐分句逗号 `P03-044` |
| `Area0_map10_a` | Bossu 对女线称「好女孩」（直译腔） | Bossu 对男线称「好小子」（NSFW）/「乖」（SFW） | 女线改为自然长辈表扬「好姑娘」`P03-023`；男线 SFW 改为「好小子」`P03-024`，去除过度幼化 |
| `AreaBTransportal2_a` | Bossu:「不能冒险让你传进实体里」 | Bossu:「不能冒险让你传送到实心地表里」 | 男线对齐女线规范改「传进实体里」`P03-017`/`P03-019` |
| `AreaE_map26` | Bossu 称「你弟弟」（具体准确） | Bossu 称「你的手足」（书面生硬） | 男线改口语自然的「你姐姐」`P03-031`，双线对称 |
| `GenderSwapped` | Yiffany:「我……我稍后再打给你！」 | Yiffai:「伊、伊吠，先走了！」 | 男线「先走了」误当面对话，改为慌乱挂机「伊、伊吠挂了！」`P03-041`/`P03-042` |
| `Slime` | Yiffany 发声「黏糊……？」 | Yiffai 发声「咕叽……？」 | 女线拟声词误意译为名词，纠正为「咕叽……？」`P03-001` |
| `Feral/SlimePickup` | Bossu 同场前称「通讯器」后称「无线电」 | Bossu 统一称「无线电」 | 女线统一为「无线电」`P03-003`/`P03-005`，消除漂移 |
| `Airlock` | 女线 NSFW:「没人偷偷把它穿走」 | 男线及 SFW:「没人偷偷把它拿走」 | 女线 NSFW 对齐为「没人偷偷把它拿走」`P03-043` |

## 五、排版宽度测量与容器合规
- 本批 44 条提案均使用 12px 字体位图度量工具进行了实测模拟。
- 全部提案折行数均控制在 1～3 行内（最大不超过 3 行），无任何单行超限导致页面溢出。
- 所有前缀（如 `  Bossu: `、`  Mauser: `、`  Yiffai: `、`  Yiffany: `、`  Tomcat: `）及方括号严格保留原样。

## 六、未覆盖项与本工单边界
- 本工单仅对 batch-03 涉及的 53 场（Bossu 及同场无线电往来）进行精校。
- 不修改游戏代码控制逻辑、不改动归档 SHA、不涉及未包含在本批中的其他角色主线文本。
