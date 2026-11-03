本表由脚本从仓库现状生成，只描述结构一致性，不代表语义或实机验收。

## 一、逐批

| 批次 | gate 状态 | 操作数 | 台账行数 | apply | reject | hold | 基础候选 |
| --- | --- | --- | --- | --- | --- | --- | --- |
| batch-01 | verified_for_application | 32 | 32 | 32 | 2 | 1 | localization/builds/r8-puzzle-candidate12 |
| batch-03 | verified_for_application | 28 | 28 | 28 | 5 | 2 | localization/builds/r9-polish-candidate13 |
| batch-02 | verified_for_application | 24 | 24 | 24 | 11 | 3 | localization/builds/r9-polish-candidate14 |
| batch-04 | verified_for_application | 19 | 19 | 19 | 14 | 7 | localization/builds/r9-polish-candidate15 |
| batch-05-part01 | verified_for_application | 41 | 41 | 41 | 11 | 4 | localization/builds/r9-polish-candidate16 |
| batch-05-part03 | verified_for_application | 36 | 36 | 36 | 18 | 2 | localization/builds/r9-polish-candidate17 |
| batch-05-part02 | verified_for_application | 26 | 26 | 26 | 27 | 2 | localization/builds/r9-polish-candidate18 |
| batch-06-part02 | verified_for_application | 30 | 30 | 30 | 11 | 2 | localization/builds/r9-polish-candidate19 |
| batch-06-part01 | verified_for_application | 28 | 28 | 28 | 8 | 2 | localization/builds/r9-polish-candidate20 |
| batch-06-part04 | verified_for_application | 20 | 20 | 20 | 14 | 1 | localization/builds/r9-polish-candidate21 |
| batch-06-part03 | verified_for_application | 41 | 41 | 41 | 19 | 2 | localization/builds/r9-polish-candidate23 |
| batch-07-part01 | verified_for_application | 32 | 32 | 32 | 4 | 2 | localization/builds/r9-polish-candidate24 |
| batch-07-part02 | verified_for_application | 23 | 23 | 23 | 7 | 0 | localization/builds/r9-polish-candidate25 |
| batch-08-part01 | verified_for_application | 24 | 24 | 24 | 26 | 3 | localization/builds/r9-polish-candidate26 |
| batch-08-part02 | verified_for_application | 25 | 25 | 25 | 2 | 1 | localization/builds/r9-polish-candidate27 |
| batch-08-part03 | verified_for_application | 24 | 24 | 24 | 0 | 1 | localization/builds/r9-polish-candidate28 |
| batch-08-part04 | verified_for_application | 32 | 32 | 32 | 3 | 1 | localization/builds/r9-polish-candidate29 |
| batch-08-part05 | verified_for_application | 27 | 27 | 27 | 23 | 0 | localization/builds/r9-polish-candidate30 |
| batch-09-part01 | verified_for_application | 24 | 24 | 24 | 23 | 0 | localization/builds/r9-polish-candidate31 |
| batch-09-part02 | verified_for_application | 15 | 15 | 15 | 6 | 0 | localization/builds/r9-polish-candidate32 |
| batch-09-part03 | verified_for_application | 24 | 24 | 24 | 32 | 0 | localization/builds/r9-polish-candidate33 |
| batch-09-part04 | verified_for_application | 17 | 17 | 17 | 15 | 0 | localization/builds/r9-polish-candidate34 |
| batch-10-part01 | verified_for_application | 10 | 10 | 10 | 1 | 0 | localization/builds/r9-polish-candidate35 |
| batch-10-part02 | verified_for_application | 8 | 8 | 8 | 0 | 0 | localization/builds/r9-polish-candidate36 |
| batch-10-part03 | verified_for_application | 15 | 15 | 15 | 3 | 0 | localization/builds/r9-polish-candidate37 |
| batch-11 | verified_for_application | 25 | 25 | 25 | 1 | 0 | localization/builds/r9-polish-candidate38 |
| batch-12-part01 | verified_for_application | 14 | 14 | 14 | 6 | 0 | localization/builds/r9-polish-candidate39 |
| batch-12-part02 | verified_for_application | 13 | 13 | 13 | 16 | 0 | localization/builds/r9-polish-candidate40 |
| batch-12-part03 | verified_for_application | 12 | 12 | 12 | 11 | 0 | localization/builds/r9-polish-candidate41 |
| batch-13 | verified_for_application | 17 | 17 | 17 | 25 | 0 | localization/builds/r9-polish-candidate42 |

## 二、候选与回归

