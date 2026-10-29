import json, hashlib, re
from pathlib import Path
BASE=Path('localization/editorial/r1')
IP=BASE/'corpus/snapshot-01/packets/packet-06.reader.md'
JP=IP.with_name('packet-06.json')
OUT=BASE/'audit/packet-06'
scenes=json.loads(JP.read_text(encoding='utf-8'))
byrow={r['review_row_id']:(s,r) for s in scenes for r in s['rows']}
lines=IP.read_text(encoding='utf-8').splitlines()
def ids(a,b):
 return [re.match(r'ROW (\S+) ',l)[1] for l in lines[a-1:b] if l.startswith('ROW ')]
findings=[]
def add(a,b,sev,cat,zh,reason,refs=None,status='proposal'):
 rr=ids(a,b); s=byrow[rr[0]][0]; rows=[byrow[x][1] for x in rr]
 assert all(byrow[x][0]['scene_id']==s['scene_id'] for x in rr)
 findings.append(dict(finding_id=f'P06-{len(findings)+1:03}',scene_id=s['scene_id'],row_ids=rr,severity=sev,category=cat,source_quote='\n'.join(r['source'] for r in rows),current_quote='\n'.join(r.get('current_line') or '' for r in rows),proposed_zh=zh,reason=reason,evidence_refs=[s['logical_path']+'#'+s['root']]+[r.get('location','') for r in rows]+[r['unit_id'] for r in rows if r.get('unit_id')],reference_keys=refs or [],status=status,apply_scope='scene_draft_only',branch={'mode':s['mode'],'logical_path':s['logical_path'],'root':s['root'],'controls':s.get('controls',[])},alias_scope='仅本场景；别名来源保持原映射，不扩展到内容或控制不同的场景'))
