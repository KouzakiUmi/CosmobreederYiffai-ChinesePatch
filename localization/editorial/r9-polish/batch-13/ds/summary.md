# batch-13 精校小结（毛鼠旁白提示 MauserHints）

## 一、输入与覆盖

| 项 | 值 |
| --- | --- |
| 工单正文 | `localization/editorial/r9-polish/batch-13/orders/batch-13.reader.md`，824 行（第 1–420 行一段、421–824 行一段，两段分读、每段读完即落盘） |
| 结构化数据 | `orders/batch-13.json`（50 场／183 ROW，其中 56 条 ROW 的 `current` 为空） |
| 规范 | `orders/ORDER.md`、`orders/reference-excerpt.md` |
| 定点参照 | `localization/editorial/r8-puzzle/README.md`（只查裁决口径）、`localization/review/glossary.csv`、`localization/translations/character-names.json`、`localization/editorial/r4-pending/reports/pending-01/SUMMARY.md` 与 `translations/editorial-r4-pending-repairs.jsonl`、快照 `snapshot-03` 的术语用法检索 |
| 读完场景 | **50／50 场**（`read_full` 50 场，无 `partial`／`not_read`） |
| 行尾空格判据 | 只用了英文原文侧：`units.jsonl` 的 `source`（无 occurrence 记录的 16 条 SFW ROW 按工单 JSON 的 `source`）。全批只有 2 条英文行尾带半角空格（`SFWefcd89cea0a176b4c7285fcd`、`SFW4b339dfc63ada9959224d6b9`），其中文行为空，未产生中文行尾空格问题，未报 |

## 二、发现分布

**共 12 条**：A 0 ／ B 7 ／ C 3 ／ needs_evidence 2。

| 编号 | 场 | root 主题 | 级别 | 类别 | 一句话 |
| --- | --- | --- | --- | --- | --- |
| P13-D001 | SC3c709e08abecdd6b ＋ SC8b485ccdf0b6b9fc | Area0.AfterBigboldV2KilledSafe | needs_evidence | source_uncertainty | TRANSMISSION POINT 译「传输点」，库内 TRANSMISSIONS 一律「通讯」，但该地点无第二出处可定它是通讯中继还是传送设施 |
| P13-D002 | SCa4aeea4fcaaf7602 ＋ SCee65d81001fa7f60 | Area0.AfterFirstAgentRescued | C | idiom | 「派上用场，用来」两个「用」叠在一句，可压到「帮你前往新区域」 |
| P13-D003 | SC567b9e156beb4379 | Area0.Endgame（男） | B | term | 第 4 行「监狱月球」与同场第 8 行「监狱卫星」自相矛盾；glossary 的 Exile 条写明不另造月球义 |
| P13-D004 | SC2c6addff352bfb13 | AreaB.AfterPsyStar（女） | B | term | 「超能力者能力」术语套叠，库内与男版同句都作「超能力」，按键名 SELECT／UP+ATTACK 不变 |
| P13-D005 | SC8fb6708eb73e3670 | AreaB.AfterWerehundDefeat（男） | B | idiom | 「我方对那处区域的通讯记录显示」介词当属格，句子不成立；女版同句作「我方通讯记录显示」 |
| P13-D006 | SC65bfc7226dcf8d7d | AreaB.AfterWerepupDefeat（男） | B | term | 同一处 DEPOT 这里译「补给站」，全库与女版同句都是「仓库」 |
| P13-D007 | SC68434f2afb7359a4 ＋ SC745aeb8f8f9dc42d | AreaB.ReturnFromAreaA | C | idiom | 「我还以为……了呢？」陈述句挂问号 |
| P13-D008 | SCae10fcc52e96b81c | AreaC.EnelyeHint（男） | C | idiom | 「哪儿有一张高级门卡」易读成疑问，女版同句作「某处」 |
| P13-D009 | SC87179380694e608e | AreaC.OpenMode（男） | B | term | NAVMAP 作「导航地图」，界面名与同批另四处是「导航图」 |
| P13-D010 | SCedea7267588eb179 | AreaE.AfterFirstEnteredAreaE（女） | needs_evidence | source_uncertainty | 女线原文（patch 生效行）称呼 YIFFAI，同提示 SFW 女版与其余女线都称 YIFFANY；现译照英文作「伊吠」 |
| P13-D011 | SCa1e42fd2a89cb4a7 | AreaE.AfterSeenLock（女） | B | term | 「流放东北」把地名截成动词：R4 的 P05-037 只补了 SFW 副本，nsfw 这条漏改 |
| P13-D012 | SCb83c11a1adaf52ec（并含 SCa1e42fd2a89cb4a7、SC6fc409e41e2a9bb6） | AreaE.AfterOpenedLock／AfterSeenLock | B | term | 同一 VAULT 男线作「金库」、女线三行作「宝库」，语料主角自述也作「金库」 |

