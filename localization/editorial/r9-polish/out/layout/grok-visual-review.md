读图：成功（108/108）。标点垂直错位无法从 read_image 转写判断（转写只有文字、没有基线；8px 卡面转写还有错字），该项标「无视觉依据」，不把字模 yoffset 写成眼见。

读图范围：`card/card-01.png`…`card-48.png`、`data/data-01.png`…`data-30.png`、`dialogue/dialogue-01.png`…`dialogue-30.png`。12px 图（数据书、对话）转写能对上原文和行数；断行位置与出图脚本 `render_layout_samples.wrap` 一致，严重切词在图上能读出来。8px 卡面转写会把「阿尔法」读成「网法」、「犬」读成「光」，不能用来判缺字或引号高低。PNG 比栏宽多 8px 是样本渲染左右各 4px 留白（`render.py` `padding=4`），不是字溢出。

## ① 标点错位

### 必须修

行首标点（折行把全角标点甩到下一行开头，图上能读出，不是字号问题）：

| 图 | 位置 | 字符 | 定位 |
|---|---|---|---|
| dialogue-05 | 第 2 行行首 | `，` | `vsn/f_AgentF03/script.vsn` `vsn/23` L62。上一行以「混蛋」结束 |
| dialogue-06 | 第 4 行行首 | `，` | `vsn/m_AgentM01/script.vsn` `vsn/209` L49。上一行以「底下」结束 |
| dialogue-09 | 第 2 行行首 | `，` | `vsn/m_AgentM03/script.vsn` `vsn/221` L63。上一行以「对」结束 |
| dialogue-12 | 第 2 行行首 | `，` | `vsn/m_AgentM03/script.vsn` `vsn/221` L49。上一行以「飞龙」结束 |
| dialogue-14 | 第 3 行行首 | `，` | `TomcatItems.SpecialFap` `datadf/1` L4462 |
| dialogue-15 | 第 3 行行首 | `，` | `Tomcat.FeralPickup noselect noamendfreq` `datadm/1` L3808 |
| dialogue-16 | 第 3 行行首 | `，` | `vsn/m_ClassicWerepup/script.vsn` `vsn/347` L11 |
| dialogue-19 | 第 2 行行首 | `：` | `vsn/f_ClassicWerepup/script.vsn` `vsn/149` L67。上一行以「脑子」结束 |
| dialogue-20 | 第 3 行行首 | `，` | `vsn/m_AgentM02/script.vsn` `vsn/215` L29 |
| dialogue-26 | 第 2 行行首 | `。` | `MauserHints_AreaA.DragonHint noselect` `datadf/1` L3462。dialogue-29 同图（`datadf/1` L3413） |
| data-22 | 第 2 行只有这一个字 | `！` | `ui.end.Tier1.l7`。第 1 行停在「不错的尝试」 |

### 直引号实例（位置在图对应文本里，高低无视觉依据）

本批 **story12 图（数据书 30 + 对话 30）里没有 ASCII 直引号 `"` `'` 夹在汉字中间**。对话里的引号是全角/弯引号 `“”` `‘’` `「」`，转写能读出，没有读成方框。

仅有的 ASCII `"` 在 classic 8px 卡面，不在 `story12.fnt`：

| 图 | 行 | 字符 | 定位 |
|---|---|---|---|
| card-08 | 第 3 行，行首 `"` 与「艾斯卡姆尔」之间，以及「尔」与「的」之间 | ASCII `"` `"` | `ui.card.CosmoCardDragon.desc.Front`。文本：`如今名为\|"艾斯卡姆尔"的` |
| card-29 | 第 7 行，行首 `"` 与「他」之间，以及「的」与「领」之间 | ASCII `"` `"` | `ui.card.CosmoCardRedbull.desc.Front`。文本：`任何闯入\|"他的"领地的人。` |

这两张的 read_image 转写是糊的，**看不出引号偏上、偏下或偏小**。无视觉依据，不判成已确认错位。

### 其他半角标点（出现位置确认，偏小/错位无视觉依据）

字号和基线看不出来。下列只记录「汉字行里有半角标点」，不写成已看见错位：

- ASCII `[` `]`：data-01…data-13 第 3 行，包住谜题提示（如 data-01 `ui.data.f_AgentFZ1.desc` `[星星在十字与方块之间]`）。data-01 与 data-02 同图，data-04 与 data-09、data-05 与 data-10、data-06 与 data-11、data-07 与 data-12、data-08 与 data-13 同图。对话里说话人方括号也是 ASCII `[` `]`（dialogue-03、08、10、13–15、17、18、22–26、29），紧挨汉字。
- ASCII `-`：data-17 第 1 行，「宙」与 `-` 之间。`ui.end.Tier4.l8`，文本 `宇宙-`。
- ASCII `!`：data-25 第 2 行，全角 `！` 后面还有一个半角 `!`。`ui.end.Tier3.l9`，`手！ !`。data-17、data-22、data-26、data-27 行首 `*!` 是拉丁标记，不夹在汉字中间。
- ASCII `.`：data-20 `MR.SATURN` 的句点在拉丁字母之间，不是汉字行内标点。
- 逗号、问号、圆括号、破折号、省略号的**全角**形式：转写里跟汉字在同一行，没有读成方框。是否贴底、是否与汉字基线一致，转写看不出，不判。