add(285,287,'B','voice','这把精灵拆信刀可真精巧，我可没夸口！轻得像羽毛，跟穿上精灵做的裙子一样轻飘飘的……当然，那些裙子我可不懂！','当前“就像……会让你感觉的那样”照搬从句，末句僵硬否认也削弱说漏嘴后的掩饰；重写整段保留轻盈比较和嘴硬，不认定商人的实际穿衣经历。',['characters-support:Macsen'])
add(331,336,'B','gameplay','一定要多关爱宠物，也别饿着它们！把任意一只宠物的亲密度提升到最高，再回来领特别奖励。\n有了这块水晶，喜欢你的生物就能给你特殊加成！在亲密度满了以后摸摸它们，就能给水晶充能。每种生物赋予的力量都不一样，都试试吧！','MAXXXED与MAX属于可译的程度，不是按键或资源ID；“一项亲密度”未把对象说清。建议分支分别使用对应短段，不把前后两个条件合成同次对话。',['world:I05'])
add(367,371,'B','idiom','伊法妮：[波苏，是这里的炮变强了，还是我变弱了？]\n波苏：[这些炮似乎已经有一阵子不用自我修复了，所以开火的威力也更大。]\n伊法妮：[太——好了，还嫌麻烦不够多是吧……]','首问there疑为their源拼写异常，但中文可据后续these还原此处炮台比较；末句just what I needed是反讽抱怨，当前“正好是我需要应付的”落点生硬。建议保留seem，不加具体修复耗能机理。',['world:D01'])
add(491,491,'B','source_uncertainty',None,'源句MAUSER ORDERS IN... WHAT?本身突兀且speaker为Yiffany，可能是故意复述/听错，也可能源异常；当前简化为再次呼叫丢失orders字面内容。需对照原JAR演出或音讯语境再定，不能凭NSFW对应场景删除本行。',status='needs_evidence')
add(513,519,'B','continuity','伊法妮：[什么异常？]\n毛瑟：[这个，不是想吓你……不过……]\n波苏：[这片区域似乎还有一名特工，而且一直在四处活动。行动完全不受限制。]\n伊法妮：[另一名特工……]\n毛瑟：[我们还在试着呼叫对方，可是……嗯……现在看起来，对方的无线电已经关了。]','单一未知agent被反复译“他们”，且“自由地”孤立作补语不自然；核心是其他探员被捕时这位却能自由行动。改“对方”避免提前确定身份、性别和关机主体；末句也可保守译“对方的无线电已经关了”。',['characters-primary:揭示门槛'])
add(665,665,'B','idiom','[不客气，祝你们的卡片约会愉快！嘻嘻！]','Anytime回应同事“谢你牵线”，不是承诺自己随时参与约会；“随时奉陪”把应答转成自身参加，打乱两人被凑对的笑点。',['characters-primary:Yiffany'])
add(682,682,'B','idiom','[不客气，祝你们的卡片约会愉快！嘻嘻！]','SFW独立场景中同样是在回应牵线致谢；保留本版未含成人卡背说明的结构，不与NSFW通话合并。',['characters-primary:Yiffany'])
add(687,690,'A','term','[那姑娘不会又被几个狗头人打倒，把无线电弄丢了吧……又来一次……]\n[……？！]\n[说真的，希望她醒来后还能把它找回来。]','当前“收音机”把可双向联络的任务radio说成单向收音设备；此处Tomcat误以为Kobo捡走通讯器。保留误认，不将台词改成已认出主角。',['characters-support:Tomcat'])
add(775,777,'A','source_uncertainty',None,'本行源文them可指keycards或doors，字面“门上所标等级以内的门”成为自指，当前照译后无法说明门卡权限。本包同女线SpecialKeycard1已说明门终端是最低需求且高卡兼开低门。须核4级卡实际触发/显示对象，若them指卡建议“拿着门卡走进能量门就能开门；门的等级不超过门卡等级就行。”不能在本轮直接覆写源歧义。',['world:I04'],status='needs_evidence')
add(815,816,'B','term','[嗯，这把东西在这个象限的任何星系都过不了规格检验。不过应急倒是能用。]','system为星系/辖属地域而非电脑系统，pass spec是符合规格；“任何系统里过不了规格”失去科技装备说明的自然表达。保留口语评估，不额外宣称具体违法条款。',['characters-support:Tomcat'])
add(859,860,'A','term','要是在外头找到无线电，记住：在物品菜单里按SELECT，就能用它联络！','有SELECT使用提示且进入通讯系统，当前“收音机”错误限定为广播接收机；SELECT保留，不改按键。',['world:I10'])
add(1047,1055,'B','voice','伊法伊：[喂、喂！我只是一时没掌握好力道！]\n波苏：[别一打上头就忘了正事。下次遇到生物，优先采集数据。]\n伊法伊：[明白，波苏！不会让你失望的。]\n波苏：[好小子，等着看你的数据！再碰到新生物，就用27.850呼叫我。还有，别忘了把新装备装上。完毕！]\n伊法伊：[知道啦，我又不是小狗崽……]','H-HEY是急辩口吃，不是“嘿嘿”笑声；heat of moment是上头冲动，不是“热劲卷住”；末尾Pup未译使嘴硬回应失去落点。全段建议保持各人和频率节点，不按段落平均回填。',['characters-primary:Yiffai','characters-support:Bossu'])
add(1112,1117,'A','meaning','波苏：[斯凯菲亚的精灵虽说全是女性，却并不个个长生不老。她们能与任何物种的雄性繁衍，因此逐渐带上了更多凡俗生物的特征。]\n伊法伊：[等等，也就是说，她们之中真有长生不老的？]\n波苏：[没错，至少我们目前掌握的资料是这样。]','may all be female在may...but结构作让步，不是独立不确定“也许全是雌性”；当前把让步误作概率。“有朽特征”“所能看出的而言”不自然。结论仍归Bossu资料，不宣称世界全知真理。',['world:D04'])
add(1121,1123,'B','idiom','波苏：[别光顾着惊叹。打起精神，才能挡住那些年轻精灵的攻击。]\n伊法伊：[对，得专心。]','give in to awe在此是制止看呆、提醒战斗，当前“别向敬畏屈服”语域与上下句不接。保留警觉与防御目的，不增加侮辱或敌意。',['characters-support:Bossu'])
add(1162,1163,'A','voice','[糟了，你的生命值掉下去了。你还能站起来吗？]','关切伤情、询问是否能起身，被译“你以为你还能站起来吗”成威胁或嘲讽；同场后续Bossu提供战术提示，明确是支援语境。',['characters-support:Tomcat'])
add(1205,1207,'B','voice','[外头不少食物都能帮你回点血，有些还能提升属性！要是有哪只野兽打不过，就多备点吃的。]','“治疗你一点”是英语宾语结构硬搬；教程需自然说明恢复与备粮，不把吃不消扩大为强制购买。',['characters-support:Gitgud'])
add(1211,1214,'B','voice','你好，伊法伊。你不认识我，不过我偷偷接入了你的卫星链路。其实我已经留意你一阵子了，想跟你谈笔交易……\n很简单：把你在外头找到的那些高级芯片带给我，我就替你破解门锁！这不是双赢嘛！','“有点偷看了”逐词追随kinda，中文搭配不成立；snoop satlink对应私自接入/窥探通讯，不是目视查看链路。按共享黑客身份范围，不扩认所有测试黑客为The0。',['characters-support:The0'])
add(1473,1473,'A','meaning','[我碰到一个发光的球体，它在我身上留下了个印记。]','glowing明确可观察特征，当前丢失“发光”；该特征承接识别古代科技的后文，不宜删。',['world:I06'])
add(1721,1721,'B','idiom','挥爪轻轻打着呼噜，|你一走近，便乖乖|收起了那双利爪。','murder mittens是对猫爪的幽默称法，sheathe为收爪；当前“收起凶器肉垫”像把肉垫收进身体。保留礼貌地收敛威胁的亲密度变化，不把整组状态合成一次动作。')
add(1733,1733,'B','term',None,'本包同名Enelye在男线裙子通话为“恩内莉”，卡名及卡文为“恩莉耶”，女线失败C末尾又“恩内莉”。是同一原名的可追踪不一致，但本轮参照未终裁正式译名；请统一专名裁决后按身份与语境处理，暂不强选一个新译名。',['world:W14'],status='needs_evidence')
add(1838,1838,'A','meaning','旧杂货','该键明确位于shops/female/Area0_Macsen1/products/2/displayName，是商品名称；“旧货铺”把商品译成店铺。建议仅在商品字段写“旧杂货/旧货”，不改变店名或资源键。')
add(1942,1948,'B','voice','……这名旅者终于失守，抵挡不住那股黑暗灵能。力量与痛苦席卷全身，直到连心智也不再由自己掌控。\n不，从那一刻起，这名旅者便听命于更黑暗的力量……特蕾让做什么，就做什么！','“其便”重复书面代词和“力量奔涌过”影响讲述连贯性。建议保留Fox历史讲述、触碰后失去自主的因果；不替前段好奇/操控动机终裁。每个cut前后段分别用，不跨演出合并。',['world:H06'])
add(2119,2120,'B','idiom','不得不说，他们真有一套。在跟我做过的攻里，绝对能排进前三。那些倒刺来回刮蹭，力道恰——到好处……嗯唔！','top three tops为前三名性伴/攻方双关，当前“前三个上位”不是自然的性角色称呼且像体位排行。维持兔子回忆中的自述评价，不更改此前被制服的事实。',['world:R07'])
add(2228,2230,'B','voice','汪！汪！万岁！\n汪！汪！万岁！\n赞颂宇宙育种者，我们星球的救星！','Yip呼应犬类欢呼并仿hip hip hooray，当前残留YIP和“愿……受颂”不自然。建议保留两次重复和庆典语气，不当角色常态犬吠口癖。',['world:E02'])
add(2240,2241,'B','voice','干得漂亮，姑娘！你和你那小狗崽弟弟，可把下面的坏蛋收拾了个干净！\n等你们出了名，可别得意得忘了我们这些总部同事啊，好吗？','grrrrl为拉长girl，不是受保护词；结局祝贺中原样留英文破坏同事口吻。只按本句译姑娘，不全局固定妞/喵。',['characters-support:Tomcat'])
add(2258,2258,'B','format','[PPP以有这两位特工为荣。]                      ——署名：波苏','-SIGNED, BOSSU是报告署名而非控制命令，当前未译破坏中文报告收尾；名字沿本包既有暂译，仅为提案不裁最终专名。',['world:W06'])
add(2330,2330,'B','voice','[我的太空神啊，你开什么玩笑！]','当前凭空添“他妈”，原句夸张但无对应粗口；此处保留高声惊呼与荒诞信仰套语即可，不把Yiffai统一升级粗俗程度。',['characters-primary:Yiffai'])
add(2350,2353,'B','continuity','[伊法伊特工想必会很欣慰，自己也为这些发现出了份力。]\n[遗憾的是，我们在触手坑里找到他时，他已经无力体会别的了——只能充当活体电池，靠无休止的性快感获得安抚。]','当前“状态已无法，”“除了……外，对别的”拼接断裂，安抚又重复。整段须保留前句冷幽默与后句残酷反差；不是宣称他已恢复、也不替PPP后文的恢复希望打包票。控制cut不跨越回填。',['world:E04'])

