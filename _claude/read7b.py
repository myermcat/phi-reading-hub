f='week-7/index.html'; h=open(f,encoding='utf-8').read()
def sub(old,new):
    global h
    assert old in h, 'MISS: '+old[:80]
    h = h.replace(old,new,1)

# ---------------- 19.1 ----------------
sub('''<p><b>The assumption underneath, which has a name.</b> The <b>deficit model</b>: the public has a hole where knowledge should be, and filling it will produce support for science. Science studies has pushed against it for decades, which is where calls for <b>democratic science</b> come from.</p>
            <p><b>Where the demand came from historically, and this is the part worth holding on to.</b> It takes root after the Second World War, and it is tangled with <b>nationalism</b>. An assumption that science is good in itself did not survive the war. <b>Who controlled it mattered.</b> Giordano puts the asymmetry plainly: Germany could be condemned for unethical experimentation that harmed and killed millions, while the United States had to defend its use of the atomic bomb on hundreds of thousands. So the push for a scientifically literate public was about national pride and national security, and the worry about science in the <em>wrong hands</em> runs from Cold War politics into the war on terror and into bioethics today.</p>''',
'''</div>

          <dl class="facts">
            <dt>The deficit model</dt>
            <dd>The public has <b>a hole where knowledge should be</b>, and filling it will produce support for science. Science studies has pushed against this for decades, which is where calls for <b>democratic science</b> come from.</dd>
          </dl>

          <div class="body">
            <p><b>Where the demand came from historically, and this is the part worth holding on to.</b> It takes root after the Second World War, and it is tangled with <b>nationalism</b>. An assumption that science is good in itself did not survive the war. <b>Who controlled it mattered.</b></p>
          </div>

          <div class="keep">
            <b>The asymmetry Giordano puts plainly</b>
            Germany could be condemned for unethical experimentation that harmed and killed millions,
            while the United States had to defend its use of the atomic bomb on hundreds of thousands.
          </div>

          <div class="body">
            <p><b>So the push for a scientifically literate public was about national pride and national security</b>, and the worry about science in the <em>wrong hands</em> runs from Cold War politics into the war on terror and into bioethics today.</p>''')

# ---------------- 19.2 ----------------
sub('''<p><b>Her two cases.</b> A politics of <b>respectability</b>, meaning conformity to white, heterosexual, middle-class norms about how a woman behaves and what family she lives in, was used to justify withholding state support from poor Black women by blaming individuals or culture. And the campaign for same-sex marriage won healthcare benefits for couples with jobs that provide healthcare <b>while leaving marriage itself unquestioned</b>, so people without jobs or insurance stayed outside. The pattern both share: the boundary moved, and the people on the far side of the new one became harder to see.</p>''',
'''<p><b>Her two cases, and they share a pattern.</b></p>
            <ol>
              <li><b>Respectability.</b> Conformity to white, heterosexual, middle-class norms about how a woman behaves and what family she lives in. It was used to justify withholding state support from poor Black women, by blaming individuals or culture.</li>
              <li><b>Same-sex marriage.</b> The campaign won healthcare benefits for couples with jobs that provide healthcare, <b>while leaving marriage itself unquestioned</b>, so people without jobs or insurance stayed outside.</li>
            </ol>
            <p><b>In both, the boundary moved</b>, and the people on the far side of the new one became harder to see.</p>''')

# ---------------- 19.3 ----------------
sub('''<p><b>Her example of what happens to anybody who says this out loud.</b> During the Fees Must Fall protests in South Africa in 2016, a student suggested that science is a colonial project and should be abandoned before something new is built. The video went round under <b>#ScienceMustFall</b>. Giordano's point is about the response: the suggestion was <b>not argued with but used as evidence of ignorance</b>, and then used to discredit the whole movement.</p>
            <p><b>And the sentence that makes the argument serious.</b> The people making the decisions that reproduce an unequal society every day <b>are the best educated people in it.</b> So more education cannot be the whole answer, and the alternatives she gathers are unlearning, rewriting, unschooling, failure and illiteracy.</p>
            <p><b>What to do with this if you think it is wrong.</b> Her own footnote concedes the obvious objection: this is not a purist stance, and nobody is giving up medicine or phones. The claim is narrower, that in specific cases refusing the scientific framing is a legitimate move, and never a deficit. That narrow claim is the one to argue against if you want to, and <b>the broad version is one she does not make.</b></p>
          </div>''',
'''</div>

          <div class="exm">
            <b>Example &middot; what happens to anybody who says this out loud</b>
            <p><b>The event.</b> During the Fees Must Fall protests in South Africa in 2016, a student suggested that science is a colonial project and should be abandoned before something new is built. The video went round under <b>#ScienceMustFall</b>.</p>
            <p><b>Giordano's point is about the response.</b> Nobody argued with the suggestion. It was treated as evidence of ignorance, and then used to discredit the whole movement.</p>
          </div>

          <div class="body">
            <p><b>And the sentence that makes the argument serious.</b> The people making the decisions that reproduce an unequal society every day <b>are the best educated people in it.</b> So more education cannot be the whole answer. The alternatives she gathers are five:</p>
            <ul>
              <li><b>Unlearning</b>, <b>rewriting</b>, <b>unschooling</b>, <b>failure</b> and <b>illiteracy</b>, each of which she treats as a way of working that the deficit model has no room for.</li>
            </ul>
            <p><b>What to do with this if you think it is wrong.</b> Her own footnote concedes the obvious objection: this is no purist stance, and nobody is giving up medicine or phones. The narrow claim is that in specific cases refusing the scientific framing is a legitimate move. That narrow claim is the one to argue against if you want to, and <b>the broad version is one she does not make.</b></p>
          </div>''')

