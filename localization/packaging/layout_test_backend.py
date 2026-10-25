"""Isolated layout-test policy; the original backend remains the install engine."""
import base_patch_tool as _base
from base_patch_tool import *  # Preserve the launcher's existing public API.

_PATHS = ("cosmobreeder-multi.jar", "patch.pak")
_install, _uninstall, _check = _base.cmd_install, _base.cmd_uninstall, _base.cmd_check


def _fixed(root, name):
    path = os.path.join(os.path.realpath(root), name)
    if os.path.realpath(path) != path:
        raise ValueError("拒绝链接或路径漂移：" + path)
    return path


def _manifest():
    man = load_manifest()
    for var in variants_of(man).values():
        files = var.get("files", [])
        names = [e["path"] for e in files]
        if not names or len(names) != len(set(names)) or any(p not in _PATHS for p in names):
            raise ValueError("manifest 只允许两个固定游戏路径")
        for e in files:
            if e["payload"] != e["path"]:
                raise ValueError("manifest payload 路径漂移")
        if any(p not in _PATHS for p in var.get("detect", {})):
            raise ValueError("manifest detect 路径漂移")
    return man


def verify_payload():
    """Read only embedded resources; never discover or access an installation."""
    man, files = _manifest(), {}
    for e in all_files_map(man).values():
        actual = sha256(_fixed(PAYLOAD, e["payload"]))
        if actual != e["sha256"]:
            raise ValueError("补丁包已损坏：" + e["payload"])
        files[e["path"]] = actual
    if any(e["sha256"] != files[e["path"]] for v in variants_of(man).values() for e in v["files"]):
        raise ValueError("manifest 的同路径 payload SHA 不一致")
    return {"version": man["version"], "sha256": files, "files": files,
            "activation": man.get("activation", "layout-test"), "status": man.get("status", "verified"),
            "game_started": False, "installed": False}


def _context(args):
    if getattr(args, "force", False) or getattr(args, "backup_dir", None):
        raise ValueError("测试版禁止 --force 和自定义备份目录")
    man = _manifest()
    game = os.path.realpath(resolve_game(args))
    for name in (*_PATHS, STATE_NAME, BACKUP_DIRNAME):
        _fixed(game, name)
    bdir = _fixed(game, BACKUP_DIRNAME)
    for name in _PATHS:
        _fixed(bdir, name)
    args.game_dir = game  # Pin discovery once; the reused engine must target this same game.
    return game, man, bdir


def cmd_install(args):
    game, man, bdir = _context(args)
    sp = _fixed(game, STATE_NAME)
    if os.path.lexists(sp):
        raise ValueError("已有测试版状态记录；禁止覆盖（包括损坏的状态）")
    verify_payload()
    _, var, _ = pick_variant(man, game)
    if not var or not var.get("available", True):
        raise ValueError("不支持的游戏版本")
    for e in var["files"]:
        dst, bp = _fixed(game, e["path"]), _fixed(bdir, e["path"])
        if sha256(dst) != e["original"]["sha256"]:
            raise ValueError("源文件 SHA 不匹配：" + e["path"])
        if os.path.exists(bp) and sha256(bp) != sha256(dst):
            raise ValueError("旧测试备份 SHA 不匹配：" + e["path"])
    paths = [sp] + [_fixed(game, e["path"]) for e in var["files"]]
    paths += [_fixed(bdir, e["path"]) for e in var["files"]]
    before = {}
    for path in paths:
        with io.open(path, "rb") if os.path.exists(path) else io.BytesIO() as f:
            before[path] = f.read() if os.path.exists(path) else None
    had_bdir = os.path.isdir(bdir)
    source_hashes = {e["path"]: e["original"]["sha256"] for e in var["files"]}
    write_before = _base.write_state
    def write_exact_source(target, state):
        return write_before(target, dict(state, source_sha256=source_hashes))
    _base.write_state = write_exact_source
    try:
        return _install(args)
    except BaseException as error:
        failures = []
        for path, data in before.items():
            try:
                if _fixed(os.path.dirname(path), os.path.basename(path)) != path:
                    raise ValueError("rollback 路径漂移")
                if data is None:
                    if os.path.lexists(path):
                        os.remove(path)
                else:
                    if os.path.isfile(path):
                        with io.open(path, "rb") as current:
                            if current.read() == data:
                                continue  # Never rewrite untouched files after a backup/preflight failure.
                    with io.open(path, "wb") as f:
                        f.write(data)
            except BaseException as rollback_error:
                failures.append(str(rollback_error))
        if not had_bdir and os.path.isdir(bdir):
            try:
                if _fixed(game, BACKUP_DIRNAME) != bdir:
                    raise ValueError("rollback 备份路径漂移")
                os.rmdir(bdir)
            except OSError as rollback_error:
                failures.append(str(rollback_error))
        if failures:
            raise RuntimeError("安装失败且 rollback 失败：" + "; ".join(failures)) from error
        raise
    finally:
        _base.write_state = write_before


def cmd_uninstall(args):
    game, man, bdir = _context(args)
    state, _ = read_state(game)
    if not isinstance(state, dict):
        raise ValueError("测试版安装记录格式无效")
    defs = all_files_map(man)
    names = state.get("files", [])
    if (not state or state.get("patch") != man["name"] or state.get("version") != man["version"]
            or names not in [list(e["path"] for e in v["files"]) for v in variants_of(man).values()]
            or state.get("sha256") != {p: defs[p]["sha256"] for p in names}
            or state.get("backup_dir") != bdir):
        raise ValueError("缺少本测试版的有效安装记录；拒绝还原陌生备份")
    recorded_sources = state.get("source_sha256")
    if not isinstance(recorded_sources, dict) or set(recorded_sources) != set(names):
        raise ValueError("缺少安装前的精确来源 SHA；拒绝推断还原版本")
    skipped = False
    for p in names:
        bp, dst = _fixed(bdir, p), _fixed(game, p)
        sources = {e["original"]["sha256"] for v in variants_of(man).values() for e in v["files"] if e["path"] == p}
        if recorded_sources[p] not in sources:
            raise ValueError("来源记录不属于支持的版本：" + p)
        if not os.path.isfile(bp):
            skipped = True
            continue
        backup_sha = sha256(bp)
        if backup_sha != recorded_sources[p]:
            raise ValueError("备份 SHA 不属于本次安装前的精确版本：" + p)
        skipped |= os.path.isfile(dst) and sha256(dst) not in {defs[p]["sha256"], backup_sha}
    mapping_before = _base.all_files_map
    def exact_originals(manifest):
        return {p: dict(e, original=dict(e["original"], sha256=recorded_sources.get(p, e["original"]["sha256"])))
                for p, e in mapping_before(manifest).items()}
    _base.all_files_map = exact_originals
    try:
        result = _uninstall(args)
        return result if result else int(skipped)
    finally:
        _base.all_files_map = mapping_before


def cmd_check(args):
    _manifest()
    return _check(args)


_base.cmd_install, _base.cmd_uninstall, _base.cmd_check = cmd_install, cmd_uninstall, cmd_check
