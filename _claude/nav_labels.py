"""A nav entry is a signpost. Some of these were 79 characters, which is a sentence, and a
column of sentences is what made the list taller than the window."""
import re, glob, html as H

L = {
 # week 2
 'r1-1':'The story','r1-2':'What the parts mean','r1-3':'An argument about education',
 'r1-4':'Knowing and opinion','r1-5':'Crafts and mathematics','r1-6':'The return',
 'r1-7':'Going back down','r1-8':'Who attacks the ranking',
 'r3-1':'Why this text','r3-2':'Physis','r3-3':'Techn&#275;','r3-4':'Copying and finishing',
 'r3-5':'What they could not think','r3-6':'Technique as danger',
 'r4-1':'What went wrong','r4-2':'Knowledge and power','r4-3':'The bent instrument',
 'r4-4':'His induction',
 'r6-1':'The claim','r6-2':'Two arguments for the law','r6-3':'The best argument',
 'r6-4':'Hierarchy of the sciences','r6-5':'Against Plato',
 'r7-1':'What he concedes','r7-2':'The argument in three steps',
 'r9-1':'The test','r9-2':'Two legitimate sentences','r9-3':'What this kills',
 'r9-4':'Why metaphysics persists','r9-5':'Two objections','r9-6':'Section 4',
 'r44-1':'Why it is here','r44-2':'The fact to explain','r44-3':'Invention of invention',
 'r44-4':'Three religious habits',
 'r49-1':'What he is doing','r49-2':'Dualism','r49-3':'An organic brain',
 'r49-4':'Robots as artefacts','r49-5':'Cog',
 # week 3
 'sismondo-1':'Why the chapter is set','sismondo-2':'Whig history','sismondo-3':'What a paradigm is',
 'sismondo-4':'Crisis and revolution','sismondo-5':'Incommensurability','sismondo-6':'Taking it apart',
 'sismondo-7':'Talking across a boundary','sismondo-8':'What the book destroyed',
 'sismondo-9':'The three boxes',
 'kuhn-1':'The book','kuhn-2':'What people took from it','kuhn-3':'Normal science',
 'kuhn-4':'Paradigm','kuhn-5':'Anomaly to revolution','kuhn-6':'Incommensurability',
 'kuhn-7':'Why it is set here',
 'r54-1':'The plague town','r54-2':'Defining discipline','r54-3':'The Panopticon',
 'r54-4':'It is a diagram','r54-5':'Why it is in this course',
 # week 4
 'ch4-9':'Getting in','ch4-10':'Staying in','ch4-11':'Getting on',
 'ch6-1':'What the chapter does','ch6-2':'Social reality','ch6-3':'Box 6.1',
 'ch6-4':'Things and phenomena','ch6-5':'Material environments','ch6-6':'Theories',
 'ch6-7':'Heterogeneous construction','ch6-8':'Kinds','ch6-9':'Nature','ch6-10':'The conclusion',
 # week 6
 'ch5-1':'MeToo','ch5-2':'What ignorance is','ch5-3':'Tuana&#8217;s five kinds',
 'ch5-4':'The five ways it is made',
 'nelson-1':'Four faults','nelson-2':'The peacock&#8217;s tail','nelson-3':'The baboons',
 'nelson-4':'What it proves',
 'ch15-1':'The HRT case','ch15-2':'Five places a value gets in','ch15-3':'What replaces the VFI',
 'ch15-4':'Value management','ch15-5':'Social justice',
 'ch19-1':'Public understanding','ch19-2':'Inclusion that changes nothing',
 'ch19-3':'Illiteracy as resistance','ch19-4':'Who was already doing it',
 'ch19-5':'When it became fashionable',
 'ch3-1':'The claim','ch3-2':'Why women produced nothing','ch3-3':'Her rule',
 'ch3-4':'The quarrel','ch3-5':'On hypotheses',
}
# week 4 chapter 4 and week 6 chapter 4 share ids, so those go per file
PER_FILE = {
 'week-4/index.html': {
   'ch4-1':'The opening number','ch4-2':'The measuring instrument','ch4-3':'Two opposite policies',
   'ch4-4':'What counts as productive','ch4-5':'The Matthew Effect','ch4-6':'Discrimination',
   'ch4-7':'The golden age','ch4-8':'The pipeline','ch4-12':'The maths gene',
   'ch4-13':'The conclusion'},
 'week-6/index.html': {
   'ch4-1':'Two objectivities','ch4-2':'The nine phases','ch4-3':'Walking the chain',
   'ch4-4':'What could it mean now','ch4-5':'Longino','ch4-6':'Harding','ch4-7':'Wylie',
   'ch4-8':'The pragmatists'},
}

for f in sorted(glob.glob('week-*/index.html')):
    h = o = open(f, encoding='utf-8').read()
    if 'class="sb"' not in h:
        continue
    table = dict(L); table.update(PER_FILE.get(f, {}))
    missing = []

    def one(m):
        hid = m.group(1)
        if hid not in table:
            missing.append(hid); return m.group(0)
        return '%s%s</a>' % (m.group(0)[:m.group(0).index('</b>') + 4], table[hid])

    h = re.sub(r'<a class="sb" data-of="[^"]*" href="#([^"]+)">.*?</a>', one, h)
    assert not missing, (f, missing)

    # week 3's Kuhn article carries no chapter number, so its sections were numbered "?.1"
    h = re.sub(r'(<h4 id="kuhn-(\d+)" data-n=")\?\.\2(")', r'\g<1>\g<2>\g<3>', h)
    h = re.sub(r'(<a class="sb" data-of="kuhn" href="#kuhn-(\d+)"><b>)\?\.\2(</b>)', r'\g<1>\g<2>\g<3>', h)

    if h != o:
        open(f, 'w', encoding='utf-8').write(h); print('relabelled', f)
