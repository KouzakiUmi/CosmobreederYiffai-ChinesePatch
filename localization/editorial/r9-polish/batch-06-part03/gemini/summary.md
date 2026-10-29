# batch-06-part03 审校总结报告（Gemini 路）

## 一、审校范围与完成度

- **工单文件**：`orders/batch-06-part03.reader.md`（共 1,519 行，全长完整阅读，无任何截断）
- **结构化工单**：`orders/batch-06-part03.json`（共 65 个场景）
- **审校场景总数**：65 场
  - 全部场景 `read_status` 均为 `read_full`，无遗漏、无部分阅读（`partial: 0`，`not_read: 0`）。
- **产出文件**：
  - `gemini/findings.jsonl`：共 32 条发现（编号从 `P06c-101` 至 `P06c-132` 严格连续）。
  - `gemini/coverage.jsonl`：共 65 行（每场一行，对应全量 65 个场景）。
  - `gemini/summary.md`：本审校总结报告。

---

## 二、发现分布与统计

### 1. 分级统计

| 等级 | 数量 | 占比 | 主要问题特征 |
| :--- | :---: | :---: | :--- |
| **A 级** | 7 | 21.9% | 核心玩法按键汉化违背硬约束、门卡玩法逻辑颠倒、否定语序颠倒、核心定语漏译、残留旧译「狗头人」、非人代词错位 |
| **B 级** | 25 | 78.1% | 打断处半角连字符替代破折号、行尾多余半角空格、句末缺失标点/省略号、前缀格式错误、翻译腔微调 |
| **C 级** | 0 | 0.0% | 严格遵循不为润色凑数的判据，意思与口吻均成立者一律记为 retain |
| **needs_evidence** | 0 | 0.0% | 本批场景设定与上下文逻辑自洽，无原文矛盾未明事项 |
| **合计** | **32** | 100% |  |

### 2. 类别统计

- **format（结构缺陷/格式规范）**：24 条（含 2 处违反硬约束翻译按键名、9 处行尾多余空格、4 处打断连字符、2 处前缀多余空格、3 处句末缺标点等）
- **meaning（语义理解/否定/定语漏译）**：3 条（P06c-102 否定与频度副词错位、P06c-114 漏译 glowing、P06c-124 怪物指代误用「他们」）
- **continuity（语境承接/顺畅度）**：3 条（P06c-122、P06c-129、P06c-131）
- **gameplay（玩法机制与指代关系）**：1 条（P06c-108 门卡与门代词混淆导致逻辑颠倒）
- **term（术语一致性）**：1 条（P06c-115 残留旧译「狗头人」改「科博德」）

### 3. 按场景与 Root 归组统计

| Root 模块 | 场景总数 | 发现问题场景数 | 发现项编号 |
| :--- | :---: | :---: | :--- |
| `TomcatItems.DoggyBody` | 1 | 1 | P06c-101 (B), P06c-102 (A) |
| `TomcatItems.IceCola` | 1 | 1 | P06c-103 (B), P06c-104 (B) |
| `TomcatItems.KoboHead` | 1 | 1 | P06c-105 (B) |
| `TomcatItems.PsyJuice` | 2 | 1 | P06c-106 (B) |
| `TomcatItems.SpecialHookshot` | 1 | 1 | P06c-107 (A) |
| `TomcatItems.SpecialKeycard2` | 1 | 1 | P06c-108 (A) |
| `TomcatItems.SpecialLeftmark` | 2 | 2 | P06c-109 (B), P06c-110 (B) |
| `TomcatItems.SpecialPsycards` | 1 | 1 | P06c-111 (B) |
| `TomcatItems.SpecialRadio` | 2 | 1 | P06c-112 (B) |
| `TomcatItems.SpecialRightmark` | 2 | 2 | P06c-113 (B), P06c-114 (A), P06c-115 (A), P06c-116 (B) |
| `TomcatItems.SpecialShoes` | 1 | 1 | P06c-117 (A) |
| `TomcatItems.SpecialTorch` | 1 | 1 | P06c-118 (B), P06c-119 (B) |
| `TomcatItems.StatTadpole` | 2 | 1 | P06c-120 (B) |
| `TomcatItems.TazerCombat` | 2 | 2 | P06c-121 (B), P06c-122 (B), P06c-123 (B) |
| `TomcatItems.TazerTrainer` | 1 | 1 | P06c-124 (A) |
| `TomcatItems.TribalHead` | 2 | 1 | P06c-125 (B) |
| `TomcatItems.VitDrumstick` | 1 | 1 | P06c-126 (B) |
| `TomcatItems.Vitamin` | 1 | 1 | P06c-127 (B), P06c-128 (B) |
| `TomcatItems.ZenerSquare` | 1 | 1 | P06c-129 (B), P06c-130 (B) |
| `TomcatItems.ZenerTriangle` | 2 | 1 | P06c-131 (B), P06c-132 (B) |
| 其余未列出 Root | 42 | 0 | 均全场 retain |

