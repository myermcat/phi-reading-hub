import re
f='week-6/index.html'; h=open(f,encoding='utf-8').read()
def sub(old,new):
    global h
    assert old in h, old[:80]
    h = h.replace(old,new,1)

i = h.find('<h4 id="ch4-3"')
j = h.find('<h4 id="ch4-4"')
assert 0 < i < j
OLD = h[i:j]

NEW = '''<h4 id="ch4-3" data-n="4.3">Walking the case down the chain</h4>
          <div class="body">
            <p><b>Run the rod and frame test down the nine phases and you can watch the conclusion being assembled.</b> Phases 1 and 2 were chapter 3's business. These are the six the authors say people fight about.</p>
            <ol>
              <li value="3"><b>Which observations count.</b> Researchers assumed the rod and frame test is a measure of visual-spatial ability. That assumption is the whole experiment, and nobody ever argued for it.</li>
              <li value="4"><b>Collecting.</b> They collected that men aligned the rod correctly more often. Correct, as far as it goes.</li>
              <li value="5"><b>Interpreting.</b> They read that as men having better spatial cognition. The authors make a point here worth copying: the researchers also shared the widely held belief that men and women differ cognitively, <b>which made that reading the easy one and every other reading the effortful one.</b></li>
              <li value="6"><b>When to stop.</b> The chapter's key term lives in this phase, and it gets its own treatment below. The short version is that the expected result made less evidence feel like enough.</li>
              <li value="7"><b>Concluding.</b> They concluded the difference could only be explained by biology. The authors call this unwarranted for a specific reason: <b>the differences are small, even where they are statistically significant.</b> Reporting the significance while leaving out the size is itself a choice about what matters.</li>
              <li value="8"><b>Alternatives, and this is the phase that does the damage.</b> Social and environmental explanations existed. So did experimental error, meaning the test measures assertiveness. Neither was ruled out, because <b>neither occurred to anybody.</b> Concluding means inferring to the best explanation, and you can only compare the explanations you have thought of, so <b>who is in the room changes how well supported the conclusion actually is.</b></li>
              <li value="9"><b>Robustness.</b> The missing alternatives point at <b>confounding variables</b>, meaning factors other than the one you are studying that move with the thing you are measuring. Name them and you can design controls for them. Later studies did, and the gap shrank.</li>
            </ol>
          </div>

          <h5>Phase 6 in detail, because the term here is the one to know</h5>
          <div class="body">
            <p><b>Deciding you have enough evidence is a judgment about the risk of being wrong, and that is called <b>inductive risk</b>.</b> How much evidence is enough depends on the probability the hypothesis is true <em>and</em> on what it would cost if you got it wrong. The second half is a value judgment. The authors run it both ways, which is what keeps it an argument:</p>
            <ul>
              <li><b>Wrongly accept that spatial ability is biologically fixed by sex</b>, and you reinforce a stereotype, which bears on whether girls are encouraged into mathematics, engineering and architecture. Those are well-paid fields, so the cost shows up in women's earnings. And because the stereotype is already everywhere, and people weight evidence that agrees with what they already think, the error spreads easily.</li>
              <li><b>Wrongly reject it when it is true</b>, and you lose the chance to understand a real difference and deal with it fairly, and you may back policies that cannot work.</li>
            </ul>
            <p><b>Which error is worse is a value judgment, and somebody makes it every time.</b> The practical rule the chapter offers: when the cost of error is high and nothing is urgent, collect more and avoid sweeping conclusions.</p>
          </div>

          <div class="keep">
            <b>Why this is not a story about bad scientists</b>
            In hindsight it is tempting to call this sloppy design, preconceptions and hasty
            conclusions. The authors refuse. These were peer-reviewed studies that still shape a live
            research field, and the two ways values entered, through inductive risk and through which
            alternatives come to mind, look like features of how knowledge gets produced at all. That
            is why the chapter cannot end by telling anybody to try harder.
          </div>

          '''
h = h[:i] + NEW + h[j:]
open(f,'w',encoding='utf-8').write(h)
print('ok')
