"""The top bar stopped where the contents column ended, because it sits in the flow and the
flow is what gets pushed right to make room. The bottom dock is fixed, so it always spanned.
Both bands now span the window and keep their contents lined up with the page column."""
import glob, re

OLD = '''  @media (min-width: 1000px) {
    #nav { display: flex; left: 16px; width: 150px; }
    body { padding-left: 182px; }
  }
  @media (min-width: 1320px) {
    #nav { left: max(16px, calc(50vw - 640px)); }
    body { padding-left: 0; }
  }'''
NEW = '''  @media (min-width: 1000px) { :root { --navpad: 182px; } #nav { display: flex; left: 16px; width: 150px; } }
  @media (min-width: 1320px) { :root { --navpad: 0px; } #nav { left: max(16px, calc(50vw - 640px)); } }
  body { margin: 0; padding-left: var(--navpad); }
  /* a full-bleed band that keeps its contents on the page column: the negative margin
     widens the box to the window edge, the padding puts the content back where it was */
  .site, .sitefoot { margin-left: calc(0px - var(--navpad)); padding-left: var(--navpad); }
  .dock { padding-left: var(--navpad); }'''

for f in sorted(glob.glob('week-*/index.html')):
    h = o = open(f, encoding='utf-8').read()
    if OLD not in h:
        continue
    h = h.replace(OLD, NEW, 1)
    h = h.replace('    --display: "Newsreader"', '    --navpad: 0px;\n\n    --display: "Newsreader"', 1)
    assert '--navpad: 0px;\n\n    --display' in h, f
    open(f, 'w', encoding='utf-8').write(h); print('patched', f)
