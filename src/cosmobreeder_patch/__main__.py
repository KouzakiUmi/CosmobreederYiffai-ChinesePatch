import argparse
import json
import os
from pathlib import Path
import sys
from cosmobreeder_patch import installer as engine

def license_text():
    base = Path(getattr(sys, '_MEIPASS', Path(__file__).parent)).absolute()
    if not hasattr(sys, '_MEIPASS') and base.parent.name == 'src':
        base = base.parent.parent
    def checked(path):
        if path.is_symlink() or path.resolve() != path.absolute():
            raise ValueError('拒绝链接许可证: ' + str(path))
        return path
    checked(base)
    files = [checked(base / name) for name in ('LICENSE', 'NOTICE', 'THIRD_PARTY_NOTICES.md')]
    directory = checked(base / 'licenses')
    for root, dirs, names in os.walk(directory, followlinks=False):
        for name in dirs:
            checked(Path(root) / name)
        files += [checked(Path(root) / name) for name in sorted(names)]
    if not all(f.is_file() for f in files) or len(files) < 4:
        raise ValueError('缺少许可证目录或根声明')
    return '\n\n'.join(f.relative_to(base).as_posix() + '\n' + f.read_text('utf-8') for f in files)

def main():
    p = argparse.ArgumentParser(description='Cosmobreeder 简体中文差分补丁 alpha0.1 预发行')
    p.add_argument('--payload', type=Path, default=Path(getattr(sys, '_MEIPASS', Path(__file__).parent)) / 'payload')
    p.add_argument('--game-dir', type=Path)
    group = p.add_mutually_exclusive_group()
    for action in ('verify-payload', 'check', 'install', 'uninstall', 'licenses'):
        group.add_argument('--' + action, action='store_true')
    args = p.parse_args()
    if args.licenses:
        print(license_text())
        return
    if args.verify_payload:
        m = engine.verify(args.payload)
        print(json.dumps({'version': m['version'], 'status': 'verified', 'game_started': False}))
        return
    if any((args.check, args.install, args.uninstall)):
        if not args.game_dir:
            p.error('需要 --game-dir')
        if args.check:
            print(engine.detect(args.game_dir, engine.verify(args.payload)))
        elif args.install:
            print(engine.install(args.game_dir, args.payload))
        else:
            print(engine.uninstall(args.game_dir, args.payload))
        return
    import tkinter as tk
    from tkinter import filedialog, messagebox
    root = tk.Tk()
    root.title('Cosmobreeder 简中补丁 alpha0.1（预发行）')
    selected = tk.StringVar()
    tk.Label(root, text='请选择含 cosmobreeder-multi.jar 的目录。\n不会启动游戏，不访问存档；请先关闭游戏和Java。').pack(padx=20, pady=12)
    tk.Entry(root, textvariable=selected, width=65).pack(padx=12)
    def browse():
        path = filedialog.askdirectory()
        if path:
            selected.set(path)
    tk.Button(root, text='选择游戏目录', command=browse).pack(pady=5)
    def action(name):
        try:
            game = Path(selected.get())
            if not selected.get():
                raise ValueError('请先选择游戏目录')
            if name == 'check':
                result = engine.detect(game, engine.verify(args.payload))
            else:
                result = getattr(engine, name)(game, args.payload)
            messagebox.showinfo('结果', str(result))
        except Exception as e:
            messagebox.showerror('操作未完成', str(e))
    for label, name in [('检测档位', 'check'), ('安装汉化', 'install'), ('还原 / 中断恢复', 'uninstall')]:
        tk.Button(root, text=label, command=lambda n=name: action(n)).pack(pady=4)
    def show_licenses():
        window = tk.Toplevel(root)
        window.title('第三方许可与声明')
        text = tk.Text(window, width=90, height=30, wrap='word')
        text.pack(fill='both', expand=True)
        text.insert('1.0', license_text())
        text.configure(state='disabled')
    tk.Button(root, text='第三方许可与声明', command=show_licenses).pack(pady=4)
    root.mainloop()

if __name__ == '__main__':
    try:
        main()
    except Exception as error:
        print(str(error), file=sys.stderr)
        sys.exit(1)