OUT.mkdir(parents=True,exist_ok=True)
(OUT/'findings.jsonl').write_text(''.join(json.dumps(x,ensure_ascii=False)+'\n' for x in findings),encoding='utf-8')
coverage=[]
for s in scenes:
 rr=list(dict.fromkeys([r['review_row_id'] for r in s['rows']]+[r['review_row_id'] for a in s.get('aliases',[]) for r in a['rows']]))
 ff=[f for f in findings if f['scene_id']==s['scene_id']]
 kind=s['kind']; root=s['root']; rows=s['rows']
 if kind in ('code','image'):
  result='inventory_only'; note='代码常量仅逐项登记，未证实玩家可见用途，不把空中文判漏译、不翻资源键或错误常量。' if kind=='code' else '只读图像转录的两条菜单文字；未看图、未OCR核对、未做图像本地化质量验收。'
 elif ff:
  result='issues_found' if any(f['status']=='proposal' for f in ff) else 'needs_evidence';note='完整英文与控制边后连读当前中文；具体段落问题与分支边界见关联提案。其余句子保留，不把已合句空尾行列为漏译。'
 elif kind=='vsn':
  result='retain';note='已按完整脚本先英文/演出、后连读中文：本场叙述的行动、先后、否定及信息落点相符；保留角色自述/不可靠认知，不因narrator元数据推定全知旁白。'
 elif kind=='ui':
  result='retain';note='名称、说明或状态文本与本项英文含义相符，数字、按键、占位/分栏符保留；通顺译法不额外凑润色。'
  if any(r.get('current_kind')=='nested_json_value_runtime_usage_check' for r in rows):
   result='inventory_only';note='嵌套JSON文本已逐项对读，当前含义可保留；任务占位/运行时用途未验证，不冒称玩家实显。'
 else:
  result='retain'
  if 'Hints' in root or 'Dex' in root or 'Items' in root or 'Tip' in root: note='本场问答/说明连读成立，操作对象、方向、否定和已有推测限定保留；合句尾行按整段计义，不另列漏译。'
  elif any(x in root for x in ('Dog','Kobo','Feral','Slime','GenderSwapped')): note='已区分当前形态与常态身份；对方的误认/逗狗话术和本场行动相符，不当作主角实际履历或身份变化终裁。'
  elif any(x in root for x in ('SoldOut','Purchase','Purchased','Money','Inventory','Goodbye','Hello')): note='本场招呼、交易反馈或告别语义/对象清楚，语气成立；不据星号元数据追加实际发言者姓名。'
  else: note='本场连续原文与当前中文相承，调侃、自述和提示对象保留；未把合法口语变体报成错误，也不跨版本合并经历。'
 excerpt=' / '.join(r['source'] for r in rows)[:160]
 coverage.append(dict(scene_id=s['scene_id'],read_status='read_full',row_ids=rr,context_checked=True,findings=[f['finding_id'] for f in ff],result=result,notes=note,scene_anchor={'mode':s['mode'],'kind':kind,'logical_path':s['logical_path'],'root':root},reviewed_source_anchor=excerpt,alias_scene_ids=[a['scene_id'] for a in s.get('aliases',[])],scope='文本与所给控制边静态审读；非实机'))
