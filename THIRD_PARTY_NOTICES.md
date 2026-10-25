# 第三方声明

本项目不是原游戏，也不声称取得原游戏代码、文本、图片、音频或原有位图字体的再许可权。发行物是依赖用户合法持有的、SHA-256匹配的原文件才能应用的差分；不包含完整游戏JAR/PAK。

## Fusion Pixel Font（新增中文字体贡献）

- 来源：https://github.com/TakWolf/fusion-pixel-font
- 本次原生12px源：2026.10.16发行版 `fusion-pixel-12px-monospaced-zh_hans.bdf`。
- Copyright (c) 2022, TakWolf；SIL Open Font License 1.1。
- 主要许可：[完整OFL](<licenses/fonts/OFL.txt>)；[上游声明](<licenses/fonts/NOTICE.txt>)。
- 字库上游同时分发的组件许可：[Ark Pixel](<licenses/fonts/LICENSES/ark-pixel/OFL.txt>)、[Cubic 11](<licenses/fonts/LICENSES/cubic-11/OFL.txt>)、[Galmuri](<licenses/fonts/LICENSES/galmuri/LICENSE.txt>)。
- 上述许可覆盖对应的开源字体贡献，不覆盖原游戏ASCII位图、图集或其他原游戏资源。发行物不会单独提供含原游戏位图的组合字体；其变更通过源依赖差分应用。

## Windows独立安装器

源码运行版的应用逻辑只使用Python标准库；Windows独立EXE由Python和PyInstaller打包，并使用Tk图形界面。

- Python 3.12：Python Software Foundation License及其所含第三方声明，见[完整许可](<licenses/runtime/Python-LICENSE.txt>)，来源 https://www.python.org/ 。
- PyInstaller：GPL 2.0或更新版本，含允许发布应用可执行文件的bootloader例外，见[完整许可及例外](<licenses/runtime/PyInstaller-COPYING.txt>)，来源 https://pyinstaller.org/ 。原项目应用代码并不因该例外而自动改成GPL。
- Tcl 8.6.15 / Tk：独立BSD式许可与原作者声明；见[官方匹配版本的Tcl完整许可](<licenses/runtime/Tcl-license.terms>)、[随运行时分发的Tk许可](<licenses/runtime/Tk-license.terms>)及 https://www.tcl-lang.org/software/tcltk/license.html 。Tcl许可来源：https://github.com/tcltk/tcl/blob/core-8-6-15/license.terms 。

使用源码运行版时，请以所使用Python/Tcl/Tk发行版的实际许可为准。构建工具不属于原游戏，不提供任何原游戏再分发授权。

## 项目代码与翻译

本项目原创程序代码及项目文档适用[MIT许可](<LICENSE>)。翻译数据不改变其原作的版权归属，不应把MIT许可解释为对原游戏内容的许可。项目为非官方alpha，未承诺完全翻译、完整实机验收或稳定兼容所有版本。
