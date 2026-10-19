"""Define the word the dispute turns on, and pay for it by cutting.

"Whether science may use hypotheses at all" is nonsense to anybody who knows what a hypothesis is
today, and that is why it needed explaining: in 1740 the word meant something else. Nothing in the
chapter said so, so the dispute could not be followed.
"""
import re, html as H
f='week-7/index.html'; h=open(f,encoding='utf-8').read()

def wc(s):
    return len(H.unescape(re.sub(r'<[^>]+>',' ',re.sub(r'<svg.*?</svg>','',s,flags=re.S))).split())
def chap():
    a=h.find('<article class="rd p-close" id="ch3">'); return h[a:h.find('</article>',a)]
before = wc(chap())

def sub(old,new,label):
    global h
    assert old in h, label
    h = h.replace(old, new, 1)

# the why block retold the three steps the section below gives in full
sub('''This is the cleanest case of it anybody has. &Eacute;milie Du Ch&acirc;telet was shut out of the French academy, noticed that beliefs about women were held without anybody ever examining them, and turned that into a rule: <b>examine a belief before you hold it</b>. She applied it to the question of whether science may use hypotheses at all, where the British and the French were each defending their own, and answered that hypotheses are necessary and have to obey four rules. The field took another century and a half to agree.''',
    '''This is the cleanest case of it anybody has, and the three steps from the one to the other are below.''', 'why')

sub('''<p><b>The answer, in the framework Detlefsen uses: two camps, and the dispute was about whether hypotheses are allowed at all.</b></p>''',
    '''<p><b>Start with the word, because it did not mean then what it means now.</b> Today a hypothesis is a guess you go and test. In 1740 it meant <b>an unobservable mechanism proposed to account for what you can see</b>. Descartes is the case everybody argued about: he said space is filled with invisible swirling matter, and that these vortices carry the planets round their orbits. Nobody could see a vortex or measure one, and it was proposed because it made the motions come out right.</p>
            <p><b>So the dispute was whether a scientist may propose a cause nobody can observe</b>, and two camps had formed around it.</p>''', 'word')

sub('''<p><b>What they meant by the charge.</b> Newton: experimental philosophy reduces phenomena to general rules, while hypothetical philosophy consists in <b>imaginary explications of things and imaginary arguments</b> for or against them, and he follows the first while Descartes and Leibniz follow the second too much. A contemporary dismisses the systems of Descartes, Gassendi and Hobbes as possibly <b>chimeras and amusing notions, fit to entertain working heads.</b></p>''',
    '''<p><b>Why Newton's side said no.</b> Newton showed that gravity acts as the inverse square of the distance between two bodies, then refused to say what gravity <em>is</em> or what causes it, because he could demonstrate neither. His phrase for the refusal is <em>hypotheses non fingo</em>, I feign no hypotheses. His followers turned it into a ban: propose no cause you cannot show. In his own words, experimental philosophy reduces phenomena to general rules, while hypothetical philosophy consists in <b>imaginary explications of things</b>, and Descartes and Leibniz go in for the second too much.</p>''', 'newton')

sub('''<p><b>And the nationalism riding on top of it, which is why her rule is relevant.</b> Voltaire's <em>Elements of Newton's Philosophy</em> draws a bright line between the old French way of hypotheses and the new British hard-headed experimentalism, and tells the French to catch up. <b>So the scientific question had an English answer and a French answer</b>, which is exactly the situation her letter to her son is about.</p>''',
    '''<p><b>And the nationalism on top of it, which is why her rule matters here.</b> Descartes was French and Newton was English, so defending vortices was defending French science, and taking Newton meant conceding to the English. Voltaire's <em>Elements of Newton's Philosophy</em> told the French to give up Descartes and take the British physics, ban included. <b>So the scientific question had an English answer and a French answer</b>, which is the situation her letter to her son is about.</p>''', 'nationalism')

sub('''<p><b>One piece of context worth having, because it changes who she is.</b> For decades her thought was treated as derivative of Voltaire's, with whom she lived and worked. Detlefsen calls that claim evidence-free, and says close examination of her work has debunked it. Her treatment of hypotheses is the example: <b>she does not agree with him.</b></p>''',
    '''<p><b>Her thought was treated as Voltaire's for two centuries</b>, since they lived and worked together. Detlefsen calls that evidence-free, and hypotheses are the example: <b>she does not agree with him.</b></p>''', 'voltaire context')

after = wc(chap())
open(f,'w',encoding='utf-8').write(h)
print('ch3: %d words -> %d  (%+d)' % (before, after, after - before))
