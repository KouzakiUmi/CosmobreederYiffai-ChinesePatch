# batch-08-part05 审校报告（Gemini 路）

## 一、审校概况与覆盖

- **输入工单**：
  - `localization/editorial/r9-polish/batch-08-part05/orders/batch-08-part05.reader.md`（共 1,704 物理行）
  - `localization/editorial/r9-polish/batch-08-part05/orders/batch-08-part05.json`（共 16 场场景，449 行 ROW）
- **审校执行**：按 200 行分段读取推进，全批 16 场、449 行 ROW 100% 完整审校（`read_status: read_full`），无截断、无遗漏。
- **产出文件**：
  - `localization/editorial/r9-polish/batch-08-part05/gemini/findings.jsonl`（5 条发现，编号 `P08-0501`～`P08-0505`）
  - `localization/editorial/r9-polish/batch-08-part05/gemini/coverage.jsonl`（16 场记录，每场列全 `row_ids`）
  - `localization/editorial/r9-polish/batch-08-part05/gemini/summary.md`（本报告）

---

## 二、发现统计与分布

### 1. 分级统计

| 分级 | 数量 | 占比 | 说明 |
| :--- | :---: | :---: | :--- |
| **A** | 1 | 20.0% | `P08-0502`（残留未译英文种族名 Elves） |
| **B** | 4 | 80.0% | 术语不一致、场内前后译名冲突及装备未译实词（council / Cosmohelm / Cosmosuit） |
| **C** | 0 | 0.0% | 无单纯润色凑数项 |
| **needs_evidence** | 0 | 0.0% | 无原作者逻辑存疑项 |
| **合计** | **5** | **100.0%** | |

### 2. 发现清单与归组

1. **场景**：`SC9f1bb2ff4b29b7d6` (`vsn/f_AgentFZ1/script.vsn`)
   - **finding_id**：`P08-0501`
   - **row_ids**：`["SFW25bf347341e6feb42c079492"]` (L23)
   - **severity**：`B` / **category**：`term`
   - **原文**：`All major quarrels were sorted out by a council of the wisest ESPers we had.`
   - **当前行**：`lang(Fox): 所有重大纷争，都由我们中最睿智的超能力者所组成的理事会来化解。`
   - **提案行**：`lang(Fox): 所有重大纷争，都由我们中最睿智的超能力者所组成的议会来化解。`
   - **依据**：council 依前序批次及库内统一术语裁决应作“议会”（参考 orders/reference-excerpt.md 及已知库内事实），不作“理事会”。且同场后文（L38、L48）均使用“议会”，同场内前后产生不一致。

2. **场景**：`SC9e9ceda84c287300` (`vsn/f_AgentFZ3/script.vsn`)
   - **finding_id**：`P08-0502`
   - **row_ids**：`["CAT:O3097f924a69022f9c990"]` (L37)
   - **severity**：`A` / **category**：`term`
   - **原文**：`Some, like the noble Elves, took up ancient weapons in order to aid us Fenfen...`
   - **当前行**：`lang(Fox): 其中一些，比如高贵的Elves，拿起了古老的武器来援助我们Fenfen……`
   - **提案行**：`lang(Fox): 其中一些，比如高贵的精灵，拿起了古老的武器来援助我们Fenfen……`
   - **依据**：Elves 为残留未译英文实词。全库统称“精灵”（如 datadf/all.ds:2472“精灵女王恩莉耶”、vsn/m_ClassicEnelye:11“图托恩精灵的不朽至高女领主”、男线同型对白 vsn/m_AgentMZ3:37“有些如高贵的精灵”）。

3. **场景**：`SCf793f8e2f2b5b70f` (`vsn/f_AgentFZ4/script.vsn`)
   - **finding_id**：`P08-0503`
   - **row_ids**：`["SFW3840c04d50de9a060aa17ace"]` (L37)
   - **severity**：`B` / **category**：`continuity`
   - **原文**：`fleeing from the powers of the Fenfen council.`
   - **当前行**：`lang(Fox): 纷纷逃离Fenfen理事会的力量。`
   - **提案行**：`lang(Fox): 纷纷逃离Fenfen议会的力量。`
   - **依据**：同一场内 L18 已将 Fenfen council 译为“Fenfen 核心成员所在议会”，且依据统一术语（参考 orders/reference-excerpt.md 及已知库内事实），council 应统一为“议会”，同场内前后译名不一致（“议会”与“理事会”混用）。