(OUT/'coverage.jsonl').write_text(''.join(json.dumps(x,ensure_ascii=False)+'\n' for x in coverage),encoding='utf-8')
refs=['LOCALIZATION_BRIEF.md','WORK_ORDERS.md','reference/characters-primary.md','reference/characters-support.md','reference/world-and-plot.md']
log=dict(packet='packet-06',input_path=str(IP).replace('\\','/'),input_sha256=hashlib.sha256(IP.read_bytes()).hexdigest(),packet_json_path=str(JP).replace('\\','/'),packet_json_sha256=hashlib.sha256(JP.read_bytes()).hexdigest(),read_status='read_full',read_ranges=[[a,min(a+99,2361)] for a in range(1,2362,100)],truncated_ranges=[],reader_line_count=2361,reading_method='24次read，每次limit100，实际顺次读完；先理解完整英文与控制边再回连当前中文，不以搜索/脚本扫描代替。JSON仅用于稳定ID、别名和证据摘录/覆盖构造。',references_read=[dict(path=str(BASE/r).replace('\\','/'),sha256=hashlib.sha256((BASE/r).read_bytes()).hexdigest()) for r in refs],reference_notes='primary首读输出裁剪于277，已补278–377；world首次不存在，落盘后完整补读1–150、151–300、301–406。',scene_count=len(scenes),row_count=sum(len(s['rows']) for s in scenes),coverage_row_count=sum(len(c['row_ids']) for c in coverage),findings_count=len(findings),uncovered='无reader缺口；code用途、图像画面、JSON运行时用途、游戏加载/触发及视觉排版均未验证。',status_boundary='仅proposal/needs_evidence；未正式应用，未approved，未部署，未Git写。')
(OUT/'reading-log.json').write_text(json.dumps(log,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
from collections import Counter
stats=Counter(f['severity'] for f in findings);statuses=Counter(f['status'] for f in findings);results=Counter(c['result'] for c in coverage)
summary=f'''# packet-06 首轮粗校提案\n\n仅文档/提案，未回写正式译文、catalog、资源或游戏；未 approved/部署/Git写。\n\n## 实际覆盖\n\n- reader 2361行，逐100行24次read完整通读，无裁剪；297个场景、1316条主rows。覆盖每场全部主row及alias row（去重后写收据）。\n- 先理解完整英文、条件与演出，再连读candidate4中文；旧ledger仅溯源，已合句空行未列漏译。\n- {len(findings)}条发现：{dict(stats)}；状态 {dict(statuses)}。覆盖结果 {dict(results)}。等级与待核状态独立。\n- code仅常量用途inventory；图像仅转录inventory；嵌套JSON除明确商品字段错误外仍保留用途未验证。未看图、未运行游戏、未验证版面。\n\n## 高风险连续段\n\n1. 男主初战通讯：急辩口吃被写成笑声、heat of moment直译、Pup残留；用整段重写恢复“显摆—提醒—急辩—服从—嘴硬”。\n2. 男线Werehund失败提示：关切问句变讥讽。失败A报告末尾句法断裂，需保留编辑冷幽默与恢复希望的限定。\n3. 女线炮台与轻盈裙比较：反讽、说漏嘴后的掩饰需用自然中文重建。\n4. 新手黑客交易、Gitgud食物提示与宠物亲密度：中文搭配/程度词残留影响玩法说明。\n5. 通讯器多处“收音机”、商品OLD JUNK译成店铺；均只按所列场景提案，不自动替换全库。\n\n## 待核而非强改\n\n- SFW女线Mauser.AreaB_map29_a中的MAUSER ORDERS IN... WHAT?源语异常。\n- SpecialKeycard4的them指代/等级说明源文歧义，须核实际卡/门显示对象。\n- Enelye的“恩内莉/恩莉耶”须统一专名裁决；本轮不另定正式译名。\n\n## 新增证据与保留\n\n- world最终稿已补读全406行；保留Pigobin自身古语（源thou/thine支持），不将其古风扩散到科幻通讯。\n- Fenfen Z5/Z6为Fox讲述/历史记忆，动机未知与未来宿主可能性均不升级事实。narrator不是实际发言者判定。\n- 男女主、SFW/NSFW、形态条件分别审读；结局与失败不拼成必经剧情。哨子亲属方向当前成立，保留。\n- 兄姐弟关系、全名、通讯频率、按键、数值和符号保留；大量通顺商品招呼与口语变体保留，不为数量凑问题。\n\n## 后续\n\n优先独立复审上述问答/失败报告/玩法范围；再形成实际节点写入映射与dry-run。本次完整段建议不能按行数平均切回脚本，不跨控制事件/发话者合句。\n'''
(OUT/'summary.md').write_text(summary,encoding='utf-8')
assert len(coverage)==len(scenes) and len({x['scene_id'] for x in coverage})==len(scenes)
assert all(set(r['review_row_id'] for r in s['rows'])<=set(c['row_ids']) for s,c in zip(scenes,coverage))
assert all(f['status'] in ('proposal','needs_evidence') for f in findings)
print(json.dumps({'scenes':len(scenes),'main_rows':log['row_count'],'coverage_rows':log['coverage_row_count'],'findings':len(findings),'severity':dict(stats),'statuses':dict(statuses),'coverage_results':dict(results)},ensure_ascii=True))
