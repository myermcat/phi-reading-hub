"""Catch a page whose containers do not close.

Weeks 5, 6 and 7 all shipped with the page wrapper left open, which put the footer, the
comment rail and every script inside it. Nothing looked broken until a rule that targets a
direct child of body stopped applying. Browsers repair this silently, so only a check finds it.

    python3 _claude/tag_balance.py          # every page
    python3 _claude/tag_balance.py week-7/index.html
"""
import re, sys, glob

TAGS = 'div|aside|section|article|footer|header|main|nav|details|figure|dl|table|ul|ol'

def check(f):
    h = open(f, encoding='utf-8').read()
    m = re.sub(r'<script\b.*?</script>', '', h, flags=re.S)
    m = re.sub(r'<style\b.*?</style>', '', m, flags=re.S)
    m = re.sub(r'<!--.*?-->', '', m, flags=re.S)
    stack, stray = [], []
    for t in re.finditer(r'<(/?)(%s)\b[^>]*>' % TAGS, m):
        name = t.group(2)
        if t.group(1):
            if stack and stack[-1][0] == name:
                stack.pop()
            else:
                stray.append((name, m[:t.start()].count('\n') + 1))
        else:
            stack.append((name, m[:t.start()].count('\n') + 1))
    return stack, stray, m

bad = 0
# _claude holds page fragments that are deliberately half a document
pages = [p for p in sorted(glob.glob('**/*.html', recursive=True)) if not p.startswith('_claude/')]
for f in (sys.argv[1:] or pages):
    stack, stray, m = check(f)
    if not stack and not stray:
        continue
    bad += 1
    print(f)
    for name, line in stack:
        print('   never closed  <%s>  line %d' % (name, line))
    for name, line in stray:
        print('   closed twice  </%s>  line %d' % (name, line))
sys.exit(1 if bad else 0)
