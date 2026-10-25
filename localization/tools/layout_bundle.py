"""Fail-closed consumer for an explicitly selected, isolated layout bundle.

The bundle is not a visual acceptance certificate. It can only be selected with
an explicit package CLI option; ordinary packaging remains unchanged.
"""
from __future__ import annotations
import hashlib
import json
import io
from pathlib import Path, PurePosixPath
from classfile import load
from codec import decrypt_file
from projectlib import parse_atlas
from PIL import Image


def sha(data):
    return hashlib.sha256(data).hexdigest()


def _safe_file(root, relative):
    name = PurePosixPath(relative)
    if name.is_absolute() or '..' in name.parts or '\\' in relative:
        raise ValueError('Unsafe layout bundle path')
    path = root.joinpath(*name.parts)
    if not path.resolve().is_relative_to(root.resolve()):
        raise ValueError('Layout bundle path escapes root')
    return path


COMPONENTS = {'vsn-opening', 'save-single-card', 'item-selected-detail'}
REQUIRED_HELPERS = {'PRG/LayoutBridge.class', 'PRG/VsnLayout.class',
                    'PRG/SaveMenuLayout.class', 'PRG/ItemMenuLayout.class',
                    'cosmoloc/layout/FontAccess.class', 'cosmoloc/layout/PixelLayout.class'}
BASELINE = Path(__file__).resolve().parents[1] / 'layout/baseline.json'


def class_dependencies(raw):
    cf = load(raw)
    dependencies = set()
    for index, (tag, value) in cf.cp.items.items():
        if tag == 7:
            name = cf.cp.cls(index).lstrip('[')
            if name.startswith('L') and name.endswith(';'): name = name[1:-1]
            if name.startswith(('PRG/', 'cosmoloc/layout/')): dependencies.add(name + '.class')
        elif tag == 1:
            # Descriptor-only references also need resolution (fields/parameters).
            import re
            for name in re.findall(r'L((?:PRG/|cosmoloc/layout/)[^;<>]+);', cf.cp.utf8(index)):
                dependencies.add(name + '.class')
    return dependencies


def read_layout_bundle(bundle):
    root = Path(bundle).resolve()
    raw = (root / 'layout-manifest.json').read_bytes()
    manifest = json.loads(raw)
    if manifest.get('schema_version') != 1 or manifest.get('status') != 'candidate_not_accepted':
        raise ValueError('Unsupported layout manifest/acceptance state')
    if manifest.get('game_version') != '1.0.5_full':
        raise ValueError('Layout bundle game version mismatch')
    if manifest.get('runtime_activation') != 'explicit_candidate_profiles_only':
        raise ValueError('Unknown or missing layout activation contract')
    components = manifest.get('components')
    if not isinstance(components, list) or len(components) != len(COMPONENTS) or set(components) != COMPONENTS:
        raise ValueError('Incomplete or unknown layout component declaration')
    files = manifest.get('classes', {})
    targets = manifest.get('original_classes', {})
    baseline = json.loads(BASELINE.read_text(encoding='utf-8'))
    if manifest.get('baseline_revision') != baseline.get('baseline_revision', 1):
        raise ValueError('Layout baseline revision mismatch')
    expected_targets = {name + '.class': digest for name, digest in baseline['target_classes'].items()}
    if targets != expected_targets or not set(targets).issubset(files) or not REQUIRED_HELPERS.issubset(files):
        raise ValueError('Incomplete or unpinned layout class set')
    for entry, spec in files.items():
        if not entry.endswith('.class') or not entry.startswith(('PRG/', 'cosmoloc/layout/')):
            raise ValueError('Unexpected layout archive entry')
        data = _safe_file(root, spec['path']).read_bytes()
        if sha(data) != spec['sha256']:
            raise ValueError('Layout class checksum mismatch: ' + entry)
        if entry in targets and sha(data) == targets[entry]:
            raise ValueError('Declared layout target is still unpatched: ' + entry)
        if data[:4] != b'\xca\xfe\xba\xbe' or int.from_bytes(data[6:8], 'big') > 52:
            raise ValueError('Runtime helper/target is not Java 8 compatible: ' + entry)
        if load(data).this_name + '.class' != entry:
            raise ValueError('Class internal identity does not match archive path: ' + entry)
    # Explicit list seals presence and hashes, including paired font/license files.
    for relative, expected in manifest.get('sealed_resources', {}).items():
        if sha(_safe_file(root, relative).read_bytes()) != expected:
            raise ValueError('Layout sealed resource mismatch: ' + relative)
    if not manifest.get('font_bindings'):
        raise ValueError('Missing layout/font binding')
    if set(manifest['font_bindings']) != {'default', 'classic'}:
        raise ValueError('Missing required default/classic font pair')
    for role, font in manifest['font_bindings'].items():
        if set(font) != {'fnt_entry', 'fnt_sha256', 'png_sha256', 'runtime_png'}:
            raise ValueError('Invalid font binding for ' + role)
        expected_pair = ('bbc2.fnt', 'bbc2-cjk-10.png') if role == 'default' else ('classic.fnt', 'classic-cjk.png')
        if (font['fnt_entry'], font['runtime_png']) != expected_pair:
            raise ValueError('Unexpected font role/resource pairing')
        if manifest.get('sealed_resources', {}).get('fonts/' + font['fnt_entry']) != font['fnt_sha256']:
            raise ValueError('Font definition is not sealed in bundle')
        if manifest.get('sealed_resources', {}).get('fonts/' + font['runtime_png']) != font['png_sha256']:
            raise ValueError('Font image is not sealed in bundle')
    return manifest, sha(raw)


