"""The five places a value gets in, against week 6's nine phases.

A comparison across cases, which is what earns a drawing: the reader sees that this week's five
and last week's nine are the same chain cut differently, which no caption carries.
"""
f='week-7/index.html'; h=open(f,encoding='utf-8').read()

CSS_AT = '  figure.dia svg[aria-labelledby="dg-three7"] { min-width: 700px; }'
assert CSS_AT in h
h = h.replace(CSS_AT, CSS_AT + '\n  figure.dia svg[aria-labelledby="dg-five7"] { min-width: 660px; }', 1)

ROWS = [
 ('1', 'Framing the', 'research problem',
      'Contraceptive research', 'aimed at women, so women', 'carry the risk.',
      'Phases 1 and 2', 'subject, question'),
 ('2', 'Observing and', 'describing',
      'The passive egg and the', 'burrowing sperm, in every', 'textbook.',
      'Phases 3 and 4', 'what counts, collecting'),
 ('3', 'A concept that', 'carries a value',
      'Harm to children of divorce.', 'Safety in home birth.', 'Male mice only.',
      'Phase 3', 'what counts as data'),
 ('4', 'Choosing the', 'model',
      'A model keeps some features', 'and drops others, so building', 'one decides what matters.',
      'Phase 5', 'interpreting'),
 ('5', 'Interpreting, and', 'weighing alternatives',
      'How much evidence is enough,', 'and which rival explanations', 'came to mind.',
      'Phases 6 to 8', 'inductive risk'),
]

y, parts = 30, []
parts.append('<text class="dg-m dg-dim" x="12" y="17" font-size="11">WHERE IT GETS IN</text>')
parts.append('<text class="dg-m dg-dim" x="214" y="17" font-size="11">THE CASE TO QUOTE</text>')
parts.append('<text class="dg-m dg-dim" x="478" y="17" font-size="11">WEEK 6&#8217;S CHAIN</text>')
for n, a1, a2, b1, b2, b3, c1, c2 in ROWS:
    hi = ' dg-hi' if n == '3' else ''
    parts.append('<rect class="dg-box%s" x="8" y="%d" width="644" height="74" rx="3"/>' % (hi, y))
    parts.append('<text class="dg-t" x="18" y="%d" font-size="13" font-weight="600">%s &nbsp;%s</text>' % (y+24, n, a1))
    parts.append('<text class="dg-t" x="18" y="%d" font-size="13" font-weight="600">&nbsp; &nbsp; %s</text>' % (y+42, a2))
    for k, line in enumerate((b1, b2, b3)):
        parts.append('<text class="dg-t" x="214" y="%d" font-size="12.5">%s</text>' % (y+24+k*17, line))
    parts.append('<text class="dg-t" x="478" y="%d" font-size="12.5" font-weight="600">%s</text>' % (y+24, c1))
    parts.append('<text class="dg-t dg-dim" x="478" y="%d" font-size="12">%s</text>' % (y+42, c2))
    y += 80

FIG = '''
          <figure class="dia">
            <div class="draw">
            <svg viewBox="0 0 660 %d" role="img" aria-labelledby="dg-five7" style="font-family:var(--body)">
              <title id="dg-five7">The five places a value enters research, each with the case the chapter uses, set against the phases of the research chain from week 6.</title>
              %s
            </svg>
            </div>
            <figcaption><b>The same chain as last week, cut into five instead of nine.</b> Week 6 asked where in research a value can enter and answered with nine decision points. This chapter asks the same question of the same chain and groups it differently, which is why the right column is worth reading across: anything in it you already know. The third row is highlighted because it is the one with no equivalent in week 6, where the value is inside the concept being measured and no amount of care at later phases removes it. Harm, safety and a standard laboratory animal are all decided before any data exists.</figcaption>
          </figure>
''' % (y + 8, '\n              '.join(parts))

ANCHOR = '''<p><b>The answer is five places, and this is the list to be able to produce.</b> Each comes with a case, and the case is where the argument is.</p>
          </div>
'''
assert ANCHOR in h, 'anchor'
h = h.replace(ANCHOR, ANCHOR + FIG, 1)
open(f, 'w', encoding='utf-8').write(h)
print('diagram added, height %d' % (y + 8))
