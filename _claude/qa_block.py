"""Every section of week 7 opens with a question and then answers it. That structure was
invisible, because the question was one more paragraph with a bold lead-in."""
import re, sys

CSS = '''  .qa { border-left: 2px solid var(--accent); padding: 4px 0 4px 18px; max-width: var(--measure);
        font-family: var(--display); font-size: 19px; line-height: 1.38; color: var(--ink); }
  .qa b { display: block; margin-bottom: 6px; font-family: var(--mono); font-size: 10.5px;
          font-weight: 500; letter-spacing: 0.11em; text-transform: uppercase; color: var(--accent); }
'''

for f in sys.argv[1:]:
    h = open(f, encoding='utf-8').read()
    anchor = '  .body > p > b:first-child { color: var(--lead); }\n'
    assert anchor in h
    if '.qa {' not in h:
        h = h.replace(anchor, anchor + CSS, 1)

    n = [0]
    def one(m):
        indent, q = m.group(1), m.group(2).strip()
        q = q[0].upper() + q[1:]
        n[0] += 1
        return ('%s</div>\n\n%s<div class="qa">\n%s  <b>The question</b>\n%s  %s\n%s</div>\n\n'
                '%s<div class="body">' % (indent, indent, indent, indent, q, indent, indent))

    h = re.sub(r'<div class="body">\n(\s*)<p><b>The question:(.*?)</b></p>\n',
               lambda m: one(m)[len('</div>\n\n'):].lstrip() and
                         ('<div class="qa">\n%s  <b>The question</b>\n%s  %s\n%s</div>\n\n%s<div class="body">\n'
                          % (m.group(1), m.group(1), (lambda s: s[0].upper()+s[1:])(m.group(2).strip()),
                             m.group(1), m.group(1))),
               h, flags=re.S)
    open(f, 'w', encoding='utf-8').write(h)
    print('%s: %d question blocks' % (f, h.count('<div class="qa">')))
