"""Put a figure between two paragraphs of a .body block, closing and reopening the block.

Doing this by hand is how week 6 ended up with four unclosed containers: a figure dropped inside
a flex column stops the float and the gap behaves differently, and a figure dropped between two
divs without closing the first one silently reparents the rest of the page.
"""
import re

def before(h, marker, fig, indent='          '):
    """Insert fig immediately before the <p> (or <blockquote>) that contains marker."""
    k = h.find(marker)
    assert k > 0, 'marker not found: ' + marker[:50]
    start = max(h.rfind('<p>', 0, k), h.rfind('<p ', 0, k), h.rfind('<blockquote', 0, k))
    assert start > 0, 'no block start before marker'
    open_div = h.rfind('<div class="body">', 0, start)
    assert open_div > 0 and open_div < start, 'not inside a body block'
    inner = open_div + len('<div class="body">')
    assert h.count('<div', inner, start) == h.count('</div>', inner, start), 'nested and unclosed'
    line_start = h.rfind('\n', 0, start) + 1
    return (h[:line_start]
            + indent + '</div>\n\n'
            + fig.strip('\n') + '\n\n'
            + indent + '<div class="body">\n'
            + h[line_start:])

def after_list(h, marker, fig, indent='          '):
    """Insert fig after the </ul> or </ol> that follows marker, closing the body first."""
    k = h.find(marker)
    assert k > 0, 'marker not found: ' + marker[:50]
    end = min(x for x in (h.find('</ul>', k), h.find('</ol>', k)) if x > 0) + 5
    nl = h.find('\n', end) + 1
    close = h.find('</div>', nl)
    assert close > 0 and h[nl:close].strip() == '', 'list is not the last thing in its body'
    return h[:close + 6] + '\n' + fig.rstrip('\n') + h[close + 6:]
