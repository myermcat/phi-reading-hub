"""Replace the portraits that were filling a coverage slot with the thing the section argues about.

The coverage rule was never a portrait quota. It says each part of the reading deserves a picture,
and a face is what you reach for when you have not asked what the section is actually about.
"""
import sys; sys.path.insert(0, '_claude')
from figmove import cut
f = 'week-6/index.html'
h = open(f, encoding='utf-8').read()

for img in ('img/mills.jpg', 'img/tuana.jpg', 'img/darwin.jpg'):
    h, _ = cut(h, img)
    print('removed', img)

FIG = '''
          <figure class="pic">
            <a class="zoom" style="width:420px" href="img/clitoris.svg" target="_blank" rel="noopener"
               title="Open this picture at full size">
              <img class="ink" src="img/clitoris.svg" width="600" height="600" loading="lazy"
                   alt="A medical illustration of the clitoris seen from the front. A small rounded
                        glans sits at the top, and below it a much larger wishbone-shaped structure of
                        paired arms and paired bulbs spreads downward and outward on either side of the
                        urethral and vaginal openings. Six parts are labelled.">
            </a>
            <figcaption><b>Tuana's second kind, drawn.</b> The labelled glans at the top is the part a
            standard anatomy drawing showed, and everything below it, the paired crura and the bulbs of
            the vestibule, is the same organ again. It was absent from the textbooks for decades. Her
            point is that nobody weighed it up and rejected it as unimportant, which is what the first
            kind would be. Study of the genitals was organised around reproduction, the clitoris was
            taken to play no part in reproduction, and so it was not a thing anybody could be ignorant
            about. The full internal structure was not published until 1998.
            <span class="cred">Amphis, vectorised by Marnanel, public domain, via Wikimedia Commons.
            Labels in the other seventeen languages removed.</span></figcaption>
          </figure>
'''

ANCHOR = '''            </ol>
          </div>

          <h5>Willful ignorance, kind 4'''
assert ANCHOR in h, 'anchor'
h = h.replace(ANCHOR, '            </ol>\n          </div>\n' + FIG + '\n          <h5>Willful ignorance, kind 4', 1)

open(f, 'w', encoding='utf-8').write(h)
print('clitoris figure placed in 5.3')
