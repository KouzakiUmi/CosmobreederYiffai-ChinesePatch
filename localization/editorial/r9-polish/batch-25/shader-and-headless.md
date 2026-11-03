# Shader 复算、离屏渲染与动画时间状态研究

本报告承接 [模拟渲染研究](simulated-render-research.md)。三步均已完成，并按步骤分别落盘。证据基线为 [原版jar](../../../../backup/cosmobreeder-multi.jar)（manifest ReleaseTag `1.0.5_full`、ShortCommit `2ee26ee87c`）与 [原版patch.pak](../../../../backup/patch.pak)。

## 第一步：`vsn_term_shade` 的 Python 等价复算（完成）

### 结论

`shaders/vsn_term_shade.frag` 是透明底上的终端掩码着色与邻域描边：红通道大于零的像素变为金黄色，纯不透明蓝色标记变为暗金色，其余像素按邻居的红通道生成暗金描边或透明。每 8 个纹理行有一行不检查 `v+stepY` 的邻居，形成周期性的断行效果；并不是将整个输入画面的亮度乘上正弦扫描线。

**`texture_size` 的真实值已查到：256×224。** 原版 `PRG/jl` 的静态方法 `a(PRG.ZJ, PRG.amq, int, int, boolean, int, int, PRG.SN, PRG.anh, PRG.amU)`，字节码偏移 108–132：依次加载 `vsn_term_shade`、`texture_size`、`256.0f`、`224.0f`，构造 `PRG/aAJ` 二元组并调用 `PRG/SV.a` 设置 uniform；偏移 147–153 将该 shader 应用到文字层句柄。偏移 236 起才是合成后的 `vsn_fade`。因此不能把场景图集的 4096×512 或外层窗口大小当成此 uniform。

### 源码逐行解释

下面保留原 shader 的所有有效语句（空行和原注释省略），逐行附解释：

```glsl
#version 120                          // 桌面 GLSL 1.20。
#ifdef GL_ES                          // GLES 编译分支。
  #define LOWP lowp                   // GLES 的低精度限定宏，本文件后面未使用。
  precision mediump float;            // GLES 默认浮点精度。
#else                                // 桌面分支。
  #define LOWP                       // 桌面上 LOWP 展开为空。
#endif                               // 结束平台分支。
varying vec4 v_color;                 // 顶点颜色，声明但整个 main 未读取。
varying vec2 v_texCoords;             // 当前片元的归一化纹理坐标。
uniform sampler2D u_texture;          // 输入 RGBA 纹理。
uniform vec2 texture_size;            // 步长与每8行周期的参考尺寸，实际为256×224。
void main() {                        // 每个片元独立执行。
    vec4 base_color = texture2D(u_texture, v_texCoords); // 采样本像素。
    vec4 black = vec4(0.0, 0.0, 0.0, 1.0); // 不透明黑，VSN版本实际未使用。
    vec4 white = vec4(1.0, 1.0, 1.0, 1.0); // 不透明白，实际未使用。
    vec4 inner_color = vec4(0.972, 0.721, 0.0, 1.0); // 字形内芯金黄。
    vec4 glow_color = vec4(0.313, 0.188, 0.0, 1.0);  // 描边暗金。
    if (base_color == vec4(0.0, 0.0, 1.0, 1.0)) { // RGBA四通道精确等于纯蓝标记。
        gl_FragColor = glow_color;    // 标记直接输出暗金。
    } else if (base_color.r > 0) {    // 任意正红值都算内芯；此处不检查alpha。
        gl_FragColor = inner_color;   // 输出完全不透明金黄。
    } else {                         // 黑色、透明黑等进入邻域测试。
        vec2 stepSize = 1.0 / texture_size; // 分量相除，得到1/256、1/224。
        vec4 sum = vec4(0.0);         // 初始化邻居之和。
        sum += texture2D(u_texture, vec2(v_texCoords.x - stepSize.x, v_texCoords.y)); // 左邻。
        sum += texture2D(u_texture, vec2(v_texCoords.x + stepSize.x, v_texCoords.y)); // 右邻。
        sum += texture2D(u_texture, vec2(v_texCoords.x, v_texCoords.y - stepSize.y)); // v负方向邻居。
        float py = v_texCoords.y * texture_size.y; // 纹理坐标换算为行位置；通常落在像素中心。
        int my = int(mod(py + 1.0, 8.0)); // GLSL正模后截断为整数，周期为8。
        if (my != 0) {               // 每周期有一个行区间跳过下一项。
            sum += texture2D(u_texture, vec2(v_texCoords.x, v_texCoords.y + stepSize.y)); // v正方向邻居。
        }                            // 结束周期判断。
        gl_FragColor = sum.r > 0 ? glow_color : vec4(0.0); // 有红邻居则暗金，否则透明黑。
    }                                // 结束颜色分支。
}                                    // 结束片元函数。
```

