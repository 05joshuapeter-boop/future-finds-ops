# AGENT OPERATING PROCEDURES
## Future Finds — UGC Deal Pipeline
## Version 1.0 · July 2026

---

## Status note (2026-07-12) — SUPERSEDES the 2026-07-11 note below

**NocoDB is live and fully populated.** Account: `hello@futurefindsmedia.com` (credentials + API token in `Agent Infrastructure\.env`, not in this doc). Workspace `w44rupyt`, base `Future Finds UGC Pipeline` (id `pqwtuyy7dhpjby1`). Two tables, both migrated from the CSV trackers and verified by read-back:
| Table | Table ID | Rows |
|---|---|---|
| Deals | `mxa9byegmihhmhv` | 43 (from `Outbound_Target_List.csv`) |
| Category_Exclusivity | `mt7tu12z9znwyqs` | 6 (from `Category_Exclusivity_Log.csv`) |

Deals fields: Brand, Category, Warmth, Why They Fit, Contact Route, Status, Last Touch, Notes, Draft ID, QA Status, Asset Link. Category_Exclusivity fields: Date, Brand, Product Category, Relationship, Exclusivity Window, Window Ends, Notes. Access is plain REST (`GET`/`POST`/`PATCH` on `https://app.nocodb.com/api/v2/tables/{tableId}/records`, header `xc-token`) — no MCP server involved.

