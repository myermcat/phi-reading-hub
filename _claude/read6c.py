import re
f='week-6/index.html'; h=open(f,encoding='utf-8').read()
def sub(old,new):
    global h
    assert old in h, 'MISS: '+old[:80]
    h = h.replace(old,new,1)

# ---------- 5.1 ----------
sub('''<p><b>What the authors say it did, which is more interesting than what it is usually credited with.</b> It made visible something most people had not known: how common sexual assault and harassment are, especially at work. And it did something sharper. <b>It gave survivors a way to see their own experience differently.</b> Women who had described an encounter with an employer as consensual, including Monica Lewinsky and several NBC employees who worked with Matt Lauer, later said the consent had come partly from fear of what refusing would do to their careers. The movement handed people a concept, and with it the encounter changed shape.</p>''',
'''<p><b>What the authors say it did, which is more interesting than what it is usually credited with.</b> It made visible something most people had not known: how common sexual assault and harassment are, especially at work.</p>
            <p><b>And it did something sharper. It gave survivors a way to see their own experience differently.</b> Women who had described an encounter with an employer as consensual, including Monica Lewinsky and several NBC employees who worked with Matt Lauer, later said the consent had come partly from fear of what refusing would do to their careers. The movement handed people a concept, and with it the encounter changed shape.</p>''')

sub('''<p><b>Then the question that opens the field.</b> Sexual violence and the laws against it had existed for decades. So why did this count as <em>news</em>? How can facts stay unknown, or get obscured, for very large numbers of people?</p>
          </div>''',
'''</div>

          <div class="keep">
            <b>The question that opens the field</b>
            Sexual violence and the laws against it had existed for decades. So why did any of this
            count as news? How can facts stay unknown, or get obscured, for very large numbers of
            people at once?
          </div>''')

# ---------- 5.3, kinds 1 to 3 become a list, kinds 4 and 5 get headings ----------
sub('''<p><b>1. What we do not know but do not care to.</b> Since the 1960s hormonal contraception has been aimed at women and tested on women. <b>Male hormonal contraception was considered and dropped.</b> The reasoning was that men would be less motivated to use it and less willing to accept side effects, with reduced libido the example. Nobody worried about reduced libido in women, <b>because of the standing assumption that women did not have much desire to begin with</b>. Pharmaceutical companies also assumed preventing conception was women's job, so it looked unmarketable. We still have no safe effective male hormonal contraceptive, and the reason is a decision, and never a difficulty.</p>
            <p><b>2. What we do not know that we do not know.</b> Hard to spot, and in hindsight it looks like the first. Tuana's case is the anatomy of the clitoris. Study of the genitals was organised around reproduction, the clitoris was taken to play no part in reproduction, and so it was <b>not a thing to be ignorant about</b>. It was not rejected as unworthy. It was never an object of enquiry at all.</p>
            <p><b>3. What they do not want us to know.</b> The pharmaceutical industry concealing known risks and side effects of oestrogen in contraceptives, to protect its margins. The chapter notes that this kind is not automatically wrong, since restricted dangerous knowledge is also somebody deciding what you may not know.</p>
            <p><b>4. Willful ignorance: what we do not know and do not want to.</b> The one the chapter treats most seriously, and the only kind where the ignorant person is <b>doing something</b>, namely employing active strategies to avoid knowing, including neglecting evidence that would force the knowledge on them.</p>
          </div>''',
'''<ol>
              <li><b>What we do not know but do not care to.</b> Since the 1960s hormonal contraception has been aimed at women and tested on women. <b>Male hormonal contraception was considered and dropped.</b> The reasoning was that men would be less motivated to use it and less willing to accept side effects, with reduced libido the example. Nobody worried about reduced libido in women, <b>because of the standing assumption that women did not have much desire to begin with</b>. Pharmaceutical companies also assumed preventing conception was women's work, so it looked unmarketable. We still have no safe effective male hormonal contraceptive, and what stopped it was a decision about who would buy it.</li>
              <li><b>What we do not know that we do not know.</b> Hard to spot, and in hindsight it looks like the first. Tuana's case is the anatomy of the clitoris. Study of the genitals was organised around reproduction, the clitoris was taken to play no part in reproduction, and so it was <b>not a thing to be ignorant about</b>. Nobody rejected it as unworthy. It was never an object of enquiry at all.</li>
              <li><b>What they do not want us to know.</b> The pharmaceutical industry concealing known risks and side effects of oestrogen in contraceptives, to protect its margins. The chapter notes that this kind is not automatically wrong, since restricted dangerous knowledge is also somebody deciding what you may not know.</li>
            </ol>
          </div>

          <h5>Kind 4, willful ignorance, which the chapter spends most of its length on</h5>
          <div class="body">
            <p><b>What we do not know and do not want to.</b> This is the only one of the five where the ignorant person is <b>doing something</b>, namely employing active strategies to avoid knowing, including neglecting evidence that would force the knowledge on them.</p>
          </div>''')

sub('''<p><b>5. What we cannot know.</b> The one kind that is not a failing.''',
'''<p><b>What we cannot know.</b> The one kind that is no failing at all.''')
sub('''<div class="body">
            <p><b>What we cannot know.</b> The one kind that is no failing at all.''',
'''<h5>Kind 5, and the one that asks something of the reader</h5>
          <div class="body">
            <p><b>What we cannot know.</b> The one kind that is no failing at all.''')

sub('''<p><b>And Tuana's own caveat.</b> The list is not exhaustive, and one phenomenon can occupy several rows. White ignorance can be not caring to know, or blocked by current interests, or willful, or lovingly ignorant even in somebody actively anti-racist, because they can never fully know what it is to live as a Black person in a racist society.</p>
          </div>''',
'''</div>

          <div class="keep">
            <b>Tuana's own caveat</b>
            The list is not exhaustive, and one phenomenon can occupy several rows at once. White
            ignorance can be not caring to know, or blocked by present interests, or willful, or
            lovingly ignorant even in somebody actively anti-racist, because they can never fully know
            what it is to live as a Black person in a racist society.
          </div>''')

sub('which she reads as a campaign against produced ignorance, and never only a campaign for access, and the order',
    'which she reads as a campaign against produced ignorance as much as a campaign for access, and the order')

open(f,'w',encoding='utf-8').write(h)
print('ok')
