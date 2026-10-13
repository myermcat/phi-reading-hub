import sys; sys.path.insert(0, '_claude')
from figmove import cut
f='week-7/index.html'; h=open(f,encoding='utf-8').read()
def sub(old,new):
    global h
    assert old in h, 'MISS: '+old[:80]
    h = h.replace(old,new,1)

# ---------------- the argument ----------------
sub('''what stops it being a free-for-all?</p>\n''',
'''what stops it being a free-for-all?</p>

    <h3 class="sub">Four readings, one question</h3>
    <p class="lede">Three of them answer it and disagree about how much to demand. The fourth asks who was ever allowed to answer.</p>
    <div class="scroller">
      <table class="nine">
        <thead><tr><th>The reading</th><th>What it contributes</th><th>The case it runs on</th></tr></thead>
        <tbody>
          <tr><td><b class="tag t1">Chapter 15</b><span>Intemann</span></td>
            <td>Names the five places a value enters, and sets out the two models that could replace the value-free ideal.</td>
            <td>Sixty years of hormone replacement therapy</td></tr>
          <tr><td><b class="tag t2">Chapter 19</b><span>Giordano</span></td>
            <td>Says both models are academics arguing about academics, and asks who counts as a scientist at all.</td>
            <td>Black Panther clinics, and the do-it-yourself biology labs</td></tr>
          <tr><td><b class="tag t3">Chapter 3</b><span>Du Ch&acirc;telet</span></td>
            <td>A worked historical case: a woman gets the account of hypotheses right in 1740 and is read as derivative for two centuries.</td>
            <td>The quarrel over whether hypotheses are allowed</td></tr>
          <tr><td><b class="tag t3">Chapter 20</b><span>Nelson</span></td>
            <td>Already in the week 6 guide. One field running both of week 6's questions for 150 years.</td>
            <td>Darwin's peacock, and the baboons</td></tr>
        </tbody>
      </table>
    </div>
''')

sub('''<p><b>Start with what is being given up, because it has a name and it is the thing every chapter attacks.</b> The <b>value-free ideal</b>, which this week abbreviates <b>VFI</b>, says that social, moral and political values must play no part in the <em>core</em> of science. Nobody ever claimed values are absent entirely: of course they decide what gets funded and what you may do to a research subject. The claim is narrower and tougher. Heather Douglas calls the protected part the <b>heart</b> of scientific reasoning: deciding what counts as evidence, which theory the evidence supports, and what to accept. There, values are supposed to be out.</p>''',
'''<p><b>Start with what is being given up, because it has a name and every chapter attacks it.</b> Nobody ever claimed values are absent from science entirely: of course they decide what gets funded and what you may do to a research subject. The claim being made is narrower and tougher.</p>
    </div>

    <dl class="facts">
      <dt>The value-free ideal</dt>
      <dd>Abbreviated <b>VFI</b> all week. Social, moral and political values must play no part in the <em>core</em> of science.</dd>
      <dt>The core, or the heart</dt>
      <dd>Heather Douglas's name for the protected part: <b>deciding what counts as evidence, which theory the evidence supports, and what to accept</b>. There, values are supposed to be out.</dd>
    </dl>

    <div class="body">''')

# the three answers are three parallel things, so they are a list, and the diagram that
# tabulates them belongs above them
h, dia = cut(h, '<title id="dg-three7">')
sub('''<p><b>Then the problem the week actually has to solve.</b> Take away the VFI and you owe an account of what replaces it, or the objection from week 5 comes straight back: if any values are allowed, anybody can claim their own, and there is nothing left to argue with. The two answers in chapter 15 are both attempts to pay that debt.</p>
      <p><b>Answer one, the value-management model.</b> Any values may enter, provided the community is diverse enough and critical enough to catch the ones doing damage. Values get <em>managed</em>, and never chosen. This is Longino's four norms from week 6, now used as a political proposal.</p>
      <p><b>Answer two, the social justice model.</b> That is not enough, because it assumes a level field that does not exist. Publicly funded science should have an aim, and the aim is to benefit everyone and especially the worst off. This one <b>picks</b> values, where the first only manages them.</p>
      <p><b>And the third chapter asks a question neither of them asks.</b> Giordano points out that both answers are arguments conducted among academics about how academics should behave. If you look instead at people outside universities who have produced real knowledge, Black Panther clinics, the women's health movement, the AIDS activists who rewrote how drug trials run, then the question stops being which values scientists should hold and becomes <b>who counts as a scientist at all.</b></p>
    </div>''',
'''<p><b>Then the problem the week actually has to solve.</b> Take away the VFI and you owe an account of what replaces it, or the objection from week 5 comes straight back: if any values are allowed, anybody can claim their own, and there is nothing left to argue with.</p>
    </div>

    ''' + dia + '''

    <div class="body">
      <p><b>Three attempts to pay that debt, and the third one changes the subject.</b></p>
      <ol>
        <li><b>The value-management model.</b> Any values may enter, provided the community is diverse enough and critical enough to catch the ones doing damage. Values get <em>managed</em>. This is Longino's four norms from week 6, now used as a political proposal.</li>
        <li><b>The social justice model.</b> Management alone assumes a level field that does not exist. Publicly funded science should have an aim, and the aim is to benefit everyone and especially the worst off. This one <b>picks</b> values where the first only manages them.</li>
        <li><b>Giordano's question, which neither of the other two asks.</b> Both answers are arguments conducted among academics about how academics should behave. Look instead at people outside universities who have produced real knowledge, the Black Panther clinics, the women's health movement, the AIDS activists who rewrote how drug trials run, and the question stops being which values scientists should hold and becomes <b>who counts as a scientist at all.</b></li>
      </ol>
    </div>''')

