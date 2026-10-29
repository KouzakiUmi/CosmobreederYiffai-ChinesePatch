"""Compile a source-locked, display-carrier-only R3 name preview.

No archive writes, builder/helper edits, approval promotion or game execution.
Usage: --registry PATH --output NEW_DIRECTORY_UNDER_r3-names/compiled
"""
from pathlib import Path
import sys
sys.dont_write_bytecode = True
import argparse
from collections import Counter, defaultdict
import hashlib
import json
import re
import zipfile

ROOT = Path(__file__).resolve().parents[4]
R3 = Path(__file__).resolve().parents[1]
INVENTORY = R3/'engineering/inventory.json'
BASELINE = 'localization/builds/r28-editorial-repairs-candidate6'
sys.path.insert(0, str(ROOT/'localization/tools'))
import editorial_repairs
from codec import decrypt_file

sha = lambda data: hashlib.sha256(data).hexdigest()
PUZZLE_NON_NAMES = {'RATS', 'ELGNAIRT', 'ELCRIC', 'SSORC'}
PROTECTED_ID = re.compile(r'(?<![A-Za-z0-9_])(?:[A-Za-z]+[0-9][A-Za-z0-9_-]*|[A-Za-z][A-Za-z0-9]*_[A-Za-z0-9_]+)(?![A-Za-z0-9_])')


class NamesError(ValueError):
    pass


def read_json(path):
    return json.loads(path.read_text('utf8'))


def write_json(path, value):
    path.write_text(json.dumps(value, ensure_ascii=False, indent=2)+'\n', encoding='utf8')


def target_key(carrier):
    if ('line' in carrier) == ('pointer' in carrier):
        raise NamesError('carrier must have exactly one locator')
    return (carrier['archive'], carrier['entry'], 'line' if 'line' in carrier else 'json',
            carrier.get('line', carrier.get('pointer')))


def boundary(text, start, end, form):
    """Latin token boundary, not an engine-ID/path/member substring.

    A sentence-ending period is allowed, but Foo.Tomcat or Tomcat.Area0 is not.
    Chinese adjacent prose is not a Latin word continuation.
    """
    latin = bool(re.search('[A-Za-z0-9]', form))
    if start and (text[start-1] in '@_/' + chr(92) or latin and re.match(r'[A-Za-z0-9]', text[start-1])):
        return False
    if end < len(text) and (text[end] in '_/' + chr(92) or latin and re.match(r'[A-Za-z0-9]', text[end])):
        return False
    if start >= 2 and text[start-1] == '.' and re.match(r'[A-Za-z0-9_]', text[start-2]):
        return False
    if end+1 < len(text) and text[end] == '.' and re.match(r'[A-Za-z0-9_]', text[end+1]):
        return False
    return True


def protected_spans(text):
    return [(m.start(), m.end()) for rx in (editorial_repairs.MARKERS, PROTECTED_ID)
            for m in rx.finditer(text)]


def carrier_allowed(c, name_id):
    if c.get('needs_manual_alignment') or not c.get('matched_variants'):
        return False, 'source_only_or_manual_alignment'
    if c.get('carrier') not in {'json_display_value', 'report_title', 'report_description',
                                'dex_title', 'dex_prose', 'task_log', 'dialogue_prose', 'vsn_prose'}:
        return False, 'unknown_carrier_usage'
    classification = c.get('classification')
    source = (c.get('source') or '').strip().upper()
    if classification == 'fenfen_reverse_puzzle_title_not_blanket_name':
        if name_id not in {'Sevaw', 'Erauqs'} or source in PUZZLE_NON_NAMES:
            return False, 'unproven_personal_name_puzzle_title'
    elif classification != 'proper_name_candidate':
        return False, 'context_sensitive_or_unknown_usage'
    pointer = c.get('pointer', '')
    if re.search(r'(?:^/supporters/|credits|backers|sponsor|patron|staff)', pointer, re.I):
        return False, 'real_credits_or_supporters'
    parts = editorial_repairs._pointer(pointer) if 'pointer' in c else ()
    if any(re.fullmatch(r'(?i)(?:id|.*_id|uuid|guid|internal_?id|flag|actor|speaker|portrait|gfx)', p)
           or re.fullmatch(r'.+Id', p) for p in parts):
        return False, 'protected_ID_or_control_field'
    if c.get('carrier') == 'report_title' and source in PUZZLE_NON_NAMES:
        return False, 'unproven_personal_name_puzzle_title'
    return True, None