### 可疑

- dialogue-08 第 1 行以 `“按` 结束，第 2 行才是 `SELECT`。开引号和引文被拆开。`MauserHints_AreaB.AfterPsyStar` `datadm/1` L3598。引号是弯引号 `“`，不是 ASCII `"`。
- 卡面把省略号或叹号单独成行（`|` 是作者断行，不是 240px 自动折行）：card-13 第 14 行只有 `……`（`ui.card.CosmoCardElf.desc.Back`）；card-19 第 14 行只有 `……`（`ui.card.CosmoCardKobold.desc.Back`）；card-23 第 11 行只有 `……`（`ui.card.CosmoCardOmegobin.desc.Front`）；card-29 第 11 行只有 `……`；card-38 第 11 行只有 `！`（`ui.card.CosmoCardSwiper.desc.Front`）；card-46 第 14 行只有 `！！`（`ui.card.CosmoCardWyvern.desc.Back`）。

### 非眼见（字模，不作为本报告的视觉结论）

`story12.fnt`：汉字与全角 `，。！？「」“”‘’……` 为 12×12、`yoffset=0`。ASCII `"` 为 7×5、`yoffset=-1`，`'` 为 6×5、`yoffset=-1`，`,` `.` 为 4–5px 且 `yoffset=4`。这批 story12 样本没有用到 ASCII `"` `'`，所以已知缺陷在这 60 张 12px 图上没有实例。classic 的 `"` 也是 7×5、`yoffset=-1`，汉字格是 8×8；card-08、card-29 若在实机偏高，是 classic 的问题，本轮转写确认不了。

## ② 折行切词

自动折行按字宽贪心切，不认词。下面「必须修」只收双字词、专名或控制键被从中间切开的。短语边界（如「面条／里」「往／成就」）放可疑。

### 必须修

对话（240px）：

| 图 | 行 | 切开 | 定位 |
|---|---|---|---|
| dialogue-01 | 3→4 | 特／工（特工） | `vsn/m_AgentM06/script.vsn` `vsn/239` L86 |
| dialogue-02 | 2→3 | 矮／人 | `vsn/m_AgentM04/script.vsn` `vsn/227` L19 |
| dialogue-02 | 3→4 | 可／惜 | 同上 |
| dialogue-04 | 1→2 | 其／他（其他） | `vsn/f_AgentF01/script.vsn` `vsn/11` L38 |
| dialogue-05 | 2→3 | 多／亏（多亏） | `vsn/f_AgentF03/script.vsn` `vsn/23` L62 |
| dialogue-07 | 2→3 | 紧／紧（紧紧） | `vsn/m_AgentM06/script.vsn` `vsn/239` L64 |
| dialogue-08 | 2→3 | `UP+A`／`TTACK`（ATTACK） | `MauserHints_AreaB.AfterPsyStar` `datadm/1` L3598 |
| dialogue-08 | 3→4 | 执／行（执行） | 同上 |
| dialogue-10 | 1→2 | 拿／到（拿到） | `MauserHints_AreaA.DragonHint noselect` `datadm/1` L3525 |
| dialogue-11 | 1→2 | 牢／房（牢房） | `vsn/m_AgentM04/script.vsn` `vsn/227` L80 |
| dialogue-11 | 2→3 | 没／有（没有） | 同上 |
| dialogue-11 | 3→4 | 孩／子（孩子）。第 4 行只有「子。」 | 同上 |
| dialogue-12 | 2→3 | 气／味（气味） | `vsn/m_AgentM03/script.vsn` `vsn/221` L49 |
| dialogue-13 | 1→2 | 自／愿（自愿） | `Tomcat.AreaH_map02_a noselect` `datadf/1` L2592 |
| dialogue-14 | 1→2 | 要／是（要是） | `TomcatItems.SpecialFap` `datadf/1` L4462 |
| dialogue-16 | 1→2 | 就／是（就是） | `vsn/m_ClassicWerepup/script.vsn` `vsn/347` L11 |
| dialogue-18 | 1→2 | 用／来（用来） | `BossuDex.ClassicSpikebot` `datadm/1` L3028 |
| dialogue-20 | 1→2 | 因／为（因为） | `vsn/m_AgentM02/script.vsn` `vsn/215` L29 |
| dialogue-22 | 1→2 | 活／动（活动） | `Mauser.AreaA_map33_a` `datadf/1` L2216。dialogue-24（同场景 L2210）同图 |
| dialogue-23 | 1→2 | 活／动（活动） | `Mauser.AreaA_map33_a` `datadm/1` L2227。dialogue-25（L2206）同图 |
| dialogue-27 | 2→3 | 挑／逗（挑逗） | `vsn/f_ClassicWerepup/script.vsn` `vsn/149` L105 |
| dialogue-30 | 1→2 | 训／练（训练） | `vsn/m_ClassicWerepup/script.vsn` `vsn/347` L20 |
| dialogue-30 | 2→3 | `V`／`R`（VR） | 同上 |

