# batch-06-part02 第二路（Gemini）审校总结

## 一、审校范围与执行概况

- **工单文件**：`localization/editorial/r9-polish/batch-06-part02/orders/batch-06-part02.reader.md`（共 1540 行）。
- **结构数据**：`batch-06-part02.json`。
- **审校规模**：实际完整读完 65 场，覆盖全部 441 个物理行（ROW 节点），无截断、无跳读、无遗漏。
- **全场判定分布**：
  - **保留场（retain）**：47 场
  - **发现缺陷场（issues_found）**：18 场
  - **存疑需取证场（needs_evidence）**：0 场
- **发现总数**：共计 20 条（编号 `P06b-101` ~ `P06b-120`，连续递增）。

## 二、发现等级与类别分布

### 1. 严重程度等级分布

| 等级 | 数量 | 说明 |
| :--- | :--- | :--- |
| **A** | 4 | 包含点名 3 处超限行压缩（P06b-109、P06b-117、P06b-120），以及 1 处硬约束按键代码违规汉化（P06b-110 `UP+攻击` → `UP+ATTACK`） |
| **B** | 16 | 结构性缺陷：句末标点缺失（8 处）、行尾多余半角空格（4 处）、半角连字符代替破折号（1 处）、跨行复句漏标点（1 处）、残留旧译名「狗头人」（1 处 `P06b-114`） |
| **C** | 0 | 纯润色不提，严格遵循精校与保留原则 |
| **needs_evidence** | 0 | 原文事实与施受关系清晰，无需留置 |

### 2. 类别分布

- `format`：18 条（超限行压缩 3 条、标点缺失与补齐 8 条、行尾多余空格清除 4 条、破折号规范 1 条、跨行标点 1 条、句尾空格 1 条）
- `gameplay`：1 条（P06b-110 恢复受保护的硬约束玩法按键 `UP+ATTACK`）
- `term`：1 条（P06b-114 依据已落地裁决纠正残留旧译名「狗头人」为「科博德」）

### 3. 按 Root 归组统计

| Root | 场数 | 发现数 | 涉及 Finding ID |
| :--- | :--- | :--- | :--- |
| `TomcatItems.CosmoCard` | 1 | 1 | P06b-101 |
| `TomcatItems.IceCola` | 1 | 1 | P06b-102 |
| `TomcatItems.JudoBody` | 1 | 2 | P06b-103, P06b-104 |
| `TomcatItems.KoboHead` | 2 | 3 | P06b-105, P06b-106, P06b-107 |
| `TomcatItems.PsyTea` | 1 | 1 | P06b-108 |
| `TomcatItems.SpecialFap` | 1 | 1 | P06b-109（点名超限行） |
| `TomcatItems.SpecialHookshot` | 1 | 1 | P06b-110（玩法按键） |
| `TomcatItems.SpecialPsycards` | 1 | 1 | P06b-111 |
| `TomcatItems.SpecialRadio` | 1 | 1 | P06b-112 |
| `TomcatItems.SpecialRightmark` | 1 | 1 | P06b-113 |
| `TomcatItems.StatCream` | 1 | 1 | P06b-114（科博德术语） |
| `TomcatItems.StatMelon` | 1 | 1 | P06b-115 |
| `TomcatItems.StatPepper` | 1 | 1 | P06b-116 |
| `TomcatItems.TazerPirate` | 2 | 1 | P06b-117（点名超限行） |
| `TomcatItems.ZenerSquare` | 2 | 2 | P06b-118, P06b-119 |
| `TomcatItems.ZenerStar` | 1 | 1 | P06b-120（点名超限行） |
| 其余 47 场 | 47 | 0 | 全场保留（retain） |

## 三、三条实测超限行的处理结果（ORDER.md 第四节之二）

本批在 240px / 12px 容器下实测折成 4 行、超出每页 3 行限制的 3 处既有合句遗留行，已全部逐行压回安全线以内（每行控制在 31~34 个全角字），保留全部限定条件、传闻语境与玩法事实：

1. **`CAT:Ob2dee70046f920c2187b` (`TomcatItems.SpecialFap`, P06b-109)**
   - 原文：`[TECHNICALLY, A FIELD ATTENUATED PRISM. IF YOU'VE / GOT A CREATURE WHO LIKES YOU A LOT, YOU CAN PET THEM TO / CHARGE UP YOUR CRYSTAL WITH POWER! THE EFFECT IT HAS / VARIES PER CREATURE!]`
   - 当前（56字，折成4行）：`  Tomcat: [严格说，是场衰减棱镜。如果你有一只很喜欢你的生物，可以抚摸它来给你的水晶充上力量！它产生的效果因生物而异！]`
   - 提案（33字，折成3行以内）：`  Tomcat: [严格讲是场衰减棱镜。抚摸亲近你的生物能给水晶充能，效果因生物而异！]`
   - 效果：完整保留「严格讲是场衰减棱镜」技术全称、「抚摸亲近你的生物」触发条件、「给水晶充能」以及「效果因生物而异」全部原意事实。

