"""SFW-only derived translation ledger and read-only candidate API.

No archive writer, CLI deployment, catalog mutation or implicit PAK fallback.
Input resources MUST be decrypted original JAR bytes, before dialogue_sfw joins.
"""
from __future__ import annotations

from collections import Counter, defaultdict
from dataclasses import dataclass
from hashlib import sha256
import json
from pathlib import Path
import re
import zipfile

from codec import decrypt_file

SCHEMA = 'sfw-derived-ledger/v1'
ARCHIVE = 'cosmobreeder-multi.jar'
DS_TEXT = re.compile(r'^(\s*\*\s?|\s*[^<>{}#*\s][^:]{0,40}:\s?)(.*)$')
VSN_TEXT = re.compile(r'^(\s*(?:text|lang\([^)]*\)|auto\([^)]*\))\s*:\s?)(.*)$')
PLACEHOLDER = re.compile(r'@[A-Za-z][A-Za-z0-9_]*|\$\{[^{}]+\}|\{[^{}\r\n]+\}|%(?:\d+\$)?[-+#0 ]*\d*(?:\.\d+)?[sdifouxXeEgGc%]')
TAGS = re.compile(r'</?[a-z][^<>\r\n]*>')
NUMBER = re.compile(r'\d+(?:\.\d+)?')
KEY = re.compile(r'(?<![A-Za-z0-9_])(?:SELECT|START|ESC|F[1-9][0-2]?)(?![A-Za-z0-9_])')
IDENTIFIER = re.compile(r'(?<![A-Za-z0-9_])(?:[A-Za-z0-9]*[A-Za-z]\d+[A-Za-z0-9-]*|\d+[A-Za-z][A-Za-z0-9-]*)(?![A-Za-z0-9_])')


class SfwValidationError(ValueError):
    """No candidate may be emitted when source identity or target QA drifts."""


def digest(data: bytes) -> str:
    return sha256(data).hexdigest()


def text_digest(text: str) -> str:
    return digest(text.encode('utf-8'))


def marker_signature(text: str) -> dict:
    """Exact multisets, not set membership; protects repeated placeholders too."""
    return {
        'placeholders': sorted(PLACEHOLDER.findall(text)),
        'tags': sorted(TAGS.findall(text)),
        'numbers': sorted(NUMBER.findall(text)),
        'identifiers': sorted(x for x in IDENTIFIER.findall(text) if not re.fullmatch(r'(?:KEYCARD|BIGBOLD)\d+', x)),
        'key_combinations': sorted(re.findall(r'[A-Z]+(?:\+[A-Z]+)+', text)),
        'pipes': text.count('|'), 'newlines': text.count('\n'),
        'carriage_returns': text.count('\r'),
        'open_square': text.count('['), 'close_square': text.count(']'),
        'open_angle': text.count('<'), 'close_angle': text.count('>'),
        'underscore_runs': sorted(re.findall(r'_+', text)),
        'dollar_markers': text.count('$'),
    }


def validate_target(source: str, target: str, glyphs=None) -> None:
    if not isinstance(target, str) or not target.strip():
        raise SfwValidationError('empty translation is not coverage')
    if marker_signature(source) != marker_signature(target):
        raise SfwValidationError('marker/placeholder/key/number multiset drift')
    # Distinguish a literal controller key from English verbs (START MONITORING,
    # SELECT A LINE). A target must retain every literal source key occurrence.
    required_keys = KEY.findall(source) if (re.search(r'(?i)press\s*\(?\s*(?:SELECT|START|ESC|F\d+)', source) or re.fullmatch(r'(?:SELECT|START|ESC)(?:/[A-Z]+)?', source)) else []
    for token, count in Counter(required_keys).items():
        if len(re.findall(r'(?<![A-Za-z0-9_])' + re.escape(token) + r'(?![A-Za-z0-9_])', target)) != count:
            raise SfwValidationError('literal key multiset drift: ' + token)
    if any(ord(c) < 32 and c not in '\n\r\t' or c in '\x85\u2028\u2029' for c in target):
        raise SfwValidationError('unexpected control character/line separator')
    if glyphs is not None:
        missing = sorted({c for c in target if not c.isspace() and c != '|' and ord(c) not in glyphs})
        if missing:
            raise SfwValidationError('full target glyph coverage missing: ' + ''.join(missing))


def _line_parts(line: str):
    for eol in ('\r\n', '\n', '\r'):
        if line.endswith(eol):
            return line[:-len(eol)], eol
    return line, ''


