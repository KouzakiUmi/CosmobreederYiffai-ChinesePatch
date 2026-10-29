"""Isolated tests: no game/archive IO and no external dependencies."""
import hashlib
import importlib.util
from pathlib import Path
import unittest

spec = importlib.util.spec_from_file_location('editorial_repairs', Path(__file__).parents[1] / 'tools/editorial_repairs.py')
m = importlib.util.module_from_spec(spec)
spec.loader.exec_module(m)


def operation(data, old, new, *, entry='datadf/1', line=2, pointer=None, op_id='r1'):
    result = dict(op_id=op_id, archive='patch.pak', archive_entry=entry,
                  kind='json' if pointer is not None else 'line',
                  before_resource_sha256=hashlib.sha256(data).hexdigest(), old=old, new=new,
                  finding_ids=['R1-1'], source_refs=['review:R1'])
    result['pointer' if pointer is not None else 'line'] = pointer if pointer is not None else line
    return result


class EditorialRepairsTests(unittest.TestCase):
    def apply(self, data, ops, entry='datadf/1'):
        return m.apply_entry('patch.pak', entry, data, ops)[0]

    def reject(self, data, ops, entry='datadf/1'):
        with self.assertRaises(m.EditorialRepairError): self.apply(data, ops, entry)

    def test_joined_blank_tail_and_mixed_eol_preserved(self):
        data = '<scene>\r\nDerek: 原句。合句尾。\r\n \n\t\r#event\n'.encode()
        op = operation(data, 'Derek: 原句。合句尾。', 'Derek: 修订后的完整合句。')
        self.assertEqual(self.apply(data, [op]), '<scene>\r\nDerek: 修订后的完整合句。\r\n \n\t\r#event\n'.encode())

    def test_preflight_late_failure(self):
        data = b'<s>\n*: one\n*: two\n'
        a = operation(data, '*: one', '*: changed')
        b = operation(data, '*: wrong', '*: changed', line=3, op_id='r2')
        self.reject(data, [a, b]); self.assertEqual(data, b'<s>\n*: one\n*: two\n')

    def test_identity_scope_old_and_reapplication(self):
        data = b'<s>\n*: one\n'
        op = operation(data, '*: one', '*: two')
        self.reject(self.apply(data, [op]), [op])
        for field, value in [('archive', 'other.jar'), ('archive_entry', 'datadf/2'),
                             ('before_resource_sha256', '0'*64), ('old', '*: bad')]:
            self.reject(data, [dict(op, **{field: value})])
        for entry in ['datadf/0', 'datadf/01', '../datadf/1', 'code/1', 'image/1', 'datadf/1/x']:
            self.reject(data, [op], entry)
        with self.assertRaises(m.EditorialRepairError): m.apply_entry('jar', 'datadf/1', data, [op])

    def test_prefix_control_blank_newline(self):
        data = b'<s>\nDerek: one\n\n#event\n'
        for new in ['Other: two', 'Derek: two\nthree', 'Derek: ', '#event', 'Derek: two\u2028three']:
            self.reject(data, [operation(data, 'Derek: one', new)])
        self.reject(data, [operation(data, '', '*: new', line=3)])
        self.reject(data, [operation(data, '#event', '*: new', line=4)])

    def test_vsn_prefix(self):
        data = b'lang(Derek): one\nauto(3): two\ncommand: go\n'
        for n, old, new in [(1, 'lang(Derek): one', 'lang(Other): two'), (2, 'auto(3): two', 'auto(4): one'), (3, 'command: go', 'command: new')]:
            self.reject(data, [operation(data, old, new, entry='vsn/2', line=n)], 'vsn/2')
        op = operation(data, 'lang(Derek): one', 'lang(Derek): 中文', entry='vsn/2', line=1)
        self.assertIn('中文'.encode(), self.apply(data, [op], 'vsn/2'))

    def test_marker_segment_reordering_and_barrier(self):
        data = b'<s>\n*: @Derek one\n*: two\n#event\n*: three\n'
        a = operation(data, '*: @Derek one', '*: one')
        b = operation(data, '*: two', '*: @Derek two', line=3, op_id='r2')
        self.apply(data, [a, b])
        self.reject(data, [a])
        c = operation(data, '*: three', '*: @Derek three', line=5, op_id='r3')
        self.reject(data, [a, c])
        data = b'<s>\n*: @Derek @Derek\n'
        self.reject(data, [operation(data, '*: @Derek @Derek', '*: @Derek')])

    def test_percent_math_not_placeholder(self):
        data = b'<s>\n*: 50% damage + 2\n'
        self.apply(data, [operation(data, '*: 50% damage + 2', '*: 50% 伤害加 2')])

    def test_duplicate_target(self):
        data = b'<s>\n*: one\n'
        a = operation(data, '*: one', '*: two')
        b = dict(a, op_id='r2')
        self.assertEqual(self.apply(data, [a, b]), self.apply(data, [a]))
        self.reject(data, [a, dict(b, new='*: three')])
        self.reject(data, [a, a])

    def test_json_token_splice_unicode_nested_pointer(self):
        data = b'{ "a/b" : {"~x": ["\\u4e00 @Derek", 42, true, null]}, "keep":"\\u4e8c" }\r\n'
        op = operation(data, '一 @Derek', '@Derek 中文', entry='datay/4', pointer='/a~1b/~0x/0')
        out = self.apply(data, [op], 'datay/4')
        self.assertEqual(out, data.replace(b'"\\u4e00 @Derek"', '"@Derek 中文"'.encode()))
        self.reject(data, [dict(op, pointer='/a~1b/~0x/1', old='42')], 'datay/4')
        self.reject(data, [dict(op, pointer='/a~2b')], 'datay/4')
        self.reject(data, [dict(op, new='中文')], 'datay/4')
        self.reject(data, [dict(op, old='一')], 'datay/4')

    def test_json_duplicates_keys_and_nonstrings_protected(self):
        for data in [b'{"x":"a","x":"b"}', b'{"a":{"x":1,"x":2}}', b'{"x":NaN}']:
            self.reject(data, [], 'datav/1')
        data = b'{"x":42,"id":"name","v":"KEYCARD12"}'
        for pointer, old, new in [('/x', '42', '43'), ('/id', 'name', 'other'), ('/v', 'KEYCARD12', 'KEYCARD13')]:
            self.reject(data, [operation(data, old, new, entry='datav/1', pointer=pointer)], 'datav/1')

    def test_json_existing_newlines_exact_token_splice(self):
        data = b'{ "card": "old\\n", "keep": "\\u4e8c", "n": 7 }\r\n'
        op = operation(data, 'old\n', '新说明\n', entry='datav/1', pointer='/card')
        self.assertEqual(self.apply(data, [op], 'datav/1'), data.replace(b'"old\\n"', '"新说明\\n"'.encode()))
        for new in ['新说明', '新说明\n\n', '新说明\r', '新\t说明\n', '新\x00说明\n']:
            self.reject(data, [dict(op, new=new)], 'datav/1')
        data = b'{"card":"old\\r\\n"}'
        op = operation(data, 'old\r\n', '新说明\r\n', entry='datav/1', pointer='/card')
        self.assertEqual(self.apply(data, [op], 'datav/1'), '{"card":"新说明\\r\\n"}'.encode())
        self.reject(data, [dict(op, new='新说明\n')], 'datav/1')

    def test_actor_and_command_segments(self):
        data = b'<s>\nMauser: @Derek one\n\nMauser: two\nYiffai: three\nMauser: four\n'
        a = operation(data, 'Mauser: @Derek one', 'Mauser: one')
        b = operation(data, 'Mauser: two', 'Mauser: @Derek two', line=4, op_id='r2')
        self.apply(data, [a, b])
        for line, old, new in [(5, 'Yiffai: three', 'Yiffai: @Derek three'), (6, 'Mauser: four', 'Mauser: @Derek four')]:
            self.reject(data, [a, operation(data, old, new, line=line, op_id='r3')])
        data = b'auto(3): @Derek one\nauto(4): two\n'
        a = operation(data, 'auto(3): @Derek one', 'auto(3): one', entry='vsn/1', line=1)
        b = operation(data, 'auto(4): two', 'auto(4): @Derek two', entry='vsn/1', line=2, op_id='r2')
        self.reject(data, [a, b], 'vsn/1')

    def test_all_entries_preflight(self):
        data = b'<s>\n*: one\n'
        a = operation(data, '*: one', '*: two')
        b = operation(data, '*: wrong', '*: three', entry='datadm/2', op_id='r2')
        entries = {('patch.pak', 'datadf/1'): data, ('patch.pak', 'datadm/2'): data}
        with self.assertRaises(m.EditorialRepairError): m.apply_entries(entries, [a, b])
        self.assertTrue(all(v == data for v in entries.values()))


if __name__ == '__main__':
    unittest.main()