对照 `shaders/cosmo_term_shade.frag`：它先执行 `base_color.a == 0` 时直接输出透明，且无红邻居时输出不透明黑；VSN 版去掉这两个行为，让透明黑周边也可以长出描边，背景本身保持透明。两者都有未使用的 `white` 和 `v_color`，VSN 另有未使用的 `black`。两版均没有时间 uniform。

### 复算所需的真实输入

| 输入 | 实际所需值 / 已核程度 |
| --- | --- |
| `u_texture` | 原管线的文字 framebuffer 纹理；要得到整幅实机画面应先对该文字层着色，再与背景合成。下方样例按任务要求用真实场景帧诊断此算子。 |
| `texture_size` | **256×224，字节码硬编码，已核实。** |
| `v_texCoords` | 来自绘制四边形，影响每8行缺边的相位和方向。Python 显式接收顶部/底部v坐标；本次样例使用顶部1、底部0。原运行管线该次draw的最终翻转状态尚未完整追踪，不把此相位假设称为GPU截图实证。 |
| `v_color` | 不参与输出，不需要真实顶点颜色。 |
| 采样状态 | 下列函数采用完整纹理、最近邻、边界夹取；`vsn/3` 图集声明 `Nearest, Nearest`、`repeat: none`。文字FBO的最终采样状态尚未独立核全；若为线性采样或子区域UV，须改采样器，不能直接套此函数。 |
| 输出格式与合成 | 下列函数量化到8位RGBA；shader内部先产生浮点颜色。输出本身为直通alpha（透明黑或alpha=1），尚未包含后续blend、`vsn_fade`和窗口缩放。 |

注意：RGBA=(255,0,0,0) 也会被该 shader 变为不透明金黄；复算时不能擅自按alpha预先清除隐藏RGB。透明纯蓝不是纯不透明蓝标记。邻域只检查红通道，不做模糊加权，描边也不累积亮度。

### 可执行 Python 函数

仅依赖 Python 标准库和 Pillow。输入为 PIL RGBA 图像；默认处理完整纹理和一比一输出。`v_top/v_bottom` 是在输入图按屏幕从上往下存储的前提下，对应四边形顶边/底边的v值。

```python
import math
from PIL import Image


def vsn_term_shade(layer, texture_size=(256, 224),
                   v_top=1.0, v_bottom=0.0):
    """Nearest + clamp-to-edge；输出8位RGBA，未做后续blend或调色。"""
    src = layer.convert('RGBA')
    w, h = src.size
    tw, th = map(float, texture_size)
    if min(w, h, tw, th) <= 0 or v_top == v_bottom:
        raise ValueError('invalid dimensions/UV interval')
    pix = src.load()
    out = Image.new('RGBA', (w, h))
    dst = out.load()
    # 归一化常量量化为8位：round(channel * 255)。
    inner, glow = (248, 184, 0, 255), (80, 48, 0, 255)

    def sample(u, v):
        x = min(w - 1, max(0, math.floor(u * w)))
        y = min(h - 1, max(0, math.floor(
            (v - v_top) / (v_bottom - v_top) * h)))
        return pix[x, y]

    for y in range(h):
        v = v_top + (v_bottom - v_top) * ((y + 0.5) / h)
        for x in range(w):
            u = (x + 0.5) / w
            base = pix[x, y]
            if base == (0, 0, 255, 255):
                color = glow
            elif base[0] > 0:
                color = inner
            else:
                red = (sample(u - 1/tw, v)[0]
                       + sample(u + 1/tw, v)[0]
                       + sample(u, v - 1/th)[0])
                if int((v * th + 1.0) % 8.0) != 0:
                    red += sample(u, v + 1/th)[0]
                color = glow if red > 0 else (0, 0, 0, 0)
            dst[x, y] = color
    return out
```

