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
| 2026-07-21 | Spec Ad 004 draft 1 / `4eacb208` | PASS on all machine checks (listen-flag pending) | **First clean-look paid-track draft — the §7 go/no-go experiment.** Transcript word-perfect. Frames verified: deep focus held (background sharp, no bokeh — the §7d language beat the model's cinema default first try), selfie-arm geometry visible, phone screen dark/unreadable, no brand text, canon wardrobe/accessories. Analyser confirms handheld sway + direct eye contact + no music. Remaining: operator listen (accent/warmth/half-laugh) — same protocol as 016. Nitpick only: kitchen reads US-condo rather than London; fix in final-render prompt ("compact UK kitchen"). | 35 | Provisional: clean-look track is VIABLE — §1 camera block + §3 carried rules worked without the 2012 shield. Confirm after operator listen. |
| 2026-07-22 | Spec Ad 004 draft 1 (operator review) | REDO (one targeted fix) | Operator watched it: audio/delivery fine; single flag = **the prop phone rendered as an old gold-bodied iPhone** — "seeing someone use an iPhone so old and talk about a new latest app just seems odd." Diagnosis: camera-era styling language bled into the hand-prop. | 0 (review) | **Rule extracted (paid + organic): when a phone appears as a PROP, describe it explicitly as a current-generation iPhone (edge-to-edge screen, slim flat edges, dark neutral colour) — never leave prop-device age implicit, especially in prompts that also describe camera hardware.** Added to draft-2 prompt; promote to director spec §3 if it holds. |
| 2026-07-22 | Spec Ad 004 draft 2 / `0728371e` | PARTIAL → operator chose one more draft | Kitchen fix landed perfectly (compact UK kitchen, kettle, draining board, terraced houses through the window — unmistakably London). Phone: modern edge-to-edge silhouette achieved, but the GOLD finish persisted despite "dark neutral colour, no gold vintage body" — diagnosis: the model colour-coordinates hand-props with her canon gold jewellery (hoops/chain/rings in every frame). | 35 | Refinement of the prop rule: naming a colour isn't enough against a palette-coordination bias — give the model an object it can't stylize. Draft 3 = plain matte-black CASE + "deliberately does NOT match her jewellery" + colour repeated at every prop mention. Promote to spec §3 with the prop-era rule if draft 3 holds. |
| 2026-07-22 | Spec Ad 004 draft 3 / `5981ee0c` | FAIL (phone) → prop DROPPED by operator decision | The matte-black-case language half-worked (screen side black) but the visible rim rendered GOLD for the third consecutive draft — the jewellery palette-coordination bias beats explicit colour instruction 3/3. Bonus finds: the phone lift rendered face-height/prominent (bigger than the scripted wrist-height beat), and the kettle rendered as a SMEG with readable logo despite the generic no-brand-text line. Kitchen otherwise even better (boiler, sash window, terraces). | 35 | **Two rules extracted:** (1) unrenderable-prop rule — after 2 failed prompt-fights on a prop attribute, REMOVE the prop instead of describing harder (same class as 015's fix); she is the ad, product UI is edit-stage B-roll. (2) Object-specific brand bans — "no brand text anywhere" fails; name the object ("a plain cream kettle with no logo"), same lesson as 015's jam jar. Both promoted to PAID_AD_DIRECTOR_SPEC.md §3. |
| 2026-07-22 | Spec Ad 004 FINAL / `efc9ad13` | **PASS (with free post-fix)** | 10s·1080p·std (90cr — preflight also RESOLVED the spec §6 open item: no 8s cap at 1080p/std). Performance/face/energy excellent at 1080p; deep focus held; no phone prop (problem class eliminated); UK kitchen held. ONE miss: kettle rendered as a cream SMEG with readable logo in-frame throughout — the object-specific ban FAILED because "cream kettle" itself summons the Smeg prior. Fixed free in post: ffmpeg `delogo` patch (x1 y1080 200x100) verified across the full sway range at 6 timestamps — logo gone everywhere, minor smoothing on the kettle body visible only at ~300% zoom, invisible at feed size. Master: `Raw Videos\004_specad_FINAL_1080p_delogo_master.mp4`. | 90 | **Rule refined:** object-specific brand bans must also avoid COLOUR+OBJECT combos with iconic brand priors ("cream kettle"→Smeg, and e.g. "colourful stand mixer"→KitchenAid) — specify "brushed stainless, no markings" or omit the appliance entirely. Also: `delogo` is the proven cheap fix for a static-ish background logo before considering any re-roll. Promoted to PAID_AD_DIRECTOR_SPEC.md §3. |

---

## Running credit tally (this log only, not full-project balance)
Total spent across logged generations above: **455 credits** across 15 generation attempts
(organic: 385 across 13 for 11 final clips; paid track: 70 across 2 drafts of Spec Ad 004 so
far, draft 3 in flight +35 when logged). 006, 008, 009 passed clean first-try and aren't
itemized — see note below. Note: credits now refresh 9,000/mo (see Production_Economics.md
v1.1), so this tally tracks discipline/pass-rate, not runway.

**Backfill note:** 006, 008, 009 generated clean on first attempt per the pipeline log but predate
this QA_LOG file — not itemized here to avoid fabricating verdict detail this file didn't
capture at the time. Going forward, EVERY generation (including clean first-pass ones) gets a
row, not just the ones with drama — a log that only records failures can't show the true
pass-rate trend.
