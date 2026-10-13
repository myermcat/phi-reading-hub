import re
f='week-6/index.html'; h=open(f,encoding='utf-8').read()
def sub(old,new):
    global h
    assert old in h, 'MISS: '+old[:80]
    h = h.replace(old,new,1)

# ---- 20.2 : move the peacock up to the paragraph it illustrates, list the two processes,
#             split the long Darwin-on-women paragraph, lift Hubbard's line out
import sys; sys.path.insert(0, '_claude')
from figmove import cut
h, peacock = cut(h, 'img/peacock.jpg')

sub('''<b>So why has natural selection permitted it?</b></p>
            <p><b>Darwin's patch: sexual selection.</b> These traits are not about surviving, they are about <b>reproducing</b>, and survival is necessary for evolution without being sufficient. His definition from <em>The Descent of Man</em>, 1871: the advantage which certain individuals have over others of the same sex and species, in exclusive relation to reproduction. It works by two processes: <b>males compete with each other for access to females</b>, and <b>females choose</b>. Large size helps with the first, bright colour with the second, and the tail is explained.</p>
            <p><b>Then the part that has nothing to do with tails.</b> Darwin did not give human females mate choice, saying men make those choices, and Nelson traces the reasoning to Victorian England and to views about the sexes going back to Aristotle. He also claimed sex differences in behaviour and psychology: males <b>generally eager to mate with any female</b>, females less eager and, in the <em>Descent</em>, <b>coy</b>. And he attributed to males stronger passions, higher intelligence, greater strength, better senses and better movement, caused by the selection pressures he thought they alone faced: competing for mates, providing and protecting, defending the community. Women have some of these qualities, he allowed, to a far lesser degree, <b>and only because they inherit them from men</b>.</p>
            <p><b>Ruth Hubbard's line, which is the one to remember.</b> On Darwin's account women have enjoyed <b>a free evolutionary ride on the backs of their male conspecifics</b>.</p>
          </div>''',
'''<b>So why has natural selection permitted it?</b></p>
          </div>

          ''' + peacock + '''

          <div class="body">
            <p><b>Darwin's patch: sexual selection.</b> These traits are about <b>reproducing</b> where natural selection was about surviving, and survival is necessary for evolution without being sufficient. His definition from <em>The Descent of Man</em>, 1871: the advantage which certain individuals have over others of the same sex and species, in exclusive relation to reproduction. It works by two processes:</p>
            <ol>
              <li><b>Males compete with each other</b> for access to females. Large size helps here.</li>
              <li><b>Females choose.</b> Bright colour helps here, and the tail is explained.</li>
            </ol>
            <p><b>Then the part that has nothing to do with tails.</b> Darwin did not give human females mate choice, saying men make those choices, and Nelson traces the reasoning to Victorian England and to views about the sexes going back to Aristotle. He also claimed sex differences in behaviour and psychology: males <b>generally eager to mate with any female</b>, females less eager and, in the <em>Descent</em>, <b>coy</b>.</p>
            <p><b>And a list of male advantages with a cause attached.</b> Stronger passions, higher intelligence, greater strength, better senses and better movement, all caused by the selection pressures he thought males alone faced: competing for mates, providing and protecting, defending the community. Women have some of these qualities, he allowed, to a far lesser degree, <b>and only because they inherit them from men</b>.</p>
          </div>

          <div class="keep">
            <b>Ruth Hubbard's line, which is the one to remember</b>
            On Darwin's account women have enjoyed a free evolutionary ride on the backs of their male
            conspecifics.
          </div>''')

sub('''were not needed to solve the peacock problem at all and <b>track the social views of the time, and not the biology</b>.''',
    '''were not needed to solve the peacock problem at all, and <b>they track the social views of the time far more closely than they track the biology</b>.''')

sub('''<p><b>Three objections Nelson reports, and the first two are empirical.</b> Males of many species produce accessory secretions as well as sperm. High sperm production is generally needed for insemination to work at all. In humans and others, males produce millions of sperm per egg. <b>A proper accounting of investment would have to count these.</b> Third, and this is the gendered-metaphor point from her own list: <b>investment</b>, <b>cheap</b> and <b>expensive</b> are economic terms applied to biology, and they smuggle a conclusion in with the vocabulary.</p>''',
'''<p><b>Three objections Nelson reports, and the first two are empirical.</b></p>
            <ol>
              <li><b>Males contribute more than sperm.</b> Males of many species produce accessory secretions as well, and <b>a proper accounting of investment would have to count them</b>.</li>
              <li><b>Sperm is not cheap in bulk.</b> High sperm production is generally needed for insemination to work at all, and in humans and others males produce millions of sperm per egg.</li>
              <li><b>The words are doing the arguing.</b> This is the gendered-metaphor fault from her own list: <b>investment</b>, <b>cheap</b> and <b>expensive</b> are economic terms applied to biology, and they smuggle a conclusion in with the vocabulary.</li>
            </ol>''')

# ---- 20.3 : move the baboon portrait up, list the three findings
h, baboon = cut(h, 'img/baboon.jpg')

