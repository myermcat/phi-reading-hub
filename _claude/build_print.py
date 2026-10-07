"""The printable cheat sheet: two sides of A4, the map then the glossary.

Reads the same glossary.py the web page and the question hints read, then applies
the print cuts in print_data.py. Nothing is written twice.
"""
import os, re, sys
HERE = os.path.dirname(os.path.abspath(__file__)); REPO = os.path.dirname(HERE)
sys.path.insert(0, HERE)
from glossary import GROUPS
from print_data import DROP_GROUPS, DROP, SHORT, MAP, TWICE

# Tuned by rendering at A4 and measuring the overflow. Capacity goes with the square
# of the type size, so a page that needs 1.5 times the room needs type 1.23 times smaller.
P1_FONT, P1_COLS = "7.9pt", 3
P2_FONT, P2_COLS = "6.35pt", 3

CSS = """
@page { size: A4 portrait; margin: 7mm; }
:root{--ink:#17201b;--soft:#3c4a42;--mute:#6d7a72;--rule:#c9d4cd;--hair:#e2e9e4;
      --green:#1a6450;--wash:#e8f1ec;--violet:#5b3f86;--vwash:#efeaf7;--amber:#8a5d12}
*{box-sizing:border-box}
html,body{margin:0;padding:0;background:#fff;color:var(--ink);
  font-family:"Source Sans 3","Helvetica Neue",Arial,sans-serif;
  font-size:7.2pt;line-height:1.3;-webkit-print-color-adjust:exact;print-color-adjust:exact}
.page{width:196mm;height:283mm;overflow:hidden;position:relative}
.page + .page{page-break-before:always;break-before:page}
.top{display:flex;align-items:baseline;justify-content:space-between;gap:4mm;
  border-bottom:.5pt solid var(--green);padding-bottom:1.1mm;margin-bottom:2.2mm}
.top h1{margin:0;font-size:11pt;font-weight:600;letter-spacing:-.01em;color:var(--green)}
.top .sub{font-size:6.6pt;color:var(--mute)}
.cols{column-gap:4.2mm;height:275mm}
.cols.m{column-count:__P1C__;font-size:__P1F__;line-height:1.3}
.cols.m .card h3{font-size:calc(__P1F__ * 1.14)}
.cols.m .card h3 .n,.cols.m .card h3 .yr{font-size:calc(__P1F__ * 0.88)}
.cols.m .card .q{font-size:calc(__P1F__ * 0.96)}
.cols.m .lead{font-size:calc(__P1F__ * 0.92)}
.cols.m h2.grp{font-size:calc(__P1F__ * 1.12)}
.cols.g{column-count:__P2C__;font-size:__P2F__;line-height:1.28}
.cols.g h2.grp{font-size:calc(__P2F__ * 1.14)}
.cols.g .who{font-size:calc(__P2F__ * 0.9)}
.card{break-inside:avoid;margin:0 0 1.9mm;padding:1.3mm 1.6mm;background:var(--wash);
  border-left:1.2pt solid var(--green);border-radius:0}
.card.c{background:var(--vwash);border-left-color:var(--violet)}
.card h3{margin:0 0 .5mm;font-size:8pt;font-weight:600;color:var(--green);display:flex;gap:1.2mm;align-items:baseline}
.card.c h3{color:var(--violet)}
.card h3 .n{font-size:6.4pt;opacity:.75}
.card h3 .yr{font-size:6.2pt;font-weight:400;color:var(--mute);margin-left:auto;text-align:right}
.card .q{font-style:italic;color:var(--soft);margin:0 0 .6mm;font-size:6.9pt}
.card ul{margin:0;padding-left:2.6mm;list-style:none}
.card li{margin:0 0 .45mm;color:var(--soft);position:relative}
.card li::before{content:"";position:absolute;left:-2.2mm;top:1.5mm;width:1mm;height:1mm;
  background:var(--green);border-radius:50%}
.card.c li::before{background:var(--violet)}
.lead{break-inside:avoid;margin:0 0 1.9mm;padding-left:2.2mm;font-size:6.5pt;font-style:italic;color:var(--mute)}
.lead::before{content:"\\2193  ";font-style:normal;color:var(--green)}
h2.grp{break-inside:avoid;break-after:avoid;margin:0 0 1mm;font-size:8pt;font-weight:600;color:#fff;
  background:var(--green);padding:.7mm 1.4mm;letter-spacing:.01em}
h2.grp.first{margin-top:0}
h2.grp:not(.first){margin-top:2.4mm}
.t{break-inside:avoid;margin:0 0 1.3mm}
.t b.term{color:#0c3f31;font-weight:600;background:#c4e3d4;padding:0 .7mm;font-size:calc(__P2F__ * 1.12)}
.t .who{color:var(--mute);font-size:6.2pt}
.t span.d{color:var(--soft)}
.tw{break-inside:avoid;margin:0 0 1.4mm;padding:1.3mm 1.6mm;background:#f6f3ec;border-left:1.2pt solid var(--amber)}
.tw b.n{color:var(--amber)}
.foot{position:absolute;bottom:0;left:0;right:0;font-size:5.8pt;color:var(--mute);
  border-top:.4pt solid var(--hair);padding-top:.8mm}
b{font-weight:600}
"""

