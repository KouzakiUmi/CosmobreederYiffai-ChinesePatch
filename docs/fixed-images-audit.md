# `assets/fixed/` 4 张独立位图资产审计报告

> 2026-11-14 定位记录：四处待补位图变体的位置、两档差异和接入位置。原版切片是本地参考输入；当前构建使用[稀疏覆盖格式](workflows/images.md)。

## 一、结论摘要

1. **4 个目标全部位于图集精灵表内，不存在独立散装 PNG**。两个归档均为 ZIP 容器：`dataq/5` 解密后是 libGDX 文本图集（`.atlas`），`dataq/6` 解密后是 `sprites.png`（4096×4096 RGBA）。JAR 图集 6898 个区域，PAK 图集 7142 个区域；PAK 多出的 38 个名字全部是 `ClassicPrisoner*` 角色帧（NSFW 内容），**没有新增 UI 面板**。
2. **4 个目标与历史重绘清单中已有字段吻合**：它们位于已重绘区域或同名的待补变体，而不是全新资产。
   - `SUB MENU BESTIARY` / `-SELECT DATA TO VIEW BELOW-` → 区域 **CosmoSubData**（IMG-010，jar+patch 两行均已 redrawn）
   - `"A" KEY TO FLIP CARD` → 区域 **CardViewMenuBG** 的 **patch 变体**（IMG-001 patch 行含该 operation；jar 变体无此句）
   - `(L+R) ON GAMEPAD / OR (Q+E) ON KEYBOARD` + `TO ACCESS GAME CONFIGURATION` → 区域 **ClassicPretitleGamepad**（IMG-014，仅 jar 行）
   - `[R18]` + `ENTER CONFIG MENU WITH (Q)+(E) / OR (L SHOULDER) + (R SHOULDER)` → 区域 **CosmoSaveMenuBG** 的 **patch 变体**（IMG-008，含成人限定标记与配置入口提示）
3. **真正的缺口在变体覆盖**：`ClassicPretitleGamepad`（PAK 有 **2 个同名区域**）、`CardViewMenuBGTitle`（仅 jar 行）、`CosmoTitleData`（仅 jar 行）的 patch 变体在 manifest 中缺失；`ClassicPretitleFMOD`/`ClassicPretitleLogo`/`ClassicOptions*` 等区域未进 manifest（是否含烘焙文本未经图像核验，见 §六限制）。
4. **接入建议：扩展 `assets/images/manifest.json` + `optimized_images.py` 现有管线**，不需要新流水线。`A<hash>.png` 只是工作清单占位名，产物应复用 `assets/images/png|masks/` 命名规范。

## 二、物理来源定位

### 2.1 容器结构（两归档一致）

| 归档 | 条目 | 说明 |
| --- | --- | --- |
| `originals/cosmobreeder-multi.jar` | `dataq/0..7` | `dataq/5`=atlas 文本，`dataq/6`=sprites.png；`dataq/1` 为小 PNG，`dataq/3/4/7` 为其他加密资源 |
| `originals/patch.pak` | `dataq/0..7` + `vsn/`×404 + `datadf|datadm|datav` | 同上；`vsn/` 为演出脚本，无位图 |

解密走 `tools/lib/codec.py::decrypt_file`，图集解析走 `tools/lib/projectlib.py::parse_atlas`。JAR 散装根目录 PNG（`icon*.png`、`st*.png`、`japanese.png`、`blank16.png` 等）均为图标或 `.fnt` 字体页引用图，与 4 个目标无关；`.fnt` 引用的 `bbc2.png`/`classic.png`/`nes.png`/`dingbats.png` 等字体页不在根目录，属字体管线（`optimized_fonts.py`）范围。

### 2.2 图集规格

| 变体 | `dataq/5` 解密大小 | 区域数 | `dataq/6` sprites.png |
| --- | --- | --- | --- |
| jar（SFW） | 804,800 B | 6,898 | 4096×4096 RGBA |
| pak（NSFW） | 830,475 B | 7,142 | 4096×4096 RGBA |

PAK 重打包后**多数 UI 区域坐标全部变化**，同名区域须按各自 atlas 取 xy；像素哈希对比（RGBA 全图 SHA-256 前 16 位，见 `assets/fixed/sources.json`）：

- **像素完全一致**（jar=panks 同图）：`ClassicPretitleFMOD`、`ClassicPretitleLogo`、`ClassicOptionsCheatFrame`、`ClassicOptionsCheatWarning`、`ClassicOptionsConfirmWarning`、`CosmoItemMenuBG`、`CosmoMissionLogMenuBG`、`CosmoShopBG`、`CosmoGalleryBG`、`CosmoGalleryViewerBG`、`CosmoSubMapBG`、`CosmoSubMapV2BG`、`CardViewMenuFlipping`（全部帧）、`CosmoHUDUpdatedFlagDefault`（2 实例）
- **像素不同**（NSFW 重绘/改字）：`CosmoSubData`、`CosmoTitleData`、`CardViewMenuBG`、`CardViewMenuBGTitle`、`ClassicPretitleGamepad`（pak 有 2 个变体，均异于 jar）、`ClassicHUDBreedMenu`、`ClassicHUDSubBreed`、`CosmoCodecMenuBG`、`CosmoNameEntryMenuBG`、`CosmoSaveMenuBG`

