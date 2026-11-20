# Cosmobreeder Yiffai 汉化技术报告

> **2026-10-21 字体实现复核：** 后续补丁制作请以[字体渲染逆向与补丁指南](<字体渲染逆向与补丁指南.md>)为入口，包含原归档指纹、类/字段/方法映射、完整缓存绘制链和精确字节码证据。新增确认：VSN 有独立的 16 像素行步进；地图通过 SN 接口调用居中辅助；dingbats 有真实消费方；终端着色器存在 8 像素周期采样。下文历史实验不等于全 UI 排版验收。

> **2026-10-18 接手复核更新：中文字幕已在隔离测试副本正常显示，VSN 正文规则补丁已通过真实 JVM 测试。**
> 实心字块的根因是新字库透明 RGB 与游戏混合模式不匹配，不是已证实的 128×128 硬限制。以下第 6–8 节保留为历史排查记录，其推测和下一步建议已被新证据取代。
> **最新结论、截图、67 份有效 VSN 回归结果与复现步骤见 [接手研究结论](<../research/接手研究结论.md>)。** Steam 原安装未改，尚未完成全量翻译。

> 目标：把游戏内文本全部替换为简体中文，并让中文能正常渲染。
> 本报告只记录**可复现的实验结论**；未验证的内容明确标为「待验证」。

---

## 0. 当前状态摘要

| 环节 | 状态 | 说明 |
|---|---|---|
| 资源解包 / 重打包 | ✅ 完成 | 加解密与归档重建验证通过 |
| 文本提取 / 回写 | ✅ 完成 | 对话 `.ds`、VSN `.vsn`、UI `dictionary.json`，往返字节级一致 |
| 工作表 | ✅ 完成 | 6,845 条待译单元，含宽度预算与术语表 |
| 字体架构分析 | 静态主链已复核 | 见[字体实现指南](<字体渲染逆向与补丁指南.md>)；全 UI 排版未验收 |
| 字体文件可控性 | ✅ 已证明 | 把任意字母重映射到任意字形**成功**（见 §5.3） |
| **CJK 字形显示** | ✅ **隔离实机验证通过** | 修正透明 RGB 后中文正常显示；旧 §6 保留为历史记录 |
| 文本替换 | ✅ 技术冒烟通过 / ⏸ 全量待译 | 正文 Unicode 规则补丁通过，67 份有效 VSN 原文回归通过 |

---

## 1. 游戏结构

| 项 | 值 |
|---|---|
| 启动器 | `CosmobreederYiffai.exe`（40KB，负责注入 `lib/x64/*.dll`） |
| 主程序 | `cosmobreeder-multi.jar`（44.8MB，`Main-Class: co.kemosho.cosmo.Main`，ReleaseTag `1.0.5_full`） |
| 运行时 | 自带 Temurin JRE 17.0.6 |
| 技术栈 | Java 17 + libGDX（**整个 libGDX 被混淆进 `PRG/*`**）+ Scala 3 + FMOD + Steamworks4J |
| 混淆 | ProGuard，7,736 类；字符串常量**未加密** |
| 补丁层 | `patch.pak`（12.5MB，普通 ZIP），jar 的叠加层，`dataq/` 内容与 jar **不同** |

> ⚠️ 必须用 `CosmobreederYiffai.exe` 启动；直接 `java -jar` 会因 `fmodstudio.dll` 未注入而失败。

---

## 2. 资源容器与加密（已破解）

```
<group>/0     加密 JSON 索引 {"sprites.png":6, "sprites.atlas":5, ...}
<group>/<n>   加密资源 blob
```

**Salsa20/20**，布局 `nonce(8) ‖ ciphertext ‖ key(32)`；counter 从 1 开始，每 64 字节 +1，rotl 7/9/13/18。对称，可用随机 key 重写。文本全程 UTF-8。

---

## 3. 文本系统

| 类型 | 载体 | 规模 |
|---|---|---|
| 对话 | `datadf/all.ds`（女）、`datadm/all.ds`（男） | 987 条目 / 2,894–2,912 单元 |
| 剧情字幕 | `vsn/*/script.vsn` | 106 脚本 / 2,245 单元 |
| UI / 物品 / 单位 | `datav/dictionary.json` | 1,012 键 / 813 单元 |
| 代码内字符串 | `.class` 常量池 | 847 候选 |

VSN 全部是**内联文本**（`text:` 2108 行、`lang(...)` 272、`auto(...)` 8），没有「key → 字典」写法。

---

## 4. 字体架构（历史摘要，完整实现见新指南）

### 4.1 绘制链路

1. `PRG/iF.a(PRG/Yh)` 注册三款字体：

```java
"default"  ← new BitmapFont(Gdx.files.internal("bbc2.fnt"),    <atlas region "bbc2">, false)
"classic"  ← new BitmapFont(Gdx.files.internal("classic.fnt"), <atlas region "classic">, false)
"dingbats" ← new BitmapFont(Gdx.files.internal("dingbats.fnt"),<atlas region "dingbats">, false)
```

