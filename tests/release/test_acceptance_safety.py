"""Gate regressions using synthetic paths and results, never installed games."""
import copy
import os
from pathlib import Path
import sys
import tempfile
import unittest

sys.path.insert(0, str(Path(__file__).resolve().parents[2] / 'tools/lib'))
from acceptance_checks import CPU_STATUS, CPU_STEPS, validate_cpu_result  # noqa: E402
from output_paths import check_outputs, workspace_output  # noqa: E402
sys.path.insert(0, str(Path(__file__).resolve().parents[2] / 'tools'))
from tl_tool import check_runtime_markers  # noqa: E402


class AcceptanceSafetyTests(unittest.TestCase):
    def test_output_rejects_input_roots_current_workspace_and_backtracking(self):
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp).resolve()
            for output in ('.', 'tests', 'originals', 'payload', 'build', 'build/../originals', root.parent / 'elsewhere'):
                with self.subTest(output=output), self.assertRaises(ValueError):
                    workspace_output(root, output, parents=('payload', 'build'))
            self.assertEqual(workspace_output(root, 'payload', exact=('payload',)), root / 'payload')
            self.assertEqual(workspace_output(root, 'build/session/candidate', parents=('build',)),
                             root / 'build/session/candidate')

    def test_output_rejects_hardlinks(self):
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            fixture = root / 'fixture'
            fixture.write_bytes(b'preserve')
            os.link(fixture, root / 'generated')
            with self.assertRaisesRegex(ValueError, '硬链接'):
                check_outputs(root, ('generated',))
            self.assertEqual(fixture.read_bytes(), b'preserve')

    def test_full_cpu_seal_requires_exact_steps_and_candidate(self):
        result = {'status': CPU_STATUS, 'candidate_sha256': 'abc',
                  'test_sources_unchanged_after_run': True,
                  'steps': [{'name': name, 'exit_code': 0} for name in CPU_STEPS]}
        validate_cpu_result(result, 'abc')
        for revision in ({'steps': []}, {'steps': result['steps'][1:]}, {'candidate_sha256': 'other'},
                         {'test_sources_unchanged_after_run': False}):
            with self.assertRaisesRegex(ValueError, '必需步骤'):
                validate_cpu_result({**result, **revision}, 'abc')
        failed = copy.deepcopy(result)
        failed['steps'][3]['exit_code'] = 1
        with self.assertRaisesRegex(ValueError, '必需步骤'):
            validate_cpu_result(failed, 'abc')

    def test_script_guard_rejects_missing_dynamic_fields_and_changed_separators(self):
        check_runtime_markers('test', '[Hello, @Player]!|%d items', '[你好，@Player]！|%d 件')
        for edited in ('你好！|%d 件', '[你好，@Player]！%d 件', '[你好，@Player]！|%s 件'):
            with self.assertRaisesRegex(ValueError, '占位符或分隔符'):
                check_runtime_markers('test', '[Hello, @Player]!|%d items', edited)
