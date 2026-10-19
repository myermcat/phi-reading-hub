"""Darwin comes with the Nelson chapter, and Longino gets a face where her norms are the answer."""
import re
f='week-7/index.html'; h=open(f,encoding='utf-8').read()
def ins_after(marker, block, label):
    global h
    k=h.find(marker); assert k>0, label
    end=h.find('</div>', h.find('</p>', k)); end=h.find('\n', end)+1
    h = h[:end] + '\n          ' + block.strip() + '\n' + h[end:]

DARWIN = open('/tmp/fig_darwin.html', encoding='utf-8').read().strip()
ins_after('Three objections Nelson reports', DARWIN, 'darwin')

LONGINO = '''<figure class="pic">
            <a class="zoom" style="width:200px" href="img/longino.jpg" target="_blank" rel="noopener" title="Open this picture at full size">
              <img src="img/longino.jpg" width="300" height="419" loading="lazy"
                   alt="A head and shoulders photograph of an older woman with short grey hair, smiling, in a pale pink jacket over a dark top, standing in front of a wooden wall.">
            </a>
            <figcaption><b>Helen Longino, whose four norms are the first of the two answers.</b> Her position is that no individual can get out from under the assumptions she shares with everybody around her, so objectivity has to be a property of how a community is organised. That is why her model lets any value in and puts the whole weight on whether criticism actually changes what the community believes. <span class="cred">Helen E Longino, CC BY-SA 4.0, via Wikimedia Commons.</span></figcaption>
          </figure>'''
ins_after('The mechanism, in one line', LONGINO, 'longino')
open(f,'w',encoding='utf-8').write(h)
print('Darwin and Longino placed')