def verify_font_atlas(source_zip, replacements, manifest, runtime):
    """Verify the actual selected encrypted atlas, not merely the external PNG."""
    def selected(entry):
        return replacements[entry] if entry in replacements else source_zip.read(entry)
    index = json.loads(decrypt_file(selected('dataq/0')))
    atlas_key = 'dataq/' + str(index['/sprites.atlas'])
    png_key = 'dataq/' + str(index['/sprites.png'])
    pages, regions = parse_atlas(decrypt_file(selected(atlas_key)).decode('utf-8'))
    if len(pages) != 1:
        raise ValueError('Unsupported font atlas page count')
    with Image.open(io.BytesIO(decrypt_file(selected(png_key)))) as image:
        actual = image.convert('RGBA')
    page = pages[0]
    size = ', '.join(map(str, actual.size))
    if page['name'] != 'sprites.png' or page['properties'].get('size') != size:
        raise ValueError('Font atlas page identity/dimensions mismatch')
    if any(region['page'] != page['name'] for region in regions):
        raise ValueError('Font region points to a different page')
    for role, font in manifest['font_bindings'].items():
        region_name = 'bbc2' if role == 'default' else 'classic'
        matches = [region for region in regions if region['name'] == region_name]
        if len(matches) != 1:
            raise ValueError('Font atlas region is not unique: ' + region_name)
        region = matches[0]
        x, y = region['xy']; width, height = region['size']
        if region['rotation'] or region['offset'] != [0, 0] or region['orig'] != region['size']:
            raise ValueError('Unexpected font region transform')
        if min(x, y) < 0 or x + width > actual.width or y + height > actual.height:
            raise ValueError('Font atlas region out of bounds')
        with Image.open(runtime / font['runtime_png']) as image:
            expected = image.convert('RGBA')
        if expected.size != (width, height) or actual.crop((x, y, x + width, y + height)).tobytes() != expected.tobytes():
            raise ValueError('Actual archive font pixels mismatch: ' + role)


def apply_layout_bundle(source_zip, replacements, bundle, code_changes=None, expected_manifest_sha256=None):
    """Merge into the existing replacement table; never read/rewrite an archive.

    A layout class must still equal its pinned original at this stage. CP edits
    referring to original pool indices cannot safely be applied after ASM pool
    reconstruction, so an overlap is rejected, not silently overwritten.
    """
    root = Path(bundle).resolve()
    manifest, identity = read_layout_bundle(root)
    if expected_manifest_sha256 is not None and identity != expected_manifest_sha256:
        raise ValueError('Layout bundle changed after packaging plan was prepared')
    overlap = set(code_changes or {}) & set(manifest['original_classes'])
    if overlap:
        raise ValueError('CP-index and layout patch overlap requires explicit composition: ' + ', '.join(sorted(overlap)))
    for entry, expected in manifest['original_classes'].items():
        try:
            original = source_zip.read(entry)
        except KeyError as error:
            raise ValueError('Layout target absent from source: ' + entry) from error
        if sha(original) != expected:
            raise ValueError('Original layout class mismatch: ' + entry)
        if entry in replacements and replacements[entry] != original:
            raise ValueError('Earlier replacement would be overwritten: ' + entry)
    for entry, spec in manifest['classes'].items():
        if entry not in manifest['original_classes'] and entry in source_zip.namelist():
            raise ValueError('Layout helper name collision: ' + entry)
        if entry not in manifest['original_classes'] and entry in replacements:
            raise ValueError('Layout helper replacement collision: ' + entry)
    # Check runtime pairs at consumption time, not only when the bundle was made.
    runtime = Path(__file__).resolve().parents[1] / 'runtime'
    for role, font in manifest['font_bindings'].items():
        fnt_entry = font['fnt_entry']
        fnt = replacements.get(fnt_entry)
        if fnt is None:
            raise ValueError('Required font definition not selected: ' + role)
        if sha(fnt) != font['fnt_sha256'] or sha((runtime / font['runtime_png']).read_bytes()) != font['png_sha256']:
            raise ValueError('Font pair no longer matches layout bundle: ' + role)
    verify_font_atlas(source_zip, replacements, manifest, runtime)
    # Do not mutate the caller's table until all identities and collisions pass.
    added = {entry: _safe_file(root, spec['path']).read_bytes()
             for entry, spec in manifest['classes'].items()}
    available = set(source_zip.namelist()) | set(added)
    for entry, data in added.items():
        if sha(data) != manifest['classes'][entry]['sha256'] or load(data).this_name + '.class' != entry:
            raise ValueError('Layout class changed during consumption: ' + entry)
        missing = class_dependencies(data) - available
        if missing:
            raise ValueError('Missing layout runtime dependency: ' + ', '.join(sorted(missing)))
    if sha((root / 'layout-manifest.json').read_bytes()) != identity:
        raise ValueError('Layout manifest changed during consumption')
    summary = {'manifest_sha256': identity, 'status': manifest['status'],
               'class_count': len(added), 'components': manifest['components'],
               'runtime_activation': manifest['runtime_activation'],
               'visual_acceptance': False}
    replacements.update(added)
    return summary
