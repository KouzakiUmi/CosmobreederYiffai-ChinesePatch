# batch-05-part01（BossuDex 图鉴与首领资料 第 1／3 部分）精校 summary

## 一、输入与读全情况

| 项 | 值 |
| --- | --- |
| 工单 | `batch-05-part01.reader.md` 1,409 行；`batch-05-part01.json` 4,992 行；`reference-excerpt.md` 57 行；`ORDER.md` 89 行 |
| 场景 | 49 场（全部 `read_full`，**无截断**） |
| 物理行 | 419 行 |
| `current` 为空的 ROW | 103 行（既有合句尾行，按工单不计漏译、不填充） |
| reader.md 读法 | 分 6 段读（1-130 / 131-380 / 381-630 / 631-880 / 881-1130 / 1131-1409），每段读完即落盘 coverage 与 findings |

`read_status` 全部 `read_full`；没有 `partial` / `not_read`。

## 二、发现分布

**33 条发现**（P05-101 … P05-133，连续无跳号），其中 31 条 `proposal`、2 条 `needs_evidence`。

| 级别 | 条数 |
| --- | --- |
| A | 3 |
| B | 21 |
| C | 7 |
| needs_evidence | 2 |

按 root 归组（全部为 `BossuDex.*`，单 root 批次）：

| root | 发现 |
| --- | --- |
| ClassicArcher | P05-101（A）、P05-109（B） |
| ClassicBugFlier | P05-106（B） |
| ClassicBugSpiker | P05-102（B）、P05-103（C） |
| ClassicCeilingTurret | P05-107（B）、P05-108（B） |
| ClassicDriller | P05-104（B）、P05-105（B） |
| ClassicDwarf / DwarfThrower | P05-111（B，跨 3 场同文） |
| ClassicFlamer | P05-112（B） |
| ClassicFlyDrone | P05-113（B） |
| ClassicFlybomb | P05-114（B） |
| ClassicGhoster | P05-115（C）、P05-132（C） |
| ClassicJellyfish | P05-116（B）、P05-123（B）、P05-131（C） |
| ClassicKobold | P05-117（B）、**P05-118（A，超限行）** |
| ClassicMine | P05-120（B） |
| ClassicMineCeilingZero | P05-121（needs_evidence）、P05-125（B） |
| ClassicSpikeball | P05-127（B，跨 2 场）、P05-133（C） |
| ClassicSpikebot | **P05-119（A，超限行）** |
| ClassicSwiper | P05-122（B） |
| ClassicViner | P05-124（B） |
| ClassicWyvern | P05-128（B） |
| ClassicXCannonCeiling / XCannonWall | P05-126（B）、P05-129（C） |
| ClassicFenfen | P05-130（needs_evidence） |

**场景结果分布**：`issues_found` 27 场、`retain` 22 场。retain（明确保留、不制造改动）：

SCb00e0afe598df446、SCf8c62480a20fd0e4、SCf6586c40fbe9c116、SC536952495ec81fad、SCbd0a2701a22721fa、SC0bb58fe0fcf2b7ae、SCc7497cb2ed284765、SCa0ee2bc475820f52、SC46fe33beaab2503d、SC751bba20914410de、SCbe1d43bc532dc353、SCded62a4b2c94a01d、SC3d677634b0b2a050、SC91e39fc45d57fee5、SCa226bce097a955f8、SCd87d2287f39ac987、SC7cbaa892b91bca38、SCdd47cd9cedefd19d、SC86c4c6277617752f、SC85c26ce8e54ee7d9、SC9d161b4b01135e77、SC4638eb14a860d6e2。

## 三、工单「四之二」的两条超限行（必报项）

| row_id | 场 | 现状 | 处理 |
| --- | --- | --- | --- |
| `CAT:O422deacf720938629a08` | SCcc1017cf7ebd30ac（ClassicKobold，女版） | 中文正文 56 全角字，实测 4 折行 | **P05-118（A）** 压到 41 字，条件全保留（早先报告／不少同僚特工／被科博德抓／能救就救／先做交易／保证他们安全） |
| `SFW01c279ac5b41aa55ec6a42b2` | SCfae065df9d829e6c（ClassicSpikebot，sfw） | 中文正文 66 全角字，实测 4 折行 | **P05-119（A）** 压到 47 字，保留「原本／如今」时间对比、运送对象、粗陋尖刺、搜寻入侵者四项事实 |

两条都属「三行英文已合并在一个物理行」的遗留，后面两个 ROW 的 `current` 保持为空，本条提案不改物理行数、不填充空行。压后正文分别为 41 与 47 个全角字，按每行约 20 全角字估，落在 3 行内，但**仍需实机 240px 复测确认**（见第六节）。

## 四、高风险连续段

### 4.1 问答错位（ClassicMine）
`SCb6f36febbdf9e0cd` 的 mine（矿）／mines（地雷）双关是全批最难处理的一处：
- Bossu 说「THE MINES OF TUTONE HAVE BEEN MINED」，现译「矿区，处处都是『雷区』」用引号硬造双关；
- Yiffai 的追问 `WELL SURE, BUT WHAT'S THAT GOTTA DO WITH EXPLOSIONS?` 被译成「挖矿有那么多忌讳？」，**凭空加了「忌讳」**（P05-120）；
- 由 Mauser 出面拆解（「老矿工在自家的矿井里埋了地雷」），这一段是全场信息落点，处理正确、不要动。

