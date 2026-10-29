# batch-05-part03 精校小结（DS 路）

## 一、输入与阅读范围

| 项目 | 数值 |
| --- | --- |
| 工单正文 | `orders/batch-05-part03.reader.md`，1400 行 |
| 结构化数据 | `orders/batch-05-part03.json`，50 场、415 行 |
| 实际读完场景 | **50 / 50**（全部 `read_full`） |
| 实际读完行数 | **415 / 415**，无截断、无跳过 |
| `current` 为空的合句尾行 | **107 行**（参照摘录第三节写 103 行，实测多 4 行；按 ORDER 四·9 一律不报漏译、不填空行） |

阅读方式：`reader.md` 分 6 段（1–240、241–480、481–720、721–960、961–1200、1201–1400）逐段读完，并另建 974 行的 EN/ZH 归并视图（把空尾行折回其宿主句）以保证合句判读成立；归并视图只作读稿辅助，结论仍逐行对回 `batch-05-part03.json` 的 `row_id`。

## 二、发现总数与分布

**27 条发现**：A 3 条、B 24 条、C 0 条、needs_evidence 0 条。

按 category：format 12、term 7、idiom 4、meaning 3、continuity 1。

| 严重度 | finding_id | 判点 | root |
| --- | --- | --- | --- |
| A | P05c-101 | `MAY ALL BE FEMALE` 被升为断言（`虽说全是雌性`） | ClassicArcher |
| A | P05c-106 | ORDER 四之二点名的超限行压缩 | ClassicBullfrog |
| A | P05c-115 | 起名台词把 HOPPER 写成「跳跳兽」，词典条目为「跳跃者」 | ClassicHopper |
| B | P05c-102 | 半角连字符代替破折号 | ClassicBarker |
| B | P05c-103 | 整句结束缺句号 | ClassicBarker |
| B | P05c-104 | 整句结束缺句号 | ClassicBigboldEnemy |
| B | P05c-105 | 物种名残留英文 `Blocker`（5 行同批） | ClassicBlocker |
| B | P05c-107 | 同一物件一行「这些炮」一行「加农炮」 | ClassicCannonCeilingC |
| B | P05c-108 | 「炮台」应为「炮塔」 | ClassicCeilingTurret |
| B | P05c-109 | 收线套语「伊吠妮撤了」未跟库内「通话完毕」 | ClassicCeilingTurret |
| B | P05c-110 | 汉字间夹半角空格 | ClassicFenfen |
| B | P05c-111 | `FENFEN` 全大写夹空格，同场三行三种写法 | ClassicFenfen |
| B | P05c-112 | 喷火兽→喷火者、龙兽科→龙类（同句两处） | ClassicFlamer |
| B | P05c-113 | 同 root 仍写「喷火兽」 | ClassicFlamer |
| B | P05c-114 | 「被扰乱的灵能的化身」三个「的」连缀且读法偏 | ClassicGhoster |
| B | P05c-116 | 汉字间夹半角空格 | ClassicJellyfish |
| B | P05c-117 | 整句结束缺句号 | ClassicJellyfish |
| B | P05c-118 | 行尾两个多余半角空格；`LECT` 两侧空格 | ClassicKobold |
| B | P05c-119 | 感应地雷／引信施受错配 | ClassicMineZero |
| B | P05c-120 | 「你自己选」缺句末句号 | ClassicMineCeilingZero |
| B | P05c-121 | 「你选吧」缺句末句号 | ClassicMineWallZero |
| B | P05c-122 | 带刺无人机提醒缺句号（3 行同批） | ClassicSpikeballZero |
| B | P05c-123 | 完整句缺句号 | ClassicTentacle |
| B | P05c-124 | 「把这些报告当作不可靠的给驳回了」叠架句式读不通 | ClassicBlocker |
| B | P05c-125 | 与 part01 已改的同一英文句不同步 | ClassicBugFlier |
| B | P05c-126 | `WHILE` 从句读成使令，施受关系反 | ClassicWyvern |
| B | P05c-127 | `GAMBLED AWAY` 的「赌」被压掉 | ClassicDwarf |

