"""Anything a question tests has to be findable on the cheat sheet.

The student hit a question about the Vienna Circle, went to look it up, and the
cheat sheet named it once in passing with no entry. A practice set that tests
something the revision page does not carry is a trap.
"""
import os, re, sys
HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
from bank_week2 import WEEK2
from bank_week3 import WEEK3
from bank_week4 import WEEK4
from bank_mixed import MIXED

# Words that look like names and carry no course content.
STOP = set("""The This That What Which Who How Why When Where Her His She He It They Both Three Four Two
One Notice Note Ask Picture Compare Think Take Worth Read Every Each Nothing Correct Too Far Real Half
Under Here Something Between From Around Once Leaving Calling Learning Saying Given Progress Break
Places Losing Backlighting Whose Only After Before Their There Then Than Also Even Still Other Same
Against Because Before Being Most Much More Less Just Such Does Will Would Could Should American
English French German Greek Greeks Western European Christian Dutch Australia Athens Athenian Europe
Rome Kevin United States Weeks Standardized Genealogical Explanation Sensible Intelligible Thought
Enlightenment Ethics Novum Organum Science Nature Order Form Forms Chapter Claims Institutional
Roughly Smaller Genders Feminisation Harvard Greece Kuhnian Platonic Second Gods Scientists Women
Researchers Discipline Normal Puzzle Material Knowledge Truth Power Prisoners Education Hierarchical
Watch Rank Record Both Half Where Into Over Many Some None With Without Within Mass Planet Burning
Plenty Each Either Neither Three Four Five Several Authorship Economic Fear Give Once Labour Compare""".split())
NAME = re.compile(r"\b[A-Z][a-z]{3,}(?:\s+[A-Z][a-z]{3,})*\b")

def names_in(text):
    out = set()
    for m in NAME.findall(re.sub(r"<[^>]+>", " ", text)):
        m = m.strip()
        if m in STOP or m.split()[0] in STOP:
            continue
        out.add(m)
    return out

if __name__ == "__main__":
    cs = re.sub(r"\s+", " ", re.sub(r"<[^>]+>", " ",
         open(os.path.join(os.path.dirname(HERE), "exam-1", "cheat-sheet.html"), encoding="utf-8").read()))
    missing = {}
    for label, bank in [("week2", WEEK2), ("week3", WEEK3), ("week4", WEEK4), ("mixed", MIXED)]:
        for n, (topic, stem, opts, a, hint) in enumerate(bank, 1):
            for nm in names_in(stem + " " + opts[a - 1][0]):
                # "Karin Knorr Cetina" is covered by an entry headed "Knorr Cetina"
                surname = nm.split()[-1]
                if nm.lower() not in cs.lower() and surname.lower() not in cs.lower():
                    missing.setdefault(nm, []).append("%s q%d" % (label, n))
    for nm in sorted(missing):
        print("  %-30s tested in %s" % (nm, ", ".join(missing[nm][:3])))
    print("tested and absent from the cheat sheet:", len(missing))
    sys.exit(1 if missing else 0)
