"""The word the chapter turns on was not a glossary term, and a caption said there was an
argument without saying what it was."""
import re
f='week-7/index.html'; h=open(f,encoding='utf-8').read()
def sub(a,b,label):
    global h
    assert a in h, label
    h=h.replace(a,b,1)

# the dashed underline reads from the glossary, so a term that is not in it is never marked
sub('''<dt>the ethics of belief</dt>''',
    '''<dt>hypothesis, in 1740</dt><dd>An <b>unobservable mechanism proposed to account for what you can see</b>, which is not the modern sense of a guess you go and test. Descartes's vortices are the case everybody argued about. Whether a scientist may propose one at all is the quarrel this chapter is about.</dd>
            <dt>the ethics of belief</dt>''', 'glossary entry')

sub('''Portraits of women of her rank did not usually carry instruments, and the painting is making the same argument she spent her life making.''',
    '''Portraits of women of her rank did not usually carry instruments. The painting puts her in the posture of someone who measures and calculates, which is the claim she spent her life making: that women are kept from this work by their education and by what everyone assumes, and not by their minds.''', 'caption')
open(f,'w',encoding='utf-8').write(h)
print('hypothesis defined; caption says what the argument is')
