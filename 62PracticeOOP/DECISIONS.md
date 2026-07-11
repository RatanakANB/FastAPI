# DECISIONS.md

Every notable teaching decision gets recorded here — not just *what* was taught, but *why* the approach changed. This lets a future agent session understand the reasoning behind how teaching evolved, not just the raw outcomes in `MEMORY.md`.

Append only. Do not delete or rewrite past decisions, even if a later decision reverses one.

## Format

```
Decision
[what was changed — e.g. example/analogy swapped, extra time spent, pacing adjusted]

Reason
[why — tied to observed student behavior, not guesswork]

------
```

## Log

```
Decision
(none yet)

Reason
Project just initialized — no teaching decisions made yet.

------
```

Decision
Started Lesson 01 with a procedural dog example instead of a class example.

Reason
The student needed to feel the repetition and manual state management first so the motivation for OOP would be concrete before introducing any pillar.

------

Decision
Changed lesson formatting to lead with wording-only instructions and place the full code later in the lesson.

Reason
The student learns better by reading, predicting, and typing their own code first, then comparing against a reference after the idea has had time to land.

------

Decision
Reconciled the "wording-only then full code near the end" approach with a stricter spec-only approach: locked in a merged policy where no code or reference solution is shown at all while the student is writing, and the full reference solution is revealed exactly once — after the student has executed their own code and reported the observation, not just "near the end" of the lesson.

Reason
"Wording-only, then reveal near the end" didn't specify *when* near the end, which risked the reveal happening before the student had actually run and self-checked their own code. Tying the reveal to right after Execute/Observe keeps the real-attempt discipline (no peeking at a solution before trying) while preserving the worked-example comparison the student found useful in Lesson 01.

------

Decision
Taught the "Object" concept using built-in Python collections (lists and dicts) and a "sticky notes vs. boxes" analogy.

Reason
By using familiar built-in structures first, the student was able to isolate and understand object identity, mutable state, and built-in behavior (methods) before adding the syntactic complexity of defining custom classes. The sticky-note analogy resolved confusion about variables vs. objects.

------