def card(n, name, yr, q, lines, lead, critic):
    cls = "card c" if critic else "card"
    li = "".join("<li>%s</li>" % x for x in lines)
    out = ('<div class="%s"><h3><span class="n">%d</span>%s<span class="yr">%s</span></h3>'
           '<p class="q">%s</p><ul>%s</ul></div>') % (cls, n, name, yr, q, li)
    if lead:
        out += '<p class="lead">%s</p>' % lead
    return out

def glossary_html():
    out, first = [], True
    for gid, title, rows in GROUPS:
        if gid in DROP_GROUPS:
            continue
        rows = [r for r in rows if r[0] not in DROP]
        if not rows:
            continue
        out.append('<h2 class="grp%s">%s</h2>' % (" first" if first else "", title)); first = False
        for term, who, short, extra in rows:
            s, e = SHORT.get(term, (short, extra))
            body = s[0].upper() + s[1:] + "."
            if e:
                body += " " + e
            w = ' <span class="who">%s</span>' % who if who else ""
            out.append('<p class="t"><b class="term">%s</b>%s <span class="d">%s</span></p>' % (term, w, body))
    return "".join(out)

def build():
    p1 = ['<div class="page"><div class="top"><h1>PHI2394 &middot; exam 1 &middot; the map</h1>'
          '</div><div class="cols m">']
    for n, name, yr, q, lines, lead, critic in MAP:
        p1.append(card(n, name, yr, q, lines, lead, critic))
    p1.append('<h2 class="grp">Who turns up twice</h2>')
    for name, times, body in TWICE:
        p1.append('<div class="tw"><b class="n">%s</b> <span class="who">%s</span><br>%s</div>' % (name, times, body))
    p1.append('</div></div>')

    p2 = ['<div class="page"><div class="top"><h1>PHI2394 &middot; exam 1 &middot; the glossary</h1>'
          '</div>'
          '<div class="cols g">', glossary_html(), '</div></div>']

    html = ('<!doctype html><html lang="en"><meta charset="utf-8">'
            '<title>PHI2394 Exam 1 Cheat Sheet, print</title>'
            '<link rel="stylesheet" href="https://fonts.googleapis.com/css2?'
            'family=Source+Sans+3:wght@400;600&display=swap">'
            '<style>%s</style>%s%s</html>') % (
                CSS.replace("__P1F__", P1_FONT).replace("__P1C__", str(P1_COLS))
                   .replace("__P2F__", P2_FONT).replace("__P2C__", str(P2_COLS)),
                "".join(p1), "".join(p2))
    path = os.path.join(REPO, "exam-1", "print.html")
    open(path, "w", encoding="utf-8").write(html)
    return path, len(html)

if __name__ == "__main__":
    p, n = build()
    print("built", os.path.relpath(p, REPO), n, "bytes")