---

## 三、保留场景（Retain）

全批 65 场中，共有 **42 场** 判定为完全保留（`retain`，未发现任何 A/B 级缺陷）：
- `SC8852723f33cca1c4` (`TomcatItems.CosmoBody`)
- `SC68dc400330a64e6b` (`TomcatItems.CosmoCard`)
- `SCe946e1615557b3b0` (`TomcatItems.CosmoHead`)
- `SCeee7ed3bf405040c` (`TomcatItems.DoggyHead`)
- `SC90603cd8369952c3` (`TomcatItems.FakeMeat`)
- `SCae0193408d5c5952` (`TomcatItems.Key`)
- `SC713dd4f4639c27ba` (`TomcatItems.KoboBody`)
- `SC4f4a4681733bb015` (`TomcatItems.KoboBody`)
- `SC08992bdfdaac71d2` (`TomcatItems.MapDataANorth`)
- `SCefc0658ae5f91646` (`TomcatItems.MapDataASouth`)
- `SCb4cb2468911b4ddf` (`TomcatItems.MapDataASouth2`)
- `SCe146c433653ff1ac` (`TomcatItems.MapDataCWest`)
- `SCc208e23b19701617` (`TomcatItems.PirateHead`)
- `SC95acdb756277c139` (`TomcatItems.PsyJuice`)
- `SCc88414db26b72d6f` (`TomcatItems.ShipGun`)
- `SC1356d42d140300ed` (`TomcatItems.ShipRadar`)
- `SC156d54281be3db1d` (`TomcatItems.SpecialAnklet`)
- `SC082d1b3508575bc4` (`TomcatItems.SpecialBrace`)
- `SC43c37118b5ace3c2` (`TomcatItems.SpecialBrace`)
- `SC9dd4b9fe2a82c8d9` (`TomcatItems.SpecialCosmoID`)
- `SC6c3b75ae520ac8a6` (`TomcatItems.SpecialGeiger`)
- `SCe9732a0041688966` (`TomcatItems.SpecialKeycard1`)
- `SC9bb714108286af8a` (`TomcatItems.SpecialKeycard3`)
- `SC8378b700b839e0ab` (`TomcatItems.SpecialRadio`)
- `SC1152b760ddce4ff4` (`TomcatItems.StatFishtaco`)
- `SCa65282877c3f637d` (`TomcatItems.StatFortune`)
- `SCe8ddc9a22b3f0425` (`TomcatItems.StatFortune`)
- `SCcfed64c6d940ad62` (`TomcatItems.StatOctopus`)
- `SC8cff10bbe01476b9` (`TomcatItems.StatOctopus`)
- `SC9f9c8b44c91a0546` (`TomcatItems.StatSpirit`)
- `SC01445b26a7f89ccc` (`TomcatItems.StatTadpole`)
- `SC098d910f490ceae6` (`TomcatItems.TazerKobo`)
- `SC185dc07922df6938` (`TomcatItems.TazerKobo`)
- `SCf0b74e4a2e72ba8d` (`TomcatItems.TazerKobo`)
- `SCa84ca531944c6858` (`TomcatItems.TazerPirate`)
- `SC790eb4964d498889` (`TomcatItems.TribalHead`)
- `SCa4638c3c48cd8a1f` (`TomcatItems.UpgradeChip`)
- `SC2021e07e5d156b67` (`TomcatItems.VitBone`)
- `SC90897e71c7ab3192` (`TomcatItems.VitBone`)
- `SC9f73cfb4361705ec` (`TomcatItems.VitBone`)
- `SC3eca555452e3d9dd` (`TomcatItems.ZenerCross`)
- `SC188abbfbd53fac7b` (`TomcatItems.ZenerTriangle`)