`int(mod(...))` 不能改成简单的 `y % 8`，否则会丢失像素中心的半像素和UV方向。要完整模仿GPU浮点舍入、非整数缩放或线性过滤，需要进一步模拟这些状态；本函数在上述明确采样条件下等价于片元逻辑。

### 真实数据样例与检查

已用 `localization/tools/codec.py` 的 `decrypt_file` 解密原版 `backup/patch.pak` 的 `vsn/4` PNG（4096×512），依据 `vsn/3` atlas 和 `vsn/6` 切片表拼出 `ClassicPretitle01CToD` **第48帧（从0开始）**，再以真实 uniform **256×224** 运行上面的函数。

产物：[shaded-sample.png](../out/layout/scenes/shaded-sample.png)，256×224。输入有10种RGBA值；输出只有预期的三种：金黄27,607像素、暗金954像素、透明黑28,783像素，总计57,344像素。已用 `read_image` 查看，能看到大块金黄色区域、中央深色轮廓及透明区域，符合「按红通道二值映射 + 暗金边缘」的行为。

这张图是**真实场景素材经过文字shader的诊断图**：场景中的大片红通道为正的区域自然会塌缩成金黄色，并非该场景的实机最终配色。真实还原应将同一函数用于文字层，再按原顺序合成背景；本次没有把此诊断样例当作实机截图。试验脚本仅放在 `/tmp/shade_sample.py`。

## 第二步：真实 libGDX 管线的离屏可行性（完成，静态判断）

### 三档结论

**整体判定：需改造。** 在本机桌面 OpenGL 环境中，用隐藏 GLFW 窗口提供 GL 上下文、复用现有 framebuffer 管线，再回读 PNG，技术上可行；现有入口没有现成的批量离屏截图模式。若要求完全不创建任何原生窗口对象，现有 GLFW 桌面启动路径不可直接满足；换成名为 Headless 的后端也不能凭空提供此渲染路径所需的 OpenGL。

| 目标 | 判档 | 原因 |
| --- | --- | --- |
| 原 shader + 原 framebuffer，用隐藏窗口渲染 | **可行**（依赖层支持；运行未验证） | 已有 LWJGL3/GLFW 上下文、FBO池、shader应用与合成设施。 |
| 从当前游戏入口直接无窗口、指定台词导图 | **需改造**（总体结论） | 默认随后显示窗口；缺少确定时间、脚本定位、导图和自动退出的适配入口。 |
| 现有入口不创建窗口对象、也不提供 GL 上下文就跑真实shader | **不可行**（限定现有路径） | shader和FBO真实调用OpenGL；GLFW窗口与context绑定。换EGL/OSMesa等是新后端工作，不是现成开关。 |

### 主入口与后端证据

- jar manifest：`Main-Class: co.kemosho.cosmo.Main`。
- `co.kemosho.cosmo.Main.main(String[])` 偏移0–4调用 `PRG/jF.MODULE$.a(args)`；`PRG/jF.a` 再进入 `PRG/iF.a`。
- `PRG/iF.a(String[], PRG.azy)` 偏移235创建 `PRG/aqj` 配置，454–462创建 `PRG/aqg(listener, config)`；后者常量池含 `Lwjgl3Application`，并直接调用 `org.lwjgl.glfw.GLFW`。这是被混淆的 LWJGL3 桌面后端。
- 扫描所有class常量池：`Lwjgl3Application` 命中 `PRG/aqg`；`LwjglApplication`、`HeadlessApplication` 均无命中。无命中仅表示没有这些明文引用；实际后端由上述可追踪调用确认，不能只靠类名搜索断言所有被混淆类的身份。
- `PRG/aqg` 在建context后还有 “OpenGL 2.0 or higher with the FBO extension is required” 检查。这个管线明确需要真实GL能力。
- `org.lwjgl.Version` 常量为 LWJGL **3.3.1**；jar内 `org.lwjgl.glfw.GLFW` 的版本常量为 GLFW **3.4.0**。libGDX自身精确版本在所查manifest、class字符串和Maven元数据中未确认，不能用当前API名称直接替代本jar的混淆符号。

