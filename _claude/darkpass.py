import re, glob

# dark palette only; every occurrence of these hexes in the repo is a dark token
SWAP = {
    '#141815': '#191E1B',   # paper, lifted off near-black
    '#1B201D': '#232924',   # surface
    '#10130F': '#141916',   # sunk
    '#E4E8E3': '#D3DAD4',   # ink, 14.5:1 -> 11.9:1
    '#B4BCB6': '#A9B2AB',   # ink-soft
    '#8B948D': '#848D86',   # muted
    '#2C332E': '#333A35',   # rule
    '#232925': '#2A302C',   # rule-soft
    '#262C28': '#2C332E',   # ghost
    '#214136': '#24463A',   # close-wash / accent-wash
    '#3C3220': '#413725',   # skim-wash / hot-wash
    '#272D29': '#2D332F',   # skip-wash
    '#221B25': '#272029',   # curious-bg
    # teaching page, purple cast
    '#16141A': '#1C1A21',
    '#1E1B24': '#262330',
    '#110F15': '#16141B',
    '#E7E3EC': '#D6D1DE',
    '#B9B2C4': '#AEA7BA',
    '#8E8799': '#888095',
    '#322C3A': '#3A3443',
    '#272230': '#2E2938',
}
RX = re.compile('|'.join(re.escape(k) for k in SWAP), re.I)

changed = []
for f in sorted(glob.glob('**/*.html', recursive=True)):
    h = o = open(f, encoding='utf-8').read()
    h = RX.sub(lambda m: SWAP[m.group(0).upper()], h)

    # dark reading wants more leading and a shorter line than light does
    if '--ghost:' in h and 'line-height: 1.6;' in h:
        h = h.replace('--mono:    "IBM Plex Mono"',
                      '--lh: 1.6; --measure: 82ch;\n\n    --mono:    "IBM Plex Mono"', 1)
        h = re.sub(r'(--ghost: #2C332E;)', r'\1 --lh: 1.76; --measure: 68ch;', h)
        h = h.replace('font-size: 17.5px; line-height: 1.6;',
                      'font-size: 17.5px; line-height: var(--lh);', 1)
        h = h.replace('max-width: 82ch', 'max-width: var(--measure)')

    if h != o:
        open(f, 'w', encoding='utf-8').write(h)
        changed.append(f)
print('\n'.join(changed))
