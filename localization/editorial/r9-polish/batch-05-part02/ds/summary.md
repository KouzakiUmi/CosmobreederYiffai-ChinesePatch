# batch-05-part02 二路精校小结（ds 路）

## 一、输入与读取

| 项 | 值 |
| --- | --- |
| 工单正文 | `localization/editorial/r9-polish/batch-05-part02/orders/batch-05-part02.reader.md`，共 **1412 行** |
| 结构化数据 | `orders/batch-05-part02.json`（scene_id / row_id / line / controls 同源） |
| 口径文件 | `orders/ORDER.md`（90 行）、`orders/reference-excerpt.md`（66 行） |
| 场景数 | **50 场**（`BossuDex.*` 图鉴 38 个 root，其中 8 个 root 有 2–3 个版本场） |
| 行数 | **419 行**，其中 `current` 为空 **117 行**、非空 **302 行** |
| 读完情况 | reader.md 分 6 段、按 offset/limit 全部读完（1–1412 行，无跳读）；JSON 侧全量程序化复核一遍 |

`current` 为空的 117 行全部是既有合句的尾行，**按 §四.9 一律不报漏译、不填内容**；本路对每一处合句都按整场合计意思核对过完整性，未发现被合句丢掉的英文句子。

## 二、发现总数与分布

**23 条**：A 0 ／ B 10 ／ C 12 ／ needs_evidence 1。

| category | 条数 |
| --- | --- |
| format | 12 |
| term | 6 |
| meaning | 4 |
| source_uncertainty | 1 |

按 root 归组（只列有发现的 21 个 root）：

| root | B | C | needs_evidence |
| --- | --- | --- | --- |
| ClassicBugSpiker | 1 | | |
| ClassicBullfrog | 1 | | |
| ClassicDriller | 2 | | |
| ClassicElf | 2 | | |
| ClassicMineCeiling | 1 | | |
| ClassicSpikeballZero | 1 | 1 | |
| ClassicSpikebot | 1 | | |
| ClassicTentacle | 1 | 1 | |
| ClassicBugFlier | 1 | | |
| ClassicFenfen | 1 | | |
| ClassicGhoster | 1 | | |
| ClassicKobold | 1 | | |
| ClassicMineWall | 1 | | |
| ClassicMineZero | 1 | | |
| ClassicSqueaker | 1 | | |
| ClassicViner | 1 | | |
| ClassicXCannonFloor | 1 | | |
| ClassicXCannonWall | 1 | | |
| ClassicMineWallZero | | | 1 |

其余 **29 场明确记 retain**（含 ClassicBarker、ClassicBigboldEnemy、ClassicBulber、ClassicBumperC×2、ClassicBumperPlus×2、ClassicCannonFloor／FloorC／WallC×2、ClassicDwarfThrower、ClassicFire、ClassicFlybomb、ClassicHopper、ClassicIvyball、ClassicJellyfish、ClassicKobold（短版除点）、ClassicMineWall（除连字符）、ClassicOmegothrower、ClassicOrber、ClassicSpaceHead、ClassicSpiderbot×2、ClassicXeno×2 等）：这些场的意思、口吻、施受关系、条件与页内行数都成立，未为制造改动而重写。

## 三、§四之二 指定超限行的处理结果

| row_id | 原（240px／224px） | 压后（240px／224px） |
| --- | --- | --- |
| `CAT:Od65baabc30d343ed6f34`（ClassicBullfrog） | 4 ／ 4 | **3 ／ 3** |
| `CAT:O829863279bb55814844e`（ClassicSpikebot） | 4 ／ 4 | **3 ／ 3** |

两条都把英文三到四句压回一条物理行（保留合句结构，不增删物理行），只删冗余虚词，条件与能力信息全留：
- 牛蛙行保留「有报道称」（情报来源限定）、「跳跃者」「牛蛙」两个词、喷泡泡与修长舌头伤敌两项能力；
- 刺机器虫行保留「曾用来运送矿井里的矿石和工具」「已被改装」「简陋尖刺」「搜寻入侵者的逻辑」四项。