def parse_resource(logical_path: str, data: bytes) -> list[dict]:
    """Parse original SFW payloads. Byte ranges are derived, never PAK line IDs."""
    text = data.decode('utf-8')
    rows = []
    if logical_path == 'datav/dictionary.json':
        # A top-level object of string values; reject duplicate keys and nonstrings.
        dec = json.JSONDecoder()
        pos = 0
        def ws(i):
            while i < len(text) and text[i].isspace(): i += 1
            return i
        pos = ws(pos)
        if text[pos:pos+1] != '{': raise SfwValidationError('dictionary is not an object')
        pos += 1
        seen = set()
        while True:
            pos = ws(pos)
            if text[pos:pos+1] == '}':
                pos = ws(pos+1)
                if pos != len(text): raise SfwValidationError('dictionary trailing data')
                break
            key, pos = dec.raw_decode(text, pos)
            if not isinstance(key, str) or key in seen: raise SfwValidationError('duplicate/invalid dictionary key')
            seen.add(key)
            pos = ws(pos)
            if text[pos:pos+1] != ':': raise SfwValidationError('dictionary missing colon')
            pos = ws(pos+1)
            start = pos
            value, pos = dec.raw_decode(text, pos)
            if not isinstance(value, str): raise SfwValidationError('dictionary non-string value')
            rows.append({'root': key, 'prefix': '', 'raw_source': value,
                         'start': len(text[:start].encode('utf-8')), 'end': len(text[:pos].encode('utf-8')),
                         'line': None, 'kind': 'ui', 'role': ''})
            pos = ws(pos)
            if text[pos:pos+1] == ',': pos += 1
            elif text[pos:pos+1] != '}': raise SfwValidationError('dictionary separator')
    else:
        root = Path(logical_path).parent.name if logical_path.endswith('.vsn') else ''
        offset = 0
        for number, line in enumerate(text.splitlines(keepends=True), 1):
            body, _ = _line_parts(line)
            header = re.fullmatch(r'\s*<([^>]+)>\s*', body)
            match = None
            if logical_path.endswith('.ds'):
                if header: root = header.group(1)
                elif body.strip() and not re.match(r'^\s*(?:include\b|if\b|else\b|\}|do\b|#)', body):
                    match = DS_TEXT.match(body)
            elif logical_path.endswith('.vsn'):
                match = VSN_TEXT.match(body)
            else: raise SfwValidationError('unsupported SFW resource')
            if match and match.group(2).strip():
                prefix, raw = match.groups()
                start = offset + len(prefix.encode('utf-8'))
                role = re.search(r'lang\(([^)]+)\)', prefix)
                rows.append({'root': root, 'prefix': prefix, 'raw_source': raw,
                             'start': start, 'end': start + len(raw.encode('utf-8')), 'line': number,
                             'kind': 'ds' if logical_path.endswith('.ds') else 'vsn',
                             'role': role.group(1) if role else ''})
            offset += len(line.encode('utf-8'))
    groups = defaultdict(list)
    for row in rows:
        row['raw_source_sha256'] = text_digest(row['raw_source'])
        groups[(row['root'], row['prefix'], row['raw_source_sha256'])].append(row)
    for group in groups.values():
        for i, row in enumerate(group):
            row['source_ordinal'] = i
            row['source_multiplicity'] = len(group)
    return rows


def inventory_archive(path) -> tuple[dict, dict[str, bytes]]:
    """Read JAR indexes and encrypted entries only; never create/extract an archive."""
    path = Path(path)
    if path.name != ARCHIVE: raise SfwValidationError('SFW API rejects PAK/renamed archive')
    archive_sha = digest(path.read_bytes())
    resources = []
    payloads = {}
    with zipfile.ZipFile(path, 'r') as archive:
        for group in ('datadf', 'datadm', 'datav', 'vsn'):
            index_entry = group + '/0'
            index_blob = archive.read(index_entry)
            index = json.loads(decrypt_file(index_blob))
            routes = defaultdict(list)
            for key, slot in index.items(): routes[group + '/' + str(slot)].append(key)
            for key, slot in sorted(index.items()):
                logical_path = group + '/' + key.lstrip('/')
                if not (logical_path in ('datadf/all.ds', 'datadm/all.ds', 'datav/dictionary.json') or
                        logical_path.startswith('vsn/') and logical_path.endswith('/script.vsn')):
                    continue
                entry = group + '/' + str(slot)
                if len(routes[entry]) != 1: raise SfwValidationError('ambiguous archive route')
                blob = archive.read(entry)
                data = decrypt_file(blob)
                payloads[logical_path] = data
                resources.append({'logical_path': logical_path, 'archive_entry': entry,
                                  'index_entry': index_entry, 'index_key': key,
                                  'index_raw_sha256': digest(index_blob),
                                  'stored_entry_sha256': digest(blob), 'resource_sha256': digest(data)})
    return {'schema': SCHEMA, 'archive': ARCHIVE, 'archive_sha256': archive_sha,
            'variant': 'sfw', 'resources': resources}, payloads


