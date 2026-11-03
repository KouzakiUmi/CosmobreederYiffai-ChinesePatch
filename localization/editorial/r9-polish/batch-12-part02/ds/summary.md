# batch-12-part02 精校小结（本路提案）

## 一、输入与实际阅读

| 项 | 值 |
| --- | --- |
| 工单正文 | `orders/batch-12-part02.reader.md`，1,013 行（158 场、219 行 ROW） |
| 结构化数据 | `orders/batch-12-part02.json`，158 场 |
| 读取方式 | 分三段整读（行 1–340 / 341–680 / 681–1013），每段读完即追加该段 coverage 与 findings |
| 每段场数 | 60 / 58 / 40 |
| 实际读完 | **158 场（read_full，100%）**，219 行 ROW 全部连读 |
| 每段发现数 | 2 / 1 / 7 |

## 二、发现总数与分布

**10 条**：A 3 ／ B 5 ／ C 2 ／ needs_evidence 0。另有 148 场判 `retain`。

按类别：`term` 5、`meaning` 3、`format` 1、`idiom` 1。全部为 `status: proposal`。

| finding_id | root | 分级 | 类别 | 判点 |
| --- | --- | --- | --- | --- |
| P12-0201 | `/missionLog/female/6/header` | B | term | ACQUIRED 写法跨侧不一（已获取异常体／已获得异常／获得），统一为「获得异常体 ALPHA」 |
| P12-0202 | `/missionLog/{female/4,7,9, male/2,5,8}/text` | C | format | 占位 text 场中文末尾多出 3 个半角空格（英文 `source` 无尾随空格），删空格、其余不动 |
| P12-0203 | `ClassicKingbold` | A | meaning | KINGBOLD→「胆王」误译（bold 读作「胆大」），改「大壮兽王」（BIGBOLD＝大壮兽） |
| P12-0204 | `SpecialGeiger` | C | term | COMMUNICATE AND｜DETECT SECRETS! 两侧写法不同（通讯联络／通讯，并），以对仗写法统一 |
| P12-0205 | `SpecialRadio` | B | term | 按键名 SELECT 被译成「选择」，回退为 `按 (SELECT)｜进行通讯` |
| P12-0206 | `SpecialShoes` | B | term | 按键名 DOWN+JUMP 被译成「下+跳跃」，两侧统一到保留键名的写法 |
| P12-0207 | `StatMelon` | B | idiom | a good pair→「一对好货」不成搭配且丢双关，改「一对好瓜」（MELON＝瓜已落地） |
| P12-0208 | `StatPretzel` | A | meaning | TWISTED BREAD｜BAKED FRESH→「硬结打卷｜育得正好」整段误译，改「扭结面包｜新鲜出炉」 |
| P12-0209 | `TazerRapier` | A | meaning | RAPER（另侧源文 RAPIER）→「强奸者」误读，改「细剑」，与描述行及另一侧一致 |
| P12-0210 | `ZenerStar` | B | term | 词条「星星」与任务日志「泽纳星形」同一物品两处不同名，词条改「星形」 |

## 三、高风险连续段

1. **任务日志 header 的 ACQUIRED 家族**（`/missionLog/*/header`）：库内 14 行作「获得」，只有 ANOMALY 四条走「已获取异常体／已获得异常」两种写法。这一族是本批最容易只改一侧就造成新的不一致的地方（P12-0201 已把两侧 `row_id` 都写出）。
2. **占位 text 模板族**（`Lorem ipsum…` 与 `Line N | …`）：模板本身是开发占位，正文不该润色，但模板里带着与英文不一致的行尾空格（本批 6 行，库内同模板另有 10 行不在本批）。此处只按行尾空格判据处理，未动正文与 `|` 段数。
3. **按键名（`DOWN+JUMP`、`SELECT`、`UP+ATK`）**：同一按键在说明文本里保留英文、在物品说明里被译成中文键名（「下+跳跃」「(选择)」），是本批最集中的结构/体例风险点（P12-0204～0206）。
4. **词典 jar／pak 双份**：`TazerRapier` 两条的**英文源本身不同**（`RAPER` / `RAPIER`），中文因此分成「强奸者／细剑」。这类条目只按中文对齐不够，需两侧一起看（P12-0209）。
5. **Zener 部件命名**：词典侧 `星星/波浪/三角/方块/圆圈/十字`，任务日志侧 `星形/波/三角形/方形/圆形/十字`。本批只对「星星 vs 泽纳星形」提案（实际不同名），`波浪/波` 等同义差异未提案（P12-0210 note 已记录其余部件不在本批）。
6. **商店与物品名**：本批 158 场里没有 `displayName` 与 `ui.item` 的成对条目（库内 `displayName` 仅 `OLD JUNK` 两条，不在本批），因此「商店名与物品名一致」这一条本批只能声明**未适用**，不能证明两侧已一致。

## 四、两侧（sfw／nsfw、jar／pak、任务日志／词典）不一致清单

