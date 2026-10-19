"""Put the author portraits back, beside the teaching pictures rather than in place of them.

Cutting them was half right. A portrait that stands in for a teaching picture is filling a slot.
A portrait next to one tells the reader whose argument she is reading, which she says helps, so
they go back on top of what replaced them.
"""
import sys; sys.path.insert(0,'_claude')
import re
f='week-6/index.html'; h=open(f,encoding='utf-8').read()

PLACE = [
  ('mills',  'Willful ignorance, kind 4'),      # the section his argument carries
  ('tuana',  '5. Selective representation'),    # her five strategies end here
  ('darwin', 'Three objections Nelson reports'),
]
for name, anchor in PLACE:
    blk = open('/tmp/fig_%s.html' % name, encoding='utf-8').read().strip()
    if name == 'darwin':
        continue                                 # Darwin went to week 7 with the Nelson chapter
    k = h.find(anchor)
    assert k > 0, anchor
    end = h.find('</div>', h.find('</p>', k))
    end = h.find('\n', end) + 1
    h = h[:end] + '\n          ' + blk + '\n' + h[end:]
    print('restored', name)
open(f,'w',encoding='utf-8').write(h)
