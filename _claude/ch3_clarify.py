"""Two sentences that assumed a reader already had the example."""
import re
f='week-7/index.html'; h=open(f,encoding='utf-8').read()
def sub(a,b,label):
    global h
    assert a in h, label
    h=h.replace(a,b,1)

sub('''<b>Hume</b> aims at religious authority, arguing in <em>On Miracles</em> that people set aside countless regularities of nature on the strength of one reported exception. A marble statue said to bleed outweighs every piece of marble that has never bled.''',
    '''<b>Hume</b> aims at religious authority, in <em>On Miracles</em>, and his case is how a miracle report gets believed. Somebody reports that a marble statue bled. That one report is allowed to outweigh every piece of marble anybody has ever watched fail to bleed. The evidence for the rule is enormous, the evidence for the exception is one person's word, <b>and belief goes the other way.</b>''', 'hume')

sub('''<dd>An <b>unobservable mechanism proposed to account for what you can see</b>, which is not the modern sense of a guess you go and test. Descartes's vortices are the case everybody argued about. Whether a scientist may propose one at all is the quarrel this chapter is about.</dd>''',
    '''<dd>An <b>unobservable mechanism proposed to account for what you can see</b>, which is not the modern sense of a guess you go and test. Hawking radiation is one in this sense: nobody has observed it, and it is proposed because the theory needs it. In 1740 the case everybody argued about was Descartes's vortices. Whether a scientist may propose one at all is this chapter's quarrel.</dd>''', 'glossary')
open(f,'w',encoding='utf-8').write(h)
print('Hume example unpacked; glossary uses an example she knows')
