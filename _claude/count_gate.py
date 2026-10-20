"""A stated number followed by a list.

"Four faults" over a bulleted list of four makes the reader count them to find out whether the
heading was right, and she did. A number said out loud is a promise that the items carry it, so
the list is numbered and its length matches.
"""
import re, sys, glob, html as H

WORD = {'two':2,'three':3,'four':4,'five':5,'six':6,'seven':7,'eight':8,'nine':9,'ten':10,
        '2':2,'3':3,'4':4,'5':5,'6':6,'7':7,'8':8,'9':9,'10':10}
NUM = re.compile(r'\b(two|three|four|five|six|seven|eight|nine|ten|[2-9]|10)\b', re.I)
SKIP = re.compile(r'\b(pp?|pages?|chapters?|century|centuries|years?|times?|volumes?)\b', re.I)

def text(s):
    return H.unescape(re.sub(r'<[^>]+>', ' ', s)).strip()

bad = 0
for f in sorted(sys.argv[1:] or glob.glob('week-*/index.html')):
    h = open(f, encoding='utf-8').read()
    # a lookahead, so one lead-in's match does not swallow the next one's list
    pat = r'<(h[2-5]|b)[^>]*>(.*?)</\1>(?=(.{0,900}?)<(ul|ol)\b(.*?)</\4>)'
    for m in re.finditer(pat, h, re.S):
        lead, between, tag, body = text(m.group(2)), text(m.group(3)), m.group(4), m.group(5)
        lead = re.sub(r'^\s*\d+(\.\d+)*[.)]?\s+', '', lead)  # a section number is not a count
        if len(between) > 400 or SKIP.search(lead):
            continue
        # a heading between the two means the list belongs to the next section
        if re.search(r'</h[2-5]>', m.group(3)):
            continue
        # the number has to be counting something named right after it
        DULL = {'and','but','the','was','were','are','is','for','that','she','her','his','its',
                'they','their','you','had','has','have','who','when','which','this','these','not',
                'with','from','into','over','under','only','also','more','most','such','same'}
        found = []
        for c in re.finditer(r'\b(two|three|four|five|six|seven|eight|nine|ten|[2-9]|10)\s+([a-z]{3,})',
                             lead, re.I):
            if c.group(2).lower() in DULL:
                continue
            if re.search(r'\b(week|weeks|ch|chapter|phase|step|part|figure|page)\s*$', lead[:c.start()], re.I):
                continue
            found.append(c)
        if not found:
            continue
        got = len(re.findall(r'<li\b', body))
        # a list that starts part way through a numbered run says so on its items
        first = re.search(r'<li[^>]*\bvalue="(\d+)"', body)
        if first:
            got += int(first.group(1)) - 1
        line = h[:m.start()].count('\n') + 1
        # one count in the lead naming the right number is enough. Two numbers in one sentence
        # are usually a count and something else.
        hit = [c for c in found if WORD[c.group(1).lower()] == got]
        if not hit:
            c = found[0]
            print('%s:%d  says %s, list has %d  >> %s' % (f, line, c.group(1), got, lead[:70]))
            bad += 1
        elif tag == 'ul':
            print('%s:%d  says %s over a bulleted list, number it  >> %s'
                  % (f, line, hit[0].group(1), lead[:70]))
            bad += 1
print('%d to fix' % bad)
sys.exit(1 if bad else 0)