# ---------------- 15.1, a chronology written as paragraphs ----------------
sub('''<p><b>The answer is yes, and hormone replacement therapy is the case.</b> Here it is in order.</p>
            <p><b>From the 1940s, HRT became the standard treatment</b> for the symptoms of menopause: hot flushes, night sweats, broken sleep. Uncontroversial so far.</p>
            <p><b>In 1966 a physician named Robert Wilson published a bestseller called <em>Feminine Forever</em></b>, and prescriptions jumped. His claim was larger than symptom relief. HRT would <b>reverse or prevent</b> menopause and <b>preserve femininity</b>: more sexual drive, less vaginal dryness, and skin that did not age or droop.</p>
            <p><b>By the 1980s and 1990s the claims had grown again.</b> HRT was being described as safe, effective, and protective against cardiovascular disease, osteoporosis and some cancers.</p>
            <p><b>In 2002 one of the largest randomised trials ever run reported.</b> The Women's Health Initiative found that HRT, in some forms and in some women, <b>raised</b> the risk of breast cancer, heart disease, stroke and clots.</p>
            <p><b>And the sentence that makes it a philosophy case.</b> Some argued the result should have surprised nobody, because there had been warnings for decades that the evidence for the benefits was thin and that evidence of risk existed.</p>
            <p><b>So where exactly did the value judgments get in?</b> Intemann names three, and they are three different kinds.</p>''',
'''<p><b>The answer is yes, and hormone replacement therapy is the case.</b> Here it is in order.</p>
          </div>

          <div class="scroller">
            <table class="nine">
              <thead><tr><th>When</th><th>What was claimed</th></tr></thead>
              <tbody>
                <tr><td>From the 1940s</td>
                  <td>HRT becomes the standard treatment for the symptoms of menopause: hot flushes, night sweats, broken sleep. Uncontroversial so far.</td></tr>
                <tr><td>1966<span>the book</span></td>
                  <td>A physician named Robert Wilson publishes a bestseller, <em>Feminine Forever</em>, and prescriptions jump. His claim is larger than symptom relief: HRT would <b>reverse or prevent</b> menopause and <b>preserve femininity</b>, meaning more sexual drive, less vaginal dryness, and skin that did not age or droop.</td></tr>
                <tr><td>1980s and 1990s</td>
                  <td>The claims grow again. HRT is described as safe, effective, and protective against cardiovascular disease, osteoporosis and some cancers.</td></tr>
                <tr><td>2002<span>the trial</span></td>
                  <td>One of the largest randomised trials ever run reports. The Women's Health Initiative finds that HRT, in some forms and in some women, <b>raised</b> the risk of breast cancer, heart disease, stroke and clots.</td></tr>
              </tbody>
            </table>
          </div>

          <div class="body">
            <p><b>And the sentence that makes it a philosophy case.</b> Some argued the result should have surprised nobody, because there had been warnings for decades that the evidence for the benefits was thin and that evidence of risk existed.</p>
            <p><b>So where exactly did the value judgments get in?</b> Intemann names three, and they are three different kinds.</p>''')

sub('''<p><b>Nobody in this story is a villain</b>, which is the point. The chapter's claim is that careful people following the rules produced this, so stricter rules are not the fix.</p>
          </div>''',
'''</div>

          <div class="keep">
            <b>Nobody in this story is a villain</b>
            That is the point of telling it. Careful people following the rules produced sixty years
            of this, so stricter rules cannot be the fix.
          </div>''')

# ---------------- 15.5 ----------------
sub('''Intemann presents it as an addition to the first model, and never a rival to it.''',
    '''Intemann presents it as an addition to the first model, on top of it rather than against it.''')
sub('''<p><b>The method attached to it has a name you should keep.</b> <b>Studying up</b>, or studying from the margins out. In practice that means working with members of the affected group to frame the problem, identifying everyone affected, asking whether the usual concepts serve all of them, investigating how the problem shows up differently for different groups, and asking how systems of power contribute to it.</p>''',
'''<p><b>The method attached to it has a name you should keep: studying up</b>, or studying from the margins out. Five things it asks of a researcher:</p>
            <ol>
              <li>Work with members of the affected group to <b>frame the problem</b>.</li>
              <li>Identify everyone the problem affects.</li>
              <li>Ask whether the field's usual concepts serve all of them.</li>
              <li>Investigate how the problem shows up differently for different groups.</li>
              <li>Ask how systems of power contribute to it.</li>
            </ol>''')
sub('''<p><b>And she does not pretend it is finished.</b> Three questions she poses and leaves open: are there competing conceptions of justice, and what if they conflict? Should <em>all</em> research aim at it, or can research be worth doing without advancing it? And how is it applied to a concrete decision?</p>''',
'''<p><b>And she does not pretend it is finished.</b> Three questions she poses and leaves open:</p>
            <ol>
              <li>Are there competing conceptions of justice, and what happens when they conflict?</li>
              <li>Should <em>all</em> research aim at it, or can research be worth doing without advancing it?</li>
              <li>How is any of it applied to a concrete decision?</li>
            </ol>''')

open(f,'w',encoding='utf-8').write(h)
print('ok')
