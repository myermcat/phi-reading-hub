"""A summary that names the shape of a step and leaves out its content is a blurb.

"Applied it to the biggest scientific quarrel of her day and took the correct middle position"
tells a reader the shape of three sentences and none of their content. Which quarrel, which
sides, which position: all withheld, the way a back cover withholds them.
"""
f='week-7/index.html'; h=open(f,encoding='utf-8').read()
def sub(old,new,label):
    global h
    assert old in h, label
    h=h.replace(old,new,1)

sub('''She applied that rule to the biggest scientific quarrel of her day, saw that <b>both sides were holding positions out of national loyalty</b>, and so was free to take the correct middle position that neither side could reach.''',
'''She applied that rule to the scientific dispute Europe was having at the time, which was whether a scientist may use a hypothesis at all. The British read Newton as saying no, and Voltaire was telling the French to drop Descartes and follow them. She saw that each side was holding its position because of <b>where it lived</b>, with the evidence doing no work, and that left her free to say what neither of them could: hypotheses are necessary wherever no other route to the cause exists, and the job is to set rules they have to obey. She set four.''', 'step 3')

sub('''<h1>Who Gets to Decide What Science Is For</h1>''',
    '''<h1>Which Values Belong in Science, and Who Decides</h1>''', 'title')

sub('''Science cannot be made value-free. Last week showed why, so somebody now has to choose which values it runs on. Two chapters propose rules for choosing. A third says the real question is who gets counted as a scientist at all. And a fourth follows a woman barred from the French academy who got the modern account of hypotheses right in 1740.''',
    '''Science cannot be made value-free. Last week showed why, so somebody has to decide which values are allowed. Two chapters propose rules for deciding. A third says the real question is who gets counted as a scientist at all. And a fourth follows a woman barred from the French academy who argued in 1740 that science needs hypotheses, and set four tests they have to pass.''', 'standfirst')
open(f,'w',encoding='utf-8').write(h)
print('step 3 carries its content; title and standfirst name the week')
