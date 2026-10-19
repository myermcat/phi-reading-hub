"""Say what happened. The metaphor is never clearer than the thing it stands for."""
S = {
 'week-7/index.html': [
  ('<b>Week 6 killed it.</b> Chapter 4 cut research into nine phases and found a person',
   '<b>Week 6 showed that no research works that way.</b> Chapter 4 divided research into nine phases and found a person'),
  ('what stops a tobacco company or a creationist calling their politics science?',
   'what stops a tobacco company or a creationist calling their politics science?'),
  ('replacement for it. <b>Three attempts to pay that debt follow, and the third changes the\n      subject.</b>',
   'replacement for it. <b>Three replacements follow, and the third changes the question.</b>'),
  ('<b>That is why feminists went after it, where noting it was inaccurate would have been\n      enough for anybody else.</b>',
   '<b>That is why feminists wanted it removed, where calling it inaccurate would have been\n      enough for anybody else.</b>'),
  ('and cannot be scrubbed out,', 'and cannot be removed,'),
  ('<b>doing a job</b>: it shut three\n      arguments down without anybody having to answer them.',
   '<b>useful</b>: it let three arguments be dismissed without anybody answering them.'),
  ('useful for dismissing those\n      three arguments without answering them.',
   'and it let those three arguments be dismissed unanswered.'),
  ('The answer, in the framework Detlefsen uses: two camps, and the fight was about whether hypotheses are allowed at all.',
   'The answer, in the framework Detlefsen uses: two camps, and the dispute was about whether hypotheses are allowed at all.'),
 ],
 'week-6/index.html': [
  ('Grant that scientists are ordinary people carrying ordinary opinions.',
   'Grant that scientists are ordinary people with ordinary opinions.'),
 ],
}
for f, pairs in S.items():
    h = open(f, encoding='utf-8').read()
    n = 0
    for old, new in pairs:
        if old == new or old not in h:
            continue
        h = h.replace(old, new, 1); n += 1
    open(f, 'w', encoding='utf-8').write(h)
    print('%-20s %d replaced' % (f, n))