另有第三行在 224px 下也超 3 行：`CAT:O9df35108fe2d4ae2dd0e`（ClassicSpikebot 男线同句，240px 为 3 行、224px 为 4 行）。它不在 §四之二 的指定名单内，本路**未擅自改动**，仅在此记录：若按 224px 数据簿口径验收，该行需与女线同句一并压缩。

## 四、高风险连续段

1. **Mine／mined／mine 双关段**（ClassicMineCeiling 女线、ClassicMineWall 男线、ClassicMineZero／MineWallZero 四场）
   R5 P08-013 已裁决改成「认主／炸毛」结构。男线已落地；**女线 ClassicMineCeiling 仍留着英文 mine 未译**（`CAT:O2efd47e2bce33a316b21`「都埋了mine」、`CAT:O19a64d3545f4e849130e`「我说的是mine炸了」），是本批唯一残留未译英文实词的对话行，已报 P05b-106。此段风险在于：若把女线的 mine 意译成「矿／地雷」，三重同形双关在中文里必失；若保留英文，则中英混排不可读。本路按已裁决口径补齐 P05b-106，并把争议点在 106 的 note 里写明可由主代理降为 needs_evidence。
2. **无线电套语段**（ClassicBugFlier、ClassicKobold、ClassicGhoster、ClassicSpikebot、ClassicDriller）
   固定式「波苏！我是特工伊吠，请求支援！」／「伊吠通话完毕／通话结束」在本批出现 5 种收尾写法（通话完毕／通话结束／通话完毕！／伊吠通话完毕／伊、伊吠通话结束），其中 `SCf220ad115895cc8e` 用「通话结束」而女线其余场用「通话完毕」。这属于同一角色的套语漂移，但因两版分用不同词、各场内部一致，且属 C 级口吻打磨，本路只在此记录、**未单独立案**（避免凑数）。
3. **问答错位风险段**（ClassicSpikeballZero 的 LITERALLY／FIGURATIVELY 对话）
   下一行的追问依赖上一行是否保留 LITERALLY，现译把 LITERALLY 抹平导致问句无指，已报 P05b-103。
4. **合句断点段**（ClassicMineZero／MineWallZero 六场）
   `YOU CAN EITHER GET NEAR THEM SO THAT THEY DESTRUCT / OR STRIKE THEM TO CAUSE THEM TO EXPLODE. YOUR CHOICE` 三句被并进一条物理行。两版处理不同：sfw 场作「你自己选。」、nsfw 场作「你选吧」（漏句号，已报 P05b-120）。六个同台词场只有这一处漏标点。
5. **ACTUAL_HINTS 占位符段**（ClassicMineWallZero 三场）
   英文把全大写令牌写进台词，三场 current 完全一致。已报 needs_evidence（P05b-123），不擅改。

## 五、男女两版（datadf／datadm）不一致清单

以下为**同 root、同台词、两版中文不同**的对照，均按 §四.10 分别处理，未机械对齐：

| root | 女线（datadf，Yiffany） | 男线（datadm，Yiffai） | 判断 |
| --- | --- | --- | --- |
| ClassicElf | `CAT:Odcf4e4e895a30ca6a957` | `CAT:Oa299621be2e312a2d893` | 同因误译，**各报一条**（P05b-104／105） |
| ClassicElf（sfw） | — | `SFW3ab6eac16bdc3fa6a06204be`「也许全是雌性」 | 此场正确，作为上两条的出处 |
| ClassicDriller | `CAT:O92e…`／`CAT:O4afe…` | `SFW5fe9…`／`SFW96fc…` | 同因术语，**各报一条**（P05b-109／110） |
| ClassicSpiderbot | 「蛛网」「粘胶」「退休」「*看着*吓人」 | 「蛛丝」「黏胶」「退隐」「*看着*吓人」 | 两版内部各自一致，属允许差异，**不立案**；「黏胶」与词典写法更近 |
| ClassicSpikebot | 超限行（P05b-102） | `CAT:O9df35108fe2d4ae2dd0e` 未超 240px | 只改女线，男线记录 |
| ClassicKobold | — | `SFW9d77dbbdc02ceee322e5d387`「 lect 」小写带空格（P05b-112） | 女线无对应行 |
| ClassicKobold（短版） | `SFWf5e2d63876c039cc8f63fe79` 行尾两空格 | 同场 `SFW9d77…` 无尾空格 | 只在 P05b-122 的 note 记录，未另立案 |
| ClassicGhoster | `SFWf25c39e15833ca1e59294c34` 行尾两空格（P05b-122） | 无对应行 | 已立案 |
| ClassicXeno | 「幼体…从你的子宫里破体而出」 | 「后代…直接破开你的子宫钻出来」 | 均贴原文，允许差异 |
| ClassicBumperC | 「装甲似乎比你之前见过的同类更好」 | 「装甲似乎比你见过的其他弹跳机都要好」 | 均成立，允许差异 |
| ClassicCannonWallC／CannonFloorC | 「炮变强了」 | 「加农炮变强了」 | 均成立，允许差异 |
| ClassicMineZero／MineWallZero | 「你自己选。」／「关掉」 | 「你选吧」／「重新停用」 | 标点差异已报 P05b-120 |
| ClassicTentacle／Bulber／Flybomb 等 | 无女线场次 | — | 不存在对照 |