**保留理由**：
上述场景连读上下文流畅，角色性格与口吻鲜明（雄猫的调侃、伊吠的顺从反差、伊吠妮的豪放），既有合句尾行完整承接语义，保护标记及按键名完整无缺，无翻译腔滞涩或事实冲突，符合「无语病且保留人物差异的译文明确记 retain」原则。

---

## 四、高风险连续段与重点判点

1. **按键名汉化违背硬约束（A 级重大违规）**：
   - **`P06c-107` (`SC380c91faa6db871f`)**：`UP+ATTACK` 在伊吠台词中被译作「UP+攻击」，而同场紧接着雄猫的台词已采用「UP+ATTACK」。ORDER.md 第四节明确要求按键名原样保留，故修正为英文原样。
   - **`P06c-117` (`SCc628ffe48ea2eae1`)**：`PRESS "DOWN"+"JUMP"` 被翻译为「按"下"+"跳跃"」，严重违反硬约束保护标记，且前缀带有两个空格，修正为「按 DOWN+JUMP」。
2. **门卡玩法逻辑颠倒（A 级机制破坏）**：
   - **`P06c-108` (`SCb28ad558d39b8510`)**：原文 `YOU CAN OPEN DOORS UP TO THE LEVEL DISPLAYED ON THEM!`，代词 `them` 指代前文的 `keycard`（即：能打开最高不超过门卡等级的门）。现有译文误作为「你能打开等级不超过门上所标数字的门」，导致语义混乱不可解。对照同类场景 `SC9bb714108286af8a` 修正为「凭这张门卡，同级或更低级的门都能打开！」。
3. **否定词与频度副词错位反问失效（A 级误义）**：
   - **`P06c-102` (`SC1667be893970acf7`)**：`YOU'RE GONNA TELL ME YOU STILL DON'T DIP INTO SOFT FOOD EVERY NOW AND AGAIN?` 现译直搬英文为「你该不会告诉我，你现在还是不偶尔吃点软食吧？」，双重否定导致语意反转。修正为符合中文反诘逻辑的「你该不会想说，你现在平时都不偶尔吃点软食了吧？」。
4. **物种旧译残留（A 级术语统一）**：
   - **`P06c-115` (`SCac703fc5683db815`)**：`KOBOLD` 在全库 99 处统一为「科博德」，但在该 SFW 场景中残留了旧译「狗头人」，已依据全库事实与对应 NSFW 场修正。

---

## 五、男女两版及 SFW/NSFW 差异说明

- **`TomcatItems.KoboBody`**：
  - 女线 NSFW (`SC713dd4f4639c27ba`)：伊吠妮大肆调侃雄猫在学院时期加入的「性社团（sex club）」与鳞装玩具尺寸，雄猫羞愤想挂断通讯。
  - 男线 SFW (`SC4f4a4681733bb015`)：雄猫仅科普鳞装造价高昂（数千 Lect），语气正经。两线差异巨大，系原作独立台词，两边各自完整成立。
- **`TomcatItems.StatOctopus`**：
  - 男线 NSFW (`SCcfed64c6d940ad62`)：雄猫狂热喊「DUDE...」，台词排版镜像为「老——兄……」。
  - 女线 SFW (`SC8cff10bbe01476b9`)：雄猫台词末尾译作「兄 弟 ……」，已确认是原文 `D U D E . . .` 的逐字排版镜像，按工单指示保留不报。
- **`TomcatItems.SpecialShoes`**：
  - 男线在此前批次已处理，女线在此出现，雄猫出现典型猫叫口癖「BOUNCE BOUNCE, MEOW!!」（弹啊弹，喵！！），此为原文仅有的猫叫设计，予以保留。

---

## 六、本工单不能证明的东西

1. **折行与实际渲染像素**：所有提议的中文行长度（均控制在 20–28 个汉字区间，单页最多 3 行）是基于 240px 容器及 12px 字体折行的理论估算，无法在纯静态文本下 100% 证明在游戏 libGDX 特殊抗锯齿或不同分辨率下拉伸后的精确换行位置。
2. **失真无线电与全大写情绪**：原文全大写在道具说明中多为系统说明或雄猫夸张调侃，译文在大部分场景采用了全角感叹号与生动措辞，但无法断定玩家实机音效或无线电特效是否伴有特殊颤音。
