"""Underline in the same two colours as the highlighter, for marking without flooding the line."""
import glob

CSS_AT = "  mark.hl-n { background: rgba(31,107,87,.10); border-bottom: 1px dashed var(--accent); }"
CSS_NEW = CSS_AT + """
  mark.hl-uy { background: none; border-radius: 0; box-shadow: inset 0 -2px 0 rgba(255,206,0,.95); }
  mark.hl-up { background: none; border-radius: 0; box-shadow: inset 0 -2px 0 rgba(255,92,168,.9); }"""

DOT_AT = "  .bmi .dot.p { background: rgba(255,92,168,.7); }"
DOT_NEW = DOT_AT + """
  .bmi .dot.uy { background: none; box-shadow: inset 0 -3px 0 rgba(255,206,0,.85); }
  .bmi .dot.up { background: none; box-shadow: inset 0 -3px 0 rgba(255,92,168,.7); }"""

BTN_AT = '  #hl-bar button[data-c="p"] { background: rgba(255,92,168,.45); }'
BTN_NEW = BTN_AT + """
  #hl-bar button[data-c="uy"] { background: var(--paper); box-shadow: inset 0 -4px 0 rgba(255,206,0,.85); }
  #hl-bar button[data-c="up"] { background: var(--paper); box-shadow: inset 0 -4px 0 rgba(255,92,168,.7); }"""

MK_AT = ("      '<button type=\"button\" data-c=\"p\" title=\"Highlight pink\" "
         "aria-label=\"Highlight pink\"></button>' +\n")
MK_NEW = MK_AT + (
 "      '<button type=\"button\" data-c=\"uy\" title=\"Underline yellow\" "
 "aria-label=\"Underline yellow\"></button>' +\n"
 "      '<button type=\"button\" data-c=\"up\" title=\"Underline pink\" "
 "aria-label=\"Underline pink\"></button>' +\n")

for f in sorted(glob.glob('**/*.html', recursive=True)):
    h = o = open(f, encoding='utf-8').read()
    if "bar.id = 'hl-bar'" not in h:
        continue
    for a, b in ((CSS_AT, CSS_NEW), (DOT_AT, DOT_NEW), (BTN_AT, BTN_NEW), (MK_AT, MK_NEW)):
        assert a in h, (f, a[:46])
        h = h.replace(a, b, 1)
    open(f, 'w', encoding='utf-8').write(h); print('patched', f)
