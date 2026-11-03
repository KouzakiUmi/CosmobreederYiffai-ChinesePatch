# 真实场景渲染：把游戏跑到那一帧

这份记录说明怎么用归档里的素材**重建游戏画面**，而不是画一个框叠文字。

## 素材在哪

之前以为美术资源不在归档里，错了。`patch.pak` 里每个场景是一组六个条目：

```
script   vsn/<n-3>   演出脚本：fadein(...): Sprite / text: 台词
slices   vsn/<n-2>   {"动画名": [[切片ID, ...], ...]}  每帧 14 条
manifest vsn/<n-1>   dirName 与文件哈希
timing   vsn/<n>     {"动画名": {"delays": [...], "loop": ...}}
atlas    vsn/<n+1>   scene.png 4096×1024 的切片图集
page     vsn/<n+2>   那张 4096×1024 的 PNG
```

另有全局 UI 图集 `dataq/5`（atlas）+ `dataq/6`（4096×4096 PNG，7142 个区域），
含 `FrameNinePatch`、`TextBox` 名、各类 HUD 元素。

## 一帧怎么拼

`SLICE_H = 16`，画面 256×224 = 14 条横带。`slices.json` 给的是**切片 ID 列表**，
按顺序自上而下贴：

```python
for row, slice_id in enumerate(slices[animation][frame_index]):
    x, y, w, h = regions[slice_id]      # 从 atlas 文本解析
    canvas.alpha_composite(page.crop((x, y, x+w, y+h)), (0, row * 16))
```

切片 ID `0` 表示空带。

工具：`tools/scene_frame.py`（`load_scene` / `frame` / `script_events`）。

## 中文台词已经是译文

`vsn` 脚本里的 `text:` 行在候选产物中**已经是中文**：

```
fadein(1.0, 4): Asset16
rewind!
text: 现在……伊吠，你一定要醒过来啊！
text: 要是你已经不在里面了……我不，我不知道该怎么办！！
```

所以场景渲染能直接验证这批译文在真实画面里的样子，不需要另找文本。

## 文本层

`vsn` 的 `text:` 走字幕容器 `SubtitleLayout.pages(text, 240)`：240px、3 行、12px 字模。
`SceneRender` 加了 `subtitle` 这个容器，与 `story` / `radio` 并列。

字模从 jar 里取：`story12.fnt` + `r28-font/bbc2.png`，字形按 alpha 通道染色，
颜色取自真实截图（底 `(2,2,0)`、琥珀 `(255,155,0)` / `(232,176,0)`）。

工具：`tools/asset_render.py`（取字模、染色、绘制）、`tools/real_scene.py`（合成）。

## 成果

`out/layout/scenes/` 下 77 张：39 个含对话的场景 × 前两条台词。每张都是
**归档里的真实背景 + 候选产物里的真实中文 + 引擎真实折行 + jar 真实字模**。

## 一条没验证的假设

**字幕几何现在是从字节码推出来的，并且被真实截图印证。**

`PRG/jo` 的字节码给出三个常量：

| 字节码 | 含义 |
| --- | --- |
| `bipush 16` + `imul` + `isub` | 行距 **16** |
| `bipush 8` + `imul` + `iadd` | 中文 x 偏移 **8** |
| `bipush 40` + `isub` | 垂直 **-40** |

`jl` 的原点是 `It.a(2)=16`、`It.b(6)=54`；`StoryFont12.draw` 的中文分支再
`bipush 8` + `Math.subtractExact` 减 8。于是 `drawX=8`、`drawY=54`。

在 256×224 的 y-up 目标里，字形 PNG 顶边是

```
top = 224 - (drawY + 1) + yoffset      yoffset 来自 FNT
```

行 i 的 drawY = `54 - 16*i`，所以 `top = 169 + 16*i`；减去中文那 8px 得 **161**。

**独立印证**：从 `research/intro-05.png`（784×711 真实截图，画布自 y=32 起、缩放
3.06×）量出的文字带正好是 **y=161..173**。两个来源一致。

FNT 自身也吻合：`story12.fnt` 的 `lineHeight=16`、`base=8`、`padding=1,1,1,1`，
汉字字形 12×12、`yoffset=0`。

仍未验证：真实对话框是否有边框与内边距会遮住文字。这需要一张**真实对话截图**，
本会话没有。

## 这套工具验不了本批的 96 行

`batch-25` 改的是 `datadf`/`datadm` 里的对话资源，键形如 `<TomcatItems.VitBone>`。
实测：**97 个这类键完全不被任何 `vsn` 脚本引用**，它们是游戏代码按场景 ID 直接查表的
独立资源，不经过演出脚本。

所以两套文本系统互不相通：

| 系统 | 资源 | 容器 | 本会话能否渲染真实画面 |
| --- | --- | --- | --- |
| 演出脚本台词 | `vsn/<n-3>` 的 `text:` | `SubtitleLayout` 240px | **能**（已出图） |
| 对话/物品说明 | `datadf`/`datadm` | **无线电 150px**（见下） | 背景已找到，见下节 |

### 物品说明走的是无线电，不是故事框

之前按「这批是对话，所以走 240px 故事框」验收，**这个推断错了**。反编译给出的调用链：

```
PRG/JB  （常量池含 "TomcatItems"，作为字符串键传进 aEg 构造器）
  → PRG/JM  （显示 CosmoCodecMenuBG + 双头像）
    → PRG/JQ
      → PRG/JR
        → DialogueWrap.radio   （150px / bbc2 10px / 每行 15 汉字）
```

逐环核对（`class` 字节里是否含下一环的引用）：

| 类 | 引用 | 结果 |
| --- | --- | --- |
| `PRG/JM` | `PRG/JQ` | True |
| `PRG/JQ` | `PRG/JR` | True |
| `PRG/JR` | `DialogueWrap` | True |
| `PRG/JB` | `TomcatItems` | True |

所以 96 行里有 **72 行**（位于 `<TomcatItems.*>` / `<BossuDex.*>` 条目下）走 **150px
无线电**。按故事框验收的「92→35」对这些行不成立；无线电实测是 **74→72**。

物品说明的背景是 UI 图集里的 `CosmoCodecMenuBG`（`xy=1392,3000`，**256×192**），
可从 `dataq/6` 裁出，见 `out/assets/codec-menu-bg.png`。

本批的排版验收仍按 `scene_render` 的分页结果（96 行 92→35 处切词），
真实画面渲染用于**另一条线**：验证 `vsn` 台词的实际观感。
