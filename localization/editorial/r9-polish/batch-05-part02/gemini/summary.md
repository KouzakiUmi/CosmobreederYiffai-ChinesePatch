# batch-05-part02 精校（第二路·Gemini）审校总结

## 一、审校范围与执行概况

- **输入工单**：`localization/editorial/r9-polish/batch-05-part02/orders/batch-05-part02.reader.md`
- **正文规模**：工单全文共 1412 行，包含 50 个独立剧情／图鉴场景（均为 `BossuDex` 系列条目对白），418 个物理行节点（含 103 个既有合句留空行）。
- **读取与执行**：全文严格按 6 段分段依次读完（1-250、251-500、501-750、751-1000、1001-1250、1251-1412），每段读完即时落盘 findings 与 coverage，无任何跳读、遗漏或上下文截断。
- **全场覆盖率**：全批 50 个场景均完成整场连读并建立 coverage 台账记录（`read_full` 50 场，覆盖率 100%）。

---

## 二、发现总数与分布

本轮精校坚持**「默认保留、只提确凿问题」**的原则，共提出 **28 条提案（P05b-101 ～ P05b-128）**，涉及 18 个场景；其余 32 个场景全部通顺且符合人物口吻，明确判定为保留（retain）。

### 1. 级别（Severity）分布

| 级别 | 数量 | 占比 | 说明 |
| :--- | :---: | :---: | :--- |
| **A 级** | 10 | 35.7% | 包含两处 ORDER.md 四之二硬约束超限行、未译英文术语（SPIKERS、DRILLER、mine、Blocker）等结构与语义硬伤 |
| **B 级** | 18 | 64.3% | 标点缺失（漏句号）、西文引号/双引号、半角问号、半角连字符代替破折号、行内多余空格、保护标记大小写不规范等 |
| **C 级** | 0 | 0.0% | 不提无明确更优依据的润色，避免制造无谓改动 |
| **needs_evidence** | 0 | 0.0% | 原文逻辑与说话人明确，无存疑留置项 |

### 2. 类别（Category）分布

- **format（格式与标点）**：21 条（占 75.0%）
  - 句末漏标点：8 条（L2932、L2847、L2776、L2908、L3329、L2875、L2887 等整句末尾缺句号）
  - 西文标点与引号规范：7 条（弯引号改直角引号、半角转义双引号、半角问号空格、连字符代替破折号）
  - 容器超限压缩：2 条（四之二指定超限行 CAT:Od65baabc30d343ed6f34 与 CAT:O829863279bb55814844e）
  - 空白与空格缺陷：4 条（汉字夹空格、行尾残留空格、保护字段夹空格）
- **term（术语未译与一致性）**：6 条（占 21.4%）
  - `SPIKERS` → 「刺虫」（P05b-102）
  - `DRILLER` → 「钻探者」（P05b-104, P05b-105, P05b-106, P05b-107）
  - `BLOCKER` → 「阻挡者」（P05b-124）
- **continuity（同场前后一致性）**：1 条（占 3.6%）
  - Fenfen 在同一场内大小写及空格不一致（P05b-108）

---

## 三、硬约束与超限行处理结果

依照 ORDER.md 第「四之二」节实测超限行要求，本批点名的 2 行超限文本均已在保证原意、事实与条件完整的前提下精简压回安全线，并在 findings.jsonl 中立项：

1. **`CAT:Od65baabc30d343ed6f34`（`P05b-103`，ClassicBullfrog）**
   - 原文行：`  Bossu: [有报道称，一只「跳跃者」只要吸收了足够的灵能，就会变成「牛蛙」，能从远处朝目标喷吐泡泡，甚至还能用新长出来的修长舌头造成伤害。]`（共 62 字，实测折成 4 行，超限爆框）
   - 提案行：`  Bossu: [据报「跳跃者」吸足灵能会化为「牛蛙」，能远射泡泡，并以长舌伤人。]`（压缩至 32 字，保留据报传闻、吸收灵能化为牛蛙、远程吐泡与长舌伤害全要素，压回 3 行以内）
2. **`CAT:O829863279bb55814844e`（`P05b-122`，ClassicSpikebot）**
   - 原文行：`  Bossu: [那些小小的轮式无人机曾经用来运送矿井里的矿石和工具，但这些单元已经被加上简陋尖刺和搜寻入侵者的逻辑，经过了改装。]`（共 59 字，实测折成 4 行，超限爆框）
   - 提案行：`  Bossu: [这些轮式无人机原用于矿井运输，现已被改装上粗糙尖刺与搜敌逻辑。]`（压缩至 30 字，保留轮式无人机、原矿井运输功能、改装尖刺与搜敌逻辑全要素，压回 3 行安全线以内）