## 三、高风险连续段

1. **跨版本（女线 datadf／男线 datadm）同句不同步**是本批最集中的风险。图鉴台词多为「同一英文句 + 男女两版载体」，历史批次（batch-05-part01）已对其中若干句定过改法，本批的姐妹载体却停在旧写法：P05c-101、P05c-109、P05c-111、P05c-112、P05c-114、P05c-116、P05c-117、P05c-120、P05c-121、P05c-122、P05c-125 均属此类。这类问题单看一场看不出，必须两条载体对读才成立。
2. **合句断点**：本批 415 行里 107 行是空 `current` 的尾行，句号该落在哪一行极易判错。所有「缺句末标点」的发现（P05c-103/104/117/120/121/122/123）都先确认了「英文句到此结束、下一行换说话人或换句」，不是把尾行的缺失错报到主行上。
3. **无线电套语**：`YIFFANY OUT` / `YIFFAI OUT` 在库内口径是「通话完毕」（part01 R9-0014／R9-0038）。本批 ClassicDwarf 与 ClassicDwarfThrower 已是「伊吠妮通话完毕」，ClassicCeilingTurret 仍是「伊吠妮撤了！」——同一套语一处掉队（P05c-109）。
4. **术语三处不齐**：阻挡者（P05c-105）、跳跃者（P05c-115）、喷火者（P05c-112/113）、炮塔（P05c-108）、加农炮（P05c-107）、龙类（P05c-112）、Fenfen（P05c-111）。每一条的 `reason` 都给了行级依据（`datav/dictionary.json` 条目名、同 root 另一场、或同批姐妹场的写法），没有只写「按术语表」。
5. **超限行**：全批 415 行用 candidate13 的 `story12` 实际字模逐字测宽，只有 1 行超限（即 ORDER 四之二点名的 `CAT:O6a441ed4e465d53414e1`，844px／4 行）。压缩稿 604px，240px 折 3 行、224px 折 3 行，已回到上限内（详见第五节）。

## 四、男女两版不一致清单

| 英文句 | 女线（datadf）／sfw | 男线（datadm） | 现状 |
| --- | --- | --- | --- |
| `THE ELVES OF SCEAFYA MAY ALL BE FEMALE…` | `虽然全是雌性`（SC1a561dc84c24895f，SFW3c55b548e14bb21d02c561d4） | `虽说全是雌性`（SCfa5abde862c1f019，CAT:O25871effa77ad5bdc2c5） | 两版都把 `MAY` 升成断言；已按 P05c-101 给出替换文本，本批只对 nsfw 载体开条，同一文本同时适用于 sfw 载体 |
| `THAT APPEARS TO HAVE BEEN A BLOCKER.` | `那看来是一只Blocker。`（SCaf4aa1fa18c98fd1） | `那看来是一只Blocker。`（SC3011f2ede9bd4f18） | 两版一致地保留英文，替换清单在 P05c-105 note |
| `WE DISMISSED THOSE REPORTS AS UNRELIABLE, BUT...` | `把这些报告当作不可靠的给驳回了`（SCaf4aa1fa18c98fd1） | `觉得这些报告不可靠，没有采信`（SC3011f2ede9bd4f18） | 女线不顺、男线通顺，P05c-124 只改女线 |
| `THESE CANNONS SEEM TO HAVE GONE A WHILE WITHOUT…` | `这些加农炮`（SC78ced646a25915e8、SC46b40e6ec47e8a6d） | `这些炮`（SC230a3742479654b5） | 仅男线术语不齐，P05c-107 |
| `W-WHAT'S UP WITH THESE ROBO BUGS…?` | `朝我冲过来…是怎么回事？`（SC81615de25860505a） | part01 已改「朝我扑…怎么搞的」 | P05c-125 只补 sfw 侧 |
| `SAAAY BOSSU, I'M NOT A MERMAID, AM I?` | `我说啊 波苏`（SCec58e954ab659019） | part01 已改「我说啊，波苏」 | P05c-116 只补 sfw 侧 |
| `WATCH OUT FOR THOSE PRICKLY DRONES…` | 男线／女线／sfw 三处均无句号 | 三处一致 | P05c-122 一条覆盖三条（note 列全） |
| `BE BOUND SECURELY WHILE THEIR COMRADES HIDE NEARBY.` | sfw 场无此句 | 男线 `让同伴埋伏` | P05c-126，施受关系错，仅男线 |
| `DUDE I MET AT A BAR…` | sfw 写「为自己赌博输光的」（正确） | nsfw 写「为输光的」（丢「赌」） | P05c-127，仅 nsfw |

