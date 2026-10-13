"""Pointing at the exam inside the prose tells the reader nothing about the argument.
The one place it belongs is the My note block, which exists for it."""
FIX = {
 'week-5/index.html': [
   ("The field this belongs to has a name you will not have met, and it is almost certainly examinable.",
    "The field this belongs to has a name you will not have met."),
 ],
 'week-6/index.html': [
   (" The nine phases and the three names are the most examinable content in the term so far.", ""),
   ("<b>Two warnings they attach to the list, and both are the kind of thing an exam asks for.</b>",
    "<b>Two warnings they attach to the list.</b>"),
   ("<b>And the definition to write down.</b> The two words are the examinable pair in this section.",
    "<b>And the definition to write down.</b> The two words are a pair, and the second is defined against the first."),
   (" The field has a name, a five-part taxonomy and five production strategies, all of which are the kind of thing an examiner can ask you to list.",
    " The field has a name, a five-part taxonomy and five production strategies."),
   ("<b>Nancy Tuana, whose five kinds are the thing to memorise from this chapter.</b>",
    "<b>Nancy Tuana, whose five kinds are the spine of this chapter.</b>"),
 ],
 'week-7/index.html': [
   (" The two on the right differ in one thing, which is worth getting straight before the exam.",
    " The two on the right differ in one thing."),
   ("Chapter 15 is the one the exam will come from.", "Chapter 15 carries the week's argument."),
   (" Each comes with a case, and the cases are better revision than the headings.",
    " Each comes with a case, and the case is where the argument is."),
 ],
}
for f, pairs in FIX.items():
    h = o = open(f, encoding='utf-8').read()
    for a, b in pairs:
        assert a in h, (f, a[:50])
        h = h.replace(a, b, 1)
    open(f, 'w', encoding='utf-8').write(h); print('cleaned', f)
