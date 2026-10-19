"""Week 7's argument section asked its question three times and answered it three times.

Tracing a reader through it: the question at the heading, again four paragraphs later, again
nine paragraphs after that. The answer stated, restated, then finally given as a list. The
value-free ideal defined twice. Roughly 700 words of circling before any content arrives, which
is why it reads as though nothing is happening. Every fix I made added a lap instead of
replacing one.

This is one pass: the rule, its death, the problem that creates, the three answers, the table,
and only then why the rule mattered politically.
"""
import re
f = 'week-7/index.html'
h = open(f, encoding='utf-8').read()

start = h.find('<section id="s-arg">')
end = h.find('<figure class="dia">', start)
assert 0 < start < end
old = h[start:end]

table = re.search(r'    <h3 class="sub">Four readings.*?\n    </div>\n', old, re.S)
assert table, 'table block'
TABLE = table.group(0)

JOBS = re.search(r'      <ol>\n        <li><b>It made diversity.*?\n      </ol>\n', old, re.S)
assert JOBS, 'three jobs list'

THREE = re.search(r'      <ol>\n        <li><b>The value-management model.*?\n      </ol>\n', h, re.S)
assert THREE, 'three attempts list'

NEW = '''<section id="s-arg">
    <h2>Values are in. So what stops anybody calling their politics science?</h2>
    <p class="lede">Week 7 inherits that question from week 6 and owes an answer to it.</p>

    <div class="keep">
      <b>The rule this week is dismantling</b>
      The value-free ideal, VFI for short. Social, moral and political values play no part in the
      core of science, meaning the part where you decide what counts as evidence, which theory the
      evidence supports, and what to accept. Heather Douglas calls that part the heart.
    </div>

    <div class="body">
      <p><b>Nobody ever claimed values are absent from science altogether.</b> Of course they decide
      what gets funded and what may be done to a research subject. A <b>value</b> here means a
      judgment about what matters that the data does not settle, like treating skin that ages as a
      health problem, or deciding this much evidence is enough to publish. The VFI is narrower and
      tougher: it says that once you are weighing evidence, values are out.</p>
      <p><b>Week 6 killed it.</b> Chapter 4 cut research into nine phases and found a person
      deciding at every one, with nothing in nature deciding for them, and twenty years of the rod
      and frame test is that happening in public, done by careful people following the rules.</p>
      <p><b>Which leaves this week holding the problem.</b> If values are in the core and cannot be
      scrubbed out, what stops a tobacco company or a creationist calling their politics science?
      That is <b>relativism</b>, the objection from week 5, and a week that removes a rule owes a
      replacement for it.</p>
      <p><b>Three attempts to pay that debt, and the third changes the subject.</b></p>
''' + THREE.group(0) + '''    </div>

''' + TABLE + '''
    <div class="body">
      <p><b>One thing left, and it is the part that makes this political.</b> The VFI was never only
      a bad description of science. Intemann's point, and what separates her chapter from an
      ordinary philosophy-of-science complaint, is that it was <b>doing a job</b>: it shut three
      arguments down without anybody having to answer them.</p>
''' + JOBS.group(0) + '''      <p><b>That is why feminists went after it, where noting it was inaccurate would have been
      enough for anybody else.</b> Non-feminist philosophers attacked it too, mostly for being
      unattainable. The feminist complaint is that it was an obstacle, useful for dismissing those
      three arguments without answering them.</p>
    </div>

'''
h = h[:start] + NEW + h[end:]
h = h.replace(THREE.group(0), '', 1) if h.count(THREE.group(0)) > 1 else h
open(f, 'w', encoding='utf-8').write(h)
print('rebuilt in one pass')