**Git repo is live:** [github.com/05joshuapeter-boop/future-finds-ops](https://github.com/05joshuapeter-boop/future-finds-ops) — the 10 reference docs pushed and confirmed. Open question, not yet resolved: `brand-pitch.html` is in this repo for Supervisor to edit testimonial placeholders, but whether this repo becomes the actual deploy source for the live site (vs. Supervisor just drafting edits here for manual copy-over) hasn't been decided.

**Three Claude Managed Agents are live and now carry the real NocoDB IDs/endpoints in their system prompts** (updated 2026-07-12, all at version 2):
| Role | Agent ID |
|---|---|
| Sales/Deal | `agent_01FG6h1qtAZ9riUkQK7AQ1Jq` |
| Production | `agent_0117j1ZWCE7Wg7qCwZYZs2xw` |
| Supervisor | `agent_01Mf4fCRcFtJubmYgzBenKmV` |

Still no environment or session created — nothing is actually *running* yet, this is a fully-wired scaffold.

**Still blocked — needs the user, not another autonomous pass:**
1. **Gmail MCP wiring for the Sales agent — genuinely unresolved, not just unset up.** Managed Agents' MCP connector needs a `url` field (a public MCP server endpoint) plus a registered `vault` credential — it does NOT reuse whatever connector plumbing exists inside a Claude Code session. I don't currently know whether the `hello@futurefindsmedia.com` Gmail connector has an exposable URL of this kind, or whether it needs its own dedicated MCP server + OAuth app stood up from scratch. Sales agent was created *without* Gmail wired in — it will refuse email actions per its own system prompt until this is resolved. This needs real investigation, not a guess.
2. **Environments + first session** — the last mechanical step once Gmail is sorted (Production and Supervisor don't need Gmail at all and could get a first test session sooner).
3. **The brand-pitch.html live-sync question** flagged above.

<details>
<summary>2026-07-11 note (superseded)</summary>

**monday.com is abandoned as the system of record** (workspace/board still exist at https://05joshuapeters-team.monday.com/boards/5100087206 but were never usable — all writes beyond board/workspace creation returned `User unauthorized to perform action`). Decided via a 4-stance adversarial debate (workflow `wf_58ce6539-d9c`, 2026-07-11): **NocoDB free Cloud tier is the system of record**, reached by plain REST/HTTP from Managed Agents (no MCP server, no tunnel needed) — self-hosting NocoDB lost because it would need to be internet-reachable for cloud-scheduled agents to reach it, recreating a monday-style single point of failure as a live security exposure instead. Full reasoning: `Agent Infrastructure\architecture_debate_synthesis.md`.

Definitions saved at `Agent Infrastructure\agent_sales.json`, `agent_production.json`, `agent_supervisor.json` — these are the version-1 originals, now superseded by version 2 above.

</details>

**Original monday.com note (2026-07-10, superseded above):** was a hybrid: monday.com (`Future Finds — UGC Ops` workspace, `UGC Deal Pipeline` board, both created) as the visual system of record, with Claude running the actual agent roles below and reading/writing those boards.

**monday write access was blocked.** The connected integration could create workspaces/boards but not columns, groups, or even basic items — every write returned `User unauthorized to perform action`. Reads worked fine. Likely a plan-tier or seat-permission restriction, not fixable from this side.

---

## How to invoke a role

These aren't standing background processes (yet — see "Scheduling" at the bottom). Each is a mode of operation: tell Claude "run the sales agent" / "check on production" / "run the supervisor pass" and it picks up this document, reads current state, and acts within the boundaries defined below. Nothing here authorizes autonomous unattended operation on its own — invocation is still the trigger, unless/until scheduling is explicitly turned on.

---

## 1. Sales / Deal Agent

**Owns:** the full client relationship, start to finish — pitch, negotiation, delivery, and feedback. One agent, one thread per brand, no handoff to a separate "closer."

**Where state lives:** `Outbound_Target_List.csv` (status column), `Category_Exclusivity_Log.csv` (conflict check), the `hello@futurefindsmedia.com` Gmail thread per brand.

**Inputs it reads before acting:**
- `Outreach_Email_Templates.md` — pitch structure, tone rules, personalisation checklist
- `Website\rate-card.html` — pricing (send only after interest is confirmed, never cold)
- `PRODUCTION SOP\Usage_Rights_Terms_Sheet.md` — what terms are and aren't negotiable
- `Category_Exclusivity_Log.csv` — **must check for conflicts before any new pitch goes out**

**Process:**
1. **New pitch:** pick next "Not Contacted" row from the target list → check exclusivity log for category conflicts → if clear, personalise the right template (warm/cold/agency) → `create_draft` in Gmail → update CSV status to "Pitch Drafted." Nothing sends automatically — the Gmail connector is draft-only by design, so this is a hard stop, not a policy choice.
2. **Checking replies:** `search_threads` against tracked contacts → for each reply, read the thread, draft a response (negotiation, follow-up, or answering questions) → update CSV status accordingly (Replied / Negotiating).
3. **Deal closing:** once terms are agreed in-thread, draft a confirmation email summarizing the agreed scope, rate, usage rights, and exclusivity (if any) → update CSV status to "Deal Closed" → **write a brief** (see below) → hand off to Production.
4. **Delivery:** once Production + user approval clears a clip (see §2, §3), draft the delivery email with the final asset(s) + a specific feedback/testimonial ask → update CSV status to "Delivered," then "Complete" once feedback is received or 14 days pass without one.
5. **Exclusivity log:** on every Deal Closed, add/update the row in `Category_Exclusivity_Log.csv` with the real terms agreed (not the rate-card default — the actual negotiated window).

**Boundaries:**
- Never sends. Every email is a Gmail draft for the user to review and send.
- Never agrees to terms outside the rate card / usage rights sheet without flagging it to the user first — draft the proposed exception but mark it clearly as needing sign-off, don't fold it into a sent-sounding confirmation.
- Never pitches a brand that conflicts with an active exclusivity window — this is a hard check, not a judgment call.

**Output/handoff — "The Brief":**
When a deal closes, the Sales Agent produces a short brief (as a reply in this thread or a note in the CSV's Notes column) containing: brand name, product, agreed format (organic / UGC ad / retainer), budget, usage rights scope, exclusivity terms, any brand-specific creative direction from the negotiation, and delivery deadline. This is what Production works from — Production should never have to go back to raw email threads to find the brief.

---

## 2. Production Agent

**Owns:** turning an approved brief into QA'd, client-ready clips.

**Inputs it reads before acting:**
- The brief from Sales (above)
- `MASTER_CHARACTER_BIBLE.md` — non-negotiable for voice, appearance, behavior
- `Future_Finds_Design_Philosophy.md` — if any accompanying visual assets are needed
- `PRODUCTION SOP\iPhone_Camera_Spec.md` and `Hook_Playbook.md`
- The three existing `Spec_Ad_*.md` docs as the reference method (script structure, Seedance prompt pattern, QA process)

**Process:**
1. Write the script in Maruri's voice against the brief — pull the hook formula and camera spec from the existing playbooks, don't reinvent them per job.
2. Generate via Higgsfield (Soul ID `e047f76e-91cb-44df-8492-15ec1d47e09a`, character element `b40df106-df2c-4015-ab66-19fbd488d634`, `seedance_2_0`, native audio) — same production settings validated on the three spec ads.
3. QA before showing the user anything: cross-clip face consistency, product accuracy against the reference image, gesture/beat timing against the script, pause rhythm via silence-detection, no visual glitches at any cut point. This is the same frame-by-frame process used on the spec ads this session — don't skip steps because a deadline is close.
4. Package for review: the clip(s), a one-line QA summary, and a reminder of what still needs human ears (exact wording/accent — QA can't verify audio content, only rhythm).

**Boundaries:**
- Never sends a clip to a client. Every asset goes to the user for approval first (§3) — no exceptions, this is the explicit human checkpoint in the whole pipeline.
- If QA fails (product mismatch, face drift, bad cut, generation glitch) — regenerate before presenting to the user, don't present known-flawed work "for a first look."
- If the brief is ambiguous or missing something a script genuinely needs, ask rather than guess — a wrong assumption here costs a full regeneration cycle.

---

## 3. Approval — Human Checkpoint (not an agent)

The user reviews the clip(s) against the original brief and either approves or requests changes. This step is deliberately manual — it is the one place in the pipeline with no agent, by explicit design. On approval, Sales Agent §1.4 (Delivery) picks up.

---

## 4. Supervisor Agent

**Owns:** keeping the whole pipeline honest, and closing the loop after a job completes.

**Where state lives:** `Outbound_Target_List.csv`, `Category_Exclusivity_Log.csv`, `Website\brand-pitch.html` (Selected Work + testimonial placeholders).

**Process (run this as a periodic pass — see Scheduling below for suggested cadence):**
1. **Stuck-item check:** scan the target list for anything with no status change in 4+ business days that isn't "Complete" or "Lost/Passed" — flag it to the user rather than silently letting it rot.
2. **Conflict re-check:** before Sales drafts any new cold pitch, confirm the exclusivity log has no active window for that category (this duplicates part of §1's own check as a second gate — cheap insurance).
3. **On Complete:** 
   - If a testimonial/feedback was received, replace one of the `[Client testimonial — to be added]` placeholders in `brand-pitch.html` (§5, Selected Work section).
   - If the final asset is strong and the brand consents, consider it for the Selected Work video grid (currently 3 spec ads live there).
   - Confirm the exclusivity log entry reflects the real, final agreed terms (not just what was drafted mid-negotiation).
4. **Report:** a short summary to the user of what moved, what's stuck, and what got updated — not a silent pass.

**Boundaries:**
- Never edits brand-pitch.html copy beyond the testimonial placeholders and Selected Work grid without the user's sign-off — it's a live brand-facing page.
- Never removes or overwrites an exclusivity log row — append/update only, keep history.

---

## Affiliate marketing agents — deferred

Per the sequencing decision (2026-07-10): UGC pipeline first. When this track is picked up, it maps onto the existing Master Overview pipeline (Research → Scoring → Script → Video → Edit → Schedule → Analyse) as:
- **Research/Scoring Agent** — best-seller-filtered candidates run through the existing Gate (G1–G6) + Scoring (D1–D5) framework already defined in `FUTURE_FINDS_MASTER_OVERVIEW.md` §5.3.
- **Production Agent** — very likely the *same* agent as §2 above, fed an organic-post brief instead of a UGC-ad brief; revisit whether a split is actually needed once volume is real.
- **Analytics Agent** — closes a real gap flagged in the original project review: no revenue/EPC/save-rate tracking exists anywhere yet.

Not built yet. Revisit once the UGC pipeline above is running for real.

---

## Scheduling — not yet turned on

Everything above currently runs on manual invocation ("run the sales agent," etc.). To make Sales Agent inbox-checking and Supervisor's stuck-item pass actually autonomous on a schedule (e.g., Sales checks + drafts daily, Supervisor runs weekly), that needs an explicit recurring scheduled job — worth setting up once the process has been run manually a few times and the user is comfortable with how it behaves. Given the Gmail connector is draft-only, the ceiling of what an unattended scheduled run can do is bounded (it can never actually send), but it's still worth a deliberate go-ahead before it runs unattended rather than turning it on by default here.

---

*Future Finds · Agent Operating Procedures v1.0 · July 2026*
