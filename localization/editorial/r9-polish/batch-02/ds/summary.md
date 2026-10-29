# batch-02 精校小结（ds 路）

## 一、输入与阅读范围

| 项 | 值 |
| --- | --- |
| 工单正文 | `localization/editorial/r9-polish/batch-02/orders/batch-02.reader.md`，1873 行 |
| 结构化数据 | `localization/editorial/r9-polish/batch-02/orders/batch-02.json`，6581 行、56 场、566 ROW |
| 执行规范 | `orders/ORDER.md`（82 行）、`orders/reference-excerpt.md`（90 行） |
| 实际读完场景 | **56 / 56**，无截断；reader.md 用 offset/limit 分 12 段读到 1873 行末 |
| 覆盖行 | coverage.jsonl 56 行，每行 `read_status=read_full`，`row_ids` 与 json 逐场一致（脚本校验通过） |
| 基线 | candidate13 显示行；未读 `batch-01/`、`batch-03/`、任何 `review/`，未参考另一路产物 |

`current` 为空的 118 个 ROW 全部按「既有合句尾行」处理：未报漏译、未提任何填充提案。

## 二、发现总数与分布

**71 条**（`P02-001` … `P02-071`），每条一个判点、一条可落库的完整物理行。

| 分级 | 数量 | 说明 |
| --- | --- | --- |
| A | 5 | 3 条容器超限（合句后 4 折行）+ 2 条无线电结束语误义 |
| B | 62 | 术语口径、称呼漂移、语用/衔接、笑点、口吻 |
| C | 2 | 只报有明确更优理由的两条（语气节奏、斜杠强调分寸） |
| needs_evidence | 2 | LIGHTTAZER 三口径冲突、失真段处理分歧 |

按 category：`term` 32、`voice` 15、`continuity` 8、`format` 6、`meaning` 5、`idiom` 4、`source_uncertainty` 1。

**按版本**：男线（datadm / SFW 男）41 条，女线（datadf / SFW 女）30 条。两边分别判断，未把任何一句措辞机械移植到另一线；71 条中有 40 条存在「另一线同源行」，均按各自语境单独措辞，只在 `note` 里指出同型位置。

**按 root 归组**（findings 落在该 root 的行上）：

| 条数 | root |
| --- | --- |
| 14 | `Tomcat.AreaC_map64_b` |
| 9 | `Tomcat.AreaH_map02_a` |
| 7 | `Tomcat.AreaA_map42_a` |
| 7 | `Tomcat.AreaC_map56_a` |
| 6 | `Tomcat.KoboPickup` |
| 5 | `Tomcat.Area0_First_CosmoCard` |
| 4 | `Tomcat.Feral` |
| 4 | `Tomcat.Slime` |
| 3 | `Tomcat.Kobo` |
| 3 | `Tomcat.Area0_map16_a` |
| 2 | `Tomcat.AreaC_map45_a` |
| 各 1 | `Tomcat.GenderSwapped`、`Tomcat.GenderSwappedPickup`、`Tomcat.AreaB_map03_a`、`Tomcat.TestA`、`Tomcat.AreaX_fenfen_rescued`、`Tomcat.SlimePickup`、`Tomcat.FeralPickup` |

**retain 场次：18 场**（coverage `result=retain`），其余 38 场 `issues_found`。retain 不等于「没问题」，而是「本场本路不再提判点」，三种情形：另一线同型问题已单独立条（如 SC3aafb021237724ae、SC70cabd30400d26f1 的卫星段拆行处理得比男线干净）；原文自身把同一玩笑换成另一形态（如 SC92ab63c597a375c2 的 Kobo 挂断理由与男线不同）；判定成立且人物差异已保住（如 SC0c36a41f62a4e9af 用「对方」处理中性 THEY）。

## 三、A 类逐条（必须报出的部分）

1. **P02-001 / P02-002（`CAT:O84f58ac1929bd4e50de4`、`SFW004f0ab00a8d33d90afecb9e`）** —— 靴子操作说明的英文三行已合到一行，现译用 12px 字形实测 **4 折行**，越过 240px／3 行页限。压缩只删「如果接触到任何」的重复框套，保留「必须已在空中」「必须命中会承受伤害的目标才回弹」两个玩法条件与 `DOWN + JUMP`。
2. **P02-003（`CAT:O819647f6652669d93d6f`）** —— 女线「宇宙大使」手册腔那段四行合句，实测 **4 折行**，本批最长正文（59 字）。压缩只去连接词与量词，「双方同意 / 自愿给出 / 联结 / 重要数据 / 宇宙大使」五个义项及顺序不变，`cosmo ambassador` 的反讽性质不变。
3. **P02-004 / P02-005（`CAT:Ob7711f8dc438e6e9ed0d`、`CAT:Obc38d2918bf863d8853b`）** —— `Y-YIFFAI OUT!` 的 OUT 是无线电结束语，现译「伊、伊吠，先走了！」读成了离场告退，实际他没走、是仓促挂断。本批 `YIFFAI OUT` 共四处两种处理，此处按结束语统一为「伊吠完毕」。

