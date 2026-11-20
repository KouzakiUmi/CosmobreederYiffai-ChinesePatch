"""CPU acceptance contract for a full candidate."""

CPU_STEPS = (
    'compile-tests', 'radio-labels', 'core-regression', 'pixel-layout', 'dialogue-grid',
    'dialogue-wrap', 'continue', 'subtitle', 'pattern', 'ending-sfw', 'ending-nsfw',
    'scenes', 'story12-lifecycle', 'shop-text', 'ds-parse', 'compact-inputs',
    'compact-compile', 'compact-cpu', 'compact-pixels',
)
CPU_STATUS = 'passed_cpu_only_not_real_clip_CRT_input'
ACCEPTANCE_STATUS = 'passed_cpu_and_readback_not_real_clip_CRT_input'
LEGACY_ACCEPTANCE_STATUS = 'passed_cpu_and_independent_review_not_real_clip_CRT_input'


def validate_cpu_result(result: dict, candidate_sha: str) -> None:
    expected = [{'name': step, 'exit_code': 0} for step in CPU_STEPS]
    if (result.get('status') != CPU_STATUS or result.get('candidate_sha256') != candidate_sha
            or result.get('steps') != expected or result.get('test_sources_unchanged_after_run') is not True):
        raise ValueError('CPU 回归记录未覆盖当前归档的全部必需步骤')