---

## 四、场景保留判定清单（32 场）

以下 32 个场景经全文通读，对白完整、符合波苏/特工的人设语域、无设定与格式缺陷，明确判定为全部保留（retain）：

- `SCbbb3f9743ac83409` (ClassicBarker)
- `SCc77858a16e5f3301` (ClassicBigboldEnemy)
- `SC8284617482e0142b` (ClassicBulber)
- `SCa7d50e8f2d64a2e7` (ClassicBumperC 女线)
- `SCf89ffbe39fe88fa1` (ClassicBumperC 男线)
- `SC3fd869c6a2937dd3` (ClassicBumperPlus 男线)
- `SC74eacd540a84f4fd` (ClassicBumperPlus 女线)
- `SC9acf15ba7fbb4877` (ClassicCannonFloor)
- `SCbbbce3c2e89f8789` (ClassicCannonFloorC)
- `SC26dbe5fa7ee9cf03` (ClassicCannonWallC 女线)
- `SCef111241d8b20356` (ClassicCannonWallC 男线)
- `SCca127a62c96d9ff5` (ClassicDwarfThrower)
- `SC1ed8b1131ee2b80b` (ClassicElf 女线)
- `SC8a64100509cd1232` (ClassicElf 男线)
- `SC3048c12be4e1ae2d` (ClassicElf SFW线)
- `SC0a53291b68449545` (ClassicFire)
- `SCe892358017ef4806` (ClassicFlybomb)
- `SC7cb61827f3957704` (ClassicIvyball)
- `SC5c5f5477be1d2b03` (ClassicJellyfish)
- `SCc39f2393aa7808ee` (ClassicMineWallZero 女线)
- `SC862403c68f1d4607` (ClassicMineWallZero SFW线)
- `SC2314258606729cd4` (ClassicMineZero SFW线)
- `SCcac2a16949d1ed95` (ClassicOmegothrower)
- `SCa365f4cac4cbee44` (ClassicOrber)
- `SCcca65604ac8d3a29` (ClassicSpaceHead)
- `SC3a28513b100a3730` (ClassicSpiderbot 女线)
- `SCeb6f35bc1c4dc1e8` (ClassicSpiderbot 男线)
- `SCd60875d2efc81ef1` (ClassicSpikebot 男线)
- `SC56e5db567ec62cce` (ClassicXeno 男线)
- `SC6b77e7e0f15fd941` (ClassicXeno 女线)

---

## 五、高风险段与男女版本差异观察

1. **矿井与地雷谐音烂梗（`mines` / `mined` / `mine!`）**：
   - 英文原文利用了 mine（矿井）、mine（地雷）、mine（我的）的三重同音双关。在 `SCf220ad115895cc8e` 中前轮译者直接裸留了英文单词「mine」（`埋了mine`、`mine炸了`），已在 P05b-113 与 P05b-114 中修正为「地雷」。在 `SCb84957d4bbe46c64` 中前轮译者采用了创译「认了主」，但夹带西文引号与半角连字符，已在 P05b-116～P05b-119 修正标点。
2. **男女版差异**：
   - 女线（伊吠妮 Yiffany）与男线（伊吠 Yiffai）各对白根据角色语气有细微差别（女线略显傲娇吐槽，男线偏向学生气与莽撞），译文均成立并分别保留，未做跨版本机械抹平。
   - `ClassicSpiderbot` 中男女线对白结构基本对称，女线用「射蛛网」、男线用「喷蛛丝」，均自然成立。

---

## 六、未覆盖项与本工单不能证明的事情

1. **折行宽度为理论估算**：改动行的折行宽度是基于数据书 224px 宽、12px 字体（约 18 个全角字/行，3 行上限约 30 字，安全线 28-30 字）进行的静态字符数与视觉长度估算，**尚未经过游戏引擎底层实际运行时的像素排版渲染核验**。
2. **未填充合句空尾行**：本批中 103 个 `current` 为空的物理行严格按规定未报漏译、未提案填充，整句逻辑均已在上部行内闭环。
3. **未被点名的长合句行**：部分非点名但长度偏长的合句首行（如 `SCd60875d2efc81ef1` 的 `CAT:O9df35108fe2d4ae2dd0e` 约 49 字），按工单「默认保留、不越界重写」原则未作擅自压缩，交由后续阶段决定是否实测调整。
