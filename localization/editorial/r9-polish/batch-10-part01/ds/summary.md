# batch-10-part01 精校小结（路线 ds）

## 一、输入与覆盖

- 工单正文：`localization/editorial/r9-polish/batch-10-part01/orders/batch-10-part01.reader.md`，共 1606 行（含场头与空行），正文 **98 场／459 条 ROW**。
- 同源结构数据：`orders/batch-10-part01.json`（用于取精确 `scene_id`／`row_id`／`source`／`current`／行尾空白）。
- 规范：`orders/ORDER.md`、`orders/reference-excerpt.md` 已逐节读完；方法口径按 `TRANSLATION_PLAN.md` 第五节七步重写与第七节分级执行（未整读长文）。
- **实际读完 98／98 场**，`coverage.jsonl` 98 行、`scene_id` 无重复、`row_ids` 与工单逐场一致；`read_status` 全为 `read_full`。
- 逐段核对的结构项：每场的 `|` 段数与 `source` 逐行比对（459 行**无段数不符**）；`<…>`、`@EmuButtons`、`___`、`*你*`、`$`、`[ ]`、坐标数字与逗号后半角空格、存档点代号均原样保留；卡面与资料卡行尾补白（`    \n` 一类）按镜像不动。

## 二、发现总数与分布

**7 条**：A 0／B 4／C 3／needs_evidence 0。按 root 归组：

| root | 条数 | finding_id |
| --- | --- | --- |
| `ui.achievement_popup` | 1 | P10-0101（C／format） |
| `ui.breeding.Kobold.affinity` | 1 | P10-0102（B／term） |
| `ui.card.CosmoCardRedbull.desc` | 1 | P10-0103（C／format） |
| `ui.data.f_ClassicWerehund`＋`ui.data.m_ClassicWerehund` | 1 | P10-0104（B／continuity，跨两版两条 row_id） |
| `ui.data.m_GameOverArea0` | 1 | P10-0105（C／idiom） |
| `ui.inputConfig`（SFW 侧） | 2 | P10-0106（B／term，SELECT）、P10-0107（B／term，START） |

零发现 root：`/patchDictionary/navmap`（AreaA）、`navmap` 及 Area0／AreaA／AreaC／AreaH／TestArea、`input`、`input.gdx2.psx`、`input.gdx2.std`、`input.xinput`、`save`（nsfw＋sfw）、`ui.achievement.*`、`ui.breeding.*`（其余物种）、`ui.card.*`（其余卡与两页说明）、`ui.cheats.*`、`ui.data`（名录 58 行）、`ui.end`、`ui.end.Tier3`、`ui.gameOver`、`ui.log`、`ui.options*`、`ui.presetcheat.*`、`ui.save`。这些场在 `coverage.jsonl` 中逐场记了判断与边界。

## 三、高风险连续段

1. **`ui.inputConfig` 双版本（SCaa4e9abd60ef4ece／SCf784fa152a41c9cc）**：动作名（跳跃/攻击/返回/菜单）与菜单键名（SELECT／START）混在一屏，中文侧是否把键名也中文化没有单一口径；本路按批内多数（3 处作「选择/开始」）出提案，方向本身留给裁决。
2. **多键拼装的警告对话框（SC3da55b03891395ae、SC909ece114f8d7c87）**：整句被拆成 8／3 个独立键，中译在相邻键上换位（`MAKING ANY CHANGES TO THE` 与 `CURRENT CHEAT MENU SETTINGS`），这是为中文动宾语序做的重排；键数未变，但「换位是否与引擎显示顺序一致」本工单无法证明（见第五节）。
3. **资料卡定宽折行（`ui.card.*.desc`，11～14 段／页）**：断词、断句与行尾补白三件事同时受约束；P10-0103 正是在这一层发现「分神」跨行、感叹号独占一行。
4. **跨侧地名（`/patchDictionary/navmap.AreaA` ↔ `navmap.AreaA`）**：本 part 只有 AreaA 可两侧对照，逐键一致；其余 Area 的 patch 侧不在本 part。
5. **`ui.end`（SC580371689798d88c）与 `ui.data`（SC617b0e6e84523b03）**：前者全是居中空格装置，后者是 58 行名录用 `DEFEAT 1～4` 计数；两处都是「看起来能顺手改、实际不能动」的区域，已一律记 retain。

## 四、男女两版不一致清单

