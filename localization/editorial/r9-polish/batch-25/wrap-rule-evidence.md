# 反编译取证：游戏真实的折行规则

这份记录回答一个问题：**游戏实际怎么给中文台词折行。**

之前所有排版批次（batch-22、batch-23、batch-25 的前几版）都基于一个错误前提：以为折行是按像素宽度 + 标点禁折规则。实际不是。

## 工具

JDK 17 已随仓库提供，`javap` 就在里面，无需安装：

```
localization/toolchains/microsoft-jdk17/jdk-17.0.20.1+1/bin/javap.exe
```

反编译原版归档里的混淆类（`backup/cosmobreeder-multi.jar`，SHA 与 `localization/sources/archives.json` 一致）。

## 关键发现一：`DialogueWrap` 没接进游戏

`PRG/DialogueWrap` 是本项目新增的类，它的 `story` / `radio` / `storyPages` / `pages` 四个方法**只被回归测试调用**。

`CorePatch.java` 里对它只有一处注入：

```java
m.instructions.set(found, new MethodInsnNode(INVOKESTATIC,
    "PRG/DialogueWrap", "terminalText", ...));
```

即只替换了 `terminalText`。对话折行没有走 `DialogueWrap`，游戏仍在跑原版混淆类 `PRG/amw`。

所以 `engine_wrap.py` 前两版（纯贪心、以及 `PixelLayout` 的标点禁折规则）测的都是参考实现，不是游戏行为。

## 关键发现二：原版按固定字符数硬切

调用链，用 `javap -p -c` 逐层读出：

```
PRG.amw.a(String, amq)          // 切成行
  -> PRG.amr$e.a(String, String)   // 先按 "<p>" 分段
  -> PRG.aDJ.e(String, int)        // 返回 aCj 迭代器
  -> PRG.aDI$a.p()                 // 每行取 substring(c, c + cols)
  -> PRG.aDJ.a(String, int, int)   // 就是 String.substring(start, end)
```

`PRG.aDI$a.p()` 的字节码（简化）：

```
getfield c            // 游标
getfield b            // 列数
iadd
invokevirtual String.substring(II)
```

**没有像素测量，没有标点避让，没有词边界。** 每行固定 `b` 个 UTF-16 字符，切在哪就是哪。

`PRG.aDJ.a(String,int,int)` 的完整字节码只有 `Math.max` / `Math.min` / `substring`，确认是纯切片。

## 关键发现三：列数常量

从各常量的 `<clinit>` 里读出：

| 类 | 含义 | 值 |
| --- | --- | ---: |
| `PRG.Ol` | 故事框列数 | **28** |
| `PRG.Ob` | 无线电列数 | **20** |
| `PRG.NY` | 结局面板列数 | 12 |
| `PRG.Om` | 每页行数 | 3 |

`PRG.amw.b(char)` 只判断空格：

```java
if (c == 32) return true; else return false;
```

`PRG.amw.a(char)` 无条件返回空格。也就是说，混淆层对「断点」的唯一概念是 ASCII 空格——而中文没有空格。

## 这解释了 batch-24 为什么必然失败

固定字数硬切下，只要句子长度不是列数的整数倍，就**必然在某处被切开**，切点完全由字数决定。

所以「把一处切词挪到别处」是这条路的固有性质，不是实现失误。batch-24 的 41 行全部「换一个地方切」正是这个原因。

改文案仍然有用，但作用方式不同：**它不能消除切点，只能把切点移到标点后或虚词后**，而不是让切点落在实词中间。

## 对验收的影响

`engine_wrap.py` 现在直接实现这条真实规则：

```python
COLS_STORY = 28
COLS_RADIO = 20

def hard_rows(text, cols):
    return [text[i:i + cols] for i in range(0, len(text), cols)]
```

`assemble_rewrites.py` 按 28 列（对话走故事框）判合格，20 列的切点作为观察记录但不作失败条件——本批 96 行都是 `datadf`/`datadm` 的对话，走 28 列。

## 未验证

- 没有跑游戏验证实际显示。上面的调用链是静态反编译结果，`amw` 的注入点未逐个核对（`amw` 本身没被替换，这点已确认）。
- 28 个汉字在 12px 字模下是 336px，比 240px 的框宽。游戏如何呈现这个宽度（裁剪、缩小还是原本框就更宽）未验证。这是既有问题，不是本批引入。
- 结局面板 12 列的含义未在实机核对。
