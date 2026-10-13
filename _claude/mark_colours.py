"""Mark colours become tokens, which is the only way they follow the theme.

The dark values for the highlighters were written as :root[data-theme="dark"] rules. Nothing sets
that attribute any more, so they had been dead since the light/dark toggle came out, and every
mark was drawing at its light alpha on a dark page. The underlines were worse: they went in at
.95 and .9 against fills of .42 and .34, so the quieter mark was the loudest thing on the line.
"""
import re, glob

LIGHT_AT = '    --ghost:      #DADFD9;'
LIGHT_NEW = LIGHT_AT + '''

    --hl-y:     rgba(255,206,0,.42);
    --hl-p:     rgba(255,92,168,.34);
    --hl-n:     rgba(31,107,87,.10);
    --hl-n-act: rgba(31,107,87,.22);
    --ul-y:     rgba(196,152,0,.55);
    --ul-p:     rgba(208,62,130,.48);'''

DARK_AT = '--ghost: #2C332E;'
DARK_NEW = DARK_AT + ('''
      --hl-y: rgba(255,206,0,.24); --hl-p: rgba(255,92,168,.24);
      --hl-n: rgba(100,191,161,.12); --hl-n-act: rgba(100,191,161,.22);
      --ul-y: rgba(217,169,87,.48); --ul-p: rgba(255,151,198,.38);''')

RULES = [
 ('  mark.hl-y { background: rgba(255,206,0,.42); }',
  '  mark.hl-y { background: var(--hl-y); }'),
 ('  mark.hl-p { background: rgba(255,92,168,.34); }',
  '  mark.hl-p { background: var(--hl-p); }'),
 ('  mark.hl-n { background: rgba(31,107,87,.10); border-bottom: 1px dashed var(--accent); }',
  '  mark.hl-n { background: var(--hl-n); border-bottom: 1px dashed var(--accent); }'),
 ('  mark.hl-n.act { background: rgba(31,107,87,.22); }',
  '  mark.hl-n.act { background: var(--hl-n-act); }'),
 ('  mark.hl-uy { background: none; border-radius: 0; box-shadow: inset 0 -2px 0 rgba(255,206,0,.95); }\n'
  '  mark.hl-up { background: none; border-radius: 0; box-shadow: inset 0 -2px 0 rgba(255,92,168,.9); }',
  '  mark.hl-uy { background: none; border-radius: 0; box-shadow: inset 0 -1.5px 0 var(--ul-y); }\n'
  '  mark.hl-up { background: none; border-radius: 0; box-shadow: inset 0 -1.5px 0 var(--ul-p); }'),
 ('  .bmi .dot.uy { background: none; box-shadow: inset 0 -3px 0 rgba(255,206,0,.85); }\n'
  '  .bmi .dot.up { background: none; box-shadow: inset 0 -3px 0 rgba(255,92,168,.7); }',
  '  .bmi .dot.uy { background: none; box-shadow: inset 0 -3px 0 var(--ul-y); }\n'
  '  .bmi .dot.up { background: none; box-shadow: inset 0 -3px 0 var(--ul-p); }'),
 ('  #hl-bar button[data-c="uy"] { background: var(--paper); box-shadow: inset 0 -4px 0 rgba(255,206,0,.85); }\n'
  '  #hl-bar button[data-c="up"] { background: var(--paper); box-shadow: inset 0 -4px 0 rgba(255,92,168,.7); }',
  '  #hl-bar button[data-c="uy"] { background: var(--paper); box-shadow: inset 0 -4px 0 var(--ul-y); }\n'
  '  #hl-bar button[data-c="up"] { background: var(--paper); box-shadow: inset 0 -4px 0 var(--ul-p); }'),
 ('  #hl-bar button[data-c="y"] { background: rgba(255,206,0,.55); }',
  '  #hl-bar button[data-c="y"] { background: var(--hl-y); }'),
 ('  #hl-bar button[data-c="p"] { background: rgba(255,92,168,.45); }',
  '  #hl-bar button[data-c="p"] { background: var(--hl-p); }'),
]
DEAD = re.compile(r'\n  :root\[data-theme="dark"\] mark\.hl-[ynp] \{[^}]*\}')

for f in sorted(glob.glob('week-*/index.html')):
    h = o = open(f, encoding='utf-8').read()
    if 'mark.hl-uy' not in h:
        continue
    assert LIGHT_AT in h and h.count(DARK_AT) == 2, f
    h = h.replace(LIGHT_AT, LIGHT_NEW, 1)
    h = h.replace(DARK_AT, DARK_NEW)
    for a, b in RULES:
        assert a in h, (f, a[:48])
        h = h.replace(a, b, 1)
    h, n = DEAD.subn('', h)
    assert n == 3, (f, n)
    open(f, 'w', encoding='utf-8').write(h)
    print('%s: tokenised, %d dead rules removed' % (f, n))
