"""Three drawings for week 6, each one the claim rather than the subject."""
import re
f = 'week-6/index.html'
h = open(f, encoding='utf-8').read()

CSS_AT = '  figure.dia svg[aria-labelledby="dg-faults"] { min-width: 660px; }'
assert CSS_AT in h
h = h.replace(CSS_AT, CSS_AT
  + '\n  figure.dia svg[aria-labelledby="dg-frame"] { min-width: 600px; }'
  + '\n  figure.dia svg[aria-labelledby="dg-five-yr"] { min-width: 560px; }'
  + '\n  figure.dia svg[aria-labelledby="dg-gametes"] { min-width: 520px; }', 1)

# ---- 4.5 Longino: one number, two background assumptions -------------------
FRAME = '''
          <figure class="dia">
            <div class="draw">
            <svg viewBox="0 0 600 268" role="img" aria-labelledby="dg-frame" style="font-family:var(--body)">
              <title id="dg-frame">The same finding about housework placed under two different background assumptions, where it is a stray fact under the first and the central thing to be explained under the second.</title>
              <text class="dg-m dg-dim" x="12" y="16" font-size="11">THE FINDING, UNCHANGED</text>
              <rect class="dg-box" x="8" y="26" width="584" height="46" rx="3"/>
              <text class="dg-t" x="22" y="47" font-size="13.5" font-weight="600">When a woman out-earns her male partner, he does less housework than before.</text>
              <text class="dg-t dg-dim" x="22" y="64" font-size="12">Julie Brines, 1994</text>
              <path class="dg-ln" d="M150 78 L150 96 M450 78 L450 96" stroke-width="1.3"/>
              <rect class="dg-box" x="8" y="100" width="284" height="158" rx="3"/>
              <rect class="dg-box dg-hi" x="308" y="100" width="284" height="158" rx="3"/>
              <text class="dg-t dg-dim" x="22" y="120" font-size="11" style="font-family:var(--mono)">ASSUMPTION A</text>
              <text class="dg-t dg-dim" x="322" y="120" font-size="11" style="font-family:var(--mono)">ASSUMPTION B</text>
              <text class="dg-t" x="22" y="142" font-size="13" font-weight="600">A marriage is two people</text>
              <text class="dg-t" x="22" y="159" font-size="13" font-weight="600">bargaining over money.</text>
              <text class="dg-t" x="322" y="142" font-size="13" font-weight="600">A marriage is also</text>
              <text class="dg-t" x="322" y="159" font-size="13" font-weight="600">somewhere gender is performed.</text>
              <text class="dg-t" x="22" y="188" font-size="12.5">More earnings, more bargaining</text>
              <text class="dg-t" x="22" y="205" font-size="12.5">power, less housework. The finding</text>
              <text class="dg-t" x="22" y="222" font-size="12.5">runs the wrong way and connects</text>
              <text class="dg-t" x="22" y="239" font-size="12.5">to nothing.</text>
              <text class="dg-t" x="322" y="188" font-size="12.5">A man who is out-earned has</text>
              <text class="dg-t" x="322" y="205" font-size="12.5">failed at the breadwinner part, so</text>
              <text class="dg-t" x="322" y="222" font-size="12.5">he refuses the part coded female.</text>
              <text class="dg-t" x="322" y="239" font-size="12.5">The finding is what needs explaining.</text>
              <text class="dg-m dg-dim" x="22" y="249" font-size="10.5">A STRAY FACT</text>
              <text class="dg-m" x="322" y="249" font-size="10.5" style="fill:var(--close)">EVIDENCE</text>
            </svg>
            </div>
            <figcaption><b>Nothing is evidence on its own.</b> The box at the top never changes. What changes is the assumption underneath, and with it whether the number is evidence for anything at all. This is contextual empiricism in one picture, and it is why Longino puts objectivity in the community: the assumption on the left was shared across the field, so nobody inside it was troubled by a fact that fitted nowhere. Seeing it took somebody who held a different one.</figcaption>
          </figure>
'''
A1 = '''<p><b>Then the objectivity.</b>'''
assert A1 in h
h = h.replace(A1, FRAME + '\n          <div class="body">\n            ' + A1, 1)
h = h.replace('''          </div>

''' + FRAME, FRAME, 1)