# ---------------- 19.5 ----------------
sub('''<p><b>And the argument she uses to make that stick.</b> Harriet Washington's <b>medical apartheid</b>: it is not that all women need including, it is that <b>some women, primarily Black women, have been used for the benefit of other women's health.</b> The separation was neither unfortunate nor accidental. Some bodies are undervalued so they can be used for the benefit of others. If that is right, then democratising science means counting the people whose bodies have been most subjected to the medical gaze, and not women in general.</p>''',
'''</div>

          <dl class="facts">
            <dt>Medical apartheid</dt>
            <dd>Harriet Washington's term, and the argument Giordano uses to make her correction stick. <b>Some women, primarily Black women, have been used for the benefit of other women's health.</b> The separation was neither unfortunate nor accidental: some bodies are undervalued so they can be used for the benefit of others.</dd>
          </dl>

          <div class="body">
            <p><b>What follows from that.</b> Democratising science means counting the people whose bodies have been most subjected to the medical gaze, where counting women in general would leave the arrangement exactly as it is.</p>''')

# ---------------- 3.2 ----------------
sub('''<div class="body">
            <p><b>The question she asks in the preface to her translation of Mandeville: why have women produced nothing?</b></p>
            <p><b>And her answer is that the question is the wrong way round.</b>''',
'''<div class="qa">
            <b>The question she asks in the preface to her translation of Mandeville</b>
            Why have women produced nothing?
          </div>

          <div class="body">
            <p><b>And her answer is that the question is the wrong way round.</b>''')

sub('''<p><b>What makes this more than a complaint.</b> She identifies a loop. The belief that women are naturally frivolous produces institutions that give women nothing to do with their minds, which produces women who have done nothing, which confirms the belief. <b>And she names the part done from inside</b>, where women take the prejudice on themselves and bury what they have.</p>
            <p><b>Then the generalisation, from her <em>Discourse on Happiness</em>.</b> A source of happiness is to be free of prejudice, and <b>the decision rests with us</b> to be rid of it. Her definition is the usable one: <b>prejudice is an opinion accepted without examination, because it would be indefensible otherwise.</b> We all have enough intelligence to examine what others want us to believe.</p>
          </div>''',
'''<p><b>What makes this more than a complaint: she identifies a loop, and it closes.</b></p>
            <ol>
              <li>The belief that women are naturally frivolous</li>
              <li>produces institutions that give women nothing to do with their minds,</li>
              <li>which produces women who have done nothing,</li>
              <li>which confirms the belief.</li>
            </ol>
            <p><b>And she names the part done from inside</b>, where women take the prejudice on themselves and bury what they have.</p>
            <p><b>Then the generalisation, from her <em>Discourse on Happiness</em>.</b> A source of happiness is to be free of prejudice, and <b>the decision rests with us</b> to be rid of it. We all have enough intelligence to examine what others want us to believe.</p>
          </div>

          <dl class="facts">
            <dt>Prejudice</dt>
            <dd>Her own definition, and the usable one: <b>an opinion accepted without examination, because it would be indefensible otherwise.</b></dd>
          </dl>''')

# ---------------- 3.4 ----------------
sub('''<p><b>Speculative natural philosophy</b> reasons from principles about how things must be. <b>Experimental natural philosophy</b> builds from experiment and observation. By the 1690s the experimental side had hardened into <b>opposition to hypotheses</b>, which is the part a modern reader finds strange.</p>''',
'''</div>

          <dl class="facts">
            <dt>Speculative natural philosophy</dt>
            <dd>Reasons from <b>principles about how things must be</b>.</dd>
            <dt>Experimental natural philosophy</dt>
            <dd>Builds from <b>experiment and observation</b>. By the 1690s this side had hardened into opposition to hypotheses altogether, which is the part a modern reader finds strange.</dd>
          </dl>

          <div class="body">''')

# ---------------- 3.5 ----------------
sub('''<p><b>And the argument from who used them.</b> Copernicus, Kepler, Huygens, Descartes, Leibniz <b>and Newton himself</b> all devised useful hypotheses to explain difficult phenomena, so those who want to ban them from philosophy <b>intend harm to the interests of science.</b> The target is anybody leaning too hard on Newton's famous line that he feigns no hypotheses.</p>''',
'''<p><b>And the argument from who used them.</b> Copernicus, Kepler, Huygens, Descartes, Leibniz <b>and Newton himself</b> all devised useful hypotheses to explain difficult phenomena.</p>
            <p><b>So, she says, those who want to ban them from philosophy intend harm to the interests of science.</b> Her target is anybody leaning too hard on Newton's famous line that he feigns no hypotheses.</p>''')

open(f,'w',encoding='utf-8').write(h)
print('ok')
