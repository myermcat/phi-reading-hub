f='week-6/index.html'; h=open(f,encoding='utf-8').read()
def sub(old,new):
    global h
    assert old in h, 'MISS: '+old[:70]
    h = h.replace(old,new,1)

sub('''<p><b>Three findings, and the third undoes the original picture.</b> She described baboon mothers doing several things at once, <b>juggling</b> competing priorities and <b>budgeting</b> their time, and their interactions with juveniles and with other adults were key to the group's social dynamics. She found substantial interactions between adult males and infants, and that females built special relationships with particular males who then protected them from other baboons. Hrdy's summary: infants are often the focal point of elaborate male, female and infant relationships, <b>relationships often initiated by the females themselves</b>.</p>
            <p><b>Altmann's conclusion, stated against the field she was in.</b> The <b>high drama</b> of encounters between male baboons is <b>not nearly as important</b> to the group's social dynamics as the <b>micro-practices</b> of the females.</p>''',
'''<p><b>Three findings, and the third undoes the original picture.</b></p>
            <ol>
              <li><b>Mothers run several things at once.</b> Altmann described them <b>juggling</b> competing priorities and <b>budgeting</b> their time, and their dealings with juveniles and with other adults turned out to be key to the group's social dynamics.</li>
              <li><b>Adult males deal with infants a great deal.</b> The first generation of fieldworkers had recorded almost none of this.</li>
              <li><b>Females build special relationships with particular males</b>, who then protect them from other baboons. Hrdy's summary: infants are often the focal point of elaborate male, female and infant relationships, <b>relationships often initiated by the females themselves</b>.</li>
            </ol>
          </div>

          <div class="keep">
            <b>Altmann's conclusion, stated against the field she was in</b>
            The high drama of encounters between male baboons matters far less to the social dynamics
            of the group than the micro-practices of the females.
          </div>

          <div class="body">''')

open(f,'w',encoding='utf-8').write(h)
print('ok')