def make_record(manifest: dict, resource: dict, parsed: dict) -> dict:
    row = {k: parsed[k] for k in ('root', 'prefix', 'raw_source', 'raw_source_sha256',
                                  'source_ordinal', 'source_multiplicity', 'kind', 'role')}
    row.update({k: resource[k] for k in ('logical_path', 'archive_entry', 'resource_sha256')})
    row.update({'schema': SCHEMA, 'archive': ARCHIVE, 'archive_sha256': manifest['archive_sha256'],
                'variant': 'sfw', 'source_line_evidence': parsed['line']})
    key = [row[k] for k in ('archive', 'archive_sha256', 'logical_path', 'archive_entry', 'root',
                            'prefix', 'raw_source_sha256', 'source_ordinal')]
    row['id'] = 'SFW' + text_digest(json.dumps(key, ensure_ascii=False, separators=(',', ':')))[:24]
    row.update({'translation': None, 'status': 'needs_translation', 'provenance': None, 'review_notes': []})
    if row['role'] in ('Fox', 'HardFox'):
        row['symbol_source'] = row['raw_source']
        row['pattern_policy'] = 'preserve-role; dual-representation-required'
    return row


@dataclass(frozen=True)
class CandidateReplacement:
    ledger_id: str
    start: int
    end: int
    original: bytes
    replacement: bytes
    role: str
    symbol_source: str | None


def candidate_replacements(*, archive: str, archive_sha256: str, logical_path: str,
                           archive_entry: str, original_bytes: bytes, records: list[dict],
                           glyphs=None, allow_pattern_candidates=False) -> list[CandidateReplacement]:
    """Validate all records before emitting replacements; does not write any file.

    All records for this resource (including unresolved records) are mandatory.
    Unknown source, partial ledger, duplicates, ambiguous route/identity, mutation,
    changed prefix, or unsafe candidate raises. Candidate status is NOT approval.
    Pattern candidates require explicit opt-in; runtime dual-representation support
    and visible symbol-glyph verification remain the downstream builder's duty.
    """
    if archive != ARCHIVE: raise SfwValidationError('archive variant must be SFW JAR')
    parsed = parse_resource(logical_path, original_bytes)
    actual_sha = digest(original_bytes)
    expected = {(p['root'], p['prefix'], p['raw_source_sha256'], p['source_ordinal']): p for p in parsed}
    if len(expected) != len(parsed): raise SfwValidationError('ambiguous original identity')
    seen = set()
    ids = set()
    candidates = []
    for row in records:
        if row.get('schema') != SCHEMA or row.get('variant') != 'sfw': raise SfwValidationError('wrong ledger schema/variant')
        for name, value in (('archive', archive), ('archive_sha256', archive_sha256), ('logical_path', logical_path),
                            ('archive_entry', archive_entry), ('resource_sha256', actual_sha)):
            if row.get(name) != value: raise SfwValidationError('source identity drift: ' + name)
        key = (row['root'], row['prefix'], row['raw_source_sha256'], row['source_ordinal'])
        if key in seen or row['id'] in ids: raise SfwValidationError('duplicate replacement identity')
        seen.add(key); ids.add(row['id'])
        source = expected.get(key)
        if source is None or source['raw_source'] != row['raw_source'] or text_digest(row['raw_source']) != row['raw_source_sha256']:
            raise SfwValidationError('raw source drift')
        if row['source_multiplicity'] != source['source_multiplicity'] or row['role'] != source['role'] or row['kind'] != source['kind']:
            raise SfwValidationError('source multiplicity/role/kind drift')
        recomputed = make_record({'archive_sha256': archive_sha256}, row, source)['id']
        if row['id'] != recomputed: raise SfwValidationError('ledger ID drift')
        target = row.get('translation')
        if row['status'] not in ('candidate', 'reused_candidate', 'preserved', 'needs_translation', 'needs_review'):
            raise SfwValidationError('unknown candidate status')
        if row['status'] in ('needs_translation', 'needs_review'):
            continue
        if row['status'] == 'preserved':
            if target != row['raw_source']: raise SfwValidationError('preserved source changed')
            continue
        validate_target(row['raw_source'], target, glyphs)
        if row['role'] in ('Fox', 'HardFox'):
            if row.get('symbol_source') != row['raw_source'] or row.get('pattern_policy') != 'preserve-role; dual-representation-required':
                raise SfwValidationError('pattern source identity lost')
            if not allow_pattern_candidates:
                continue
        # Preserve edge whitespace as part of exact original body contract.
        before_left = row['raw_source'][:len(row['raw_source'])-len(row['raw_source'].lstrip())]
        before_right = row['raw_source'][len(row['raw_source'].rstrip()):]
        after_left = target[:len(target)-len(target.lstrip())]
        after_right = target[len(target.rstrip()):]
        if (before_left, before_right) != (after_left, after_right):
            # One source-ID-pinned cosmetic credit-padding correction. This is
            # NOT a generic whitespace exception or a 32-column limit increase.
            padding = {'source_left': 4, 'source_right': 4, 'target_left': 3, 'target_right': 3}
            if not (row['id'] == 'SFW4ef0d94ee90867f2faa6b2ca'
                    and row.get('cosmetic_padding') == padding
                    and row['raw_source'] == '    FMOD STUDIO BY FIRELIGHT    '
                    and target == '   FMOD STUDIO，由 FIRELIGHT 开发   '):
                raise SfwValidationError('edge whitespace drift')
        replacement = json.dumps(target, ensure_ascii=False).encode('utf-8') if source['kind'] == 'ui' else target.encode('utf-8')
        original = original_bytes[source['start']:source['end']]
        candidates.append(CandidateReplacement(row['id'], source['start'], source['end'], original,
                                                replacement, row['role'], row.get('symbol_source')))
    if seen != set(expected): raise SfwValidationError('incomplete resource ledger')
    candidates.sort(key=lambda c: c.start)
    for left, right in zip(candidates, candidates[1:]):
        if left.end > right.start: raise SfwValidationError('overlapping replacements')
    return candidates


