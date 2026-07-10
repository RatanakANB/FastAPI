# MEMORY.md

Append-only log. **Never rewrite or delete an existing entry.** This file behaves like a git commit history — read top to bottom for the full story of how teaching progressed. If a past entry needs correcting, append a new entry noting the correction; don't edit the old one.

Only the `CURRENT STATE` block at the very bottom is rewritten each time (it's a pointer, not history).

## Entry format

```
## [Lesson NN] — [Concept name] — [date/session]
STATUS: mastered / failed-retry-pending / in-progress
WHAT HAPPENED: 1-3 lines — what was taught, what the student got right/wrong
MISTAKES: specific mistake pattern, if any
STUDENT PROFILE (this entry):
  - Strengths shown this lesson
  - Weaknesses shown this lesson
  - Compared to previous entry: [improved / same / regressed] on [specific trait]
NEXT ACTION: exact next lesson/step
```

---

## [Lesson 00] — Setup — (no entries yet)
STATUS: n/a
WHAT HAPPENED: Project initialized. No lessons taught yet.
MISTAKES: none yet
STUDENT PROFILE (this entry):
  - Strengths: unknown, no data yet
  - Weaknesses: unknown, no data yet
  - Compared to previous entry: n/a (first entry)
NEXT ACTION: Begin Lesson 01 — "Why OOP exists"

## [Lesson 01] — Why OOP exists — session 1
STATUS: mastered
WHAT HAPPENED: The student observed a procedural example with separate dog variables and helper functions, then correctly identified that the repetition becomes painful as more dogs are added.
MISTAKES: Initial reflection focused on the manual repetition but needed a small nudge to phrase the core pain more clearly.
STUDENT PROFILE (this entry):
  - Strengths shown this lesson: noticed repetition, correctly predicted the effect of adding a third dog, and connected the example to future pain in scaling.
  - Weaknesses shown this lesson: needs a little help turning observations into a crisp one-sentence takeaway.
  - Compared to previous entry: improved on observation and prediction
NEXT ACTION: Begin Lesson 02 — "Object"

---

CURRENT STATE (rewritten each entry — always reflects latest only)
- Current lesson: lesson02 — Object
- Progress: 0% (0 of 4 pillars reached)
- Points to the most recent entry above for full context