def validate_registry(registry):
    if registry.get('baseline') != BASELINE:
        raise NamesError('registry must pin accepted candidate6 baseline')
    seen = set()
    for n in registry['names']:
        ident = n['name_id']
        if not isinstance(ident, str) or ident in seen:
            raise NamesError('duplicate/invalid name_id')
        seen.add(ident)
        for item in [n] + n.get('nicknames', []):
            if not isinstance(item['target'], str) or not item['target']:
                raise NamesError('empty/non-string name target')
            if not isinstance(item['old_forms'], list) or any(not isinstance(x, str) or not x for x in item['old_forms']):
                raise NamesError('invalid old_forms')
            editorial_repairs._safe_string(item['target'])
            for form in item['old_forms']:
                editorial_repairs._safe_string(form)
        # preserve_ascii_case means preserve a matching spelling byte-for-byte.
        if n.get('preserve_ascii_case') and any(x.casefold() != n['target'].casefold() for x in n['old_forms']):
            raise NamesError('preserve_ascii_case cannot authorize a different name')
    family = registry.get('family', {})
    if family and not family.get('preserve_repeated_full_name'):
        raise NamesError('full-name repetition must be preserved')


def nickname_source(c, nickname):
    source = c.get('source') or ''
    scope = nickname.get('allowed_carriers')
    if scope is not None and not any(c.get('archive') == s['archive'] and c.get('entry') == s['entry']
                                    and c.get('line') == s.get('line') and c.get('pointer') == s.get('pointer')
                                    for s in scope):
        return False
    flags = 0 if nickname.get('case_sensitive_source') else re.I
    return any(any(boundary(source, m.start(), m.end(), form)
                   for m in re.finditer(re.escape(form), source, flags))
               for form in nickname['source_forms'])


def rules_for_carrier(c, entries):
    rules = []
    for n in entries:
        for form in n['old_forms']:
            rules.append({'name_id': n['name_id'], 'form': form, 'target': n['target'],
                          'preserve_ascii_case': n.get('preserve_ascii_case', False),
                          'nickname': False, 'source_initials': [s[0] for s in n['source_forms']]})
        for nick in n.get('nicknames', []):
            if nickname_source(c, nick):
                for form in nick['old_forms']:
                    rules.append({'name_id': n['name_id'], 'form': form, 'target': nick['target'],
                                  'preserve_ascii_case': False, 'nickname': True,
                                  'source_initials': [s[0] for s in nick['source_forms']]})
    # Replacement reads only original text; targets never feed another rule.
    return sorted(rules, key=lambda x: (-len(x['form']), x['name_id'], x['form']))


def stutter_prefix(text, start, rule):
    """Adapt only contiguous, already-present one-sound name repetitions."""
    initials = {rule['form'][0], *rule['source_initials']}
    if rule['name_id'] == 'Tomcat':
        initials.add('汤')  # R2 withdrew full 汤姆猫 but may retain its stutter sound.
    allowed = {c.casefold() for c in initials}
    cursor = start
    repeats = []
    # Strict single-sound + separator, no inferred hesitation or inserted event.
    while cursor >= 2 and text[cursor-1] in '-、，':
        sound = text[cursor-2]
        if sound.casefold() not in allowed:
            break
        repeats.append((sound, text[cursor-1]))
        cursor -= 2
    if not repeats:
        return start, '', 0
    # The caller checks the complete expanded span against identifier boundaries.
    repeats.reverse()
    return cursor, ''.join(rule['target'][0]+sep for _, sep in repeats), len(repeats)


