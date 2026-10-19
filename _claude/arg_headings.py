"""The week's question becomes the heading.

Every guide's most important line sat in body text under a heading reading "The argument", which
is the same on every week and says nothing. The heading pass that fixed 4.1 through 3.5 only ran
inside the chapters and never touched the sections above them.
"""
F = {
 'week-5/index.html': (
   '<h2>The argument</h2>',
   '<h2>What happened when women started watching the female monkeys</h2>'),
 'week-6/index.html': (
   '<h2>The argument</h2>',
   '<h2>Where does a value get in, and what happens to what nobody looked for?</h2>'),
 'week-7/index.html': (
   '<h2>The argument</h2>',
   '<h2>If values cannot be kept out, what stops science being a free-for-all?</h2>'),
}
for f, (old, new) in F.items():
    h = open(f, encoding='utf-8').read()
    assert h.count(old) == 1, (f, h.count(old))
    open(f, 'w', encoding='utf-8').write(h.replace(old, new, 1))
    print('%-20s %s' % (f, new[4:-5]))

# the nav entry should say the same thing the heading does, in fewer words
N = {
 'week-5/index.html': ('<a class="grp" href="#s-arg">The argument</a>',
                       '<a class="grp" href="#s-arg">Watching the females</a>'),
 'week-6/index.html': ('<a class="grp" href="#s-arg">The argument</a>',
                       '<a class="grp" href="#s-arg">Where a value gets in</a>'),
 'week-7/index.html': ('<a class="grp" href="#s-arg">The argument</a>',
                       '<a class="grp" href="#s-arg">The free-for-all problem</a>'),
}
for f, (old, new) in N.items():
    h = open(f, encoding='utf-8').read()
    assert old in h, f + ' nav'
    open(f, 'w', encoding='utf-8').write(h.replace(old, new, 1))
print('nav entries renamed')
