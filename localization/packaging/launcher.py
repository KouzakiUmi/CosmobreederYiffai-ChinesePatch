# -*- coding: utf-8 -*-
"""Cosmobreeder Yiffai 中文汉化补丁 —— 图形安装器。

打包成 exe 后用双击运行，不需要装 Python。界面只做三件事：
找游戏目录、按按钮跑 patch_tool、把输出显示出来。

设计上照 Winds of Change / FizRP 的汉化补丁安装器：控制台输出重定向到窗口里的滚动区，
后台线程执行避免卡界面，出错时提示日志路径。
"""
import contextlib
import logging
import os
import platform
import queue
import sys
import threading
import tkinter as tk
from tkinter import filedialog, messagebox, scrolledtext, ttk

import patch_tool

APP_NAME = "Cosmobreeder Yiffai 简体中文补丁"


def log_path():
    base = os.environ.get("LOCALAPPDATA") or os.path.expanduser("~")
    folder = os.path.join(base, "CosmobreederYiffaiCN", "logs")
    os.makedirs(folder, exist_ok=True)
    return os.path.join(folder, "installer.log")


class QueueWriter:
    def __init__(self, target):
        self.target = target

    def write(self, value):
        if value:
            self.target.put(value)
        return len(value)

    def flush(self):
        pass


