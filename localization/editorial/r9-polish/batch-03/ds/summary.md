# batch-03 精校总结（ds 路）

## 一、输入与实际读完范围

| 项 | 值 |
| --- | --- |
| 工单 | `localization/editorial/r9-polish/batch-03/orders/ORDER.md`（82 行，全读） |
| 工单正文 | `localization/editorial/r9-polish/batch-03/orders/batch-03.reader.md`（1478 行） |
| 结构化同源 | `localization/editorial/r9-polish/batch-03/orders/batch-03.json`（5248 行，按需精确取 row_id／line／source／current） |
| 参照摘录 | `localization/editorial/r9-polish/batch-03/orders/reference-excerpt.md`（91 行，全读） |
| 方法口径 | `localization/editorial/r1/TRANSLATION_PLAN.md` 第五、七节 |
| 人物参照 | `localization/editorial/r1/reference/characters-support.md` 的 Bossu 段（定点） |

**reader.md 用 offset/limit 分 9 段读完全部 1478 行，未截断。** 53 场、437 个 ROW 全部读到；`coverage.jsonl` 逐场列出本场全部 row_id，合计 437，与工单一致。未读 `batch-01/`、`batch-02/`、任何 `review/` 目录的裁决内容（仅用 `localization/translations/character-names.json`、`glossary.csv`、`zh-CN.jsonl` 做术语与既有译法核对，这些不是本批裁决）。

`current` 为空的 ROW 一律按合句尾行处理：不报漏译、不提案填充。涉及空行承接的发现（P03-004、P03-017、P03-030、P03-034）已在 `note` 写明两行合看与分配建议。

## 二、发现分布

**38 条**：A 5 / B 29 / C 3 / needs_evidence 1。

按 root 归组（本批 root 均为 `Bossu.*`，按场景职能再分）：

| 场景职能 | 场数 | 发现 | 判点 |
| --- | --- | --- | --- |
| StarkillHint（报讯—姐姐/弟弟定位） | 3 | P03-025、P03-038 | 标点空格残留；原文 `I'VE WAS` 破损记为来源不确定 |
| map10（数据采集要求＋收尾） | 4 | P03-012、P03-013、P03-014、P03-015、P03-035 | HOLD/劲头承接、GOOD BOY、GEEZE、OVER AND OUT、LECT 排法 |
| map18（护腕滑行） | 4 | 无（全 retain） | 提示两行与操作句正确，`DOWN`／`JUMP` 原样 |
| map26（救特工＋DATA VIEW＋P.A.W.） | 4 | P03-003、P03-008、P03-009、P03-017 | 单数 THEY、干员/特工、人名空格、BODES 断行 |
| map68_b（过度探索） | 2 | P03-026 | 句末标点缺失 |
| AreaBTransportal2（传送门规程） | 3 | P03-016、P03-029、P03-030、P03-031 | OUT 套语、SOLID SURFACE、同义堆叠、NOT ONLY THAT |
| AreaE_map26（黑暗能量警示） | 2 | P03-004、P03-005 | OVERTAKEN 语义、SIBLING 称谓 |
| AreaH_map01（机库休息区） | 2 | P03-027 | AUTOPILOT 设定句主谓错位；克制挖苦已正确保留 |
| CapturedPet（观测单元/动物魔法） | 4 | P03-018、P03-019、P03-020、P03-037 | 观测单元/装置、FAUNA MAGIC、REWARD AS THANKS、表扬句语序 |
| Feral / FeralPickup | 4 | P03-007、P03-024 | 规章句三种写法、WHO IS THIS 四种译法 |
| Kobo / KoboPickup | 6 | P03-002、P03-022、P03-023、P03-034 | 单数 THEIR、套鳞装、装束、tiny puppy 让步调序 |
| GenderSwapped(+Pickup) | 4 | P03-001、P03-027(P03-036) | OUT 译成离场动作、HUH 惊叹词跨线不一 |
| Slime / SlimePickup | 4 | P03-021、P03-006 | GOOP/GLOOP 撞词、RADIO 术语回退 |
| NoteFrequency | 2 | 无（retain） | 两线措辞属版本差异 |
| TestA | 2 | 无（retain） | 占位测试句无问题 |
| TransitionAreaEAirlock1 | 3 | P03-028 | BELONGS TO 被改成位置关系 |

## 三、高风险连续段

1. **AreaBTransportal2 传送门拒绝段**（三场）。这是本批规程面与风险面最密集的一段：`NEGATIVE`→「不批准」正确，`NAP-OF-THE-EARTH RE- STRICTIONS` 断词没有被译成结巴或拉长音（正确），`RI- SK` 同样处理正确。风险在**跨行分配**：男线 NSFW 把「不过，你的飞船已经顺利抵达你的位置，没有受到袭扰」整句塞进 `NEGATIVE…` 那一行，而 SLIME 关的 `HOWEVER, YOUR SHIP HAS NAVIGATED TO YOU UNMOLESTED` 是独立的下一物理行（`CAT:Obf14fb92146b87ed170e`，空行）；`NOT ONLY THAT…` 三行（`O428120c`／`Od404e7f`／`O047f344`）只剩首行有字。男线 SFW 更极端：三行合一。三场落库前必须按行重分配，否则第二行永远是空的。本次提案只动首行文本，分配建议写在 note。