def render_candidate(original_bytes: bytes, replacements: list[CandidateReplacement]) -> bytes:
    """Render already validated spans in memory, preserving every other byte."""
    output = bytearray()
    cursor = 0
    for r in sorted(replacements, key=lambda x: x.start):
        if not (cursor <= r.start <= r.end <= len(original_bytes)) or original_bytes[r.start:r.end] != r.original:
            raise SfwValidationError('candidate span/source drift')
        output.extend(original_bytes[cursor:r.start]); output.extend(r.replacement)
        cursor = r.end
    output.extend(original_bytes[cursor:])
    return bytes(output)


def validate_ending_fields(dictionary, metrics=None):
    """Enforce original 60-field / 32-cell classic8 ending contract.

    With actual FNT metrics supplied, also check every actual glyph and advance.
    The default 8px grid is not a runtime/font-ink acceptance claim.
    """
    fields = {key: value for key, value in dictionary.items() if key.startswith('ui.end.')}
    if len(fields) != 60: raise SfwValidationError('ending field count must remain 60')
    report = {'field_count': 60, 'nonempty_fields': 0, 'maximum_columns': 0, 'maximum_width_px': 0, 'fields': []}
    for key, value in sorted(fields.items()):
        columns = len(value.encode('utf-16-le')) // 2
        if metrics is not None and any(ord(c) not in metrics for c in value):
            raise SfwValidationError('ending field missing actual classic glyph: ' + key)
        width = sum(metrics[ord(c)] if metrics is not None else 8 for c in value)
        if value.strip():
            if columns > 32 or width > 256: raise SfwValidationError('ending field exceeds unchanged 32 columns/256px: ' + key)
            report['nonempty_fields'] += 1
        report['maximum_columns'] = max(report['maximum_columns'], columns)
        report['maximum_width_px'] = max(report['maximum_width_px'], width)
        report['fields'].append({'key': key, 'text': value, 'columns': columns, 'width_px': width})
    return report


def load_ledger(data_dir) -> tuple[dict, list[dict]]:
    """Read a frozen derived ledger; no fallback to a canonical/PAK catalog."""
    base = Path(data_dir)
    manifest = json.loads((base / 'source-manifest.json').read_text(encoding='utf-8'))
    if manifest.get('schema') != SCHEMA or manifest.get('variant') != 'sfw' or manifest.get('archive') != ARCHIVE:
        raise SfwValidationError('manifest schema/variant drift')
    rows = []
    for kind in ('ds', 'vsn', 'ui'):
        name = 'ledger-' + kind + '.jsonl'
        raw = (base / name).read_bytes()
        if digest(raw) != manifest['ledger_sha256'].get(name): raise SfwValidationError('ledger file digest drift')
        batch = [json.loads(line) for line in raw.decode('utf-8').splitlines() if line.strip()]
        if any(row['kind'] != kind for row in batch): raise SfwValidationError('ledger kind drift')
        rows.extend(batch)
    if len(rows) != manifest['record_count'] or len({row['id'] for row in rows}) != len(rows):
        raise SfwValidationError('ledger count/uniqueness drift')
    return manifest, rows