sub('''<p><b>What they said was in it.</b> Irven DeVore and Sherwood Washburn argued <b>male dominance</b> was the most important feature of baboon social structure, organising and controlling the group the way political leadership does in human societies. Alongside it came a <b>division of labour by sex</b>: males provide, protect and maintain the structure that benefits everyone, females take primary responsibility for the young. And <b>male aggression</b> was recorded as a trait and attributed to men as well.</p>''',
'''</div>

          ''' + baboon + '''

          <div class="body">
            <p><b>Three things Irven DeVore and Sherwood Washburn said were in the pattern.</b></p>
            <ol>
              <li><b>Male dominance</b>, which they called the most important feature of baboon social structure, organising and controlling the group the way political leadership does in human societies.</li>
              <li><b>A division of labour by sex.</b> Males provide, protect and maintain the structure that benefits everyone, while females take primary responsibility for the young.</li>
              <li><b>Male aggression</b>, recorded as a trait of the species and attributed to men as well.</li>
            </ol>''')

# ---- 20.4 : two debates, so two headings
sub('''<h4 id="nelson-4" data-n="20.4">The argument about what all this proves</h4>
          <div class="body">
            <p><b>First debate: was the old research simply bad science?</b> If it was, feminist critique tells you nothing about how science works, only that these particular people were careless. <b>Nelson says no, and this is the most important sentence in the chapter.</b> The studies were in keeping with the accepted hypotheses, priorities, methods and norms of their fields. The scientists gave the evidence they recognised its due. The feminist claim is that <b>there was more and different evidence to be considered</b>.</p>
            <p><b>Second debate: did feminism actually cause the change?</b> Two rival explanations are on offer. That science simply <b>self-corrects</b>. Or that it was <b>coincidence</b> that women influenced by the women's movement arrived in these fields just as the thinking about gender changed.</p>
            <p><b>Hrdy on the coincidence story, and it is a good line.</b> She seriously questions whether chance or sequence caused a small group of primatologists in the 1960s, who happened to be mostly male, to focus on male competition and on how many matings a male achieved, while a later group including many women, from the 1970s, shifted the focus to female behaviours with long-term consequences for infants.</p>
            <p><b>And the serious reply to the self-correction story.</b> Theories do change in the face of new evidence, so the mechanism is real. But in these cases <b>it was not the people who built the androcentric hypotheses who eventually saw the problem</b>. It was the new arrivals. And biologists including Altmann and Hrdy say in their own words that feminism is what let them see it.</p>
            <p><b>The complication Nelson states against her own case.</b> There are women in evolutionary biology, developmental biology and primatology who accept that their fields changed and <b>reject any role for feminism in it</b>. Linda Fedigan's explanation is that many primatologists, women included, see feminism as outside science, where it could be within it, and still treat it as a purely political perspective incompatible with doing science well.</p>
          </div>''',
'''<h4 id="nelson-4" data-n="20.4">The argument about what all this proves</h4>

          <h5>First debate: was the old research simply bad science?</h5>
          <div class="body">
            <p><b>What hangs on the answer.</b> If it was bad science, feminist critique tells you nothing about how science works, only that these particular people were careless. The studies were in keeping with the accepted hypotheses, priorities, methods and norms of their fields, and the scientists gave the evidence they recognised its due.</p>
          </div>

          <div class="keep">
            <b>Nelson's answer, and it is the most important sentence in the chapter</b>
            The work was not careless. There was more evidence, and different evidence, to be
            considered.
          </div>

          <h5>Second debate: did feminism actually cause the change?</h5>
          <div class="body">
            <p><b>Two rival explanations are on offer, and both deny feminism any credit.</b></p>
            <ol>
              <li><b>Science self-corrects.</b> New evidence would have overturned the androcentric hypotheses sooner or later, whoever was in the room.</li>
              <li><b>Coincidence.</b> Women influenced by the women's movement happened to arrive in these fields just as the thinking about gender was changing anyway.</li>
            </ol>
            <p><b>Hrdy on the coincidence story, and it is a good line.</b> She seriously questions whether chance or sequence caused a small group of primatologists in the 1960s, who happened to be mostly male, to focus on male competition and on how many matings a male achieved, while a later group including many women, from the 1970s, shifted the focus to female behaviours with long-term consequences for infants.</p>
            <p><b>And the serious reply to the self-correction story.</b> Theories do change in the face of new evidence, so the mechanism is real. In these cases, though, the people who built the androcentric hypotheses were never the ones who saw the problem. The new arrivals were. And biologists including Altmann and Hrdy say in their own words that feminism is what let them see it.</p>
          </div>

          <div class="keep">
            <b>The complication Nelson states against her own case</b>
            There are women in evolutionary biology, developmental biology and primatology who accept
            that their fields changed and reject any role for feminism in it. Linda Fedigan's
            explanation is that many primatologists, women included, see feminism as something outside
            science, and treat it as a purely political perspective incompatible with doing science
            well.
          </div>''')

sub('''because that is what makes the case bear on how science works, and not merely on how these people worked.''',
    '''because that is what makes the case bear on how science works at all, over and above how these particular people worked.''')

open(f,'w',encoding='utf-8').write(h)
print('ok')
