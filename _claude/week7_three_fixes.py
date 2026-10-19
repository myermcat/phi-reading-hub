import re
f='week-7/index.html'; h=open(f,encoding='utf-8').read()
def sub(a,b,label):
    global h
    assert a in h, label
    h=h.replace(a,b,1)

# the day dividers already link to the split, so the entry above them is a second copy
sub('  <a class="grp" href="#s-days">Monday &amp; Wednesday</a>\n', '', 'duplicate nav entry')

# "calling their politics science" asked the reader to translate twice before she could start
sub('<h2>Values are in. So what stops anybody calling their politics science?</h2>',
    '<h2>Values are in. What stops anyone picking the ones that suit them?</h2>', 'h2')
sub('<a class="grp" href="#s-arg">Values are in, now what</a>',
    '<a class="grp" href="#s-arg">Which values, and who picks</a>', 'nav label')

# a name with no position attached reads as agreement, and "the heart" is a metaphor
sub(' Heather Douglas calls that part the heart.', '', 'heart')

# the reading table follows the order the chapters are now in
rows = {m.group(1): m.group(0) for m in
        re.finditer(r'<tr><td><b class="tag t\d">Chapter (\d+)</b>.*?</tr>', h, re.S)}
assert set(rows) == {'15','19','3','20'}, sorted(rows)
first = min(h.find(r) for r in rows.values())
last = max(h.find(r)+len(r) for r in rows.values())
mid = h[first:last]
for r in rows.values(): mid = mid.replace(r,'')
assert mid.strip()=='' , 'rows not contiguous'
h = h[:first] + '\n          '.join(rows[k] for k in ['3','20','15','19']) + h[last:]

open(f,'w',encoding='utf-8').write(h)
print('heading, nav label, Douglas sentence and table order')
