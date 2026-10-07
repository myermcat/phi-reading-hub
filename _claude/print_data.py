# What the printed sheet carries, as against the web version.
#
# DROP      terms that come off entirely
# SHORT     terms whose definition is replaced with a tighter one
# The week 4 group is dropped whole: the exam prep said the last lecture on the
# paper is Kuhn, and none of her eleven topics touches that week.

DROP_GROUPS = {"week4"}
DROP = {"Descartes", "Instrumentalism", "Epistemology", "<i>The School of Athens</i>", "Fox 1983"}

SHORT = {
 "Ad hoc":
  ("put together for the one case in hand, with no general rule behind it",
   "Science is ad hoc and disunified and works anyway. Wittgenstein's games: solitaire has no competition, "
   "snakes and ladders no skill, ring-a-ring-a-roses no winner. No one feature is in every game, only "
   "overlaps, which he calls a <b>family resemblance</b>. So there is no scientific method, singular."),
 "Incommensurability":
  ("no shared unit for measuring two paradigms against each other",
   "<b>Mass:</b> fixed in Newton, changes with velocity in Einstein, so \"mass is conserved\" is true in one "
   "and false in the other. <b>Three reasons:</b> meanings of terms change, indoctrination, historical "
   "context changes. <b>Counter-example:</b> particle detectors survived a theory change unchanged."),
 "The cave":
  ("prisoners chained facing a wall, taking the shadows for the real things",
   "Out of the <b>sensible</b> world (what the senses reach) up to the <b>intelligible</b> (what only thought "
   "reaches), which Plato calls the journey of the soul. Being freed is <b>painful</b> and has to be compelled. "
   "The returner is laughed at; whoever unchains the others would be killed. It asks how we know what is true "
   "and what method to use, so it is a text about method."),
 "Lynn White Jr.":
  ("religious worldviews decide which technologies get built",
   "God is an architect, man is made in his image and told to rule the world, and Christian history runs one "
   "way toward a goal where other religions had it circling. So there is no time to lose and manual work "
   "becomes worship. Written against the view that economic need drives technology."),
 "Geocentrism":
  ("the earth at the centre, everything else turning round it",
   "Falls out of <i>telos</i>: earth's natural place is the centre, which is why a rock falls, so the earth "
   "sits at the centre too. Patient observation confirmed it daily for two thousand years."),
 "Foundationalism":
  ("every claim rests on a claim below it, down to a bottom layer needing nothing under it",
   "The kettle boils at 100 because water does, because every measurement came out that way, and there the "
   "chain stops. The bottom layer is laid by <b>induction</b>, so it is the least secure part. Traced "
   "<i>down</i> through reasons, never <i>back</i> through time, which is Whig history."),
 "Positivism":
  ("only what can be observed and measured counts as knowledge",
   "So research has to be <b>non-contextual</b> (the result cannot depend on who ran it, or where, or when), "
   "<b>standardised</b> (anyone following the same procedure gets the same result), and <b>analytic</b> "
   "(isolate one variable, hold the rest still). <b>Kuhn's target:</b> a paradigm is a context, so the first "
   "of the three goes."),
}