2. **Feral／Slime 盘问—规章—挂断链**（4 场 × 7 行）。同一规章句四种写法、同一盘问句四种写法，且这两句恰好是全批唯一「对面只会汪汪/咕叽，Bossu 仍按规章公事公办」的笑点所在。P03-007 与 P03-024 必须先定死再动其它文字，否则四处会继续分叉。

3. **Kobo 男线 `SCc27e8f58c8e9a99d` 的四行合句**（`Oc8bd53`／`O90bf06`／`O86b63b`／`O1cf2d2`）。原文 `THAT BOY MAY NOT HAVE PUT UP MUCH OF A FIGHT / AS MINISCULE AND WEAK FRAMED AS HE IS / BUT JUST WAIT… / AND THEN YOU'LL REGRET…` 全压在首行，后三行全空。这是本批最容易被误判为「三行漏译」的位置——它们不是漏译，是既有合句尾行。

4. **CapturedPet 男线 `SCa245cbaf6436d18f` 的荤梗落点**（`Oc6b77402`「…得用上你的——」→ `O4be9a09`「喂、喂！…」）。Tomcat 的半句被打断后由主角抢白，是「损友式支援」与「Bossu 立刻拉回救援任务」三面同框的一段，不能为了通顺把 Tomcat 那半句补完。

5. **map10 四场的无线电收尾**。`OVER!`（Bossu）／`OVER AND OUT`（Yiffany）／`OUT!`（Yiffai）三种报尾在本批出现五套译法，是全批最系统性的口径问题（P03-015、P03-016）。

## 四、男女两版不一致清单

| 项 | 男线 row_id | 女线 row_id | 差异 | 处置 |
| --- | --- | --- | --- | --- |
| RADIO | `CAT:O91d8541235ea4f1a020b`（无线电） | `CAT:O633dd30d9d8ac4dd23cf`（通讯器） | 术语回退 | P03-006 |
| RADIO | `CAT:Ob5895441a3e28c0fc4d9`（无线电） | `CAT:Oa5cf4f42568296c05e07`（通讯器） | 同上 | P03-006 |
| 规章句 | `CAT:Ob1f70f52ae86474ae5c2`／`CAT:O0c07dadcb3188edea015` | `CAT:Oe1a023ea3f4c5e26556c`／`CAT:Occ34d2fa6f13b899dd40` | 三／四种写法 | P03-007 |
| WHO IS THIS | `CAT:O48071ad927899a84a1e7`（你是谁？） | `CAT:O5e6ecefda5125c3d1b0d`（这是谁？） | 两种译法 | P03-024 |
| SCALE SUIT | `CAT:O573acfd2fb9dc344c1f9`（鳞片套装） | `SFW51cc855dfa95eb9439729918`（套鳞装） | 生造词 | P03-022 |
| OBSERVATION UNITS | `CAT:O80597cd2a53f4fa2a5cc`（观测装置） | `CAT:Oda2c444361d4ffdf92f8`（观测单元） | 术语二选 | P03-018 |
| GOOD BOY | `CAT:Oa6d11b8a0dc25131cbc4`（好小子） | — | 男线内部 NSFW `CAT:Ob31…` 处 `SFW179934b1d5a42a73a1099914` 译「乖，」 | P03-013 |
| GEEZE | `SFW815bf41357d8a0501b11f43b`（哎呀） | — | 男线内部 NSFW `CAT:Ob31df43cd88f8778dff1` 漏语气词 | P03-014 |
| HOLD YOUR OWN | `SFW89aa149fad8028feb7a3b6b9` | `SFW2a885f9873e302d6b290f59b` | 两线同错 | P03-010 |
| OVERTAKEN | 男线 `CAT:Oeffd8246732a55809cc2`（吞噬） | `CAT:O8ed5328423c2d0e56b38`（控制） | 语义分叉 | P03-004 |
| OUT! | `CAT:Of0aa61857047c59585d7`（结束通话） | `CAT:O20555292d580fdb20496`（行——！…结束通话） | 套语不一 | P03-016 |
| OVER AND OUT | — | `CAT:O31052ad862684434c0fe`／`SFW6a5d562adaa4c8f78930364c` | 两场同文一致，但与 OVER 口径不一 | P03-015 |
| HUH?! | `CAT:O688d2472506d66853ba0`（哈？！） | `CAT:O9a5e5c5b93cc37f246ed`（呃？！） | 同角色两惊叹词 | P03-036 |
| 单数 THEY | NSFW 女线 `CAT:Oebc81acbc6616c0c1f95`（对方） | SFW 女线 `SFWea0b5d5779c09240002d7613`（他们） | 女线内部 NSFW/SFW 不一致 | P03-003 |
| SOME OF THE FAUNA | `CAT:O3c87dfed23594e1c16d0`（不少） | `CAT:O96a7314bc333c954f54c`（无） | 女线 NSFW 丢 SOME OF | P03-037 |
| BELONGS TO | `CAT:Oc1b58dc3bb8dfca993ec`（属于） | `SFW041a290cd3f66966eb7b0d8f`（就在…上） | 女线 SFW 改归属为位置 | P03-028 |
| SIBLING 称谓 | `CAT:O24cd6378b36499ce88d2`（手足） | `CAT:O8ed5328423c2d0e56b38`（弟弟） | 男线比女线含糊 | P03-005 |