## 六、未覆盖项与不能证明的东西

**未覆盖项**：无。50 场全部 `read_full`，coverage.jsonl 每场一行、无遗漏无重复，419 个 row_id 全部覆盖。

**本工单不能证明的东西**（请勿把这批结论当作已验收）：

1. **行宽只有估算，没有实机证据。** 全部行数是用 `localization/runtime/bbc2-12px.fnt` 的真实字形 xadvance 在 240px／224px 两种框宽下算的，**不是游戏里渲染出来的结果**。字距、行距、换行断点（是否允许在标点前断）都会影响真实行数，无法在工单内证明。
2. **资料卡容器的两种宽度口径没有统一。** 参考摘录与 R7 记录的数据簿是 **224px／最多 3 行**，而 §四之二 的超限判定用的是 **240px**。本路两条压缩行在两种口径下都是 3 行，但 `CAT:O9df35108fe2d4ae2dd0e` 在 224px 下是 4 行；到底以哪个为准，工单内无法确定。
3. **女线 mine 双关该不该保留英文，无法判定。** 见第四节第 1 条；两种做法各有依据（R5 已裁决口径 vs. 原文字面双关），需要主代理对照 R5 决策原文决定。
4. **ACTUAL_HINTS 三处到底是占位符还是故意打破第四面墙的台词**，没有依据可判，故列 needs_evidence 而不改。
5. **未与译文台账 `zh-CN.jsonl` 对照**，也未读任何历史评审产物（`gemini/` 等），故不能断言本批发现与既往轮次无重叠。
6. **术语出处只取到 `datav/dictionary.json` 与同 root／同批正文**。`SPIKEBALL`、`IVYBALL`、`JELLYFISH`、`SPACEHEAD`、`PSY`、`ZENER` 在词典里没有独立条目，因此凡涉及这些名字的写法（如「刺球」「光球」）本路**未提任何改名主张**。
7. **未启动游戏、未修改归档、未改任何构建产物**；除 `ds/findings.jsonl`、`ds/coverage.jsonl`、`ds/summary.md`（及本次生成用的临时脚本 `ds/_build.py`）外未写任何文件。

## 七、字段与结构自检

- `findings.jsonl`：23 条，`finding_id` 从 `P05b-101` 连续到 `P05b-123`，无重复无跳号；每条 12 个字段齐全。
- 所有 `current_quote` 逐字等于 json 里的 `current`（含行首缩进与行尾空格），脚本断言通过。
- 所有 `proposed_zh` 是完整物理行，行首前缀（`  Bossu: [`、`  Yiffai: [`）与原行逐字相同，方括号数量一致，脚本断言通过。
- 所有 `proposed_zh` 在 240px 与 224px 下折行均 ≤ 3；全部字符都在 12px 字库中有码点（无缺字）。
- 已用仓库自带 `localization/editorial/r9-polish/tools/verify_batch.py` 复核：`ds` 路 `problems` 为空（结构、行身份、前缀、标记、宽度增量全部通过）。
- `coverage.jsonl`：50 行，与 50 个 scene_id 一一对应，`row_ids` 覆盖该场全部行；`result` 分布为 issues_found 20 ／ retain 29 ／ needs_evidence 1。
