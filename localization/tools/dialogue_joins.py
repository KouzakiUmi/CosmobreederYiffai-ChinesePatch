"""Explicit occurrence-level DS joins; canonical units and global QA are unchanged.

Only candidate_user_requested ledger entries are applied, not inferred candidates.
No runtime dialogue/index keys are invented. Later physical lines become blank
lines (including removal of their actor prefix), never empty dialogue nodes.
"""
from collections import Counter
from pathlib import Path
import argparse
import json
import re

from projectlib import (PROJECT, current_translations, digest, glyph_metrics,
                        load_occurrences, load_units, protected, read_jsonl,
                        source_hash)

LEDGER = PROJECT / 'translations/dialogue-joins.jsonl'
WORK = PROJECT / 'work/dialogue-join-test'
HEADER = re.compile(r'^<([^<>\r\n]+)>$')
PREFIX = re.compile(r'^[ \t]*(?:\* |[A-Za-z][A-Za-z0-9_]*(?:/[A-Za-z][A-Za-z0-9_]*)?: )$')
HAN = re.compile(r'[\u3400-\u9fff]')


class JoinValidationError(ValueError):
    """A complete apply is rejected; no partially modified bytes are returned."""


def _require(condition, message):
    if not condition:
        raise JoinValidationError(message)


def _split(data):
    """Retain exact LF/CRLF/CR bytes, including a missing final terminator."""
    data.decode('utf-8')
    return data.splitlines(keepends=True)


def _body_eol(line):
    for eol in (b'\r\n', b'\n', b'\r'):
        if line.endswith(eol):
            return line[:-len(eol)], eol
    return line, b''


def _contexts(lines, dialogue_lines):
    """Pin the full header and preceding non-text branch/event evidence."""
    result = {}
    header = root = None
    header_line = None
    controls = []
    for number, raw in enumerate(lines, 1):
        body = _body_eol(raw)[0].decode('utf-8')
        match = HEADER.fullmatch(body.strip())
        if match:
            header, root, header_line = body, match[1].split()[0], number
            controls = []
        elif number not in dialogue_lines and body.strip() and not body.lstrip().startswith('#'):
            controls.append({'line': number, 'body': body, 'sha256': source_hash(body)})
        result[number] = {'root': root, 'full_header': header,
                          'header_line': header_line, 'control_lines': list(controls)}
    return result


def _signature(text):
    # Multisets, not just counts: replacement of one tag/placeholder by another
    # must fail even when the number of tokens is unchanged.
    return {'placeholders': Counter(protected(text)),
            'angle_tags': Counter(re.findall(r'<[^<>\r\n]*>', text)),
            'underscore_runs': Counter(re.findall(r'_+', text)),
            'pipes': text.count('|'), 'newlines': text.count('\n'),
            'open_square': text.count('['), 'close_square': text.count(']')}


def _whole_bracket(text):
    return (text.startswith('[') and text.endswith(']')
            and text.count('[') == text.count(']') == 1
            and not protected(text[1:-1]))


def load_records():
    return read_jsonl(LEDGER)


def _validate_markers(record, sources, inputs, merged):
    for source, text in zip(sources, inputs):
        _require(_signature(source) == _signature(text), 'Input/source marker drift')
    coalesce = record.get('coalesce_outer_brackets')
    _require(type(coalesce) is bool, 'Missing explicit bracket policy')
    delta = -(len(inputs) - 1) if coalesce else 0
    _require(record.get('expected_marker_delta') ==
             {'open_square': delta, 'close_square': delta}, 'Incorrect bracket delta')
    if coalesce:
        _require(all(_whole_bracket(t) for t in sources + inputs + [merged]),
                 'Coalesce requires complete, unnested, variable-free outer []')
    before, after = _signature(''.join(inputs)), _signature(merged)
    for key in before:
        expected = before[key] + delta if key in ('open_square', 'close_square') else before[key]
        _require(after[key] == expected, 'Merged marker drift: ' + key)


