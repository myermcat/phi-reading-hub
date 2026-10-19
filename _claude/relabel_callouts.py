"""A callout label states the thing. It does not point at it.

Every one of these was a pointer: "the claim this week attacks", "the sentence that saves the
theory", "her flat version of it". The reader has to read the block to find out what the label
meant, which is the same fault as a section heading reading "The argument".
"""
L = {
 '_done_week-6': [
  ('The claim this week attacks',
   'Method cancels out the person running it'),
  ('What this leaves of objectivity',
   'Objectivity can no longer mean a method anyone could run'),
  ('Why this is not a story about bad scientists',
   'Peer-reviewed work, done properly, produced this'),
  ('The sentence that saves the theory from being silly',
   'A standpoint is earned, and identity alone does not give you one'),
  ('The question that opens the field',
   'Why did any of this count as news?'),
  ("Tuana's own caveat",
   'One case can sit in several of the five kinds at once'),
  ('The difficulty the chapter raises against itself',
   'Discrediting looks exactly like asking a fair question'),
 ],
 'week-7/index.html': [
  ('The rule this week is dismantling',
   'The value-free ideal, the rule all four chapters reject'),
  ('Nobody in this story is a villain',
   'Careful people following the rules produced sixty years of this'),
  ('The asymmetry Giordano puts plainly',
   'Germany was condemned for its experiments and the United States defended its bomb'),
  ('A correction she makes to her own side',
   'Treating women as one group has meant white middle-class women'),
  ('Her flat version of it',
   'Without hypotheses there would be no astronomy'),
  ("Ruth Hubbard's line, which is the one to remember",
   'Women got a free evolutionary ride on the backs of men'),
  ("Altmann's conclusion, stated against the field she was in",
   'What the females do drives the group, and the male drama does not'),
  ("Nelson's answer, and it is the most important sentence in the chapter",
   'The work was not careless, and there was other evidence to be had'),
  ('The complication Nelson states against her own case',
   'Women in these fields who deny feminism had any part in the change'),
 ],
}
for f, pairs in L.items():
    h = open(f, encoding='utf-8').read()
    for old, new in pairs:
        a = '<b>' + old + '</b>'
        assert a in h, (f, old)
        h = h.replace(a, '<b>' + new + '</b>', 1)
    open(f, 'w', encoding='utf-8').write(h)
    print('%-20s %d labels now state the thing' % (f, len(pairs)))
