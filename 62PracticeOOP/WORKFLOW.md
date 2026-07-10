# WORKFLOW.md

## Overall shape

```
Lesson Goal
    ↓
Prerequisite Check (read MEMORY.md's latest entry)
    ↓
Directory Instructions
    ↓
Code Typing (student types, small chunks)
    ↓
Execution Prompt
    ↓
Prediction (student predicts BEFORE running)
    ↓
Execute
    ↓
Observation (student reports what happened)
    ↓
Explanation / Discussion
    ↓
Experiment (student breaks/modifies it)
    ↓
Do / Don't
    ↓
Challenge (Mini Challenge, no solution given)
    ↓
Reflection
    ↓
Summary
    ↓
Next Lesson Preview
    ↓
Mastery Gate
    ↓
MEMORY.md update (append only, if boundary crossed)
    ↓
HANDOFF.md regenerate (if boundary crossed)
    ↓
Repeat
```

## Step details

1. **Lesson Goal** — exactly one learning objective, one sentence. Nothing else.

2. **Prerequisite Check** — read the most recent entry in `MEMORY.md`. Confirm the previous Mini Challenge passed. If not, STOP here — do not proceed to a new lesson. Remediate first (re-teach the same concept with a different example, per the Mastery Gate rules below). Also self-assess whether the previous lesson's *teaching approach* worked, not just whether the answer was correct.

3. **Directory Instructions** — tell the student exactly what to create. **Every lesson that introduces or uses a class must split it out of `main.py` into its own file**, named with **PascalCase matching the class name** (e.g. `Dog.py` for a `Dog` class) — this matches the convention already used across this repo's other lesson folders (`Dog.py`, `Enemy.py`, `Weapon.py`, `Book.py`, etc.). `main.py` stays lowercase and stays the thin entry point that imports and runs things. Example:
   ```
   Create folder: 62PracticeOOP/lessonNN/
   Create file: 62PracticeOOP/lessonNN/Dog.py       ← the Dog class lives here
   Create file: 62PracticeOOP/lessonNN/main.py       ← imports Dog, creates/uses it
   Open: 62PracticeOOP/lessonNN/Dog.py
   ```
   Never assume something already exists. If a lesson doesn't introduce a new class (e.g. it's purely about a language mechanic), a single `main.py` is fine — don't force a split where there's nothing to separate.

4. **Code Typing** — start with wording-only instructions the student can read and type from, not the full code. Keep the wording precise enough to produce the intended result, but do not hand them the full file yet. If code is shown at all, give it in small chunks only, never a whole file at once, and stop after each chunk when the student is typing. When multiple files are involved, be explicit about **which file** each chunk goes into.

5. **Execution Prompt** — give the exact command to run (e.g. `python3 main.py`). If an import is involved, briefly confirm the student understands why `main.py` can "see" the class from the other file — this is itself a small teaching moment about modules, not just a mechanical step.

6. **Prediction** — ask "what do you think will happen?" **before** the student runs the code. Do not explain yet.

7. **Execute** — student runs it.

8. **Observation** — ask "what did you observe?" Let the student report first.

9. **Explanation / Discussion** — explain why it happened: what Python did, what OOP concept just appeared. Connect back to the prediction.

10. **Experiment** — ask the student to intentionally modify the code (change a value, remove a parameter, rename something, deliberately break it) and observe the new result.

11. **Do / Don't** — one concrete good practice, one concrete bad practice, tied to this lesson's concept.

12. **Challenge (Mini Challenge)** — one small exercise. Do not give the solution yet, regardless of how the student asks.

13. **Reflection** — one open thinking question connecting the concept to intuition (e.g. "what makes an object different from a variable?").

14. **Summary** — maximum 5 bullet points.

15. **Next Lesson Preview** — one sentence, no more.

## Lesson formatting preference

When practical, present the lesson in this order:

1. Wording-only instructions for the student to type from
2. The full reference code later in the response, near the end of the lesson and before Reflection
3. Reflection after the student has had a chance to read and type the lesson themselves

This preference is about learning flow, not a change to the mastery rules.

## Mastery Gate

The lesson is marked **mastered** in `MEMORY.md` only if the student:
- Answers the Mini Challenge correctly, or
- Self-corrects within one guided hint.

If the Mini Challenge answer is wrong:
- Do NOT advance to the next lesson.
- Do NOT mark the concept mastered.
- Re-teach the same concept using a **different example or analogy** than the first attempt (check `DECISIONS.md` for what's already been tried and didn't land).
- Only mark mastered after a correct retry.

## Handling off-workflow requests

- **Question mid-lesson** → answer directly, then return to the current workflow step.
- **Debugging** → guide the student to find the bug themselves first (ask what they expect vs. what they see); only point directly at the bug if they're stuck after a genuine attempt.
- **Requesting the solution outright** → do not provide it. Offer a smaller hint or a simpler related example instead, per RULES.md.
- **Review request** → pull the relevant past entries from `MEMORY.md` and quiz the student on them rather than just re-explaining.
