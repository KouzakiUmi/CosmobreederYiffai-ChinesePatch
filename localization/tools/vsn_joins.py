"""Frozen r27 PAK VSN occurrence joins and four continuation translations.

Pure apply APIs: no writes, archive mutation, game, locale-table changes, or SFW
line-number fallback. The derived review ledger, not a heuristic, is authoritative.
"""
from collections import Counter
from pathlib import Path
import hashlib
import json
import re

DATA = Path(__file__).resolve().parents[1] / 'optimization/r28/vsn'
TEXT = re.compile(r'^(text: |lang\([A-Za-z]+\): |auto\([0-9.]+\): )')


class VsnJoinValidationError(ValueError):
    """Atomic rejection: no partially rewritten bytes or success report exists."""


def sha(data):
    return hashlib.sha256(data).hexdigest()


def _require(condition, message):
    if not condition:
        raise VsnJoinValidationError(message)


def _body_eol(line):
    for eol in (b'\r\n', b'\n', b'\r'):
        if line.endswith(eol):
            return line[:-len(eol)], eol
    return line, b''


def _split(data):
    _require(isinstance(data, bytes), 'Expected immutable UTF-8 bytes')
    try:
        data.decode('utf8')
    except UnicodeDecodeError as exc:
        raise VsnJoinValidationError('Invalid UTF-8') from exc
    # Only physical CR/LF are script line delimiters, never U+2028 or formfeed.
    return re.findall(rb'[^\r\n]*(?:\r\n|\r|\n|$)', data)[:-1]


def _markers(text):
    return {'placeholders': Counter(re.findall(r'@[A-Za-z][A-Za-z0-9_]*|\$\{[^{}]+\}|\{[^{}\r\n]+\}|%(?:\d+\$)?[-+#0 ]*\d*(?:\.\d+)?[sdifouxXeEgGc%]', text)),
            'tags': Counter(re.findall(r'<[^<>\r\n]*>', text)),
            'hearts': text.count('<3'), 'emphasis': text.count('*'),
            'slashes': text.count('/'), 'square_open': text.count('['),
            'square_close': text.count(']'), 'underscores': Counter(re.findall(r'_+', text)),
            'manual_pages': text.count('<p>'), 'pipes': text.count('|')}


def _load():
    manifest = json.loads((DATA / 'component.json').read_text('utf8'))
    raw = (DATA / 'operations.jsonl').read_bytes()
    _require(sha(raw) == manifest['operations_sha256'], 'Derived operation ledger SHA mismatch')
    records = [json.loads(row) for row in raw.decode('utf8').splitlines() if row]
    return manifest, records


def load_records():
    """Return exact reviewed operations (joins plus standalone translations)."""
    return _load()[1]


