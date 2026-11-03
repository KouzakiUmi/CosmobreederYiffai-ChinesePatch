有 2 个阻断

只读核验。快照 `HEAD = 2aee1ba`。未改已有文件，未做 git 写、构建、回归、装依赖或启动游戏。工具按文档命令用仓库自带 JDK 17 实跑；候选 jar 为 `localization/builds/r9-polish-candidate54/cosmobreeder-multi.jar`（对照文本用 candidate52）。

# 1. 跑的是不是游戏自己的类

**故事框这条入口：是。没有替身，没有 fallback。**

`SceneRender.java` 只调用 `DialogueWrap.storyPages`。`scene_render.py` 的 classpath 是 `候选 jar` 在前、编译目录在后。实跑时四个类的 `CodeSource` 都是 candidate54 的 jar，不是 `localization/layout/src`，也不是测试类：

```
classpath=...\r9-polish-candidate54\cosmobreeder-multi.jar;...\scene-review\classes
PRG.DialogueWrap source=file:/D:/Software%20Projects/.../r9-polish-candidate54/cosmobreeder-multi.jar
cosmoloc.layout.DialogueGrid source=同一 jar
cosmoloc.layout.PixelLayout source=同一 jar
PRG.StoryFont12 source=同一 jar
storyPages.declaring=PRG.DialogueWrap
```

去掉 jar 再跑，直接 `ClassNotFoundException: PRG.DialogueWrap`。`SceneRender.class` 不在 jar 里，编译目录里也没有同名布局类。candidate52 与 candidate54 的 `DialogueWrap` / `DialogueGrid` / `PixelLayout` / `StoryFont12` / `JR` / `Nb` 类文件 SHA-256 相同（`DialogueWrap` 前缀 `7ffc26e7ce785293`），所以改前改后的差异只在文本，不在类。

jar 内字节码（不是源码树）：

- `PRG.JR` 第 221 条：`invokestatic PRG/DialogueWrap.radio`
- `PRG.Nb` 第 198 条：`invokestatic PRG/DialogueWrap.story`
- `storyPages`：`StoryFont12.metrics()`，然后 `formatCapped(..., 28, 3, 240.0)`
- `formatCapped` 只转给 `format`
- `radio`：列数 20、宽度 `150.0`，走 `pages()`，字模是 `/bbc2.fnt`

实跑 `StoryFont12.metrics().glyph`：`中` xAdvance=12；`A` 与空格=8；全角 `，。！`=12；ASCII `[` `]`=8。`bbc2` 的 `中` xAdvance=10。

# 2. 喂的是正文还是整行

**是剥掉说话人前缀的正文，括号留着。不是整行。**

`render-corpus.tsv` 按 CRLF 计 17,890 条，全部 5 列。物理行多出来的 2,380 行是正文里的 U+2028；Java `readLine` 不把它当换行，工具吃进的就是这 17,890 条。键 `A`/`B` 各 8,945。

用 `codec.py` 解密 candidate52 / candidate54 的 jar 与 pak 里 `datadf/1`、`datadm/1`，按 batch-23 的说话人正则剥前缀后对照：

| 对照 | 剥前缀后相等 | 等于整行（含 `Tomcat:`） | 其他 |
| --- | ---: | ---: | ---: |
| candidate52 | 17,794 | 0 | 96 |
| candidate54 | 17,794 | 0 | 96 |

那 96 条不是喂错了整行，是另一侧快照的改写。`render-input.tsv` 的 96 对对得上：键 `B` 的正文 = BEFORE = candidate52；键 `A` = AFTER = candidate54。交叉匹配是 0。

例：`datadf/1:2027` 归档行是 `  Yiffany: [是啊，我已完全撤离出来了。…]`，TSV 的 A 正文是 `[是啊，我已完全撤离出来了。…]`。

同一句实跑，带前缀会改断点：正文断在 `不了`（行长 20/3）；整行 `  Tomcat: [……]` 被 `toUpperCase` 成 `TOMCAT:`，断点变成另一对（行长 23/10）。喂整行的话结果确实全错。当前输入没有这个错。

# 3. 文档里的数字

**故事框口径下，表上的数复算成立。它们描述的不是无线电上玩家看见的分页。适用性见阻断 1。**

新鲜实跑与已提交的 JSON 逐字节相同：

```
SceneRender <candidate54 jar> render-input.tsv  → rendered 192 cases
  与 orders/render-output.json SHA-256 相同（c349a8f0c4e4f679，79,557 字节）
SceneRender <candidate54 jar> render-corpus.tsv → rendered 17890 cases
  与 orders/render-corpus.json SHA-256 相同（5611059eddece4d8，5,594,385 字节）
```

17,890 条 `ok: true`，引擎错误 0。每页行槽都是 3。`pixelWidth` 全是 240.0（见观察 2）。

复算口径：引擎 `breaks` 里，两字在键 A（candidate54 正文）的汉字相邻频次 ≥30。这就是文档那张表，不是另一套人工分词。

| 范围 | 复算 | 文档 |
| --- | ---: | ---: |
| 96 行改前 | 92 | 92 |
| 96 行改后 | 35 | 35 |
| 键 B（candidate52，8,945 行） | 349 | 349 |
| 键 A（candidate54，8,945 行） | 292 | 292 |

「全库 17,890 行」是 A+B 两次渲染的条数。每一侧是 8,945 行，不是 17,890 行各算一遍。