按 root 归组（50 场 / 23 个 root；发现只落在下表带 ✅ 的 root）：

| root | 场数 | 发现 |
| --- | --- | --- |
| MauserHints.AreaC.PigobinHint noselect | 2 | — |
| MauserHints.AreaC_OneBossDefeated | 2 | — |
| MauserHints_Area0.AfterBigbold1Killed | 2 | — |
| MauserHints_Area0.AfterBigboldV2KilledEscape | 2 | — |
| MauserHints_Area0.AfterBigboldV2KilledSafe | 2 | ✅ D001 |
| MauserHints_Area0.AfterFirstAgentRescued | 2 | ✅ D002 |
| MauserHints_Area0.BeforeBigbold1Killed | 2 | — |
| MauserHints_Area0.Endgame | 2 | ✅ D003 |
| MauserHints_Area0.ReturnFromAreaB | 2 | — |
| MauserHints_AreaB.AfterEnteredAreaB | 4 | — |
| MauserHints_AreaB.AfterPsyStar | 2 | ✅ D004 |
| MauserHints_AreaB.AfterWerehundDefeat | 2 | ✅ D005 |
| MauserHints_AreaB.AfterWerepupDefeat | 2 | ✅ D006 |
| MauserHints_AreaB.ReturnFromAreaA | 2 | ✅ D007 |
| MauserHints_AreaC.AfterFirstEnteredAreaC | 2 | — |
| MauserHints_AreaC.End | 2 | — |
| MauserHints_AreaC.EnelyeHint noselect | 2 | ✅ D008 |
| MauserHints_AreaC.OpenMode | 2 | ✅ D009 |
| MauserHints_AreaC.ReturnLater | 2 | — |
| MauserHints_AreaE.AfterFirstEnteredAreaE | 3 | ✅ D010 |
| MauserHints_AreaE.AfterOpenedLock | 2 | ✅ D012 |
| MauserHints_AreaE.AfterSeenLock | 3 | ✅ D011、D012 |
| MauserHints_AreaH.Stub | 2 | — |

保留判定（`retain`）的 14 个 root 不是没看，是逐条比过英文与语料后判为成立：方向与顺序（西南部、东部、东北部、越往上、westward）、条件句（IF／IF ONLY／NOW THAT）、玩法指向（护腕→新区域、门卡→更深处、手电筒→照明、宇宙服→上卫星）、称呼方向（女线弟弟／男线姐姐）都对得上。

## 三、高风险连续段

1. **合句断点（56 条空行，全是合句尾行，未报漏译）**
   - 最重一处：`AreaB.AfterPsyStar` 女版把 4 条英文（含两条带引号的按键说明）压成一物理行，正文约 80 字、折行约 3 行；D004 只在里面换术语，未拆行（拆行需要改物理行结构，按 ORDER 四·3 只写在 note）。
   - `AreaB.AfterEnteredAreaB` 男女各把 2 条英文压成 1 行（41／38 字）；`AreaC.Endgame`、`AreaC.ReturnLater`、`AreaE.AfterSeenLock` 同型。
   - 同一提示的 SFW 女版（`SC6fdb8418c5faf950`）反而三行各自成句，与 nsfw 版的合并策略不同；这是既有基线差异，未改。
2. **问答／应答错位**
   - `AfterWerehundDefeat` / `AreaC.End`：毛鼠报人数 → 主角应答「我去找他们／交给我吧」。人数（两名／三名）、地点（那处区域／附近）是硬信息，D005 只动结构不动数字。
   - `AreaE.AfterSeenLock`：主角问「有什么办法能打开它吗」→ 毛鼠答 FENFEN 技术。FENFEN 中文名未终裁，本批保留英文，未借机定名。
   - `Area0.Endgame` 三个 `else` 分支（导航图找人／先找回宇宙服／已可上卫星）在同场内相邻，D003 只改一个名词，未跨支串词。
3. **无线电套语**
   - 「OUR RECORD OF TRANSMISSIONS FOR THAT AREA SHOWS」全批出现 3 处，中文三种写法：「我方通讯记录显示，那处区域附近有两名特工」「我方对那处区域的通讯记录显示，共有两名特工在附近」「我方通讯记录显示，那处区域附近一共有三名特工」。D005 只修男版那处病句，不强行统一「共有／一共有」。
   - 应答套语：男线「我去找他们！交给我吧！」／女线「我会找到他们的！包在我身上！」——两版各成一套，保留。
4. **窄框**
   - 12 条提案的整行长度与原行相差 −5 ～ +1 字（D004 由 84 字减到 81 字；D010、D011 各多 1 字，是补称呼／补地名所必需，属持平）；D004 的 `note` 写「行宽待实测」。本批没有一条会让 ≤3 行折行变成 >3 行的提案。

## 四、男女两版不一致清单（只列可见差异，未强统）

