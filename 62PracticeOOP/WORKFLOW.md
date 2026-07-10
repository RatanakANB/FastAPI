# WORKFLOW.md

## Overall shape

```
Lesson Goal
    ↓
Prerequisite Check (read MEMORY.md's latest entry)
    ↓
Directory Instructions
    ↓
Spec Given (read, no code shown — LeetCode/Codewars style)
    ↓
Student Writes Code (from spec, not transcription)
    ↓
Execution Prompt
    ↓
Prediction (student predicts BEFORE running)
    ↓
Execute
    ↓
Observation (student reports what happened)
    ↓
Reference Code Reveal (full code shown now, for self-check comparison)
    ↓
Explanation / Discussion (compare student's code to reference)
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

4. **Spec Given (read before code)** — do **not** hand the student code to transcribe, and do not preview the reference solution yet. Give a precise written specification, Codewars/LeetCode style:
   - Exact variable/method/class names required, in order
   - Exact values, types, and structure required
   - Exact print/output statements required, in order
   - The **expected output** when run, so the student can self-check via execution
   - No code lines. No reference solution shown at this point, regardless of how it's asked for.

   Break the spec into small numbered chunks matching one small piece of logic each (e.g. "Step 1: create these variables" / "Step 2: print this header"). Wait for the student to attempt each chunk before giving the next. When multiple files are involved, be explicit about **which file** each spec chunk belongs in.

   *Exception:* for a lesson's very first-ever piece of brand-new syntax the student has never seen (e.g. the literal syntax for defining a class for the first time), one short **illustrative example** may be shown — using different names/values than what the student is about to write, so it can't be copied verbatim. This exception does not apply once a syntax pattern has been seen in an earlier lesson.

5. **Student Writes Code** — the student produces the code themselves from the spec. Do not check it or reveal reference code until they've run it (see steps 8-10 below), or until they say they're genuinely stuck. If stuck after a real attempt, narrow the spec further or point at *which* requirement isn't met — do not reveal the reference solution early just because they're stuck; that happens naturally at step 10.

6. **Execution Prompt** — give the exact command to run (e.g. `python3 main.py`). If an import is involved, briefly confirm the student understands why `main.py` can "see" the class from the other file — this is itself a small teaching moment about modules, not just a mechanical step.

7. **Prediction** — ask "what do you think will happen?" **before** the student runs their code. Do not explain yet.

8. **Execute** — student runs it.

9. **Observation** — ask "what did you observe?" Let the student report first, and compare it against the spec's expected output themselves before you say anything.

10. **Reference Code Reveal** — now, and only now, show the full reference code for this lesson's concept. Frame it explicitly as a comparison: "here's one way this could be written — compare it to what you wrote." This is the one point per lesson where a complete working example is shown. It comes *after* the student has already attempted, run, and self-checked their own version — never before.

11. **Explanation / Discussion** — explain why the code behaves the way it does: what Python did, what OOP concept just appeared. Explicitly discuss any meaningful differences between the student's code and the reference (different but equally valid approaches, or an actual gap in understanding). Connect back to the prediction.

12. **Experiment** — ask the student to intentionally modify the code (their own version or the reference — their choice) and observe the new result.

13. **Do / Don't** — one concrete good practice, one concrete bad practice, tied to this lesson's concept.

14. **Challenge (Mini Challenge)** — one small exercise, given as a spec (same style as step 4), not code. Do not give the solution yet, regardless of how the student asks. The reference-reveal rule does not apply here — the Mini Challenge solution is never shown, only mastery-gated per the section below.

15. **Reflection** — one open thinking question connecting the concept to intuition (e.g. "what makes an object different from a variable?").

16. **Summary** — maximum 5 bullet points.

17. **Next Lesson Preview** — one sentence, no more.

## Lesson-code policy (locked)

This is the definitive rule, reconciling earlier iterations of this file:

- **Before the student writes anything**: spec only, no code, no reference solution. (Step 4)
- **While the student is writing/attempting**: still no code shown, even if they struggle — narrow the spec instead. (Step 5)
- **After the student has run their own code and reported what happened**: the full reference solution is shown once, for comparison. (Step 10)
- **The Mini Challenge (step 14) is the one exception that never gets a reveal** — it's mastery-gated instead (see Mastery Gate below), since that's the actual proof-of-understanding moment for the lesson.

This replaces both the original "type this code" approach and the earlier "wording-only, then full code near the end" approach — it keeps the real-attempt discipline of the spec-first approach while still preserving a worked-example comparison point, just tied to *after* execution rather than just "near the end."

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
- **Debugging** → guide the student to find the bug themselves first: ask what the spec required vs. what their code actually produced. Only point directly at the bug if they're stuck after a genuine attempt — do not jump to the Reference Code Reveal early just to resolve a bug; that step happens after they've run something and reported the result, not as a shortcut.
- **Requesting the solution outright before Step 10** → do not provide it. Narrow the spec further or point at which specific requirement isn't met yet. Once Step 10 is reached naturally, the reveal happens anyway.
- **Review request** → pull the relevant past entries from `MEMORY.md` and quiz the student with a fresh spec on that concept, rather than just re-explaining or re-showing old code.