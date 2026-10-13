f='week-7/index.html'; h=open(f,encoding='utf-8').read()
def sub(old,new):
    global h
    assert old in h, 'MISS: '+old[:80]
    h = h.replace(old,new,1)

# 19.3 the announced count has to match the list under it
sub('''<p><b>And the sentence that makes the argument serious.</b> The people making the decisions that reproduce an unequal society every day <b>are the best educated people in it.</b> So more education cannot be the whole answer. The alternatives she gathers are five:</p>
            <ul>
              <li><b>Unlearning</b>, <b>rewriting</b>, <b>unschooling</b>, <b>failure</b> and <b>illiteracy</b>, each of which she treats as a way of working that the deficit model has no room for.</li>
            </ul>''',
'''<p><b>And the sentence that makes the argument serious.</b> The people making the decisions that reproduce an unequal society every day <b>are the best educated people in it.</b> So more education cannot be the whole answer. She gathers five alternatives, each a way of working the deficit model has no room for.</p>
            <ol>
              <li>Unlearning</li>
              <li>Rewriting</li>
              <li>Unschooling</li>
              <li>Failure</li>
              <li>Illiteracy</li>
            </ol>''')

# 19.5 a correction somebody makes to their own side is a callout
sub('''<p><b>Then a correction she makes to her own side.</b> Harding defines democratising science as making sure that those who bear the consequences of science policy have a proportionate share in making it, so that <b>women's interests and values count</b>. Giordano accepts the sentiment and rejects the category: <b>treating women as a single group with shared interests has stood in for the interests of white middle-class women.</b></p>''',
'''</div>

          <div class="keep">
            <b>A correction she makes to her own side</b>
            Harding defines democratising science as making sure that those who bear the consequences
            of science policy have a proportionate share in making it, so that women's interests and
            values count. Giordano accepts the sentiment and rejects the category: treating women as a
            single group with shared interests has stood in for the interests of white middle-class
            women.
          </div>

          <div class="body">''')

# 3.5 her flattest line is the one to remember, so it stops being a clause
sub('''<p><b>First, why they are necessary.</b> Hypotheses are needed in all cases where the true reason for a phenomenon cannot be discovered <b>either in advance, from truths already known, or afterwards, from experiment.</b> That gap is permanent, so the tool is permanent. Her flat version: without hypotheses there would be no astronomy now.</p>''',
'''<p><b>First, why they are necessary.</b> Hypotheses are needed in all cases where the true reason for a phenomenon cannot be discovered <b>either in advance, from truths already known, or afterwards, from experiment.</b> That gap is permanent, so the tool is permanent.</p>
          </div>

          <div class="keep">
            <b>Her flat version of it</b>
            Without hypotheses there would be no astronomy now.
          </div>

          <div class="body">''')

open(f,'w',encoding='utf-8').write(h)
print('ok')
