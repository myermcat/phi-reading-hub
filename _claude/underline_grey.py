"""A third underline, green-grey and lighter than the other two, for the everyday mark."""
import glob

PAIRS = [
 ('    --ul-p:     rgba(208,62,130,.48);',
  '    --ul-p:     rgba(208,62,130,.48);\n    --ul-g:     rgba(58,98,84,.34);'),
 ('--ul-y: rgba(217,169,87,.48); --ul-p: rgba(255,151,198,.38);',
  '--ul-y: rgba(217,169,87,.48); --ul-p: rgba(255,151,198,.38);\n      --ul-g: rgba(116,166,148,.30);'),
 ('  mark.hl-up { background: none; border-radius: 0; box-shadow: inset 0 -1.5px 0 var(--ul-p); }',
  '  mark.hl-up { background: none; border-radius: 0; box-shadow: inset 0 -1.5px 0 var(--ul-p); }\n'
  '  mark.hl-ug { background: none; border-radius: 0; box-shadow: inset 0 -1.5px 0 var(--ul-g); }'),
 ('  .bmi .dot.up { background: none; box-shadow: inset 0 -3px 0 var(--ul-p); }',
  '  .bmi .dot.up { background: none; box-shadow: inset 0 -3px 0 var(--ul-p); }\n'
  '  .bmi .dot.ug { background: none; box-shadow: inset 0 -3px 0 var(--ul-g); }'),
 ('  #hl-bar button[data-c="up"] { background: var(--paper); box-shadow: inset 0 -4px 0 var(--ul-p); }',
  '  #hl-bar button[data-c="ug"] { background: var(--paper); box-shadow: inset 0 -4px 0 var(--ul-g); }\n'
  '  #hl-bar button[data-c="up"] { background: var(--paper); box-shadow: inset 0 -4px 0 var(--ul-p); }'),
 ("      '<button type=\"button\" data-c=\"uy\" title=\"Underline yellow\" aria-label=\"Underline yellow\"></button>' +",
  "      '<button type=\"button\" data-c=\"ug\" title=\"Underline, the everyday one\" aria-label=\"Underline, the everyday one\"></button>' +\n"
  "      '<button type=\"button\" data-c=\"uy\" title=\"Underline yellow\" aria-label=\"Underline yellow\"></button>' +"),
]
for f in sorted(glob.glob('week-*/index.html')):
    h = o = open(f, encoding='utf-8').read()
    if 'mark.hl-uy' not in h:
        continue
    for a, b in PAIRS:
        assert a in h, (f, a[:52])
        h = h.replace(a, b, 1)
    # the dark block is written twice, in the media query and under data-theme
    h = h.replace('--ul-y: rgba(217,169,87,.48); --ul-p: rgba(255,151,198,.38);\n      --ul-g: rgba(116,166,148,.30);',
                  '--ul-y: rgba(217,169,87,.48); --ul-p: rgba(255,151,198,.38);\n      --ul-g: rgba(116,166,148,.30);', 1)
    open(f, 'w', encoding='utf-8').write(h); print('patched', f)