## 五、超限行的处理结果

ORDER 四之二点名 `CAT:O6a441ed4e465d53414e1`（`BossuDex.ClassicBullfrog`，SCe041bcb2aac8daaa）。

- 实测：现译整行 **844px**，240px 折 **4 行**、224px 折 **4 行**，触发数据书 3 行上限。
- 提议：`  Bossu: [有报道称，吸足灵能的「跳跃者」会变成「牛蛙」，能从远处朝目标喷泡泡，也能用长舌头伤人。]`
- 实测：**604px**，240px 折 **3 行**、224px 折 **3 行**。
- 保留的条件逐项核对：报道称（REPORTS）／跳跃者（HOPPER）／吸足灵能（ABSORBS ENOUGH PSYCHIC ENERGY）／会变成牛蛙（WILL TURN INTO A BULLFROG）／能从远处朝目标喷泡泡（SHOOTING BUBBLES AT TARGETS FROM AFAR）／用长舌头伤人（DEALING DAMAGE WITH THEIR NEW ELONGATED TONGUE）。压掉的只有「一只」「只要…就」与「新长出来／修长／甚至」三个程度修饰，事实项无一删减。
- 全批其余 414 行同样逐行测过：无第二行超限；本批 27 条提议中也无一条把行数从 ≤3 推到 >3（逐条比对过 240px 与 224px 两个阈值）。

## 六、明确 retain 的场景

**28 场整场 retain**（无发现）：SCfaf58c7106ebaa23、SCd4c62fe6ca775014、SC2f1a5ca430de8d01、SC9c95983f9faabe43、SC78ced646a25915e8、SC46b40e6ec47e8a6d、SCad5fbd3752d9240e、SC6b734ddd13998107、SC8258ba5ecae9dd40、SC6c339d6b78783cae、SC1a561dc84c24895f、SCb327e21964f6852f、SCa1065637eb6d279f、SC9d02455b05384a16、SCf35da9060c1c0845、SC645851d9103deb6e、SC856845a9a0b37ad5、SCc6b40497803affd0、SCdcf3783bd4dd71a9、SC665698ef37728126、SC56eac4767b4dbc1a、SC242d9e3c6d253668、SCd9a68f9fcfe4b8e9、SCd847acdbd850f3b5、SC8fb3057f1201a27c、SCe810fe1962b453b0、SC46dca9c3abc6c734、SC259a5b414528c4fe。

其余 22 场记 `issues_found`。逐场判断与边界写在 `coverage.jsonl` 的 `notes`。

## 七、看过但**不报**的项（避免下一路重复劳动）

