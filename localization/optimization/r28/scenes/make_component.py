"""Refresh scene-only integration manifest and 61-consumer decision ledger."""
from pathlib import Path
import hashlib,json,re
ROOT=Path(__file__).resolve().parents[4];HERE=Path(__file__).resolve().parent
runtime=['localization/layout/src/PRG/SceneText.java','localization/layout/src/PRG/EndingReportLayout.java']
tools=['localization/layout/tools/java/SceneTextPatch.java']
tests=['localization/layout/tests/SceneTextTest.java','localization/layout/tests/EndingReportLayoutTest.java']
patch=(ROOT/tools[0]).read_text('utf8')
pins=dict(re.findall(r'raw.put\("([^"]+)","([a-f0-9]{64})"\)',patch))
helpers=sorted(p.relative_to(HERE/'run010/runtime').as_posix() for p in (HERE/'run010/runtime').rglob('*.class'))
manifest={
 'component':'r28-scenes','integration_base':'localization/builds/r27-story12-shaderfix-test5/cosmobreeder-multi.jar',
 'runtime':runtime,'tools':tools,'tests':tests,'helper_classes':helpers,
 'target_pins':{k+'.class':v for k,v in pins.items()},
 'patcher_class':'SceneTextPatch','patcher_entry':'public static void apply(Map<String,ClassNode>)',
 'patch_order':'Raw-SHA check all six entries; ClassReader.EXPAND_FRAMES; apply while these targets are pristine r27; do NOT reapply old EndingReportPatch. Other disjoint patchers may run before/after.',
 'pin_contract':'Driver must enforce target_pins on raw class bytes. apply additionally enforces complete canonical ASM17 class-tree SHA and exact method descriptors/callsite ordinal counts, atomically before mutation.',
 'resource_requirements':{'new_resources':[],'font_roles':['default','classic'],'requirements':['Existing default10 and classic8 glyph metrics/pixels preserved; only append missing glyphs.','classic printable ASCII must retain original Yq fixed-width setup (8px advance).','Retain original 1px transparent Latin glyph quad padding.','FontAccess/LayoutBridge and PixelLayout public APIs already in r27; do not globally patch It/Yg centering.']},
 'candidate_cpu_tests':[
  {'main':'EndingReportLayoutTest','arguments':['{fontdir}/classic.fnt','{sfw-dictionary.json}']},
  {'main':'EndingReportLayoutTest','arguments':['{fontdir}/classic.fnt','{nsfw-dictionary.json}']},
  {'main':'SceneTextTest','arguments':['--candidate','{candidate.jar}','{fontdir}','{sfw-dictionary.json}','{nsfw-dictionary.json}'],'vm_extra':['-Dscenes.report={new-output}/breeding-corpus.json']}
 ],
 'test_classpath_order':['{testclasses}','{candidate.jar}','{toolclasses}'],
 'vm_flags':['-Dfile.encoding=UTF-8','-Xverify:all','--add-exports','java.base/jdk.internal.org.objectweb.asm=ALL-UNNAMED','--add-exports','java.base/jdk.internal.org.objectweb.asm.tree=ALL-UNNAMED'],
 'fontdir_files':['bbc2.fnt','classic.fnt'],'font_pin_staging':['PRG/EndingReportLayout.FONT_SHA256 must match candidate classic.fnt (original pixels/metrics plus appended glyphs).'],
 'frozen_r27_evidence':'localization/optimization/r28/scenes/run010/results.json',
 'source_sha256':{p:hashlib.sha256((ROOT/p).read_bytes()).hexdigest() for p in runtime+tools+tests},
 'unknown':['No complete UI parent/FBO/clip/CRT/GPU execution.','No real keyboard/controller/input traversal.','No arbitrary user text or unknown overheight content viewing strategy; capacity failures refuse rather than truncate.','Full Jm front/back/flip scene and kn SA Reverse/AlBhed transformations not replayed.']}
(HERE/'component.json').write_text(json.dumps(manifest,ensure_ascii=False,indent=2)+'\n',encoding='utf8')
base=json.loads((ROOT/'docs/font-layout-audit-20261025/consumer-coverage.json').read_text('utf8'))
reasons={}
def assign(names,reason):
 for name in names.split():reasons['PRG/'+name]=reason