中文无法复现 mine 双关，P05-120 只做最小修正；若主代理希望保留「误解感」，备选是「……？矿区里当然有矿，可这跟爆炸有什么关系？」，但这句更靠近加义，需裁定。

### 4.2 合句断点（103 个空 current 的来源）
本批几乎所有「英文 2-3 行 → 中文 1 个物理行」的合句都没有句末标点，连读时会粘到下一句。已合并报为一条格式判点，不逐条凑数：
- P05-108（天花板炮塔）、P05-122（挥爪 sfw）、P05-123（水母女版）、P05-124（藤蔓怪）、P05-125（sfw 感应雷）、P05-126（加农炮男版）、P05-127（刺球，跨 2 场）、P05-105（钻探者）、P05-102（刺虫）。
- 女版双足飞龙 `SC91e39fc45d57fee5` 与 `SC09028b606f1f544b` 两行**行尾有半角空格**（P05-115 备注），会参与行宽测量，应删。

### 4.3 无线电套语
`YIFFAI/YIFFANY OUT` 在本批出现 4 种写法：`通话完毕`（5 处，主流）、`完毕`（2 处，短句收尾）、`下线`（1 处，P05-107）、`没译`（0 处）。P05-107 与 P05-128 指向「通话完毕」；建议主代理按全 root 频次一次统一，不要单点改。

## 五、男女两版不一致清单

| 现象 | 男版 | 女版 | 处理 |
| --- | --- | --- | --- |
| 精灵 MAY ALL BE FEMALE | 「也许全是雌性」 | 男版 sfw 场作「虽说全是女性」（升格为断言） | P05-101（A） |
| INDEED, AS FAR AS WE CAN TELL | 「就我们所能看出的而言」（直搬） | 「至少据我们目前了解是这样」／「据我们掌握的情况」 | P05-109 |
| 水母／灵能说法 | 「灵能扰乱」「灵能动荡」 | 「灵能躁动」／「灵能扰动」 | P05-132（C，建议统一为「灵能躁动」） |
| 矮人指称 | 「它们」与「他们」混用 | 全用「他们」 | P05-111（B，3 场同文） |
| 刺球 LITERALLY 对举 | 「打比方吧？」 | 「只是夸张一下吧？」 | P05-133（C，只改男版） |
| 加农炮 BELIEVE IT OR NOT | 「更近期造出来的，出自……之手」 | 女版一场作「那些是……那些蜥蜴……最近造出来的」（两个「那些」） | P05-129（C，只改女版天花板场） |
| 双足飞龙战术 | 删去束缚内容（sfw） | 保留 TEASER／BOUND SECURELY（nsfw） | 差分正确，**不动**（retain 判定） |
| 矮人 SO HUNG | 保留 | sfw 版整行删去 | 差分正确，**不动** |

## 六、未覆盖项与「本工单不能证明的东西」

1. **折行只是估算**。本批没有 240px／12px 的实际渲染证据，所有「压回 3 行」的判断基于字符宽度累计（全角 2、半角 1，正文 240px ≈ 20 全角字／行）。两行超限行的处置**必须**在构建里跑一次数据书容器校验才能确认，否则可能仍抛异常。
2. **`LIGHTTAZER` 与失真字幕口径**：本批未出现 `LIGHTTAZER`，失真字幕也无实例，因此对这两项**本工单不能提供任何新证据**。
3. **`ACTUAL_HINTS` 的下划线**（P05-121，`SC03c43e680b4ff75e` 的 `SFW3c0385107b32a2c4d0d39b95`）：不确定它是源文件排版残留还是运行时标记，标 `needs_evidence`，未提案。需比对归档原条目字节或看运行时是否替换。
4. **`FENFEN` / `Fenfen` 大小写**（P05-130，`SC46fe33beaab2503d`）：物种名在图鉴里是否应有中文条目名（「芬芬」？）本批无法判定，只建议统一英文写法，不新造译名。
5. **`lect` / `Lect`**（P05-117）：本批唯一一处小写写法，已按受保护标记口径建议恢复 `Lect`，但**不能证明**游戏内是否有大小写敏感的关键词替换。
6. **专名未译**：`ZERONIA`→「泽罗尼亚」、`PPP`（领地）、`TUTONE`→「图托恩」、`SCEAFYA`→「斯凯菲亚」在本批维持现状；这些属跨批次专名裁决，本批只记录，不提案。
7. **`DRACONID` 的族名**（P05-112）：`龙形科` → `龙类` 是本批唯一一处，但如果别批次已按「龙形科」落地，会形成新的跨批不一致——**本工单只覆盖 part01，无法证明**别批写法。
8. **引号风格不统一**：全批 `“”` 与 `「」` 混用（条目名「挥爪」「雷区」「挑逗」用 `“”`；「刺虫」「幽灵者」「光球」用 `「」`）。本批只在 P05-102 一处补了引号，**未做全局统一**——这属于跨 part 的格式裁决，留给主代理。
9. **成人向内容的保留**：本批 nsfw 场（双足飞龙束缚战术、矮人 SO HUNG、挥爪交配、芬芬服装）均按原文保留、未净化也未加码；`retain` 判定里已注明。**没有**对任何成人描写提出删改建议。
