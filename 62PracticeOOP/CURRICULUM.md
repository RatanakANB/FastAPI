# CURRICULUM.md

Locked to the 4 Pillars of OOP. Do not add topics outside this sequence (see RULES.md Scope Lock for the explicit exclusion list).

## Phase 1 — Concept sequence

```
Why OOP exists
    ↓
Object
    ↓
Class
    ↓
Attribute
    ↓
Method
    ↓
self
    ↓
Constructor
    ↓
State
    ↓
Behavior
    ↓
Encapsulation
    ↓
Inheritance
    ↓
Polymorphism
    ↓
Abstraction
```

This order is fixed because each concept depends on the one before it (e.g. you can't meaningfully teach `self` before `Method`, or `Encapsulation` before `State`). Do not reorder without a strong, logged reason in `DECISIONS.md`.

## Per-lesson metadata template

Every lesson, when introduced, should be defined with:

```
LESSON: [name, e.g. "Constructor"]
DEPENDENCIES: [prior concepts required, e.g. "Class, Attribute, self"]
OBJECTIVES: [the single learning objective for this lesson]
EXPECTED MASTERY: [what correctly answering the Mini Challenge looks like]
REQUIRED FILES: [e.g. "62PracticeOOP/lesson07/Car.py (Car class), 62PracticeOOP/lesson07/main.py (entry point)" — PascalCase filename matching the class name, split into separate files whenever a class is introduced; single-file only for lessons with no new class]
ESTIMATED TIME: [e.g. "15 minutes"]
```

Only generate this metadata for the **current** lesson (and optionally the next one, as a one-line preview). Never pre-generate metadata for lessons far in the future — the curriculum adapts to how the student is actually doing (see Agile note below).

## Agile note

This curriculum sequence is the target path, not a rigid plan. If `MEMORY.md` or `DECISIONS.md` shows the student needs more time on a concept, or a different example/analogy, the *next* lesson's content adapts — but the concept order itself stays locked.
