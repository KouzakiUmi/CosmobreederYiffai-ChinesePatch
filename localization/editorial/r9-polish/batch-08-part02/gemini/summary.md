# batch-08-part02 审校报告（Gemini 路）

## 一、审校概况与覆盖

- **输入工单**：
  - `localization/editorial/r9-polish/batch-08-part02/orders/batch-08-part02.reader.md`（共 1,891 物理行）
  - `localization/editorial/r9-polish/batch-08-part02/orders/batch-08-part02.json`（共 16 场场景，470 行 ROW）
- **审校执行**：按 200 行分段读取推进，全批 16 场、470 行 ROW 100% 完整审校（`read_status: read_full`），无截断、无遗漏。
- **产出文件**：
  - `localization/editorial/r9-polish/batch-08-part02/gemini/findings.jsonl`（1 条发现，连续编号 `P08-0201`）
  - `localization/editorial/r9-polish/batch-08-part02/gemini/coverage.jsonl`（16 场记录，每场列全 `row_ids`）
  - `localization/editorial/r9-polish/batch-08-part02/gemini/summary.md`（本报告）

---

## 二、发现统计与分布

### 1. 分级统计

| 分级 | 数量 | 占比 | 说明 |
| :--- | :---: | :---: | :--- |
| **A** | 0 | 0.0% | 无误译、漏译、施受倒错或结构损坏 |
| **B** | 1 | 100.0% | `P08-0201`（未译英文实词/术语统一定名） |
| **C** | 0 | 0.0% | 无单纯润色凑数项 |
| **needs_evidence** | 0 | 0.0% | 无原作者逻辑存疑项 |
| **合计** | **1** | **100.0%** | |

### 2. 发现清单与归组

- **场景**：`SC74fa82aa35846705` (`vsn/f_ClassicSqueakerBoss/script.vsn`)
  - **finding_id**：`P08-0201`
  - **row_ids**：`["CAT:O3a34ed7c9ce9097944e7"]` (L18)
  - **severity**：`B` / **category**：`term`
  - **原文**：`It's my standard issue Cosmohelm! I've been looking for this since I landed!`
  - **当前行**：`text: 这就是我的标配Cosmohelm！我一落地就在找它！`
  - **提案行**：`text: 这就是我的标配宇宙头盔！我一落地就在找它！`
  - **依据**：`Cosmohelm` 残留未译英文实词。在 `datav/dictionary.json#CosmoHead.desc` 中条目定名为“宇宙头盔”；在 `datadm/all.ds:4157` 中 Tomcat 对白亦有“再把这套衣服配上宇宙头盔”的配对说明。应统一定名为“宇宙头盔”。字符数约 22 字，完全在安全宽度范围内。

---

## 三、判定保留（retain）的场次清单（15 场）

除 `SC74fa82aa35846705` 外，其余 15 场全部判定保留（`result: retain`）：

1. **`SC5b08efc340c04910`** (`vsn/f_AgentF01/script.vsn`, 39 rows, nsfw)：特工讲述与吠犬（barker）群相遇及深入交流。双关语“外星舔语（exolingus）”翻译出彩，术语吠犬使用准确，合句连贯，判定保留。
2. **`SC293a09cd1a3e883d`** (`vsn/f_AgentF08/script.vsn`, 47 rows, nsfw)：特工维克斯（Vickers）自述海盗女王幻想破灭及被科博德捕获经历。科博德（Kobo）定名准确，打断连字符镜像处理恰当，判定保留。
3. **`SCc7795e6405707551`** (`vsn/f_AgentF0B/script.vsn`, 26 rows, nsfw)：新人特工戴眼镜自述遭遇，口吻生动活泼，合句自然，判定保留。
4. **`SCcf4e44e2dba4cfa6`** (`vsn/f_AgentFZ5/script.vsn`, 19 rows, nsfw)：Fenfen 灵能记忆场景，女线版。保留“让心神向内”，Traeh 与 Fenfen 保留拉丁，图托恩（Tutone）符合词典，判定保留。
5. **`SCc035945720439679`** (`vsn/f_AgentFZ6/script.vsn`, 22 rows, sfw)：Fenfen 理事会陷落背景，女线版。文风典雅凝练，判定保留。
6. **`SC6c92dcf306eb4565`** (`vsn/f_ClassicBigboldV2/script.vsn`, 81 rows, nsfw)：经典首领战演出。大蜥蜴、超能护腕（hyper bracer）、科博德（kobofolks）、宇宙育种者等术语完全符合规范，高潮演出节奏极佳，判定保留。
7. **`SC19b93e1f465c6352`** (`vsn/f_ClassicBossRedbull/script.vsn`, 20 rows, sfw)：红牛首领战过场，伊吠妮（Yiffany）自述口吻强硬自信，判定保留。
8. **`SCfc42c34b7707b552`** (`vsn/f_ClassicWerepup/script.vsn`, 14 rows, sfw)：女线小狼犬关卡。伊吠妮大姐姐口吻温柔自然，1级门卡（Level 1 Keycard）术语准确，判定保留。
9. **`SC3b2e2ad5011ee43d`** (`vsn/m_AgentM07/script.vsn`, 41 rows, nsfw)：卡拉卡尔特工自述，结巴、双足飞龙、宇宙靴（Cosmoshoes）、俯冲踢（DIVEKICK）及矮人狗铁砧双关传神到位，判定保留。
10. **`SC3c96e35204cd3dcc`** (`vsn/m_AgentM08/script.vsn`, 54 rows, nsfw)：公狐狸特工牢房反客为主记录，亨舍尔（Henschel）角色背景与“上位特工（top agent）”性双关巧妙吻合，F.A.P.保留原样，判定保留。
11. **`SC7de8c86ddb5e03bc`** (`vsn/m_AgentMZ2/script.vsn`, 22 rows, nsfw)：Fenfen 灵能记忆场景，男线版。保留“将心神转向内在”，与女线分别保持内部一致，判定保留。
12. **`SCc2e08d1dfc6c98fd`** (`vsn/m_AgentMZ3/script.vsn`, 19 rows, nsfw)：Fenfen 反抗军崛起历史，男线版。词藻沉雄有力，判定保留。
13. **`SCbe1fe03046dd63f0`** (`vsn/m_AgentMZ6/script.vsn`, 22 rows, nsfw)：Fenfen 理事会陷落背景，男线版。男线心神转向内部一致，判定保留。
14. **`SCb30b71ae110c4cbc`** (`vsn/m_ClassicPigobinV3/script.vsn`, 16 rows, sfw)：猪哥布林古风古语对白，古雅口吻（汝、吾、尔）与现代主角口语对比分明，判定保留。
15. **`SCfd5dbc6a5b6f9666`** (`vsn/m_ClassicWerepup/script.vsn`, 17 rows, sfw)：男线小狼犬关卡。伊吠（Yiffai）自称“伊吠大叔（Uncle Yiffai）”，长辈调侃口吻生动自然，判定保留。