2. `PRG/Yg` 消费字体注册表：`Yq.f().apply(name)` → `Yq$b` → `BitmapFont`。上层还包括 `SN` 接口调用、`jo` 字幕定位及 `Id` 逐字/字体选择，不能据此认定全部排版只在 Yg。
3. 默认字体名硬编码为 `"default"`（`Yg.a()/b()/c()/d()`、`PRG/amS$a`）。

**证据**：把 `PRG/iF` 里的 `"classic.fnt"` 等长替换成 `"zzzzzzz.fnt"`，游戏立刻报 `PRG.ats: File not found: zzzzzzz.fnt` —— 证明这条注册路径确实在运行时执行。

### 4.2 `.fnt` 存活表

| 文件 | 状态 |
|---|---|
| `bbc2.fnt` | **活（= default）** |
| [classic 定义](<font-evidence/snapshot/classic.fnt.txt>) / [dingbats 定义](<font-evidence/snapshot/dingbats.fnt.txt>) | 均注册；`Id` 确实传入 dingbats，旧“无调用方”结论撤回；classic 场景仍待核验 |
| `st.fnt` | **死**：`Yq.<init>` 急加载（删掉会崩），但 `Yq.o` 字段只写不读 |
| `st2x / nes / japanese / dmg_numbers / lsans-15` | 死（零引用） |

### 4.3 字形像素来自 atlas region

`PRG/arp`（BitmapFont）用 `arp(FileHandle, TextureRegion, boolean)` 构造，**传入的 region 作为 page 纹理**，忽略 `.fnt` 的 `page file=`。

UV 公式（反汇编 `PRG/arp$a.a(arp$b, arI)` 与上游 libGDX 一致）：

```
u = region.u + srcX / texture.getWidth()
v = region.v + srcY / texture.getHeight()
```

### 4.4 两个界面不同来源

| 界面 | 文字来源 |
|---|---|
| Pretitle 引导页（"THIS GAME IS BEST PLAYED…"） | **预渲染位图**（`ClassicPretitleGamepad` 等 256×224 图） |
| VSN 字幕 / 游戏正文 | `bbc2.fnt` + `sprites.png` 的 `bbc2` region |

> Pretitle 顶部 `THIS SOFTWARE IS FOR ADULTS ONLY` 是**闪烁**的，单帧截图不可靠，需连拍取亮帧。

---

## 5. 字体改造（做到哪一步）

### 5.1 已实现

```
sprites.png   4096×4096 -> 4096×6144   （原美术保留在顶部）
region bbc2   128×128   -> 2048×2048 @ (0,4096)
bbc2.fnt      97 字形/128/lineHeight 8 -> 7,489 字形/2048/lineHeight 13/base 10
```

脚本：`build_cjkfont.py` + `apply_font_singlepage.py`（不需要改任何 class，region 名保持 `bbc2`）。

### 5.2 已验证

- 英文字幕渲染完全正常（`sp_13.png`），`[]` 高亮标记正常
- 两个归档的 `sprites.png` 在目标坐标上确实是「中」「一」等字形（逐像素核对）

### 5.3 关键正面证据：字体完全可控

把 `.fnt` 里字母 `e` 的坐标改成字母 `z` 的坐标后，字幕变成：

```
bzcomz a driving forcz for
spacz zxploration.
```

把 `A` 也改过去 → `ORGzNIZzTION`。

**这证明**：`.fnt` 被正确解析、坐标生效、UV 映射正常、字形像素从 atlas 正确取得。

---

## 6. 卡点一：CJK 字形采样失败（未定位）

### 6.1 现象

| 目标坐标 | 结果 |
|---|---|
| ASCII 区任意字形（x,y < 128） | ✅ 正常 |
| (106, 37) | ✅ 正常（字母 z） |
| (1, 137) | ⚠️ 几乎不可见（该字形本身是顿号） |
| (1, 179) / (1, 221) / (491, 543) | ❌ 实心方块 |
| (1471, 137) | ❌ 实心方块 |

**有效范围看起来是 128×128**（正好等于原始 `bbc2` region 尺寸）。

### 6.2 已排除

| 假设 | 实验 | 结果 |
|---|---|---|
| 图片数据错 | 逐像素核对两个归档的 `sprites.png` | ❌ 数据正确 |
| atlas 修改未生效 | 把 `bbc2` 的 `xy` 改成 (0,0) | ❌ 生效（字幕变成精灵碎块） |
| `size:`/`orig:` 未写入 | 打印两个归档的 `bbc2` 块 | ❌ 均为 2048×2048 |
| 字段名映射错 | 反汇编 `arE/arF/arv/arH/ary` | ❌ 映射正确（`size`→`eI/fI`） |
| 字形被裁剪 | 修改 `arp$a` 两处裁剪分支（`ifle`→恒真，等长栈平衡补丁） | ❌ 补丁通过校验、游戏不崩，但仍是方块 |
| 新页方案 | 增加 atlas 第二页 | ❌ 页被解析，但字体不绑定该页 |