def rebuild_candidate_entries(source_jar, data_dir, *, canonical_join_records=None,
                              glyphs=None, allow_pattern_candidates=False,
                              enable_ds_polish=True) -> tuple[dict[str, bytes], dict]:
    """Return (archive_entry -> DECRYPTED candidate bytes, machine report).

    The source is the pinned *original* JAR, NOT the already translated r27 JAR.
    The caller may overlay returned entries onto its frozen r27 target after
    applying its own encryption/packaging. No output files are created here.

    If canonical joins are supplied, execute their existing read-only validator
    on original SFW bytes, then use this JAR's own parsed source identities to
    overlay candidates ONLY on unconsumed source lines. Already joined nodes
    keep their canonical merged text; suppressed derived candidates are reported.
    This avoids both PAK offsets and canonical rewriter clobbering repaired keys.
    """
    manifest, records = load_ledger(data_dir)
    join_raw = (Path(data_dir) / 'vsn-joins.jsonl').read_bytes()
    if digest(join_raw) != manifest['ledger_sha256'].get('vsn-joins.jsonl'):
        raise SfwValidationError('SFW VSN join ledger digest drift')
    vsn_joins = [json.loads(line) for line in join_raw.decode('utf-8').splitlines() if line.strip()]
    polish_records = []
    if enable_ds_polish:
        polish_raw = (Path(data_dir) / 'ds-polish.jsonl').read_bytes()
        if digest(polish_raw) != manifest['ledger_sha256'].get('ds-polish.jsonl'):
            raise SfwValidationError('SFW DS polish ledger digest drift')
        polish_records = [json.loads(line) for line in polish_raw.decode('utf-8').splitlines() if line.strip()]
    actual, payloads = inventory_archive(source_jar)
    if actual['archive_sha256'] != manifest['archive_sha256'] or actual['resources'] != manifest['resources']:
        raise SfwValidationError('archive/index/entry source drift')
    grouped = defaultdict(list)
    for row in records: grouped[row['logical_path']].append(row)
    if set(grouped) != set(payloads): raise SfwValidationError('resource set drift')
    if any(j.get('logical_path') not in payloads for j in vsn_joins): raise SfwValidationError('foreign SFW VSN join resource')
    entries = {}
    report = {'schema': 'sfw-candidate-rebuild/v1', 'source_archive_sha256': actual['archive_sha256'],
              'entries_are': 'decrypted plaintext bytes', 'writes': 0, 'resources': [],
              'glyph_gate': 'all target characters checked' if glyphs is not None else 'not supplied; downstream must validate complete final font repertoire',
              'pattern_candidates_enabled': allow_pattern_candidates}
    for resource in actual['resources']:
        logical = resource['logical_path']
        original = payloads[logical]
        rows = grouped[logical]
        replacements = candidate_replacements(archive=ARCHIVE, archive_sha256=actual['archive_sha256'],
                         logical_path=logical, archive_entry=resource['archive_entry'], original_bytes=original,
                         records=rows, glyphs=glyphs, allow_pattern_candidates=allow_pattern_candidates)
        result = render_candidate(original, replacements)
        item = {'logical_path': logical, 'archive_entry': resource['archive_entry'],
                'source_sha256': digest(original), 'emitted_candidates': len(replacements),
                'unresolved_ids': [r['id'] for r in rows if r['status'] in ('needs_review', 'needs_translation')],
                'pattern_withheld': [r['id'] for r in rows if r['role'] in ('Fox', 'HardFox') and not allow_pattern_candidates]}
        if logical.endswith('.ds') and canonical_join_records is not None:
            import dialogue_sfw
            joined, join_report = dialogue_sfw.rewrite_sfw(logical, original, original, canonical_join_records)
            consumed = {n for group in join_report['groups'] for n in group['actual_sfw_lines']}
            source_rows = parse_resource(logical, original)
            source_by_span = {(s['start'], s['end']): s for s in source_rows}
            joined_lines = joined.decode('utf-8').splitlines(keepends=True)
            original_lines = original.decode('utf-8').splitlines(keepends=True)
            if len(joined_lines) != len(original_lines): raise SfwValidationError('joined physical lines drift')
            suppressed = []
            for replacement in replacements:
                source = source_by_span[(replacement.start, replacement.end)]
                number = source['line']
                if number in consumed:
                    suppressed.append(replacement.ledger_id)
                    continue
                # Lines and prefix come exclusively from this validated original
                # JAR. Never use a canonical occurrence's physical line number.
                _, eol = _line_parts(original_lines[number-1])
                joined_lines[number-1] = source['prefix'] + replacement.replacement.decode('utf-8') + eol
            result = ''.join(joined_lines).encode('utf-8')
            item['canonical_join_report'] = join_report
            identity_rows = {(r['root'], r['prefix'], r['raw_source_sha256'], r['source_ordinal']): r for r in rows}
            row_at_line = {s['line']: identity_rows[(s['root'], s['prefix'], s['raw_source_sha256'], s['source_ordinal'])] for s in source_rows}
            item['canonical_join_source_mapping'] = [
                {'join_id': group['join_id'], 'retained_first_source_line': group['actual_sfw_lines'][0],
                 'blanked_source_lines': group['actual_sfw_lines'][1:],
                 'inputs': [{'sfw_source_line': n, 'ledger_id': row_at_line[n]['id'],
                             'raw_source_sha256': row_at_line[n]['raw_source_sha256'],
                             'root': row_at_line[n]['root'], 'prefix': row_at_line[n]['prefix']}
                            for n in group['actual_sfw_lines']]}
                for group in join_report['groups']]
            item['joined_source_candidate_ids_suppressed'] = suppressed
            item['unjoined_candidates_applied'] = len(replacements) - len(suppressed)
        if logical.endswith('.ds') and enable_ds_polish:
            result, polish_report = apply_ds_polish(logical, original, result, rows, polish_records,
                    canonical_join_report=item.get('canonical_join_report'), glyphs=glyphs)
            item['sfw_ds_polish_report'] = polish_report
        if logical.endswith('.vsn'):
            result, vsn_report = apply_vsn_joins(logical, original, result, rows, vsn_joins, glyphs=glyphs)
            item['sfw_vsn_join_report'] = vsn_report
        if glyphs is not None:
            for final in parse_resource(logical, result):
                missing = sorted({c for c in final['raw_source'] if not c.isspace() and c != '|' and ord(c) not in glyphs})
                if missing: raise SfwValidationError('full final-output glyph coverage missing: ' + ''.join(missing))
        if logical == 'datav/dictionary.json':
            item['ending_grid_report'] = validate_ending_fields(json.loads(result))
        item['output_sha256'] = digest(result)
        item['output_bytes'] = len(result)
        entries[resource['archive_entry']] = result
        report['resources'].append(item)
    report['entry_count'] = len(entries)
    report['sfw_vsn_applied_groups'] = sum(r.get('sfw_vsn_join_report', {}).get('applied_groups', 0) for r in report['resources'])
    report['sfw_vsn_retained_groups'] = 0
    report['sfw_ds_polish_applied_operations'] = sum(r.get('sfw_ds_polish_report', {}).get('applied_operations', 0) for r in report['resources'])
    report['sfw_vsn_click_reduction'] = sum(r.get('sfw_vsn_join_report', {}).get('click_reduction', 0) for r in report['resources'])
    return entries, report


