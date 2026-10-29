"""Materialize the editorial naming decisions; no archive/game writes."""
from pathlib import Path
import json
ROOT=Path(__file__).resolve().parents[4];R3=ROOT/'localization/editorial/r3-names'
inv=json.loads((R3/'engineering/inventory.json').read_text('utf8'))
choices={
'Mauser':('毛鼠','保Mauser近音，以鼠保已证鼠身份；中文音义创译，不声称作者释名，军武联想只能部分保留。'),
'Tomcat':('雄猫','保tomcat词义及电台呼号感；角色相关成人双关仍由原对白承接，不改成色猫。'),
'Yiffai':('伊吠','与姐姐整组音义创译：伊保近音，吠取已证犬类发声层；不声称吠完整等于yiff成人义，不新增狐狼亚种。'),
'Yiffany':('伊吠妮','共享伊吠词根并以妮保女名形式，姓氏仍为伊吠；这是中文功能补偿而非作者构词定论。'),
'Bossu':('波苏','boss领导层可见，物种未证，不硬牛化或狗化；既有姓名自然，统一当前英文/中文写法。'),
'Macsen':('麦森','保近音和商人身份的姓名感；无可见姓名源时不新增露脸或把匿名商贩强命名。'),
'The0':('The0','保数字0的黑客代号样式；不纯音译西奥而丢0，不依据名字推神名或犬亚种。'),
'Gitgud':('季高','季高谐技高，中文编辑补偿原git gud游戏技能梗；不声称姓季是原作设定，无可见源不新增揭名。'),
'Starkill':('星杀','保受控代号及揭示时点，不以改名把后期真身份灌到前期。'),
'Yogo':('约戈','无可靠动物词义，保现有可呼叫姓名，不由熟悉犬科推本人犬科。'),
'Buntleen':('邦妮琳','Bun与原文明示BUNNY的联想转为邦妮加琳，保女性姓名形与兔趣，不定亚种。'),
'Kahr':('卡尔','保近音和可核同名军武层；不凭拟声推猫种。'),
'Komet':('彗珂','以已核Komet彗星义配Ko近音形成短名；不新增速度/战机/种族事实。'),
'Erma':('艾玛','用自然中文姓名近音，不以厄字强化灾厄含义；水獭身份不硬塞进名字。'),
'Daleir':('黛蕾','保主要音节与姓名感，统一标题达莱尔和正文黛蕾尔；不凭近形认定诱骗词源。'),
'Nambu':('南布','保自然近音与同名军武层，spotty不足硬定斑点犬。'),
'Vickers':('维克斯','保军武同名辨识和强势呼叫；狐狸/foxy梗在菜单，不把未证vixen拆词强译为薇狐。'),
'Cetartni':('塞塔特尼','异常拼写无可靠构词证据，不任意删音或猜倒写；保可追踪近音并统一正文英文。'),
'Gaoru':('高鲁','收束Gao/ru形成短人名；吼声只作听感，不据此定虎/犬种。'),
'Gepard':('猎豹','按已核德语名字义直译，可兼同名军武呼号；不在角色物种档案中由此推定猎豹亚种。'),
'Truvelo':('特鲁维洛','保近音/同名军武辨识，不凭姓名给已证鬣狗强加新词根。'),
'Vulcan':('伏尔甘','既有神名式音译保火与锻造文化层，不把名字当人物火能力。'),
'Henschel':('亨舍尔','保近音及同名军武层；不据Hen给猫角色强加母鸡名。'),
'Franchi':('弗兰基','保近音，不把战姿文化线索硬断血统，不添红熊字。'),
'Chauchat':('绍狞','绍保首音及传统绍沙影子；狞取原文明示caracal，补偿可核chat猫义；是中文创译非作者释名。'),
'Karbine':('卡宾','已有通行武器词义与姓名感，狐身份另由原位outfox双关承接。'),
'Pancor':('潘科','保可呼叫近音，不凭缺一手资料的同名线索另造兔科。'),
'Redbull':('红牛','原定称有透明动物词义，保留；不把其他饮料/普通红色牛也当同一个人。'),
'Enelye':('恩莉耶','自报个人名，统一恩内莉变体；无证不性俚语化，High Lady称号独立。'),
'Pigobin':('猪哥布林','保古老实体定称及pig/Gobin层，不推广到Gobin/Omegobin全族。'),
'Traeh':('Traeh','保TRAEH反写HEART信息，不直送中文心形谜底；只在源名出现处用，不用Queen先行揭名。'),
'Werehund':('狼犬','保特定父亲个体的现称谓，不造出生名、不全物种改名。'),
'Werepup':('狼崽','保特定幼子称谓，不把玩家成人往事主体并入幼崽。'),
'Sevaw':('Sevaw','已证个体名，保SEVAW反写WAVES信息；不是Dragon本身，不改谜题线索。'),
'Erauqs':('Erauqs','已证长老/母亲个体，保ERAUQS反写SQUARE信息；Elder称号独立。'),
'Jakov':('雅科夫','只将冠名人名作通行近音，不新增物种；Obscura等道具非人名部分不顺改。')}
assert set(choices)==set(inv['characters'])-{'Bigbold','Dragon'}
records=[]
for name,(target,reason) in choices.items():
 v=inv['characters'][name];forms=[x for x in v['known_current_variants'] if not (name=='Tomcat' and x=='汤姆')]
 record={'name_id':name,'source_forms':[name]+(['Yifany'] if name=='Yiffany' else []),
         'old_forms':forms,'target':target,'reason':reason,'action':'rename_or_standardize',
         'current_carriers':len(v['carriers']),'preserve_ascii_case':name=='The0',
         'radio_aliases':[name]+(['Yifany'] if name=='Yiffany' else []),
         'evidence':['localization/editorial/r3-names/research/'+('agents.json' if name in list(choices)[9:27] else 'bosses.json' if name in list(choices)[27:35] else 'core.json')],
         'nicknames':[]}
 if name=='Tomcat':record['nicknames']=[{'source_forms':['TOM','Tom'],'old_forms':['汤姆'],'target':'阿雄','reason':'仅原文TOM昵称位置保亲近，不添年龄/军阶。'}]
 if name=='Jakov':record['evidence']=['localization/editorial/r1/reference/world-and-plot.md#L355']
 records.append(record)
value={'schema':'r3.character-names.v1','status':'proposed_for_independent_review','baseline':'localization/builds/r28-editorial-repairs-candidate6',
       'names':records,'family':{'surname':'Yiffai','male_given':'Yiffai','female_given':'Yiffany','preserve_repeated_full_name':True},
       'excluded':['Bigbold/Dragon等通用物种和无名Boss','仅Queen/High Lady头衔的出现','RATS/ELGNAIRT/ELCRIC/SSORC仅证档案标题，不改其既有显示','制作人员/赞助名单','actor/JSON key/控制/动态@占位符'],
       'notes':['人物物种证据与名字字面义译分开','新增名字不虚构新剧情或在无可见源处新增出现','全部来源与旧名变体以candidate6实际载体为准']}
out=R3/'decisions/names-proposed.json'
if out.exists():raise ValueError('New registry only')
out.parent.mkdir(parents=True,exist_ok=True);out.write_text(json.dumps(value,ensure_ascii=False,indent=2)+'\n',encoding='utf8')
print('Recorded',len(records),'character naming decisions')
