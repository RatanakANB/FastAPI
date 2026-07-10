Since you're committing this to GitHub, both prompts need to be **fully self-contained** — no assumption that the new agent/session/PC has any conversation history. Everything must come from reading the files themselves.

## Prompt 1 — First time starting (fresh, no MEMORY.md entries yet)

```
You are working inside this repository's 62PracticeOOP/ project.

Read AGENT.md first — it is the entry point and tells you which files
to read next, in what order (ROLE.md, RULES.md, WORKFLOW.md,
CURRICULUM.md, MEMORY.md, HANDOFF.md, DECISIONS.md).

This is a fresh start. MEMORY.md currently has no real lessons logged
yet (only the Lesson 00 placeholder). Follow AGENT.md and WORKFLOW.md
exactly, for this and every future response in this project.

Start Lesson 01 from CURRICULUM.md: "Why OOP exists."
```

## Prompt 2 — Resuming (different PC, different agent, cloned from GitHub)

```
You are resuming an existing teaching project inside this repository's
62PracticeOOP/ project. You have no memory of prior sessions — treat
this as a cold start and reconstruct all context from the files.

Read AGENT.md first — it defines the required read order and workflow.
Then read ROLE.md, RULES.md, WORKFLOW.md, and CURRICULUM.md.

Then read HANDOFF.md for a fast summary of where I left off, and confirm
it against the most recent entry in MEMORY.md (the full log — HANDOFF.md
is only a summary of it). If they disagree, trust MEMORY.md.

Check DECISIONS.md for any teaching approaches already tried and logged
as not working, so you don't repeat them.

Once you've confirmed current lesson, mastery status, and student
profile from those files, tell me:
1. What lesson we're on and its mastery status
2. A one-line trend summary (improving / steady / struggling with what)
3. What you're about to teach next

Then continue exactly where WORKFLOW.md says we left off — do not
restart or skip ahead.
```

**Why Prompt 2 is built this way:**

- Explicitly says "you have no memory" — stops the new agent from ever guessing or hallucinating progress instead of reading files.
- Forces it to **cross-check HANDOFF.md against MEMORY.md** rather than trusting the summary blindly, since HANDOFF.md could theoretically go stale if a session ended before regenerating it.
- Makes it **report back to you first** (lesson, status, trend, next step) before teaching anything — so you catch it immediately if it misread the state, rather than 3 lessons deep.
- References `DECISIONS.md` explicitly so a new agent doesn't repeat a dead-end example/analogy from a previous machine's session.

One practical tip for the GitHub habit: make sure `MEMORY.md` and `HANDOFF.md` are actually committed and pushed **at the end of every session**, not just locally saved — otherwise a different PC pulling the repo will resume from stale state. Worth adding as a manual checklist item for yourself, since the agent can't push git commits on your behalf unless you're using a tool-enabled agent that has git access.