### 已有 framebuffer 能直接复用

仅搜索 `FrameBuffer` 明文会漏掉大部分设施，因为库类也混淆了：

1. `PRG/arM<T extends PRG.arf>` 是GL framebuffer基类（常量池保留附件错误文本及FBO能力检测）；`PRG/arL extends PRG/arM<PRG.ark>` 提供 `(format, width, height, depth)` 构造器。其 `b(PRG.ark)` 对 `GL_FRAMEBUFFER=36160`、`GL_COLOR_ATTACHMENT0=36064`、`GL_TEXTURE_2D=3553` 调用纹理附件接口。
2. 游戏类 `PRG/Yc` 维护 `AtomicLong` 句柄、`PRG/arL` 映射和可复用句柄队列；私有 `e()` 偏移0–17创建无深度FBO，公开 `b(format,w,h,depth)` 也能分配。
3. `PRG/Ym implements PRG/SV` 使用这套FBO池；第一步的 `PRG/jl` 已经通过 `SV` 分别绘制背景层和文字层、应用 `vsn_term_shade`、合成、按需应用 `vsn_fade`，最后再绘制输出。需要导图时应在最终内部目标释放回池之前读回，避免读到复用后的内容。
4. 可回读到CPU的底层入口存在：jar内 `org.lwjgl.opengl.GL11/GL11C.glReadPixels`。本次只确认存在该能力；没有确认游戏已经封装了可直接调用的PNG导出方法，需适配绑定目标FBO、像素格式、pack alignment和上下翻转。

这里也补强了第一步的采样证据：`PRG/Yc.e()` 偏移21–31、`b(...)` 偏移14–25把两个过滤项都设为 `PRG/ark$a.a`；该枚举初始化明确是 `Nearest`（9728）。`PRG/arL` 创建附件时将wrap设为 `PRG/ark$b.b`，枚举名为 `ClampToEdge`。因此池中新建FBO的默认采样确实支持第一步Python采用的最近邻与边界夹取；仍需注意后续draw的UV朝向。

### 隐藏窗口如何成立，哪里还要改

`PRG/aqg.a(PRG.aqj,long)`：偏移0重置window hints，偏移3–6立即调用 `glfwWindowHint(131076, 0)`；jar内常量确认 **131076 = GLFW_VISIBLE**。因此创建GLFW窗口时本来就是先隐藏。

但 `PRG/aqg.a(PRG.aqx,PRG.aqj,long)` 偏移13–18随后读取配置布尔字段 `R` 并调用 `PRG/aqx.a(boolean)`；该方法true分支调用 `glfwShowWindow`、false分支调用 `glfwHideWindow`。`R` 声明于父类 `PRG/aqK`，构造器默认赋true。当前经裁剪的 `aqK/aqj` 公共方法中没有保留 `setInitialVisible` 名称或设置 `R` 的专门setter。

可供后续实现的最小方案是：独立的适配launcher在构造后端前，通过同包访问或反射将 `PRG/aqK.R=false`；接入指定场景/台词状态，用确定时间推进，复用原内部256×224渲染目标，读回并结束。另一方案是独立初始化隐藏GLFW上下文，再适配游戏需要的 `Gdx`/服务对象；后者要重建的初始化较多。单独在外部先设 `GLFW_VISIBLE=false` 不够，因为后端会先重置hints，且默认稍后仍会show。

