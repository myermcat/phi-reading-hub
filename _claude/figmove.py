"""Cut a <figure> out of a page by the file it shows, so it can be put where it belongs."""
def cut(h, imgfile):
    k = h.find(imgfile)
    assert k > 0, 'no such picture: ' + imgfile
    i = h.rfind('<figure', 0, k)
    j = h.find('</figure>', k) + len('</figure>')
    assert 0 < i < k < j, imgfile
    return h[:i] + h[j:].lstrip('\n'), h[i:j]