def apply_joins(logical_path: str, original_bytes: bytes, localized_bytes: bytes,
                records=None):
    """Return (new_bytes, report), applying only exact occurrence allowlist matches.

    original_bytes must be canonical extract/patch DS; localized_bytes is the
    unjoined R21-style inline localized resource. Every applicable record is
    preflighted before any output copy is modified. Source/input drift raises
    JoinValidationError (ValueError), never a partial result. records=[] is a
    deliberate no-op. Caller supplies decrypted bytes; this API writes nothing.
    """
    records = load_records() if records is None else list(records)
    selected = [r for r in records if r.get('logical_path') == logical_path]
    report = {'logical_path': logical_path, 'applied_groups': 0,
              'removed_text_nodes': 0, 'groups': [], 'occurrence_mapping': [],
              'input_sha256': digest(localized_bytes)}
    if not selected:
        report['output_sha256'] = digest(localized_bytes)
        return localized_bytes, report
    resources = {r['logical_path']: r for r in read_jsonl(PROJECT / 'catalog/resources.jsonl')}
    _require(logical_path in resources, 'Unknown source resource')
    source_sha = digest(original_bytes)
    _require(resources[logical_path]['sha256'] == source_sha, 'Canonical resource SourceSHA mismatch')
    units = {u['id']: u for u in load_units()}
    occurrences = {o['occurrence_id']: o for o in load_occurrences()}
    path_occurrences = {o['line']: o for o in occurrences.values()
                        if o.get('logical_path') == logical_path and o['category'] == 'dialogue'}
    translations = current_translations()
    original, localized = _split(original_bytes), _split(localized_bytes)
    _require(len(original) == len(localized), 'Physical line count drift')
    for number, (old, new) in enumerate(zip(original, localized), 1):
        _require(_body_eol(old)[1] == _body_eol(new)[1], 'EOL drift at line ' + str(number))
        if number not in path_occurrences:
            _require(old == new, 'Non-dialogue control/event/header drift at line ' + str(number))
    contexts = _contexts(original, path_occurrences)
    localized_contexts = _contexts(localized, path_occurrences)
    occupied, record_ids, plans = set(), set(), []
    metrics = glyph_metrics()
    for record in selected:
        rid = record.get('join_id')
        _require(isinstance(rid, str) and rid and rid not in record_ids, 'Duplicate/missing join id')
        record_ids.add(rid)
        _require(record.get('schema_version') == 1, 'Unknown join schema')
        _require(record.get('status') == 'candidate_user_requested', 'Unsupported join status')
        origin = record.get('origin', {})
        _require(origin.get('authorization') == 'user_requested_sentence_join'
                 and origin.get('agent') and origin.get('reason'), 'Missing truthful user-request origin')
        _require(record.get('source_resource_sha256') == source_sha, 'Ledger SourceSHA mismatch')
        inputs = record.get('inputs', [])
        _require(len(inputs) >= 2, 'Join needs at least two inputs')
        numbers = [i.get('line') for i in inputs]
        _require(all(type(n) is int and 1 <= n <= len(original) for n in numbers), 'Invalid physical lines')
        _require(numbers == list(range(numbers[0], numbers[0] + len(numbers)))
                 and numbers == record.get('physical_lines'), 'Nonconsecutive/reordered input lines')
        _require(not occupied.intersection(numbers), 'Overlapping joins')
        occupied.update(numbers)
        prefix = record.get('prefix', '')
        _require(bool(PREFIX.fullmatch(prefix)), 'Not a text-node prefix')
        actor = prefix.strip().removesuffix(':')
        _require(actor == record.get('actor'), 'Actor/expression drift')
        context = contexts[numbers[0]]
        for key in ('root', 'full_header', 'header_line'):
            _require(record.get(key) == context[key], 'Header/root drift: ' + key)
        evidence = record.get('branch_evidence')
        _require(evidence == {'consecutive_physical_lines': True,
                             'identical_prefix': prefix,
                             'intervening_control_lines': [],
                             'preceding_control_lines': context['control_lines']}, 'Invalid branch evidence')
        texts, sources = [], []
        for item, number in zip(inputs, numbers):
            oid, uid = item.get('occurrence_id'), item.get('unit_id')
            _require(oid in occurrences and uid in units, 'Unknown occurrence/unit')
            occurrence, unit = occurrences[oid], units[uid]
            _require(occurrence == path_occurrences.get(number)
                     and occurrence['unit_id'] == uid and occurrence['prefix'] == prefix,
                     'Occurrence location/unit/prefix mismatch')
            _require(occurrence['entry'] == context['full_header'].strip()[1:-1]
                     and contexts[number] == context and localized_contexts[number] == context,
                     'Root/branch/event boundary crossed')
            source = unit['source']
            _require(item.get('source_sha256') == unit['source_sha256'] == source_hash(source),
                     'Unit source hash drift')
            _require(source_hash(occurrence['leading_ws'] + source + occurrence['trailing_ws'])
                     == occurrence['raw_payload_sha256'], 'Occurrence payload hash drift')
            _require(_body_eol(original[number - 1])[0] ==
                     (prefix + occurrence['leading_ws'] + source + occurrence['trailing_ws']).encode('utf-8'),
                     'Original text/prefix mismatch')
            _require(item.get('input_field') == 'draft', 'Only pinned existing draft inputs are supported')
            tr = translations.get(uid, {})
            text = item.get('input_translation')
            _require(isinstance(text, str) and HAN.search(text) and text.strip() == text,
                     'Non-CJK/empty/edge-whitespace input')
            _require(tr.get('source_sha256') == unit['source_sha256']
                     and tr.get('draft') == text
                     and source_hash(text) == item.get('input_translation_sha256'), 'Draft/input SHA drift')
            _require(_body_eol(localized[number - 1])[0] ==
                     (prefix + occurrence['leading_ws'] + text + occurrence['trailing_ws']).encode('utf-8'),
                     'Localized CJK input/prefix mismatch')
            texts.append(text)
            sources.append(source)
        merged = record.get('merged_translation')
        _require(isinstance(merged, str) and HAN.search(merged) and merged.strip() == merged,
                 'Invalid merged translation')
        _require(not any(ord(c) < 32 or c in '\u2028\u2029' for c in merged)
                 and '|' not in merged and '<p>' not in merged, 'Merged node delimiter/control injection')
        _require(source_hash(merged) == record.get('merged_translation_sha256'), 'Merged translation SHA drift')
        _require(all(ord(c) in metrics for c in merged), 'Missing merged glyph')
        _validate_markers(record, sources, texts, merged)
        first = path_occurrences[numbers[0]]
        plans.append((record, (prefix + first['leading_ws'] + merged + first['trailing_ws']).encode('utf-8')))
    # All preflight checks above complete before modifying this copy.
    output = localized[:]
    for record, first_body in plans:
        numbers = record['physical_lines']
        output[numbers[0] - 1] = first_body + _body_eol(localized[numbers[0] - 1])[1]
        for number in numbers[1:]:
            output[number - 1] = _body_eol(localized[number - 1])[1]
        report['groups'].append({'join_id': record['join_id'], 'physical_lines': numbers,
                                 'expected_marker_delta': record['expected_marker_delta']})
        for item in record['inputs']:
            report['occurrence_mapping'].append({
                'occurrence_id': item['occurrence_id'], 'unit_id': item['unit_id'],
                'source_line': item['line'], 'merged_into_occurrence_id': record['inputs'][0]['occurrence_id'],
                'output_line': numbers[0], 'original_physical_line_retained': True,
                'disposition': 'merged_text' if item['line'] == numbers[0] else 'blank_physical_line'})
        report['removed_text_nodes'] += len(numbers) - 1
    result = b''.join(output)
    report.update(applied_groups=len(plans), output_sha256=digest(result),
                  source_resource_sha256=source_sha, physical_line_count=len(output))
    return result, report


