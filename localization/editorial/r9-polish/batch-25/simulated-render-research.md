# 模拟渲染研究：把游戏跑到某一对话时刻

目标是把「游戏运行到那一帧」的画面渲染出来，而不是画一个框叠文字。这份记录把
**已证实**与**仍是推测**分开写。

## 一、结论摘要

| 问题 | 结论 | 状态 |
| --- | --- | --- |
| 素材在哪 | 全在 `patch.pak`，无需外部 `cosmo-assets` | **已证实** |
| 场景帧怎么拼 | `slices.json` 给切片 ID 列表，按序贴 256×16 横带成 256×224 | **已证实**（出图） |
| 字幕几何 | `drawX=8`、`drawY=54`、行距 16，首行 PNG top=169+yoffset | **已证实**（字节码 + 截图互印） |
| 物品说明走哪个容器 | **无线电 150px**，不是故事框 240px | **已证实**（调用链 + 类字节） |
| 物品说明的背景 | UI 图集 `CosmoCodecMenuBG`，256×192 | **已证实** |
| 能否 headless 跑游戏 | 未评估 | **未做** |
| 最终窗口坐标 | 只到 256×224 内部目标，外层合成未做 | **未做** |

## 二、素材与结构（已证实）

`patch.pak` 里每个演出场景是一组六个条目：

```
script   vsn/<n-3>   演出脚本：fadein(1.0,4): SpriteName / text: 台词
slices   vsn/<n-2>   {"动画名": [[切片ID, ...], ...]}，每帧 14 个切片
manifest vsn/<n-1>   dirName 与文件哈希
timing   vsn/<n>     {"动画名": {"delays": [...], "loop": bool}}
atlas    vsn/<n+1>   scene.png 4096×1024 切片图集（文本格式）
page     vsn/<n+2>   那张 4096×1024 的 PNG
```

一帧的拼法：`slices[动画名][帧号]` 是 14 个切片 ID，第 k 个对应 y=k×16 那一条
256×16 横带，从 page PNG 的 `i_<ID>_slice` 区域裁出贴上。ID `0` 是空带。

全局 UI 图集：`dataq/5`（atlas 文本）+ `dataq/6`（PNG）。候选 54 是 **4096×6144**，
原版是 4096×4096——页高扩展过，所以**不能套原版的 xy 去裁候选的图**。实测多出来的
2048 高度里只有 2 个区域。

## 三、字幕几何（已证实）

### 字节码证据

`PRG/jo` 里三个常量：

| 字节码 | 含义 |
| --- | --- |
| `bipush 16` + `imul` + `isub` | 行距 **16** |
| `bipush 8` + `imul` + `iadd` | 中文 x 偏移 **8** |
| `bipush 40` + `isub` | 垂直 **-40** |

`PRG/jl` 的原点：`It.a(2)=16`、`It.b(6)=54`。
`PRG/StoryFont12.draw` 的中文分支：`bipush 8` + `Math.subtractExact(II)`，再减 8。

于是 `drawX = 16-8 = 8`、`drawY = 54-8 = 46`；进入绘制时行 i 的 drawY 为 `54-16*i`。

### 换算到 PNG 顶部坐标

256×224 的 y-up 目标，字形四边形顶边：

```
top = 224 - (drawY + 1) + FNT.yoffset
```

行 i（`drawY = 54-16*i`）得 `top = 169 + 16*i + yoffset`。首字还要加字体
padding 1px。

### 交叉印证

`story12.fnt` 自身：`lineHeight=16`、`base=8`、`padding=1,1,1,1`，汉字字形 12×12、
`yoffset=0`。与上面的 16 行距、169 首行完全对得上。

真实截图 `research/intro-05.png`（784×711，画布自 y=32 起、缩放 3.06×）量出的
文字带是 **y=161..173**，即首行 top=161 = 169-8，正好是中文那 8px 偏移。

**两个独立来源一致**，这条不再是猜的。

## 四、物品说明走无线电（已证实，且推翻旧结论）

旧文档按「这批是对话 → 走 240px 故事框」验收，**错了**。反编译调用链：

```
PRG/JB  （常量池含 "TomcatItems"，作为字符串键传进 aEg 构造器）
  → PRG/JM  （显示 CosmoCodecMenuBG + 双头像）
    → PRG/JQ
      → PRG/JR
        → DialogueWrap.radio   （150px / bbc2 10px / 每行 15 汉字）
```

逐环核验（`class` 字节里是否含下一环的引用）：

| 类 | 引用 | 结果 |
| --- | --- | --- |
| `PRG/JM` | `PRG/JQ` | True |
| `PRG/JQ` | `PRG/JR` | True |
| `PRG/JR` | `DialogueWrap` | True |
| `PRG/JB` | `TomcatItems` | True |

96 行里 **72 行**（`<TomcatItems.*>` / `<BossuDex.*>` 下）走 150px 无线电。
按故事框量的「92→35」对它们不成立；无线电实测 **74→72**。

另外 `all.ds` 的条目（`Area0_Fenfen.Hello` 这类）**不被任何 `vsn` 脚本引用**，
是游戏按「区域 + 角色 + 话题」查表的独立系统。

## 五、物品说明界面用到的素材（已证实）