def rewrite_value(text, rules):
    protected = protected_spans(text)
    candidates = []
    unchanged = Counter()
    for rule in rules:
        form = rule['form']
        flags = re.I if re.search('[A-Za-z]', form) else 0
        for m in re.finditer(re.escape(form), text, flags):
            if not boundary(text, m.start(), m.end(), form):
                continue
            if any(m.start() < b and m.end() > a for a,b in protected):
                # A no-op The0 remains literal; do not count it as an ID rewrite.
                if rule['preserve_ascii_case'] and m[0].casefold() == rule['target'].casefold():
                    unchanged[rule['name_id']] += 1
                elif m[0] != rule['target'] and any(x.start()==m.start() and x.end()==m.end() for x in PROTECTED_ID.finditer(text)) and not any(m.start()<x.end() and m.end()>x.start() for x in editorial_repairs.MARKERS.finditer(text)):
                    raise NamesError('requested name is protected by engine ID-marker heuristic; report for review, never relax: '+m[0])
                continue
            replacement = m[0] if rule['preserve_ascii_case'] else rule['target']
            start, prefix, repetitions = stutter_prefix(text, m.start(), rule)
            if not boundary(text, start, m.end(), form):
                continue
            if start != m.start() and any(start < b and m.start() > a for a,b in protected):
                start, prefix, repetitions = m.start(), '', 0
            replacement = prefix + replacement
            old = text[start:m.end()]
            candidates.append({'start': start, 'end': m.end(), 'old': old, 'new': replacement,
                               'name_id': rule['name_id'], 'old_form': m[0], 'target': rule['target'],
                               'nickname': rule['nickname'], 'existing_stutter_repetitions': repetitions})
    # Longest old-form wins overlapping candidate matches; ties must agree.
    chosen = []
    for edit in sorted(candidates, key=lambda x: (-(len(x['old_form'])), x['start'], x['name_id'])):
        overlaps = [x for x in chosen if edit['start'] < x['end'] and edit['end'] > x['start']]
        if overlaps:
            if any(edit['start'] == x['start'] and edit['end'] == x['end'] and edit['new'] != x['new'] for x in overlaps):
                raise NamesError('conflicting authorized replacements')
            continue
        chosen.append(edit)
    for edit in chosen:
        if edit['old'] == edit['new']:
            unchanged[edit['name_id']] += 1
    chosen = sorted((e for e in chosen if e['old'] != e['new']), key=lambda x:x['start'])
    output = text
    for edit in reversed(chosen):
        if text[edit['start']:edit['end']] != edit['old']:
            raise NamesError('replacement span mismatch')
        output = output[:edit['start']] + edit['new'] + output[edit['end']:]
    # Masking proves all characters outside explicit authorized spans are equal.
    old_mask, new_mask, a, b = [], [], 0, 0
    for edit in chosen:
        old_mask.append(text[a:edit['start']]); old_mask.append('<NAME>')
        size = edit['start']-a
        new_mask.append(output[b:b+size]); new_mask.append('<NAME>')
        b += size+len(edit['new']); a = edit['end']
    old_mask.append(text[a:]); new_mask.append(output[b:])
    if old_mask != new_mask:
        raise NamesError('non-name character drift')
    return output, chosen, dict(unchanged)


def get_target(text, kind, locator):
    if kind == 'line':
        return text.splitlines()[locator-1]
    tokens = editorial_repairs._json_tokens(text)
    key = editorial_repairs._pointer(locator)
    if key not in tokens or not isinstance(tokens[key][2], str):
        raise NamesError('JSON target is not a string value')
    return tokens[key][2]


def check_source(entries, resource_pins, archive_pins=None, archive_bytes=None):
    """Exact baseline whole-entry pins, not a recomputed/new beforeSHA."""
    if archive_pins is not None:
        if set(archive_bytes) != set(archive_pins):
            raise NamesError('baseline archive set drift')
        for key, expected in archive_pins.items():
            if sha(archive_bytes[key]) != expected:
                raise NamesError('candidate6 archive SHA drift: '+key)
    for key, data in entries.items():
        if key not in resource_pins or sha(data) != resource_pins[key]:
            raise NamesError('candidate6 plaintextSHA drift: '+repr(key))