数据书（224px，空格把结尾行撑满后把末词切到第 2 行）：

| 图 | 行 | 切开 | 定位 |
|---|---|---|---|
| data-20 | 1→2 | `MR.SATUR`／`N` | `ui.end.cr4` |
| data-23 | 1→2 | 真／正（真正的） | `ui.end.Tier4.l7`。第 2 行是「正的」 |
| data-24 | 1→2 | 快／吗（更快吗？） | `ui.end.Tier2.l9`。第 2 行只有「吗？」 |
| data-25 | 1→2 | 高／手（高手） | `ui.end.Tier3.l9`。第 2 行是「手！ !」 |
| data-27 | 1→2 | 种／者（育种者） | `ui.end.Tier4.l9`。第 2 行是「者！」 |
| data-28 | 1→2 | 开／发（开发） | `ui.end.cr6`。第 2 行是「发」 |

### 可疑

- dialogue-01 第 1→2 行「面条／里」、第 2→3 行「往／成就」：词本身没从中间切开。
- dialogue-03 第 3→4 行「神志／不清」：四字短语对半切。`MauserHints_AreaB.AfterPsyStar` `datadf/1` L3535。
- dialogue-06「地位／是」、dialogue-09「报名／要」、dialogue-10「更深处／好几处」「为你／放行」、dialogue-17「毕竟／他」、dialogue-21「包围／了」、dialogue-26「安保门／的」（dialogue-29 同图）：语法边界，不是双字词中切。
- data-14、data-15（同图）作者用 `|` 断成「哥布林／肉」。`ui.data.f_GameOverAreaC.desc` / `ui.data.m_GameOverAreaC.desc`。哥布林是完整词。
- data-26：`*!` 留在第 1 行，`哇！！` 整段掉到第 2 行。`ui.end.Tier4.l3`。词没切开，但这一行字幕断了。
- data-16、data-17、data-18、data-19、data-21：正文在第 1 行是完整的，第 2 行只有尾部空格（16–32px）。贴着 224px，空格被折下去。
- card-19 第 9→10 行「令人／愉悦」（`ui.card.CosmoCardKobold.desc.Back`）；card-22 第 6→7 行「小／社会」（`ui.card.CosmoCardOmegobin.desc.Back`）。这是卡面 `|` 断行，不是自动折行。

## ③ 超限／溢出／缺字／空面板

### 必须修

- 对话页：出图脚本写明 `PAGE_ROWS = 3`。dialogue-01…dialogue-11 是 4 行（图高 72px = 4×16+8），dialogue-12…30 是 3 行（56px）。样本 PNG 把第 4 行画全了，图本身没有裁切。若实机对话页只显示 3 行，这 11 张的末行会丢。未跑游戏，不能确认实机是裁切还是翻页。

### 未超限（不要当成溢出）

- 卡面行数：最大 15，card-16（`ui.card.CosmoCardEnelye.desc.Back`）、card-37（`ui.card.CosmoCardSwiper.desc.Back`）贴限，没有第 16 行。图高 128px = 15×8+8 留白。
- 数据书行数：最大 3，没有超过。
- 宽度：index 的 `widest` / 折行后字宽都没有超过 128／224／240。贴限：card-07、card-16 为 128px；data-16…data-20 为 224px；多条对话行正好 240px。card-07、card-16 的 PNG 宽 136、data-16…20 的 PNG 宽 232、对话 PNG 宽 248，都是字宽加左右各 4px 留白，不是字形画出栏外。
- 缺字：12px 转写与 index 原文一致，没有空白方块或问号框。8px 转写的错字是识别错误，不是图上的缺字框。渲染器对缺字是不画、前进 0（`render.py`），所以「没看到方框」也不能证明每个码位都有字模；这 108 张的转写没有露出缺字。
- 空面板：没有。最窄的名字条（card-03、06、09 等）也有字，高 16px。

## ④ 其他观感问题

- 同图重复，修一处即可：dialogue-22 = dialogue-24；dialogue-23 = dialogue-25；dialogue-26 = dialogue-29；data-01 = data-02；data-04 = data-09；data-05 = data-10；data-06 = data-11；data-07 = data-12；data-08 = data-13；data-14 = data-15。
- 卡面人名仍是拉丁原文（Fenfen、Sevaw、Erauqs、Traeh），不是排版缺陷。card-07、card-35、card-43、card-44。
- dialogue-20 的「雄、性、的」是原文顿号，不是折行切出来的。
- 全角标点在 12px 转写里大小看起来和汉字一格，没有单独缩成一个点；基线仍无视觉依据。
