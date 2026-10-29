"""FizRP-inspired offline installer shell; all file mutations stay in engine."""
import queue
import threading
from pathlib import Path
import tkinter as tk
from tkinter import filedialog, messagebox, scrolledtext, ttk
from . import installer as engine
from . import discovery

COLORS = {'sky': '#e9f4fe', 'ink': '#28485c', 'mint': '#d8f3e5', 'paper': '#fbfdff'}
LABELS = {'check': '检测游戏版本', 'install': '安装中文补丁', 'uninstall': '卸载并还原', 'verify': '自检补丁载荷'}


def run(payload, license_text, initial=None, selftest=False):
    root = tk.Tk()
    root.title('Cosmobreeder Yiffai · 简体中文补丁 alpha0.1（预发行）')
    root.geometry('860x650')
    root.minsize(760, 580)
    root.configure(bg=COLORS['sky'])
    style = ttk.Style(root)
    style.theme_use('clam')
    style.configure('TFrame', background=COLORS['sky'])
    style.configure('TLabel', background=COLORS['sky'], foreground=COLORS['ink'], font=('Microsoft YaHei UI', 10))
    style.configure('Title.TLabel', font=('Microsoft YaHei UI', 20, 'bold'))
    style.configure('TButton', font=('Microsoft YaHei UI', 10), padding=8)
    style.configure('Primary.TButton', background=COLORS['mint'])
    frame = ttk.Frame(root, padding=24)
    frame.pack(fill='both', expand=True)
    ttk.Label(frame, text='Cosmobreeder Yiffai', style='Title.TLabel').pack(anchor='w')
    ttk.Label(frame, text='简体中文补丁 · 安装前核对原版，自动备份；需要时安全还原').pack(anchor='w', pady=(4, 14))
    ttk.Label(frame, text='预发行候选版｜请先关闭游戏及 Java。不会启动游戏，不访问存档。\n已有旧补丁时，请先用对应旧安装器还原；不要删除原有备份。', wraplength=760).pack(anchor='w', pady=(0, 16))
    selected = tk.StringVar(value=str(initial) if initial else '')
    ttk.Label(frame, text='游戏目录（包含 cosmobreeder-multi.jar）').pack(anchor='w')
    row = ttk.Frame(frame)
    row.pack(fill='x', pady=6)
    entry = ttk.Entry(row, textvariable=selected)
    entry.pack(side='left', fill='x', expand=True)
    def auto_find():
        if busy:
            return
        set_busy(True)
        status.set('正在自动查找游戏目录…')
        append('查找 Steam 常见位置、注册表及多库配置，以及安装器附近目录；不扫描存档。')
        def worker():
            try:
                events.put((True, discovery.find_game()))
            except Exception as error:
                events.put((False, '目录查找失败：' + str(error)))
        threading.Thread(target=worker, daemon=True).start()
    auto_button = ttk.Button(row, text='自动查找', command=auto_find)
    auto_button.pack(side='left', padx=(8, 0))
    def browse():
        value = filedialog.askdirectory(parent=root, title='选择游戏所在目录')
        if value:
            selected.set(value)
    browse_button = ttk.Button(row, text='浏览…', command=browse)
    browse_button.pack(side='right', padx=(8, 0))
    actions = ttk.Frame(frame)
    actions.pack(fill='x', pady=10)
    status = tk.StringVar(value='就绪 · 点“自动查找”或手动选择游戏目录，再检测档位')
    ttk.Label(frame, textvariable=status, wraplength=760).pack(anchor='w', pady=(4, 8))
    progress = ttk.Progressbar(frame, mode='indeterminate')
    progress.pack(fill='x')
    log = scrolledtext.ScrolledText(frame, height=12, wrap='word', bg=COLORS['paper'], fg=COLORS['ink'], font=('Microsoft YaHei UI', 10), state='disabled')
    log.pack(fill='both', expand=True, pady=12)
    events = queue.Queue()
    busy = False
    failed = False
    buttons = [browse_button, auto_button]
    def append(text):
        log.configure(state='normal')
        log.insert('end', text + '\n')
        log.see('end')
        log.configure(state='disabled')
    def set_busy(value):
        nonlocal busy
        busy = value
        for button in buttons:
            button.configure(state='disabled' if value else 'normal')
        entry.configure(state='disabled' if value else 'normal')
        if value:
            progress.start(12)
        else:
            progress.stop()
    def start(action):
        if busy:
            return
        value = selected.get().strip()
        if action != 'verify' and not value:
            auto_find()
            return
        if action in ('install', 'uninstall') and not messagebox.askyesno('确认操作', LABELS[action] + '？\n目标目录：' + value + '\n请确认已关闭游戏及 Java，并保留备份直到还原完成。', parent=root):
            return
        set_busy(True)
        status.set(LABELS[action] + '中，请稍候…')
        append(status.get())
        def worker():
            try:
                if action == 'verify':
                    manifest = engine.verify(payload)
                    result = '载荷完整，版本：' + manifest['version'] + '；内容基线：' + manifest.get('baseline', '未标注')
                elif action == 'check':
                    kind = engine.detect(Path(value), engine.verify(payload))
                    result = {'vanilla': '已识别：1.0.5_full 原版档（SFW），源 SHA-256 匹配；仅安装 JAR', 'nsfw': '已识别：1.0.5_full 官方 NSFW 补丁档，两文件源 SHA-256 匹配；安装 JAR + PAK', 'installed': '检测到安装记录；如需更新请先使用对应版本还原'}.get(kind, kind)
                else:
                    result = getattr(engine, action)(Path(value), payload)
                    result = {'restored': '还原完成，原版文件校验通过', 'vanilla': '安装完成（无 patch.pak）', 'nsfw': '安装完成（含 patch.pak）'}.get(result, result)
                events.put((True, str(result)))
            except Exception as error:
                events.put((False, str(error)))
        threading.Thread(target=worker, daemon=True).start()
    for action, label in LABELS.items():
        button = ttk.Button(actions, text=label, style='Primary.TButton' if action == 'install' else 'TButton', command=lambda a=action: start(a))
        button.pack(side='left', padx=(0, 6))
        buttons.append(button)
    def licenses():
        window = tk.Toplevel(root)
        window.title('许可与第三方声明')
        text = scrolledtext.ScrolledText(window, width=100, height=32, wrap='word')
        text.pack(fill='both', expand=True)
        try:
            text.insert('1.0', license_text())
        except Exception as error:
            text.insert('1.0', '许可读取失败：' + str(error))
        text.configure(state='disabled')
    ttk.Button(frame, text='许可与第三方声明', command=licenses).pack(anchor='e')
    def close():
        if busy:
            messagebox.showwarning('操作进行中', '请等待当前操作结束，避免中断文件写入。', parent=root)
        else:
            root.destroy()
    root.protocol('WM_DELETE_WINDOW', close)
    def found_directories(paths):
        if not paths:
            status.set('没自动找到游戏。请点“浏览…”手动选择包含 cosmobreeder-multi.jar 的目录。')
            append(status.get())
            return
        for path in paths:
            append('找到候选目录：' + str(path))
        choice = str(paths[0])
        if len(paths) > 1:
            window = tk.Toplevel(root)
            window.title('选择游戏目录')
            window.transient(root)
            window.grab_set()
            ttk.Label(window, text='发现多个候选目录，请选择要检测的一处：').pack(padx=16, pady=12)
            value = tk.StringVar(value=choice)
            ttk.Combobox(window, textvariable=value, values=[str(p) for p in paths], state='readonly', width=85).pack(padx=16, pady=8)
            picked = []
            def confirm():
                picked.append(value.get())
                window.destroy()
            ttk.Button(window, text='选择并检测档位', command=confirm).pack(pady=12)
            root.wait_window(window)
            if not picked:
                status.set('已取消选择；未修改游戏文件。')
                return
            choice = picked[0]
        selected.set(choice)
        append('已选目录：' + choice + '；继续校验原版／官方 NSFW 档，未执行安装。')
        root.after(0, lambda: start('check'))
    timer = None
    def cleanup(event):
        if event.widget is root and timer is not None:
            root.after_cancel(timer)
    root.bind('<Destroy>', cleanup, add='+')
    def drain():
        nonlocal failed, timer
        try:
            ok, text = events.get_nowait()
        except queue.Empty:
            pass
        else:
            failed = failed or not ok
            set_busy(False)
            if ok and isinstance(text, list):
                found_directories(text)
            else:
                status.set(('完成：' if ok else '操作未完成：') + text)
                append(status.get())
                if selftest:
                    root.after(200, root.destroy)
                elif not ok:
                    messagebox.showerror('操作未完成', text, parent=root)
        timer = root.after(80, drain)
    timer = root.after(80, drain)
    if selftest:
        root.after(100, lambda: start('verify'))
    root.mainloop()
    if failed and selftest:
        raise RuntimeError('安装界面自检失败')
