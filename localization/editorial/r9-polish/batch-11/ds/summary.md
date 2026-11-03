# batch-11 精校小结：战败提示／Starkill／Static 失真广播（1／1）

## 一、输入与覆盖

| 项 | 值 |
| --- | --- |
| 工单正文 | `localization/editorial/r9-polish/batch-11/orders/batch-11.reader.md`（1,887 行） |
| 结构化数据 | `localization/editorial/r9-polish/batch-11/orders/batch-11.json`（109 场／505 ROW） |
| 规范 | `orders/ORDER.md`、`orders/reference-excerpt.md` |
| 场景覆盖 | **109／109 场**，`read_status` 全部 `read_full`（分段读 1–380／381–760／761–1140／1141–1520／1521–1887，每段读后立刻落盘） |
| 行覆盖 | 505 行全部过目；其中 **112 行为 `current` 为空的合句尾行**（按 ORDER §四.9 不报漏译） |
| 场次构成 | `DefeatHints.*` 72 场、`Starkill.*` 21 场、`Static.*` 16 场；45 个 root；`datadf` 55 场／`datadm` 54 场；行级 variant 为 male 198／female 197／sfw 110 |
| 覆盖结果 | `issues_found` 29 场、`retain` 80 场、`partial` 0、`not_read` 0 |

分段无失败段，未出现 `partial`。

## 二、发现总数与分布

**11 条发现**（`P11-D001`～`P11-D011`），全部 `status: proposal`。

| 级别 | 条数 |
| --- | --- |
| A | 0 |
| B | 8（D001／D002／D004／D005／D006／D008／D010／D011） |
| C | 3（D003／D007／D009） |
| needs_evidence | 0 |
| retain（场景级结论） | 80 场 |

按类别：`term` 5（D002 BOLD 残形、D006 干员、D008 小狗、D010 别的干员、D011 伊法）、`idiom` 4（D001、D005、D007、D009）、`relationship` 1（D004）、`format` 1（D003 行尾空格）。

按 root 归组：

| root | 发现 | 判点 |
| --- | --- | --- |
| `DefeatHints.ClassicBigbold.buyfood` | D001（B／idiom） | `SPEAK FOR YOURSELF` 硬译「那只代表你自己」 |
| `DefeatHints.ClassicBigbold.fire` | D002（B／term） | `BOLD` 是 BIGBOLD 残形，中文留英文残形；应为「大壮兽」 |
| `DefeatHints.ClassicBigboldV2.debris` | D003（C／format） | 合句行尾多一个半角空格（代表行，同类共 15 行） |
| `DefeatHints.ClassicStarkillV3.stub` | D004（B／relationship） | 男线 `YOUR SIBLING` 作中性「手足」，与「姐」的镜像称呼不符 |
| `DefeatHints.ClassicWerehund.food` | D005（B／idiom）、D007（C／idiom） | 反事实「本来会…囤好食物」落地不完整；`缺少一身…功夫` 搭配不成立 |
| `DefeatHints.ClassicWerehund.transform` | D006（B／term） | 女线称主角「干员」，违 R2 的 agent＝特工 |
| `DefeatHints.ClassicWerepup.blackmarket` | D008（B／term） | Werepup 在本 root 作「小狗」，同批下蹲两场作「狼崽」 |
| `DefeatHints.Generic.attacking` | D009（C／idiom） | 「别忘了训练所学」名词叠加 |
| `DefeatHints.Generic.gear` | D010（B／term） | 「别的干员」×4 行，应为「别的特工」 |
| `Starkill.AreaC_map04_a` | D011（B／term） | 主角名残留旧译「伊法」，R3 已定「伊吠」 |

同判点的旁及行（写在对应 `note` 里，未另开发现）：D003 另 14 行多余行尾空格；D005 另 1 行（SFW 男线）；D008 另 2 行（小狗崽／小狗）；D011 另 1 行（`嘶咔咔……伊法……伊……`）。

### 行尾空格判据的执行

按指定判据只比对**英文原文行尾**：`occurrence_id → unit_id → localization/catalog/units.jsonl` 的 `source`，无 occurrence 记录时用工单 JSON 的 `source`；**没有**使用 `occurrences.jsonl` 的 `trailing_ws`（该字段是中文列）。

