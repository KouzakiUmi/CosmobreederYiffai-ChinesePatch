# batch-12-part01 精校小结：界面与系统文本——未覆盖的词典与任务日志条目（第 1／3 部分）

## 一、输入与覆盖

| 项 | 值 |
| --- | --- |
| 工单正文 | `localization/editorial/r9-polish/batch-12-part01/orders/batch-12-part01.reader.md`（993 行） |
| 结构化数据 | `orders/batch-12-part01.json`（157 场／213 ROW） |
| 规范 | `orders/ORDER.md`、`orders/reference-excerpt.md` |
| 基线 | 快照 `localization/editorial/r1/corpus/snapshot-03`（candidate13 显示行）；全库 2,989 场用于「库内多数写法」计数 |
| 场次覆盖 | **157／157 场**，`read_status` 全部 `read_full` |
| 行覆盖 | 213 行全部过目；`current` 为空的行只有 1 条（SpecialFap 的空值行，英文同样为空，按 ORDER 四.9 不报漏译） |
| 分段读 | 1–330（58 场）／331–660（58 场）／661–993（41 场），每段读完立刻追加 coverage 与 findings，再读下一段；三段均一次通过，无 `partial` |
| 场次构成 | `nsfw` 139 场／`sfw` 18 场；`datav/dictionary.json` 103 场（159 行）、`datay/scripts_pack.json` 54 场（54 行）；`dictionary_value` 159 行、`nested_json_value_runtime_usage_check` 54 行 |
| 覆盖结果 | `issues_found` 17 场、`retain` 139 场、`needs_evidence` 1 场 |

行尾空格判据一律取 `occurrence_id → unit_id → catalog/units.jsonl` 的 `source`；40 条 `SFW…` 行在 `occurrences.jsonl` 无记录，按 ORDER 改用本工单 JSON 的 `source`。**未使用 `occurrences.trailing_ws`**（那是中文列）。

## 二、发现总数与分布

**11 条发现（P12-0101～P12-0111），按场次出现顺序编号。**

| 级别 | 条数 | 编号 |
| --- | --- | --- |
| A | 0 | — |
| B | 6 | 0101／0106／0107／0108／0109／0110 |
| C | 3 | 0102／0105／0111 |
| needs_evidence | 2 | 0103／0104 |
| status=proposal | 9 | 0101／0102／0105～0111 |

按类别：`term` 7（0101、0103、0104、0106、0107、0109、0110）、`format` 2（0102、0111）、`idiom` 1（0105）、`meaning` 1（0108）。

按本轮归组（`root` 为内部键，只作分组不改）：

| root | 发现 | 判点 |
| --- | --- | --- |
| `/missionLog/male/8/header` | 0101 | ANOMALY 的名词中心「体」被截掉（男线四条同型） |
| `/missionLog/{female/2,female/5,female/8,male/3,male/6}/text` | 0102 | 占位样例行中文行尾多 3 个半角空格＋多余换行（5 行同值） |
| `AnomalyGamma` | 0103 | 词典条目「伽马」对任务日志「GAMMA」，口径待裁 |
| `/missionLog/male/1/header` | 0104 | ZENER 形状名「三角形」对词典「三角」，口径待裁 |
| `ClassicSpaceHead` | 0105 | HAUNTING＝动词短语「作祟」，当标签不成立 |
| `ClassicSpikebot` | 0106 | SPIKE 已落地为「尖刺」，本条件「刺机器人」不成词 |
| `SpecialBrace` | 0107 | 两侧按键名不一：`按下+跳跃`／`按DOWN+JUMP` |
| `SpecialFap.ElfBuff` | 0108 | 增译「加成」＋语序与同组两条不一致 |
| `SpecialHookshot` | 0109 | 两侧按键名不一：`UP+ATK`／`上+攻击` |
| `SpecialRadio` | 0110 | 两侧按键名不一：`(SELECT)`／`(选择)` |
| `StatCream` | 0111 | 中文行尾多一个半角空格 |

## 三、高风险连续段

1. **双份条目区（reader 663–678 `SpecialBrace`、798–819 `StatCream`）**：同一英文在 nsfw 与 sfw 各一份，本批唯一两处两侧都在批内的场次。`SpecialBrace` 已分叉（0107）；`StatCream` 的说明行英文本身不同（`GIVES ENERGY…`／`A LOVELY DRINK…`），中文各自对应，**不构成跨侧不一致**，容易被误判成漏改，已在 coverage 注明。
2. **`SpecialFap.*` 增益三条（695–709）**：`BigboldBuff`／`ElfBuff`／`SwiperBuff` 是同一句式模板，只有 `ElfBuff` 走了另一套语序并加了「加成」（0108）；旁边还挨着 `SpecialFap` 本体的空值行，逐行核对时最易被跳过。
3. **任务日志长提示区（57–64，`female/13/text`）**：全批唯一一段多行文本，含 `|` 分段、一整行空段与感叹号收尾；中文 6＋4 行与英文管道数、行数完全对应，结构未损。原文用 `his`／`Yiffai`（男线人名），女线照原文译，未按线改称。
4. **占位样例行集中区（92、123、149、264、275 与 232）**：`Line 1…Line 15` 与 `Lorem ipsum` 两类开发占位。结构必须原样，只有行尾空格可动（0102）；`male/19/text` 的 12 行多块结构同样原样保留。
5. **按键名区（`SpecialBrace`／`SpecialShoes`／`SpecialHookshot`／`SpecialRadio` 邻域）**：本批没有任何对白，所以 ORDER 里的「问答错位」「合句断点」「无线电套语」在本批均无对应行；本批的结构风险全部集中在按键名、`|` 段数与行尾空格三点上。

