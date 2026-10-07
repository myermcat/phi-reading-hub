"""Catch the AI-prose shapes the linter misses.

prose-lint.mjs finds "X, not Y" and "X rather than Y". These are the same defect
wearing other words, plus a few framings the student has flagged by hand.
"""
import re, sys, os
PATS = [
 (r",\s+and not\b", "antithesis: 'X, and not Y'"),
 (r"\band never\b(?!\s*(mind|again))", "antithesis: 'X and never Y'"),
 (r"\bis about .{0,40}, it(?:'s| is) about\b", "antithesis: 'not about X, about Y'"),
 (r"\bwhich is what (makes|does|gives|lets)\b", "scaffolding: 'which is what makes'"),
 (r"\bthat is what (makes|does|gives|lets)\b", "scaffolding: 'that is what makes'"),
 (r"\bis the thing that\b", "scaffolding: 'is the thing that'"),
 (r"\bwhat .{0,25} (is|was) really (doing|about|saying)\b", "scaffolding: 'what X was really doing'"),
 (r"\bno more than\b|\bnothing more than\b", "dismissive flourish"),
 (r"\bit turns out that\b|\bas it turns out\b", "scaffolding: 'it turns out'"),
]
def scan(path):
    s = open(path, encoding="utf-8").read()
    hits = []
    for pat, why in PATS:
        for m in re.finditer(pat, s, re.I | re.M):
            hits.append((why, re.sub(r"\s+", " ", s[max(0, m.start()-80):m.start()+110])))
    return hits
if __name__ == "__main__":
    total = 0
    for p in sys.argv[1:]:
        h = scan(p); total += len(h)
        print("%-30s %s" % (os.path.basename(p), "clean" if not h else "%d hits" % len(h)))
        for why, ctx in h:
            print("    %-32s ...%s..." % (why, ctx[:118]))
    sys.exit(1 if total else 0)
