# batch-06-part01 精校审校报告（雄猫道具与商店线 第 1／4 部分）

**校对路线**：双路精校之 Gemini 独立轨  
**基线版本**：`localization/builds/r9-polish-candidate13`（已并入 batch-01~04 及 batch-05 全三部分）  
**审核范围**：`TomcatItems` root（共 65 场，434 物理行，正文工单 1,518 行）

---

## 一、输入与阅读覆盖

- **工单正文**：`localization/editorial/r9-polish/batch-06-part01/orders/batch-06-part01.reader.md`（共 1,518 行）
- **结构化输入**：`localization/editorial/r9-polish/batch-06-part01/orders/batch-06-part01.json`（65 场，434 物理行，含 100 个既有合句空行）
- **实际阅读情况**：使用 `read` 分 6 段完整阅读完毕，无跳读、无抽样、无截断。每段阅读后即时落地检出的 issue 与 coverage 记录。
- **场景覆盖统计**：
  - 总场景数：**65 场**
  - 全覆盖产物：`localization/editorial/r9-polish/batch-06-part01/gemini/coverage.jsonl`（65 行，每场一行）
  - 发现问题场景数（`issues_found`）：**4 场**
  - 判定保留场景数（`retain`）：**61 场**
  - 存疑场景数（`needs_evidence`）：**0 场**

---

## 二、发现总数与等级分布

全批共检出并提出 **4 条** 精校发现与提案（编号 `P06a-101` ～ `P06a-104`），详细记录于 `localization/editorial/r9-polish/batch-06-part01/gemini/findings.jsonl`。

### 1. 严重程度分布
- **A 类（按键名保护与玩法教学）**：**1 条**
  - `P06a-104`（`SCde8682ffd4c1a8db`）：组合按键 `UP+ATTACK` 错误意译为汉字「按“UP”+“攻击”」，破坏按键硬保护与玩法操作指示。统一纠正为 `UP+ATTACK`。
- **B 类（结构缺陷与术语规范）**：**3 条**
  - `P06a-101`（`SCcf94f585c1e0205e`）：残留未译英文全大写戏仿绰号 `PUPLOCK`，音译修正为「帕普洛克船长」，消除结构缺陷。
  - `P06a-102`（`SC77c24f0ada1e4704`）：残留旧译「狗头人」，按 R9 已落地术语规范纠正为「科博德」。
  - `P06a-103`（`SC5e0cdd319089fe83`）：残留旧译「狗头人」，按 R9 已落地术语规范纠正为「科博德」。
- **C 类（风格润色与轻微微调）**：**0 条**（遵循精校原则，无确凿硬伤不改动）
- **needs_evidence**：**0 条**

### 2. 按 Root 归组分布
| Root 分组 | 场景数 | 发现条数 | 发现 ID 及级别 |
| --- | --- | --- | --- |
| `TomcatItems.CosmoCard` | 1 | 0 | - |
| `TomcatItems.DoggyHead` | 2 | 0 | - |
| `TomcatItems.ElfHead` | 1 | 0 | - |
| `TomcatItems.FakeDrumstick` | 2 | 0 | - |
| `TomcatItems.FakeTea` | 2 | 0 | - |
| `TomcatItems.IceCola` | 1 | 0 | - |
| `TomcatItems.JudoBody` | 2 | 0 | - |
| `TomcatItems.JudoHead` | 1 | 0 | - |
| `TomcatItems.KoboHead` | 1 | 0 | - |
| `TomcatItems.MapData02` | 1 | 0 | - |
| `TomcatItems.MapDataANorth2` | 1 | 0 | - |
| `TomcatItems.MapDataASouth2` | 1 | 0 | - |
| `TomcatItems.MapDataB1` | 1 | 0 | - |
| `TomcatItems.MapDataCEast` | 1 | 0 | - |
| `TomcatItems.MapDataE` | 1 | 0 | - |
| `TomcatItems.Pickaxe` | 1 | 0 | - |
| `TomcatItems.PirateHead` | 2 | 1 | P06a-101 (B) |
| `TomcatItems.PsyCoffee` | 1 | 0 | - |
| `TomcatItems.ShipShield` | 2 | 0 | - |
| `TomcatItems.SpecialAnklet` | 1 | 0 | - |
| `TomcatItems.SpecialBrace` | 1 | 0 | - |
| `TomcatItems.SpecialBuckler` | 2 | 0 | - |
| `TomcatItems.SpecialFap` | 1 | 0 | - |
| `TomcatItems.SpecialKeycard0` | 1 | 0 | - |
| `TomcatItems.SpecialKeycard4` | 1 | 0 | - |
| `TomcatItems.SpecialLeftmark` | 2 | 1 | P06a-102 (B) |
| `TomcatItems.SpecialPsycards` | 2 | 0 | - |
| `TomcatItems.SpecialTorch` | 1 | 0 | - |
| `TomcatItems.StatCheese` | 2 | 0 | - |
| `TomcatItems.StatCream` | 3 | 1 | P06a-103 (B) |
| `TomcatItems.StatFishtaco` | 2 | 0 | - |
| `TomcatItems.StatMelon` | 1 | 0 | - |
| `TomcatItems.StatNut` | 2 | 0 | - |
| `TomcatItems.StatPretzel` | 1 | 0 | - |
| `TomcatItems.Statcoin` | 1 | 0 | - |
| `TomcatItems.TazerRapier` | 1 | 0 | - |
| `TomcatItems.TazerTrainee` | 1 | 0 | - |
| `TomcatItems.ThrowKnife` | 1 | 0 | - |
| `TomcatItems.TribalBody` | 3 | 0 | - |
| `TomcatItems.TribalHead` | 1 | 0 | - |
| `TomcatItems.UpgradeChip` | 1 | 0 | - |
| `TomcatItems.VitHam` | 1 | 0 | - |
| `TomcatItems.VitMeat` | 2 | 0 | - |
| `TomcatItems.Vitamin` | 1 | 0 | - |
| `TomcatItems.ZenerCircle` | 1 | 1 | P06a-104 (A) |
| `TomcatItems.ZenerSquare` | 1 | 0 | - |
| `TomcatItems.ZenerWaves` | 2 | 0 | - |
| **合计** | **65** | **4** | **A: 1, B: 3** |

