"""Catch a summary that names the shape of a step and withholds its content.

The shape of an argument is cheap to write and worthless to read. "She applied that rule to the
biggest scientific quarrel of her day and took the correct middle position" says there was a
quarrel, that it was important, and that she was right, and names none of the three. A reader
revising from it has nothing.

    python3 _claude/blurb_gate.py week-7/index.html
"""
import re, sys, glob, html as H

SHAPE = re.compile(
    # the placeholder is the giveaway: a claim about IT, the biggest quarrel of her DAY,
    # the CORRECT position. A category where an instance belongs.
    r'\b((?:claim|position|rule|point|question|argument|view|idea) about (?:itself|it|that|this|them)\b'
    r'|the (?:biggest|greatest|most important|real|key|crucial|central|main) \w+ of '
    r'(?:her|his|their|the) (?:day|time|age|career|century)\b'
    r'|the correct (?:position|answer|view|one)\b'
    r'|and so was free to\b'
    r'|which neither side could\b'
    r'|the thing that makes it\b'
    r'|something (?:about|like) that\b'
    r'|the same (?:argument|point|claim|thing) (?:she|he|they|it) \w+'
    r'|making the same \w+\b)', re.I)

bad = 0
for f in (sys.argv[1:] or sorted(glob.glob('week-*/index.html'))):
    h = open(f, encoding='utf-8').read()
    body = re.sub(r'<svg.*?</svg>', '', h[h.find('<div class="wrap">'):h.find('<footer')], flags=re.S)
    hits = []
    for m in re.finditer(r'<(p|li|dd|figcaption|div class="(?:keep|qa|kone|why)")[^>]*>(.*?)'
                         r'</(?:p|li|dd|figcaption|div)>', body, re.S):
        t = re.sub(r'\s+', ' ', H.unescape(re.sub(r'<[^>]+>', '', m.group(2)))).strip()
        for s in re.split(r'(?<=[.?!]) ', t):
            if SHAPE.search(s):
                hits.append(s)
    if hits:
        bad += 1
        print('===', f)
        for s in dict.fromkeys(hits):
            print('  *', s[:160])
sys.exit(1 if bad else 0)