2. **`CAT:O5b04f565832c0afe4716` (`TomcatItems.TazerPirate`, P06b-117)**
   - 原文：`[JUST HOLDING IT, I CAN IMAGINE THE BIG STRONG PIRATE IT / BELONGED TO. THE KINDA GUY WHO KNEW WHAT HE WANTED AND / WAS WILLING TO TAKE IT. ROUGHLY, IF NECESSARY... HEH...]`
   - 当前（68字，折成4行以上）：`  Yiffany: [光是握着它，我就能想象它原来属于的那个高大强壮的海盗。那种清楚自己想要什么，而且就会动手去夺的人，必要时还会来粗的……呵……]`
   - 提案（34字，折成3行以内）：`  Yiffany: [光握着它就能想象前主人：高大强壮、想要就夺，必要时还来粗的……呵……]`
   - 效果：完整保留握持想象海盗前主人、「高大强壮」、「想要就夺」以及「必要时还来粗的……呵……」全部风味与调侃。

3. **`CAT:Ob0a366ecee3d12369186` (`TomcatItems.ZenerStar`, P06b-120)**
   - 原文：`[THE REPORTS WE RECEIVED SAID THAT, WHILE IN COMBAT / THE AGENTS COULD CHOOSE THEIR POWER WITH "SELECT" / AND THEN THEY COULD CALL FORTH THEIR ABILITIES / BY PRESSING "UP"+"ATTACK" TOGETHER.]`
   - 当前（54字，折成4行）：`  Tomcat: [收到的报告说，在战斗中，特工能按“SELECT”选择能力，然后同时按“UP”+“ATTACK”，就能使出对应的能力。]`
   - 提案（31字，折成3行以内）：`  Tomcat: [报告称战斗中按 SELECT 选能力，再同按 UP+ATTACK 即可使出。]`
   - 效果：保留「报告称」传闻限定语、不改玩法条件、完整保留 `SELECT` 与 `UP+ATTACK` 保护按键代码。

## 四、高风险连续段与关键判定

1. **玩法操作按键硬约束一致性（P06b-110）**
   - 在 `SCc7219f770fd727bd`（`TomcatItems.SpecialHookshot`）中，前一行 Yiffany 正确表达为 `UP+ATTACK`，但下一行 Tomcat 的应答却被翻译成了「再按 UP+攻击」。按键代码汉化违反了 ORDER.md 硬约束，且破坏了同场一致性。已纠正为保留原码的 `UP+ATTACK`。
2. **已落地术语回改清理（P06b-114）**
   - 在 `SCd2d37898261b3679`（`TomcatItems.StatCream`）中，当前译文残留旧译名「狗头人」。ORDER.md 第五节与已落地术语明确规定 KOBO / KOBOLD 统一为「科博德」，已提修正案消除漂移。
3. **句末标点漏失的系统性修补**
   - 本批发现多达 8 行单句结尾完全遗漏标点（如 `慢慢看卡片背面吧，小狗`、`也许这就是你老是打起来的原因`、`别忘了你身上有光电击枪` 等），均已在 `findings.jsonl` 中逐行定位并补齐句号，消除排版断气感。
4. **行尾残余半角空格清理**
   - 发现 4 处行尾 `]` 之后带有 1~2 个半角空格（P06b-111、P06b-112、P06b-113、P06b-119），已全部提单清理，避免参与行宽测量或破坏物理行校验。

## 五、男女两版的不一致清单与对照

1. **`TomcatItems.Pickaxe`（矿镐）**：
   - 男线 `SC436d5a6ce25a8ce3`：Yiffai 关注自己臂力只能扔一次，表示「只要扔得够用力、够高就行……」；
   - 女线 `SC7c140d8789921bd4`：Yiffany 借机调侃 Tomcat「正好练习把你喝醉了扔出去」，Tomcat 吐槽「哇，真无礼」。
   - 判定：男女线剧本原设计完全不同，各自准确传达，保留差分。
2. **`TomcatItems.PirateBody`（海盗夹克）**：
   - 男线 `SCa93243c53864e00e`：Yiffai 觉得自己穿着像个酷海盗，被 Tomcat 吐槽像穿爸爸衣服的小狗崽；
   - 女线 `SCeb8000b49b6c43e2`：Yiffany 闻出前主人气味并联想潇洒亡命徒，Tomcat 调侃其想了解前主人；
   - SFW 线 `SCb95ded726391ead1`：净化调侃，转向装备属性提升教学。
   - 判定：三者角色性格与版本分级差异鲜明，保留现状。
3. **`TomcatItems.ZenerSquare`（齐纳方块）**：
   - 男线 `SC5ef5b1f865e8f630` 与 女线 `SC1c0e8e24cfeaa003`：
     - 女线分为了两行展示，前半句 `就算其他特工的故事都是真的` 漏了逗号（P06b-118 已补齐）；男线则合为单行显示，行尾残留多余半角空格（P06b-119 已清掉）。

## 六、本工单不能证明的事项（局限性声明）

1. **剧情框折行是理论估算**：
   - 本审校依据 240px 宽度、12px 字体以及中西文混排的安全字宽（每行约 18~20 全角字，安全总字数不超过 30~34 字）进行压缩。实际游戏运行时的排版受 libGDX 动态字距、标点压缩及前缀 `Tomcat: [` 宽度的影响，具体视觉效果须以实机渲染阶段验证为准。
2. **引号体例与 LIGHTTAZER 未终裁**：
   - 工单内 `“”` 与 `「」` 混用属于全局待裁事项，本批未做机械统一；`LIGHTTAZER` 的三种写法并存亦按规范未做单点翻案。
3. **既有合句尾行（current 为空）**：
   - 本批内 100 处 current 为空的 ROW 节点均属合句后半部分，经核对整场语义均已完整表达，未作漏译汇报与填充。
