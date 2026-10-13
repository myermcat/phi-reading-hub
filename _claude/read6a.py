import re
f='week-6/index.html'; h=open(f,encoding='utf-8').read()
def sub(old,new):
    global h
    assert old in h, old[:70]
    h = h.replace(old,new,1)

# 4.5 an announced count of two, written as one paragraph
sub('''<p><b>Two objections the chapter reports, with the replies.</b> That the account is too inclusive, letting in people who reject the norms themselves, and that answering every criticism would consume all a scientist's time. Kristina Rolin answers both: the four norms rule out anyone who will not keep them, and the norms oblige the <b>community</b> to respond, never each individual, so the work can be divided.</p>''',
'''<p><b>Two objections the chapter reports, and Kristina Rolin answers both.</b></p>
            <ol>
              <li><b>It lets in too many people</b>, including people who reject the norms themselves. Rolin's reply: the four norms already rule out anyone who will not keep them.</li>
              <li><b>It costs too much.</b> Answering every criticism would take all of a scientist's time. Rolin's reply: the norms put the duty to respond on the <b>community</b>, so its members can divide the work.</li>
            </ol>''')

# 4.7 five virtues buried in a comma string
sub('''<p><b>So she makes it mean something.</b> Objectivity belongs to <b>knowledge claims</b> and not to researchers, and a claim is objective to the degree it shows the <b>epistemic virtues</b>, meaning the properties that make a claim good as knowledge. The standard list, from Kuhn and from Longino: <b>empirical adequacy</b> (it fits the data), <b>inferential robustness</b> (the conclusion survives changes in assumptions), <b>explanatory power</b>, <b>internal coherence</b>, and <b>consistency with other established knowledge</b>.</p>''',
'''<p><b>So she makes it mean something.</b> Objectivity is a property of the <b>knowledge claim</b> itself, where the tradition hung it on the researcher. A claim is objective to the degree it shows the <b>epistemic virtues</b>, meaning the properties that make a claim good as knowledge. The standard list comes from Kuhn and from Longino.</p>
            <ul>
              <li><b>Empirical adequacy.</b> It fits the data.</li>
              <li><b>Inferential robustness.</b> The conclusion survives a change in the assumptions it was drawn from.</li>
              <li><b>Explanatory power.</b> It accounts for more of what needed accounting for.</li>
              <li><b>Internal coherence.</b> Its parts agree with each other.</li>
              <li><b>Consistency with other established knowledge.</b> It sits with what the field already holds.</li>
            </ul>''')

# 4.6 seven flat paragraphs, which is the block the rules are written about
OLD6_A = '''<p><b>Why that is more than a nice idea.</b> Two mechanisms, and both are concrete. A person inside the dominant framework cannot see its assumptions, because they are what seeing is done with. And marginalised knowers can state their own interests, so they can propose different accounts of what the object of study even is.</p>
            <p><b>The term for the mechanism.</b> <b>Outsider-within</b>, from Patricia Hill Collins: a researcher who is marginalised holds both the field's own framework and the lived experience of the people being studied. <b>Double consciousness</b> is seeing yourself through the dominant culture's eyes and through your own at once, and it is what makes the mismatch visible.</p>
            <p><b>The guard rail, and it is the sentence that saves the theory from being silly.</b> <b>Epistemic advantage is not automatic.</b> It does not come from identity or social position by itself. It comes from <b>conscious awareness of the power relations that make up that position</b>. Being a woman does not give you the standpoint; understanding how gender structures the field does.</p>
            <p><b>Two sociologists as worked cases.</b> <b>Dorothy Smith</b> found a mismatch between her subjects' lived experience and the concepts of traditional sociology, called those mismatches <b>lines of fault</b>, and urged treating them as the place to rebuild the method. <b>Patricia Hill Collins</b> found that neither mainstream sociology nor white feminist accounts fitted the Black women she studied, which is how standpoint theory leads into intersectional analysis, where it might merely have tolerated it.</p>
            <p><b>And the definition to write down.</b> <b>Weak objectivity</b> means meeting the traditional empiricist standards of evidence, which covers phases 3 to 7. <b>Strong objectivity</b> means scrutinising <em>all</em> the phases, including whether the subject and the questions suit the goals of the research, and for Harding those goals include the liberatory aims of feminism. Her own summary: strong objectivity requires that scientists and their communities be integrated into democracy-advancing projects for scientific and epistemological reasons as well as moral and political ones.</p>'''

NEW6_A = '''<p><b>Why that is more than a nice idea.</b> Two mechanisms carry it, and both are concrete.</p>
            <ol>
              <li><b>You cannot see what you are seeing with.</b> A person inside the dominant framework cannot inspect its assumptions, because those assumptions are the instrument.</li>
              <li><b>Marginalised knowers can state their own interests</b>, so they can propose a different account of what the object of study even is.</li>
            </ol>
          </div>

          <dl class="facts">
            <dt>Outsider-within</dt>
            <dd>Patricia Hill Collins's term for a researcher who is marginalised and so holds <b>two things at once</b>: the field's own framework, and the lived experience of the people the field is studying.</dd>
            <dt>Double consciousness</dt>
            <dd>Seeing yourself through the dominant culture's eyes and through your own <b>at the same time</b>. It is what makes the mismatch between the two visible.</dd>
          </dl>

          <div class="keep">
            <b>The sentence that saves the theory from being silly</b>
            Epistemic advantage is not automatic. It does not come from identity or social position by
            itself. It comes from conscious awareness of the power relations that make up that position.
            Being a woman does not give you the standpoint; understanding how gender structures the
            field does.
          </div>

          <div class="body">
            <p><b>Two sociologists as worked cases.</b></p>
            <ol>
              <li><b>Dorothy Smith</b> found a mismatch between her subjects' lived experience and the concepts of traditional sociology. She called those mismatches <b>lines of fault</b>, and argued they are where the method should be rebuilt from.</li>
              <li><b>Patricia Hill Collins</b> found that neither mainstream sociology nor white feminist accounts fitted the Black women she studied. That is how standpoint theory leads into intersectional analysis, where a weaker version of it would merely have tolerated it.</li>
            </ol>
            <p><b>And the definition to write down.</b> The two words are the examinable pair in this section.</p>
          </div>

          <div class="scroller">
            <table class="nine">
              <thead><tr><th>Which objectivity</th><th>What it asks of the research</th><th>Which phases it covers</th></tr></thead>
              <tbody>
                <tr><td><b class="tag t3">Weak</b></td>
                  <td>Meet the traditional empiricist standards of evidence.</td>
                  <td>Phases 3 to 7, collecting through concluding</td></tr>
                <tr><td><b class="tag t1">Strong</b></td>
                  <td>Scrutinise all of them, including whether the subject and the questions suit the goals of the research. For Harding those goals include the liberatory aims of feminism.</td>
                  <td>All nine, and the aims behind them</td></tr>
              </tbody>
            </table>
          </div>

          <div class="body">
            <p><b>Harding's own summary of the second one.</b> Strong objectivity requires that scientists and their communities be integrated into democracy-advancing projects, for scientific and epistemological reasons as well as moral and political ones.</p>'''
sub(OLD6_A, NEW6_A)

open(f,'w',encoding='utf-8').write(h)
print('ok')
