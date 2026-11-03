"""Write the r9 batch-10-part01 decision table.

Only the DS route reported for this batch: the Gemini route failed five times on
batch-10 (no output, no closing message), so this part lands single-route with
the main agent's mechanical passes standing in for the second reader. The
trailing-space family comes from `tools/r9_decisions.py`, the rest from the
verified findings below.
"""
from pathlib import Path
import sys

sys.path.insert(0, str(Path(__file__).resolve().parent))
from r9_decisions import Batch

# Centred layout blocks: their padding is a device, not a defect.
SKIP = ('ui.end', 'ui.backers', 'ui.options')

b = Batch('batch-10-part01')

# Verified findings (route, id, reason[, final override]).
b.apply_finding('ds', 'P10-0102',
                '同一张繁殖卡的收尾句在库内 16 处作「真是棒极了的宠物！」，本行是其中 2 处之一；统一收尾句不增信息。')
b.apply_finding('ds', 'P10-0103',
                '现译把「分了神！」拆成「分了」「神」「！」三段，卡面会出现两个一字宽的残行加一个独立感叹号；'
                '本行按原文 14 段重排，末段复原为「分了神！」，同时去掉没有来源的行尾空格。',
                '红牛虽懂得遮羞，|却认为|让旁人|（包括闯入者）|大方地|看见自己|整根硕大的|家伙，|其实是|表达|尊重。|可别|因此|分了神！')
b.apply_finding('ds', 'P10-0104',
                '同一英文资料卡女线作「汪！一场大胜|换来更惨的败仗！」，男线把拟声词当定语（「一场汪汪大胜」）读不通；'
                '统一到女线写法，DEFEAT 在决斗卡里指一场败仗。')
b.apply_finding('ds', 'P10-0105', '「初出任务」不成词（现代汉语只在「初出茅庐」里成立）；补「次」字对应 on his first mission。')
b.apply_finding('ds', 'P10-0106',
                '同一按键配置屏其余 14 行全为中文，nsfw 侧与 `input.xinput` 都把 SELECT 作「选择」；只 jar 侧留英文是分叉。')
b.apply_finding('ds', 'P10-0107', '同 P10-0106 同一屏同一判点：nsfw 侧与 `input.gdx2.std` 都把 START 作「开始」。')

# Left alone on purpose: the NSFW data cards still read BIGBOLD1／BIGBOLD2 while
# the SFW side says 大壮兽1／大壮兽2. The repair engine counts `BIGBOLD1` as a
# marker token, so renaming it is refused as marker drift — the same guard that
# stops gameplay IDs from being translated. Recorded in LEFTOVERS.md instead.

# Rejected.
b.reject('ds:P10-0101',
         '该行首行行首的 2 个空格与第二段行内的 9 个空格是同一套手工居中补白（原文也靠空格对齐，不是自动居中）；'
         '只删行首补白会让两行一左一右，在没有渲染证据的情况下不删。')

b.emit_trailing_space(skip_roots=SKIP,
                      reason='中文行尾（JSON 值末的换行之前）多出空格，英文原文行尾没有；只删空格，不动换行。')

print(b.close())