def build_record(occurrence_ids: list[str], merged_translation: str, reason: str,
                 *, agent: str = 'caller') -> dict:
    """Build one in-memory candidate from canonical tables, then fully preflight.

    Does NOT persist/approve the record or infer a sentence boundary. The caller
    must supply the explicit ordered occurrences, edited text and justification.
    agent identifies that caller, not an invented historical generation model.
    Canonical catalog resources only: alternate/SFW resources need their own
    real occurrence evidence, never a reused PAK line number.
    """
    _require(isinstance(occurrence_ids, list) and len(occurrence_ids) >= 2
             and all(isinstance(oid, str) for oid in occurrence_ids)
             and len(set(occurrence_ids)) == len(occurrence_ids), 'Invalid explicit occurrence list')
    _require(isinstance(merged_translation, str) and isinstance(reason, str)
             and reason.strip() and isinstance(agent, str) and agent.strip(), 'Missing caller/text/reason')
    occurrences = {o['occurrence_id']: o for o in load_occurrences()}
    _require(all(oid in occurrences for oid in occurrence_ids), 'Unknown occurrence')
    rows = [occurrences[oid] for oid in occurrence_ids]
    path = rows[0].get('logical_path', '')
    _require(path.endswith('.ds') and all(o.get('logical_path') == path
             and o['category'] == 'dialogue' for o in rows), 'Mixed/non-DS occurrence resources')
    resources = {r['logical_path']: r for r in read_jsonl(PROJECT / 'catalog/resources.jsonl')}
    _require(path in resources, 'Unknown canonical resource')
    original = (PROJECT / resources[path]['blob_path']).read_bytes()
    lines = _split(original)
    all_text = {o['line']: o for o in occurrences.values()
                if o.get('logical_path') == path and o['category'] == 'dialogue'}
    numbers = [o['line'] for o in rows]
    context = _contexts(lines, all_text)[numbers[0]]
    units = {u['id']: u for u in load_units()}
    translations = current_translations()
    inputs, sources, texts = [], [], []
    localized = lines[:]
    for occurrence in rows:
        uid, number = occurrence['unit_id'], occurrence['line']
        _require(uid in units and uid in translations, 'Missing unit/draft')
        unit, text = units[uid], translations[uid].get('draft')
        _require(isinstance(text, str), 'Missing draft input')
        sources.append(unit['source'])
        texts.append(text)
        inputs.append({'occurrence_id': occurrence['occurrence_id'], 'unit_id': uid,
                       'line': number, 'source_sha256': unit['source_sha256'],
                       'input_field': 'draft', 'input_translation': text,
                       'input_translation_sha256': source_hash(text)})
        localized[number - 1] = (occurrence['prefix'] + occurrence['leading_ws'] + text
                                 + occurrence['trailing_ws']).encode('utf-8') + _body_eol(lines[number - 1])[1]
    prefix = rows[0]['prefix']
    coalesce = all(_whole_bracket(t) for t in sources + texts + [merged_translation])
    delta = -(len(rows) - 1) if coalesce else 0
    identity = json.dumps([path, occurrence_ids, merged_translation], ensure_ascii=False, separators=(',', ':'))
    record = {'schema_version': 1, 'join_id': 'DJ' + source_hash(identity)[:20],
              'logical_path': path, 'source_resource_sha256': digest(original),
              'root': context['root'], 'full_header': context['full_header'],
              'header_line': context['header_line'], 'physical_lines': numbers,
              'prefix': prefix, 'actor': prefix.strip().removesuffix(':'),
              'branch_evidence': {'consecutive_physical_lines': True, 'identical_prefix': prefix,
                                  'intervening_control_lines': [],
                                  'preceding_control_lines': context['control_lines']},
              'inputs': inputs, 'merged_translation': merged_translation,
              'merged_translation_sha256': source_hash(merged_translation),
              'coalesce_outer_brackets': coalesce,
              'expected_marker_delta': {'open_square': delta, 'close_square': delta},
              'status': 'candidate_user_requested',
              'origin': {'agent': agent, 'authorization': 'user_requested_sentence_join',
                         'reason': reason, 'independent_qa_approval': False}}
    apply_joins(path, original, b''.join(localized), records=[record])
    return record


