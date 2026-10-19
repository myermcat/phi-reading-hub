"""Two errors and a duplicate, all in the hypotheses section.

The guide claimed she reached the position you were taught in school, two paragraphs after
explaining that the 1740 word means something school never teaches. School teaches that a
hypothesis is a testable guess. Hers is that an unobservable mechanism is permitted under rules,
which is a different claim and the whole reason the chapter is interesting.

And the section said hypotheses are necessary where no other route to the cause exists without
once showing such a case, which is the only way that sentence means anything.
"""
import re, html as H
f='week-7/index.html'; h=open(f,encoding='utf-8').read()
def wc(s): return len(H.unescape(re.sub(r'<[^>]+>',' ',re.sub(r'<svg.*?</svg>','',s,flags=re.S))).split())
def chap():
    a=h.find('<article class="rd p-close" id="ch3">'); return h[a:h.find('</article>',a)]
before=wc(chap())
def sub(a,b,label):
    global h
    assert a in h, label
    h=h.replace(a,b,1)

sub('''<p><b>And the position she reached is the one you were taught in school: hypotheses are central to science.</b> In 1740 that was close to heresy.</p>''',
    '''<p><b>The rules she set for them are, in substance, the ones the field arrived at much later.</b> In 1740 even saying hypotheses are necessary was close to heresy.</p>''', 'school claim')

sub('''That gap is permanent, so the tool is permanent.</p>''',
    '''That gap is permanent, so the tool is permanent.</p>
            <p><b>Copernicus is the case.</b> You cannot watch the Earth move, and nothing already known lets you deduce that it does. Standing still, what you see is the sun going round you. So the Earth's motion enters as a hypothesis, proposed because it makes the planetary paths come out far simpler, and then checked against what follows from it.</p>''', 'copernicus')

sub('''          <div class="keep">
            <b>Without hypotheses there would be no astronomy</b>
            Without hypotheses there would be no astronomy now.
          </div>

''', '''''', 'duplicate keep')

sub('''<p><b>And the argument from who used them.</b> Copernicus, Kepler, Huygens, Descartes, Leibniz <b>and Newton himself</b> all devised useful hypotheses to explain difficult phenomena.</p>''',
    '''<p><b>Her flattest statement of it: without hypotheses there would be no astronomy.</b> And the argument from who used them. Copernicus, Kepler, Huygens, Descartes, Leibniz <b>and Newton himself</b> all devised useful hypotheses to explain difficult phenomena.</p>''', 'astronomy line')

old=re.search(r'<p><b>So, she says, those who want to ban them from philosophy intend harm to the interests of science\.</b>.*?</p>', h, re.S)
assert old, 'target sentence'
sub(old.group(0), '''<p><b>So, she says, those who want to ban them from philosophy intend harm to the interests of science.</b></p>''', 'newton target')

after=wc(chap())
open(f,'w',encoding='utf-8').write(h)
print('ch3: %d -> %d words (%+d)' % (before, after, after-before))
