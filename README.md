# PHI2394 Reading Hub

Reading guides for **PHI2394, Scientific Thought and Social Values** at the University of Ottawa.

**→ [Read them here](https://myermcat.github.io/phi-reading-hub/)**

---

## What this is

Each week's assigned reading gets a guide that explains every argument in it, written for
somebody who has not opened the source and is not going to. A summary tells you that an
argument exists. A guide puts the argument in your head.

Each guide carries:

- **A page map** drawn to scale, so the endnotes are visible as endnotes before you start reading.
- **Every argument narrated** in stages, with each term defined where it first appears.
- **Real examples** for the abstract claims, with names, dates and what they cost.
- **The quarrel between the texts**, since the authors in a week's packet usually contradict
  each other and that is the point.
- **A glossary** at the end, grouped by text, repeating every definition so nothing has to be hunted.
- **Highlights, margin comments and notes** you write yourself.

Weeks with an exam coming also get a **cheat sheet**: everything from the reading that could be
asked for by name, built to print.

## What you write stays in your browser

Highlights, comments and notes are kept in your own browser's local storage. They survive a
reload, a closed tab and a restart of the machine.

They never leave the device. They are not sent to a server, they do not appear on your phone
after you wrote them on a laptop, and nobody else can read them. Clearing site data removes
them, and a private window keeps them only until it closes. Each guide has an **export** button
that writes everything to a JSON file and an import button that reads it back, which is how you
move your work between machines or keep a backup. If your browser refuses to store
anything, the page says so in the corner, so you find out while you can still copy the text out.

**These guides get rewritten often**, whenever a better way to answer a question turns up. A
highlight is anchored to the words around it, so it survives edits elsewhere on the page. If the
exact paragraph you marked gets rewritten, that highlight goes.

## Written with Claude

These guides were written with Claude, from the readings. Treat them as good AI writing: mostly
right, and capable of being wrong. They are dependable on the shape of an argument, on who said
what, and on how the texts collide, which is what they are for. They get weaker where a long passage has been compressed into a short one, because compression is
where detail goes missing and a claim can come out stronger or flatter than the author put it.
Anything worth quoting is worth checking against the reading, and the page numbers are there so
that check takes a minute.

## What is not here

**The readings themselves.** They are copyright material posted to a course site, so only the
guides are published. Anyone taking the course already has the PDFs.

## Building a week

The guides are single HTML files with no build step and no dependencies. Open one in a browser
and it works.

```
index.html            the hub
week-2/index.html     the guide
week-2/cheat-sheet.html
```

Made with [Claude Code](https://claude.com/claude-code) against a written spec, which lives in
`~/.claude/skills/course-readings` on the machine that produced them.
