from pathlib import Path
import json,hashlib
H=Path(__file__).resolve().parent;R=H.parent;ROOT=H.parents[4]
p=R/'final-review.json';d=json.loads(p.read_text(encoding='utf8'))
assert d['status']=='PASS','Do not generate PASS prose for a failing audit; inspect final-review.json failures first.'
link=lambda name,path:'['+name+'](<'+path+'>)'
summary=['# R3 最终实际归档独立核验：'+d['status'],
 '', '**对象：candidate8；candidate7仅过渡，不是本次封签目标。** 本地构建／CPU验收，不是实机或发行部署批准。',
 '', '## 实际归档SHA256', '']
for a,h in d['archives'].items():summary+=['- '+link(a,'localization/builds/r28-character-names-candidate8/'+a)+'：`'+h+'`']
summary += ['', '## 结论与覆盖', '',
 '- **839操作／895受控姓名span／66实际改动资源（JAR27、PAK39）：PASS。** 每个实际目标等于冻结final-01.after；before等candidate6。全部839完整field新旧值、778项R2原目标及仅授权名字变化再核通过。冻结工程预检的895-span、marker／prefix／EOL／JSON key／动态@／控制字节证明通过精确资源等价继承，不以统计替代语义审查。',
 '- JAR262、PAK417个加密资源（含索引）完整比对：除66姓名正文与字体atlas外，未发现明文差异；未重新加密者原密文字节相同，重新加密者独立解密比较。归档entry集合不增不减、无重复、CRC通过；所有其他普通资产变更白名单及字体诊断副本一致性通过。',
 '- **仅5个class差异**：RadioLabels为已审36目标／37alias显示映射；正式helper由独立javac重新编译，结果逐字节等实际包内class及builder产物。DialogueWrap、EndingReportLayout、StoryFont12、SubtitleLayout只把已知role SHA UTF8常量中和后比较完整class剩余字节，全部一致，不做宽泛指令清洗。其余class原字节不变。',
 '- 实际包内JF原字节不变；JM／JQ及控制流程原字节不变。RadioLabelsPatch仍位于JF门控之后。Macsen／Gitgud没有新增正文姓名op，不因存在备用显示映射提前揭名。The0的0与输入case保留；名字显示不反写actor、participant、脚本变量或JSON key。',
 '- **6组字体旧字形通过**：每归档default2455→2459、classic2550→2554、story12 2455→2459；每组28个旧字内部坐标位移被允许，但全部旧codepoint裁切像素、非位置metrics、ASCII完整记录0变化。font globals／kerning及非字体atlas原画全像素一致。36姓名实际classic字形8px advance；中文classic／Latin传入role及六字符频率字段48px、总104px由实际归档标签CPU验证。',
 '- **17项最终CPU均exit0**，candidate SHA对应上述实际JAR；运行源码SHA与结束稳定标记通过。radio日志同时含RADIO_CANDIDATE_OK与RADIO_LABELS_OK，测试从实际candidate加载class，覆盖36目标／37alias、大小写／The0保留、classic／Latinrole、draw／tint及频率几何。未重复启动整套CPU。',
 '- 补充：主控报告13项编译器单测、3个精确昵称carrier与2个否定边界断言通过。本核验未重复执行；单独标注为主控完成见证，不用历史preview日志冒充本轮原始执行日志。',
 '- Builder新增第10 names组件已独立读源码：全组件门控、R2后／字体前、registry与36人工裁决逐目标绑定、carrier PASS及全部evidence SHA、manifest的registry／ops／compiler／inventory SHA、candidate6归档SHA、sync --check、outer源码快照及构建后再核均具备；实际快照与当前输入全部一致。',
 '- datav显示字典／datay missionLog的值与身份键区分已在冻结 '+link('engineering-01.md','localization/editorial/r3-names/review/engineering-01.md')+' 以真实消费者反汇编证明；本轮实际资源等于获审preview，未重新放宽为“string所以安全”。',
 '- **40保守记录继续保留**：39个上下文敏感Werehund／Werepup及1个source-only／manual-alignment，不因本轮PASS推成全局语义批准；按这些记录的姓名身份未生成op。36目标是独立审过的中文创译，不是作者官方释名。',
 '', '## 已调查差异', '',
 '- Java暂存源码发生Windows换行转换：正式RadioLabels 4572B／94 LF，staging4666B／94 CRLF；只对Java源进行EOL归一化后完全相等，并以独立编译class字节相等补强。**游戏数据EOL没有归一化放宽**，仍由原始preview精确字节保证。该差异已即时通知主控。',
 '- 原始预检对Java源使用全字节比较曾报FAIL；核明换行来源后修订这一断言。没有修改生产源或归档。初始低效只读归档枚举探针已取消，完整脚本单次打开归档完成核验。',
 '', '## 证据', '',
 '- '+link('结构化最终报告／root-relative输入SHA／changed_entries／逐项checks','localization/editorial/r3-names/review/final-review.json'),
 '- '+link('隔离归档与glyph/class核验脚本','localization/editorial/r3-names/review/final-isolated-08/verify.py'),
 '- '+link('最终核验日志','localization/editorial/r3-names/review/final-isolated-08/final.log'),
 '- '+link('最终17CPU结果','localization/optimization/r28/integration/tests/character-names-final8/results.json'),
 '- '+link('实际归档radio-labels日志','localization/optimization/r28/integration/tests/character-names-final8/logs/radio-labels.log'),
 '- '+link('冻结工程预检','localization/editorial/r3-names/review/engineering-01.json')+' 未覆盖、未改写。',
 '', '## 完整继承限制与未验证', '']
summary += ['- '+s for s in d['not_verified']]
summary += ['', '## 工程范围限制', '']+['- '+s for s in d['limits']]
summary += ['', '未安装／部署，未启动游戏／访问用户存档，未GPU或全图验收，未Git写／安装依赖／再委派。所有本轮实验只写review新子目录与两份final-review。', '']
(R/'final-review.md').write_text('\n'.join(summary),encoding='utf8')
print(json.dumps({'status':d['status'],'final_review_json_sha256':hashlib.sha256(p.read_bytes()).hexdigest(),'final_review_md_sha256':hashlib.sha256((R/'final-review.md').read_bytes()).hexdigest()}))
