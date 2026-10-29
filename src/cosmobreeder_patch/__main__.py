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
    p.add_argument('--selftest', action='store_true', help='构建图形界面并校验载荷后自动退出，不安装')
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
    from cosmobreeder_patch.gui import run
    run(args.payload, license_text, initial=args.game_dir, selftest=args.selftest)

if __name__ == '__main__':
    try:
        main()
    except Exception as error:
        print(str(error), file=sys.stderr)
        sys.exit(1)