- **`ui.data.f_ClassicWerehund`（SC205dcd8ee4b31d57／CAT:O6b4934990569ea09a790）vs `ui.data.m_ClassicWerehund`（SC6bee720011b54d59／CAT:O7e2208e284fff845e691）**：同一英文 `WAN GREAT VICTORY\|LEADS TO A RUFFER DEFEAT!`，女线「汪！一场大胜\|换来更惨的败仗！」、男线「一场汪汪大胜，\|竟换来更惨的失败！」——已出 P10-0104，建议统一到女线写法。
- **`ui.inputConfig` SFW／NSFW**：SFW 侧 `SELECT`／`START` 未中文化，NSFW 侧作「选择／开始」——P10-0106／P10-0107。
- 已核对**一致**的同文条目：`ui.data.f_GameOverAreaC`／`m_GameOverAreaC`；`ui.card.CosmoCardDwarf.desc`、`CosmoCardRedbull.desc` 的 sfw／nsfw 两份（差异只在原文行尾补白）；Bigbold／Dwarf／Omegobin／Wyvern `needs` 四行一套；Omegobin `affinity` 两版；`save` 两版代号表。
- 其余「同源不同译」经全批比对仅 `---WARNING---` 一处（两条仅居中空格数不同），属排版装置，未报。

## 五、待核项（本路未提案，交主代理）

1. **`ui.end.Tier3`（SCe4ec9ed41c0f22c8）拼装模板**：`YOU'RE A`／`RANK`／`*!` 三段模板 + 称号（`WOW! SPEEDY!`／`HOTSHOT`／`NATURAL`）的显示顺序与占位规则无法从工单确定；`NATURAL ! !`→`天生的高手！ !` 若称号并列，则「高手」与 `HOTSHOT` 撞词，若为备选称号则不算撞词；全角「！」与半角「 !」混排也缺工单依据。需要引擎侧模板证据才能定案。
2. **卡面标题对齐空格**：`DWARF    <FAUNA>`→`矮人  <动物>`（4 空格→2）、`ENELYE   <ALPHA>`→`恩莉耶  <阿尔法>`（3 空格→2）、`PIGOBIN  <ALPHA>`→`猪哥布林  <阿尔法>`（2 空格维持）、`STARKILL <ALPHA>`→`星杀 <阿尔法>`（1 空格维持）。参照摘录要求「对齐空格原样保留」，但恩莉耶恢复 3 空格会到 17 列（16 列上限），矮人恢复 4 空格为 14 列则未超；两者是否该恢复需列宽实测。
3. **feral／knot 的卡面写法**：R9 已落地 `feral＝野兽`、`knot＝肉结`，`ui.card.CosmoCardDwarf.desc` 与 `CosmoCardWerehund.desc` 作「四足兽形犬科」「结已充血」「类似结的」，取的是生物学说明写法。本路未提案（改动会与已落地术语冲突，但也可能是卡面语域豁免）。
4. **P10-0106／P10-0107 的方向**：若裁决「菜单键名一律保留英文」，则须反向统一 NSFW 侧两处与 `input.xinput` 一处；两条发现成对处理。
5. **P10-0103 的取舍**：14 段结构下「！」只能落在最后一段，本路把断点移到「大方地\|看见自己」以保住「分神」完整；若认为感叹号独占一行可接受，可只取「分了\|神」合并这一处。

## 六、未覆盖项与本工单不能证明的东西

- **未覆盖**：本 part 之外的 `patchDictionary/navmap` 其余 Area（Area0／AreaC／AreaH／TestArea）不在工单内，跨侧一致性只在 AreaA 上验证过，不能外推到全表；`batch-10-part02/03` 的 `ui.*` 条目、`MauserHints*` 根均不在本 part。
- **不能证明（实机层）**：未启动游戏、未做构建与 17 步回归（按派单要求）。所有关于「不挤爆版面」的结论都是按容器上限（卡面 16 列、资料书 224px／3 行、剧情框 12px／240px）静态推算的，行宽、折行、居中装置与分页的真实渲染未留证；`ui.end.Tier3` 的模板、`confirmCheat` 的键显示顺序同理。
- **不能证明（语料层）**：`BIGBOLD1/2` 未本地化属参照摘录记载的已知缺口；`FENFEN` 中文名、`LIGHTTAZER`、引号体例（`“”`／`'…'`）未终裁，本路一律不提案；`SLAVER→奴隶贩子`、`DOGGY DOOR→幼犬门`、`BOP→拍拍`、`BOUNCY BOON→会弹的好处` 等写法在本 part 内无同批反证，均记 retain 而非「已证正确」。
- 三条提案（P10-0101／0103／0105）属 C 级打磨，不涉及语义、条件、施受或揭示顺序；四条 B 级提案（P10-0102／0104／0106／0107）均为同一 UI 组件或男女两版之间的内部不一致，未新增剧情、口吻或术语新造。