96 例页数：改前改后都是 1 页，96/96。非空行：改前 2 行 55、3 行 41；改后 1 行 4、2 行 74、3 行 18。与 `batch-25/README.md` 一致。

故事框行为（合成句 + 全库，都是 jar 里的 `storyPages`）：

- 20 个 `中` 一行（12×20=240），第 21 个换行。纯汉字行没有超过 20 的。
- `，`/`！` 放在第 20 字之后时，断点回退到 19，下一行不以该标点开头。全库软折行里，下一行以禁折标点开头的是 **0**。
- 60 个汉字 = 1 页 3 行；61 个 = 2 页。短句第三行是空串。
- 29 个 `A`（8px，232px，仍小于 240）断在 28。`q=28` 对拉丁字母生效，对汉字不生效。文档这句对故事框成立。

文档把 349/292 说成「不是 ≥30 频次、是引擎实际输出、都是实词」。频次部分不成立：上面这张表就是 ≥30，只是断点来自引擎而不是旧的 Python 折行，频次表用的是改后语料。950→901 对不上，是因为旧折行位置不同，不是因为换了一套「实词」判据。

# 4. 剩下 292 处，以及「不再处理」

**抽查的例子在故事框输出里是真的。由此推出「都是实词、不是误报、所以不再处理」站不住。**

键 A 的 292 处高频对，前几名：`的带` 34、`特工` 11、`过了` 9、`就行` 9、`能力` 8、`使用` 8、`不可` 8、`不过` 6、`攻击` 6。文档点名的 `不了` 2、`好了` 4、`生意` 4、`击枪` 2 都在改后输出里，例如 `datadf/1:471` 断 `不了`，`:531` 断 `生意`，`:1051` 断 `击枪`。

下一行在遇到非汉字之前的汉字数：1 字 256 处、2 字 1 处、3 字 34 处、6 字 1 处。那 34 处 3 字全是 `的带`（「有的 / 带标注」）。`assemble_rewrites.py` 的 `KNOWN_FALSE_POSITIVE` 已经把 `的带` 标成跨词，不是词内切分。文档写「都是实词被切开，不是判据误报」，与这 34 处直接矛盾。

「行尾只剩 1～2 个字」覆盖 257/292，不是全部。

更要紧的是这些断点多数不是玩家在对应界面看见的断点。见阻断 1。同一句：

```
[这个？就是那帮可爱太空崽子随身带的电击枪。]
  storyPages 240：电击 / 枪     breaks=击枪
  radio 150：    随 / 身带的电击枪  breaks=随身
```

故事框上的「电击枪被切开」在无线电上并不发生；无线电切开的是「随身」。按故事框断点决定「不再处理」，会放过无线电上真正被切开的词。

# 阻断

1. **工具不能当作这批语料的玩家视野。** 它只调用 `storyPages`（Nb → 故事框，240px / story12 / 20 汉字）。jar 里无线电是另一条：`PRG.JR` → `DialogueWrap.radio` → `pages(..., 20, 150.0, bbc2)`，汉字 10px，满行 15 字。`uses12` 只在 `story()` 里，管不到 `radio()`。`scene-render.md` 把这套输出写成「玩家实际看到的分页」，并把全库 17,890 条都送进 `storyPages`。96 个改写目标里，场景根是 `TomcatItems` 的有 59 行，再加上 `BossuDex` 13、`Mauser` 7、`Tomcat` 2，共 81/96。改后 292 处里，仅 `TomcatItems` 就有 98 处。这些行的玩家界面是无线电，不是这条入口。未逐个反编译混淆调用点来证明每一个根名一定进 `JR`；路由本身（JR=radio 150px，Nb=story 240px）是 jar 字节码和 `localization/layout/README-textflow.md` 的事实，TomcatItems 是本仓库对雄猫无线电道具解说的归类。

2. **「292 处都是实词切词，不是判据误报，因此不再处理」不成立。** 292 是改后语料上二字组 ≥30 的引擎断点，不是逐条分词。其中 34 处是本批自己标成误报的 `的带`。其余也混有虚词接续（`过了`、`就行`、`了吧`）和真词（`特工`、`能力`、`使用`）。即便只谈故事框，也不能用这句停手；再加上阻断 1，这 292 里很大一部分根本不是该界面的断点。

# 观察

1. `SceneRender` 不读 `args[0]`。classpath 给对、参数 jar 给错时仍会渲染（用 `DOES-NOT-EXIST.jar` 仍 `rendered 20 cases`）。文档命令两边用的是同一个 jar，这次没有跑偏。
2. 输出的 `pixelWidth` 是传入的行宽预算，不是该行实测字宽。17,890 条全是 240.0，包括 28 个拉丁字母、实际只有 224px 的行。20 字结论是靠行长和字模核对的，不是靠这个字段。
3. 「行首不出现标点」对软折行成立（0 处）。另有 28 处下一行以禁折标点开头，来源是正文里已有的 U+2028 硬切，不是 `legalBoundary` 失效。
4. 键 A/B 的命名和「17,890 行」的说法容易读成每一侧都有 17,890 行。实际每侧 8,945。数字本身在上面的口径下是对的。
5. 故事框自身的四条行为（满行 20 汉字、软折行不把标点放行首、每页 3 行不足补空、`q=28` 对汉字不生效）在 jar 类上成立。工具作为 **Nb/故事框** 的离线渲染是可用的；不能把它的输出当成 datadf/datadm 全部说话人行的实机分页。
