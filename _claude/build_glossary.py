"""Build one glossary for the whole hub, with the word forms each term actually appears as.

A term defined in week 2 gets marked when it turns up in week 7, because the reader has met it
once and will not remember where. Terms that are ordinary English carry a stoplist, since marking
every "being" and every "opinion" would put a dashed line under half the page.
"""
import re, glob, json, html as H, unicodedata

# ordinary words that happen to be technical terms here. Marking every instance is noise.
STOP = {'being', 'becoming', 'opinion', 'intellect', 'puzzle', 'crisis', 'revolution',
        'prejudice', 'sociology', 'troop', 'meaningless', 'anomaly', 'verification',
        'idols', 'cog', 'intersectionality', 'feminism', 'philosophy of science'}

# where the word the reader meets is not a suffix away from the word that was defined
EXTRA = {
 'epistemology': ['epistemic', 'epistemically', 'epistemological', 'epistemologically',
                  'epistemologies'],
 'agnotology': ['agnotological'],
 'androcentrism': ['androcentric'],
 'nominalism': ['nominalist', 'nominalists'],
 'relativism': ['relativist', 'relativists'],
 'contextual empiricism': ['contextual empiricist'],
 'feminist epistemology': ['feminist epistemologies'],
 'standpoint theory': ['standpoint theorist', 'standpoint theorists', 'standpoint empiricism'],
 'theory-ladenness': ['theory-laden', 'theory laden'],
 'incommensurability': ['incommensurable'],
 'normal science': ['normal scientist'],
 'stratification': ['stratified'],
 'sexual selection': ['sexually selected'],
 'parental investment theory': ['parental investment'],
 'willful ignorance': ['willfully ignorant'],
 'white ignorance': [],
 'inductive risk': [],
 'social construction': ['socially constructed', 'social constructionist', 'constructionism'],
 'underdetermination': ['underdetermined'],
 'situated knowledge': ['situated knowledges', 'situatedness'],
 'discipline': ['disciplinary', 'disciplines'],
 'realism': ['realist', 'realists'],
 'vitalism': ['vitalist'],
 'dualism': ['dualist', 'dualists'],
 'primatology': ['primatologist', 'primatologists'],
 'polyandrous': ['polyandry'],
 'co-production': ['co-produced', 'coproduction'],
 'dialectic': ['dialectical'],
}

def strip_accents(s):
    return ''.join(c for c in unicodedata.normalize('NFD', s) if unicodedata.category(c) != 'Mn')

NO_SUFFIX = ('ic', 'al', 'ly', 'ous', 'ed', 'ing', 'ism', 'ist', 'ists')

def forms(term):
    """The word forms this term plausibly appears as in running prose.

    Suffix rules run on the defined term only. Anything in EXTRA is already the form the
    reader meets, so putting it through the rules again produced epistemologicallies."""
    head = re.split(r'\s*,\s*', term)[0].strip()
    roots = {term, head}
    out = set(roots) | set(EXTRA.get(term.lower(), []))
    for w in sorted(roots):
        if ' ' in w or '-' in w or w.lower().endswith(NO_SUFFIX):
            continue
        if w.endswith('ism'):
            out |= {w[:-3] + 'ist', w[:-3] + 'ists'}
        elif w.endswith('logy'):
            out.add(w[:-1] + 'ical')
        elif w.endswith('y') and len(w) > 4:
            out.add(w[:-1] + 'ies')
        elif not w.endswith('s'):
            out.add(w + 's')
    for w in list(out):
        if re.search(r'[^\x00-\x7f]', w):
            out.add(strip_accents(w))
    return sorted({w for w in out if len(w) > 3 and w.lower() not in STOP},
                  key=lambda s: (-len(s), s))

entries, seen = [], {}
for f in sorted(glob.glob('week-*/index.html')):
    week = re.match(r'week-(\d+)', f).group(1)
    h = open(f, encoding='utf-8').read()
    i = h.find('id="s-gloss"')
    if i < 0:
        continue
    seg = h[i:h.find('</section>', i)]
    for m in re.finditer(r'<dt>(.*?)</dt>\s*<dd>(.*?)</dd>', seg, re.S):
        term = H.unescape(re.sub(r'<[^>]+>', '', m.group(1))).strip()
        if term.lower() in STOP:
            continue
        body = re.sub(r'\s+', ' ', m.group(2)).strip()
        if term in seen:
            continue
        seen[term] = 1
        fs = forms(term)
        if not fs:
            continue
        entries.append({'t': term, 'd': body, 'w': int(week), 'f': fs})

# two entries can share a word form, where the same word was defined twice in different senses.
# Clicking it should show both, so the senses merge into one popover.
by_form = {}
for e in entries:
    for w in e['f']:
        by_form.setdefault(w.lower(), []).append(e)
merged, used = [], set()
for e in entries:
    if id(e) in used:
        continue
    group = [e]
    for w in e['f']:
        for o in by_form[w.lower()]:
            if o is not e and id(o) not in used and set(f.lower() for f in o['f']) & set(f.lower() for f in e['f']):
                group.append(o)
    for o in group:
        used.add(id(o))
    if len(group) == 1:
        merged.append(e)
    else:
        allf = sorted({w for o in group for w in o['f']}, key=lambda s: (-len(s), s))
        merged.append({'t': group[0]['t'], 'w': min(o['w'] for o in group), 'f': allf,
                       'd': ' '.join('<b>%s.</b> %s' % (o['t'], o['d']) for o in group)})
entries = merged

entries.sort(key=lambda e: -len(e['f'][0]))
open('glossary.js', 'w', encoding='utf-8').write(
    '/* Built by _claude/build_glossary.py from every week\'s glossary. Do not edit by hand. */\n'
    'window.PHI_GLOSSARY = ' + json.dumps(entries, ensure_ascii=False) + ';\n')
print('%d entries, %d word forms' % (len(entries), sum(len(e['f']) for e in entries)))