| 候选 | results.json 位置 | status | 17 步是否全 0 |
| --- | --- | --- | --- |
| r9-polish-candidate13 | localization/optimization/r28/integration/tests/r9-polish-candidate13/results.json | passed_cpu_only_not_real_clip_CRT_input | 是 |
| r9-polish-candidate14 | localization/optimization/r28/integration/tests/r9-polish-candidate14/results.json | passed_cpu_only_not_real_clip_CRT_input | 是 |
| r9-polish-candidate15 | localization/optimization/r28/integration/tests/r9-polish-candidate15/results.json | passed_cpu_only_not_real_clip_CRT_input | 是 |
| r9-polish-candidate16 | localization/optimization/r28/integration/tests/r9-polish-candidate16/results.json | passed_cpu_only_not_real_clip_CRT_input | 是 |
| r9-polish-candidate17 | localization/optimization/r28/integration/tests/candidate17/results.json | passed_cpu_only_not_real_clip_CRT_input | 是 |
| r9-polish-candidate18 | localization/optimization/r28/integration/tests/candidate18/results.json | passed_cpu_only_not_real_clip_CRT_input | 是 |
| r9-polish-candidate19 | localization/optimization/r28/integration/tests/candidate19/results.json | passed_cpu_only_not_real_clip_CRT_input | 是 |
| r9-polish-candidate20 | localization/optimization/r28/integration/tests/candidate20/results.json | passed_cpu_only_not_real_clip_CRT_input | 是 |
| r9-polish-candidate21 | localization/optimization/r28/integration/tests/candidate21/results.json | passed_cpu_only_not_real_clip_CRT_input | 是 |
| r9-polish-candidate22 | localization/optimization/r28/integration/tests/candidate22/results.json | passed_cpu_only_not_real_clip_CRT_input | 是 |
| r9-polish-candidate23 | localization/optimization/r28/integration/tests/candidate23/results.json | passed_cpu_only_not_real_clip_CRT_input | 是 |
| r9-polish-candidate24 | localization/optimization/r28/integration/tests/candidate24/results.json | passed_cpu_only_not_real_clip_CRT_input | 是 |
| r9-polish-candidate25 | localization/optimization/r28/integration/tests/candidate25/results.json | passed_cpu_only_not_real_clip_CRT_input | 是 |
| r9-polish-candidate26 | localization/optimization/r28/integration/tests/candidate26/results.json | passed_cpu_only_not_real_clip_CRT_input | 是 |
| r9-polish-candidate27 | localization/optimization/r28/integration/tests/candidate27/results.json | passed_cpu_only_not_real_clip_CRT_input | 是 |
| r9-polish-candidate28 | localization/optimization/r28/integration/tests/candidate28/results.json | passed_cpu_only_not_real_clip_CRT_input | 是 |
| r9-polish-candidate29 | localization/optimization/r28/integration/tests/candidate29/results.json | passed_cpu_only_not_real_clip_CRT_input | 是 |
| r9-polish-candidate30 | localization/optimization/r28/integration/tests/candidate30/results.json | passed_cpu_only_not_real_clip_CRT_input | 是 |
| r9-polish-candidate31 | localization/optimization/r28/integration/tests/candidate31/results.json | passed_cpu_only_not_real_clip_CRT_input | 是 |
| r9-polish-candidate32 | localization/optimization/r28/integration/tests/candidate32/results.json | passed_cpu_only_not_real_clip_CRT_input | 是 |
| r9-polish-candidate33 | localization/optimization/r28/integration/tests/candidate33/results.json | passed_cpu_only_not_real_clip_CRT_input | 是 |
| r9-polish-candidate34 | localization/optimization/r28/integration/tests/candidate34/results.json | passed_cpu_only_not_real_clip_CRT_input | 是 |
| r9-polish-candidate35 | localization/optimization/r28/integration/tests/candidate35/results.json | passed_cpu_only_not_real_clip_CRT_input | 是 |
| r9-polish-candidate36 | localization/optimization/r28/integration/tests/candidate36/results.json | passed_cpu_only_not_real_clip_CRT_input | 是 |
| r9-polish-candidate37 | localization/optimization/r28/integration/tests/candidate37/results.json | passed_cpu_only_not_real_clip_CRT_input | 是 |
| r9-polish-candidate38 | localization/optimization/r28/integration/tests/candidate38/results.json | passed_cpu_only_not_real_clip_CRT_input | 是 |
| r9-polish-candidate39 | localization/optimization/r28/integration/tests/candidate39/results.json | passed_cpu_only_not_real_clip_CRT_input | 是 |
| r9-polish-candidate40 | localization/optimization/r28/integration/tests/candidate40/results.json | passed_cpu_only_not_real_clip_CRT_input | 是 |
| r9-polish-candidate41 | localization/optimization/r28/integration/tests/candidate41/results.json | passed_cpu_only_not_real_clip_CRT_input | 是 |
| r9-polish-candidate42 | localization/optimization/r28/integration/tests/candidate42/results.json | passed_cpu_only_not_real_clip_CRT_input | 是 |
| r9-polish-candidate43 | localization/optimization/r28/integration/tests/candidate43/results.json | passed_cpu_only_not_real_clip_CRT_input | 是 |

## 三、对不上的地方

无

## 四、说明

decisions.tsv 第 7 列的 `hold` 是合法取值，表示当场留置，不是不一致。
台账 sha256 与 gate 记录相符即代表台账未被改动。