| 内容 | datadf（女） | datadm（男） | 处理 |
| --- | --- | --- | --- |
| Prison Moon | 你真要上那颗监狱卫星吗？ | 你真的要去那座监狱**月球**吗？ | D003 改卫星 |
| 备忘录尾句 | ……**结果**它转眼就弄丢了 | ……它转眼就弄丢了 | 不报（语气差可接受） |
| AfterBigbold1Killed 跟随 | 跟上他！ | 追上去！ | 不报 |
| Escape 提示 | 快从那儿出来！！！ | 快离开那里！！！ | 不报 |
| 装备／小偷 | 你得找回你的装备，伊吠妮！／不可能走太远 | 伊吠，你得把装备找回来！／跑不了多远 | 不报 |
| 通讯记录套语 | 我方通讯记录显示 | 我方**对**那处区域的通讯记录显示 | D005 改男版 |
| 希望／应答 | 希望他们平安！／包在我身上 | 希望他们都没事！／交给我吧 | 不报 |
| 门卡→仓库 | 往**仓库**更深处 | 往**补给站**更深处 | D006 改男版 |
| 三名特工 | 一共有三名特工 | 共有三名特工 | 不报 |
| 高等级门卡 | 肯定也有张高等级门卡藏在**某处** | 那肯定说明**哪儿**有一张高级门卡 | D008 改男版 |
| NAVMAP | 记得查看**导航图** | 记得查看**导航地图** | D009 改男版 |
| 宇宙服凑齐 | 重新拼好了 | 又凑齐了 | 不报 |
| Energy signatures | 女线 nsfw／男线：能量**特征**；SFW 女版：能量**信号** | 能量特征 | 不报，记入本表 |
| VAULT | 那座**宝库**（nsfw 2 行＋SFW 1 行） | 那个**金库**（3 行） | D012 |
| EXILE 地名 | 「你在**流放**东北发现的那座宝库」（nsfw 行）/「流放地」（SFW 行） | 「流放地东北边」 | D011 补漏改 |
| 迎宾语 | 「有什么办法能让**我**打开它吗？」 | 「有什么办法能打开它吗？」 | 不报 |
| Hangar 句 | 一边计划下一步行动！ | 顺便规划你的下一步行动！ | 不报 |

另：`Area0.ReturnFromAreaB` 与 `AreaC.ReturnLater` 是两个 root，男女两版文本逐字相同（中英皆同），未构成不一致。

## 五、待核项（交主代理裁决）

1. **D001** TRANSMISSION POINT＝「传输点」还是「通讯点」：库内无第二出处，别改前请定口径（男女两行须同改）。
2. **D010** 女线 nsfw 的 YIFFAI：照译保留，还是按女线口径改「伊吠妮」。patch 覆盖后的生效原文确实是 YIFFAI。
3. **D012** VAULT 口径：本条主张「金库」（与语料主角自述、男线三行一致），但 R4 的 P05-037 修复串里保留的是「宝库」。若主代理认定沿用「宝库」，则反向把男线三行改成「宝库」。
4. **D011** 只是把 R4 已有裁决补到漏改副本，不构成翻案；若认为 nsfw 那行有意作「流放」，请驳回。

## 六、未覆盖项与本批不能证明的东西

- **未覆盖**：无。50 场全部 `read_full`，coverage 无重复 `scene_id`、无缺场。
- `MauserHints_AreaA` 属 batch-01，本批未读、未提案，也未重提那批措辞。
- 未终裁项按口径回避：LIGHTTAZER 中文名、FENFEN 中文名（`AreaE` 三场都保留英文 Fenfen）、引号体例（「」与“”并存未统一，D004 也保留「」）、`Traeh`／`Sevaw`／`Erauqs` 现状未动；R3 人名、R8 谜题措辞、R9 已落地术语（宇宙服、Cosmohelm、Kobo、council、feral、knot、nubs、UP+ATTACK 等）未翻案。
- **不能证明**：本批只做文本层精校，**未跑构建、未启动游戏、未看渲染**——所以「行宽待实测」（D004 的约 80 字合句行、41 字合句行）只是长度估算，不是实测像素；分页 3 行上限、12px 字宽在实机是否真的不溢出，没有证据。
- **不能证明**：提示的触发条件与显示时点只在脚本里读到（`if { f(...) }` / `hasItem(...)`），未在游戏内核对分支是否按预期弹出；nsfw／sfw 与男女四种变体在实机是否同时生效也未验证。
- **不能证明**：本批结论只覆盖 `MauserHints*` 这类提示，其措辞与词典条目、图像资产、其它 root 的 UI 文案是否一致，只在需要出处时做过定点检索（快照 `snapshot-03`），不是全库普查。
- 提案是否被采纳、以及采纳后 17 步回归是否仍全绿，本批不产出也不代表；本轮不写台账、不动归档、不碰其它文件。
