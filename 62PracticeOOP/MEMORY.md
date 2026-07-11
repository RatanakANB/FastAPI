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

## [Lesson 02] — Object — 2026-07-11/session 2
STATUS: mastered
WHAT HAPPENED: Explained what an object is in Python using lists and dicts. The student successfully completed the challenge showing two variables referring to the same object vs. a new object, and correctly predicted/observed the behavior.
MISTAKES: None.
STUDENT PROFILE (this entry):
  - Strengths shown this lesson: Good intuition with list/dict references and understood the difference between content equality and object identity.
  - Weaknesses shown this lesson: Needed a visual analogy to conceptualize the exact distinction between a variable (reference) and an object in memory.
  - Compared to previous entry: Same level of strong prediction/observation skills.
NEXT ACTION: Begin Lesson 03 — "Class"

## [Lesson 03] — Class — 2026-07-11/session 2
STATUS: mastered
WHAT HAPPENED: Taught the concept of a Class as a blueprint. The student defined custom classes Dog and Cat, instantiated them, checked their custom types, and compared them. The student self-corrected a minor typo in the challenge after one guided hint.
MISTAKES: In the challenge, compared instances directly (`my_dog == my_cat`) instead of their types, but self-corrected immediately.
STUDENT PROFILE (this entry):
  - Strengths shown this lesson: Understood importing and instantiation easily. Quick to self-correct.
  - Weaknesses shown this lesson: Minor syntax/requirement oversight (comparing objects instead of types) but immediately understood the difference.
  - Compared to previous entry: Improved on code adjustment and responding to feedback.
NEXT ACTION: Begin Lesson 04 — "Attribute"

## [Lesson 04] — Attribute — 2026-07-11/session 2
STATUS: mastered
WHAT HAPPENED: Taught that attributes hold instance-specific data. The student created objects, dynamically bound attributes from outside, and verified presence using `hasattr()`. Correctly predicted the AttributeError for unset attributes.
MISTAKES: None.
STUDENT PROFILE (this entry):
  - Strengths shown this lesson: Understood dynamic attribute binding and used `hasattr()` correctly. Good grasp of AttributeError concept.
  - Weaknesses shown this lesson: None.
  - Compared to previous entry: Improved on attention to detail; wrote clean, error-free code.
NEXT ACTION: Begin Lesson 05 — "Method"

## [Lesson 05] — Method — 2026-07-11/session 2
STATUS: in-progress
WHAT HAPPENED: Lesson started. Defined a method without self, instantiated, and ran it. Student observed the TypeError. Paused here at student request before the Experiment step; student has not yet read/digested the Explanation/Discussion or done the Experiment.
MISTAKES: None.
STUDENT PROFILE (this entry):
  - Strengths shown this lesson: Good prediction of errors.
  - Weaknesses shown this lesson: None.
  - Compared to previous entry: Steady progress.
NEXT ACTION: Resume Lesson 05 — Method (read the Explanation / Discussion, and execute the Experiment step)

---

CURRENT STATE (rewritten each entry — always reflects latest only)
- Current lesson: lesson05 — Method (in-progress, paused before Experiment)
- Progress: 0% (0 of 4 pillars reached)
- Points to the most recent entry above for full context
