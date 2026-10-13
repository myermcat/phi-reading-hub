"""Mark every word that has a glossary entry anywhere in the hub, and define it on click."""
import glob, re

CSS = '''
  /* A word defined in any week's glossary. The line is meant to be ignorable until wanted. */
  .gl-w { border-bottom: 1px dashed var(--gl-line); cursor: pointer; }
  .gl-w:hover { border-bottom-color: var(--accent); }
  #gl-pop[hidden] { display: none !important; }
  #gl-pop { position: absolute; z-index: 80; width: 330px; max-width: calc(100vw - 24px);
            background: var(--surface); border: 1px solid var(--rule); border-radius: 6px;
            box-shadow: 0 6px 22px rgba(0,0,0,.28); padding: 13px 15px 14px; }
  #gl-pop .t { font-family: var(--mono); font-size: 10.5px; letter-spacing: .1em;
               text-transform: uppercase; color: var(--accent); margin-bottom: 6px; }
  #gl-pop .d { font-family: var(--body); font-size: 14.5px; line-height: 1.5; color: var(--ink-soft); }
  #gl-pop .d b { color: var(--ink); font-weight: 600; }
  #gl-pop .w { margin-top: 9px; font-family: var(--mono); font-size: 10px; color: var(--muted); }
  @media print { .gl-w { border-bottom: 0; } #gl-pop { display: none !important; } }
'''

JS = r'''
<script src="../glossary.js"></script>
<script>
/* Every term defined in any week's glossary gets a faint dashed underline here, and its
   definition on click. This runs after the highlighter has restored, and skips anything inside
   a mark, so the two never fight over the same text nodes. */
(function () {
  var G = window.PHI_GLOSSARY;
  var root = document.querySelector('.wrap');
  if (!G || !G.length || !root) return;

  var SKIP = '.gl, .nb, .cmt, #nav, .site, .sitefoot, .dock, a, h1, h2, h3, h4, h5, summary, .cred, mark, code, .gl-w, .dg-t, .mynote, .nbhint';
  var BLOCK = 'p, li, td, th, dd, figcaption, blockquote, .keep, .qa, .why, .kone, .bq';

  var pairs = [];
  G.forEach(function (e, i) { e.f.forEach(function (w) { pairs.push([w, i]); }); });
  pairs.sort(function (a, b) { return b[0].length - a[0].length; });
  var idx = {};
  pairs.forEach(function (p) { if (!(p[0].toLowerCase() in idx)) idx[p[0].toLowerCase()] = p[1]; });
  function esc(s) { return s.replace(/[.*+?^${}()|[\]\\]/g, '\\$&'); }
  var rx;
  try {
    rx = new RegExp('(?<![\\w-])(' + pairs.map(function (p) { return esc(p[0]); }).join('|') + ')(?![\\w-])', 'gi');
  } catch (e) { return; }   // a browser without lookbehind simply gets no underlines

  var nodes = [], w = document.createTreeWalker(root, NodeFilter.SHOW_TEXT, null), n;
  while ((n = w.nextNode())) {
    if (!n.nodeValue || n.nodeValue.length < 4) continue;
    var p = n.parentElement;
    if (!p || p.closest(SKIP)) continue;
    nodes.push(n);
  }

  var seen = new Map();          // one mark per term per block, so a page is not all dashes
  nodes.forEach(function (node) {
    var block = node.parentElement.closest(BLOCK) || node.parentElement;
    var done = seen.get(block);
    if (!done) { done = new Set(); seen.set(block, done); }
    var text = node.nodeValue, m, hits = [];
    rx.lastIndex = 0;
    while ((m = rx.exec(text))) {
      var i = idx[m[1].toLowerCase()];
      if (i === undefined || done.has(i)) continue;
      done.add(i);
      hits.push([m.index, m.index + m[1].length, i]);
    }
    for (var k = hits.length - 1; k >= 0; k--) {
      var a = hits[k][0], b = hits[k][1];
      var tail = node.splitText(a);
      if (b - a < tail.nodeValue.length) tail.splitText(b - a);
      var s = document.createElement('span');
      s.className = 'gl-w';
      s.setAttribute('data-g', hits[k][2]);
      tail.parentNode.insertBefore(s, tail);
      s.appendChild(tail);
    }
  });

  var pop = document.createElement('div');
  pop.id = 'gl-pop'; pop.hidden = true;
  document.body.appendChild(pop);

  function hide() { pop.hidden = true; }
  function show(el) {
    var e = G[+el.getAttribute('data-g')];
    if (!e) return;
    pop.innerHTML = '';
    var t = document.createElement('div'); t.className = 't'; t.textContent = e.t;
    var d = document.createElement('div'); d.className = 'd'; d.innerHTML = e.d;
    var k = document.createElement('div'); k.className = 'w'; k.textContent = 'Glossary, week ' + e.w;
    pop.appendChild(t); pop.appendChild(d); pop.appendChild(k);
    pop.hidden = false;
    var r = el.getBoundingClientRect();
    var left = Math.min(window.scrollX + r.left, window.scrollX + document.documentElement.clientWidth - pop.offsetWidth - 12);
    var top = window.scrollY + r.bottom + 7;
    if (r.bottom + pop.offsetHeight + 16 > window.innerHeight && r.top > pop.offsetHeight + 16) {
      top = window.scrollY + r.top - pop.offsetHeight - 7;
    }
    pop.style.left = Math.max(window.scrollX + 10, left) + 'px';
    pop.style.top = top + 'px';
  }

  document.addEventListener('click', function (ev) {
    var hit = ev.target.closest && ev.target.closest('.gl-w');
    if (hit) { ev.preventDefault(); ev.stopPropagation(); show(hit); return; }
    if (!pop.contains(ev.target)) hide();
  }, true);
  document.addEventListener('keydown', function (ev) { if (ev.key === 'Escape') hide(); });
  window.addEventListener('scroll', hide, { passive: true });
  window.addEventListener('resize', hide);
})();
</script>
'''

n = 0
for f in sorted(glob.glob('week-*/index.html')):
    h = o = open(f, encoding='utf-8').read()
    if 'PHI_GLOSSARY' in h or '<nav id="nav"' not in h:
        continue
    anchor = '  @media print {'
    assert anchor in h, f
    h = h.replace(anchor, CSS.strip('\n') + '\n' + anchor, 1)
    assert h.rstrip().endswith('</html>'), f
    i = h.rstrip().rfind('</html>')
    h = h[:i] + JS.strip('\n') + '\n' + h[i:]
    open(f, 'w', encoding='utf-8').write(h); n += 1; print('wired', f)
print(n, 'guides')
