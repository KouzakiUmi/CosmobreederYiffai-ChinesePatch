# 存档单卡片无启动绘制探针

## 结果与冻结身份

**PASS：22 个场景，3172 项断言；指定运行时 `-Xverify:all` 正常退出。** 本验证不是游戏启动、GPU/CRT/实际 clip 或输入验收。

- 唯一探针源码：[SaveDrawingProbe.java](<PRG/SaveDrawingProbe.java>)。
- 最终录制：[save-drawing-recording.json](<../../work/layout-drawing-probe/save-drawing-recording.json>)；SHA-256 `fb5b0e020c8f81adae30ffcf4969ce6a8225820bd80049ae00920b599f5d2b37`，1,028,182 bytes。这个版本已经冻结，父代理应按这个身份重新离线重放，不沿用早期合成标题版本。
- 候选：[cosmobreeder-multi.jar](<../../builds/layout-r22-candidate-v2/cosmobreeder-multi.jar>)；SHA-256 `c7a015f3c0f9db6bf52ce668090659e2cb3385e1349458d1d3e3fbb8518b6923`。实际是 **12 个既有 class 改写＋34 个新增 helpers**；归档未改动。
- 默认字体：[bbc2.fnt](<../../runtime/bbc2.fnt>) SHA-256 `000c85594bb86de3402ab9c4dab3b50c0590051dbbe9b96a8d856acb7e983753`；[10px 位图](<../../runtime/bbc2-cjk-10.png>) SHA-256 `075a2803ee8c5e04ff8d755e76a7d7803fd45080b6a4b031be99bf1a656db306`。
- 编译日志：[compile.log](<../../work/layout-drawing-probe/compile.log>)；执行及类来源日志：[run.log](<../../work/layout-drawing-probe/run.log>)。编译有 Unsafe、SecurityManager 弃用及 source8 bootstrap 警告，无编译错误。实际测试 JRE 是支持该测试用 SecurityManager 的 Java17 系列，不声称已在 Java8 JRE 执行。

## 真实构造图调查与安全切口

证据由候选 JAR 直接 `javap -p -c` 获取，输出只在独占目录：[构造／绘制快照](<../../work/layout-drawing-probe/constructors-javap.txt>)、[数据依赖快照](<../../work/layout-drawing-probe/fixture-javap.txt>)、[初始化依赖](<../../work/layout-drawing-probe/init-javap.txt>)。语义对照[既有存档证据](<../research/save-menu-evidence.md>)，不采用旧日期假设。

1. `Mf(jd,int)` 取 `jd/le/SH/afT` 并建动作及 selector；**不调用这个构造器**。
2. 原 `Mf.s()` 每次直接 `Mg.a(...) -> Mg.b() -> Hi.a()`，不是有可替换字段的槽缓存。为绝不触存档服务，测试专用 `FixtureMenu extends Mf` **只覆盖 `s()`**，返回真实游戏 collection 内的合成槽。这个方法明确不是原 `Mf.s()` 执行。
3. `LY(...)` 构造器会建立 `kB`，并经 `RO/FI` 派生图标状态。测试用 Unsafe 仅分配对象，反射填入字节码已证字段：`LY.a/b` 为 3／21−3×slotID，`c/f` 为真实 `FM/GB`，`d` 为真实 `Some(parent)`，`g` 为测试分配的真实 `kB`，`h` 为 8 个真实 tuple。**未声称原 LY 构造器或 flags 派生执行**。
4. 真实 `LY.m()` 还依赖 `jA`；后者静态初始化会经 `iE/aga.toString -> XK` 读取 normally-boot-populated registry。初次隔离尝试因 `XK.b()==null` 明确失败。最终在 guard 内用**真实空 vector**初始化 XK 四注册表；没有调用游戏 bootstrap。`FI` 和 `Fr.e` 也用真实空 set/map。这样继续执行真实 formatter，而不是手写两行返回值。此合成数据只证明原 `SORTIE   000%` 回退，不证明真实地点翻译或完成率数据。
5. `LV` 同样只分配／填字段；原 `LV.a(Mf)/b(Mf)` 与 `LW` collect 照常执行。IG 使用反射精确调用 **`static LV.a(SN)V`**：`"REALLY CLEAR FILE?" -> ams.a(String) -> SN.a(text,32,94,SN.b())`。它不读取字典、不调用 `Id` 逐字绘制。**绝不调用 `LV.d(LV)`**，后者才进入 `Hi.a(slot)` 删除服务。
6. `arp.a(aqX,false)` **真实解析 FNT**；仅 `arp` 外壳用 Unsafe 分配，再填 `arp.a`，避免纹理构造。无假 font class、假 metrics 或假 glyph 数据。
7. `Iu/LX/GB/FM/FI/IA/IG/SL`、原 collection 与 tuple 使用真实构造器。IA 的标签数据是合成中文，渲染使用真实 `IB` 整行；不把它们当正式 UI 字典翻译验证。所有动作 thunk 不执行。

