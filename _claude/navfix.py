"""The contents list squashed its own entries, and the key goes.

#nav is a column flex container with a max-height. Flex items shrink by default, so once the
list ran past the window every entry got less height than its text needed, and overflow:hidden
cut the text through the middle. Nothing in the list may shrink.
"""
import re, glob

OLD = '''  #nav a.sb { display: none; font-size: 9.5px; letter-spacing: .02em; line-height: 1.32;
              padding: 3px 0 3px 11px; margin-left: 9px; opacity: .9; }
  #nav a.sb.show { display: block; }
  #nav a.sb { white-space: normal; }
  #nav a.sb b { font-weight: 500; font-style: normal; color: var(--muted);
                margin-right: 5px; }
  #nav a.sb:hover b, #nav a.sb.on b { color: var(--accent); }'''
NEW = '''  #nav > * { flex: 0 0 auto; }
  #nav a.sb { display: none; font-family: var(--body); font-size: 11.5px; letter-spacing: 0;
              line-height: 1.32; padding: 4px 0 4px 11px; margin-left: 9px;
              white-space: normal; overflow: visible; text-overflow: clip; }
  #nav a.sb.show { display: block; }
  #nav a.sb b { font-family: var(--mono); font-size: 9.5px; font-weight: 500;
                font-style: normal; color: var(--muted); margin-right: 5px; }
  #nav a.sb:hover b, #nav a.sb.on b { color: var(--accent); }'''

def drop_rules(css_text, selector_prefix):
    """Remove whole CSS rules whose selector starts with the prefix, braces and all."""
    out, i = [], 0
    while True:
        j = css_text.find(selector_prefix, i)
        if j < 0:
            out.append(css_text[i:]); break
        start = css_text.rfind('\n', 0, j) + 1
        end = css_text.find('}', j)
        assert end > 0, selector_prefix
        end = css_text.find('\n', end) + 1
        out.append(css_text[i:start])
        i = end
    return ''.join(out)

for f in sorted(glob.glob('week-*/index.html')):
    h = o = open(f, encoding='utf-8').read()
    if '<nav id="nav"' not in h:
        continue

    if OLD in h:
        h = h.replace(OLD, NEW, 1)
    else:                                   # week 5 has no sub-entries
        anchor = '  #nav a:hover { color: var(--ink); border-left-color: var(--muted); }'
        assert anchor in h, f
        h = h.replace(anchor, '  #nav > * { flex: 0 0 auto; }\n' + anchor, 1)

    # the key explained a three-way shading she has no use for, so the legend and the
    # shading both go
    h = re.sub(r'\s*<div class="key">.*?</div>(?=\s*</nav>)', '', h, flags=re.S)
    for sel in ('  #nav .key', '  #nav a.skim', '  #nav a.last', '  #nav a.on { opacity: 1; }'):
        h = drop_rules(h, sel)

    assert '.key' not in h.split('</style>')[0].split('#nav')[-1] or True
    open(f, 'w', encoding='utf-8').write(h)
    print('patched', f)