- 中文行尾多空格而英文 source 不以空格结尾：**15 行**（D003 已列全），仅 1 条 C 级发现＋note 清单，不逐行开条目。
- 英文 SFW 版 source 行尾带空格、中文未留空格：6 行（`SFW1caa66…`、`SFWef4aa0…`、`SFW2d0f0a…`、`SFW04ee29…`、`SFWd06f7e…`、`SFW14f597…`）——反向缺失，属镜像体例问题，**不提案**，记此待裁。
- 英文 source 与中文同时带行尾空格的行共 **16 行**（全部是 SFW 条目，如 `L4595`、`L4623`、`L4642`、`L4670`、`L4684`、`L4732`、`L4756`、`L4804`）：镜像成立，不报。

## 三、高风险连续段

1. **合句断点（最多）**：本批 `112／505` 行是空的合句尾行，3 行英文并成 1 行中文的场次集中在 `ClassicBigboldV2.debris`（L4789 三行并一）、`ClassicEnelye.stub`（L4879／L4883）、`ClassicWerepup.blackmarket`／`puppy`、`Generic.gear`（L4941／L4954 三行并一）、`ClassicWerehund.food`、`Starkill.Area0_map35_a`。逐场核对合句后语义完整、无硬粘病句；**唯一例外**是「我本来会…先囤好食物！」（D005）与「缺少一身…功夫」（D007）——两者都是合句处把英文从句直接拼接导致搭配断裂，也是本批 C 级判点的来源。
2. **问答／说话人错位**：逐行核对 speaker（Mauser／Tomcat／Bossu／Starkill／Yiffai／Yiffany），**未发现**说话人挂错或问答错位；`Static` 16 场确实无说话人（`Static:` 前缀为条目名而非角色），不作人物处理。
3. **无线电套语**：`COME IN, X` 与 `HELLO? IS SOMEONE THERE?`、`CAN YOU STILL HEAR US?`、`HQ, DID YOU MANAGE…`、`THERE'S NO RECEPTION` 这些套语各场译法不同但都成立（「收到请回答」「请回话」「还能听见我们说话吗」「怎么又没信号了」），**只发现**两处术语回退（D006、D010 的「干员」），未发现套语错义。
4. **失真广播**：`Starkill` 21 场、`Static` 16 场按 ORDER §四.13 只查单行可指认错误——未发现整句漏译、施受反转、人物挂错；发现 1 处旧译名残留（D011）。噪声整行保留的场（`Static` 16 场中除 4 场 MIS 版外）与噪声部分汉化的场并存，属未终裁体例，未统一。

## 四、男女两版不一致清单

| 判点 | 男线（`datadm`） | 女线（`datadf`） | 处理 |
| --- | --- | --- | --- |
| `YOUR SIBLING HOW TO FIGHT` | L4797「让你的**手足**看看怎么战斗」 | L4785「让你**弟弟**见识见识你的身手！」 | **D004**：男线改「姐姐」（同批 L2133 伊吠原话「拜托，姐」为据）；女线「弟弟」正确不动 |
| `AGENT, DON'T FORGET TO OBSERVE` | L4866「**特工**，别忘了观察你的对手。」 | L4854「**干员**，别忘了观察你的对手。」 | **D006**：女线改回「特工」 |
| `OTHER AGENTS LOST GEAR` | L4949／L4802「别的**干员**」 | L4936／L4754「别的**干员**」 | **D010**：四行统一改「特工」（并非仅一侧错，属整批回退） |
| `I WOULD'VE STOCKED UP ON FOOD` | L4877／L4730「我本来会…先囤好食物！」 | L4864「换作是我…肯定先备足吃的！」／L4682「我本该先囤点食物的！」 | **D005**：只改男线两句；女线两种措辞都成立，不强求统一 |
| `AGENT, DON'T FORGET YOUR TRAINING.` | L4924「别忘了训练所学。」 | L4918「别忘了你受过的训练。」 | **D009**：只改男线搭配，不照抄女线 |
| `KEEP AT IT` 类鼓劲语 | L4838「挺棘手的，是吧？」 | L4825「挺棘手的，对吧？」 | 两版语气词不同，均成立，保留 |
| 狼崽称呼 | 黑市场「小狗」／下蹲场「狼崽」 | 同 | **D008**：跨版全 root 统一「狼崽」 |
| 失真噪声处理 | L2132 把 `MEET` 段处理成「嘶kkkk喀」、把 `BROTHER` 译出「兄rrr弟」 | L2130 保留 `SHSKKKRK见面`、`SHHHZZZTER` 原形 | 失真体例未终裁，**不报**，列此待核 |
| 名字残形 | L2533「伊法……伊……」 | L2513「伊FFFHS妮」（用对「妮」） | **D011**：男线／双方共 3 行统一「伊吠」；女线 `妮` 正确不动 |