1. **`PPP` 两侧的空格**：`超出 PPP 的领地`、`PPP 手册` 等写法在语料里有 48 处，属既定排版，不报。
2. **`真正_有用的提示` 的下划线**：原文即 `ACTUAL_HINTS`，是对占位符风格玩笑的直译，全批仅此一处，判为有意的装置，不报。
3. **引号体例「」与“”并存**：项目内全局并存，单批内改动只会制造新的不一致，属体例问题而非本批判点，不报。
4. **`它们`／`他们` 的性别化改法**：ORDER 三与既有裁决明确排除，不报。
5. **`这些加农炮似乎已经有一段时间不需要自行修复了`**：`A WHILE WITHOUT NEEDING` 的时态被压成「不需要」而非「有一段时间没需要」，属语义轻微偏移，但三场逐字同文、且与紧随其后的「因此功率更高」因果链仍读得通，本批判为不构成误义，**不报**，仅在此记录供裁决参考。
6. **`THESE CANNONS SEEM TO HAVE GONE…` 一句里的「这些炮／这些加农炮」**：只把术语不齐作为判点（P05c-107），句子结构不动。
7. **`AHH, THAT SEEMS TO BE A SMALLER VERSION OF THE BLOCKER` 的「Blocker 的缩小版」**：已并入 P05c-105 的 5 行替换清单，不另开条。
8. **`IF I THOUGHT THAT YOU HAD THE OPTION, AGENT / I'D ENCOURAGE YOU WHOLEHEARTEDLY`**：现译「要是我觉得你有得选，我一定会全力支持你」意思成立，语气略平于原文的 `encourage…wholeheartedly`，属文笔层，不报。
9. **`FOR THE SAKE OF YOUR VIT BAR` 译作「为了你的体力条着想」**：`VIT BAR` 是 UI 血条，译法直白可读，不报。
10. **结巴与破音（`T-TRUE`、`GREEAAAAAT`、`W-WHAT`）**：均按功能保留了「说、说得也是」「真——好」「什、什么」，不报。

## 八、本工单不能证明的东西

1. **折行是估算，不是实机**。宽度用 `r7-render/tools/render.py` 的 `story12`（candidate13）真实字模逐字累加、240px 贪心折行得出，未在游戏内渲染验证。224px 数据书阈值另按容器事实复核了一遍，两档都 ≤3 行，但**真实分页仍以实机为准**；本批没有启动游戏，也没有截图佐证。
2. **术语改动只到「有行级依据」为止**。`阻挡者/跳跃者/喷火者/炮塔/加农炮` 的依据是 `datav/dictionary.json` 的条目名（`ClassicBlocker.popup`、`ClassicHopper.popup`、`ClassicFlamer.popup`、`ClassicCeilingTurret.popup`、`ClassicCannonCeilingC.popup`），`龙类` 无词典条目、依据是本批姐妹场写法与 part01 R9-0012。**这些依据能证明「库内不一致」，不能证明「译名已终裁」**；终裁权在 R3/R4 与主代理。
3. **107 行空 `current` 的合句归属是推断**。JSON 里空行不带英文，我按「紧邻上一非空行 + 说话人序列 + 英文断句」判定归属；若某行的宿主判错，基于它的标点判点（P05c-103/104/117/120/121/122/123）需要重判。全批逐条核对过「下一行是否换说话人/换句」，但没有归档侧的行级映射作二次校验。
4. **参照摘录与语料的 103／107 差额未定位**。摘录说本批 103 行空 `current`，实测 107 行。差额 4 行我未逐一定位到具体 `row_id`，只确认了总数。不影响判读（两类行都不报漏译），但说明摘录的计数口径与当前 JSON 不完全同步。
5. **只判了文字面**。没有做玩法条件、触发器、占位符替换的运行时验证；`@DerekChipReport`、`<3`、`$`、`%`、`|`、`Lect`、`OTP` 等保护标记在本批出现的行都原样保留，但**未跑构建或回归**。
6. **风格层只点到为止**。ORDER 三要求 C 级只报「能给出明确更优理由的」；本批 C 报 0 条。这不等于没有可继续打磨的句子，只等于我没有把握把某句判成「明显更优」而非「另一种写法」。
7. **未读取本目录 `ds/` 下已存在的评审文件**，本路结论与其他路完全独立，不构成交叉核验结果。
