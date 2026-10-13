"""Number the h4s inside each chapter, give them ids, and list them in the side nav.

The nav already existed on every guide. It was hidden under a 1180px window, it stopped at
chapter level, and h4 was styled as a 10.5px mono label, which put it below the green lead-in
of the paragraph underneath it. Scrolling a chapter gave no sense of rank.
"""
import re, sys, html as H

CSS_OLD = '  .rd h4 { margin: 8px 0 -7px; font-family: var(--mono); font-size: 10.5px; letter-spacing: 0.1em; text-transform: uppercase; color: var(--muted); font-weight: 500; }'
CSS_NEW = '''  .rd h4 { margin: 16px 0 -13px; font-family: var(--display); font-weight: 600;
           font-size: 20px; line-height: 1.22; letter-spacing: -0.005em; color: var(--ink);
           text-wrap: balance; scroll-margin-top: 78px; }
  .rd h4::before { content: attr(data-n); display: block; margin-bottom: 6px;
           font-family: var(--mono); font-size: 10.5px; font-weight: 500;
           letter-spacing: 0.12em; color: var(--accent); }'''

H5_OLD = '  .rd .body h5 { margin: 12px 0 -4px; font-family: var(--display); font-weight: 600; font-size: 18.5px; line-height: 1.25; color: var(--ink); letter-spacing: -.005em; }'
H5_NEW = '  .rd .body h5 { margin: 14px 0 -4px; font-family: var(--display); font-weight: 600; font-size: 16.5px; line-height: 1.3; color: var(--ink-soft); letter-spacing: 0; }'

NAV_OLD = '  @media (min-width: 1180px) { #nav { display: flex; } }'
NAV_NEW = '''  @media (min-width: 1180px) { #nav { display: flex; } }
  @media (min-width: 1000px) and (max-width: 1179px) {
    #nav { display: flex; left: 12px; }
    body { padding-left: 150px; }
  }
  #nav { top: 84px; transform: none; max-height: calc(100vh - 160px);
         overflow-y: auto; scrollbar-width: none; }
  #nav::-webkit-scrollbar { display: none; }
  #nav a.sb { display: none; font-size: 9.5px; letter-spacing: .02em; line-height: 1.32;
              padding: 3px 0 3px 11px; margin-left: 9px; opacity: .9; }
  #nav a.sb.show { display: block; }
  #nav a.sb b { font-weight: 500; font-style: normal; color: var(--rule);
                margin-right: 5px; }
  #nav a.sb:hover b, #nav a.sb.on b { color: var(--accent); }'''


def patch(f):
    h = open(f, encoding='utf-8').read()
    if 'data-n=' in h:
        print('already done:', f); return

    subs = []           # (chapter anchor, h4 id, number, title)
    def one_article(m):
        art = m.group(0)
        aid = re.search(r'id="([^"]+)"', art).group(1)
        chn = re.search(r'class="ch">CH\s*(\d+)', art)
        chn = chn.group(1) if chn else ''
        n = [0]
        def h4(mm):
            n[0] += 1
            num = ('%s.%d' % (chn, n[0])) if chn else str(n[0])
            had = re.search(r'id="([^"]+)"', mm.group(1) or '')
            hid = had.group(1) if had else '%s-%d' % (aid, n[0])
            title = re.sub(r'<[^>]+>', '', mm.group(2)).strip()
            subs.append((aid, hid, num, title))
            return '<h4 id="%s" data-n="%s">%s</h4>' % (hid, num, mm.group(2))
        return re.sub(r'<h4( [^>]*)?>(.*?)</h4>', h4, art, flags=re.S)

    h = re.sub(r'<article class="rd[^"]*" id="[^"]+">.*?\n      </article>',
               one_article, h, flags=re.S)
    assert subs, f

    for old, new, must in ((CSS_OLD, CSS_NEW, 1), (H5_OLD, H5_NEW, 0), (NAV_OLD, NAV_NEW, 1)):
        assert old in h or not must, (f, old[:40])
        h = h.replace(old, new, 1)

    # hang each chapter's sections under its own nav entry
    for aid in dict.fromkeys(a for a, _, _, _ in subs):
        nav = re.search(r'<nav id="nav".*?</nav>', h, re.S)
        link = re.search(r'<a [^>]*href="#%s"[^>]*>.*?</a>' % re.escape(aid),
                         h[nav.start():nav.end()], re.S)
        if not link:            # single-chapter weeks already list their h4s in the nav
            continue
        at = nav.start() + link.end()
        rows = ''.join(
            '\n  <a class="sb" data-of="%s" href="#%s"><b>%s</b>%s</a>' % (a, i, nn, H.escape(t))
            for a, i, nn, t in subs if a == aid)
        h = h[:at] + rows + h[at:]

    open(f, 'w', encoding='utf-8').write(h)
    print('patched %s, %d subsections' % (f, len(subs)))

for f in sys.argv[1:]:
    patch(f)