## 四、B 类主体（按主题）

- **术语口径（32 条，占本批最大宗）**：`trainer tazer` 一处「训练电击器」；`tazer` 两处「电击器」；`KOBOLD` 四处「狗头人」；`HOOKSHOT` 三处三种叫法（钩锁／钩爪枪／钩爪，UI 短名是「钩爪」）；`UP+ATTACK` 四条问题行、三种写法（UP+攻击／上+攻击，另有两条正确基准行不动）；`TAIL RAISER` 四处四个外号；`NUB` 一处「小肉棒」；`COMMAND CENTER` 一处「指挥中心」（其余全线「总部」）；`MARK IV COSMOBOOTS` 一处留英文；`ESPER POWERS` 一处「超能力者能力」叠词；`local life` 四种写法；`28.880` 与 `R18` 的数字排法；`NEGATIVE` 一处「否定」。
- **称呼漂移（PUPS/PUP 一组 4 条）**：同一批里 PUPS→「小家伙」、PUP→「小狗／小狗崽」并存，「小狗崽」是主流，已按主流收束。
- **语用与衔接（continuity 8 条）**：`会不会是你认错了？`（反问写成倒装陈述）、`解释一下，特工。`（公文腔）、`隔壁那间房里有什么东西……`（缺主语与句号）、`LIKE WHAT THE HELL…`（「比如」读成举例）、`AFTER SHE'S DONE…` 两处把时间状语塞进「希望」的宾语导致主谓错位。
- **笑点（idiom 4 条）**：`'MIRIN'`（羡慕→围观）、`TORCH`（女线抢话的梗必须落「火把」才能与男线 Bossu 那句闭环）、`GOOP`（拟声被译成形容词「黏糊」）、`ME!`（「我诶」读不出抗议）。
- **口吻**：`SOME OF US HAVE WORK TO DO` 两处把说话人自己推出画面；`I DUNNO ABOUT THAT` 读成理解障碍；`YOU NEED A NEW SENSE OF HUMOR` 读成对笑点的评价。

## 五、C 类（只 2 条）

- `CAT:O0cfa5bde1146fdd6ecea`：`AHHH, WELL…` 的敷衍重心落在「这个」上，读不出「原来如此、那我完了」。
- `CAT:O3a775d3332e66cb5e7fc`：`/EXPENSIVE/` 的斜杠强调被译成词典释义「/昂贵的/」，男线同句是「/贵得要命/」。

另有 1 条 C 类候选（`SECTION THREE-TWO DOT… UH, SIX` 的二次卡壳）**主动撤回**：让「3-2.6」还原成「3-2…6」会改动数字形态，触碰「不改数字」的硬约束，收益不抵风险。

## 六、needs_evidence（2 条，不冒充 A/B/C）

- **P02-070（`CAT:O0c8211a9d37463e29f8d`，LIGHTTAZER）**：三处口径冲突——参照摘录与 R1 术语提案写「光能电击刃」，全库现行正文（含本批同场景其它行、全库 21 处）一律「光电击枪」，本行又写「轻型电击枪」。按「不重提已裁决术语」，只报冲突不擅定名；`proposed_zh` 给的是候选取向，`note` 写明「若裁定以现行『光电击枪』为准则改为光电击枪保养」。
- **P02-071（`CAT:Oe0516f955ca5fbd52759`，失真段）**：同一位置的失真台词在四场里分成三种处理（女线 NSFW 整行留英文 / 女线 SFW 译成可读中文 / 男线洗成纯拟声）。`...ITCH!` 是 WAKE UP 残片还是独立残词，工单内无证据；`proposed_zh` 按「不改动失真 ASCII」保留原行，两个方向都写进 `note`，不由本路单方决定。

## 七、高风险连续段