assign('ET Ie IV','保留：HUD数值/拾取串/固定状态列需逐字段矩形；未改动全局步进，真实全状态未知。')
assign('Eu Ev Ez','保留：繁育相邻消费者不等同Ew描述槽；图标/状态列和各自输入几何未证，不盲套224px。')
assign('IB Ml Zl aak','保留：通用helper由具体调用者传字体/矩形；未使用全局String.length或全局字号替换。')
assign('II','保留：航运两列和选中图标需独立窄栏预算，本轮不套全屏居中。')
assign('IO IR','保留：标题/暂停按钮含位图与动态文本，未改变闪烁/动作/命中范围；完整验收未知。')
assign('Id Yg Yq arp arq arr iF jl','保留：共享字体/渲染基础设施；场景局部调用已有接管，不全局改8格或居中，其他调用者未知。')
assign('Ix','保留：错误提示最小诊断后备，不能依赖新字体初始化成功；长错误信息未知。')
assign('JM','保留：主菜单独立消费路径；本轮没有该字段矩形/状态闭环，不宣称被场景helper覆盖。')
assign('JQ','保留：无线电正文由上游JR/core工作处理；说话者标签不是本轮profile。')
assign('Jq Jt Jv','保留：作弊/旋钮的四参format和逐字底板未改；必须联动输入格/警告列，不能为布局改变选项语义。')
assign('Jw KW KX','保留：独立奖励/数值/动画路径，不凭排版推断交易或奖励值域；动态字段几何未知。')
assign('Kk','保留：Continue属于另一工作范围，原输入/事件不在SceneText中接管。')
assign('LC LE','保留：设备名/键位图案与双列输入映射未改，不改变绑定语义；完整长设备名路径未知。')
assign('LG LJ LK LL$a LL$b LV','保留：选项/确认窄栏/双列/面包屑各有独立矩形；没有证据支持统一240px或全局替换。')
assign('LX LY Mb Mc Mn','保留：紧凑姓名/存档由独立工作范围处理，本轮不改存储、名字内容或槽位。')
assign('Lb Lg','保留：现有道具ItemFont8已局部接管；用户明确排除修改该helper，本轮不冒称全道具菜单通过。')
assign('Lh','保留：道具类别/邻接标签独立于已登记Lg说明；安全宽度和完整状态未知。')
assign('Lq Lr','保留：任务日志滚动/列表与详情字体传递未闭环，不以修复四参格式器替代完整查看路径。')
assign('ME MN','保留：商店动作/价格/货币字段未改；正文上游适配不代表交易控件覆盖。')
assign('Na jo','保留：剧情/字幕由其他工作范围处理，不修改StoryFont12/SubtitleLayout或语言解码语义。')
fixed={
 'PRG/Ew':'已修指定affinity/needs全文源头和完整绘制；含中文needs默认10/12行距，原显式3行affinity必要classic8；原图标/FOUND/姓名/交互未改。',
 'PRG/Jm':'已修两处卡牌四参format+右侧行/标题，128px/8px行距用classic8，原normalization/统计/翻卡/选择语义保留；完整父clip与前后动画未验。',
 'PRG/kn':'已修30列×2完整format及两处实际glyph居中；原标题位图/动画/时长/SA变换链不变；全文超两行拒绝，Reverse/AlBhed未验。',
 'PRG/Lx':'已修唯一底栏居中调用，使用实际绘制role的arr度量，未改全局Yg/It；地图左/右竖排/图例/图标未改。',
 'PRG/Po':'已修唯一传送目标地名居中调用；固定标题/MISSION/PAWSED及状态输入完全保留。',
 'PRG/Kc':'已修r27完整说明source local9之后的format/zip截尾；$不再侵占第28可绘列，双pass/颜色/偏移保持；标题/列表/输入未改。',
 'PRG/Kr':'沿用r27整行classic8结算接管，helper重新编译；真实Ks/Kr两档60字段与动态值/颜色/闪烁通过，不冒称全结局演出通过。'}
records=[]
for row in base['records']:
 c=row['class'];records.append({'class':c,'decision':'partial_fixed' if c in fixed else 'retained_not_covered','reason':fixed.get(c,reasons.get(c,'保留：非本轮独占范围；该具体消费者矩形、输入及全文查看路径仍未知，未宣称覆盖。')),'source_snapshot':row['snapshot'],'runtime_parent_clip':'not_verified','whole_class_or_scene_coverage':False})
(HERE/'consumer-status.json').write_text(json.dumps({'scope':'One decision per original direct consumer; NOT a coverage percentage or per-class runtime coverage claim.','records':records},ensure_ascii=False,indent=2)+'\n',encoding='utf8')
print('Wrote scene component and',len(records),'individual consumer decisions')