---

## 四、高风险连续段核验

1. **合句与空行断点**：
   本批包含多处既有合句（如两条英文合并为一条完整中文）。经逐一核对，所有 `ZH:` 为空的行均为合句尾行，整句意思完整无遗漏，未破坏句子结构或信息揭示顺序。
2. **成人向自述与角色口吻**：
   特工记录（AgentF/AgentM）包含大量第一人称自述与成人向内容。现译既未删减弱化其原本的肉欲与诙谐（如各种 sex 双关、叫声、锁结 tie、身体部位），亦未恶意加码或拔高语域，各角色性格（大条、傲娇、怯懦结巴、粗犷自傲）区分度清晰。
3. **保护标记与按键保留**：
   全场所有 `<3`、`>:3`、`PPPC`、`F.A.P.`、`Traeh`、`Fenfen` 等保护标记原样保留无损坏。

---

## 五、男女两版的不一致清单

1. **小狼犬关卡（Werepup）**：
   - **女线 `SCfc42c34b7707b552`**（`vsn/f_ClassicWerepup`）：
     - 伊吠妮自称“救星”，对小狗崽是亲切鼓励的平辈/大姐姐视角（“要是遇到麻烦，就叫一声，我会冲过来救你的！”、“你真的在帮助自己的星球！”）。
   - **男线 `SCfd5dbc6a5b6f9666`**（`vsn/m_ClassicWerepup`）：
     - 伊吠自称“伊吠大叔（Uncle Yiffai）”，称小狼犬为“小侄子（nephew）”，自居豪迈长辈视角（“你的伊吠大叔就在附近，尽管汪汪叫着求救！我会跑过来的。”、“伊吠大叔哪还能找到比你更棒的小侄子？”）。
   - **判定**：原文男女性格与人设差异所致，译文精准还原了各自语气，**判定各自保留，互不对齐**。
2. **Fenfen 记忆开场白（Turn your mind inward）**：
   - **女线 `SCcf4e44e2dba4cfa6` / `SCc035945720439679`**：`让心神向内，去见证塑造这片土地的那些往事……`
   - **男线 `SC7de8c86ddb5e03bc` / `SCc2e08d1dfc6c98fd` / `SCbe1fe03046dd63f0`**：`将心神转向内在，见证塑造这片土地的往事……`
   - **判定**：已知库内事实，男女两版各自内部高度统一，**判定各自保留，禁止机械拉平**。

---

## 六、未覆盖项与本工单不能证明的事项

1. **实际字宽折行渲染**：
   本批剧情框规格为 240px、12px 字体，每页最多 3 行（约 20 全角字/行）。虽然全部译文行长均处于安全范围，但特定带有长标点或拉丁缩写（如 `Cosmohelm` 替换后的 `宇宙头盔`、`P.A.W.` 等）在游戏引擎实际运行时的断行与文本框底边表现，仍需以实机渲染回归为准。
2. **全局引号体例**：
   游戏文本中全角双引号 `“”` 与直角引号 `「」` 的混用属于全局待裁规范，本工单严格遵循“不报引号体例”约束，未作变动。
