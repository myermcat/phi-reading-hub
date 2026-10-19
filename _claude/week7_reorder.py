"""Put the three answers where the text promises them, with the drawing that tabulates them."""
import re
f='week-7/index.html'; h=open(f,encoding='utf-8').read()

# the original list and its intro, which sat after the diagram
blk = re.search(r'\n    <div class="body">\n      <p><b>Three attempts to pay that debt, and the third one changes the subject\.</b></p>\n      <ol>\n.*?\n      </ol>\n    </div>\n', h, re.S)
assert blk, 'original three-attempts block'
OL = re.search(r'      <ol>\n.*?\n      </ol>\n', blk.group(0), re.S).group(0)
h = h[:blk.start()] + '\n' + h[blk.end():]

# the drawing belongs beside the three it tabulates
fig = re.search(r'\n<figure class="dia">\n.*?\n    </figure>\n', h, re.S)
assert fig, 'diagram'
FIG = fig.group(0)
h = h[:fig.start()] + '\n' + h[fig.end():]

anchor = '      <p><b>Three attempts to pay that debt, and the third changes the subject.</b></p>\n    </div>\n'
assert anchor in h
h = h.replace(anchor,
              '      <p><b>Three attempts to pay that debt, and the third changes the subject.</b></p>\n'
              + OL + '    </div>\n' + FIG, 1)

open(f,'w',encoding='utf-8').write(h)
print('three answers and their drawing moved up')