| 元素 | 区域 | 尺寸 |
| --- | --- | --- |
| 背景 | `CosmoCodecMenuBG` `xy=1392,3000` | 256×192 |
| 双头像 | `PortraitBossuDefault` / `PortraitBossuTalk` `xy=1880,120` 等 | 32×32 |
| 边框 | `FrameNinePatch` `xy=2040,3432` | 24×24（九宫格拉伸） |

`TextBox` 不是精灵名——它是 `PRG/amG` 的命令名，不能因为 atlas 里没有它就推断
「程序化九宫格」。边框用的是 `FrameNinePatch`。

## 六、仍缺的（未做）

### 6.1 shader：源码读到了，但配色对不上真实截图

`vsn_term_shade.frag` 的完整逻辑（`texture_size` 由 `PRG/jl` 设为 `(256.0, 224.0)`）：

- 红通道非零 → 文字像素，涂 `inner_color` = `(0.972, 0.721, 0.0)` = **(248,184,0)**；
- 恰好是 `(0,0,1)` → 标记像素，涂 `glow_color` = `(0.313, 0.188, 0.0)` = **(80,48,0)**；
- 其余像素取左、右、上三个邻居；不在每 8 行的扫描线空档时再取下方；任一邻居有红
  就给 `glow_color`，否则全透明。

已用 Python 复算并出图（`out/layout/scenes/shaded-sample.png`）。

**但配色与真实截图不符，这是必须写明的矛盾：**

| 颜色 | 来源 | 真实截图里出现次数 |
| --- | --- | ---: |
| `(248,184,0)` | shader `inner_color` | **0** |
| `(80,48,0)` | shader `glow_color` | **0**（但场景 PNG 里有，是画师画的） |
| `(255,155,0)` | 截图实测 | 8273 |
| `(232,176,0)` | 截图实测 | 8207 |
| `(88,57,0)` | 截图实测 | 7458 |

`research/intro-05.png` 是真实截图，里面**完全没有**这两个 shader 常量。所以那张画面
没有经过 `vsn_term_shade`。而且 `(255,155,0)` 不在 jar 的任何 PNG 里，说明它是运行时
生成的——最可能是调色板重映射（`vsn_fade` + 某个 `*LUT.png`，jar 里有 16 个 LUT）。

**这条路径没有复现。** 所以现在有两种颜色可用、但都不能当定论：

- `INK_DRAWN` = shader 常量，适合「过了 vsn_term_shade 的图层」；
- `INK_CAPTURED` = 截图实测值，适合「匹配开场那张的观感」。

`asset_render.py` 两个都保留并注明，避免把某一个当成唯一正确答案。

### 6.2 时间状态

`fade(9, 0, 1)`、`fadein(0.5, 4)` 这类命令有动画进度。取哪一帧（首帧？淡入完成？）
没有确定，现工具固定取帧 0。

### 6.3 外层合成

出图是 256×224 内部目标。真实窗口还有缩放、黑边、letterbox。未做。

### 6.4 headless 可行性

未评估。需要判断 libGDX 有无离屏 framebuffer 路径能在无窗口下跑完整管线。
本会话没有做这个实验（不启动游戏是硬边界）。

## 七、可执行方案

按保真度分三级，每级都是完整可用的产物。

### 第一级：布局级（现在就能做，已完成）

素材：`patch.pak` 切片 + 候选 jar 字模。
文本：引擎真实入口 `SubtitleLayout.pages(text, 28)`（**第二参数是 UTF-16 列数 28，
不是像素宽 240**）、`DialogueWrap.storyPages`、`DialogueWrap.pages(q=20,150px)`。
几何：上文字节码推导值。

能回答：分页对不对、行首有没有标点、字挤不挤、断词在哪。
不能回答：颜色是否被 shader 改过、动画进度、窗口缩放。

工具：`scene_frame.py` / `asset_render.py` / `real_scene.py` / `scene_render.py`。
产出：`out/layout/scenes/` 77 张。

### 第二级：像素级（差 shader）

在合成后对文字层跑 `vsn_term_shade.frag` 的等价运算（这是纯片元函数，可读源码用
Python 复算：按 `texture_size` 做扫描线调制）。需要先确定 `texture_size` uniform
的真实取值。

风险：shader 逻辑若依赖 GPU 浮点行为，Python 复算会有细微差异。要如实标注。

### 第三级：等价实机（要离屏跑真引擎）

用 libGDX 的离屏 framebuffer 起一个无窗口实例，喂同一批资源，让**真实渲染管线**
出图。这是唯一能称「等价」的路径。代价是搭一套 headless 启动，且必须解决
无窗口下 GL 上下文的问题（可能需 EGL/OSMesa 或虚拟显示）。

前置判断（可先做）：`cosmobreeder-multi.jar` 是否用 `LwjglApplication` 而非
`HeadlessApplication`；有无 `Framebuffer` 用法可复用。

## 八、给后续维护者的提醒

1. **别再用像素宽当 q**。`SubtitleLayout.pages` 与 `formatCapped` 的第二参数是
   UTF-16 列数上限。240/150/220 是函数内部的像素常量。
2. **候选与原版的 UI 图集页高不同**（6144 vs 4096）。裁图必须用候选的 atlas 坐标。
3. **容器归属要按调用链查**，不能按「这是对话所以走故事框」推断。`TomcatItems`
   这类条目走无线电。
4. **字幕几何有两条独立证据**（字节码与截图），改动前先核这两处是否仍然一致。
