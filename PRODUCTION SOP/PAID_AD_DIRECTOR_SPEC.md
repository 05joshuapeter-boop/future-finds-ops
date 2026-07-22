# PAID AD DIRECTOR SPEC — the clean-look canon
## v1.0 · 2026-07-21 · governs ALL paid-track / client / portfolio ad generation
## Companion to MARURI_GENERATION_MASTER_REFERENCE.md (which governs ORGANIC only). Where the
## two conflict on a paid clip, THIS doc wins. The §7d anti-AI-tell physics rules apply to BOTH.

---

## 0. ROLE

This spec is the "professional UGC ad director" — every paid-track prompt is assembled from
these blocks, and every paid-track output is judged against §6 before it reaches a client or
the portfolio. Purpose: direct-response ad creative that a performance marketer would run,
with zero AI tells, while staying true to Maruri's brand (warm, intelligent, never shouty).

**The core difference from organic:** the organic track hides AI tells behind a 2012-era
degradation shield. The paid track has NO shield — it must survive scrutiny at modern clean
quality. That means the model-weakness rules (§3) matter MORE here, not less.

---

## 1. LOOK — "modern creator UGC ad", never "production shoot"

The convention paid UGC lives in: shot by a creator on their own current-gen iPhone, in their
own home, in daylight. Clean but casual. It must NOT look like an agency shoot — brands buy
UGC precisely because it doesn't look like advertising.

**Camera block (paste-adapt into every paid prompt):**
> Shot on a current iPhone front camera, handheld selfie-style at arm's length, eye level,
> with slight natural handheld sway — never tripod-static, never gimbal-smooth. Small phone
> sensor with deep focus: everything from her face to the background equally sharp — NO
> background blur, NO bokeh, NO shallow depth of field, NO portrait mode. Bright natural
> daylight from a window, even and true-to-life — no studio lighting, no rim light, no
> beauty-dish look, no colour grade, no cinematic contrast. Modern phone processing: clean,
> neutral, slightly punchy but ordinary — exactly how an iPhone renders a bright room, not
> how a film camera renders a set. Subject fills ~70–78% of frame, framing very slightly
> imperfect and off-centre, like a real self-recorded creator ad.

**Banned words in paid prompts (they summon the film-set look):** cinematic, bokeh, studio
lighting, colour grade, shallow depth of field, film look, dramatic lighting, golden hour
glow, lens flare, slow push-in.

## 2. DIRECTION — energy, structure, delivery

- **Register: "warm direct-response."** Brighter and ~15% faster-paced than organic Maruri,
  but still her — conspiratorial, intelligent, soft-spoken confidence. Never shouty, never
  salesy-grinning, never MLM energy. The viewer is a smart friend, not a lead.
- **Structure (10s):** hook lands inside the first 2 seconds (no camera-fumble openings on
  paid — that's an organic device; ads earn attention with the words, not the stumble) →
  build → one product claim → memorable close with direct eye contact.
- **Eye contact:** direct to camera for hook and close; may glance at prop mid-clip. The
  close ALWAYS lands on-camera with a warm look (the organic §4 rule carries over).
- **Gestures:** small, wrist-to-chest height only (render-artifact zone above/faster).
- **Single continuous take.** Multi-shot edits come from CapCut/client B-roll, never from
  multi-shot generation (cross-shot face drift is an instant tell).
- **WITH-not-AT applies to ads too:** pain-point hooks tease the problem playfully, never
  scold the viewer ("do you actually know..." = in on the joke; "you're wasting money" = AT).

## 3. ANTI-AI-TELL RULES (carried from §7d — these are model physics, not aesthetics)

| Rule | Why it survives the track switch |
|---|---|
| Force deep focus, repeat NO-bokeh several ways | the model defaults to cinema DOF; a clean ad with bokeh reads "AI film", not "phone" |
| No hero-object staging; props incidental, angled, low | styled product tableaus read as CGI adverts |
| No live manipulation of food/soft/deforming objects | deformation physics is the model's weakest render |
| **Screens NEVER readable** — phone angled away/low | generated UI text is a guaranteed tell; real client UI arrives as B-roll in the edit |
| No brand text rendered anywhere | garbled text = instant giveaway |
| Accurate lip-sync, realistic blinking, micro-movements pinned in every prompt | dead-eye stillness is the #1 clean-look tell |
| Accent pins verbatim from organic canon (consistent soft London English, never drifting) | voice drift breaks the character across the portfolio |
| Small gestures only | hand artifacts |

## 4. AUDIO

Clean modern phone-mic voice: intelligible, present, natural room tone, no boxy vintage EQ.
No music bed at generation (beds/SFX are an edit-stage decision per deliverable — client ads
usually get the brand's own audio treatment anyway). Prompt pin: "clean spoken voice with
natural quiet room tone only — no music, no sound effects."

## 5. COMPLIANCE (every paid script, before generation)

- **ASA presenter framing:** product-capability claims only ("this is the app that shows
  you"), never personal testimony ("it fixed my finances"). Check the script doc's ASA line.
- **Concept work** stays clearly labelled as concept in the portfolio; never imply a real
  client relationship that doesn't exist.
- Deliverables to real clients ship with a one-line note: platform AI-disclosure toggles are
  the advertiser's responsibility (contract clause 5), plus which toggle to tick on Meta/TikTok.

## 6. DRAFT PROTOCOL + QA GATE (credit discipline, paid edition)

1. **Draft at 10s · 720p · fast (35cr).** Iterate at draft tier until the clip passes QA.
   Max ONE revision draft on prompt-language changes (same rule as organic: change the
   words, not the dice) before stopping to reassess.
2. **QA checklist (judge the RAW draft — no grade will rescue it on this track):**
   lip-sync exact · transcript word-perfect · accent consistent London · deep focus verified
   (background sharp) · no readable screen/text · hands clean · energy = warm
   direct-response, not flat/salesy · hook lands <2s · close on-camera warm look.
3. **Final render at 1080p · std (90cr)** ONLY after a draft passes QA fully.
   ⚠ OPEN ITEM: plan sheet suggests 1080p/std may cap at 8s duration — verify with
   `get_cost`/`models_explore` at final-render time; if capped, options are (a) tighten
   delivery to 8s (preferred — ads are better shorter) or (b) render 720p/15s and
   `upscale_video`. Resolve on first final render and record the answer here.
4. Every attempt gets a QA_LOG.md row, same as organic.

## 7. THE GO/NO-GO GATE (why Ad 004 exists)

After the 004 draft cycle, make the honest call: **does clean-look Seedance output pass a
performance marketer's eye?**
- **PASS** → proceed to 005/006, then finals, then portfolio → outreach.
- **BORDERLINE** → iterate ONE more prompt revision; if still borderline, downgrade the
  claim on the site (sell hook-scripting + stylized/organic-look ads, not clean-look) before
  any outreach goes out.
- **FAIL** → the studio pitch changes to what we CAN prove (organic-style ads, scripts,
  strategy) — do NOT run outreach on an undeliverable promise. Selling a look we can't
  render is the #1 rookie mistake this project must not make.