## 四、男女两版（及两侧包）不一致清单

| 类别 | 一侧 | 另一侧 | 处理 |
| --- | --- | --- | --- |
| `ACQUIRED ANOMALY ALPHA／BETA／GAMMA／OMICRON` | 女线四条＝「已获取异常体 X」 | 男线四条＝「已获得异常 X」 | 0101 只改批内的男/8 GAMMA；男/6、男/7、男/9 三条在批外，已在 note 点名。动词「已获取／已获得」保留各自版本，不机械统一（ORDER 四.10） |
| `ACQUIRED ANOMALY GAMMA` | female/8/header | male/8/header | 同一英文两版写法不同，构成「跨版本不一致」，见 0101 |
| `DEPOT B`／`ZERONIA`／`AYSKAMMR`／`SCEAFYA`／`HQ`／`MISSION`／`LIVEWARE`／`ENTERED …` | 女线各字段 | 男线各字段 | 两侧写法一致，retain，无发现 |
| `SpecialBrace`（nsfw／sfw 双份） | `按下+跳跃` | `按DOWN+JUMP` | 0107，方向＝保留拉丁键名 |
| `SpecialHookshot`（sfw 本批／nsfw part03） | `…按UP+ATK` | `上+攻击，且…` | 0109，改动目标在对侧，已注明所在 part |
| `SpecialRadio`（sfw 本批／nsfw part02） | `按(SELECT)` | `按 (选择)` | 0110，同上 |
| `StatCream` 说明行 | nsfw＝`GIVES ENERGY ｜TO MAKE MORE!` | sfw＝`A LOVELY DRINK｜FRESH & WARM` | 英文源本身不同，两侧中文各自对应，**不算不一致** |
| `SpecialShoes`（两侧，均在批外） | `空中下+跳跃` | `空中按DOWN+JUMP` | 同型分叉，只登记不提案（0107 note） |
| `AnomalyGamma`／`ZenerTriangle`（词典对日志） | 词典条目 | 任务日志 | 0103、0104，跨文件命名口径待裁 |

## 五、口径冲突与待核项

1. **`torch` 口径冲突（已按语料处理）**：参照摘录三把 R2 裁决的 `torch＝手电` 列为术语，但库内 23 处全部作「手电筒」（含本批 `SpecialTorch` 的 `TORCH` 与对白「你和那支手电筒可是救星」），且无一处作「手电」。按 ORDER 四.11「以语料为准」，`TORCH＝手电筒` **保留不改**；此处按 ORDER 要求在 note 报出冲突，术语表是否需要更新请主代理决定。
2. **`GAMMA／伽马`（0103）**：词典四条全中文、任务日志八条全拉丁，各自内部一致；统一方向会牵动批外 6 条日志行与 3 条词典行，本路不出提案。
3. **`三角形／三角`（0104）**：Zener 形状名在词典（星星／圆圈／三角／方块／十字）与日志（星形／圆形／三角形／十字）两套写法；批内成对行只有 TRIANGLE 一处。
4. **男线补「体」的连带改动**：0101 采纳后，男/6 ALPHA、男/7 BETA、男/9 OMICRON（均在批外）需同步，否则男线内部再分叉。
5. **对侧改动归属**：0109 的改动目标是 `SC1c19db45fc018a66`（batch-12-part03），0110 的是 `SC48112ce4d73a0f7e`（batch-12-part02）。本路只登记，未跨批改；两条的 `proposed_zh` 与本侧 `current` 相同，repair 时不要重复写回。
6. **`female/13/text` 的人称**：原文写 `his ship`／`agent Yiffai`，女线照译作「飞船坠毁」「特工伊吠」；是否按线改称属主代理裁决，本批不动。
7. **未终裁项一律未动**：`FENFEN`（`TribalHead`「Fenfen神圣的|羽饰帽」保留）、`LIGHTTAZER`（本批未出现）、引号体例（`“”` 与 `「」` 并存未统一）、`Traeh／Sevaw／Erauqs`（本批未出现）。

## 六、未覆盖项与「本工单不能证明的东西」

- **无对白可校**：本批 213 行全部是词典值与任务日志字段，没有 speaker、控制行、合句尾行，ORDER 里针对台词的分级判据（施受关系、口吻、称呼矩阵）在本批基本用不上；`voice` 类别为 0 条。
- **未做实机与渲染验证**：短标签长度只按字符数比较（提案均 ≤ 英文原长），但卡片 16 列 × 128px、数据书 224px／≤3 行的实际折行、CJK 与拉丁混排的字宽未在游戏内实测；0102 与 0111 的改动只涉及行尾空白，不影响折行，但同样未实测。
- **`|` 结构只做计数校验**：全批 213 行管道数与物理行数均与英文一致（0 处结构损坏），但「段数与英文相同」不等于「每段宽度都放得下」，宽体字挤压未验证。
- **两侧包是否都装载这两份词典**：本批只比较 `datav/dictionary.json` 在 nsfw／sfw 两份里的写法，没有验证打包后游戏实际读哪一份、是否两份都会显示。
- **对侧部分未知**：part02／part03 的工单正文未读（避免两路互相参考），因此 0109／0110 的对侧是否已被同批其它部分处理，本工单不能证明。
- **库内计数依赖快照**：所有「库内 N 处」均基于 `snapshot-03`（candidate13 基线），后续 R9 批次的改动不在其中；若某批已改过同一串，计数会偏移。
- **未验证项**：`BIGBOLD1／BIGBOLD2`、`FENFEN` 中文名、`LIGHTTAZER` 中文名等已知缺口本批未涉及或按口径未动，本工单不对其结论负责。