### 6.3 尚未排除

- 运行时 `region.getRegionWidth()/getRegionHeight()` 的真实值
- `glyph.srcX/srcY` 在 `setGlyphRegion` 之前是否被其它逻辑改写过
- 纹理实际尺寸是否真的是 4096×6144

**建议下一步**：写一个 `-javaagent` 在 `PRG/arp$a.a(arp$b, arI)` 入口打印 region 尺寸与 glyph 坐标（JRE 自带 `java` 支持 agent，无需 JDK）。

---

## 7. 卡点二：VSN 脚本解析器拒绝非 ASCII

```
java.lang.Exception: Parse Error, Position 6:15, found "组织已成为推动太空探索…"
	at PRG.auG$b.e(PRG:54)
	at PRG.amV.a(PRG:174)
```

- 中文放进 `[]` 内 → 报错
- 中文移到 `[]` 外 → **同样报错**
- `dictionary.json` 无 `vsn.*` 键，脚本也无 key 语法

解析链：`amV.a(String, acU, afT)` → `auL` 包装 → `ava.a(...)` → 组合子 → 失败时 `auG$b.e()`。字符判定在 `ava`/`auI`/`auG$c` 层，尚未定位。

---

## 8. 后续路径（按推荐顺序）

### A. 运行时插桩确认 region 尺寸（最小成本、最高价值）

写 Java agent 打印 `region.getRegionWidth()/Height()` 与 `glyph.srcX/u`。这一步能直接判定 §6 的根因，避免继续盲试。

### B. 若 region 尺寸确为 128：patch 掉尺寸来源

可能位置：`PRG/art.a(art$b)` 构造 `art$a` 时传的 w/h，或 `PRG/arI.a(IIII)` 的 `rI/sI`。改动需要重排字节码或使用等长替换。

### C. 若 region 尺寸正常：查 UV 与纹理

核对 `PRG/ark`（Texture）的实际宽高，确认 PNG 是否被按 4096×4096 加载。

### D. VSN 字符集

定位 `ava`/`auI`/`auG$c` 中的字符判定后，把上界放大。需要 `javaclass.py` 扩展为可写回（当前只解析）。

### E. 可立刻推进、不依赖以上卡点

`dictionary.json`（813 条 UI/物品/单位）是 UTF-8 JSON，**不经过 VSN 解析器**，可先翻译并用游戏内菜单验证中文渲染链路（前提是 §6 解决）。

### F. Pretitle 位图

`ClassicPretitleGamepad` / `ClassicPretitleLogo` / `ClassicPretitleFMOD` 三张 256×224 图需走图片本地化流程（`game-image-localization`）。

---

## 9. 工具与产物

| 文件 | 用途 |
|---|---|
| `javaclass.py` | 纯 Python class 解析 + 反汇编（机器无 JDK） |
| `explore.py` | `m <类>` / `d <类>` 查看方法、反汇编 |
| `cosmo_codec.py` | Salsa20 加解密 |
| `extract.py` | 解包两个归档 |
| `textfmt.py` | `.ds` / `.vsn` 解析回写（往返一致） |
| `make_worksheet.py` | 生成 `translation/*.csv` 与 `worksheet.xlsx` |
| `validate.py` | 标记符、边缘空格、宽度预算、字形覆盖校验 |
| `build_cjkfont.py` | 构建 `build/bbc2.fnt` + `build/cjkfont.png` |
| `apply_font_singlepage.py` | **把字体装进两个归档（当前方案）** |
| `apply_font.py` | 旧「新增 atlas 页」方案（已废弃，保留对照） |
| `check_atlas.py` | 按 libGDX 规则静态校验 atlas |
| `patch_vsn_test.py` | 往 VSN 塞中文的冒烟脚本 |
| `cap2.ps1` | 按 PID 抓窗口截图 |
| `repack.py` | 翻译打包（字体注入部分仍是 `st.*`，需更新） |

产物：`translation/`（工作表）、`build/`（字体）、`backup/`（原始归档备份）。

---

## 10. 实验方法论（黑盒必备）

1. **按 PID 截图**：`cap2.ps1 -TargetPid`，按进程名会抓错窗口
2. **连拍取亮帧**：Pretitle 有闪烁
3. **正交探针**：改步进（是否用这个字体）、改坐标（字形来自哪）、改页 `format` 为非法（页是否被解析）
4. **等长字节码补丁**：`ifle`→恒真时要把操作数改成 `iconst_0` + nop 填充，否则触发 `Inconsistent stackmap frames`
5. **静态模拟**：`check_atlas.py` 提前抓页/region 归属错误

---

## 11. 已知限制

1. **历史字块问题已修复，端到端中文字幕在隔离副本成功**；全游戏菜单、多行排版与对话仍待专项验收
2. Pretitle 引导页是位图，字体方案无法翻译
3. 行距 8→13，对话框可容纳行数减少
4. 803 条代码内字符串需改 class 常量池
5. `testgame*` / `tg_*` 测试副本约 **5GB**，随时可删
