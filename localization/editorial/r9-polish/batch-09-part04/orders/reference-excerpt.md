# batch-09 参照摘录（区域场景与条件分支）

各区域（`AreaA`～`AreaH`）的临时对白：`_Macsen*` 是麦森、`_Prison*` 是监狱段、`_Slaver*` 是奴隶贩子段、`_Cellar` 是地窖，另有 `_Shared` 结尾的共用句、`Queen`、`Gitgud`、`Proto_*`、`Test_*`。本批共 1,597 行，拆成 4 个 part 出工单。定向摘录自 R1 参照库与游戏内词典。

## 一、这类文本的特点

1. **场景碎、每场只有两三行**：一批两百多个场景，每个场景是玩家走到某处触发的一小段。上下句常常跨场景不连续，**不要拿隔壁场景的句子去顺这一场**。
2. **`text: `／`lang(Fox): `／`lang(HardFox): ` 前缀**：冒号加一个空格是前缀，提案原样保留。`CONTROL` 行是脚本指令，不改、不提案、不算漏译。
3. **`ZH:` 为空的 ROW 是合句尾行**：不报漏译、不填充；合句硬粘成病句要报。
4. **`_Prison*` 与 `_Slaver*` 是拘禁与买卖段落**：含成人向与暴力内容，照原文尺度处理，不净化也不加码。

## 二、谁在说话

- **麦森（Macsen）**：`_Macsen*` 段落里来回喊话的人，语速快、爱插科打诨。
- **波苏（Bossu）**：无线电指挥官。
- **雄猫（Tomcat）／毛鼠（Mauser）**：支援位。
- **主角**：伊吠（Yiffai，男线）／伊吠妮（Yiffany，女线）。
- `_Slaver*` 段落里的贩子是反派，语气粗鄙；不要写成主角的口吻。

## 三、术语（中文一侧照 `datav/dictionary.json` 的条目名）

| 英文 | 中文 |
| --- | --- |
| Agent | 特工 |
| KOBOLD／Kobo | 科博德 |
| SPIKER／DRILLER／BLOCKER／HOPPER／FLAMER／SQUEAKER／SWIPER／BARKER／BUMPER | 刺虫／钻探者／阻挡者／跳跃者／喷火者／吱吱怪／挥爪／吠犬／弹跳机 |
| HOOKSHOT／H. BRACE／BUCKLER | 钩爪／超能护腕／小圆盾 |
| Cosmohelm／Cosmosuit | 宇宙头盔／宇宙服 |
| LECT | LECT（大写，两侧留半角空格） |
| P.A.W. | P.A.W.（带点） |
| Traeh／Starkill／Enelye | Traeh／星杀／恩莉耶 |
| UP+ATTACK／DOWN+JUMP／SELECT | 原样保留，**按键名不改** |
| council | 议会 |

术语改动**必须给出处**：要指出依据在哪一行，不能只写「按术语表」。

## 四、容器与结构限制

- 剧情框 12px、240px 折行、每页 3 行；单行正文尽量不超过约 20 个全角字。
- 提案不得让任何行由 ≤3 行折行变成 >3 行。
- `current` 为空的 ROW：不报漏译、不填充。

## 五、已裁决、不得重提

- R3 人名全套；R2 的 agent＝特工、torch＝手电；R6 的 Bumper＝弹跳机。
- R9 已落地：无线电／安保门／竖井网／`UP+ATTACK`／Kobo＝科博德／Cosmohelm＝宇宙头盔／Cosmosuit＝宇宙服／council＝议会／feral＝野兽／knot＝肉结／nubs＝凸粒。
- 门卡等级那句：`ON THEM` 指**门**，等级标在门上，不要再改成「卡上所标」。

## 六、本批已知不报的类型

- 原文逐字加空格的排版镜像；**英文原行本身行尾带空格的，中文行尾空格是镜像**（英文没有、中文多出来的才是缺陷；判据是 `catalog/units.jsonl` 的 `source`，不是 `occurrences.trailing_ws`）。
- 原文跨行断词处的连字符（`o-`／`-hey` 这类）。
- 引号体例（`“”` 与 `「」` 并存）、CJK 与拉丁间距体例：全局待裁，本批不统一。
- LIGHTTAZER 中文名：未终裁，**不要提案改它**。

## 七、本批不可外推

- 不因场景碎就每场补一句原文没有的过渡语。
- 不把反派写成主角的口吻，也不把主角写成反派。
- 不替场景补原文没有的演出指令或台词。