def scan_candidates():
    """Read-only heuristic audit, NEVER an approval or input to apply_joins.

    Strict adjacent physical lines, same root and exact actor/expression prefix;
    both drafts contain Han and the left fragment lacks terminal punctuation
    (one complete outer [] pair is ignored for this heuristic only).
    """
    translations = current_translations()
    units = {u['id']: u for u in load_units()}
    by_path = {}
    for o in load_occurrences():
        if o['category'] == 'dialogue':
            by_path.setdefault(o['logical_path'], {})[o['line']] = o
    pairs = []
    for path, rows in sorted(by_path.items()):
        for number, left in sorted(rows.items()):
            right = rows.get(number + 1)
            if not right or left['entry'] != right['entry'] or left['prefix'] != right['prefix']:
                continue
            if not PREFIX.fullmatch(left['prefix']):
                continue
            a, b = [translations.get(o['unit_id'], {}).get('draft', '') for o in (left, right)]
            tail = a[1:-1].rstrip() if _whole_bracket(a) else a.rstrip()
            if not (HAN.search(a) and HAN.search(b)) or not tail or re.search(r'[。！？!?；;…\.：:]$', tail):
                continue
            pairs.append({'logical_path': path, 'root': left['entry'].split()[0],
                          'entry': left['entry'], 'prefix': left['prefix'],
                          'physical_lines': [number, number + 1],
                          'occurrence_ids': [left['occurrence_id'], right['occurrence_id']],
                          'unit_ids': [left['unit_id'], right['unit_id']],
                          'sources': [units[o['unit_id']]['source'] for o in (left, right)],
                          'drafts': [a, b], 'status': 'unreviewed_audit_only'})
    groups = []
    for pair in pairs:
        if (groups and groups[-1]['logical_path'] == pair['logical_path']
                and groups[-1]['root'] == pair['root'] and groups[-1]['prefix'] == pair['prefix']
                and groups[-1]['physical_lines'][-1] == pair['physical_lines'][0]):
            for key in ('physical_lines', 'occurrence_ids', 'unit_ids', 'sources', 'drafts'):
                groups[-1][key].append(pair[key][-1])
        else:
            groups.append({k: list(v) if isinstance(v, list) else v for k, v in pair.items()})
    return {'policy': 'strict-adjacent-same-root-prefix-CJK-unfinished-left; audit-only',
            'pair_count': len(pairs), 'group_count': len(groups), 'groups': groups}


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--audit', action='store_true', required=True,
                        help='Write unreviewed candidates only under localization/work/dialogue-join-test')
    args = parser.parse_args()
    if args.audit:
        audit = scan_candidates()
        WORK.mkdir(parents=True, exist_ok=True)
        path = WORK / 'candidate-audit.json'
        path.write_text(json.dumps(audit, ensure_ascii=False, indent=2) + '\n', encoding='utf-8')
        print(json.dumps({'pairs': audit['pair_count'], 'groups': audit['group_count'],
                          'output': str(path)}, ensure_ascii=False))


if __name__ == '__main__':
    main()
