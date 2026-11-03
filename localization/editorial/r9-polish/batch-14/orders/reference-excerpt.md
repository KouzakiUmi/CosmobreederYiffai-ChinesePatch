# batch-14 参照摘录（补漏 21 场：AreaA 提示／The0／Area0 旁白）

## 一、这类文本的特点

1. **本批是三种文本**：`MauserHints_AreaA.*`（毛鼠对旧矿井、传送门、反重力踝环的提示）、`The0.*`（芯片贩子 The0 的推销与吐槽，会模仿玩家的口吻）、`Area0_Macsen1／MacsenBar／Prison1`（麦森的无线电嘱托与旁白）。
2. **提示的物件、方向与先后顺序就是玩法信息**：改错指代（把「上面的门」写成「下面的门」）、改丢条件（删掉"如果"）、改掉动作（撬锁→打开）都按 A 级处理；只能往更准改，不能改出新条件。
3. **`MauserHints_AreaA` 已由 batch-01 精校过**，不在本批范围内；本批不要重提那批的措辞。
4. **先查 R8 的谜题提示裁决**（`localization/editorial/r8-puzzle/README.md`）：那是谜题夹具的提示措辞，已裁决过的写法不要翻案；冲突时以 R8 为准并在 `note` 写明。
5. **提示框很窄**：改写后长度不得明显超过原文，也不能靠加标点凑语气（原文没有感叹号就别加）。
6. 场景名带 `noamendfreq`、`no select`、`override` 一类后缀，是脚本选择条件，不改、不提案、不算漏译。

## 二、谁在说话

- **毛鼠（Mauser）**：战败提示的主讲，语速快、爱自嘲、会拿自己开涮。
- **波苏（Bossu）**：无线电指挥官，讲解时更简短、更命令式。
- **主角**：伊吠（Yiffai，男线）／伊吠妮（Yiffany，女线）。
- 本批没有星杀或干扰广播；`MauserHints*` 只有毛鼠一个说话人，偶尔以「麦森」称呼玩家。

## 三、术语（中文一侧照既有裁决与 `datav/dictionary.json` 条目名）

| 英文 | 中文 | 依据 |
| --- | --- | --- |
| Mauser／Tomcat／Bossu | 毛鼠／雄猫／波苏 | R3 |
| Yiffai／Yiffany | 伊吠／伊吠妮 | R3 |
| Starkill | 星杀 | R3 |
| ClassicBigbold／Bigbold | 大壮兽（BIGBOLD 条目） | 词典条目名，库内 4 处 |
| ClassicWerehund／Werehund | 狼犬 | 词典条目名，库内 5 处 |
| ClassicWerepup／Werepup | 狼崽 | 词典条目名，库内 5 处 |
| ClassicBossRedbull／Redbull | 红牛 | 词典条目名，库内 6 处 |
| ClassicPigobin／Pigobin | 猪哥布林 | 词典条目名，库内 5 处 |
| ClassicEnelye／Enelye | 恩莉耶 | R3／词典条目名，库内 5 处 |
| UP+ATK | 原样保留，**按键名不改** | 既定体例 |
| LECT | LECT（大写，两侧留半角空格） | 既定体例 |

`THAT LARGE BOLD MAKES IT CLEAR` 里的 `BOLD` 是 `BIGBOLD` 被脚本截断后的残形，**不是新术语**；此处当前译作「那只巨大的 BOLD 会……」把英文残形留在了中文里。术语改动**必须给出处**（条目名或同 root 另一场），不能只写「按术语表」。

## 四、容器与结构限制

- 剧情框 12px、240px 折行、每页 3 行；单行正文尽量不超过约 20 个全角字。
- 提案不得让任何行由 ≤3 行折行变成 >3 行。
- `current` 为空的 ROW：不报漏译、不填充。

## 五、已裁决、不得重提

- R3 人名全套；R2 的 agent＝特工、torch＝手电；R6 的 Bumper＝弹跳机；R8 谜题提示措辞；R9 已落地项（无线电／安保门／竖井网／`UP+ATTACK`／Kobo＝科博德／Cosmohelm＝宇宙头盔／Cosmosuit＝宇宙服／council＝议会／feral＝野兽／knot＝肉结／nubs＝凸粒）。
- 失真字幕体例本身**待全库终裁**：不要把它当成本批可以自行统一的事。

## 六、本批已知不报的类型

- 原文逐字加空格的排版镜像；英文原行本身行尾带空格的，中文行尾空格是镜像（判据是 `catalog/units.jsonl` 的 `source`，不是 `occurrences.trailing_ws`）。
- 原文跨行断词处的连字符与噪声断句（`o-`／`-hey`、`SSSH`／`KKZZT`）。
- 引号体例（`“”` 与 `「」` 并存）、CJK 与拉丁间距体例：全局待裁，本批不统一。
- `LIGHTTAZER` 中文名：未终裁，**不要提案改它**。
- 全大写不等于吼叫：提示语全大写是体例，不因大写加叹号。

## 七、本批不可外推

- 不因提示语短就补原文没有的鼓励句、吐槽或演出指令。
- 不把失真广播"修通顺"：噪声是原设计，抹平等于改风格。
- 不把男女两版合并成一套措辞，也不把姐姐／哥哥亲属关系错置。

## 八、本批特别注意

1. **同 root 的其余场次已由 batch-01 落地**：`MauserHints_AreaA` 同族 14 场、`The0` 同族 28 场、`Area0_*` 同族 75 场都已审过。术语、称呼与语气以那批为准；两边不一致时报「跨场不一致」并给出两处 `row_id`。
2. `The0.Feral`（`[BARK?!]`）、`The0.Slime`（`[GLOOP?!]`）、`The0.Kobo`（`[HIYA KOBO!]`）是 The0 把玩家当成兽形／史莱姆／科博时的调侃，`BARK`／`GLOOP` 是拟声，不是漏译。
3. `Area0_Macsen1.Talk.hornets` 与 `Area0_MacsenBar.Talk.secretcode3` 是麦森的教学／彩蛋台词，`SELECT` 等按键名保留英文。
4. 多数场是合句：第一行有中文、后续行 `current` 为空，空行不报漏译。