4. **场景**：`SCe68f2e03acd6f17b` (`vsn/m_ClassicSqueakerBoss/script.vsn`)
   - **finding_id**：`P08-0504`
   - **row_ids**：`["CAT:O670c59a52e7d88ed0538"]` (L19)
   - **severity**：`B` / **category**：`term`
   - **原文**：`It's my Cosmohelm! It got all the way over here somehow!`
   - **当前行**：`text: 是我的Cosmohelm！它不知怎么一路跑到这边来了！`
   - **提案行**：`text: 是我的宇宙头盔！它不知怎么一路跑到这边来了！`
   - **依据**：Cosmohelm 为残留未译英文实词；依据已知库内既定事实及 datav/dictionary.json#CosmoHead.desc、datadm/all.ds:4157，该装备统一定名为“宇宙头盔”。

5. **场景**：`SCe68f2e03acd6f17b` (`vsn/m_ClassicSqueakerBoss/script.vsn`)
   - **finding_id**：`P08-0505`
   - **row_ids**：`["CAT:Oaea9196d5c151cdad1dd"]` (L21)
   - **severity**：`B` / **category**：`term`
   - **原文**：`Just need to keep an eye out for the Cosmosuit portion...`
   - **当前行**：`text: 只要再留心Cosmosuit那一部分就好...`
   - **提案行**：`text: 只要再留心宇宙服那一部分就好……`
   - **依据**：Cosmosuit 为残留未译英文实词；依据 datav/dictionary.json#SpecialZentaiSuit.name（UI 条目 Ub29a9dd5c0e2a77d7bea）及全库统一既有译名（如 datadf/all.ds:2528、datadm/all.ds:4163），该装备统称为“宇宙服”；行末半角三点改用全角省略号规范标点。

---

## 三、判定保留（retain）的场次清单（12 场）

除上述 4 场出现需要修正的缺陷外，其余 12 场全部判定保留（`result: retain`）：

1. **`SC409ec23e7cec48f7`** (`vsn/ClassicPreTitle/script.vsn`, 8 rows, sfw)：经典序章背景介绍。超光速航行、赛博机器人、[3P组织]、[宇宙育种者]等专名方括号保留完好，语言庄重大气，判定保留。
2. **`SC4d550b4a736dbb6d`** (`vsn/f_AgentF04/script.vsn`, 39 rows, nsfw)：浣熊女特工牢房自述。肉结（knot）、双足飞龙（Wyverns）、嘴瓢（hunky iron -> hunk of iron）传神到位，合句完整，判定保留。
3. **`SC8559b2a4c2d88fb3`** (`vsn/f_AgentF05/script.vsn`, 44 rows, nsfw)：水獭妹特工（Erma）自述。少女娇憨口吻与触手牢房高潮自述连贯自然，合句完整，判定保留。
4. **`SC960d377d64349226`** (`vsn/f_AgentF06/script.vsn`, 56 rows, nsfw)：狐狸特工（Daleir）自述。与水獭搭档互为因果的反差自白，语调俏皮，判定保留。
5. **`SC5aaca5284184e89a`** (`vsn/f_AgentFZ2/script.vsn`, 22 rows, sfw)：Fenfen 灵能记忆场景2（女线）。保留女线规范“让心神向内”，Traeh 与图托恩（Tutone）符合词典规范，判定保留。
6. **`SCde64a3347a222a67`** (`vsn/f_AgentFZ5/script.vsn`, 19 rows, sfw)：Fenfen 灵能记忆场景5（女线）。流星坠落与星际闯入者被 Traeh 腐化的悲壮历史，判定保留。
7. **`SCf72bb408100fe80c`** (`vsn/f_ClassicStarkillV3/script.vsn`, 18 rows, nsfw)：女线星杀 Boss 战。弟弟 Yiffai 被暗黑女王控制后唤醒，姐姐与弟弟的羁绊、爸爸的旧哨子伏笔温情贴切，判定保留。
8. **`SCf1e352091c207f10`** (`vsn/m_AgentM04/script.vsn`, 50 rows, nsfw)：壮汉特工自述。死要面子、自夸与男婊子、乖孩子双关心理反差生动传神，判定保留。
9. **`SCba223e0dcbb46a0c`** (`vsn/m_AgentM06/script.vsn`, 53 rows, nsfw)：小熊猫特工自述。假装胜者受精灵服侍到最后发现被困牢房的幽默剧情，口吻鲜明，判定保留。
10. **`SCe240b1877125bd63`** (`vsn/m_AgentMZ4/script.vsn`, 23 rows, sfw)：Fenfen 灵能记忆场景4（男线）。保留男线规范“将心神转向内在”，议会术语一致，判定保留。
11. **`SCcba1968e6380c012`** (`vsn/m_ClassicBossRedbull/script.vsn`, 20 rows, sfw)：男线经典 Boss 红牛战。打架装酷被瞬间打脸的喜剧节奏与双关语还原精准，判定保留。
12. **`SC9ac2eccd1d8bd48f`** (`vsn/m_ClassicPigobinV3/script.vsn`, 16 rows, nsfw)：猪哥布林古风（HardFox）对白。“汝”、“吾”、“尔”的半文言与主角现代口语形成强烈戏剧张力，判定保留。

