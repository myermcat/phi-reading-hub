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
 "nominalis": "Nominalist and realist about kinds", "constructivis": "Constructivism",
 "co-produc": "Co-production", "heterogeneous": "Heterogeneous engineering",
 "stratificat": "Stratification", "cumulative advantage": "Cumulative advantage",
 "meritocra": "Meritocracy", "epistemolog": "Epistemology",
 "instrumentalis": "Instrumentalism", "deism": "Deism", "dualis": "Dualism",
 "knorr cetina": "Knorr Cetina", "social construction": "Social construction",
}

missing = sorted({v for v in MATCH.values()} - set(_BY_NAME))
assert not missing, "MATCH points at terms the glossary does not define: %s" % missing

GLOSS = {k: (MATCH[k], _BY_NAME[MATCH[k]]) for k in MATCH}
