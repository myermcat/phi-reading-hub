"""Gate: every technical term is explained the first time a page uses it.

The rule it enforces is the student's, in her words: explain the thing plainly
first, and only then give it its name. So the check looks for a gloss marker
within a short window of the term's first appearance on each built page.
"""
import re, sys, os

TERMS = ["induction","inductive","epistemolog","metaphysic","positivis","contingent","taxonom",
 "empiricis","dialectic","teleolog","telos","paradigm","incommensurab","normalization",
 "genealogical","nominalist","instrumentalis","constructivis","ontolog","dualis","stratification",
 "meritocra","co-produc","heterogeneous","semantic","utilitarian","disciplinary matrix",
 "whig history","ad hoc","foundationalis","doxa","empeiria","episteme","physis","techne",
 "atechnia","furtive","docile","ideological","propensity","anomal"]

MARK = re.compile(
    r"(is called|called|means|meaning|named|the name for|is Kuhn's|is what .{0,40} calls"
    r"|, which is|, the |, mere |, meaning|is an? <b>|is an? \w+ for|"
    r"<i>\w+</i>\s*,\s*[a-z]|<b>\w+</b>\s*,\s*[a-z]|\bis opinion\b)", re.I)

def check(path):
    h = open(path, encoding="utf-8").read()
    # a term printed in a hint's own definition list counts as explained on that page
    defined = set()
    for block in re.findall(r'<ul class="terms">(.*?)</ul>', h, re.S):
        for lab in re.findall(r'<li><b>(.*?)</b>', block, re.S):
            defined.add(re.sub(r"<[^>]+>", "", lab).strip().lower())
    h = re.sub(r"<style.*?</style>", "", h, flags=re.S)
    h = re.sub(r"<script.*?</script>", "", h, flags=re.S)
    text = re.sub(r"<[^>]+>", " ", h)
    text = re.sub(r"\s+", " ", text)
    bad = []
    for t in TERMS:
        m = re.search(t, text, re.I)
        if not m:
            continue
        if any(t in d for d in defined):
            continue
        window = text[max(0, m.start() - 220): m.start() + 620]
        # "the inductive method, reasoning upward from ..." is an appositive gloss
        appositive = re.search(t + r"[a-z]*(?:\s+\w+){0,2},\s+[a-z]", window, re.I)
        if not (MARK.search(window) or appositive):
            bad.append((t, re.sub(r"\s+", " ", window[120:290])))
    return bad

if __name__ == "__main__":
    total = 0
    for p in sys.argv[1:]:
        bad = check(p)
        total += len(bad)
        print(("%-26s %s" % (os.path.basename(p), "clean" if not bad else "%d unglossed" % len(bad))))
        for t, ctx in bad:
            print("    %-18s ...%s..." % (t, ctx[:150]))
    sys.exit(1 if total else 0)