---

## 四、高风险连续段核验

1. **合句与空行断点**：
   本批包含多处既有合句（如两条至四条英文合并为一条完整中文）。经逐行核对，所有 `ZH:` 为空的行均为既有合句尾行，整句意思完整无遗漏，未破坏句子结构或信息揭示顺序。
2. **成人向自述与角色口吻**：
   特工自述（AgentF/AgentM）保持各自特工的鲜明口吻（浣熊大条、水獭娇憨、狐狸腹黑、壮汉死要面子、小熊猫傲娇自大），成人向内容（肉结 knot、带棱鸡巴、触手高潮等）严格按照原文尺度表达，既未弱化亦未恶意加码。
3. **保护标记与既定术语保留**：
   全场所有 `<3`、`Traeh`、`Fenfen`、`UP+ATTACK` 等保护标记原样保留无损坏；`KOBOLD＝科博德`、`Cosmohelm＝宇宙头盔`、`knot＝肉结`、`feral＝野兽` 等既定库内事实均严格执行。

---

## 五、男女两版的不一致清单

1. **Fenfen 灵能记忆开场白（Turn your mind inward）**：
   - **女线（`SC9f1bb2ff4b29b7d6` 等）**：`让心神向内，去见证塑造这片土地的那些往事……`
   - **男线（`SCe240b1877125bd63` 等）**：`将心神转向内在，见证塑造这片土地的往事……`
   - **判定**：已知库内事实，男女两版各自内部高度统一，判定各自保留，禁止机械拉平。
2. **Fenfen council 议会译名对照**：
   - **女线 `SCf793f8e2f2b5b70f` L37**：曾误译为 `Fenfen理事会`；
   - **男线同型场景 `SCe240b1877125bd63` L37**：正确译为 `Fenfen议会`。
   - **判定**：本次通过 `P08-0503` 将女线修正为“Fenfen议会”，消除了跨版本译名不一致。
3. **Elves 精灵译名对照**：
   - **女线 `SC9e9ceda84c287300` L37**：残留未译 `Elves`；
   - **男线同型场景 `vsn/m_AgentMZ3:37`**：正确译为 `高贵的精灵`。
   - **判定**：本次通过 `P08-0502` 补译为“精灵”，与男线及全库统一步调。

---

## 六、未覆盖项与本工单不能证明的事项

1. **实际字宽折行渲染**：
   本批剧情框规格为 240px、12px 字体，每页最多 3 行（约 20 全角字/行）。虽然全部译文行长均处于安全范围，但特定带有长标点或缩写（如“宇宙头盔”、“宇宙服”）在游戏引擎实际运行时的断行与文本框底边表现，仍需以实机渲染回归为准。
2. **全局引号体例**：
   游戏文本中全角双引号 `“”` 与直角引号 `「」` 的混用属于全局待裁规范，本工单严格遵循“不报引号体例”约束，未作变动。