| 英文 | 本批一侧（row_id） | 另一侧（row_id） | 差异 | 处置 |
| --- | --- | --- | --- | --- |
| ACQUIRED ANOMALY ALPHA | `CAT:O8e693539f4176a2c26f8`（已获取异常体 ALPHA） | `CAT:O51cb2f4e2b75ec5d5388`（已获得异常 ALPHA） | 动词 + 名词都不同 | P12-0201，统一「获得异常体 ALPHA」 |
| COMMUNICATE AND｜DETECT SECRETS! | `SFWb5b657b5499b27ce4e15ff79`（通讯联络｜探测秘密！） | `CAT:O9d4031d64526ba4032e9`（通讯，并｜探测秘密！） | 连接词硬译 | P12-0204，以本侧为准 |
| PRESS (SELECT)｜TO COMMUNICATE | `CAT:Ob0ffde2b7cc35a20ba51`（按 (选择)｜进行通讯） | `SFW9c8e090c508293aaaf7d3076`（按(SELECT)｜进行通讯） | 键名译／不译 | P12-0205，回退 SELECT |
| DOWN+JUMP MID-｜AIR DIVEKICKS! | `CAT:O90d8f279d41f9619c1f6`（空中下+跳跃｜俯冲踢！） | `SFW083152e4179a990986277979`（空中按DOWN+JUMP｜使出俯冲踢！） | 键名译／不译 | P12-0206，统一到保留键名 |
| RAPER ／ RAPIER | `CAT:Oda01761b7ab029ed8329`（强奸者） | `SFWbb9a036fc151263a56b5e55f`（细剑） | 英文源拼写不同 → 中文误读 | P12-0209，统一「细剑」 |
| STAR ／ ACQUIRED ZENER STAR | `CAT:O6dab2711b737b0d5d952`（星星） | `CAT:O3b7a9cb0c1e4564a0470`（获得泽纳星形） | 同一物品两处不同名 | P12-0210，词条改「星形」 |
| WAVES ／ ACQUIRED ZENER WAVES | `CAT:Ob303708cc17dd79a2dcc`（波浪） | `CAT:O6c8c72674ecd9051df36`（获得泽纳波） | 同义不同形 | **未提案**（不造成误读） |
| FENFEN 系列 | `SFW8e386526313445bc13993663`（翻译项链） | `CAT:O94e5f06616f550a23c5e`（Fenfen的｜传统武器。）、`SFW6d386582d126a91285a276d7`（Fenfen神圣的｜羽饰帽） | 专名保留／省略 | **未提案**（8 字列宽放不下「Fenfen」＋名称，FENFEN 中文名未终裁） |

男／女线之间：`/missionLog/{male,female}/…` 的地名、字段名（泽罗尼亚／艾斯卡姆尔／斯凯菲亚／仓库B／总部／任务／活体样本）两侧写法完全一致，无待处理项；唯一分歧就是上表的 ANOMALY header。

## 五、未覆盖项与本工单不能证明的东西

**未覆盖（本批内）**：无——158 场全部 `read_full`，无 `partial`／`not_read`。

**未做／不能证明**：

1. **列宽未实测**：ORDER 要求「长度不得超过英文」，本路只按字符数（必要时按 CJK 双宽估算）核对，**没有渲染验证**卡面 16 列 × 128px、数据书 224px、每页 3 行等容器；提案中「同长或更短」的结论是字符级判断。
2. **词典双份未穷举**：只核到 `TazerRapier` 两侧英文源不同这一例；其余 300 余条词典条目是否存在「一侧已译、一侧未译」未逐条比对（本批外的条目不在范围内）。
3. **未执行构建、回归或实机**：未跑 `build_candidate.py` / `test_candidate.py`，未启动游戏，未写台账（`editorial_repairs.py` 的落地校验不在本工单内）。
4. **未核物理行**：ROW 的 `line`、前缀、`controls` 一行未改也未验证；提案只给完整物理行文本，`|` 段数与位置按工单现状保持。
5. **英文原文自身问题只记录不改**：`RAPER`、`DRUMSTIK`、`HEADRESS`、`S.POTION`、`FENFEN T`、`With ger ship downed` 等拼写/截断按硬约束原样保留，是否回填属上游归档裁决。
6. **按裁决未碰**：LIGHTTAZER 中文名、FENFEN 中文名、引号体例（`“”`／`「」`）、`Traeh`／`Sevaw`／`Erauqs` 现状；场景名（`ClassicBulber`、`Bomb`、`SpecialHookshot` 等内部键）一律不动、不提案。
7. **跨 root 命名未统一**：任务日志 header 保留拉丁 `ALPHA/BETA/GAMMA/OMICRON`，词典作「阿尔法／贝塔／伽马／奥密克戎」；词典 `圆圈/方块/三角` 与任务日志 `圆形/方形/三角形` 同样不齐。这两组涉及本批外条目，只在 note 记录，未提案。
8. **text 场末尾换行未动**：中文 text 值普遍以换行结尾、英文多数不以换行结尾，属库内既有存储约定；本批只处理「3 个半角空格」，未主张删换行，也未证明换行对渲染无影响。
9. **`needs_evidence` 为 0**：本批未遇到原文自相矛盾或说话人/触发条件存疑的行；ANOMALY header 的动词分歧是写法不统一（有 14 行同类可比），不按「原文矛盾」处理。
