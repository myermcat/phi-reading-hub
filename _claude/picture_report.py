"""List every picture with what it shows and what its caption claims, so the cut is her call.

The coherence principle is the best-supported finding in the research, and it says to remove
material that the outcome does not depend on. It does not say what the outcome is. That has to
come from outside, which here means the practice questions and the cheat sheet. Where those do
not exist yet for a week, this prints what there is to judge by and decides nothing.
"""
import re, sys, glob, html as H

def txt(s):
    return re.sub(r'\s+', ' ', H.unescape(re.sub(r'<[^>]+>', ' ', s))).strip()

def near(h, pos, after):
    seg = h[pos:pos + 4000] if after else h[max(0, pos - 4000):pos]
    ps = re.findall(r'<p>(.*?)</p>', seg, re.S)
    if not ps: return ''
    return txt(ps[0] if after else ps[-1])

f = sys.argv[1]
h = open(f, encoding='utf-8').read()
tests = ' '.join(open(p, encoding='utf-8').read() for p in glob.glob('exam-*/*.html'))

print('PICTURES IN %s\n' % f)
for i, m in enumerate(re.finditer(r'<figure class="pic[^"]*">.*?</figure>', h, re.S), 1):
    blk = m.group(0)
    src = re.search(r'src="([^"]+)"', blk).group(1)
    alt = txt(re.search(r'alt="([^"]*)"', blk).group(1))
    cap = txt(re.search(r'<figcaption>(.*?)</figcaption>', blk, re.S).group(1))
    cred = re.search(r'<span class="cred">(.*?)</span>', blk, re.S)
    if cred: cap = cap.replace(txt(cred.group(1)), '').strip()
    claim = cap.split('.', 1)[1].strip() if '.' in cap else ''
    # a name that also turns up in the practice sets is doing work beyond the page
    names = set(re.findall(r'\b([A-Z][a-z]{3,})\b', cap))
    hit = sorted(n for n in names if n in tests)
    print('%d. %s' % (i, src))
    print('   shows    %s' % alt[:150])
    print('   claims   %s' % (claim[:230] or '(nothing beyond naming the subject)'))
    print('   section  %s' % near(h, m.start(), False)[:110])
    print('   tested   %s' % (', '.join(hit) if hit else 'nothing in this caption appears in any practice set'))
    print()
