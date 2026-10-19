"""Gloss at first use, unpack the quotation, name the Scholastics."""
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

# the word is used from the standfirst down and was defined forty thousand characters in
sub('''She applied that rule to the dispute over whether science may use hypotheses at all,''',
    '''She applied that rule to the dispute over whether science may use <b>hypotheses</b> at all, the word then meaning an unobservable mechanism like Descartes's invisible matter between the planets,''', 'first use gloss')

# a quotation is a compressed argument and gets unpacked
sub('''<b>which is dangerous everywhere in life and ridiculous in physics.</b></p>''',
    '''<b>which is dangerous everywhere in life and ridiculous in physics.</b> The dispute is Newton against Descartes, and she is telling a thirteen-year-old that holding a position because of the country he was born in is absurd when the question is what the world is like.</p>''', 'quote')

sub('''<b>Descartes</b> aims at the Scholastics,''',
    '''<b>Descartes</b> aims at the <b>Scholastics</b>, the medieval university philosophers who settled questions by reasoning from Aristotle and from established authority,''', 'scholastics')

# a pointer with no content, and the heading below it already says this
sub(''', and the three steps from the one to the other are below.''', '.', 'why pointer')
open(f,'w',encoding='utf-8').write(h)
print('ch3: %d -> %d words (%+d)' % (before, wc(chap()), wc(chap())-before))
