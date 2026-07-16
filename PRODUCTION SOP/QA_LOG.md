# QA LOG
## v1.0 · 2026-07-16 · Phase 0.6 of BUILD_PLAN_GAP_CLOSURE.md

## Purpose
Every generation gets ONE row here — pass, fail, or redo — with the specific reason. This is
the fix for the gap the user surfaced directly: *"i've been approving and rejecting videos
without clueing you in and that's 1 gap... that's the reason why i only have 7 posts when we
created so much content already."* A rejection that isn't logged can't turn into a rule, so
the same mistake gets regenerated (and re-paid-for) indefinitely.

**Rule:** every rejection here should either (a) get promoted into a standing rule in
MARURI_GENERATION_MASTER_REFERENCE.md §7d, or (b) be explicitly logged as a one-off/parked.
Don't let a failure disappear silently — that's the whole point of this file.

## How to log
One row per generation attempt (including redos — a redo is a NEW row, not an edit of the old
one, so the credit cost of the whole chase is visible). Format:

| Date | Clip/Job ID | Verdict | Reason | Credits | Rule extracted? |
|---|---|---|---|---|---|

- **Verdict:** PASS / REDO / KILLED (killed = abandoned, not regenerated)
- **Rule extracted?:** link to the master-sheet rule this produced, or "n/a — one-off"

---

## Log

| Date | Clip/Job ID | Verdict | Reason | Credits | Rule extracted? |
|---|---|---|---|---|---|
| 2026-07-13 | 007 v1 | REDO | Full two-handed product-reveal turn — breaks core Type 6 rule (no product handling reveal). | 35 | Hook_Playbook Type 6 anti-reveal language strengthened. |
| 2026-07-13 | 007 v2 | PASS (accepted with flag) | Improvement over v1 but still a brief body-turn "shows how it hangs" beat. Accepted rather than chasing a v3 — third generation not worth it for a minor residual. | 35 | n/a — one-off, documented as an accepted deviation. |
| 2026-07-13 | 010 v1 | REDO | Unwanted lofi background music throughout, despite explicit "no music" instruction in the prompt. | 35 | Audio constraint language made much more forceful/specific for future prompts. |
| 2026-07-13 | 010 v2 | PASS | Clean — no music, correct gesture. | 35 | n/a |
| 2026-07-13 | 011/012/013 (batch) | PASS (generation) / KILLED post-hoc (tone) | Generated clean on Higgsfield's own terms, but a later tone audit found the delivery read entitled/snobbish across all three — flat opinions, turning away without eye contact, dismissive phrasing. | 105 (35x3) | Root-caused and fixed: Hook_Playbook Type 7 guardrails rewritten (WITH-not-AT rule), master sheet §4 added. This was the single costliest lesson of the project — a full generated batch had to be tone-rewritten and effectively redone as 014/015/016. |
| 2026-07-13 | 015 v1 | REDO | The "unbranded" jam jar rendered WITH a visible text label — AI-tell + brand-exposure risk, failed the script's own pre-written criterion. | 35 | n/a — one-off prompt fix (bare-glass-no-text language). |
| 2026-07-13 | 015 v2 | PASS (later reopened, see v3) | Label gone, transcript word-perfect. Passed QA at the time. | 35 | n/a |
| 2026-07-16 | 015 v2 (reopened) | KILLED by operator post-posting-prep | Operator watched the graded clip fresh and flagged it "looks AI generated" — the ffmpeg grade alone didn't fix it. Diagnosed as cinematic shallow depth-of-field + styled food-hero board (a composition/framing problem, not a texture problem the grade could touch). | 0 (diagnosis was free — a heavy-grade test proved the fix wasn't in post) | **Rule extracted: master sheet §7d gained 3 new rows** — force deep focus/no bokeh, no hero-object staging, no live food/soft-object manipulation. This is the project's clearest example of the QA-log discipline working as intended. |
| 2026-07-16 | 015 v3 | PASS | Framing regen (selfie-held, face-led, incidental already-assembled food, hard no-bokeh language) fixed the tell at the source. QA-frame-verified: face-led ✓, background back in focus ✓, food incidental ✓, warm-look close ✓. Now the current master. | 35 | Confirmed the 3 §7d rules above are effective — no further action. |
| 2026-07-13 | 014 | PASS (with listen-flag) | Transcript word-perfect bar one elision flag ("Guests get" heard as "Guest get") — judged a pass, confirm by ear before posting. | 35 | n/a |
| 2026-07-13 | 016 | PASS (with listen-flag, resolved) | Analyser transcribed "my mom... team mom" — flagged as a possible accent break (redo trigger if American-sounding). **Operator confirmed by ear 2026-07-16: it's "mum," not "mom." No redo needed.** | 35 | n/a — resolved, listen-flag protocol worked as designed. |

---

## Running credit tally (this log only, not full-project balance)
Total spent across logged generations above: **385 credits** across 13 generation attempts for
11 final clips (006, 008, 009 passed clean first-try and aren't itemized above pending backfill
— see note below).

**Backfill note:** 006, 008, 009 generated clean on first attempt per the pipeline log but predate
this QA_LOG file — not itemized here to avoid fabricating verdict detail this file didn't
capture at the time. Going forward, EVERY generation (including clean first-pass ones) gets a
row, not just the ones with drama — a log that only records failures can't show the true
pass-rate trend.
