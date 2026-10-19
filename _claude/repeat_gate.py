"""Catch a section that says the same thing twice, which reading the prose will not catch.

Each pass on its own is fine, so the repetition is invisible from inside the sentences. Listing
the blocks and comparing them finds it in a second.

    python3 _claude/repeat_gate.py week-7/index.html
    python3 _claude/repeat_gate.py --list week-7/index.html   # print the outline to read
"""
import re, sys, glob, html as H
from difflib import SequenceMatcher

STOP = set('the a an of to in is are and or that this it for on as be was with by its into'.split())

def words(s):
    return [w for w in re.findall(r"[a-z']+", s.lower()) if w not in STOP and len(w) > 2]

def blocks(path):
    h = open(path, encoding='utf-8').read()
    body = h[h.find('<div class="wrap">'):h.find('<footer')]
    body = re.sub(r'<svg.*?</svg>', '', body, flags=re.S)
    body = re.sub(r'<div class="curious">.*?\n\s*</div>\n', '', body, flags=re.S)
    # the glossary restates the body on purpose, and a heading shares words with its own section
    g = body.find('id="s-gloss"')
    if g > 0:
        body = body[:body.rfind('<section', 0, g)]
    out, section = [], 'top'
    for m in re.finditer(r'<(h2|h3|h4|h5|p|li|dd|div class="(?:keep|qa|kone|why)")[^>]*>(.*?)'
                         r'</(?:h2|h3|h4|h5|p|li|dd|div)>', body, re.S):
        kind = m.group(1).split()[0]
        if 'class' in m.group(1):
            kind = m.group(1).split('"')[1]
        t = re.sub(r'\s+', ' ', H.unescape(re.sub(r'<[^>]+>', ' ', m.group(2)))).strip()
        if len(t) < 25:
            continue
        if kind in ('h2', 'h3', 'h4'):
            section = t[:52]
        out.append((section, kind, t))
    return out

def main():
    show = '--list' in sys.argv
    files = [a for a in sys.argv[1:] if not a.startswith('--')] or sorted(glob.glob('week-*/index.html'))
    bad = 0
    for f in files:
        bs = blocks(f)
        if show:
            print('===', f)
            for sec, kind, t in bs:
                print('  [%-4s] %s' % (kind[:4], t[:104]))
            continue
        pairs = []
        for i in range(len(bs)):
            for j in range(i + 1, len(bs)):
                if bs[i][0] != bs[j][0]:
                    continue                      # only within one section
                if bs[i][1].startswith('h') or bs[j][1].startswith('h'):
                    continue                      # a heading names its section, which is the job
                a, b = set(words(bs[i][2])), set(words(bs[j][2]))
                if len(a) < 6 or len(b) < 6:
                    continue
                overlap = len(a & b) / min(len(a), len(b))
                ratio = SequenceMatcher(None, bs[i][2], bs[j][2]).ratio()
                if overlap > 0.55 or ratio > 0.55:
                    pairs.append((overlap, bs[i], bs[j]))
        if pairs:
            bad += 1
            print('===', f)
            for ov, x, y in sorted(pairs, reverse=True)[:12]:
                print('  %.0f%% shared, in "%s"' % (ov * 100, x[0]))
                print('     [%s] %s' % (x[1][:4], x[2][:96]))
                print('     [%s] %s' % (y[1][:4], y[2][:96]))
    sys.exit(1 if bad else 0)

main()