def apply_ds_polish(logical_path, original_bytes, localized_bytes, records, polish_records,
                    *, canonical_join_report=None, glyphs=None):
    """Repair explicitly reviewed DS Chinese pollution after own-source joins.

    A Chinese old-text match alone is never sufficient: own complete ordered
    English/source IDs and the actually applied canonical join are mandatory.
    """
    selected = [p for p in polish_records if p.get('logical_path') == logical_path]
    report = {'applied_operations': 0, 'withheld_without_canonical_joins': [], 'operations': []}
    parsed = parse_resource(logical_path, original_bytes)
    old_lines = original_bytes.decode('utf-8').splitlines(keepends=True)
    lines = localized_bytes.decode('utf-8').splitlines(keepends=True)
    if len(old_lines) != len(lines): raise SfwValidationError('DS polish physical line count drift')
    if [_line_parts(s)[1] for s in old_lines] != [_line_parts(s)[1] for s in lines]: raise SfwValidationError('DS polish EOL drift')
    source_text_lines = {p['line'] for p in parsed}
    for number, (old, new) in enumerate(zip(old_lines, lines), 1):
        if number not in source_text_lines and old != new:
            raise SfwValidationError('DS polish non-dialogue control drift')
    by_id = {r['id']: r for r in records}
    seen = set(); occupied = set(); plans = []
    for operation in selected:
        if operation.get('schema') != 'sfw-ds-polish/v1' or operation.get('variant') != 'sfw' or operation.get('archive') != ARCHIVE:
            raise SfwValidationError('DS polish schema/variant drift')
        if operation['operation_id'] in seen: raise SfwValidationError('duplicate DS polish operation')
        seen.add(operation['operation_id'])
        if operation.get('resource_sha256') != digest(original_bytes): raise SfwValidationError('DS polish resource source drift')
        inputs = operation.get('source_inputs', [])
        if not inputs: raise SfwValidationError('DS polish missing source identity')
        sources = []
        for item in inputs:
            row = by_id.get(item.get('ledger_id'))
            if row is None: raise SfwValidationError('DS polish unknown SFW source id')
            for field in ('archive_sha256', 'logical_path', 'archive_entry', 'resource_sha256', 'root', 'prefix'):
                if row.get(field) != operation.get(field): raise SfwValidationError('DS polish source identity drift: ' + field)
            for field in ('raw_source', 'raw_source_sha256', 'source_ordinal'):
                if row.get(field) != item.get(field): raise SfwValidationError('DS polish raw English identity drift')
            sources.append(row)
        matches = []
        for i in range(len(parsed)-len(sources)+1):
            group = parsed[i:i+len(sources)]
            if all(p['root'] == r['root'] and p['prefix'] == r['prefix'] and p['raw_source'] == r['raw_source']
                   and p['raw_source_sha256'] == r['raw_source_sha256'] and p['source_ordinal'] == r['source_ordinal'] for p, r in zip(group, sources)):
                numbers = [p['line'] for p in group]
                if numbers == list(range(numbers[0], numbers[0]+len(numbers))): matches.append(numbers)
        if len(matches) != 1: raise SfwValidationError('DS polish source not uniquely consecutive')
        numbers = matches[0]; join_id = operation.get('canonical_join_id')
        if join_id:
            if canonical_join_report is None:
                report['withheld_without_canonical_joins'].append(operation['operation_id']); continue
            groups = [g for g in canonical_join_report['groups'] if g['join_id'] == join_id and g['actual_sfw_lines'] == numbers]
            if len(groups) != 1: raise SfwValidationError('DS polish canonical join was not applied to own source')
            if any(_line_parts(lines[n-1])[0] for n in numbers[1:]): raise SfwValidationError('DS polish consumed join tail not blank')
        elif len(numbers) != 1:
            raise SfwValidationError('DS polish multi-source operation missing canonical join')
        elif canonical_join_report and any(numbers[0] in g['actual_sfw_lines'] for g in canonical_join_report['groups']):
            raise SfwValidationError('DS polish single source was consumed elsewhere')
        if occupied.intersection(numbers): raise SfwValidationError('overlapping DS polish operations')
        occupied.update(numbers)
        old_payload = operation['old_payload']; replacement = operation['replacement']
        if text_digest(old_payload) != operation['old_payload_sha256'] or text_digest(replacement) != operation['replacement_sha256']:
            raise SfwValidationError('DS polish payload SHA drift')
        identity = [operation['archive_sha256'], logical_path, [r['id'] for r in sources], join_id, text_digest(old_payload)]
        if operation['operation_id'] != 'SFWDSP' + text_digest(json.dumps(identity, separators=(',', ':')))[:24]:
            raise SfwValidationError('DS polish operation ID drift')
        if _line_parts(lines[numbers[0]-1])[0] != operation['prefix'] + old_payload:
            raise SfwValidationError('DS polish old Chinese candidate drift')
        validate_target(old_payload, replacement, glyphs)
        plans.append((operation, numbers))
    for operation, numbers in plans:
        _, eol = _line_parts(lines[numbers[0]-1])
        lines[numbers[0]-1] = operation['prefix'] + operation['replacement'] + eol
        report['applied_operations'] += 1
        report['operations'].append({'operation_id': operation['operation_id'], 'actual_sfw_source_lines': numbers,
              'source_ledger_ids': [i['ledger_id'] for i in operation['source_inputs']], 'canonical_join_id': operation['canonical_join_id']})
    return ''.join(lines).encode('utf-8'), report


