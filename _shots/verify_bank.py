# -*- coding: utf-8 -*-
import io, re
from collections import Counter
src = u"C:\\Users\\96236\\Doubao\\chats\\2026-09-30\\new-chat\\mood-check\\心境自查.html"
out = u"C:\\Users\\96236\\Doubao\\chats\\2026-09-30\\new-chat\\mood-check\\_shots\\verify_result.txt"
html = io.open(src, encoding='utf-8').read()
bank_block = html.split('var BANK = [')[1].split('];')[0]
items = re.findall(r"\{id:(\d+),dim:'(\w+)',text:'(.*?)',rev:(true|false)\}", bank_block)
lines = []
lines.append("total questions: %d" % len(items))
ids = [int(i[0]) for i in items]
lines.append("ids unique: %s | min: %d max: %d" % (len(set(ids)) == len(ids), min(ids), max(ids)))
c = Counter(i[1] for i in items)
lines.append("per dim: %s" % dict(c))
for tier, q in [(10, [2,1,2,1,2,2]), (20, [4,3,4,3,3,3]), (50, [9,8,9,8,8,8]), (80, [14,13,14,13,13,13])]:
    ok = all(need <= c[d] for need, d in zip(q, ['emotion','sleep','stress','social','self','life']))
    lines.append("tier %d quota sum=%d bank enough=%s" % (tier, sum(q), ok))
io.open(out, 'w', encoding='utf-8').write("\n".join(lines))
print("done")