[GLFW 3.4官方context guide](https://www.glfw.org/docs/3.4/context_guide.html#context_offscreen) 明确说明：GLFW不提供不关联窗口的context，但可以用 `GLFW_VISIBLE=false` 创建永久隐藏窗口；隐藏窗口尺寸未必可靠，建议渲染到FBO，并继续处理事件。[libGDX官方离屏context示例](https://github.com/libgdx/libgdx.github.io/blob/dev/wiki/graphics/3d/virtual-reality.md) 同样采用隐藏GLFW窗口、make-current、GL capabilities初始化后设置Gdx对象。这里的「无窗口」可操作实现应定义为**无可见窗口，保留隐藏窗口对象**。

jar的GLFW绑定虽然还包含 `GLFW_PLATFORM_NULL`、`GLFW_EGL_CONTEXT_API`、`GLFW_OSMESA_CONTEXT_API` 常量，但常量存在不能证明本机带有对应GL驱动/运行库，也不能证明游戏后端已设置相应初始化hint。完全无桌面/无显示服务的环境适配在本次静态证据下仍未知。

### 粗略工作量与验证缺口

若只做单场景、单确定时刻的隐藏窗口导图适配，估计 **1–3个工程日**：launcher与资源/服务初始化半天到一天，注入场景状态与固定时间约半天到一天，FBO读回与像素/方向校验约半天。批量定位任意台词、控制逐字显示/输入分支/音频依赖，预计再 **2–5日**。这是按已找到的复用设施估算，未执行原型；完全不创建窗口对象的后端改造需另评估。

本步只运行 `javap` 与归档/常量池读取，并对照官方文档；游戏、GLFW context、shader编译和真实FBO读回均未启动验证。

## 第三步：动画时间状态与「看到某句台词」的取帧（完成）

### 可操作结论

**没有对所有台词通用的「第0帧」或固定帧号。** 必须先确定目标页进入时刻、动画最近一次启动/重启时刻、文字逐字显示状态，以及玩家此前何时按键。用于排版验收，建议统一采用：**在目标页仍显示的条件下，取当前淡入已完成、该页文字已完整显示之后的第一个固定60Hz采样时刻，再向后留1个tick；循环背景按该时刻正常选帧。** 这里「稳定」表示转场结束且文字完整，并不要求循环背景静止。

如果目的是「刚开始看到这句」而非完整可读状态，则取该页进入后的首个更新/绘制tick，保留真实逐字显示量；它可能只有首字，不能同时当作整句排版截图。对于需要玩家按键推进的页，历史等待时长会改变循环背景相位，无法从台词文本唯一反推出玩家当时看见的背景帧。批量离线验收应记录一套固定按键策略（例如完整显示后1tick推进）及其时间轴。

### `fade` 参数含义：示例里的9不是9秒

`PRG/amS$a.a(PRG.aAZ)`（构造fade命令的方法）字节码偏移6–30依次取脚本三项，偏移36–43实际按 **第二项double、第一项int、第三项int** 构造 `PRG/amI(DII)`。`PRG/amI` 的 `m_()` 是 `VSFade`；其执行方法偏移0–20调用：

```text
state.fadeState.add(state.currentTime, duration, targetPalette, steps)
```

因此脚本语法应读为：

```text
fade(targetPalette, durationSeconds, quantizationSteps)
fade(9, 0, 1) = 目标调色板9，耗时0秒，进度量化分段数1
```

第三项不是秒数，也不是需要查外部表的混合模式：`PRG/amK.b(double, amJ)` 偏移30–45先算 `(now-start)/(end-start)`，再调 `PRG/afL.a(progress, steps)`；后者偏移0–9明确是 `int(steps*progress)/steps`，然后在起止调色板编号间插值。`amK` 在duration=0时直接返回目标编号，不做除法。调色板编号由第一步已定位的 `vsn_fade`/`fadelut` 后期使用；`vsn_term_shade` 本身没有时间参数。

`PRG/amK.a(now,duration,target,steps)` 偏移18–31记录起始palette（无历史时0）、目标palette、start=now、end=now+duration和steps；有历史时从前一次目标palette接续。**单独 `fade(...)` 只添加时间区间，不自行等待结束**：`PRG/amI` 返回时保留当前时钟与待执行队列，后续文字可以与长fade并行。

### `fadein(0.5,4)` 会冻结，再重启动画

`PRG/amS$a` 的 `b(PRG.aAZ)`（紧邻 `fadeinCmd` 的返回转换方法）字节码32–115将 `fadein(duration,steps): name` 展开为 `PRG/amO`（`VSMulti`）中的这五条命令，顺序由链表构造保留：

```text
SnapAnimation(name)            // PRG/amD：清空动画队列，以当前时刻启动name
VSFreeze                      // PRG/amL：记录当前时刻为动画取样的冻结时间
VSFade(duration, 0, steps)     // PRG/amI：淡到palette 0
VSWait(duration)              // PRG/anq：阻塞后续命令直到当前时刻+duration
SnapAnimation(name)            // 再次清空队列并启动name，解除冻结
```

证据：`PRG/amD.a(state,assets)` 偏移2–32调用 `state.animationQueue.f()` 清队列，再用当前时刻 `state.e()` 调 `ane.a(name, metadata, now)`；返回的新队列冻结字段为空。`PRG/amL`（`VSFreeze`）偏移6–32把当前时刻写入 `ane` 的可选冻结字段。`PRG/anq`（`VSWait`）偏移4–17构造 `PRG/anw(now+duration)` 挂起后续命令。`PRG/ane.a(now)` 偏移0–16优先使用冻结时间，偏移129–159把有效时刻减去所选动画的启动时间，传出局部动画时间。

故 `fadein(0.5,4): ClassicPreTitle01A` 淡入期间动画固定在起始画面；半秒等待结束并执行最后一条snap后，动画局部时间重新从0开始。不能把淡入消耗的0.5秒算进后续正文的动画进度。脚本调度以更新tick处理，精确进入时刻需用实际状态记录，可能落在理论0.5秒后的首个tick。

真实 `vsn/5` 的开头就是 `fade(9,0,1)`、`fadein(0.5,4): ClassicPreTitle01A`、两条 `auto(8.0)`。在淡入后的首个正文进入时刻，背景应以最后一次snap为起点；完整显示正文时的背景通常早已不是第0帧。

### `timing.delays` 的单位、循环和精确边界

`vsn/2` 解密得到的metadata是实际例子：`ClassicPretitle01B` 的delays为5个0.2，loop=true；`ClassicPretitle01CToD` 为98个0.1，loop=false。delays是**各帧停留的秒数**，不是累计时间，也不是帧号。

调用链：`PRG/XH` JSON派生reader字段名包含 `delays`、`loop`、`sfx`，读成 `PRG/XE`（`AnimationMetadata`）；`PRG/Yq.a(...)` 偏移11–34把 `XE.a()` 的delays、对应帧集合和 `XE.e()` 的loop送入 `PRG/SX`（`KAnimation`）。实际VSN绘制 `PRG/jl.a(amU,SN,int,int,aAZ)` 偏移45–51把局部时间先转float再转double，然后调用 **`SX.a(double)`** 选帧，偏移83–88用选出的索引取 `slices[name][index]`。不能误用同类的 `SX.b(float)`：后者是按首帧delay等分的另一套方法，真实VSN切片绘制走的是前者。

`SX.a(double)` 的规则是毫秒量化后，选第一个累计结束时间**严格大于**当前时间的帧：

1. 每个delay先计算 `int(delay*1000)`，再累计成各帧结束毫秒；`SX` 的惰性累计函数偏移16–23明确先截断单帧时长再加到此前累计值。
2. 当前局部时间在draw处经过float32往返，再计算 `int(localSeconds*1000)`。
3. loop=true时对 `int(sum(delays)*1000)` 取余；loop=false时超过最后结束点停在末帧。注意循环总周期与累计端点分别计算，含小数的资料可能有毫秒级截断差；不得把两者擅自合并。
4. 小于第一结束点返回0；大于等于最后结束点返回末帧；中间寻找首个结束点>当前毫秒。即半开区间 `[start,end)`，边界点归下一帧。若动画排队或冻结，先按队列/冻结状态得到有效局部时间，再应用此规则。

下面是可执行复算（正时长、非负局部时间输入）。使用逐项double相加模拟普通累计，避免Python 3.12的内建 `sum` 优化改变舍入；严格跨平台逐位对比时仍应直接复用jar中的数值路径。

```python
import bisect
import struct


def f32(x):
    return struct.unpack('>f', struct.pack('>f', x))[0]


def vsn_frame_index(delays, loop, local_seconds):
    if not delays or local_seconds < 0 or any(d <= 0 for d in delays):
        raise ValueError('need positive frame delays and nonnegative time')
    ends, cumulative_ms, total_seconds = [], 0, 0.0
    for delay in delays:
        cumulative_ms += int(delay * 1000.0)
        ends.append(cumulative_ms)
        total_seconds += delay
    tick = int(f32(local_seconds) * 1000.0)
    if loop:
        total_ms = int(total_seconds * 1000.0)
        if total_ms <= 0:
            raise ValueError('zero loop period')
        tick %= total_ms
    return min(len(ends) - 1, bisect.bisect_right(ends, tick))
```

已用原版真实metadata运行此复算：

| 动画 | 局部秒数 → 从0开始的帧号 |
| --- | --- |
| `ClassicPretitle01B`（5帧、循环） | 0→0；0.199→0；0.2→1；0.999→4；1.0→0；1.21→1 |
| `ClassicPretitle01CToD`（98帧、不循环） | 0→0；0.1→1；4.85→48；9.9→97；20→97 |

这是静态字节码规则的CPU演算核对，不是运行游戏采样。试验脚本为 `/tmp/frame_rule_check.py`。

### 完整文字的时刻也必须计入

`PRG/amn` 保存正文、startTime、可选的强制完整显示时间及每字间隔；`a(now,boolean)` 偏移58–71以 `int((now-startTime)/interval)` 决定已揭示字符位置，已有强制完整显示时间且now到达时则直接返回全部长度。构造器将字符与原索引配对后过滤ASCII空格（`amn.a(aAJ)` 检查char != 32），据此计算揭示步数N。不能直接把包括空格和格式控制符的脚本原串长度当作N。

`amn.i()` 在无显式完整显示时刻时返回 `startTime + N*interval`（其静态辅助方法偏移0–16）；`PRG/ams` 静态初始化把普通正文间隔b和auto间隔c都设为 **0.06f秒**，`PRG/amH`（`VSAutoText`）偏移43–58明确用c创建 `amn`。实际应以运行状态对象的N、interval和当前页正文为准：先替换动态文本、完成真实分页和控制标记解释，再算此时间；补丁改变分页后尤其不能沿用英文原串时长。

`auto(duration)` 另外设置 `amG`（`TextBox`）的自动推进截止时间为当前时刻+duration（`amH` 偏移73–96）。它与文字逐字显示时长是两件事：若目标页在完整显示前已经自动离开，则不存在该次播放中的「全字稳定帧」，应记录无此时刻并另取首个/末个真实可见状态，不能在过去的背景上强行叠完整句子。

### 推荐的确定性取帧流程

1. 按真实脚本顺序重放到目标**显示页**，记录state时钟、队列、最近一次snap、freeze字段、fade区间、字幕start/interval/强制显示时间与当前自动退出截止；非阻塞fade允许与正文重叠，wait与fadein必须推进其等待状态。
2. 以 `T_full = 当前页amn.i()` 为完整显示时刻（或明确按键让其提前完整显示后的状态时间），以 `T_fade = 当前仍影响画面的转场结束时间` 为后期稳定时刻，设置 `T_ready=max(T_full,T_fade,目标页进入时间)`。
3. 固定验收采样为 `T_sample=ceil(T_ready*60)/60 + 1/60`，并执行该tick到应有的命令状态，再确认目标页仍在显示。60Hz是建议的离线策略，不是素材的帧率；源delays仍按各自秒数计算。若页已离开，不能越过截止时间强取截图，应改用该页真实可见区间内的采样并标明文字状态。
4. 用动画队列计算该时刻当前动画的 `t_effective - t_animation_start`；冻结时用冻结时刻代替当前时刻。队列切换不能仅以脚本行号猜：`ane.a(name,metadata,now)` 会按前一个动画结束/循环边界安排后继启动时间。最稳妥的真实管线适配是直接复用此状态类。
5. 用上面的 `vsn_frame_index` 取切片帧，绘制该时刻已揭示的目标页文字，给文字层执行 `vsn_term_shade`，合成背景后再应用该时刻的palette/fade状态。保存动画名、帧号、state时间、局部时间、页号与取帧策略，供重复验收。

这能回答「在约定播放/按键时间轴下，玩家看到这页完整文字时应该取哪帧」。如果用户要求还原某次实际游玩的那一帧，则还需要那次输入和delta时间记录；仅凭脚本与台词无法唯一确定循环相位。三步研究至此均已完成并落盘。
