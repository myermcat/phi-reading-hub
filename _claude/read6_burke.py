import sys; sys.path.insert(0, '_claude')
from figmove import cut
f='week-6/index.html'; h=open(f,encoding='utf-8').read()
h, fig = cut(h, 'img/burke.jpg')
anchor = 'with it the encounter changed shape.</p>\n'
assert anchor in h
k = h.find(anchor) + len(anchor)
h = h[:k] + '          </div>\n\n          ' + fig + '\n\n          <div class="body">\n' + h[k:]
open(f,'w',encoding='utf-8').write(h)
print('burke moved')
