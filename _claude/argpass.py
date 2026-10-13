import re
f = 'week-6/index.html'
h = open(f, encoding='utf-8').read()

# ---- CSS: colour the lead-ins, and chips for the summary table
css_anchor = '  .rd .body > ol > li > b:first-child { color: var(--lead); }'
assert css_anchor in h
h = h.replace(css_anchor, css_anchor + '''
  .body > p > b:first-child { color: var(--lead); }
  .nine td:first-child .tag { display: inline-block; font-weight: 500; margin-bottom: 6px; }
  .tag.t1 { background: var(--close-wash); color: var(--close); }
  .tag.t2 { background: var(--skim-wash); color: var(--skim); }
  .tag.t3 { background: var(--curious-bg); color: var(--curious); }
  .keep + p, .scroller + .body { margin-top: 6px; }''', 1)

# ---- pull the three readings into a table above the prose
TABLE = '''
    <h3 class="sub">Three readings, two questions</h3>
    <p class="lede">Chapter 4 and chapter 5 ask opposite halves of the same thing, and Nelson runs both of them through one science.</p>
    <div class="scroller">
      <table class="nine">
        <thead>
          <tr><th>The reading</th><th>The question it asks</th><th>The case it runs on</th></tr>
        </thead>
        <tbody>
          <tr><td><b class="tag t1">Chapter 4</b><span>Crasnow and Intemann</span></td>
            <td>Where in a piece of research can a value get in, once you grant that method is supposed to keep it out?</td>
            <td>The rod and frame test, run on men and women from the 1950s to last year</td></tr>
          <tr><td><b class="tag t2">Chapter 5</b><span>Crasnow and Intemann</span></td>
            <td>How does not knowing something get produced, in the way a finding gets produced?</td>
            <td>Why there is still no hormonal contraceptive for men</td></tr>
          <tr><td><b class="tag t3">Nelson</b><span>Biology, 150 years</span></td>
            <td>What does one field look like after both of those questions have been running inside it for a century and a half?</td>
            <td>Darwin on the peacock, and who was watching the baboons</td></tr>
        </tbody>
      </table>
    </div>
'''

old_lede_end = 'and what happens to the things nobody went looking for.</p>\n'
assert old_lede_end in h
h = h.replace(old_lede_end, old_lede_end + TABLE, 1)

# ---- split the opening paragraph: the apparatus, then what it was used for
h = h.replace(
 'while sitting tilted in the dark with a stranger. From the 1950s to the 1970s researchers used this to test whether men have better spatial ability than women. <b>Men scored better, and the conclusion drawn was that male and female brains differ.</b> Versions of the test are still in use and papers from 2019 and 2022 still draw that conclusion.</p>',
 'while sitting tilted in the dark with a stranger.</p>\n      <p><b>From the 1950s to the 1970s this was a standard way of testing whether men have better spatial ability than women.</b> Men scored better, and the conclusion drawn was that male and female brains differ. Versions of the test are still in use, and papers from 2019 and 2022 still draw that conclusion.</p>', 1)
assert 'a standard way of testing' in h

# ---- the defence becomes a callout rather than one more paragraph
OLD_P3 = '<p><b>Now the defence this is aimed at.</b> Suppose you grant that scientists are ordinary people with ordinary opinions. The usual reply is that it does not matter, <b>because method sorts it out</b>: follow the procedure, run the controls, and whatever you personally believe is washed out by the time the result arrives. That is what a method is for.</p>'
assert OLD_P3 in h
h = h.replace(OLD_P3, '''<div class="keep">
        <b>The claim this week attacks</b>
        Grant that scientists are ordinary people carrying ordinary opinions. It still makes no difference
        to the finding, because method sorts it out: follow the procedure, run the controls, and whatever
        you personally believe has been washed out by the time the result arrives.
      </div>''', 1)

# ---- split chapter 5 at the worked case
h = h.replace(
 'is often a product, where it looks like a gap. The clearest case in the chapter: there is still no safe hormonal contraceptive for men.',
 'is often a product, where it looks like a gap.</p>\n      <p><b>The clearest case in the chapter is contraception.</b> There is still no safe hormonal contraceptive for men.', 1)
assert 'The clearest case in the chapter is contraception' in h

# ---- the closing paragraph becomes the takeaway block
OLD_P7 = '<p><b>And the sentence that ties this week to last week.</b> If a value can enter at any link in the chain, then <b>objectivity cannot mean a method anyone could run with the same result</b>, and it cannot mean a researcher with no commitments. Both of those are now off the table. The three names in chapter 4, Longino, Harding and Wylie, are three attempts to say what objectivity could mean instead, and all three move it off the individual.</p>'
assert OLD_P7 in h
h = h.replace(OLD_P7, '''<div class="keep">
        <b>What this leaves of objectivity</b>
        If a value can enter at any link in the chain, objectivity can no longer mean a method that anyone
        could run with the same result, and it can no longer mean a researcher who holds no commitments.
        Longino, Harding and Wylie are three attempts to say what it could mean instead, and all three
        move it off the individual.
      </div>''', 1)

# ---- the nine-phase diagram belongs under the paragraph that describes it
m = re.search(r'\n    <figure class="dia">\n.*?\n    </figure>\n(  </section>)', h, re.S)
assert m
fig = m.group(0)[:-len(m.group(1))]
h = h[:m.start()] + '\n  ' + m.group(1) + h[m.end():]

split_at = 'so nobody ruled it out.</b></p>\n'
assert split_at in h
h = h.replace(split_at, split_at + '    </div>\n' + fig.rstrip('\n') + '\n\n    <div class="body">\n', 1)

open(f, 'w', encoding='utf-8').write(h)
print('ok')
