"""Hint vocabulary, derived from the one glossary so the wording cannot drift.

MATCH maps the spelling a question stem might use to the glossary term it belongs to.
"""
from glossary import GROUPS

_BY_NAME = {}
for _gid, _title, _rows in GROUPS:
    for _term, _who, _short, _extra in _rows:
        _BY_NAME[_term] = _short

MATCH = {
 "normal science": "Normal science", "paradigm": "Paradigm",
 "disciplinary matrix": "Disciplinary matrix", "incommensurab": "Incommensurability",
 "anomal": "Anomaly", "whig history": "Whig history", "foundationalis": "Foundationalism",
 "induction": "Induction", "inductive": "Induction", "positivis": "Positivism",
 "empiricis": "Empiricism", "telos": "<span class='gk'>telos</span>",
 "physis": "<span class='gk'>physis</span>", "techne": "<span class='gk'>techne</span>",
 "episteme": "<span class='gk'>episteme</span>", "empeiria": "<span class='gk'>empeiria</span>",
 "atechnia": "<span class='gk'>atechnia</span>", "dialectic": "Dialectic",
 "metaphysic": "Metaphysics", "genealog": "Genealogy", "normaliz": "Normalization",
 "power-knowledge": "Power-knowledge", "hierarchical observation": "Three techniques of control",
 "docile": "Docile bodies", "utilitarian": "Utilitarianism", "panopticon": "Panopticon",
 "kalliopolis": "Kalliopolis", "ad hoc": "Ad hoc", "contingent": "Contingent",
 "nominalis": "Kinds: realist against nominalist", "constructivis": "Constructivism",
 "co-produc": "Co-production", "heterogeneous": "Heterogeneous engineering",
 "stratificat": "Stratification", "cumulative advantage": "Cumulative advantage",
 "meritocra": "Meritocracy", "epistemolog": "Epistemology",
 "instrumentalis": "Instrumentalism", "deism": "Deism", "dualis": "Dualism",
 "knorr cetina": "Knorr Cetina", "social construction": "Social construction",
}

missing = sorted({v for v in MATCH.values()} - set(_BY_NAME))
assert not missing, "MATCH points at terms the glossary does not define: %s" % missing

# Ordinary vocabulary a question leans on. Explained in the hint, left off the cheat
# sheet, which is for the course's own terms. The definitions are deliberately neutral,
# so that defining a word in an option does not hand over the answer.
PLAIN = {
 "theological": ("Theological", "to do with God or the gods"),
 "metaphysical, then positive": ("Positive, in this sense", "limited to what can be observed and measured"),
 "extension": ("Extension", "taking up space. The technical word for physical stuff, used as the opposite of thinking"),
 "unilinear": ("Unilinear", "running in one direction, with no going back round"),
 "non-contextual": ("Non-contextual", "where and when the work was done should make no difference to the result"),
 "analytic": ("Analytic", "separating something into parts and examining one at a time"),
 "semantic": ("Semantic", "to do with what words mean"),
 "appositive": ("Appositive", "a phrase placed beside a noun to explain it"),
 "aristocrat": ("Aristocratic", "from the land-owning ruling families"),
 "cyclical": ("Cyclical", "going round in a circle and returning to where it started"),
 "intelligible": ("Intelligible", "reachable by thought alone, with no help from the senses"),
 "sensible world": ("Sensible", "reachable by the senses: what can be seen, heard or touched"),
 "corporeal": ("Corporeal", "having a body, physical"),
 "annular": ("Annular", "ring-shaped"),
 "furtive": ("Furtive", "hidden, done without being seen"),
 "menagerie": ("Menagerie", "a private collection of animals kept for display"),
 "postdoctoral": ("Postdoctoral", "the research post taken straight after a doctorate"),
 "primatology": ("Primatology", "the study of monkeys and apes"),
}

GLOSS = {k: (MATCH[k], _BY_NAME[MATCH[k]]) for k in MATCH}
GLOSS.update(PLAIN)