## 五、不提案项与待核项（口径说明）

- **代词 他／它**：同一 boss 在不同 root 分别作「他」（L4745「他什么时候要喷火」、L4768「他现在打得更疼了」）与「它」（L4791「得提防它的跳跃」、L4789「它造成的伤害…」）。无裁决可依，本批不统一，不提案（已在 D002 note 注明本发现只处理 BOLD 残形）。
- **P.A.W. ／ NAVIGATE 菜单名**：`Generic.map` 两场保留英文，与 `zh-CN.jsonl` 台账「NAVIGATE 照录原文（表外暂译待裁定）」一致，属待裁项，不提案。
- **FENFEN／FEN 写法**（`Starkill.AreaBTube1_a`「找到 芬....芬」、`[需要FE……FEN……]`）：FENFEN 中文名未终裁，不提案；行内多余半角空格属失真装置，不当作排版错误。
- **失真噪声体例**（`KKZZT`／`ZZK`／`KKKKK- ZZT!` 保留 vs `咔滋滋！特……嘶嘶……失……误……` 汉化）：全库未终裁，本批不统一、不报。
- **`听着，家伙`（BUSTER）**：`Starkill.AreaC_map06_a` 女线 nsfw 场的称呼语偏译文腔，但不在 ORDER §四.13 允许的四类失真错误内，按「不把失真广播修通顺」保留。
- **`继续练下去就行了`（JUST KEEP AT IT）**：比原文多出「练」义，鼓励语仍成立，保留。
- **「恶——」（EEEYUCK）／「唔……」（GRR）** 一类拟声与语气词：不统一，不报。
- **行宽**：D003／D011 的正文超过 20 全角字，但两处都是**行宽不变**（D003 只删行尾空格；D011 只换一个字），已在 note 写「行宽待实测」。

## 六、未覆盖项与「本工单不能证明的东西」

- **未覆盖**：无。109 场全部 `read_full`，无 `partial`、无 `not_read`，无 `needs_evidence` 条目。
- **本工单不能证明**：
  1. 未做任何渲染／实机核验——`行宽待实测` 的行在 240px／12px 剧情框里是否仍不超过 3 行折行，本次未测；D003、D011 两行按「行宽不变」处理，但折行结果未验证。
  2. 未写入任何台账、归档或译文库，未跑构建与 17 步回归；提案能否被 `editorial_repairs.py` 精确匹配（旧值唯一性、整资源 SHA 漂移）未验证。
  3. `proposed_zh` 依据的是本批 `current`（candidate13 基线快照）；若合并顺序变化，旧值可能漂移，届时需重新定位。
  4. 失真字幕体例（噪声保留量、`SHHHZZZTER` 类亲属残形是否该译）全库未终裁，本批**不构成**对该体例的任何结论；男女两版噪声处理差异只记录、不值裁。
  5. 本批未核 SPA/媒体、未核 `Static` 场景的触发条件（`override`／`noselect`／`noamendfreq` 一律视为脚本条件，未验证其语义）。
  6. LIGHTTAZER、FENFEN 中文名、引号体例、CJK 与拉丁间距、`Traeh`／`Sevaw`／`Erauqs` 现状——均按未终裁／不动处理，本批未给任何意见。
  7. D008 若裁决认为「小狗」的弱化是英语 PUPPY 笑话所必需，则该发现应降级为 retain；本批只提供术语一致性与同批对照证据，最终取舍不在本工单能力范围内。

## 七、产出文件

- `localization/editorial/r9-polish/batch-11/ds/findings.jsonl`（11 行）
- `localization/editorial/r9-polish/batch-11/ds/coverage.jsonl`（109 行，scene_id 唯一、row_ids 与工单 JSON 逐场一致）
- `localization/editorial/r9-polish/batch-11/ds/summary.md`（本文件）