### 2.3 类引用佐证（`PRG/*.class` 常量池）

| 类 | 引用区域 | 用途 |
| --- | --- | --- |
| `PRG/Iz` | `ClassicPreTitle`/`ClassicPretitleFMOD`/`ClassicPretitleGamepad`/`ClassicPretitleLogo` | 标题前置流程（L+R/Q+E 进入配置的提示屏） |
| `PRG/Jm` | `CardViewMenuBG`+`CardViewMenuBGTitle`+`CardViewMenuFlipping` | 宇宙卡查看器 |
| `PRG/Jn` | `CardViewMenuFlipping` | 翻卡动画帧 |
| `PRG/Kc` | `CosmoSubData`+`CosmoTitleData` | 数据/图鉴查看器（配 `ui.data.*`） |
| `PRG/Jt` | `ClassicOptionsCheatFrame`+`ClassicOptionsRedArrow` | 作弊码菜单框 |
| `PRG/LL$a/b/c` | `ClassicOptionsCheatWarning`/`ClassicOptionsConfirmWarning` | 选项警告对话框 |
| `PRG/LE/LF/LC` | 仅 `ui.inputConfig.*` 文本键 + `ClassicOptionsRedArrow` | **键位配置界面为字体/控件动态渲染，无烘焙面板位图** |
| `PRG/LG` | 仅 `ClassicOptionsRedArrow` + `ui.options.*` | 游戏配置菜单同上 |

## 三、4 个目标逐项定位

### 目标 1：`Ada8d2a93e89e1525cbf1.png`（键位配置页）

- 描述：键位配置标题 / 手柄与键盘组合提示。
- **首选来源：`ClassicPretitleGamepad`**（IMG-014）。manifest jar 行 operations 为 `'THIS GAME IS BEST PLAYED / WITH A CONTROL PAD'`、`'TO ACCESS GAME CONFIGURATION'`、`'PRESS (L+R) ON GAMEPAD / OR PRESS (Q+E) ON KEYBOARD'`——即"手柄+键盘组合提示 + 配置入口"。
- **备选：`CosmoTitleData`**（IMG-013 仅 jar 行，`SUB MENU MEMORIES` + `-SELECT DATA TO VIEW BELOW-`）或 `ClassicOptionsCheatFrame`（未进 manifest，`PRG/Jt` 作弊菜单框）。
- 注意：真正的键位编辑屏（`ui.inputConfig.*`）由 `LE/LF/LC` 用字体实时渲染，**图集内不存在独立"键位配置页"位图**；若目标指该屏，则其"位图"只是字体/控件合成结果，需走字体管线而非位图重绘。
- **置信度：中**。`ClassicPretitleGamepad` 证据最强，但与目标 4 语义相邻，需人工看图裁决。

### 目标 2：`A3ad10e4fc08b09e2bef4.png`（图鉴子菜单）

- 描述：`-SELECT DATA TO VIEW BELOW-` / `SUB MENU BESTIARY`。
- **来源：`CosmoSubData`**。IMG-010 patch 行 operations 逐字为 `'SUB MENU BESTIARY'` + `'-SELECT DATA TO VIEW BELOW-'`；jar 行同位置为 `'SUB MENU MEMORIES'`（SFW 版用词不同）。
- 坐标：jar `dataq/6` xy=[600,3176] 256×192；pak xy=[2184,3000] 256×192。
- **置信度：高**（字符串逐字命中）。manifest 已覆盖 jar+patch 两变体。

### 目标 3：`Acfb74ff046445762b007.png`（卡牌查看器提示）

- 描述：卡牌查看器标题与 `"A" KEY TO FLIP CARD`。
- **来源：`CardViewMenuBG` 的 patch 变体**。IMG-001 patch 行含 operation `"A" KEY TO FLIP CARD → 按「A」翻卡`（slot [168,1,250,16]）；同区 jar 行仅 `'COSMOCARD VIEWER'`——即翻卡提示**仅存在于 NSFW/PAK 版**，与"成人内容查看器"语义一致。
- 标题本体另见 `CardViewMenuBGTitle`（IMG-002 仅 jar 行；pak 同名区域像素不同 `e435e0d0…`，**patch 变体缺 manifest 行**）。
- 坐标：两变体 xy 均=[3432,3896] 256×192（pak 重打包后此区域恰好未挪位）。
- **置信度：高**（operation 逐字命中）。

### 目标 4：`A4b6160b4569cc8b87687.png`（成人限定与配置入口）

