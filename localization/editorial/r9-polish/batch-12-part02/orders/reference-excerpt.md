# batch-12 参照摘录（未覆盖的词典与任务日志条目）

## 一、这类文本的特点

1. **本批是前十一批没覆盖到的那部分界面文本**：311 场 `datav/dictionary.json` 条目（生物、敌人、道具、状态、结局等级等短标签，488 行）＋162 场 `datay/scripts_pack.json` 条目（任务日志的 header／subject／locationName／text 与两个商店 `displayName`）。共 473 场／650 行，拆 3 个 part 出工单。
2. **场景名（`root`）是内部键**：`ClassicBulber`、`Bomb`、`SpecialHookshot`、`AnomalyGamma` 这类键名不是玩家看到的东西，一律不改、不提案；要改的是值（`current`）。
3. **值是短标签，长度就是版面**：词典标签与任务日志字段共用固定列宽，改写后长度**不得超过英文原文**（只能同长或更短）。不要为了"顺口"加字，也不要加解释性括号。
4. **同一英文在两侧各一份**：`datav/dictionary.json` 在 jar 与 pak 里各有一个版本，同一标签可能一侧已译、一侧没译或写法不同。这类发现要写明两侧 `row_id`；只改一侧会造成游戏内前后不一致。
5. **任务日志 `text` 场是占位样例行**：原文形如 `Line 1    | Line 2    | …`，中文侧是 `第1行|第2行|…`。这是开发占位，与英文结构一致就记 `retain`，不重写、不"润色"、不补齐。
6. **任务日志的 header／subject／locationName 是面板上的一行**：`MISSION`、`ZERONIA`、`ACQUIRED ZENER STAR` 这类短句，按已落地写法统一（任务／任务名／地名后缀按现有写法）。
7. **商店 `displayName` 要与 `ui.item` 的物品名一致**：两处写法不同时报「跨 root 不一致」，把两处 `row_id` 都写出来。
8. 词典标签大量是**同一物种的多个变体**（`ClassicBigbold`／`ClassicBigboldEnemy`／`ClassicBigboldV2`），同一英文必须给同一中文；不一致时报 term，不要逐个"优化"。

## 二、谁在说话／名字

- 剧情与无线电里的说话人沿用既有裁决：麦森（Macsen）、波苏（Bossu，无线电指挥官）、雄猫（Tomcat）、毛鼠（Mauser）、主角伊吠（Yiffai，男线）／伊吠妮（Yiffany，女线）。
- 界面文本基本无说话人；`ui.data` 里的名字是资料卡名录，不是台词，不要给它们加口吻。
- **既有写法（本批当前行，按库内条数核对）**：

| 英文 | 中文 | 库内条数 |
| --- | --- | --- |
| ZERONIA | 泽罗尼亚 | 20 |
| AYSKAMMR | 艾斯卡姆尔 | 12 |
| SCEAFYA | 斯凯菲亚 | 8 |
| REDBULL | 红牛 | 6 |
| ENELYE | 恩莉耶 | 5 |
| PIGOBIN | 猪哥布林 | 5 |
| STARKILL | 星杀 | 5 |
| WEREHUND | 狼犬 | 5 |
| WEREPUP | 狼崽 | 5 |
| BIGBOLD | 大壮兽 | 4 |
| DWARF | 矮人 | 4 |
| SQUEAKER | 吱吱怪 | 3 |
| KOBOLD | 科博德 | 2 |
| SWIPER | 挥爪 | 2 |
| BARKER | 吠犬 | 2 |
| WYVERN | 双足飞龙 | 2 |
| ELF | 精灵 | 2 |
| GHOSTER | 幽灵者 | 1 |

- **未定／保留原形，本批不动**：`TRAEH` 保留 `Traeh`（R3 裁决）；`SEVAW`→`Sevaw`、`ERAUQS`→`Erauqs` 当前为原形保留；`BIGBOLD1`／`BIGBOLD2` 仍有条目作 `BIGBOLD1/2` 未本地化，属已知缺口，本批只在能指出同类条目既有写法时提改动。`FENFEN` 中文名未定（库内 `Fenfen` 124 处、`芬芬` 1 处），**不要新造，也不要按一股改另一股**。

