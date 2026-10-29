"""Only fixed game binaries and installer-owned backup/state are accessed."""
import json
import os
from pathlib import Path
import shutil
import subprocess
import tempfile
from .delta import sha, apply, validate_entry, MAX_TOTAL

NAMES = ('cosmobreeder-multi.jar', 'patch.pak')
BACKUP = '_cosmobreeder_alpha0.1_backup'
STATE = 'cosmobreeder-alpha0.1-state.json'

def fixed(root, name):
    p = Path(root) / name
    if p.is_symlink() or p.resolve() != p.absolute():
        raise ValueError('拒绝链接/路径漂移: ' + str(p))
    return p

def manifest(payload):
    path = fixed(payload, 'manifest.json')
    if path.stat().st_size > 1024 * 1024:
        raise ValueError('manifest过大')
    m = json.loads(path.read_text('utf-8'))
    if not isinstance(m, dict) or m.get('version') != 'alpha0.1' or not isinstance(m.get('files'), dict) or set(m['files']) != set(NAMES):
        raise ValueError('manifest格式无效')
    for name, e in m['files'].items():
        validate_entry(e)
        if e.get('delta') != name + '.cbd':
            raise ValueError('manifest路径无效')
    for field in ('source_size', 'target_size', 'delta_size'):
        if sum(e[field] for e in m['files'].values()) > MAX_TOTAL:
            raise ValueError('manifest总大小越界')
    return m

def verify(payload):
    m = manifest(payload)
    for e in m['files'].values():
        delta = fixed(payload, e['delta'])
        if delta.stat().st_size != e['delta_size'] or sha(delta) != e['delta_sha256']:
            raise ValueError('差分负载损坏')
    return m

def running_guard():
    if os.name == 'nt':
        result = subprocess.run(['tasklist', '/FO', 'CSV', '/NH'], capture_output=True, check=True)
        rows = result.stdout.lower()
        if any(b'"' + x + b'"' in rows for x in (b'java.exe', b'javaw.exe', b'cosmobreeder.exe')):
            raise ValueError('请先关闭游戏及Java进程')

def context(game):
    game = Path(game).absolute()
    if not game.is_dir() or game.resolve() != game:
        raise ValueError('游戏目录无效或为链接')
    for n in (*NAMES, BACKUP, STATE):
        fixed(game, n)
    for n in NAMES:
        fixed(game / BACKUP, n)
    return game

def detect(game, m):
    game = context(game)
    if (game / STATE).exists():
        return 'installed'
    names = NAMES if (game / NAMES[1]).exists() else NAMES[:1]
    for n in names:
        if not (game / n).is_file() or sha(game / n) != m['files'][n]['source_sha256']:
            raise ValueError('不支持的源文件: ' + n)
    return 'nsfw' if len(names) == 2 else 'vanilla'

def sync_file(path):
    with open(path, 'rb+') as f:
        f.flush()
        os.fsync(f.fileno())

def sync_copy(source, target):
    with open(source, 'rb') as src, open(target, 'wb') as dst:
        shutil.copyfileobj(src, dst, 1024 * 1024)
        dst.flush()
        os.fsync(dst.fileno())

def write_json(path, value):
    with open(path, 'w', encoding='utf-8') as f:
        json.dump(value, f)
        f.flush()
        os.fsync(f.fileno())

def install(game, payload):
    m = verify(payload)
    game = context(game)
    variant = detect(game, m)
    if variant == 'installed':
        raise ValueError('已有安装记录，拒绝重复安装')
    if (game / BACKUP).exists():
        raise ValueError('已有备份目录，拒绝覆盖')
    running_guard()
    names = NAMES if variant == 'nsfw' else NAMES[:1]
    # Reconstruct all outputs before modifying any original or creating backups.
    with tempfile.TemporaryDirectory(prefix='cbdelta-') as temp:
        temp = Path(temp)
        for n in names:
            apply(game / n, fixed(payload, m['files'][n]['delta']), temp / n, m['files'][n])
        backup = game / BACKUP
        replaced = []
        backup.mkdir()
        try:
            for n in names:
                shutil.copy2(game / n, backup / n)
                if sha(backup / n) != m['files'][n]['source_sha256']:
                    raise ValueError('备份校验失败')
                with open(backup / n, 'rb+') as backed_up:
                    os.fsync(backed_up.fileno())
            state = {'version': 'alpha0.1', 'variant': variant, 'files': list(names),
                     'source': {n: m['files'][n]['source_sha256'] for n in names},
                     'target': {n: m['files'][n]['target_sha256'] for n in names}}
            write_json(backup / 'transaction.json', state)
            for n in names:
                # Stage in same filesystem for atomic replace; original retained in backup.
                stage = backup / (n + '.new')
                sync_copy(temp / n, stage)
                if sha(game / n) != state['source'][n]:
                    raise ValueError('源文件在安装期间变化')
                replaced.append(n)  # Include even replace-then-interrupt failures.
                os.replace(stage, game / n)
            write_json(backup / 'state.new', state)
            os.replace(backup / 'state.new', game / STATE)
        except BaseException:
            for n in reversed(replaced):
                if sha(game / n) not in (state['source'][n], state['target'][n]):
                    raise RuntimeError('回滚遇到未知文件，保留备份供人工核对')
                sync_copy(backup / n, game / n)
            for n in replaced:
                sync_file(game / n)
                if sha(game / n) != state['source'][n]:
                    raise RuntimeError('回滚校验失败，保留备份')
            if (game / STATE).exists():
                (game / STATE).unlink()
            shutil.rmtree(backup)
            raise
    return variant

def uninstall(game, payload):
    m = verify(payload)
    game = context(game)
    running_guard()
    backup = game / BACKUP
    sp = game / STATE
    # A durable transaction journal also permits recovery after abrupt termination.
    journal = fixed(backup, 'transaction.json')
    state = json.loads((sp if sp.exists() else journal).read_text('utf-8'))
    names = state.get('files')
    if state.get('version') != 'alpha0.1' or names not in [list(NAMES), list(NAMES[:1])]:
        raise ValueError('无效安装记录')
    for n in names:
        if state.get('source', {}).get(n) != m['files'][n]['source_sha256'] or state.get('target', {}).get(n) != m['files'][n]['target_sha256']:
            raise ValueError('安装记录SHA无效')
        if sha(fixed(backup, n)) != state['source'][n]:
            raise ValueError('原版备份损坏')
        if sha(game / n) not in (state['source'][n], state['target'][n]):
            raise ValueError('当前文件被其他程序改动，拒绝覆盖')
    allowed = {'transaction.json', 'state.new'} | set(names) | {n + suffix for n in names for suffix in ('.new', '.restore')}
    if any(p.name not in allowed or p.is_symlink() or not p.is_file() for p in backup.iterdir()):
        raise ValueError('备份目录含未知文件或链接，拒绝清理')
    # Backups/journal retained until all restores succeed, making retries safe.
    for n in names:
        stage = fixed(backup, n + '.restore')
        sync_copy(backup / n, stage)
        # Re-check immediately before replacement; never overwrite a new unknown edit.
        if sha(game / n) not in (state['source'][n], state['target'][n]):
            raise ValueError('还原期间文件变化，保留备份')
        os.replace(stage, game / n)
        sync_file(game / n)
    for n in names:
        if sha(game / n) != state['source'][n]:
            raise ValueError('还原结果校验失败，保留备份')
    if sp.exists():
        sp.unlink()
    shutil.rmtree(backup)
    return 'restored'
