# batch-05-part01 精校审校报告（第 1／3 部分：图鉴与首领资料）

**校对路线**：双路精校之 gemini 独立轨  
**基线版本**：`localization/builds/r9-polish-candidate13`  
**审核范围**：`BossuDex` root（前 49 场，419 物理行）

---

## 一、输入与阅读覆盖

- **工单文件**：`localization/editorial/r9-polish/batch-05-part01/orders/batch-05-part01.reader.md`（共 1,409 行）
- **结构化输入**：`localization/editorial/r9-polish/batch-05-part01/orders/batch-05-part01.json`（49 场，419 物理行）
- **实际阅读情况**：使用 `read` 工具以分段（offset/limit）方式完整阅读完全部 49 场场景，无任何抽样，无截断。
- **场景覆盖统计**：
  - 总场景数：49 场
  - 全覆盖输出：`localization/editorial/r9-polish/batch-05-part01/gemini/coverage.jsonl`（49 行，每场一行）
  - 发现问题场景数（`issues_found`）：11 场
  - 完全保留场景数（`retain`）：38 场
  - 存疑场景数（`needs_evidence`）：0 场

---

## 二、发现总数与等级分布

全批共检出并提出 **13 条** 精校发现与提案（`P05-101` ～ `P05-113`），详细记录于 `localization/editorial/r9-polish/batch-05-part01/gemini/findings.jsonl`。

### 1. 严重程度分布
- **A 类（严重排版超限）**：**2 条**（`P05-101`、`P05-102`）
  - 严格落实工单四之二已实测超限行要求，对实测在 240px 剧情框下折成 4 行的两处既有合句进行精简重写，在完整保留原意与所有条件前提下压回 3 行以内。
- **B 类（术语、语用、连贯性）**：**9 条**
  - **term（术语规范化）**：4 条（`P05-103` Spiker 刺甲机；`P05-104`、`P05-105` Driller 钻掘机；`P05-106` Squeaker 吱吱兽）
  - **continuity（上下文连贯与理解链）**：2 条（`P05-107` mine 采矿/地雷双关链修复；`P05-111` Come in 无线电与性暗示双关呼叫修复）
  - **idiom（语言习惯与翻译腔）**：2 条（`P05-108` as far as we can tell 机器直译腔改写；`P05-109` of course 句尾状语生硬后置改写）
  - **voice（角色语域与口吻）**：1 条（`P05-110` 波苏 在此 -> 波苏收到）
- **C 类（标点规范与微调）**：**2 条**
  - `P05-112`（打断处半角破折号规范为全角 `——`）
  - `P05-113`（去除呼语后异常半角空格并规范逗号停顿）
- **needs_evidence**：**0 条**

### 2. 按 Root 归组分布
| Root 分组 | 场景数 | 发现条数 | 发现 ID 及级别 |
| --- | --- | --- | --- |
| `BossuDex.ClassicArcher` | 3 | 1 | P05-108 (B) |
| `BossuDex.ClassicBarker` | 1 | 1 | P05-109 (B) |
| `BossuDex.ClassicBugFlier` | 2 | 1 | P05-110 (B) |
| `BossuDex.ClassicBugSpiker` | 1 | 1 | P05-103 (B) |
| `BossuDex.ClassicBulber` | 1 | 0 | - |
| `BossuDex.ClassicBumper` | 1 | 0 | - |
| `BossuDex.ClassicCannonFloor` | 1 | 0 | - |
| `BossuDex.ClassicCannonWall` | 1 | 0 | - |
| `BossuDex.ClassicCeilingTurret` | 1 | 0 | - |
| `BossuDex.ClassicCrawly` | 1 | 0 | - |
| `BossuDex.ClassicDriller` | 1 | 2 | P05-104 (B), P05-105 (B) |
| `BossuDex.ClassicDwarf` | 2 | 0 | - |
| `BossuDex.ClassicDwarfThrower` | 2 | 0 | - |
| `BossuDex.ClassicFenfen` | 1 | 1 | P05-111 (B) |
| `BossuDex.ClassicFlamer` | 1 | 0 | - |
| `BossuDex.ClassicFlyDrone` | 1 | 1 | P05-112 (C) |
| `BossuDex.ClassicFlybomb` | 1 | 0 | - |
| `BossuDex.ClassicGhoster` | 1 | 0 | - |
| `BossuDex.ClassicJellyfish` | 2 | 1 | P05-113 (C) |
| `BossuDex.ClassicKobold` | 1 | 1 | P05-101 (A) |
| `BossuDex.ClassicMine` | 1 | 1 | P05-107 (B) |
| `BossuDex.ClassicMineCeilingZero` | 2 | 0 | - |
| `BossuDex.ClassicMineWall` | 1 | 0 | - |
| `BossuDex.ClassicOrber` | 1 | 0 | - |
| `BossuDex.ClassicSpaceHead` | 2 | 0 | - |
| `BossuDex.ClassicSpikeball` | 2 | 0 | - |
| `BossuDex.ClassicSpikebot` | 1 | 1 | P05-102 (A) |
| `BossuDex.ClassicSqueaker` | 1 | 1 | P05-106 (B) |
| `BossuDex.ClassicSwiper` | 2 | 0 | - |
| `BossuDex.ClassicThorner` | 2 | 0 | - |
| `BossuDex.ClassicTribulb` | 1 | 0 | - |
| `BossuDex.ClassicViner` | 1 | 0 | - |
| `BossuDex.ClassicWyvern` | 2 | 0 | - |
| `BossuDex.ClassicXCannonCeiling` | 2 | 0 | - |
| `BossuDex.ClassicXCannonWall` | 1 | 0 | - |
| `BossuDex.ClassicXeno` | 1 | 0 | - |

