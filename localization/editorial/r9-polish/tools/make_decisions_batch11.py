"""Write the r9 batch-11 decision table (single-route: DS only).

The Gemini route failed on this batch too, so coverage is DS plus the main
agent's trailing-space pass.

Defeat hints are gameplay instructions: every applied change keeps the advice,
the target and the causal order, and only fixes wording or a term that the same
batch renders differently elsewhere. The Starkill kinship lines are mirrored on
purpose (`datadm` is the older sister, `datadf` the younger brother), so the
datadm row says 姐姐 while its twin already says 弟弟 — that is the point, not an
inconsistency.
"""
from pathlib import Path
import sys

sys.path.insert(0, str(Path(__file__).resolve().parent))
from r9_decisions import Batch

b = Batch('batch-11')

b.apply_finding('ds', 'P11-D001', '「那只代表你自己」是 speak for yourself 的字面直搬，「那只」还会被读成指动物；改成口语的反驳。')
b.apply_finding('ds', 'P11-D002', '同一批的说明行都把 BIGBOLD 作「大壮兽」（本批另有 4 处），只有这行留英文 BOLD。')
b.apply_finding('ds', 'P11-D004',
                '`datadm` 侧是姐、`datadf` 侧是弟弟，两侧称谓镜像；兄弟侧已作「让你弟弟见识见识」，姐侧不能写成「手足」。')
b.apply_finding('ds', 'P11-D005', '「我本来会…先囤好食物」把虚拟语气与语序都直搬；改后仍是同一条战前建议。')
b.apply_finding('ds', 'P11-D006', 'agent 在库内 471 处作「特工」，「干员」是少数写法；同批 D010 同理。')
b.apply_finding('ds', 'P11-D007', '「缺少一身老练的战斗功夫」量词与搭配都不通；英文源行尾有空格，译文的行尾空格照留。')
b.apply_finding('ds', 'P11-D008', 'werepup 在库内作「狼崽」；「小狗」与同批的「小狼崽」自相矛盾。')
b.apply_finding('ds', 'P11-D009', '「训练所学」是生造搭配；改后仍指同一件事（练过的本事）。')
b.apply_finding('ds', 'P11-D010', '同 P11-D006：agent 统一作「特工」。')
b.apply_finding('ds', 'P11-D011', '失真广播里点名的是游戏自己的名字，库内一律作「伊吠」（Yiffai），「伊法」是错字。')

b.reject('ds:P11-D003',
         '与主代理的行尾空格条目是同一行同一点（英文源行尾没有空格，中文多一个）；'
         '取机械条目，避免同一行两条决定。')

b.emit_trailing_space(reason='中文行尾多出半角空格，英文原文行尾没有；只删空格，不动前缀与行尾。')

print(b.close())
