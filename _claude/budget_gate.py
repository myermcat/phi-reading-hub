"""A guide that is as long as its reading has saved nobody anything.

The budget has two parts. Prose about the chapters is capped per page of assigned reading, since
a printed page of these books runs about 450 words and 200 is under half of it. The week's own
framing, meaning the argument section and the front matter, gets a flat allowance instead, because
it answers the week's question and that does not get longer when the chapters do. The glossary and
the for-the-curious blocks are excluded, since neither is read straight through.

The rule that keeps it there: an edit that adds prose takes at least as much out. Every guide
drifted over by addition, one clarification at a time, with nothing ever removed.

    python3 _claude/budget_gate.py
    python3 _claude/budget_gate.py week-7/index.html
"""
import re, sys, glob
from html.parser import HTMLParser

CAP = 200        # words of prose per page of assigned reading
FRAME = 900      # a flat allowance for the week's own framing, which does not scale with pages

class Count(HTMLParser):
    SKIP_TAGS = ('script', 'style', 'svg')
    SKIP_CLASS = ('curious', 'gl', 'sitefoot')
    def __init__(self):
        super().__init__(convert_charrefs=True)
        self.n, self.skip, self.stack = 0, 0, []
    def handle_starttag(self, t, attrs):
        cls = (dict(attrs).get('class') or '').split()
        hit = t in self.SKIP_TAGS or any(c in self.SKIP_CLASS for c in cls)
        self.stack.append(hit)
        if hit:
            self.skip += 1
    def handle_endtag(self, t):
        if self.stack and self.stack.pop():
            self.skip = max(0, self.skip - 1)
    def handle_data(self, d):
        if not self.skip:
            self.n += len(d.split())

def pages(h):
    """The guide states its own page count in the tally strip."""
    cells = re.findall(r'<div[^>]*><b>(\d+)</b><span>([^<]*)</span></div>', h)
    for n, label in cells:
        if 'in all' in label or 'to read' in label:
            return int(n)
    own = [int(n) for n, label in cells if label.lstrip().startswith('pages of')]
    return sum(own) or 0

bad = 0
print('%-9s %7s %5s %8s   %s' % ('guide', 'words', 'pp', 'budget', '%d a page plus %d' % (CAP, FRAME)))
for f in (sys.argv[1:] or sorted(glob.glob('week-*/index.html'))):
    h = open(f, encoding='utf-8').read()
    body = h[h.find('<div class="wrap">'):h.find('<footer')]
    c = Count(); c.feed(body)
    pp = pages(h)
    if not pp:
        print('%-9s %7d %5s %8s   no page count in the tally' % (f[:9], c.n, '?', '?'))
        continue
    budget = CAP * pp + FRAME
    over = c.n > budget
    bad += over
    print('%-9s %7d %5d %8d   %s' % (f[:9], c.n, pp, budget,
          ('OVER by %d' % (c.n - budget)) if over else 'within, %d to spare' % (budget - c.n)))
sys.exit(1 if bad else 0)