def plan_operations(registry, inventory):
    validate_registry(registry)
    if inventory['baseline'] != BASELINE:
        raise NamesError('inventory baseline drift')
    grouped = defaultdict(list)
    pending = []
    excluded = []
    counts = {n['name_id']: {'inventory_carriers': 0, 'eligible_carriers': 0,
                            'changed_occurrences': 0, 'changed_targets': 0,
                            'nickname_occurrences': 0, 'adapted_stutter_fragments': 0,
                            'unchanged_name_occurrences': 0} for n in registry['names']}
    for n in registry['names']:
        ident = n['name_id']
        if ident not in inventory['characters']:
            raise NamesError('unknown inventory character: '+ident)
        carriers = inventory['characters'][ident]['carriers']
        counts[ident]['inventory_carriers'] = len(carriers)
        for c in carriers:
            allowed, reason = carrier_allowed(c, ident)
            if not allowed:
                record = {'name_id': ident, 'reason': reason, 'carrier': c}
                (pending if reason in {'source_only_or_manual_alignment','unknown_carrier_usage','context_sensitive_or_unknown_usage'} else excluded).append(record)
                continue
            counts[ident]['eligible_carriers'] += 1
            grouped[target_key(c)].append((n,c))
    operations, bindings = [], []
    for key, pairs in sorted(grouped.items(), key=lambda kv:repr(kv[0])):
        archive, entry, kind, locator = key
        c = pairs[0][1]
        for _, other in pairs[1:]:
            for field in ('plaintextSHA','current','prefix','source','source_resourceSHA'):
                if other.get(field) != c.get(field):
                    raise NamesError('same-target carrier metadata conflict: '+field)
        entries = [n for n,_ in pairs]
        rules = rules_for_carrier(c, entries)
        value, edits, unchanged = rewrite_value(c['current'], rules)
        for ident, amount in unchanged.items():counts[ident]['unchanged_name_occurrences'] += amount
        if not edits:
            continue
        changed_names = sorted({e['name_id'] for e in edits})
        for ident in changed_names:counts[ident]['changed_targets'] += 1
        for edit in edits:
            cc = counts[edit['name_id']]
            cc['changed_occurrences'] += 1
            cc['nickname_occurrences'] += int(edit['nickname'])
            cc['adapted_stutter_fragments'] += edit['existing_stutter_repetitions']
        prefix = c.get('prefix','') if kind == 'line' else ''
        op = {'op_id':f'NAME-{len(operations)+1:04d}', 'archive':archive, 'archive_entry':entry,
              'kind':kind, 'before_resource_sha256':c['plaintextSHA'], 'old':prefix+c['current'],
              'new':prefix+value, 'finding_ids':['NAME:'+n for n in changed_names],
              'source_refs':['CARRIER:'+json.dumps(other,ensure_ascii=False,sort_keys=True) for _,other in pairs]}
        op['line' if kind=='line' else 'pointer'] = locator
        if kind=='line' and editorial_repairs._line_role(op['old'],entry.split('/')[0]) != (prefix,c['current']):
            raise NamesError('carrier prefix not an editable display line')
        operations.append(op)
        bindings.append({'op_id':op['op_id'], 'target':list(key), 'before_resource_sha256':c['plaintextSHA'],
                         'authorized_spans_in_value':edits, 'source_carriers':[other for _,other in pairs],
                         'old':op['old'], 'new':op['new']})
    return operations, bindings, counts, pending, excluded


def verify_r2(before, after, operations, ledger):
    op_map={(op['archive'],op['archive_entry'],op['kind'],op.get('line',op.get('pointer'))):op for op in operations}
    checks=[]
    for op in ledger:
        key=(op['archive'],op['archive_entry'])
        kind=op['kind']; locator=op.get('line',op.get('pointer'))
        old=get_target(before[key].decode('utf8'),kind,locator)
        current=get_target(after[key].decode('utf8'),kind,locator)
        if old != op['new']:
            raise NamesError('baseline R2 repair mismatch: '+op['op_id'])
        names=op_map.get((*key,kind,locator))
        expected=names['new'] if names else op['new']
        if current != expected:
            raise NamesError('non-name R2 repair drift: '+op['op_id'])
        checks.append({'r2_op_id':op['op_id'],'names_op_id':names['op_id'] if names else None,
                       'before_targetSHA':sha(old.encode()),'after_targetSHA':sha(current.encode()),
                       'non_name_preserved':True})
    return {'operations_checked':len(checks), 'non_name_preserved':len(checks),
            'exact_targets_unchanged':sum(c['names_op_id'] is None for c in checks), 'checks':checks}


