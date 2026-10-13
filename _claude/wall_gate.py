"""Find the blocks readability.md calls walls.

Two measures, both from the rules:
  run   how many <p> in a row with nothing of another kind between them
  chars how much continuous prose that run adds up to
A run of 3 or more, or more than about 1200 characters, has to be broken by
something of a different kind: a list, a table, a callout, a figure.
"""
import re, sys, html as H

BREAK = ('ul', 'ol', 'table', 'figure', 'div class="exm"', 'div class="ctx"',
         'div class="keep"', 'div class="quo"', 'div class="facts"', 'dl',
         'h3', 'h4', 'h5', 'div class="nine"', 'div class="scroller"')

def text(s):
    return H.unescape(re.sub(r'<[^>]+>', '', s)).strip()

for f in sys.argv[1:]:
    h = open(f, encoding='utf-8').read()
    body = h[h.find('<div class="wrap">'):h.find('<footer')]
    heads = [(m.start(), m.group(2), text(m.group(3))[:52])
             for m in re.finditer(r'<(h[2-5])([^>]*)>(.*?)</\1>', body, re.S)]
    print('\n=== %s' % f)
    for i, (pos, lvl, title) in enumerate(heads):
        end = heads[i+1][0] if i+1 < len(heads) else len(body)
        chunk = body[pos:end]
        # a callout or a worked example is already a different kind of thing on the page,
        # so what is inside one does not count toward the run outside it
        for cls in ('exm', 'ctx', 'keep', 'curious', 'quo', 'nb', 'cmt'):
            chunk = re.sub(r'<div class="%s"[ >].*?</div>\n' % cls, '<hr>', chunk, flags=re.S)
        chunk = re.sub(r'<figcaption.*?</figcaption>', '', chunk, flags=re.S)
        run = chars = worst = worstc = 0
        for m in re.finditer(r'<(p|ul|ol|table|figure|dl|hr|blockquote|div class="[a-z]+")[ >]', chunk):
            t = m.group(1)
            if t == 'p':
                run += 1
                seg = chunk[m.start():chunk.find('</p>', m.start())]
                chars += len(text(seg))
                if run > worst: worst, worstc = run, chars
            else:
                run = chars = 0
        if worst >= 3 or worstc > 1200:
            flag = 'WALL' if (worst >= 4 or worstc > 1500) else 'tight'
            print('  %-5s %-3s run=%-2d chars=%-5d %s' % (flag, lvl, worst, worstc, title))