## 三、术语（中文一侧照 `datav/dictionary.json` 的条目名）

| 英文 | 中文 | 依据 |
| --- | --- | --- |
| Agent | 特工 | R2 裁决 |
| torch | 手电 | R2 裁决 |
| hookshot | 钩爪 | 词典条目名（batch-09-part02 已按此裁决） |
| DEPOT B | 仓库B | 词典条目名 |
| Cosmohelm／Cosmosuit | 宇宙头盔／宇宙服 | R9 已落地 |
| council | 议会 | R9 已落地 |
| COSMO CARD／COSMOCARDS | 宇宙卡牌 | 本批当前行 |
| SAVE STATION | 存档站 | 本批当前行 |
| CURRENT LOCATION | 当前位置 | 本批当前行 |
| FAUNA ENCLOSURES | 动物围栏 | 本批当前行 |
| SPACE ELEVATOR | 太空电梯 | 本批当前行 |
| AIRLOCK | 气闸 | 本批当前行 |
| SHIELD GENERATOR | 护盾发生器 | 本批当前行 |
| PSY CRYSTAL | 精神水晶 | 本批当前行 |
| ANOMALOUS SIGNAL | 异常信号 | 本批当前行 |
| CONTRABAND DETECTED | 探测到违禁品 | 本批当前行 |
| LARGE LIFEFORM DETECTED | 探测到大型生命体 | 本批当前行 |
| AGENT BEACON | 特工信标 | 本批当前行（`COSMO AGENT BEACON` 作「宇宙特工信标」） |
| SITE-TO-SITE TELEPAD | 站点传送台 | 本批当前行 |
| EXILE | 流放地 | 本批当前行 |
| LECT | LECT（大写，两侧留半角空格） | 既定体例 |
| P.A.W. | P.A.W.（带点） | 既定体例 |

术语改动**必须给出处**：要指出依据在哪一行／哪个条目，不能只写「按术语表」。

## 四、容器与结构限制

- 卡面 16 列 × 128px、≤15 行；数据书 224px、≤3 行；剧情框 12px、240px 折行、每页 3 行。
- 提案不得让任何单元由「行数够」变成「行数超」；`|` 段数改变等同于结构损坏。
- `current` 为空的 ROW：不报漏译、不填充。

## 五、已裁决、不得重提

- R3 人名全套；R2 的 agent＝特工、torch＝手电；R6 的 Bumper＝弹跳机；R8 谜题提示措辞；R9 已落地项（无线电／安保门／竖井网／`UP+ATTACK`／Kobo＝科博德／Cosmohelm＝宇宙头盔／Cosmosuit＝宇宙服／council＝议会／feral＝野兽／knot＝肉结／nubs＝凸粒）。
- **按键名不是术语**：`UP+ATK`、`TRIANGLE` 一类保留原样，不要译成中文键名。

## 六、本批已知不报的类型

- 原文逐字加空格的排版镜像；名单类行首行尾的居中空格。
- 英文原行本身行尾带空格的，中文行尾空格是镜像（判据是 `catalog/units.jsonl` 的 `source`，不是 `occurrences.trailing_ws`）。
- 引号体例（`“”` 与 `「」` 并存）、CJK 与拉丁间距体例：全局待裁，本批不统一。
- `LIGHTTAZER` 中文名：未终裁，**不要提案改它**。
- 全大写不等于吼叫：界面标签本来就是全大写，不因英文大写而加叹号或语气。

## 七、本批不可外推

- 不因界面短就补原文没有的说明句、提示语或语气词。
- 不为了「读起来顺」删掉标记、空格、坐标或按钮名。
- 不把资料卡名录里的名字改成剧情里的称呼（名录是名单，不是对话）。