---

## 三、高风险段与查证说明

1. **按键名称保护（`UP+ATTACK`）**：
   - 在 `SCde8682ffd4c1a8db` 中，当前译文将组合按键拆分并汉化为 `按“UP”+“攻击”就能发动`。这不仅违反了工单第四节第 4 条关于按键名和保留标记不改的硬约束，且与 R9 在 batch-02、batch-04 多个批次中确立的全局既有基准严重冲突。玩家在游戏中若根据汉字寻找按键将引发困惑，必须统一修正为英文原词 `UP+ATTACK`。
2. **术语落地闭环（`KOBOLD / Kobo` → `科博德`）**：
   - 依据 ORDER.md 第四节第 48 条及 reference-excerpt 第五节，`Kobo＝科博德／KOBOLD 的「狗头人」改「科博德」` 是已裁决落地的硬性规则。本批在 `SC77c24f0ada1e4704` 和 `SC5e0cdd319089fe83` 检出两处漏改残留，均已予以纠正。
3. **已裁决留置项的不动原则**：
   - `Jakov's Obscura Crystal`（`SCa75f9bf643dc1302`）：当前译文作「雅科夫的Obscura水晶」。经查证 R3 人名裁决台账（`NAME:Jakov`），明确规定「只改人名部分为雅科夫，不借此重命名 Obscura 或道具功能」，属于既有生效裁决，本路坚决不予变动。
   - `torch`（`SC48a4bc82fca232b0`）：雄猫台词中「波苏习惯叫它torch」，系利用英式英语 torch（手电）与美式 flashlight 造成的语言幽默梗，R2 及后续批次均保持留置，不作单点修改。
   - `Fenfen`（`SC278181acbd1aa2e3`）：当前译文「机械Fenfen」，全库统一保留英文名称，不新造中文名。
   - `lighttazer`（`SCae76be512589a7df`）：当前译作「光电击枪」，符合 reference-excerpt 第三节「未终裁，三种写法并存，不要单点改」的口径要求，保留现状。

---

## 四、男女两版的不一致清单与合理保留

本批涵盖多组男女线（`datadf` 与 `datadm`）同类道具的对比场景，经连读确认其差异均属原作者刻意安排的性格与情节分歧，非翻译漂移，均判定为合理保留：
- **`TomcatItems.DoggyHead`**：
  - 女线（`SC2be09e8483c914fb`）：Yiffany 关心时髦度，雄猫吐槽颜色亮红且没有铃铛，Yiffany 强调潜行实用性。
  - 男线（`SCe17ae1d4176d49ff`）：雄猫赞时髦结实，Yiffai 傲娇反驳「我只是没得选才戴着的……才不是喜欢这种东西」，展现小男生特有的别扭感。
- **`TomcatItems.PirateHead`**：
  - 女线 NSFW（`SC31281e1f7d7bb273`）：海盗角色扮演调情，Yiffany 幻想着被关进禁闭室后「船长身上只戴着三角帽进来」，引发雄猫惊呼。
  - 男线 SFW（`SCcf94f585c1e0205e`）：Yiffai 怀念小时候当太空海盗的童年梦想，自称「帕普洛克船长（Captain Puplock）」。
- **`TomcatItems.StatCream`**：
  - 女线 NSFW（`SC8ed015a4cd151b1f`）：Yiffany 称赞蜥蜴奶油「浓稠绵滑还热乎」，并讽刺某些人被罚坐办公室。
  - 男线 NSFW（`SCc47dff4af8e62e7c`）：Yiffai 单纯询问要不要带回给雄猫，雄猫嫌弃直言「蜥蜴不是哺乳动物」，毛鼠出面打圆场说回总部后安排两性异形培训课。
- **`TomcatItems.TribalBody`**：
  - 男线（`SC64e07efc93477031` / `SC6e4d979cdf3f0678`）：Yiffai 兴奋于战服「能保护我还能让大家看到我的屁股（SFW版为觉得我很酷）」。
  - 女线（`SC852279e1d4f46a57`）：Yiffany 则从纯特工实战角度评估战服适应性，雄猫嘱咐留给异星考古部。

---

## 五、未能证明的事项

1. **容器折行与视觉溢出**：本报告所提提案基于字符数与每行 20 个全角汉字（240px / 12px 字体）的理论上限推算。所有修改后的物理行正文长度均在 14~26 字之间，安全控制在每页 3 行以内；但游戏引擎底层位图字体的具体 kerning 及排版渲染仍未做实机上屏测试。
2. **合句空行的引擎渲染消费**：本批 100 个 `current` 为空的 ROW 均属引擎逻辑合句的 tail 行，静态文本已确认完整表达全句语义，但未验证在所有 libGDX 运行时对话框中是否产生多余空帧翻页。
