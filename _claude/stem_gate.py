"""A question stem asks about the world. Never about who said it in a room.

The student has objected to this three times. It keeps coming back because a stem
written straight from a set of lecture notes inherits their voice, so this runs on
every build.
"""
import re, sys, os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

# "What did she mean?" after naming Karin Knorr Cetina is ordinary English, so the
# patterns below name the lecture-voice phrases and leave a pronoun with an antecedent alone.
BANNED = [
 r"\bthe professor\b", r"\bthe lecture (said|spent|gave|told)\b",
 r"\b(she|he) (said|told|quoted|stressed|noted|gave|drew|brought|offered|called|described|listed|framed)\b",
 r"\bdid (she|he) (say|name|call|give|list|stress|note)\b",
 r"\bin (her|his) (notes|wording|words|framing|formulation|terms|list|own)\b",
 r"\bon (her|his) (own )?slide\b", r"\b(her|his) (examples?|conclusion|verdict|framing|summary|point)\b",
 r"\bwhat was (her|his) (notes?|wording|words|framing|formulation|conclusion|verdict|point|summary|examples?)\b",
 r"\b(the|this) (packet|lecture|class|slides?)\b", r"\b(the|this) course\b(?! of)", r"\bweek \d\b", r"\bthis (term|week's)\b",
 r"\bfirst-class slides\b", r"\bon the reading list\b",
]
def scan(stem):
    plain = re.sub(r"<[^>]+>", " ", stem)
    return [p for p in BANNED if re.search(p, plain, re.I)]

if __name__ == "__main__":
    from bank_week2 import WEEK2
    from bank_week3 import WEEK3
    from bank_week4 import WEEK4
    from bank_mixed import MIXED
    bad = 0
    for name, bank in [("week2", WEEK2), ("week3", WEEK3), ("week4", WEEK4), ("mixed", MIXED)]:
        for n, q in enumerate(bank, 1):
            hits = scan(q[1])
            if hits:
                bad += 1
                print("  %s q%-2d  %s" % (name, n, re.sub(r"<[^>]+>", "", q[1])[:96]))
                print("        matched: %s" % ", ".join(hits))
    print("stems asking about the room:", bad)
    sys.exit(1 if bad else 0)