def rewrite_vsn(logical_path: str, source_bytes: bytes, records=None, *, archive='patch.pak'):
    """Return (new_plaintext_bytes, report) for ONE exact frozen r27 PAK script.

    source_bytes are decrypted r27 bytes, not English, re-localized bytes or SFW.
    Every requested operation is fully preflighted before an output copy exists.
    records=None selects this file's reviewed operations; [] is an explicit no-op.
    Supplied records must be exact members of the sealed occurrence allowlist.
    Unknown path, wrong archive, source/control/EOL drift, duplicate/overlapping
    records, injected commands, or even one mismatching item rejects the call.
    No source finding by equal text or physical line alone is performed.
    """
    manifest, allowed = _load()
    _require(archive == 'patch.pak', 'Archive identity mismatch: canonical PAK only; SFW needs its own ledger')
    resources = manifest['resources']
    _require(logical_path in resources, 'Unknown canonical VSN resource identity')
    pin = resources[logical_path]
    _require(isinstance(source_bytes, bytes) and sha(source_bytes) == pin['r27_plaintext_sha256'],
             'Frozen r27 resource SourceSHA mismatch')
    before = _split(source_bytes)
    _require(len(before) == pin['physical_line_count'], 'Physical line count mismatch')
    registry = {r['operation_id']: r for r in allowed}
    selected = [r for r in (allowed if records is None else list(records)) if r.get('logical_path') == logical_path]
    seen, occupied, plans = set(), set(), []
    for record in selected:
        rid = record.get('operation_id')
        _require(isinstance(rid, str) and rid in registry and registry[rid] == record,
                 'Operation is not an exact sealed occurrence allowlist member')
        _require(rid not in seen, 'Duplicate operation identity')
        seen.add(rid)
        _require(record['schema_version'] == 1 and record['archive'] == archive
                 and record['source_resource_sha256'] == pin['canonical_source_sha256']
                 and record['input_resource_sha256'] == sha(source_bytes), 'Operation resource identity drift')
        numbers = record['physical_lines']
        _require(numbers and all(type(n) is int and 1 <= n <= len(before) for n in numbers), 'Invalid physical lines')
        _require(numbers == list(range(numbers[0], numbers[-1] + 1)) and not occupied.intersection(numbers),
                 'Nonconsecutive/overlapping physical lines')
        occupied.update(numbers)
        _require(record['kind'] in ('join', 'translation') and (len(numbers) >= 2 if record['kind'] == 'join' else len(numbers) == 1),
                 'Invalid operation arity')
        inputs = record['inputs']
        _require(len(inputs) == len(numbers), 'Missing occurrence evidence')
        texts = []
        for n, item in zip(numbers, inputs):
            body, _ = _body_eol(before[n-1])
            _require(item['line'] == n and item['logical_path'] == logical_path
                     and item['prefix'] == 'text: ' and item['occurrence_id'] and item['unit_id'], 'Occurrence identity/prefix drift')
            _require(sha(body) == item['input_line_sha256'] and body.decode('utf8') == item['input_line'], 'Localized input/prefix drift')
            _require(sha(item['source_en'].encode('utf8')) == item['source_sha256'], 'English source SHA mismatch')
            _require(body.startswith(b'text: '), 'Role/auto/control line cannot be consumed')
            texts.append(body.decode('utf8')[6:])
        text = record['replacement']
        _require(isinstance(text, str) and text.strip() == text and re.search(r'[\u3400-\u9fff]', text), 'Invalid Chinese replacement')
        _require(not any(ord(c) < 32 or c in '\u2028\u2029' for c in text)
                 and '<p>' not in text and '|' not in text, 'Replacement contains script/page/control delimiter')
        _require(sha(text.encode('utf8')) == record['replacement_sha256'], 'Replacement SHA mismatch')
        # Translations are semantic substitutions; their original inline markers
        # still must match. Joins preserve markers from the exact localized input.
        _require(_markers(''.join(texts)) == _markers(text), 'Inline markup/token conservation mismatch')
        evidence = record['control_evidence']
        for row in evidence['control_lines']:
            _require(before[row['line'] - 1].decode('utf8') == row['raw'], 'Staging control/event drift')
        _require(evidence['intervening_controls'] == [] and evidence['automatic_delay_delta_seconds'] == 0,
                 'Control boundary/auto timing violation')
        plans.append((record, ('text: ' + text).encode('utf8')))
    # No mutation or report exposing a partial result before the final preflight.
    output = before[:]
    mapping, applied = [], []
    for record, body in plans:
        nums = record['physical_lines']
        output[nums[0]-1] = body + _body_eol(before[nums[0]-1])[1]
        for n in nums[1:]:
            # An unterminated final row cannot be represented by zero bytes:
            # retain one parser-ignored space, without inventing a final EOL.
            output[n-1] = _body_eol(before[n-1])[1] or b' '  # Never an empty text command.
        applied.append(record['operation_id'])
        for item in record['inputs']:
            mapping.append({'occurrence_id': item['occurrence_id'], 'unit_id': item['unit_id'],
                            'source_line': item['line'], 'output_line': nums[0],
                            'disposition': 'replacement' if item['line'] == nums[0] else 'blank_physical_line'})
    result = b''.join(output)
    _require(len(_split(result)) == len(before), 'Output physical line count drift')
    untouched = [i for i in range(len(before)) if i + 1 not in occupied]
    _require(all(before[i] == output[i] for i in untouched), 'Unrelated bytes changed')
    report = {'archive': archive, 'logical_path': logical_path,
              'input_sha256': sha(source_bytes), 'output_sha256': sha(result),
              'canonical_source_sha256': pin['canonical_source_sha256'],
              'applied_operations': len(plans), 'applied_groups': sum(r['kind'] == 'join' for r, _ in plans),
              'translated_standalone_lines': sum(r['kind'] == 'translation' for r, _ in plans),
              'removed_text_nodes': sum(len(r['inputs']) - 1 for r, _ in plans),
              'physical_line_count': len(output), 'automatic_delay_delta_seconds': 0,
              'operations': applied, 'occurrence_mapping': mapping,
              'unmodified_control_sha256': pin['control_sha256']}
    return result, report


def apply_joins(logical_path: str, original_bytes: bytes, localized_bytes: bytes, records=None, *, archive='patch.pak'):
    """DS-shaped convenience API, additionally verifies canonical English bytes."""
    manifest, _ = _load()
    _require(logical_path in manifest['resources'], 'Unknown canonical VSN resource identity')
    _require(isinstance(original_bytes, bytes) and sha(original_bytes) == manifest['resources'][logical_path]['canonical_source_sha256'],
             'Canonical English resource SourceSHA mismatch')
    return rewrite_vsn(logical_path, localized_bytes, records, archive=archive)