class App(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title(APP_NAME)
        self.geometry("760x600")
        self.minsize(680, 520)
        self.events = queue.Queue()
        self.busy = False
        self.log_file = log_path()
        logging.basicConfig(filename=self.log_file, filemode="a", encoding="utf-8",
                            level=logging.DEBUG,
                            format="%(asctime)s %(levelname)s %(message)s")
        self.game_dir = tk.StringVar()
        self.status = tk.StringVar(value="就绪。点「自动查找」或手动选择游戏目录。")
        self._build()
        self.after(80, self._drain)

    # ------------------------------------------------------------------ UI
    def _build(self):
        pad = {"padx": 10, "pady": 6}

        head = ttk.Frame(self)
        head.pack(fill="x", **pad)
        ttk.Label(head, text=APP_NAME,
                  font=("Microsoft YaHei UI", 13, "bold")).pack(anchor="w")
        ttk.Label(head, text="把游戏文本和四张图换成中文。只改两个文件，安装前自动备份。",
                  foreground="#555").pack(anchor="w", pady=(2, 0))

        box = ttk.LabelFrame(self, text="游戏目录")
        box.pack(fill="x", **pad)
        row = ttk.Frame(box)
        row.pack(fill="x", padx=8, pady=8)
        ttk.Entry(row, textvariable=self.game_dir).pack(side="left", fill="x", expand=True)
        ttk.Button(row, text="自动查找", command=self._auto_find).pack(side="left", padx=(8, 0))
        ttk.Button(row, text="浏览…", command=self._browse).pack(side="left", padx=(6, 0))

        ttk.Label(box, text="应包含 cosmobreeder-multi.jar 和 patch.pak 的那一层目录。",
                  foreground="#777").pack(anchor="w", padx=8, pady=(0, 8))

        btns = ttk.Frame(self)
        btns.pack(fill="x", **pad)
        self.buttons = []
        for text, cmd in (("安装", "install"), ("检查", "check"), ("卸载 / 还原", "uninstall")):
            b = ttk.Button(btns, text=text, width=14,
                           command=lambda c=cmd: self._run(c))
            b.pack(side="left", padx=(0, 8))
            self.buttons.append(b)
        ttk.Button(btns, text="打开日志", command=self._open_log).pack(side="right")

        self.progress = ttk.Progressbar(self, mode="indeterminate")
        self.progress.pack(fill="x", padx=10)

        ttk.Label(self, textvariable=self.status, foreground="#333").pack(anchor="w", padx=10, pady=(4, 0))

        area = ttk.LabelFrame(self, text="运行记录")
        area.pack(fill="both", expand=True, padx=10, pady=(6, 10))
        self.log = scrolledtext.ScrolledText(area, height=18, wrap="word",
                                             font=("Consolas", 9))
        self.log.pack(fill="both", expand=True, padx=6, pady=6)
        self.log.configure(state="disabled")

        self._append("Python %s / frozen=%s\n日志文件：%s\n"
                     % (platform.python_version(), bool(getattr(sys, "frozen", False)), self.log_file))

    def _append(self, text):
        self.log.configure(state="normal")
        self.log.insert("end", text)
        self.log.see("end")
        self.log.configure(state="disabled")

    def _drain(self):
        try:
            while True:
                item = self.events.get_nowait()
                if isinstance(item, tuple) and item and item[0] == "__DONE__":
                    self._finish(item[1], item[2])
                else:
                    self._append(str(item))
        except queue.Empty:
            pass
        self.after(80, self._drain)

    # --------------------------------------------------------------- 动作
    def _auto_find(self):
        found = patch_tool.find_game()
        if not found:
            self.status.set("没自动找到。请手动点「浏览…」选择游戏根目录。")
            messagebox.showwarning("没找到游戏",
                                   "没能自动定位游戏目录。\n\n"
                                   "请点「浏览…」，选到包含 cosmobreeder-multi.jar 的那一层。")
            return
        self.game_dir.set(found[0])
        self._append("自动找到：%s\n" % found[0])
        if len(found) > 1:
            self._append("（另有 %d 处，使用第一个）\n" % (len(found) - 1))
        self.status.set("已定位游戏目录，可以点「安装」了。")

    def _browse(self):
        d = filedialog.askdirectory(title="选择 Cosmobreeder Yiffai 游戏根目录")
        if d:
            self.game_dir.set(d)
            err = patch_tool.check_game_dir(d)
            if err:
                self.status.set("这个目录看起来不对：" + err)
            else:
                self.status.set("目录有效，可以点「安装」了。")

    def _open_log(self):
        try:
            os.startfile(self.log_file)
        except Exception as exc:
            messagebox.showerror("打不开日志", "%s\n\n路径：%s" % (exc, self.log_file))

    def _run(self, command):
        if self.busy:
            return
        if command == "install" and not self.game_dir.get().strip():
            self._auto_find()
            if not self.game_dir.get().strip():
                return
        if command == "uninstall":
            if not messagebox.askyesno("确认卸载", "将用安装时的备份还原成原版。继续吗？"):
                return
        argv = [command]
        gd = self.game_dir.get().strip()
        if gd:
            argv += ["--game-dir", gd]
        self.busy = True
        self.status.set("正在执行：%s …" % command)
        self.progress.start(12)
        for b in self.buttons:
            b.state(["disabled"])
        self._append("\n=== %s ===\n" % command)
        threading.Thread(target=self._worker, args=(argv,), daemon=True).start()

    def _worker(self, argv):
        result, old = 1, sys.argv
        try:
            sys.argv = [sys.argv[0]] + argv
            w = QueueWriter(self.events)
            with contextlib.redirect_stdout(w), contextlib.redirect_stderr(w):
                try:
                    patch_tool.main()
                    result = 0
                except SystemExit as exc:
                    if isinstance(exc.code, int):
                        result = exc.code
                    elif exc.code:
                        print(str(exc.code))
                        result = 1
                    else:
                        result = 0
        except Exception:
            logging.exception("unhandled")
            self.events.put("未处理错误：\n" + __import__("traceback").format_exc())
            result = 1
        finally:
            sys.argv = old
            self.events.put(("__DONE__", result, argv[0]))

    def _finish(self, result, command):
        self.busy = False
        self.progress.stop()
        for b in self.buttons:
            b.state(["!disabled"])
        if result == 0:
            msg = {"install": "安装完成，启动游戏就是中文。",
                   "uninstall": "已还原成原版。",
                   "check": "检查完成，详情见运行记录。"}.get(command, "完成。")
            self.status.set(msg)
            messagebox.showinfo("完成", msg)
        else:
            self.status.set("没有完成，请看运行记录。")
            messagebox.showerror("操作未完成",
                                 "没能完成。请查看窗口里的运行记录，\n"
                                 "或点「打开日志」看完整信息。\n\n日志：%s" % self.log_file)


def main():
    App().mainloop()


if __name__ == "__main__":
    main()