# The map, cut to what fits a side of A4. Each card: number, name, dates, the question,
# the claim in short lines, and how it leads to the next.
MAP = [
(1, "Plato", "428 to 348 BCE", "What is actually real, and how would we find out?", [
  "The <b>Forms</b> are perfect originals in a realm outside this one. Everything visible is a copy, so the senses show shadows.",
  "<b>Dialectic</b>: question and answer until opinion is sorted from knowledge.",
  "Education is <b>turning the soul around</b> to face the light. The eyes work; they point the wrong way.",
  "<b>Kalliopolis</b>: the beautiful city, run by philosopher kings.",
 ], "His own student keeps the word form and moves it out of that other realm.", False),
(2, "Aristotle", "384 to 322 BCE", "What makes things move, and where do they come from?", [
  "Form is <b>in the thing</b>, which also has a <b>telos</b>, an end it grows toward. An acorn heads for oak.",
  "Because form is here, you can cut animals open and learn something. The first biologist.",
  "Against Plato's separate realm. Attacked later by Bacon over <i>telos</i>, and by Copernicus over his cosmos.",
 ], "His cosmos then holds for two thousand years, so the next break is a large one.", False),
(3, "The Middle Ages", "read by Lynn White", "Why did Western Europe build the technology it built?", [
  "The <b>religious picture drives the technology</b>. God is an architect, man is made in his image and told to rule the world.",
  "Christian history runs one way toward a goal, so there is no time to lose and <b>manual work becomes worship</b>.",
  "By 1300, <b>Deism</b>: God as a clockmaker who set it going and stepped back, so studying the mechanism is pious.",
 ], "Now the Greek picture starts to come apart, first in its content.", False),
(4, "Copernicus", "1473 to 1543", "How do the planets actually move?", [
  "The sun stands still and the earth moves around it.",
  "<b>Her framing:</b> he put the sun at the centre so that <b>circular motion</b> would work. He was keeping an old Greek commitment, with no new data behind it.",
  "Against Aristotle's earth-centred cosmos, which was also the Church's.",
 ], "The content has broken. Next the method breaks.", False),
(5, "Bacon", "1561 to 1626", "How should anyone find anything out?", [
  "<b>Empiricism</b>: the senses are where knowledge starts. And you make nature answer, by experiment.",
  "<b>Knowledge is power</b>, over the physical world, offered as a promise.",
  "<b>Ant</b> the alchemists, pile up and do nothing. <b>Spider</b> the Aristotelians, spin systems out of themselves. <b>Bee</b>, gathers then digests.",
  "Against <i>telos</i>: if a thing carries its purpose, you wait to receive it. He wants you to go and take it.",
 ], "Not everyone is pleased about the new confidence in progress.", False),
(6, "Rousseau", "1712 to 1778", "Has progress in the sciences and arts made people better?", [
  "<b>No.</b> Learning advanced. Morals did not.",
  "A society is measured by the <b>virtue</b> of its people. Great learning with no virtue is still barbarous.",
  "Virtue comes from <b>education</b>, on the Greek model. So that is the only route to real progress.",
 ], "Meanwhile institutions are being designed by arithmetic.", False),
(7, "Bentham", "1748 to 1832", "How should an institution be arranged?", [
  "<b>Utilitarianism</b>: the greatest happiness of the greatest number. What he was famous for in his lifetime.",
  "Lifelong <b>prison reform</b>. The <b>panopticon</b> was his humane replacement for hanging and filthy gaols, and was never built in Britain.",
  "Ring of cells, central tower, two windows per cell so the occupant shows as a silhouette.",
 ], "Bacon's confidence in method hardens into a doctrine about knowledge itself.", False),
(8, "Positivism", "Comte, the Vienna Circle", "What counts as real knowledge?", [
  "<b>Only what can be observed and measured.</b> Anything else is not knowledge.",
  "So research must be <b>non-contextual</b>: the result cannot depend on who ran it, or where, or when.",
  "<b>Standardised</b>: anyone following the same procedure gets the same result.",
  "<b>Analytic</b>: isolate one variable, hold the rest still.",
 ], "Kuhn's target. A paradigm is a context, so the first of the three goes.", False),
(9, "Kuhn", "1922 to 1996", "Does science accumulate steadily toward the truth?", [
  "<b>No.</b> Long stable stretches, broken by revisionary breaks. Against positivism and against steady progress.",
  "<b>Paradigm:</b> the shared picture a field works from, with its instruments, standards and assumptions. Newton, Lavoisier, Mendel.",
  "<b>Normal science:</b> puzzles where the final picture is agreed and every piece leads toward it.",
  "<b>Anomaly:</b> a result that will not fit. <b>Revolution:</b> the picture gets replaced and the anomaly is explained.",
  "<b>Incommensurability:</b> no shared unit for measuring old against new.",
  "Rejects <b>Whig history</b>. A revolution is <b>not progress</b>: it builds and destroys at once.",
  "<b>Her conclusion:</b> science is ad hoc and disunified and works anyway.",
 ], "If the shape of a science can shift, the next question is who benefits from the shape it has.", True),
(10, "Foucault", "1926 to 1984", "What are modern institutions doing to people?", [
  "<i>History of Madness</i>, 1961: psychiatry's claimed neutrality covers for controlling people who break social rules. Homosexuality, hysteria.",
  "<i>Discipline and Punish</i>, 1975: a <b>genealogy</b>, how a practice came to be without assuming it improved.",
  "<b>Three techniques:</b> hierarchical observation, normalizing judgment, the examination. Watch, rank, record.",
  "<b>Normalization</b> is the goal. Her examples: standardized education, medical practice, industrial production.",
  "<b>Power-knowledge:</b> Bacon's equation kept, the power now over people, the verdict reversed to an accusation.",
  "<b>Docile bodies:</b> broken into segments, analysed, recomposed for effect.",
 ], "Kuhn says the content could have gone otherwise. Foucault says knowing has a politics.", True),
(11, "Social construction", "Sismondo, Hacking 1999", "In what sense is a scientific fact made?", [
  "<b>Hacking:</b> any theory is not the only one that could have been established, so success is no evidence for it.",
  "Institutions are real because <b>enough people act as though they exist</b>. Politeness: no law, no building, constrains everybody.",
  "The test is <b>causal power</b>. Gender is real because treating people as gendered produces gendered people.",
  "<b>Kinds</b>, meaning categories like gold or ADHD. <b>Realist:</b> the world comes divided and we find the lines. <b>Nominalist:</b> we draw them, so they live in our language. Test case ADHD.",
 ], "", True),
]

TWICE = [
 ("Bacon", "three times", "<b>Week 2:</b> the founder. Empiricism, experiment, knowledge is power as a promise about nature. "
  "<b>Week 3:</b> inside Foucault, the same three words become power-knowledge, power over people, the verdict reversed. "
  "<b>Week 4:</b> a failed prediction. He expected method to level intellectual ability; ten per cent of authors produce half of all papers."),
 ("Aristotle", "three times", "<b>In his own right:</b> form in the thing, plus <i>telos</i>. <b>As Bacon's target:</b> <i>telos</i> is "
  "precisely what Bacon objects to. <b>As Copernicus's target</b>, and as Kuhn's contrast for foundationalism, since "
  "<i>telos</i> pulls from ahead and a foundation pushes from below."),
 ("Plato", "twice", "<b>Week 2:</b> the cave, and education as turning around. <b>Week 3:</b> beside Foucault, because his "
  "panoptic utopia is meant to recall Plato, the <i>Republic</i>, the Kalliopolis. One ordered city described twice, "
  "once admiringly and once as a warning."),
]