1. **合句断点（最易复发）**：`AreaA_map42_a` 与 `AreaH_map02_a` 两处 4 行合句已被压成单行，实测 4 折行。凡「操作说明 + 条件从句」的合句都要重测宽度，`measure_width.py` 的 `over_limit` 当前会命中这三条（本路提案已把其中两条压回 3 行、一条保留在 3 行内）。
2. **按键名混排**：`AreaC_map64_b` 一个场景里 `UP+ATTACK` / `UP+攻击` / `上+攻击` 三种写法并存，且同一场景里两个说话人交替使用，是全批最容易被玩家读成两个键的地方。
3. **无线电套语**：`YIFFAI OUT` 四种处理、`NEGATIVE` 作「否定」、`COMMAND CENTER` 与 `HEADQUARTERS` 混用——这三项集中在 `AreaC_map56_a`、`GenderSwapped*`、`AreaH_map02_a`。
4. **失真广播**：`AreaC_map56_a` 四场里，同一段 `KZZ…` 与 `..UP!` 的处理方式互相冲突，且男线把可辨认词形洗成了拟声。
5. **多面性保护已核对**：`AreaA_map42_a`（先调侃靴子、后讲清操作）、`AreaX_fenfen_rescued`（感应图像，收起贫嘴）、`AreaC_map45_a`（被 TORCH 反将一军后 Bossu 沉默）三处，本路提案没有把 Tomcat 改成「每句贫嘴」或「说明书朗读器」，也没有新增「喵」或猫双关。

## 八、男女两版不一致清单

| 项 | 女线 | 男线 | 本路处理 |
| --- | --- | --- | --- |
| `YIFFAI OUT` | 首张卡段「伊吠完毕！」 | 「伊吠通话结束。」／「先走了！」 | 统一「伊吠完毕」，两线各自措辞 |
| `HUH?!` | 「呃？！」 | 「哈？！」 | 只报跨版本差异，不强行统一（同一 `GenderSwapped` 剧情，两版语感可分） |
| `TAIL RAISER` | 「爱翘尾巴的／翘屁股」 | 「撅屁股的小家伙」 | 统一词根「翘尾」，保留各自句子语气 |
| 卫星编号 | 「卫星 R18」（3 处） | 「R18卫星」 | 统一「卫星 R18」 |
| `28.880` | 「28.880 是我的频率」 | 「我的频率是28.880」（贴死） | 统一留空格，语序各留 |
| `KOBOLD` | 「科博德」 | 「狗头人」（4 处） | 统一「科博德」 |
| `local life` | 「本地生物／本地生命」 | 「当地生命／当地生物」 | 统一「本地生命」 |
| `THEY`（救出的小生物） | 「他」（定成男性） | 「对方」（中性） | 报女线为问题，男线作内证 |
| `COSMOBOOTS` | 「马克 IV 型／马克 III 宇宙靴」 | 「Mark IV Cosmoboots」（留英文） | 报男线为问题 |
| 靴子操作说明 | 3 折行（基准） | 4 折行（超限） | 报男线 NSFW + SFW 两条 A 类 |
| `TORCH` 梗 | 「照明电筒」（梗断） | Bossu「火把」+ Yiffai 反问闭环 | 改女线为「火把」，不搬男线句式 |

## 九、retain 场次的判断边界

18 场 retain 中需留意三处「不是没意见，而是不该由本路改」：

- `SC3aafb021237724ae` / `SC70cabd30400d26f1`：卫星段拆行版本本身成立，是男线该学而不是女线该改。
- `SC8c2e86fa78a3a795` / `SCaea814b2761c722a` 与 `SC5e2b2e3aaaa209d1` / `SCae345fce997f566f`：两场互为完全重复的短台词，改动必须四场同步，本路只报了其中误义的那两行。
- `SCe4cad5e13991e734` / `SCe21f2978a46f98f3`：SFW 版把「胡闹完了」提前、把「希望她接电话」放后，语序反而正确；NSFW 版才是问题版（P02-058/059 已报）。

## 十、未覆盖项与本工单不能证明的东西

- 只读、只写三个输出文件。未改 `orders/`、`translations/`、`builds/`，未写台账，未跑构建，未启动游戏。
- **行宽只做了 `preview-layout` 离线测得**（240px / 12px 真实字形表）。实测结论：改前 3 条 4 折行，改后全部 ≤3 行；`P02-067` 换全角引号后仍需在真机逐帧确认。
- 未能证明：本批提案在全 566 行合句重组后是否仍保持分页连贯（合句断点属另一层结构验证）；`AreaC_map64_b` 里 `UP+ATTACK` 与 `上+攻击` 是否在下游 UI 提示中有别的固定写法（未查 UI 资源）；`LIGHTTAZER` 应以哪一套为准（缺裁决，故列 needs_evidence）。
- 未处理本批范围外的事项：`units.jsonl` 中 `D15974ea891a0dd9c6454`（另一处 `COMMAND CENTER`）不在 batch-02 场景内，仅记录不提案；`CAT:Ocd189f63e760411cfd8c` 的下一行 `CAT:O882e1b20b14202516f16` 有同一 `他/对方` 问题，本路只报前一行并注明。
- 未复核 R3 人名、R6 术语回改、R8 谜题提示、R9 batch-01 的无线电／安保门／竖井网／一次性密码本等既有裁决，也未重提。