**版本差异但保留、不属不一致**（原文本身不同）：SFW 女线 `SFW6c31580a` 用 `THESE THINGS HAPPEN` 而 NSFW 女线 `CAT:O5335e786` 用 `COME OOOOON SQUEAKS`；KoboPickup 男线 SFW `SFW51cc855` 原文无 `LIKE TOMCAT HAS?` 从句；NoteFrequency 两线措辞不同；GenderSwapped 女线原文是 `I'LL CALL YOU LATER`。

## 五、待核项（needs_evidence）

- **P03-038** `SC7979a606b9be0aad` / `CAT:O6144a9b1f8bc4b06dd88`：原文 `[I'VE WAS THAT CLOSE ALL THIS TIME... DAMN!]` 语法破损（疑为 `I'VE BEEN` 或 `I WAS` 的残留）。现译「我一直就离得那么近」意思正确，**不需要改**，只登记来源缺陷，防止后续轮次把它当译错回改，或据破损英文重写。同文 `SFW9d95d939ba850233fcf8cb13` 一并。

其余来源无自相矛盾、说话人不明或触发条件存疑之处。

## 六、未覆盖项与本工单不能证明的东西

1. **未做实证验证**：全部提案的宽度均已用 `localization/editorial/r9-polish/tools/measure_width.py` 同一套 12px 字形表（`bbc2-12px.fnt` + `bbc2-cjk-12.png`，240px 框）实测，无一条由 ≤3 行变 >3 行；但**没有**回填构建、没有跑 17 步回归、没有进游戏看实际分页与换行位置。折行数一致不等于视觉观感一致。
2. **未裁决跨行分配**：P03-004、P03-017、P03-030、P03-034 都涉及「合句内容当前全压在首行、后续行是空尾行」的结构问题。按 ORDER 第四节第 3 条，`proposed_zh` 只给本行文本，重分配方案只在 `note` 说明。**这些场的正确落库需要同时决定空行的归属**，本路无权也不应在提案里改动空行。
3. **术语终裁权不在本路**：「无线电／通讯器」（P03-006）、「特工／干员」（P03-008）、「观测单元／观测装置」（P03-018）、「鳞片套装」（P03-022/P03-023）、无线电报尾（P03-015/P03-016）五项都需要与 batch-01／batch-02 及 R6 的术语裁决合并后才能定稿。本路的判断依据是「本批 59 处特工 vs 4 处干员」「本批 8 处无线电 vs 2 处通讯器」这类批内一致性统计，**不构成对全局术语的裁决**。
4. **未读的资源**：本批只覆盖 `Bossu.*` 53 场。Bossu 在同一批归档里的其它称呼行（`sir`／`BOSS` 向、`EVAL.` 对 Tomcat 的指令链）不在本工单内，未核。Bossu 的物种、外貌、军阶按参照摘录的边界一律不推断——本路也没有从本批任何一行得出这些信息。
5. **不能证明的**：本路未访问游戏运行时，不能证明「按提案落库后玩家实际读到的是同一段话」；不能证明提案不改变任何触发条件（只逐字核对了 CONTROL 行未动）；不能证明 12px 字体对个别生僻字形的覆盖。
6. **C 类克制**：只报 3 条（P03-034、P03-035、P03-036），均是能指出明确更优理由的（让步结构、拉丁词排法、同角色惊叹词统一）。其余可打磨处（如「哎呀，就在你坠机着陆处的西边！」的 WHY 处理、「为了讨生活，有些人什么事都肯干，是吧？」的轻讽）意思与口吻都成立，按 ORDER 第三节末段的 retain 原则保留，不凑数。

## 七、retain 场次（12 场）

`SC108f8f86a462d740`、`SC4a6ba978bc909729`、`SC71c62457d7d39c80`、`SC0ba29e6323e29812`、`SC58cedb6914563db9`、`SC0a80dd8da7ba8e4d`、`SC85dc739f512caaad`、`SC1b987e6b0d3545db`、`SCbdc1360a67a4fb61`、`SCdf5a9a050d25e69b`、`SC15b44576c56cffa3`、`SCad10f274abd694b4`。

其中 `SC0ba29e6323e29812`（KoboPickup 男线）是本批最重要的一段：Bossu 察觉是套装后主动删记录，四行台词语义、语气、克制幽默全部成立，明确 retain；`SC1b987e6b0d3545db` 与 `SC71c62457d7d39c80` 保留的理由是它们恰好是「lighttazer 被偷」「cute tail」两条例外与「笨手笨脚的弟弟」刻薄评语的落点，改动会伤到人物多面性。
