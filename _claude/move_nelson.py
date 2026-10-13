"""Move the Nelson chapter from week 6 to week 7, where the revised reading guide sets it.

It was written into week 6 because the copy of the reading guide read on 28 September put it
there. The professor revised that file in place and moved chapter 20 to week 7, and the section
was left where it was with a label, on the grounds that it is the worked example for chapters 4
and 5. Week 6 is one class covering 44 pages, which is already double, so it goes where it belongs.
"""
import re, os, shutil

six = open('week-6/index.html', encoding='utf-8').read()
sev = open('week-7/index.html', encoding='utf-8').read()

# ---- lift the article out of week 6 -------------------------------------------------
art = re.search(r'\n      <article class="rd[^"]*" id="nelson">.*?\n      </article>\n', six, re.S)
assert art, 'article'
ART = art.group(0)
six = six[:art.start()] + '\n' + six[art.end():]

# nav entry and its four sub-entries
nav = re.search(r'\n  <a class="core" href="#nelson".*?(?=\n  <a class="grp")', six, re.S)
assert nav, 'nav'
six = six[:nav.start()] + six[nav.end():]

# the glossary group
glo = re.search(r'\n\s*<div class="gl-grp">\s*<h3>Biology<span>Nelson</span></h3>.*?</dl>\s*</div>', six, re.S)
assert glo, 'glossary group'
GLO = glo.group(0)
six = six[:glo.start()] + six[glo.end():]

def sub(h, old, new, label):
    assert old in h, label
    return h.replace(old, new, 1)

six = sub(six, '<div class="t-b"><b>12</b><span>pages of Nelson, which is set for week 7</span></div>',
          '<div class="t-b"><b>44</b><span>pages in all, for one class</span></div>', 'tally')
six = sub(six, ' A third chapter, set for next week, watches both happen to one field over a hundred years.',
          '', 'standfirst')
six = sub(six, '<h3 class="sub">Three readings, two questions</h3>',
          '<h3 class="sub">Two readings, two questions</h3>', 'sub head')
six = sub(six, 'Chapter 4 and chapter 5 ask opposite halves of the same thing, and Nelson runs both of them through one science.',
          'Chapter 4 and chapter 5 ask opposite halves of the same thing.', 'table lede')
six = sub(six, '''<tr><td><b class="tag t3">Nelson</b><span>Biology, 150 years</span></td>
            <td>What does one field look like after both of those questions have been running inside it for a century and a half?</td>
            <td>Darwin on the peacock, and who was watching the baboons</td></tr>''', '', 'table row')
six = sub(six, '''<p><b>Nelson's chapter is both arguments happening to one field for 150 years.</b> Darwin needed to explain why a peacock has a train that makes it easy to catch and hard to fly with, invented <b>sexual selection</b> to do it, and built into the same theory a picture of eager males and coy females that came from Victorian England. In the 1960s anthropologists watching baboons reported that male dominance ran the troop. In the 1970s Jeanne Altmann watched the females instead and concluded the opposite: the drama between males matters far less to the group than what the mothers are doing. <b>Same animals, same park, different people looking.</b></p>''',
          '''<p><b>Next week carries both arguments into one science.</b> Nelson's chapter, set for 19 to 21 October, runs chapter 4's question and chapter 5's question through biology over 150 years, and its second case study is the full version of the primatology story week 5 opened with.</p>''', 'argument para')
six = sub(six, ' The Nelson chapter at the end is set for week 7 and is kept here because it is the case study for both, and because it finishes the story week 5 began.',
          ' Nelson on biology, which the first version of the reading guide put in this week, is in the week 7 guide where the revised one sets it.', 'lede note')

# ---- put it into week 7 -------------------------------------------------------------
stub = re.search(r'\n      <article class="rd[^"]*" id="ch20">.*?\n      </article>\n', sev, re.S)
assert stub, 'stub'

WHY_OLD = re.search(r'<div class="why">.*?</div>', ART, re.S).group(0)
WHY_NEW = ('<div class="why"><b>Why this chapter is set.</b> It is the worked example for the whole '
           'of last week. Chapter 4 asked where a value can enter a piece of research and chapter 5 '
           'asked how ignorance gets produced, and this is both of them happening to one science '
           'across 150 years. Its second case study is the full version of the primatology story '
           'week 5 opened with. The first three pages are a survey and can be read quickly. '
           '<b>The two case studies are the reason it is on the list.</b></div>')
ART = ART.replace(WHY_OLD, WHY_NEW, 1)
ART = ART.replace('<span class="tag">Set for week 7</span>', '<span class="tag">Read properly</span>', 1)
ART = ART.replace('id="nelson"', 'id="ch20"').replace('href="#nelson', 'href="#ch20').replace('data-of="nelson"', 'data-of="ch20"')
ART = re.sub(r'(<h4 id=")nelson-', r'\1ch20-', ART)
sev = sev[:stub.start()] + ART + sev[stub.end():]

sev = sub(sev, '<a class="skim" href="#ch20" title="Nelson &middot; narrated in week 6">Biology<i>ch 20</i></a>',
          '<a class="core" href="#ch20" title="Routledge Handbook ch. 20 &middot; read properly">Biology<i>12 pp</i></a>\n  '
          '<a class="sb" data-of="ch20" href="#ch20-1"><b>20.1</b>Four faults</a>\n  '
          '<a class="sb" data-of="ch20" href="#ch20-2"><b>20.2</b>The peacock&#8217;s tail</a>\n  '
          '<a class="sb" data-of="ch20" href="#ch20-3"><b>20.3</b>The baboons</a>\n  '
          '<a class="sb" data-of="ch20" href="#ch20-4"><b>20.4</b>What it proves</a>', 'week7 nav')
sev = sub(sev, '<div class="t-b"><b>37</b><span>pages to read. Ch. 20 was done in week 6</span></div>',
          '<div class="t-b"><b>49</b><span>pages in all, across four chapters</span></div>', 'week7 tally')
sev = sub(sev, '''<td>Already in the week 6 guide. One field running both of week 6's questions for 150 years.</td>''',
          '''<td>One field running both of week 6's questions for 150 years, which makes it the worked example for last week.</td>''', 'week7 table row')
GLO7 = GLO.replace('\n          ', '\n      ').replace('\n            ', '\n        ')
sev = sub(sev, '\n        </dl>\n      </div>\n\n    </div>\n    </details>',
          '\n        </dl>\n      </div>' + GLO7 + '\n\n    </div>\n    </details>', 'week7 glossary')
sev = sev.replace('../week-6/img/baboon.jpg', 'img/baboon.jpg')

open('week-6/index.html', 'w', encoding='utf-8').write(six)
open('week-7/index.html', 'w', encoding='utf-8').write(sev)

os.makedirs('week-7/img', exist_ok=True)
for img in ('peacock.jpg', 'baboon.jpg'):
    shutil.move('week-6/img/' + img, 'week-7/img/' + img)
    print('moved image', img)
print('chapter moved')
