"""Materialize explicit reviewed decisions, never infer approval from candidates."""
from pathlib import Path
from collections import Counter
import difflib
import hashlib
import json
import re
import sys
import zipfile

HERE = Path(__file__).resolve().parent
ROOT = HERE.parents[3]
LOC = ROOT / 'localization'
sys.path.insert(0, str(LOC / 'tools'))
from codec import decrypt_file
from projectlib import read_jsonl
from vsn_joins import _body_eol, _split, _markers, sha


def dump(name, value):
    (HERE / name).write_text(json.dumps(value, ensure_ascii=False, indent=2) + '\n', 'utf8')


def jsonl(name, values):
    (HERE / name).write_text(''.join(json.dumps(x, ensure_ascii=False, separators=(',', ':'))+'\n' for x in values), 'utf8')


def build():
    groups = json.loads((HERE / 'review-packet.json').read_text('utf8'))
    decisions = dict(line.split('\t', 1) for line in (HERE / 'review-decisions.tsv').read_text('utf8').splitlines() if line and not line.startswith('#'))
    rs = {r['logical_path']: r for r in read_jsonl(LOC / 'catalog/resources.jsonl')}
    occs = [o for o in read_jsonl(LOC / 'catalog/occurrences.jsonl') if o['category'] == 'vsn']
    units = {u['id']: u for u in read_jsonl(LOC / 'catalog/units.jsonl')}
    trs = {t['id']: t for t in read_jsonl(LOC / 'translations/zh-CN.jsonl')}
    candidates = {
        'V167883e168bd7c10f05c': '花在之前那只蓝毛小不点狗崽身上！',
        'V867a6108a4d88bae1ff5': '我知道他快了，因为他不光插得更快，也插得更浅，',
        'V876a2c862a11be84474f': '总不让那些凸粒全滑出来，一个劲地挑逗我里面，',
        'V7dc63e6b0fb2a1999cc9': '到时候再来找我，做点更适合成年人的事吧。',
    }
    scripts, pins, full_contexts = {}, {}, {}
    build = LOC / 'builds/r27-story12-shaderfix-test5'
    with zipfile.ZipFile(build / 'patch.pak') as z:
        idx = json.loads(decrypt_file(z.read('vsn/0')))
        for logical, e in sorted(idx.items()):
            if not logical.endswith('/script.vsn'): continue
            path = 'vsn/' + logical.strip('/').split('/')[-2] + '/script.vsn'
            data = decrypt_file(z.read('vsn/' + str(e)))
            source = (LOC / rs[path]['blob_path']).read_bytes()
            assert sha(source) == rs[path]['sha256']
            en, cn = _split(source), _split(data)
            assert len(en) == len(cn)
            rows = {o['line']: o for o in occs if o['logical_path'] == path}
            for n, (a, b) in enumerate(zip(en, cn), 1):
                assert _body_eol(a)[1] == _body_eol(b)[1]
                if n not in rows: assert a == b
                else:
                    o = rows[n]; u = units[o['unit_id']]; t = trs[o['unit_id']]
                    assert _body_eol(a)[0].decode('utf8') == o['prefix'] + o['leading_ws'] + u['source'] + o['trailing_ws']
                    expected = t['draft'] if t.get('draft') else u['source']
                    assert _body_eol(b)[0].decode('utf8') == o['prefix'] + o['leading_ws'] + expected + o['trailing_ws']
            controls = [{'line': n, 'raw': line.decode('utf8')} for n, line in enumerate(cn, 1) if n not in rows]
            pins[path] = {'archive': 'patch.pak', 'archive_entry': 'vsn/' + str(e),
                          'canonical_source_sha256': sha(source), 'r27_plaintext_sha256': sha(data),
                          'physical_line_count': len(cn), 'control_sha256': sha(b''.join(cn[n-1] for n in range(1, len(cn)+1) if n not in rows))}
            scripts[path] = cn
            full_contexts[path] = [{'line': n, 'source': a.decode('utf8'), 'r27_localized': b.decode('utf8'),
                                    'is_text_occurrence': n in rows} for n, (a, b) in enumerate(zip(en, cn), 1)]
    reviewed, operations = [], []
    for g in groups:
        gid, path, nums = g['group_id'], g['logical_path'], g['lines']
        cn = scripts[path]
        controls = [{'line': row['line'], 'raw': row['r27_localized']} for row in full_contexts[path] if not row['is_text_occurrence']]
        inputs = []
        for item in g['inputs']:
            o, u, t = item['occurrence'], item['unit'], item['translation']
            line = _body_eol(cn[o['line']-1])[0]
            inputs.append({'logical_path': path, 'line': o['line'], 'occurrence_id': o['occurrence_id'],
                           'unit_id': u['id'], 'prefix': o['prefix'], 'source_en': u['source'],
                           'source_sha256': u['source_sha256'], 'raw_payload_sha256': o['raw_payload_sha256'],
                           'input_line': line.decode('utf8'), 'input_line_sha256': sha(line),
                           'input_translation': t.get('draft') or None,
                           'input_status': t['status']})
        reviewed_row = {'schema_version': 1, 'review_group_id': gid, 'archive': 'patch.pak',
                        'logical_path': path, 'source_resource_sha256': pins[path]['canonical_source_sha256'],
                        'input_resource_sha256': pins[path]['r27_plaintext_sha256'],
                        'candidate_edges': [e['lines'] for e in g['edges']], 'inputs': inputs,
                        'reviewed_context': g['context_lines'], 'joins': [], 'skipped_edges': [],
                        'origin': {'authorization': 'user_requested_vsn_sentence_join_and_translation',
                                   'method': '逐组阅读完整英中演出段及事件，显式决定；非启发式自动批准',
                                   'independent_qa_approval': False}}
        if g['prefix'] != 'text: ':
            assert gid not in decisions
            decision = 'SKIP:具名Fox/HardFox字形语言角色；没有足够语言理解状态及显露时序证据，默认保持原独立话语与点按，避免提前解读。'
        else:
            assert gid in decisions, ('unreviewed text group', gid)
            decision = decisions[gid]
        if decision.startswith('SKIP:'):
            join_nums = []
            reason = decision[5:]
        else:
            if decision.startswith('PART:'):
                _, span, replacement = decision.split(':', 2)
                a, b = map(int, span.split('-')); join_nums = list(range(a, b+1))
                reason = {'VG031': '仅接原69-70句法续行；70-71保留词中断与自我改口。',
                          'VG064': '11已是完整陈述，保留其独立话语；仅12-13主谓补语续接。',
                          'VG154': '123为以<3结束的独立祈使感叹，保留点按；仅124-125接同一句精液叙述。',
                          'VG160': '7-8为同一条件从句；8-9另起感官设置陈述，保留独立点按。',
                          'VG217': '67已完整并在68转话题；只接68-69的claim to have宾语续行。'}[gid]
            else:
                join_nums = nums
                texts = [i['input_line'][6:].strip() for i in inputs]
                replacement = ''.join(texts) if decision == '=' else decision.join(texts) if decision in ('，', '。') else decision
                reason = ('已逐组核对同演出块内的英文句法依存和中文全文；续行补足前句，'
                          '不跨任何音效/角色/画面/同步事件。保留句内省略及未完结尾，中文软换行取代原命令硬断。')
            chosen = [i for i in inputs if i['line'] in join_nums]
            assert len(chosen) == len(join_nums) and len(chosen) >= 2
            assert _markers(''.join(i['input_line'][6:] for i in chosen)) == _markers(replacement), gid
            identity = gid + '-' + '-'.join(map(str, join_nums))
            evidence = {'control_lines': controls, 'intervening_controls': [],
                        'automatic_delay_delta_seconds': 0,
                        'manual_text_node_delta': -(len(join_nums)-1),
                        'manual_policy': '合并后每一布局页仍手动推进；后页队列在原下一事件之前全部消费；只移除句中原text硬断。',
                        'protected_roles': 'lang(Fox),lang(HardFox),auto完全不改'}
            edit = [{'tag': tag, 'input_range': [a,b], 'output_range': [c,d],
                     'before': ''.join(i['input_line'][6:].strip() for i in chosen)[a:b], 'after': replacement[c:d]}
                    for tag,a,b,c,d in difflib.SequenceMatcher(None, ''.join(i['input_line'][6:].strip() for i in chosen), replacement, autojunk=False).get_opcodes()]
            op = {'schema_version': 1, 'operation_id': identity, 'review_group_id': gid, 'kind': 'join',
                  'archive': 'patch.pak', 'logical_path': path,
                  'source_resource_sha256': pins[path]['canonical_source_sha256'],
                  'input_resource_sha256': pins[path]['r27_plaintext_sha256'],
                  'physical_lines': join_nums, 'inputs': chosen, 'replacement': replacement,
                  'replacement_sha256': sha(replacement.encode('utf8')), 'control_evidence': evidence,
                  'review_reason': reason, 'text_edit_evidence': edit,
                  'status': 'candidate_user_requested', 'independent_qa_approval': False}
            operations.append(op)
            reviewed_row['joins'].append({'operation_id': identity, 'physical_lines': join_nums, 'replacement': replacement, 'reason': reason})
        edges = list(zip(join_nums, join_nums[1:]))
        for edge in g['edges']:
            if tuple(edge['lines']) not in edges:
                reviewed_row['skipped_edges'].append({'lines': edge['lines'], 'reason': reason})
        reviewed_row['decision'] = 'partial' if reviewed_row['joins'] and reviewed_row['skipped_edges'] else 'accepted' if reviewed_row['joins'] else 'retained'
        reviewed.append(reviewed_row)
    assert set(decisions) == {g['group_id'] for g in groups if g['prefix'] == 'text: '}
    translated = []
    for uid, candidate in candidates.items():
        os = [o for o in occs if o['unit_id'] == uid]
        assert len(os) == 1 and trs[uid]['status'] == 'untranslated'
        o = os[0]; u = units[uid]
        used = [r for r in operations if any(i['unit_id'] == uid for i in r['inputs'])]
        assert len(used) == 1
        translated.append({'unit_id': uid, 'occurrence_id': o['occurrence_id'], 'logical_path': o['logical_path'],
                           'line': o['line'], 'prefix': o['prefix'], 'source_en': u['source'],
                           'source_sha256': u['source_sha256'], 'raw_payload_sha256': o['raw_payload_sha256'],
                           'source_resource_sha256': pins[o['logical_path']]['canonical_source_sha256'],
                           'input_resource_sha256': pins[o['logical_path']]['r27_plaintext_sha256'],
                           'candidate_zh_CN': candidate, 'status': 'candidate_user_requested',
                           'applied_in_join': used[0]['operation_id'], 'canonical_translation_unchanged': True})
    jsonl('review-ledger.jsonl', reviewed)
    jsonl('operations.jsonl', operations)
    dump('source-join-suggestions.json', [{'canonical_operation_id': r['operation_id'],
         'scene': r['logical_path'].split('/')[1], 'prefix': 'text: ',
         'ordered_source_en': [i['source_en'] for i in r['inputs']],
         'ordered_source_sha256': [i['source_sha256'] for i in r['inputs']],
         'candidate_zh_CN': r['replacement'],
         'warning': 'Suggestion only: no SFW line numbers or approval; independently verify unique whole-source identity, staging/actor/timing context and own occurrence ledger.'}
         for r in operations])
    dump('continuation-translations.json', translated)
    dump('full-script-contexts.json', full_contexts)
    required = ''.join(sorted(set(''.join(r['replacement'] for r in operations))))
    (HERE / 'required_chars.txt').write_text(required + '\n', 'utf8')
    summary = {'reviewed_candidate_edges': sum(len(g['edges']) for g in groups), 'reviewed_maximal_groups': len(groups),
               'accepted_join_groups': len(operations), 'accepted_edges': sum(len(r['inputs'])-1 for r in operations),
               'fully_accepted_review_groups': sum(r['decision'] == 'accepted' for r in reviewed),
               'partially_accepted_review_groups': sum(r['decision'] == 'partial' for r in reviewed),
               'fully_retained_review_groups': sum(r['decision'] == 'retained' for r in reviewed),
               'explicitly_retained_edges': sum(len(r['skipped_edges']) for r in reviewed),
               'protected_lang_retained_edges': sum(len(g['edges']) for g in groups if g['prefix'] != 'text: '),
               'four_untranslated_units': len(translated), 'automatic_delay_delta_seconds': 0}
    dump('review-summary.json', summary)
    dump('component.json', {'schema_version': 1, 'component': 'canonical-pak-vsn-joins',
                           'archive': 'patch.pak', 'frozen_build': 'r27-story12-shaderfix-test5',
                           'frozen_archive_sha256': sha((build / 'patch.pak').read_bytes()),
                           'operations_sha256': sha((HERE / 'operations.jsonl').read_bytes()),
                           'review_ledger_sha256': sha((HERE / 'review-ledger.jsonl').read_bytes()),
                           'required_chars': 'localization/optimization/r28/vsn/required_chars.txt',
                           'required_chars_sha256': sha((HERE / 'required_chars.txt').read_bytes()),
                           'api': {'module': 'localization/tools/vsn_joins.py', 'function': 'rewrite_vsn',
                                   'signature': "rewrite_vsn(logical_path, source_bytes, records=None, *, archive='patch.pak') -> (new_bytes, report)",
                                   'source_bytes': 'decrypted exact r27 patch.pak plaintext for pinned logical path',
                                   'call_order': 'after decrypting frozen r27 PAK; before encrypting output; no prior translation/rewrite; SFW is forbidden',
                                   'atomicity': 'all applicable pinned operations preflight before output; raises VsnJoinValidationError on any drift'},
                           'summary': summary, 'resources': pins,
                           'tests': ['/c/Windows/py.exe -3.12 -B -m unittest discover -s localization/tests -p test_vsn_joins.py -v',
                                     '/c/Windows/py.exe -3.12 -B localization/optimization/r28/vsn/run_integration.py']})
    print(json.dumps(summary, ensure_ascii=False))

if __name__ == '__main__': build()