Unsafe 和反射仅存在于这份测试探针，不进入运行时适配、构建 bundle 或候选 JAR。没有展开游戏 class；Windows 上 `Iu/iu`、`amn/amN` 仍由 JAR 精确 entry 解析。

## 真正执行的方法

- **真实改后 `Mf.b(SN)`**：原背景调用、`SaveMenuLayout.begin`、原 `ZJ` 遍历、`end`／异常 finally 均执行。不是手工调用 begin 模拟整帧。
- **真实改后 `LX.b(SN)`、`LY.b(SN)`、`Iu.a(SN,ZH,float)`**：off 时 hook 返回 false，执行保留的原绘制方法体；on 时执行改后入口及候选 hook，选中卡片走候选，其他槽被明确抑制。因此 on **不等于旧 LY.b 绘制体也执行**。
- **真实未复制的 `LY.m()`**：姓名原规则、`Id` 数字补齐、`QL` 等级、`jA` 完成率路径、`Ov` 十六进制、SORTIE 回退。实际得到 `LVL025 TRY999` 和高／低 `7FFF`／`FFFF`，不是日期。原等级表上限为 25；没有伪造 LVL999 冒称原 formatter 输出。
- 原 `Mf.R/Q`、`Mo.a/b`、`LV.a/b`、`LW` 目标过滤、selector 选中对象路径及真实闪烁门。正常 R=7/Q=0；删除 R=2/Q=目标 LY＋IG。删除目标永远是 ID2，与取消／删除按钮 index0/1 无关。
- 原 `Id` 逐字 off 绘制、RN 性别图标选择、`LY.n()` 读取真实 tuple、真实 `IB/IA` 绘制。
- **原 `arr.a(arp,CharSequence,int,int,ara,float,int,boolean,String)` CPU glyph-run builder** 对每个录制 text 调用都实际执行。glyph identity、完整 code unit 数逐项断言。JSON 直接输出原 runs/advances；只有 quad 最后位置依照已证 arq 公式推导，没有执行 arq cache、纹理、Yg 或 GL。

## 场景与断言

- 正常模式 **全部 7 个选中 index**，各 off/on 对照；保留 3 槽＋4 动作，不把 index 当槽 ID。
- 槽0：8 中文姓名 `宇宙育种探索先锋`、TRY999、原最高等级025、8 flags 全 true。
- 槽1：真实 LX 空槽；槽2：8 code unit 混排 `宇宙AB探索CD`、flags `0xAA`，只画原顺序中对应4图标。
- 非槽动作 index3/4/5/6：候选始终展示最低槽 ID0，光标保留动作原坐标。
- LV 目标 ID2：两个按钮各 off 可见／on 可见／on 隐藏，执行真实 `Id.a(time,5)` 闪烁相位。
- 9 中文姓名明确 overflow：记录 `EXPECTED_REJECTION`；它不是适配成功。真实 `Mf.b` finally 清除 ThreadLocal，随后直接 `LX.b` 再次发出28个原逐字调用，而非候选空槽串，证明异常上下文没有泄漏。
- 录制共22场景、1450个原始SN绘制调用；所有 draw overload 都记录，`kind:other` 为0。最终独立结构检查确认仅1个预期 overflow，其余场景状态均 PASS，冻结 SHA 未变。

## JSON / 离线重放契约

顶层 `schema_version:1,width:256,height:224,font,scenarios`。字体记录真实 ascent=1、padLeft=1、scaleX=scaleY=1、lineHeight=14 与双资源 SHA。

每场景有 `id/prototype/selected_index/selected_slot/mode/time/status/calls`。每个原始 SN void 调用保留 `method/args/scenario/selected_slot/original_methods`；text 另有 `text/x/y/font/quads/bounds_candidate`，image/rect 有 `name/x/y/width/height/bounds_candidate`。

`quads` 中 `codepoint/srcX/srcY/page/width/height` 来自真实 arp glyph，`original_arr_advance/original_arr_run_x/original_arr_run_y` 来自真实 arr。最后 `x/screenTop` 为原 arq 公式的 CPU 推导：

