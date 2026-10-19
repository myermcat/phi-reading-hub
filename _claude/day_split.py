"""Say which chapters belong to which class, so the question stops being asked.

The reading guide sets a week as one list and never says which class takes which chapter. The
professor posts one set of lecture notes per class day, so she does split them, and nothing
published says how. This halves her own list in her own order, which is the only ordering with
anything behind it, and says so.
"""
f = 'week-7/index.html'
h = open(f, encoding='utf-8').read()

BLOCK = '''
  <section id="s-days">
    <h2>Monday and Wednesday</h2>
    <p class="sidenote">The reading guide lists the four chapters for the week together and does not
    say which class takes which. This halves her list in the order she gives it, which comes out
    near enough even: 24 pages and 25.</p>
    <div class="plan">
      <div class="ses">
        <div class="when"><b>Monday</b><span>19 October</span></div>
        <div class="what">
          <h3>Du Ch&acirc;telet, then biology</h3>
          <p><b>Ch. 3</b>, printed pages 41 to 52, and <b>ch. 20</b>, printed 263 to 274. Twenty-four
          pages. Chapter 20 is the one that was in last week's guide, so if the week is tight it is
          the one you have mostly done. Chapter 3 is the easiest reading of the term.</p>
        </div>
      </div>
      <div class="ses">
        <div class="when"><b>Wednesday</b><span>21 October</span></div>
        <div class="what">
          <h3>Values in science, and who gets to do it</h3>
          <p><b>Ch. 15</b>, printed pages 201 to 215, and <b>ch. 19</b>, printed 250 to 259.
          Twenty-five pages. Chapter 15 carries the week's argument and is the one to read closely.</p>
        </div>
      </div>
    </div>
  </section>
'''

A = '  <section id="s-arg">'
assert A in h
h = h.replace(A, BLOCK.strip('\n') + '\n\n' + A, 1)

N = '<a class="grp" href="#s-arg">The argument</a>'
assert N in h
h = h.replace(N, '<a class="grp" href="#s-days">Monday &amp; Wednesday</a>\n  ' + N, 1)

open(f, 'w', encoding='utf-8').write(h)
print('day split added')
