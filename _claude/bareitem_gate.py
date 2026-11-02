"""A list item that is a bare term.

"Unlearning. Rewriting. Unschooling. Failure. Illiteracy." went out as five words in a row with
nothing beside them, and she asked how she was supposed to know what any of them meant. An item
in a list carries enough words to say what it is.

    python3 _claude/bareitem_gate.py
    python3 _claude/bareitem_gate.py week-7/index.html
"""
import re, sys, glob, html as H

FLOOR = 3        # an item of one or two words is a term with its meaning left out
ALLOW = re.compile(r'^(ch|week|p{1,2})\b|^\d', re.I)   # a page or chapter label is meant to be short

bad = 0
for f in sorted(sys.argv[1:] or glob.glob('week-*/index.html')):
    h = open(f, encoding='utf-8').read()
    for m in re.finditer(r'<li\b[^>]*>(.*?)</li>', h, re.S):
        t = H.unescape(re.sub(r'<[^>]+>', ' ', m.group(1))).strip()
        if not t or ALLOW.match(t) or len(t.split()) >= FLOOR:
            continue
        # a nav entry or a tag is markup, and those live outside the article body
        before = h[:m.start()]
        if before.rfind('<nav') > before.rfind('</nav>'):
            continue
        print('%s:%d  %s' % (f, before.count('\n') + 1, t[:60]))
        bad += 1
print('%d bare list items' % bad)
sys.exit(1 if bad else 0)
