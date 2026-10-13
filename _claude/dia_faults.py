"""Nelson's four faults, with the case in her own chapter where each one shows up.

A comparison across cases, which is what earns a drawing. The checklist is the reusable thing in
the chapter and the two case studies are where it gets used, so the drawing is the join.
"""
f='week-6/index.html'; h=open(f,encoding='utf-8').read()

CSS_AT = '  figure.dia svg[aria-labelledby="dg-five"] { min-width: 660px; }'
if CSS_AT not in h:
    CSS_AT = [l for l in h.split('\n') if 'figure.dia svg[aria-labelledby=' in l][-1]
h = h.replace(CSS_AT, CSS_AT + '\n  figure.dia svg[aria-labelledby="dg-faults"] { min-width: 660px; }', 1)

ROWS = [
 ('Androcentrism', 'Male-centredness. Research takes', 'what males do as the main thing', 'to study and lets the rest go.',
  'The baboon reports, built on', 'male dominance, with what the', 'females did never recorded.'),
 ('Gender stereotypes', 'A characteristic attributed to', 'every member of a group when it', 'is untrue of many of them.',
  'Darwin&#8217;s eager males and coy', 'females. Females tied to', 'reproduction, so left unstudied.'),
 ('Gendered metaphors', 'Fine while everybody remembers', 'they are metaphors. The fault is', 'letting one do the arguing.',
  'Sperm is cheap and eggs are', 'expensive, which settles the', 'question it was meant to raise.'),
 ('Background assumptions', 'Longino&#8217;s, and not originally', 'feminist: Hempel said in the 1960s', 'that unexamined ones mislead.',
  'That a female and her young', 'need help from a male, which', 'fieldwork keeps contradicting.'),
]

y, parts = 30, []
parts.append('<text class="dg-m dg-dim" x="12" y="17" font-size="11">THE FAULT</text>')
parts.append('<text class="dg-m dg-dim" x="186" y="17" font-size="11">WHAT IT IS</text>')
parts.append('<text class="dg-m dg-dim" x="446" y="17" font-size="11">WHERE IT SHOWS UP HERE</text>')
for i, (name, a1, a2, a3, b1, b2, b3) in enumerate(ROWS):
    hi = ' dg-hi' if i == 3 else ''
    parts.append('<rect class="dg-box%s" x="8" y="%d" width="644" height="74" rx="3"/>' % (hi, y))
    parts.append('<text class="dg-t" x="18" y="%d" font-size="13" font-weight="600">%d &nbsp;%s</text>' % (y+26, i+1, name))
    for k, line in enumerate((a1, a2, a3)):
        parts.append('<text class="dg-t" x="186" y="%d" font-size="12.5">%s</text>' % (y+24+k*17, line))
    for k, line in enumerate((b1, b2, b3)):
        parts.append('<text class="dg-t" x="446" y="%d" font-size="12.5">%s</text>' % (y+24+k*17, line))
    y += 80

FIG = '''
          <figure class="dia">
            <div class="draw">
            <svg viewBox="0 0 660 %d" role="img" aria-labelledby="dg-faults" style="font-family:var(--body)">
              <title id="dg-faults">Nelson's four faults to look for in biological research, each with what it means and the place in her own chapter where it turns up.</title>
              %s
            </svg>
            </div>
            <figcaption><b>The checklist, and the chapter using it on itself.</b> The first three are the ones to carry into any piece of research, and the right column shows that the two case studies below are the same four faults twice over. The fourth is highlighted because it is the one that is not feminist in origin and the one the other three reduce to: a male-centred question, a stereotype and a metaphor are all background assumptions that nobody examined. Hempel was making the argument in the 1960s with no feminism in it at all, which is the reply to anybody who says the critique is political before it is epistemic.</figcaption>
          </figure>
''' % (y + 8, '\n              '.join(parts))

ANCHOR = '<h4 id="nelson-2" data-n="20.2">'
assert ANCHOR in h
h = h.replace(ANCHOR, FIG + '\n          ' + ANCHOR, 1)
open(f, 'w', encoding='utf-8').write(h)
print('diagram added, height %d' % (y + 8))