# ---- 5.4 selective representation: the number that says nothing ------------
YR = '''
          <figure class="dia">
            <div class="draw">
            <svg viewBox="0 0 560 264" role="img" aria-labelledby="dg-five-yr" style="font-family:var(--body)">
              <title id="dg-five-yr">A survival curve that is flat from year two to year five, so a ninety-five per cent figure quoted at five years is the same number as at two years and reports no benefit from the three years between.</title>
              <text class="dg-m dg-dim" x="12" y="16" font-size="11">SURVIVING, PER CENT</text>
              <rect class="dg-box" x="8" y="26" width="544" height="178" rx="3"/>
              <path class="dg-ln dg-dim" d="M64 54 L536 54 M64 96 L536 96 M64 138 L536 138" stroke-width="1" stroke-dasharray="3 4"/>
              <text class="dg-t dg-dim" x="26" y="58" font-size="11">100</text>
              <text class="dg-t dg-dim" x="30" y="100" font-size="11">95</text>
              <text class="dg-t dg-dim" x="30" y="142" font-size="11">90</text>
              <path class="dg-ln" d="M64 54 L176 96 L536 96" stroke-width="2.4" style="stroke:var(--close)"/>
              <circle cx="176" cy="96" r="4.5" style="fill:var(--close)"/>
              <circle cx="536" cy="96" r="4.5" style="fill:var(--close)"/>
              <path class="dg-ln" d="M176 96 L176 186 M536 96 L536 186" stroke-width="1" stroke-dasharray="3 4"/>
              <text class="dg-t" x="150" y="182" font-size="12.5" font-weight="600">year 2</text>
              <text class="dg-t" x="502" y="182" font-size="12.5" font-weight="600">year 5</text>
              <text class="dg-t" x="196" y="88" font-size="12.5">nothing happens along here</text>
              <text class="dg-t dg-dim" x="64" y="200" font-size="11.5">start of treatment</text>
              <text class="dg-t" x="8" y="228" font-size="13"><tspan font-weight="600">Reported:</tspan> 95 per cent of patients taking the drug for five years were alive.</text>
              <text class="dg-t" x="8" y="248" font-size="13"><tspan font-weight="600">Left out:</tspan> so were 95 per cent at two years.</text>
            </svg>
            </div>
            <figcaption><b>Both sentences are true, and one of them sells three years of a drug.</b> This is the chapter's clearest case of selective representation, and the thing to notice is that no figure in it is wrong. The five-year survival rate is accurate. It is quoted without the two-year rate, which is identical, so the reader supplies the only reason anybody would mention it. The flat stretch is the whole argument, and it is the part that never appears in the advertisement.</figcaption>
          </figure>
'''
A2 = '''<li><b>The drug.</b> A company reports'''
assert A2 in h
i = h.find('<ul>', h.find('Misleading with things that are true'))
j = h.find('</ul>', i) + len('</ul>\n            </div>\n')
h = h[:j] + YR + h[j:]

# ---- 20.2 sperm is cheap and eggs are expensive ---------------------------
GAM = '''
          <figure class="dia">
            <div class="draw">
            <svg viewBox="0 0 520 206" role="img" aria-labelledby="dg-gametes" style="font-family:var(--body)">
              <title id="dg-gametes">A human egg cell and a human sperm drawn to the same scale, the egg about a hundred and twenty micrometres across and the sperm head about five.</title>
              <rect class="dg-box" x="8" y="24" width="504" height="150" rx="3"/>
              <text class="dg-m dg-dim" x="12" y="16" font-size="11">DRAWN TO THE SAME SCALE</text>
              <circle cx="118" cy="99" r="58" style="fill:var(--close-wash); stroke:var(--close); stroke-width:1.6"/>
              <circle cx="118" cy="99" r="40" style="fill:none; stroke:var(--close); stroke-width:1; stroke-dasharray:3 4; opacity:.6"/>
              <text class="dg-t" x="118" y="103" font-size="12.5" text-anchor="middle" font-weight="600">egg</text>
              <text class="dg-t dg-dim" x="118" y="178" font-size="11.5" text-anchor="middle">about 120 micrometres across</text>
              <ellipse cx="318" cy="99" rx="2.4" ry="1.6" style="fill:var(--close); stroke:none"/>
              <path class="dg-ln" d="M320 99 q 14 -7 28 0 q 14 7 28 0 q 14 -7 28 0" stroke-width="1.2" style="stroke:var(--close)"/>
              <path class="dg-ln dg-dim" d="M318 112 L318 140 M404 112 L404 140" stroke-width="1" stroke-dasharray="3 4"/>
              <text class="dg-t dg-dim" x="262" y="155" font-size="11.5">head about 5 micrometres, whole cell about 55</text>
              <path class="dg-ln dg-dim" d="M300 92 L312 97" stroke-width="1"/>
              <text class="dg-t" x="244" y="90" font-size="12.5" font-weight="600">sperm</text>
            </svg>
            </div>
            <figcaption><b>Sperm is cheap and eggs are expensive, drawn.</b> The size difference is real and it is what parental investment theory is built on: the sex that invests more will be the choosier one. Nelson's objection is not that the picture is false. It is that three economic words, <b>investment</b>, <b>cheap</b> and <b>expensive</b>, were laid over it, and those words answer the question the measurement was supposed to raise. A male produces millions of these per egg, and whether that adds up to less investment is the thing in dispute, which the vocabulary settles before anybody counts.</figcaption>
          </figure>
'''
A3 = '''<blockquote>Uncritical acceptance of'''
assert A3 in h
h = h.replace(A3, '</div>\n' + GAM + '\n          <div class="body">\n            ' + A3, 1)

open(f, 'w', encoding='utf-8').write(h)
print('three drawings placed')
