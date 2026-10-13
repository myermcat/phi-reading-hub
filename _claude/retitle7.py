"""Lead with the key words.

The layer-cake scan only works when a reader can tell what is under a heading from the heading.
Half of week 7's opened with filler: "the thing she is pointing at", "the case the chapter opens
on", "the claim the chapter is making". The key word arrived eight words in, or never.
"""
f='week-7/index.html'; h=open(f,encoding='utf-8').read()
NEW = {
 'ch15-1': 'Hormone replacement therapy, studied for sixty years by the rules',
 'ch19-2': 'Inclusion that leaves the system intact',
 'ch19-3': 'Illiteracy as resistance, the argument you will want to argue with',
 'ch19-4': 'The Black Panthers, the health movement, and who else was already doing it',
 'ch19-5': 'The do-it-yourself biology labs, and who is actually in them',
 'ch3-1':  'Three steps from being shut out to getting hypotheses right',
 'ch3-2':  'What she noticed about beliefs concerning women',
 'ch3-3':  'Her rule, and the company it puts her in',
 'ch3-4':  'The quarrel over hypotheses, and why both sides were getting it wrong',
}
import re
def one(m):
    hid=m.group(1)
    return m.group(0) if hid not in NEW else '%s%s</h4>' % (m.group(0)[:m.group(0).index('>')+1], NEW[hid])
before=h
h=re.sub(r'<h4 id="([^"]+)"[^>]*>.*?</h4>', one, h, flags=re.S)
assert h!=before
for k in NEW: assert NEW[k] in h, k
open(f,'w',encoding='utf-8').write(h)
print('retitled %d headings' % len(NEW))
