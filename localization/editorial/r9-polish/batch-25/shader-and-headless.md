# Shader 复算、离屏渲染与动画时间状态研究

本报告承接 [模拟渲染研究](simulated-render-research.md)。第一步已完成；第二、三步待追加。证据基线为 `backup/cosmobreeder-multi.jar`（manifest ReleaseTag `1.0.5_full`、ShortCommit `2ee26ee87c`）与 `backup/patch.pak`。

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
