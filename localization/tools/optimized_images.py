"""Pure, fail-closed r28 image overlays. No archive, filesystem-write, CLI or deployment effects.

Consumer supplies decoded RGBA atlas and its parsed regions. The original page is
never mutated; all source pins and identities are checked before any overlay.
Paths in manifest are workspace-relative. Only jar/patch runtime rows are inputs.
"""
from __future__ import annotations
from hashlib import sha256
from pathlib import Path
import json
from PIL import Image

ROOT = Path(__file__).resolve().parents[2]
DEFAULT_MANIFEST = ROOT / 'localization/optimization/r28/images/manifest.json'


def raw_rgba_hash(image: Image.Image) -> str:
    return sha256(image.convert('RGBA').tobytes()).hexdigest()


def load_overrides(variant: str, manifest_path=None) -> list[dict]:
    """Read and verify immutable candidate PNGs/masks; do not write anything.

    Returns manifest records plus ``image`` (RGBA Image) and ``mask`` (L Image).
    Callers must also verify expected_rawRGBA_sha256 against their decoded source.
    """
    if variant not in ('jar', 'patch'):
        raise ValueError('variant must be jar or patch')
    path = Path(manifest_path) if manifest_path else DEFAULT_MANIFEST
    manifest = json.loads(path.read_text(encoding='utf-8'))
    if manifest.get('schema') != 1 or manifest.get('scope') != 'independent-staging-only':
        raise ValueError('unsupported image manifest')
    records = []
    identities = set()
    for original in manifest['replacements']:
        if original['variant'] != variant:
            continue
        row = dict(original)
        identity = (row['logical_name'], row['index'], row['ordinal'])
        if identity in identities:
            raise ValueError(f'duplicate replacement: {identity}')
        identities.add(identity)
        for key, hashkey, mode, outputkey in (
            ('newPNG', 'newPNG_sha256', 'RGBA', 'image'),
            ('approved_mask', 'approved_mask_png_sha256', 'L', 'mask'),
        ):
            candidate = (ROOT / row[key]).resolve()
            # A manifest cannot be used to read unrelated files outside its staging.
            staging = DEFAULT_MANIFEST.parent.resolve()
            if not candidate.is_relative_to(staging):
                raise ValueError(f'candidate outside image staging: {key}')
            data = candidate.read_bytes()
            if sha256(data).hexdigest() != row[hashkey]:
                raise ValueError(f'candidate file hash mismatch: {row[key]}')
            with Image.open(candidate) as im:
                if im.format != 'PNG' or list(im.size) != row['size']:
                    raise ValueError('candidate format/dimensions mismatch')
                row[outputkey] = im.convert(mode)
        if raw_rgba_hash(row['image']) != row['new_rawRGBA_sha256']:
            raise ValueError('candidate RGBA hash mismatch')
        if not set(row['mask'].tobytes()) <= {0, 255}:
            raise ValueError('nonbinary approved mask')
        records.append(row)
    return records


def verify_replacement(before: Image.Image, after: Image.Image, mask: Image.Image) -> dict:
    """Exact full-RGBA comparison, including RGB under transparent pixels."""
    before, after = before.convert('RGBA'), after.convert('RGBA')
    if before.size != after.size or before.size != mask.size:
        raise ValueError('replacement size mismatch')
    changed = outside = alpha = 0
    for old, new, allowed in zip(before.getdata(), after.getdata(), mask.convert('L').getdata()):
        if old != new:
            changed += 1
            outside += not bool(allowed)
        alpha += old[3] != new[3]
    if outside or alpha:
        raise ValueError(f'unsafe replacement: outside={outside}; alpha={alpha}')
    return {'changed_pixels': changed, 'changed_pixels_outside_approved_mask': outside,
            'alpha_changed_pixels': alpha}


def apply_overrides(page: Image.Image, regions: list[dict], variant: str, manifest_path=None):
    """Return (new_RGBA_page, report); accept name/index/ordinal/xy/size/rotation.

    The caller parses its own atlas; no catalog ordinal is substituted for the
    actual target ordinal. Rotation unsupported rather than silently misplacing.
    All preconditions are checked on the unmodified input before composing.
    """
    if page.mode != 'RGBA':
        raise ValueError('supply the decoded RGBA atlas, not a composited RGB image')
    lookup = {}
    for r in regions:
        identity = (r['name'], r['index'], r['ordinal'])
        if identity in lookup:
            raise ValueError(f'duplicate atlas identity: {identity}')
        lookup[identity] = r
    checked = []
    occupied = []
    for row in load_overrides(variant, manifest_path):
        identity = (row['logical_name'], row['index'], row['ordinal'])
        if identity not in lookup:
            raise ValueError(f'missing exact atlas identity: {identity}')
        region = lookup[identity]
        if region.get('rotation', 0) or list(region['size']) != row['size']:
            raise ValueError(f'unsupported region geometry: {identity}')
        if list(region['xy']) != row['source_xy']:
            raise ValueError(f'changed atlas placement: {identity}')
        x, y = region['xy']; w, h = region['size']
        box = (x, y, x+w, y+h)
        if x < 0 or y < 0 or x+w > page.width or y+h > page.height:
            raise ValueError(f'out-of-page region: {identity}')
        before = page.crop(box)
        if raw_rgba_hash(before) != row['expected_rawRGBA_sha256']:
            raise ValueError(f'stale source rawRGBA pin: {identity}')
        proof = verify_replacement(before, row['image'], row['mask'])
        # Packed aliases legitimately share rectangles. They must agree bytewise.
        for previous_box, previous_hash in occupied:
            overlap = min(box[2], previous_box[2]) > max(box[0], previous_box[0]) and min(box[3], previous_box[3]) > max(box[1], previous_box[1])
            if overlap and (box != previous_box or row['new_rawRGBA_sha256'] != previous_hash):
                raise ValueError('overlapping incompatible atlas replacements')
        occupied.append((box, row['new_rawRGBA_sha256']))
        checked.append((row, box, proof))
    output = page.copy()
    for row, box, _ in checked:
        # No mask argument: preserve the candidate's exact RGBA, including alpha.
        output.paste(row['image'], box[:2])
    return output, {'variant': variant, 'replacement_count': len(checked),
                    'source_page_rawRGBA_sha256': raw_rgba_hash(page),
                    'output_page_rawRGBA_sha256': raw_rgba_hash(output),
                    'records': [{'logical_name': r['logical_name'], 'index': r['index'],
                                 'ordinal': r['ordinal'], **proof} for r, _, proof in checked]}
