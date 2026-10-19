"""Say what the phrase means at the point the reader meets it.

The section opened on "once you admit that values are inside science and cannot be removed",
which compresses the whole of week 6 into four words and never says that is what it is doing.
A reader who has read week 6 has no way to tell she already knows this.
"""
f = 'week-7/index.html'; h = open(f, encoding='utf-8').read()

OLD = '''<p class="lede">The question this week settles: once you admit that values are inside science and cannot be removed, what stops it being a free-for-all?</p>'''
NEW = '''<p class="lede">This week inherits a problem from last week and has to solve it.</p>

    <dl class="facts">
      <dt>A value, here</dt>
      <dd>A judgment about what matters, made by a person, which the data does not settle. That
      skin which ages is a health problem worth treating. That this much evidence is enough to
      publish. That the rod and frame test measures spatial ability.</dd>
      <dt>Inside science</dt>
      <dd>Inside the part everyone thought was sealed. Nobody ever denied that values pick which
      topics get funded. The claim under attack is that once you are weighing evidence, deciding
      which theory it supports and deciding what to accept, values are out.</dd>
      <dt>What week 6 found</dt>
      <dd><b>They are not out.</b> Chapter 4 cut research into nine phases and showed a person
      deciding at every one, with nothing in nature deciding for them. Twenty years of the rod and
      frame test is that happening in public, done by careful people following the rules.</dd>
    </dl>

    <div class="body">
      <p><b>So the sealed part is not sealed, and the objection arrives immediately.</b> If values
      are in the core and cannot be scrubbed out, what stops anybody calling their politics science?
      A tobacco company, a creationist, anyone. That is week 5's relativism worry coming back with
      teeth, and a week that removes a rule owes a replacement.</p>
    </div>'''
assert OLD in h
h = h.replace(OLD, NEW, 1)

# the old opening paragraph now repeats what the block above says
OLD2 = '''<p><b>The answer the week gives.</b> You replace the rule that values must be absent with rules about <em>which</em> values are allowed and who gets to argue about them. Two such rules are on offer, and they disagree about how much to demand.</p>'''
NEW2 = '''<p><b>The answer the week gives.</b> You replace the rule that values must be absent with rules about <em>which</em> values are allowed and who gets to argue about them. Two such rules are on offer, and they disagree about how much to demand.</p>
      <p><b>One line to hold on to.</b> Last week removed the rule that values must be absent. This week has to say which values are allowed, and who gets to argue about them.</p>'''
assert OLD2 in h
h = h.replace(OLD2, NEW2, 1)

open(f, 'w', encoding='utf-8').write(h)
print('opening rewritten')