---

## 三、高风险连续段与特定难点核查

### 1. 240px 剧情框下 4 折行超限行修复（A 类）
- **`CAT:O422deacf720938629a08`（SCcc1017cf7ebd30ac，波苏谈科博德抓走特工）**：
  - 现译共 54 字（约 648px），在 240px 框下实测已折成 4 行，超出一页 3 行容器硬上限。
  - 提案重写为：`  Bossu: [早先报告称你的不少同僚已被科博德抓走。能救就救他们，哪怕得做交易来确保特工安全。]`（40 字，约 480px）。
  - 保留全部“早先报告”、“同僚被抓”、“能救就救”、“做交易”、“确保特工安全”条件，实测压回 2~3 行内。
- **`SFW01c279ac5b41aa55ec6a42b2`（SCfae065df9d829e6c，波苏谈轮式机改装尖刺）**：
  - 现译共 60 字（约 720px），实测折成 4 行超限。
  - 提案重写为：`  Bossu: [这些小型轮式机原本在矿井里运送矿石与工具，但已被改装，加上了粗陋尖刺与搜寻入侵者的程序。]`（44 字，约 528px）。
  - 保留小型轮式机、运送矿石工具、改装、粗陋尖刺、入侵者程序全部信息，实测稳妥折为 3 行（第三行仅 4 字符）。

### 2. 双关语理解链条与上下文闭环（SCb6f36febbdf9e0cd）
- 场景内贯穿英文单词 `mine`（矿山/采矿 vs 地雷/埋雷 vs 我的）的三重双关。
- 波苏说：`the mines of Tutone have been mined`（图托恩的矿区被布了雷）。伊吠当成字面意义废话理解（“矿区当然开采过了”），因而困惑“可这跟爆炸有什么关系？”。随后麦森解释老矿工在矿井里埋地雷是为了宣示那是自己的矿（`THAT'S MINE!`）。
- 现译将伊吠误解的一句脑补成“挖矿有那么多忌讳？”，彻底脱离英文 `WELL SURE` 的字面误解前提。修复后前后逻辑与包袱自然呼应。

### 3. 无线电通讯呼叫与性暗示双关承接（SC46fe33beaab2503d）
- 伊吠无线电呼叫 `COME IN. BOSSU?` 现译误直译为“波苏，我进来了。”，脱离无线电通讯常理。
- 波苏顺势开黄腔接“希望你别进来，孩子”，是利用 `come in` 的俚语性暗示。
- 提案重写为 `呼叫波苏，进得来吗？`，既符合无线电呼叫语境，又使波苏后续接梗完全自然成立。

---

## 四、男女两版跨版本差异清单

本批中同一生物条目在不同版本（男线 `datadm` 与女线 `datadf`；NSFW 与 SFW）存在结构性分流，均予以细致比对核实：
1. **`BossuDex.ClassicArcher`**：
   - 女线 SFW（`SCb00e0afe598df446`）与男线 SFW（`SCbb24ffbfac0746d8`）针对几百年来精灵多出凡人特征的表述略有句式差异（“几百年过去，她们身上逐渐多了凡俗生灵的特征” vs “她们身上凡人的特征越来越多，几百年来一直如此”），但语义等价，保留各自版本特色。
2. **`BossuDex.ClassicBugFlier`**：
   - 女线 NSFW（`SC203f504ddad4428c`）中伊吠妮面对反复重生的无人机独立提问；男线 NSFW（`SCfeff53e003014bf2`）中伊吠呼叫波苏求援，波苏提起“你姐姐以前也这么说”，两线呼应良好。
3. **`BossuDex.ClassicCannonFloor` / `ClassicCannonWall`**：
   - 女线由伊吠妮主动指出炮塔与家乡训练装备相似；男线由伊吠支支吾吾回忆“我们是不是也用过类似……在……”，波苏替其补全“在训练的时候”，鲜明体现两人性格反差。
4. **`BossuDex.ClassicDwarf`**：
   - 男线 NSFW（`SC9bbf1f307dac7c56`）包含伊吠对矮人身材与硕大生殖器的惊叹；女线 SFW（`SCa0ee2bc475820f52`）则是伊吠妮讲述酒吧遇到的矮人念叨挖得更深与鼓声（致敬魔戒），分流明确。
5. **`BossuDex.ClassicWyvern`**：
   - 女线 NSFW（`SC3b0f76128c2a6465`）包含双足飞龙“高潮时容易分神、负责挑逗的特工需要捆绑”的成人机制探讨；男线 SFW（`SC85c26ce8e54ee7d9`）则替换为“攻击俯冲时容易分神”，符合分级口径。

---

## 五、未覆盖项与本工单不能证明的事项

1. **实机渲染与动态视口**：
   - 本次精校基于 12px 真实字形度量表（`story12.fnt`）与 240px 剧情框几何折行算法复核，未启动游戏实机进行显卡光栅化和着色器滤镜验证。
2. **全局未裁决项**：
   - 依照工单硬性约束，`LIGHTTAZER` 的写法及失真字幕的特殊口径保持现有形态，未做单点变更。
3. **既有合句尾行**：
   - 本批共 103 处 `current` 为空的 ROW 均为既有合句尾行，整场逻辑语义完整，未作填充亦未作为漏译处理。