def compile_preview(registry_path, output):
    registry_path=registry_path.resolve(); output=output.resolve()
    allowed=(R3/'compiled').resolve()
    if output.exists() or output==allowed or not output.is_relative_to(allowed):
        raise NamesError('output must be NEW subdirectory under r3-names/compiled')
    registry_bytes=registry_path.read_bytes(); inventory_bytes=INVENTORY.read_bytes()
    registry=json.loads(registry_bytes); inventory=json.loads(inventory_bytes)
    manifest={'schema':'r3.names.compilation.v1', 'status':'unvalidated',
              'registry_status':registry.get('status'), 'semantic_approval':False,
              'baseline':BASELINE, 'registry':str(registry_path.relative_to(ROOT)).replace('\\','/'),
              'registrySHA':sha(registry_bytes), 'inventorySHA':sha(inventory_bytes),
              'compilerSHA':sha(Path(__file__).read_bytes()), 'baseline_archiveSHA':inventory['archiveSHA'],
              'game_started':False, 'installed':False, 'archive_written':False,
              'builder_or_helper_modified':False}
    operations=[]; bindings=[]; all_entries={}; reports=[]; after={}
    try:
        operations,bindings,counts,pending,excluded=plan_operations(registry,inventory)
        manifest.update({'name_counts':counts, 'pending_review':pending, 'excluded_carriers':excluded,
                         'inventory_exclusions_preserved':Counter(c['classification'] for c in inventory['excluded_or_context_sensitive_carriers']),
                         'protected_actor_carriers_not_scanned':len(inventory['actor_label_carriers']),
                         'zero_carrier_names':[n for n,c in counts.items() if c['inventory_carriers']==0],
                         'zero_change_names':[n for n,c in counts.items() if c['changed_targets']==0]})
        resource_pins={(r['archive'],r['entry']):r['plaintextSHA'] for r in inventory['resources']}
        archives={a:(ROOT/BASELINE/a).read_bytes() for a in inventory['archiveSHA']}
        # Verify archive pins before decryption and every inventoried text entry after.
        check_source({},resource_pins,inventory['archiveSHA'],archives)
        for archive,data in archives.items():
            from io import BytesIO
            with zipfile.ZipFile(BytesIO(data)) as z:
                if z.testzip() is not None:raise NamesError('candidate6 archive CRC error')
                for a,entry in resource_pins:
                    if a==archive:all_entries[(a,entry)]=decrypt_file(z.read(entry))
        check_source(all_entries,resource_pins)
        for op in operations:
            if op['before_resource_sha256']!=resource_pins[(op['archive'],op['archive_entry'])]:
                raise NamesError('operation pin differs from candidate6 inventory')
        after,reports=editorial_repairs.apply_entries(all_entries,operations)
        # The engine emits a new mapping; untouched resources retain exactly the original bytes.
        touched={(op['archive'],op['archive_entry']) for op in operations}
        for key,data in all_entries.items():
            if key not in touched and after[key]!=data:raise NamesError('untargeted resource changed')
            if re.findall(rb'\r\n|\r|\n',after[key])!=re.findall(rb'\r\n|\r|\n',data):
                raise NamesError('physical newline/CRLF event drift')
        for op in operations:
            key=(op['archive'],op['archive_entry'])
            if get_target(after[key].decode('utf8'),op['kind'],op.get('line',op.get('pointer')))!=op['new']:
                raise NamesError('post-apply exact target mismatch')
        ledger_path=ROOT/'localization/translations/editorial-r2-repairs.jsonl'
        ledger=[json.loads(s) for s in ledger_path.read_text('utf8').splitlines() if s.strip()]
        manifest['r2_preservation']=verify_r2(all_entries,after,operations,ledger)
        manifest['r2_ledgerSHA']=sha(ledger_path.read_bytes())
        manifest['status']='validated_proposed_preview_not_approved'
        manifest['all_entry_preflight']='passed'
        manifest['resources_verified_against_candidate6']=len(all_entries)
        manifest['untouched_resources_byte_identical']=len(all_entries)-len(touched)
    except (NamesError,editorial_repairs.EditorialRepairError,ValueError,KeyError,IndexError) as exc:
        manifest['failure']={'type':type(exc).__name__,'message':str(exc)}
        manifest['all_entry_preflight']='failed_or_not_reached'
    # Only this NEW isolated directory is ever written.
    output.mkdir(parents=True)
    valid=manifest['status']=='validated_proposed_preview_not_approved'
    op_path=output/('operations.jsonl' if valid else 'operations.unvalidated.jsonl')
    op_path.write_text(''.join(json.dumps(op,ensure_ascii=False)+'\n' for op in operations),encoding='utf8')
    write_json(output/'bindings.json',bindings)
    manifest['operations_file']=op_path.name; manifest['operationsSHA']=sha(op_path.read_bytes())
    manifest['operation_count']=len(operations); manifest['bindingsSHA']=sha((output/'bindings.json').read_bytes())
    manifest['target_plaintext_previews']=[]
    if valid:
        for (archive,entry) in sorted({(op['archive'],op['archive_entry']) for op in operations}):
            base=Path('plaintext')/archive/entry
            before_path=output/(str(base)+'.before.txt'); after_path=output/(str(base)+'.after.txt')
            before_path.parent.mkdir(parents=True,exist_ok=True)
            before_path.write_bytes(all_entries[(archive,entry)]); after_path.write_bytes(after[(archive,entry)])
            manifest['target_plaintext_previews'].append({'archive':archive,'entry':entry,
                'before_file':before_path.relative_to(output).as_posix(),'after_file':after_path.relative_to(output).as_posix(),
                'before_plaintextSHA':sha(all_entries[(archive,entry)]),'after_plaintextSHA':sha(after[(archive,entry)])})
    manifest['resource_reports']=reports
    write_json(output/'manifest.json',manifest)
    print(json.dumps({'status':manifest['status'],'operations':len(operations),'output':str(output),'failure':manifest.get('failure')},ensure_ascii=False))
    return valid


def main():
    parser=argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--registry',type=Path,required=True)
    parser.add_argument('--output',type=Path,required=True)
    args=parser.parse_args()
    return 0 if compile_preview(args.registry,args.output) else 1


if __name__=='__main__':
    raise SystemExit(main())
