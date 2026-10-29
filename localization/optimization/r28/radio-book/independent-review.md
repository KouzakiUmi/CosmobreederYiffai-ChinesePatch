# 无线电人名与图鉴字号独立增量审查

**PASS：可作为本地安装器打包输入；不代表实机验收或安装授权。**

## 实际归档 SHA-256

- candidate4 cosmobreeder-multi.jar: `e4ebec610af21d83840abaabbca39dde09d6ffac5aa852a0023ce6b5f51922b7`
- candidate4 patch.pak: `149768acbbc4b0a37c017baba63083cc0ab5056e808380915cb24468f4bbcccd`
- candidate2 cosmobreeder-multi.jar: `b8ad97ee9a5d96f38b8e3753bc3252d723c68c4686acef875e10ce69325c63c3`
- candidate2 patch.pak: `10db525de973dc20a4c5f20b30bd989a0dcb1b0b08d80344b122bddeaa0cf245`

## 检查证据

### PASS — archive_resource_equivalence
Compared all 649 jar and 447 pak non-class entries. Entry sets unchanged except added PRG/RadioLabels.class. All byte-different encrypted resources decrypted equal (jar 43; pak 47); remaining entries byte-identical. No non-class plaintext differences.

### PASS — fonts_unchanged
All font files and atlas/resource bytes equal after decryption to candidate2; no glyph/font asset change.

### PASS — target_scope
Only existing classes JM,JQ,Kc,SceneText changed; only new RadioLabels.class. javap semantic diff: Kc only list SN.a -> SceneText.dataName; SceneText only dataBlock and added dataName; JM/JQ only four display insertions and three draw/one drawTint substitutions. Constant-pool indices, ldc width and shifted branch offsets normalized for inspection; no other semantic instruction changes seen.

### PASS — radio_identity_and_coverage
All four JF.a name lookups in JM/JQ adapted only after lookup. JF.class unchanged. Exact-name mapping preserves null/unknown/script keys, hidden ?????? and THE0; ID arguments/control flow retained. Actual candidate radio test PASS: 4 display, 3 draw, 1 tint; six case-insensitive variants; original 48px frequency column and 104px total.

### PASS — book_layout
Chinese list/title uses classic8; hidden ASCII list names retain input role. Chinese descriptions use sn.b/default10, 10px baseline pitch, 224px width and preflight all <=3 rows before drawing. ASCII branch retains GRID8/8px and b/c roles. Actual Kc CPU tests cover 33 SFW +59 NSFW descriptions, style pass/colour, full-source conservation and overflow rejection; source fixture up to66 Chinese chars fits,67 rejects.

### PASS — actual_ink_padding
Read actual RGBA atlas alpha glyph crops: 2421 relevant visible glyphs per font. default10 Han maximum ink height9, combined y extent[0,10); classic8 Han maximum7, combined y extent[0,8); ASCII y extent[0,8). Therefore unchanged transparent BMFont padding does not force row ink overlap at respective10/8px pitches. This is pixel-alpha evidence, not GPU filtering proof.

### PASS — candidate_cpu_suite
Observed completed results status passed_cpu_only_not_real_clip_CRT_input, all17 recorded steps exit0; test_sources_unchanged_after_run true. radio/ending/scenes logs read; scenes4919 checks,16200 CPU vertices,337 corpus fields. Did not rerun suite or claim own execution.

### PASS — source_identity
Independently recomputed all candidate build source pins and test source pins: zero drift. Four build commands exit0 and integrated_candidate_not_real_clip_CRT_input_acceptance.

### PASS — prior_acceptance_inheritance
Recomputed both candidate2 archive hashes, prior build-manifest hash and all4 linked acceptance evidence hashes: all match. Unchanged resources/fonts and all other classes permit inheriting prior CPU/static evidence only for unchanged content. Changed methods covered by current incremental review/current CPU suite; prior acceptance never claimed real clip/CRT/input.

## 源文件 SHA-256

- [SceneText.java](../../../../localization/layout/src/PRG/SceneText.java): `f8456cf427a8d33d8fb180333a20e3314b35e51c52e26b038863aba5e17217a8`
- [RadioLabels.java](../../../../localization/layout/src/PRG/RadioLabels.java): `518de07397cc6450d8d7f4fc7cc1aa67da318825e73eb67c051eaac5eb2f8982`
- [SceneTextPatch.java](../../../../localization/layout/tools/java/SceneTextPatch.java): `d4d4b180c6fd2555df2ac63aa20af9ba0c085cd8d7a4333c443088a818652d2c`
- [RadioLabelsPatch.java](../../../../localization/layout/tools/java/RadioLabelsPatch.java): `20313e933a55f96fa878103e3be7cfab1347a00886d6abcd65525580c2c8fedd`
- [EndingReportLayoutTest.java](../../../../localization/layout/tests/EndingReportLayoutTest.java): `276a055e22b33083f6f417dbfd238af6a7bccf708eb12535c9eadea5bfd9016b`
- [SceneTextTest.java](../../../../localization/layout/tests/SceneTextTest.java): `e869adae478926f1ed14dcaba321695a2c57aba3c2d00edb9b926bde42575dfd`
- [RadioLabelsTest.java](../../../../localization/layout/tests/RadioLabelsTest.java): `bdd5f4963fa33e4cf783ea24333bc55e2773c6346620c209034f1894fae3a366`
- [build_candidate.py](../../../../localization/optimization/r28/integration/build_candidate.py): `9550b12e00ea1635cb86751c16ccba723b248a234aedeeeabd0dfcfa51f37418`
- [test_candidate.py](../../../../localization/optimization/r28/integration/test_candidate.py): `9d935d14dc64dbbc7ec0683acb0d596cb3cd5d5fa59513ee1af725c6102f5eed`

## 限制

- Real game reachability, hidden-character reveal interactions, input/IME and real saves
- GPU/shader/CRT/filtering and full scene parent clip/FBO/layering
- Installer package creation/installation/deployment (not performed)
- All future unknown/dynamic text; normalized javap inspection is not independent full ASM metadata canonicalization

本审查未委派、未安装部署、未执行 Git 写入；只创建本报告两文件。首次 Python 读取大清单使用默认 GBK 失败，改为显式 UTF-8 后完成，未产生工程副作用。
