"""A stated number followed by a list.

"Four faults" over a bulleted list of four makes the reader count them to find out whether the
heading was right, and she did. A number said out loud is a promise that the items carry it, so
the list is numbered and its length matches. The count can sit in the heading, in a bold lead-in,
or in the plain sentence just before the list, which is where "it identifies two threats" sat.
"""
import re, sys, glob, html as H

WORD = {'two':2,'three':3,'four':4,'five':5,'six':6,'seven':7,'eight':8,'nine':9,'ten':10,
        '2':2,'3':3,'4':4,'5':5,'6':6,'7':7,'8':8,'9':9,'10':10}
SKIP = re.compile(r'\b(pp?|pages?|chapters?|century|centuries|years?|times?|volumes?)\b', re.I)
# words a number can sit in front of without counting anything
DULL = {'and','but','the','was','were','are','is','for','that','she','her','his','its',
        'they','their','you','had','has','have','who','when','which','this','these','not',
        'with','from','into','over','under','only','also','more','most','such','same'}
LABEL = re.compile(r'\b(week|weeks|ch|chapter|phase|step|part|figure|page)\s*$', re.I)

def text(s):
    return H.unescape(re.sub(r'<[^>]+>', ' ', s)).strip()

def counts(lead):
    """Every number in the lead that is counting something named right after it."""
    lead = re.sub(r'^\s*\d+(\.\d+)*[.)]?\s+', '', lead)   # a section number is not a count
    if SKIP.search(lead):
        return []
    out = []
    for c in re.finditer(r'\b(two|three|four|five|six|seven|eight|nine|ten|[2-9]|10)\s+([a-z]{3,})',
                         lead, re.I):
        if c.group(2).lower() in DULL or LABEL.search(lead[:c.start()]):
            continue
        out.append(c)
    return out

bad = 0
for f in sorted(sys.argv[1:] or glob.glob('week-*/index.html')):
    h = open(f, encoding='utf-8').read()
    leads = []
    pat = r'<(h[2-5]|b)[^>]*>(.*?)</\1>(?=(.{0,900}?)<(ul|ol)\b(.*?)</\4>)'
    for m in re.finditer(pat, h, re.S):
        if len(text(m.group(3))) > 400 or re.search(r'</h[2-5]>', m.group(3)):
            continue   # the list belongs to a later section
        leads.append((m.start(), text(m.group(2)), m.group(4), m.group(5)))
    for m in re.finditer(r'<(ul|ol)\b(.*?)</\1>', h, re.S):
        # only back to the end of the block before the list, so a count in an unrelated
        # paragraph two blocks up is not read as this list's promise
        # back to the start of the block right before the list, so a count in an unrelated
        # paragraph two blocks up is not read as this list's promise
        win = h[max(0, m.start() - 900):m.start()]
        cut = max(win.rfind(t) for t in ('<p', '<div', '<h4', '<h3', '<blockquote', '<li'))
        leads.append((m.start(), text(win[cut:] if cut > 0 else win)[-260:],
                      m.group(1), m.group(2)))
    seen = set()
    for start, lead, tag, body in sorted(leads):
        found = counts(lead)
        if not found:
            continue
        got = len(re.findall(r'<li\b', body))
        first = re.search(r'<li[^>]*\bvalue="(\d+)"', body)
        if first:                     # a list resuming a numbered run says so on its items
            got += int(first.group(1)) - 1
        line = h[:start].count('\n') + 1
        # one count naming the right number is enough. Two numbers in one sentence are usually
        # a count and something else.
        hit = [c for c in found if WORD[c.group(1).lower()] == got]
        key = (line, bool(hit))
        if key in seen:
            continue
        seen.add(key)
        if not hit:
            c = found[0]
            print('%s:%d  says %s, list has %d  >> %s' % (f, line, c.group(1), got, lead[-70:]))
            bad += 1
        elif tag == 'ul':
            print('%s:%d  says %s over a bulleted list, number it  >> %s'
                  % (f, line, hit[0].group(1), lead[-70:]))
            bad += 1
print('%d to fix' % bad)
sys.exit(1 if bad else 0)
