"""Put the chapters in the order they are read, Monday's two first.

The guide ran chapter 15 first because it carries the week's framework. The day split halves the
professor's list in her own order, which puts chapters 3 and 20 on Monday, so the guide was
presenting Wednesday's reading before Monday's and the lookup table was the only place that said
so. Neither chapter 3 nor chapter 20 depends on chapter 15, so nothing is lost by reading in the
order the week is taught.
"""
import re
f='week-7/index.html'; h=open(f,encoding='utf-8').read()

arts = {}
for m in re.finditer(r'\n      <article class="rd[^"]*" id="(ch\d+)">.*?\n      </article>\n', h, re.S):
    arts[m.group(1)] = m.group(0)
assert set(arts) == {'ch15','ch19','ch3','ch20'}, sorted(arts)

first = min(h.find(a) for a in arts.values())
last = max(h.find(a) + len(a) for a in arts.values())
between = h[first:last]
for a in arts.values():
    between = between.replace(a, '')
assert between.strip() == '', 'something sits between the chapters: ' + between.strip()[:80]

ORDER = ['ch3', 'ch20', 'ch15', 'ch19']
h = h[:first] + ''.join(arts[k] for k in ORDER) + h[last:]

# the contents list gets the same order, with the two class days separated
nav = re.search(r'(  <a class="grp" href="#s-texts">The reading</a>\n)(.*?)(  <a class="grp" href="#s-gloss">)', h, re.S)
assert nav, 'nav block'
rows = {}
for m in re.finditer(r'  <a class="core" href="#(ch\d+)".*?\n(?:  <a class="sb".*?\n)*', nav.group(2), re.S):
    rows[m.group(1)] = m.group(0)
assert set(rows) == {'ch15','ch19','ch3','ch20'}, sorted(rows)
newnav = ('  <a class="grp day" href="#s-days">Monday 19 Oct</a>\n'
          + rows['ch3'] + rows['ch20']
          + '  <a class="grp day" href="#s-days">Wednesday 21 Oct</a>\n'
          + rows['ch15'] + rows['ch19'])
h = h[:nav.start(2)] + newnav + h[nav.end(2):]
h = h.replace('  <a class="grp" href="#s-texts">The reading</a>\n', '', 1)

# a day marker is a divider, so it is drawn as one
CSS_AT = '  #nav a.grp:first-child { margin-top: 0; }'
assert CSS_AT in h
h = h.replace(CSS_AT, CSS_AT + '''
  #nav a.grp.day { margin-top: 15px; padding-top: 11px; border-top: 1px solid var(--rule);
                   color: var(--accent); }
  #nav a.grp.day:first-child { margin-top: 0; }''', 1)

open(f,'w',encoding='utf-8').write(h)
print('chapters now run %s, and the contents list splits the two days' % ', '.join(ORDER))