```text
penX = rawSN.x + run.x + accumulated(original_arr_advance)
quadLeft = round(penX + glyph.xoffset)
screenTop = 224 - round(rawSN.y + ascent + run.y + glyph.yoffset + glyph.height)
```

**原 SN 坐标 y 向上；这些 bounds 不是实际 clip、viewport、命中区或窗口坐标。** PNG 宽高是 glyph quad／图像候选尺寸，不暗示所有 glyph alpha 像素都占满。真实图像只记录资源名，不加载纹理；背景256×224、图标8×8为既有资产证据下的候选。父代理可据位图 alpha 做像素级碰撞，不应把 quad 空白区也算墨迹。

## Guard 与不执行事项

FNT／候选身份预读后、任何 scene/model 分支前安装内置测试 SM。已有 manager 时拒绝替换；不请求策略扩大。正向只允许 JRE、精确候选 JAR、FNT/PNG 和本探针输出目录读取；写入仅允许本探针目录，拒删除、进程、网络、native library、shutdownhook、manager 替换及无来源 FD。

- `guard_active=true`，**正向场景拒绝数0**。
- 8个直接 guard API 负例均拒绝：原安装 read/write、output 外 write、exec、network、native、manager 替换、shutdownhook；这些自检不实际读取／写入／启动任何对象，和正向拒绝数分列。
- 原安装路径仅用于 `checkRead/checkWrite` 的直接拒绝断言，未实际访问。
- 类加载日志无 `Hi/Tk/Main/Yg`。`SV` 因 SN 方法签名验证加载，但没有构造或调用；类加载不冒称原方法执行。
- 未启动游戏、Main、原生 GL、安装器或任何服务；未读写用户存档、配置或备份。SM 只是本次纯 Java 测试 tripwire，**不是 OS 安全沙箱，也不保护实际游戏／native 程序**。
- 测试编译和输出不依赖其他 guard 源文件。

## 可复现命令

在仓库根目录运行；输出目录须已存在，所有产物限制在该新子目录：

```bash
mkdir -p localization/work/layout-drawing-probe
localization/toolchains/microsoft-jdk17/jdk-17.0.20.1+1/bin/javac.exe \
  -J-Duser.language=en -J-Dfile.encoding=UTF-8 -source 8 -target 8 -encoding UTF-8 \
  -cp localization/builds/layout-r22-candidate-v2/cosmobreeder-multi.jar \
  -d localization/work/layout-drawing-probe/classes \
  localization/layout/validation/PRG/SaveDrawingProbe.java \
  > localization/work/layout-drawing-probe/compile.log 2>&1
research/testgame_cjk_verified/jre/bin/java.exe -Xverify:all -verbose:class \
  -Dfile.encoding=UTF-8 \
  -cp 'localization/work/layout-drawing-probe/classes;localization/builds/layout-r22-candidate-v2/cosmobreeder-multi.jar' \
  PRG.SaveDrawingProbe \
  localization/builds/layout-r22-candidate-v2/cosmobreeder-multi.jar \
  localization/runtime/bbc2.fnt localization/runtime/bbc2-cjk-10.png \
  localization/work/layout-drawing-probe \
  > localization/work/layout-drawing-probe/run.log 2>&1
```

最终日志：`SaveDrawingProbe PASS checks=3172 scenarios=22 output=save-drawing-recording.json`。JSON 写入同目录临时文件后原子 replace，父代理只消费上述冻结 SHA。

## 发现与仍未覆盖

1. **未发现本轮真实单卡片方法在这些夹具下的新增执行缺陷**：8中文／混排、数值、图标、非槽动作、LV目标与 finally 都通过；这不等于已通过像素碰撞或发行验收。
2. 早期合成 IG 用 `Id`＋中文标题产生逐字8px碰撞，是**测试夹具假阳性**，最终已改成真实 LV caption，不能据早期截图修改生产补丁。候选真实 caption 仍为硬编码英文整行，不能声称它来源于中文 UI 字典。
3. 原 off 的固定8px逐字路径与10px字体在同一真实夹具下完整录制，可由父代理重放对比；本探针本身不生成预览或宣称 CRT 可读性。
4. 真实存档数据、8中文地点／非回退完成率、额外名字／数据域、Mp/Ms过滤输入、游戏实际 clip／CRT／键鼠手柄连续操作都未覆盖。无用户存档依赖是安全边界，不得把合成覆盖扩写成真实存档验收。
5. 9中文姓名保留原值后显式 overflow，仍需产品侧处理超出候选84px字段的合法数据域；没有截断、省略、缩小字体或吞异常。
