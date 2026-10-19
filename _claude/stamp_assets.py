"""Put each shared file's own hash in the tag that loads it.

A reader holding an older copy in cache never gets the fix. It happened with glossary.js, where
a new term stayed invisible, and again with editor.js, where an editor bug stayed broken after
it was repaired. Run this after changing anything under shared/ or the glossary.
"""
import re, glob, hashlib, os

ASSETS = ['shared/editor.js', 'glossary.js']
tags = {}
for a in ASSETS:
    if os.path.exists(a):
        tags[a] = hashlib.sha1(open(a, 'rb').read()).hexdigest()[:8]

changed = 0
for page in sorted(glob.glob('week-*/*.html')) + sorted(glob.glob('*.html')):
    h = o = open(page, encoding='utf-8').read()
    for a, tag in tags.items():
        name = os.path.basename(a)
        h = re.sub(r'(src="(?:\.\./)?(?:shared/)?%s)(?:\?v=[0-9a-f]+)?"' % re.escape(name),
                   r'\1?v=' + tag + '"', h)
    if h != o:
        open(page, 'w', encoding='utf-8').write(h); changed += 1
print('stamped %d pages: %s' % (changed, ', '.join('%s %s' % (os.path.basename(a), t) for a, t in tags.items())))