def _vsn_controls(data: bytes):
    return [line for line in data.splitlines(keepends=True)
            if line.strip() and not VSN_TEXT.match(_line_parts(line.decode('utf-8'))[0])]


def apply_vsn_joins(logical_path, original_bytes, localized_bytes, records, join_records, *, glyphs=None):
    """Apply reviewed, SFW-source-pinned ordinary text joins entirely in memory."""
    selected = [j for j in join_records if j.get('logical_path') == logical_path]
    report = {'applied_groups': 0, 'retained_groups': 0, 'click_reduction': 0, 'groups': []}
    if not selected: return localized_bytes, report
    source_lines = original_bytes.decode('utf-8').splitlines(keepends=True)
    translated_lines = localized_bytes.decode('utf-8').splitlines(keepends=True)
    if len(source_lines) != len(translated_lines): raise SfwValidationError('VSN physical line count drift')
    parsed = parse_resource(logical_path, original_bytes)
    text_at_line = {p['line']: p for p in parsed}
    for n, (source, target) in enumerate(zip(source_lines, translated_lines), 1):
        sb, se = _line_parts(source); tb, te = _line_parts(target)
        if se != te: raise SfwValidationError('VSN EOL drift')
        if n not in text_at_line:
            if source != target: raise SfwValidationError('VSN non-text command/staging drift')
        elif not tb.startswith(text_at_line[n]['prefix']):
            raise SfwValidationError('VSN command prefix/role drift')
    by_id = {r['id']: r for r in records}
    occupied = set(); seen = set(); plans = []
    for join in selected:
        if join.get('schema') != 'sfw-vsn-joins/v1' or join.get('status') != 'candidate' or join.get('variant') != 'sfw':
            raise SfwValidationError('VSN join schema/status/variant drift')
        if join.get('join_id') in seen: raise SfwValidationError('duplicate VSN join id')
        seen.add(join['join_id'])
        if join.get('resource_sha256') != digest(original_bytes) or join.get('archive') != ARCHIVE or join.get('prefix') != 'text: ':
            raise SfwValidationError('VSN join source identity/prefix drift')
        inputs = join.get('inputs', [])
        if len(inputs) < 2: raise SfwValidationError('VSN join needs multiple text nodes')
        source_records = []
        for item in inputs:
            row = by_id.get(item.get('ledger_id'))
            if row is None: raise SfwValidationError('VSN join unknown source ledger id')
            for name in ('archive_sha256', 'archive_entry', 'logical_path', 'resource_sha256'):
                if join.get(name) != row.get(name): raise SfwValidationError('VSN join resource identity drift: ' + name)
            if row['prefix'] != 'text: ' or row['role'] or row['status'] not in ('candidate', 'reused_candidate'):
                raise SfwValidationError('VSN join special role/auto/untranslated source prohibited')
            for name in ('root', 'raw_source', 'raw_source_sha256', 'source_ordinal'):
                if item.get(name) != row.get(name): raise SfwValidationError('VSN join raw source identity drift')
            if item.get('input_translation_sha256') != text_digest(row['translation']): raise SfwValidationError('VSN join input candidate drift')
            source_records.append(row)
        identity = [join['archive_sha256'], logical_path, [r['id'] for r in source_records]]
        expected_id = 'SFWJ' + text_digest(json.dumps(identity, separators=(',', ':')))[:24]
        if join['join_id'] != expected_id: raise SfwValidationError('VSN join ID drift')
        matches = []
        for i in range(len(parsed)-len(inputs)+1):
            group = parsed[i:i+len(inputs)]
            if all(p['prefix'] == 'text: ' and p['root'] == r['root'] and p['raw_source'] == r['raw_source']
                   and p['raw_source_sha256'] == r['raw_source_sha256'] and p['source_ordinal'] == r['source_ordinal']
                   for p, r in zip(group, source_records)):
                numbers = [p['line'] for p in group]
                if numbers == list(range(numbers[0], numbers[0]+len(numbers))): matches.append(numbers)
        if len(matches) != 1: raise SfwValidationError('VSN join nonunique/nonconsecutive source match')
        numbers = matches[0]
        if occupied.intersection(numbers): raise SfwValidationError('overlapping VSN joins')
        occupied.update(numbers)
        if source_lines[max(0,numbers[0]-6):numbers[0]-1] != join['context_before'] or source_lines[numbers[-1]:numbers[-1]+5] != join['context_after']:
            raise SfwValidationError('VSN join stage context drift')
        merged = join['merged_translation']
        if text_digest(merged) != join.get('merged_translation_sha256'): raise SfwValidationError('VSN merged translation drift')
        validate_target(' '.join(r['raw_source'] for r in source_records), merged, glyphs)
        for number, row in zip(numbers, source_records):
            body, _ = _line_parts(translated_lines[number-1])
            if body != row['prefix'] + row['translation']: raise SfwValidationError('VSN localized input candidate drift')
        if join.get('click_reduction') != len(numbers)-1: raise SfwValidationError('VSN click delta drift')
        plans.append((join, numbers))
    for join, numbers in plans:
        translated_lines[numbers[0]-1] = 'text: ' + join['merged_translation'] + _line_parts(source_lines[numbers[0]-1])[1]
        for number in numbers[1:]: translated_lines[number-1] = _line_parts(source_lines[number-1])[1]
        report['groups'].append({'join_id': join['join_id'], 'retained_first_source_line': numbers[0],
                'blanked_source_lines': numbers[1:], 'source_ledger_ids': [r['ledger_id'] for r in join['inputs']],
                'click_reduction': len(numbers)-1})
        report['applied_groups'] += 1; report['click_reduction'] += len(numbers)-1
    result = ''.join(translated_lines).encode('utf-8')
    if _vsn_controls(original_bytes) != _vsn_controls(result): raise SfwValidationError('VSN non-text command sequence not conserved')
    report['non_text_command_sha256_before'] = digest(b''.join(_vsn_controls(original_bytes)))
    report['non_text_command_sha256_after'] = digest(b''.join(_vsn_controls(result)))
    report['source_text_commands'] = len(parsed)
    report['output_text_commands'] = len(parse_resource(logical_path, result))
    if report['source_text_commands'] - report['output_text_commands'] != report['click_reduction']:
        raise SfwValidationError('VSN text/click conservation drift')
    return result, report


def build_replacements(original_jar_path, *, glyphs=None, allow_pattern_candidates=False):
    """Integration adapter: includes validated canonical SFW joins by default.

    Returns (dict[archive_entry, plaintextBytes], report); callers MUST NOT rerun
    dialogue_sfw over this output, because its 834 joins are already included.
    """
    import dialogue_joins
    data_dir = Path(__file__).resolve().parents[1] / 'optimization/r28/sfw'
    return rebuild_candidate_entries(original_jar_path, data_dir,
            canonical_join_records=dialogue_joins.load_records(), glyphs=glyphs,
            allow_pattern_candidates=allow_pattern_candidates)
