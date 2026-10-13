import re
f='week-6/index.html'; h=open(f,encoding='utf-8').read()
i=h.find('<h4 id="ch5-4"')
j=h.find('<figure class="pic">', i)
assert 0 < i < j

NEW = '''<h4 id="ch5-4" data-n="5.4">The five ways ignorance gets made</h4>
          <div class="body">
            <p><b>Cutting across the five kinds, the chapter names five strategies.</b> These answer <em>how</em>, where the taxonomy answered <em>what</em>.</p>
          </div>

          <h5>1. Neglect, which is simply not studying something</h5>
          <div class="body">
            <p><b>Passive when a question never occurs to anyone, active when somebody chooses to look away.</b> Three cases from the chapter:</p>
            <ul>
              <li><b>Fossils in the ancient Mediterranean.</b> Adrienne Mayor shows the accounts existed. The history of science passed over them because scholars disregarded non-elite sources and filed them as folklore, <b>so modern palaeontologists were ignorant of the earliest fossil discoveries</b>.</li>
              <li><b>What the news covers.</b> Media choose which stories to run, which is part of why people on different news diets believe different things.</li>
              <li><b>Which parts of United States history get taught.</b> The chapter's longest case, and it notes that <b>neglect happens across the political spectrum</b>: the Democratic Party's 2016 decision to concentrate on urban and suburban voters left its own officials systematically ignorant about rural conditions.</li>
            </ul>
          </div>

          <h5>2. Suppression, where the knowledge exists and fails to travel</h5>
          <div class="body">
            <p><b>Four routes, and only the first is the obvious one.</b></p>
            <ul>
              <li><b>Active.</b> Bans on teaching certain topics, or classification of dangerous material.</li>
              <li><b>Scientific.</b> Data or methods are not shared, under commercial confidentiality or claimed national security.</li>
              <li><b>Chosen by the marginalised themselves.</b> Mayor records Native American groups withholding fossil knowledge from outsiders, and many Navajo avoiding anything to do with death, including dinosaur fossils on their land.</li>
              <li><b>Language and form.</b> Latin American feminist philosophy stays invisible to Anglophone scholars, and Indigenous oral histories get excluded as unreliable.</li>
            </ul>
            <p><b>And the fifth route, citation, which has the chapter's sharpest example.</b> Cuvier wrote up Iroquois and Delaware accounts of mastodon fossils, calling the mastodon the grandfather of the buffalo. <b>When his work was translated into English twenty years later that entire section was left out</b>, which made North American fossil discovery look European and fed the story that nobody was there before.</p>
          </div>

          <h5>3. Discrediting, which has two targets</h5>
          <div class="body">
            <p><b>Attacking the knowledge.</b> Indigenous and local knowledge gets dismissed as myth for not arriving as written-up hypotheses, despite Micronesian navigation systems, Indigenous pharmacology that was then exploited, and conservation findings repeatedly rediscovered from traditional ecological knowledge. The chapter names the assumption underneath this the <b>scientification of knowledge</b>: that only the products of Western science count. Midwives are the clearest case, their experiential knowledge dismissed as unscientific and unskilled as obstetrics professionalised in the nineteenth century, with licensing restrictions that still exist.</p>
            <p><b>The main technique is uncertainty, which is the tobacco strategy.</b> Executives knew they did not have to show smoking was safe, only that the science was unsettled. They funded conflicting research, exaggerated the uncertainties, and put non-scientists on television to attack the science.</p>
          </div>

          <dl class="facts">
            <dt>Think tank</dt>
            <dd>An organisation that employs researchers to publish reports and policy arguments, funded by whoever chose to fund it. <b>It has no students and no requirement to be peer reviewed</b>, and its output looks like scholarship, which is what makes it useful to somebody who wants a conclusion to appear independent.</dd>
          </dl>

          <div class="body">
            <p><b>Attacking the knower</b> works through dismissal for an irrelevant feature: Indigenous people as savages, women as incapable, and more subtly the senators who said they believed Christine Blasey Ford had been attacked while doubting her memory of by whom. It can also target institutions, since claims of fake news aim to leave people not knowing what to trust at all.</p>
          </div>

          <div class="keep">
            <b>The difficulty the chapter raises against itself</b>
            Discrediting mimics reasonable practice. It is often right to ask whether a witness is
            credible or an expert qualified, and their example of a fair challenge is Scott Atlas, a
            radiologist with no training in epidemiology, advising the White House on masks. Telling
            fair criticism from the other kind is genuinely hard, because people doing the second kind
            phrase it as the first, and the chapter says plainly that this needs more work.
          </div>

          <h5>4. Disinformation, meaning outright false claims</h5>
          <div class="body">
            <p><b>What is new is the speed and the scale.</b> Fabricated stories, sites and images spread worldwide in seconds and keep spreading after a platform flags them. Three things amplify it: lack of trust, social networks built on shared values, and algorithms that feed you what your clicks predict you will like. Add <b>confirmation bias</b>, the tendency to weight evidence that agrees with you, and you get information silos, echo chambers and what C. Thi Nguyen calls <b>epistemic bubbles</b>.</p>
          </div>

          <h5>5. Selective representation, which is the subtlest of the five</h5>
          <div class="body">
            <p><b>Misleading with things that are true.</b> Four cases, and the second is the one to remember:</p>
            <ul>
              <li><b>The party.</b> A teenager says there will be adult supervision and leaves out that the chaperone is a friend's twenty-one-year-old sibling.</li>
              <li><b>The drug.</b> A company reports that patients taking it for five years had a 95 per cent survival rate, and does not mention that the rate was also 95 per cent at two years, <b>so patients buy three extra years of a drug for nothing</b>.</li>
              <li><b>The heavy metals.</b> Chemical companies funded studies showing less testicular cancer in rats at low doses, implying low doses are good for men, while <b>never checking whether other cancers rose at the same doses</b>.</li>
              <li><b>Political advertising</b>, which does the same with quotations and voting records.</li>
            </ul>
          </div>

          '''
h = h[:i] + NEW + h[j:]
open(f,'w',encoding='utf-8').write(h)
print('ok')
