"""Assemble the cheat sheet: fixed head, generated nav, the map, the generated glossary.

The glossary comes from glossary.py, which is the same file the practice-question hints
read, so a term reads identically in both places.
"""
import os, re, sys
HERE = os.path.dirname(os.path.abspath(__file__))
REPO = os.path.dirname(HERE)
sys.path.insert(0, HERE)
from glossary import GROUPS

PEOPLE = [("p-plato","Plato"),("p-aristotle","Aristotle"),("p-middle-ages","The Middle Ages"),
          ("p-copernicus","Copernicus"),("p-bacon","Bacon"),("p-rousseau","Rousseau"),
          ("p-bentham","Bentham"),("p-positivism","Positivism"),("p-kuhn","Kuhn"),
          ("p-foucault","Foucault"),("p-construction","Social construction")]

def nav():
    out = ['  <nav class="rail" aria-label="On this page">',
           '    <div class="k">On this page</div>',
           '    <a href="#map">The map</a>']
    for i, (pid, name) in enumerate(PEOPLE, 1):
        out.append('    <a class="sub" href="#%s"><i>%d</i>%s</a>' % (pid, i, name))
    out.append('    <a href="#twice">Who turns up twice</a>')
    for gid, title, _ in GROUPS:
        out.append('    <a href="#%s">%s</a>' % (gid, title))
    out.append('  </nav>')
    return "\n".join(out) + "\n"

def glossary():
    out = []
    for gid, title, rows in GROUPS:
        out.append('    <section>')
        out.append('      <h2 id="%s">%s</h2>' % (gid, title))
        out.append('      <dl>')
        for term, who, short, extra in rows:
            w = '<span class="who">%s</span>' % who if who else ''
            body = short[0].upper() + short[1:] + '.'
            if extra:
                body += ' ' + extra
            out.append('        <div><dt>%s%s</dt><dd>%s</dd></div>' % (term, w, body))
        out.append('      </dl>')
        out.append('    </section>')
        out.append('')
    return "\n".join(out)

def read(n):
    return open(os.path.join(HERE, n), encoding='utf-8').read()

if __name__ == "__main__":
    page = (read('_cheat_head.html') + nav() + read('_cheat_mid.html').replace('  </nav>','',1)
            + read('_map_section.html') + glossary() + read('_cheat_tail.html'))
    p = os.path.join(REPO, 'exam-1', 'cheat-sheet.html')
    open(p, 'w', encoding='utf-8').write(page)
    n = sum(len(g[2]) for g in GROUPS)
    print('built cheat-sheet.html,', n, 'glossary terms,', len(page), 'bytes')
