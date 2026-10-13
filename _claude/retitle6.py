"""Lead with the key words, same pass as week 7."""
import re
f='week-6/index.html'; h=open(f,encoding='utf-8').read()
H4 = {
 'ch4-3':   'The rod and frame test, walked down the chain',
 'ch5-1':   'MeToo, and the question it opens',
 'ch5-2':   'Agnotology, and what most people get wrong about ignorance',
 'nelson-1':'Four faults to look for in a piece of biology',
 'nelson-2':'The peacock&#8217;s tail, and what Darwin built to explain it',
 'nelson-3':'The baboons, and the primate pattern that came off them',
 'nelson-4':'What all this proves, and the two debates about it',
}
H5 = [
 ('<h5>Phase 6 in detail, because the term here is the one to know</h5>',
  '<h5>Phase 6 in detail, where inductive risk lives</h5>'),
 ('<h5>Kind 4, willful ignorance, which the chapter spends most of its length on</h5>',
  '<h5>Willful ignorance, kind 4, which the chapter spends most of its length on</h5>'),
 ('<h5>Kind 5, and the one that asks something of the reader</h5>',
  '<h5>Loving ignorance, kind 5, which asks something of the reader</h5>'),
]
def one(m):
    hid=m.group(1)
    return m.group(0) if hid not in H4 else '%s%s</h4>' % (m.group(0)[:m.group(0).index('>')+1], H4[hid])
h=re.sub(r'<h4 id="([^"]+)"[^>]*>.*?</h4>', one, h, flags=re.S)
for a,b in H5:
    assert a in h, a[:40]
    h=h.replace(a,b,1)
for v in H4.values(): assert v in h, v
open(f,'w',encoding='utf-8').write(h)
print('retitled %d headings and %d subheadings' % (len(H4), len(H5)))