- 描述：成人限定横幅、`L+R` / `Q+E` 键位提示与配置入口。
- **首选来源：`CosmoSaveMenuBG` patch 变体**（IMG-008 patch 行）：`'PERSONAL ARCHIVE WRITER [R18]'`（成人限定标记）+ `'DEFAULT KEY SETTINGS: / ENTER CONFIG MENU WITH (Q)+(E) / OR (L SHOULDER) + (R SHOULDER)'`——"[R18] 横幅 + Q+E/L+R 配置入口"逐字命中。
- **备选：`ClassicPretitleGamepad` pak 第 2 实例**（xy=[2376,3664]，pxsha=`168ac249…`，与 jar/pak#1 均不同；pak 重打包后占据 jar 中 `ClassicPretitleLogo` 的旧位置，疑为 NSFW 版前置屏）。
- 坐标：`CosmoSaveMenuBG` jar xy=[536,112]、pak xy=[3240,2736]，均 256×224。
- **置信度：中高**。`[R18]`+配置入口组合最贴合"成人限定"描述；若实机所见为开场前置屏而非存档菜单，则应取 `ClassicPretitleGamepad` pak#2。

## 四、`assets/fixed/` 现有产物

已清理为 25 张候选原图 + `sources.json`（每张含 region/variant/xy/size/RGBA-SHA256/PNG-SHA256/所在归档条目）：

- 目标 2：`CosmoSubData__jar/pak`
- 目标 3：`CardViewMenuBG__jar/pak`、`CardViewMenuBGTitle__jar/pak`（标题上下文）
- 目标 4：`CosmoSaveMenuBG__jar/pak`、`ClassicPretitleGamepad__jar/pak/pak_2`、`ClassicPretitleFMOD/Logo`（前置屏上下文）
- 目标 1 候选：`CosmoTitleData__jar/pak`、`ClassicOptionsCheatFrame/Warning/ConfirmWarning`（选项对话框上下文）、`CosmoNameEntryMenuBG__jar/pak`

全部为 RGBA、原始尺寸未缩放，直接裁自 `dataq/6` 解密图。命名规则 `<Region>__<variant>[_n]__<x>_<y>_<w>x<h>.png`。

## 五、接入方案建议

1. **走 `assets/images/manifest.json` 扩展**，不新建流水线：`optimized_images.py` 已支持 jar/patch 双变体、xy/size 定位、白名单掩码、逐 operation 槽位重绘。`A<hash>.png` 工作项应落成 manifest `replacements` 新行（或补齐缺失变体行），最终 PNG 命名沿用 `<variant>__<logical>__<index>__<ordinal>.png`。
2. **需补的 manifest 变体行**（按本审计坐标）：
   - `ClassicPretitleGamepad` patch ×2：xy=[2112,3664] 与 [2376,3664]（pak atlas 中同名双区域，ordinal 需按 `parse_atlas` 顺序实测）
   - `CardViewMenuBGTitle` patch：xy=[1056,3664]
   - `CosmoTitleData` patch：xy=[2448,3200]
   - `CosmoSubData`/`CardViewMenuBG`/`CosmoSaveMenuBG` patch 行已存在，确认其 operation 是否覆盖全部目标文本（如 `SUB MENU MEMORIES` jar 版、`[R18]` patch 版）
3. **掩码**：重绘沿用"文字槽 erase box + foreground/background + raster mask"模式；`ClassicPretitleGamepad` pak#2 与 `CardViewMenuBGTitle` patch 为新增变体，需新建掩码。
4. **若目标 1 实为键位编辑屏**：该屏无位图资产，应改走字体管线（`bbc2.fnt`/`classic.fnt` 等已由 `optimized_fonts.py` 覆盖），不应占用 `assets/fixed/` 位图工单。

## 六、限制与未决

- **本会话模型无图像输入**，`read_image` 不可用；所有"该区域含某英文文本"的结论来自 manifest `operations[].english` 逐字记录与类常量池引用，**未经像素级 OCR/目检复核**。建议接入前由可看图环境抽查 `assets/fixed/` 内 25 张原图与上述映射。
- 目标 1（`Ada8d2a93`）与目标 4（`A4b6160b`）在 `ClassicPretitleGamepad`/`CosmoSaveMenuBG`/`CosmoTitleData` 之间存在语义重叠，最终归属需以实机截图或可看图复核裁决。
- `ClassicPretitleFMOD`/`ClassicPretitleLogo`/`ClassicTitlescreen*`/`ClassicOptions*`/`ClassicHUDAchievementPopup` 等区域未进 manifest，其是否含需本地化的烘焙英文文本**未排除**（像素哈希显示 FMOD/Logo 两变体一致，Options 系列两变体一致）。
- PAK `ClassicPretitleGamepad` 双实例的具体差异（是否成人横幅版）未经图像比对确认。
- 审计未修改 `tools/`、`src/`、`tl_work/`、`review/`；写入仅限 `assets/fixed/` 与本文档。
