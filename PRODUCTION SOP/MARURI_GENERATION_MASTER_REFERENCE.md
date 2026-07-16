# MARURI GENERATION MASTER REFERENCE
## The one sheet to load before every single generation
## v1.1 · 2026-07-13 · Future Finds / Maruri Mori
## (v1.1 = post-adversarial-verification fixes: corrected camera block to the locked 2012-era spec, age per Bible, worked prompt example added, hook definitions added, repurposing sourced from graded masters only)

---

# 0. WHAT THIS IS AND HOW IT RANKS

This sheet consolidates everything that matters **at the moment of generating a clip** — character, behaviour, voice, wardrobe, camera, realism, credits, repurposing, and the affiliate/UGC business constraints — into one document, so nothing gets missed because it lived in a file nobody re-read.

**Precedence:** `MASTER_CHARACTER_BIBLE.md` remains the override authority on who Maruri *is*. This sheet is the operational layer on top of it and consolidates `Hook_Playbook.md`, `iPhone_Camera_Spec.md` (v3.0), `Production_Economics.md`, and the business docs. Where this sheet conflicts with an *older* doc (`FUTURE_FINDS_MASTER_OVERVIEW.md`'s camera spec and 2-clip format, `PRODUCTION_PIPELINE_SOP.md`'s ElevenLabs stages, Spec Ad 001/002's production notes), **this sheet wins** — those sections are superseded and listed in §12.

**The operator's standard (verbatim chat directive, 2026-07-13 session — not from any doc, recorded here as the standing bar):** *"if it's too clear and the quality and resolution are like something that you'd see in a movie then it failed it's task."* Cinematic = failure. Real phone, real girl, real room.

---

# 1. PRE-FLIGHT CHECKLIST (run this list before every generation)

1. ☐ Script matches a hook type (§3a — Type 6 or 7 preferred) and passes the tone test in §4 (WITH the viewer, not AT them).
2. ☐ Dialogue is 25–35 words for a 10s clip (hard ceiling ~40 — shipped 10s scripts run 28–36 words including fillers). Pause/beat directions live OUTSIDE the quoted dialogue (§5).
3. ☐ Character element token `<<<b40df106-df2c-4015-ab66-19fbd488d634>>>` opens the character sentence (§7a shows exact placement). Model `seedance_2_0`, 9:16, native audio.
4. ☐ Settings: **organic = 10s / 720p / fast (35 credits)**. Paid brand work = its own track, see §9.
5. ☐ Accent pin pasted verbatim (§5). Warmth pin included if she's mid-task/hurried (§5).
6. ☐ Anti-music pin pasted verbatim as the prompt's final sentence (§5).
7. ☐ Product handling written as incidental, never presented (§3) — or zero product for Type 7. Product reference image imported and attached if a product appears (§9).
8. ☐ Wardrobe: no repeat within the last 3 posts (sheet-level rule tightening the Bible's "never consecutive"). Pick freely from the unused list. Log it in §6 when the script is written.
9. ☐ Location, register, and exit style each varied from the previous clip — check the §6 rotation table, which logs all three.
10. ☐ If a product is in frame: exclusivity check (§9) passed, affiliate link ready.
11. ☐ Pass `declined_preset_id: "24bae836-2c4a-48e0-89b6-49fcc0b21612"` proactively to skip the "IN THE DARK" preset interrupt (session-verified 2026-07-13; not in any other doc — if generation errors on this ID, drop the param and handle the interrupt manually).
12. ☐ **After generation, in this order:** QA (§7c) → human listen (accent/warmth — text QA can't hear) → mandatory ffmpeg grade (§7b) → only then postable. Repurposing cuts come from the **graded master**, never the raw CDN URL (§8).
13. ☐ Plan the repurposing cuts before moving on (§8) — one generation must yield 3–4 pieces of content.

---

# 2. WHO SHE IS — IDENTITY, PERSONALITY, BELIEFS

## Identity card
| Field | Value |
|---|---|
| Name | Maruri Mori (Mah-roo-ree Mo-ree) |
| Heritage | Japanese father / Thai mother — **not** "Japanese-British" (see drift warning below) |
| Born/raised | London; lives in Westminster |
| Age (perceived) | **mid-20s** (per the Bible — Scripts 006–013 drifted to "late 20s"; the Bible wins) |
| Hair | dark brown to black, straight or softly wavy (Bible range); recent canon clips render it long and softly wavy — stay in that lane |
| Job | Product designer at a mid-size tech company (her recurring credential: "I design products for a living") |
| Archetype | Soft-Spoken High-Value Woman |

**Prompt-wording drift warning:** Scripts 006–013 described her as "mixed Japanese-British, late 20s" — both wrong per the Bible (Japanese/Thai heritage, British by birthplace only; mid-20s). The face comes from the element token regardless, so no visual damage was done. Going forward use the canonical character sentence in §7a.

## Personality — always on
Calm · emotionally mature · observant · thoughtful · soft-spoken · warm · intelligent · grounded. Warmth is conveyed through tone, never volume.

## Personality — revealed in small moments (this is where the "cute" lives)
Playful · dry wit · lightly teasing · subtly funny · genuinely cute in unplanned-feeling beats (head tilt, catching herself smiling, scrunched-nose smile at her own reflection).

## What she is NOT — hard list
Not bubbly. Not loud. Not girlboss. Not preachy. Not self-deprecating for relatability. Not trend-reactive. Not a commentator. **Not entitled, not snobbish, not aloof** — see §4, this failure mode actually happened and is now a standing guardrail.

## Beliefs (what her content quietly argues)
- Things should be chosen with care — fewer, better (father's less-is-more; mother's "beauty should invite, not intimidate").
- Recommendations are worthless unless the person would buy it again with their own money. "I don't review things. I just... only share the ones I'd actually buy again."
- Trust is worth more than reach. She is never desperate for attention — no "comment below!!", no "you NEED this", no "OMG", no "Buy now".
- Nothing has to be optimised. She's allowed to be unbothered.

## Established lore (safe to reference; keep consistent)
Minimal Westminster flat · wakes early, spends ~an hour being quiet (reading, journaling) · quit coffee for matcha (**timeline conflict exists in old scripts — say "a while ago", never a specific duration, until the operator picks canon**) · carries the same tote daily · lights the NEOM candle most evenings · silk pillowcase ~four months in · same pen since design school · close to her mother, references her taste occasionally · small friend group, quality over quantity · faith private, never preached.

---

# 3. HOW SHE BEHAVES ON CAMERA — ANTICS, QUIRKS, STAGING

## 3a. The two working hook formats (condensed from `Hook_Playbook.md` — read that file for scaffolds)

**TYPE 6 — CAUGHT MID-ACTIVITY** (product content; operator-confirmed highest engagement)
```
[mid-activity, not looking at camera] → [stop trigger: "oh—", "wait—", "actually—"]
→ [turns, talks candidly about a feeling/realisation — NOT the product yet]
→ [mid-sentence, casually touches/has the product while still talking — never a reveal]
→ [trails off back toward the activity, or a flat low-key line — never a hard CTA]
```
The product beat must not feel like a beat: she happens to be holding it while she keeps talking. If a direction reads as "now she shows the product," rewrite it. Single continuous take, no cut, always.

**TYPE 7 — THE HOT TAKE** (zero product, pure growth)
```
[mundane activity, same mid-task DNA] → [genuine trigger: "okay actually—", "no because—",
"unpopular opinion but—"] → [states the opinion plainly and confidently — no hedging,
but never at the expense of warmth] → [one brief specific reason, one or two sentences]
→ [a real, warm look at camera — she's including the viewer — then a light close that
leaves room for them, not a door-slam]
```
Two guardrails, both mandatory: (1) topics stay low-stakes taste/lifestyle only — the two-friends-over-coffee test; (2) the WITH-not-AT rule, §4.

**CAMERA FUMBLE** (stackable cold open, 1–2s, three beats max): walks into frame not yet "ready" — leans in, taps the lens, mutters something functional to the phone ("Hold on— Can you— okay. Right."), then resets into the hook. Strongest "not produced" signal available. Only works as the true opening of one unbroken take.

## 3b. Signature quirks (rotate; never all in one clip)
| Quirk | When | Frequency |
|---|---|---|
| Hair tuck | transitioning between thoughts | 1–2× per video |
| Head tilt | curiosity, considering, "unpopular opinion, but—" | 1–2× per video |
| Soft giggle / half-laugh | something genuinely delights her | 0–1× per video |
| Eyebrow raise | unexpected detail | 1–3× per video |
| Playful side smile | teasing the viewer | 0–1× per video |
| Scrunched-nose smile | catching herself (e.g. own reflection) | occasional |
| Eye-crinkle smile | knows she's being a bit cheeky | pairs with head tilt |

## 3c. Staging
She is never sitting camera-ready. Locations used so far (vary them; the per-script log is in §6): desk/workspace · kitchen · living room · bedroom (evening lamp light, never overhead) · bathroom mirror · hallway/front door · travel/hotel. All "minimal London" spaces — **lived-in, unstyled, ordinary**: a real mug, an actually-thrown throw, a few plates on the shelf. Sterile-perfect rooms are an AI tell.

## 3d. Product handling — never a reveal, ever
The model defaults to presenting products; every prompt must over-specify against it:
- Rests a hand on it without picking it up. Shifts the tote on her shoulder without lifting it. Picks the bottle up without looking at it. Gestures vaguely at the blanket while holding her mug.
- Or background placement: product on a shelf, slightly out of focus but clearly visible, part of the scene.
- Prompt language that works: *"casually, without lifting it or presenting it to camera"*, *"the pickup should look incidental, not presented"*, *"no formal product-reveal gesture"*.
- Never render brand text/labels directly — keep tins/labels turned away or out of focus. Multi-object products (charger + watch + earbuds) fail geometry; single objects only.

## 3e. Exits and sign-offs (rotate; per-script log in §6)
- Trail-off back into the task: "Anyway." / "Ask me later." / "Where was I."
- Mid-motion exit: turns to the door, clip ends mid-departure, no look back.
- Flat "Worth it." — the locked spec-ad/paid closer. Flat, final, no upward inflection.
- Type 7 warm-look close: holds real, warm eye contact with camera ON the closing line, **then** turns away — never already turned away when the line lands (§4).
- Silent close: glance down, soft half-smile, small head tilt, fade. No outro words.

## 3f. Single-take integrity — non-negotiable
Type 6/7 and camera-fumble clips are one continuous take, no cut, no splice — the illusion collapses at any edit point. If a variant is needed, generate a full second take. (CapCut stitching exists only for paid brand deliverables and non-single-take formats — never organic Type 6/7/fumble content.)

---

# 4. ATTITUDE — THE "WITH, NOT AT" RULE (standing guardrail, born from a real failure)

**What happened:** the first Type 7 batch read as entitled/snobbish. Root cause was structural: she stated opinions flatly and turned away without ever really looking at the viewer — the literal body language of not needing your reaction — plus dismissive-comeback phrasing.

**The rule (Character Bible §9.3 + §6.2):** she talks *with* the viewer, not *at* them. She is grounded, not entitled. Confidence, not superiority.

**Banned phrase patterns:**
- "It's called [X]" (dismissive-comeback structure)
- "I will never understand why..." (implies other people are foolish)
- Hard one-word full-stop closes ("Done.")
- "You can disagree / I won't be offended" (performs graciousness instead of inviting a response)

**Required beat:** every opinion clip includes one genuine, warm, direct look at camera before she moves on — eyes saying she's actually curious what you think, not permitting you to think it.

**The test:** does this sound like a grounded person thinking out loud with a friend — or a verdict from someone who doesn't need to check how it landed? If the second: rewrite drier and *warmer*, not louder or funnier.

**Opinions stay about her own taste:** "I just don't get the appeal, personally" — never a judgement on people who disagree.

---

# 5. HOW SHE SPEAKS — VOICE, ACCENT, SIGNATURE LANGUAGE

## Voice profile
Soft **London** English accent (clean but warm — not RP) · medium-low pitch · slightly slower than average, deliberate · warm texture, slightly breathy in moments · calm enthusiasm, never performative. **She never exclaims.** No exclamation points in scripts.

## Word budget
10s clip = **25–35 words of dialogue, hard ceiling ~40** (shipped 10s scripts: 28–36 words including fillers). Longer dialogue gets rushed or truncated delivery. If the script needs more words, it needs more seconds — and a reason to spend them.

## The three pins — paste verbatim, every prompt

**Accent pin** (drift is a proven recurring risk):
```
She speaks in a consistent soft London English accent throughout — the exact same accent from the first word to the last, never shifting, never drifting toward RP or any other regional accent — medium-low pitch, warm, conversational, natural pauses.
```

**Warmth pin** (whenever she's rushed, distracted, or mid-task — proven failure: "hurried" rendered as "doesn't care"):
```
Even though she is [rushing / distracted / mid-task], her energy stays genuinely warm the whole time — not flat, not indifferent, not bored.
```

**Anti-music pin** (the final sentence of every prompt — proven failure: model added lofi music unprompted; on paid work this protects a contractual warranty, §9):
```
Audio: clean spoken voice with natural quiet room tone only — no music, no sound effects.
```

## Dialogue lock + pause notation rule
```
She says exactly these words and nothing else: "..."
```
**The quoted string contains only spoken words and ellipses** ("..." = natural breath pause). `[pause]`, beat directions, and gestures live OUTSIDE the quotes as staging prose — never inside, or the model may voice them. Shipped example: dialogue = `"Wait, actually... the whole ten-step skincare routine thing is mostly just marketing."` with the staging sentence *"she half-laughs and turns more toward the camera"* written separately.

Always pair the lock with: *"Accurate lip-sync, realistic blinking, natural human micro-movements, no exaggerated acting, nothing performative — she is thinking out loud, not delivering a line."*

## Signature phrases (her verbal fingerprint — use naturally, don't stack)
- **Openers (self-interruption, mid-task):** "Wait—" · "Okay wait, sorry—" · "Hold on—" · "Oh — actually" · "No, because—" · "Okay, actually—" · "Wait, actually—"
- **Reveal:** "It's just... this." (the product dismissed as obvious, never pitched)
- **Social proof trigger:** "Someone asked me..." / "People always ask me..."
- **Habit-as-sell:** "I don't even think about it anymore" / "I notice it on the days I don't use it"
- **Genuine-self-check:** "Honestly..." / "Honestly?"
- **Landing a point:** "Sounds small. It's not." (the pause between sentences does the work)
- **Closers:** "That's it. That's the whole take." · "Worth it." · "Anyway."
- **Fillers in dialogue:** "like,", "what," mid-count, "just", "actually", "genuinely". 

## Register rotation
Default register is calm-warm. A deliberately excited register exists — forward lean, bright eyes, faster pace, like she's delivering news she's been sitting on (per Script 004 v2's direction) — used sparingly. New sheet-level rule (extending the Hook Playbook's no-same-hook-structure-back-to-back rule): don't use the excited register two posts in a row either. Register per script is logged in §6.

## Price talk
Never speak a high price aloud. £89.99 becomes "under a hundred pounds" spoken / "Under £90" in caption. Genuinely high prices (£100+) don't get said at all pre-click.

## Captions (post text)
First line = the hook, never starts with "I", max ~6 words, ends on a hard stop. 2–3 lines max. #FutureFinds first hashtag, 3–5 total, never generic-only. 🤍 recurs. Affiliate posts carry: *"(Affiliate link — I may earn a commission at no extra cost to you.)"* Links live in bio, not caption.

---

# 6. FASHION, WARDROBE & THE ROTATION LOG

**Style rule:** "off-duty tech designer" — neutrals, soft tones, muted pastels, quality fabrics, fits well, no visible logos. Never oversexualised, never trend-first, never loud. Hair: default down or relaxed half-up; tied back only with staging justification (workout, bathroom routine).

**Consistency anchors that never change:** thin gold chain, small gold hoops, the face (element token), the accent. The jewellery does NOT need to be written into every prompt — but never write a prompt that contradicts it.

**Rotation rules:** wardrobe — no repeat within the last 3 posts (pick freely from the unused list). Location, register, and exit — each varied from the immediately previous clip. **Log every new script here when it's written; confirm the row when QA passes. Next script number: 017.**

| Script | Outfit | Location | Register | Exit/sign-off |
|---|---|---|---|---|
| 001 | cream/soft-white fitted neutral top | desk | calm-warm | silent close (glance down, half-smile, fade) |
| 002a | white/soft neutral oversized button-up | desk | calm-warm | "Worth it." |
| 002b | linen/jersey travel outfit | hotel/travel | calm-warm | "Worth it." |
| 003 v2 | grey/black activewear, hair loosely back | living room, morning | warm-conspiratorial | environmental return (looks back to window) |
| 004 v2 | soft oversized cream top | kitchen | **excited** | CTA-era close ("Link's in bio") |
| 005 | clean neutral oversized shirt | desk | quiet-connoisseur | "Worth it." |
| 006 | cream ribbed knit | kitchen | calm-warm | trail-off ("more explaining than anyone needed") |
| 007 | cream ribbed knit (out-the-door) | hallway/front door | hurried-warm | mid-motion exit ("I need to go") |
| 008 | cream ribbed knit (crewneck) | desk | calm-warm | "Anyway. Where was I." |
| 009 | cream ribbed knit (oversized) | bedroom, evening lamp | soft-evening | "It's silly but it's true." |
| 010 | cream ribbed knit (cardigan) | living room, evening | calm-warm | "Ask me later." |
| 011 | oatmeal oversized cardigan | kitchen | warmly-amused | warm-look close ("That's it, that's the whole take.") |
| 012 | camel wrap cardigan over white tee | living room, evening | cute-amused | warm-look + trail-off ("Anyway.") |
| 013 | sage green fine-knit jumper | bathroom mirror, morning | wry-warm | warm-look ("Feel free to fight me on it though.") |
| 014 | black relaxed turtleneck | hallway/entry, evening | warm-ritual/honest | warm-look ON closing line, exits into flat |
| 015 | white linen shirt | kitchen, afternoon | cheeky-warm | warm-look + trailing "...sorry", back to scone |
| 016 | stone-grey loungewear set | bedroom, morning | playful-amused | warm-look + question held a beat, then pillow |
| **Unused next:** | charcoal fine-knit · dusty-blue crewneck | | | |

**Scheduling constraint (added 2026-07-13, pre-spend check):** 011–016 are six consecutive Type 7 hot takes in the script sequence — they must NOT post consecutively. Interleave every hot take with a Type 6/product or other-format post; the hot-take format itself reads as engagement-farming to this influencer-sceptical audience if it runs back-to-back.

(006–010 all rendering in the same cream knit is the mistake that created the rotation rule.)

---

# 7. CAMERA & REALISM — THE ANTI-AI PLAYBOOK

## The goal, stated plainly
The clips should be real enough that **the comment section argues about whether she's real or AI**. That debate is the engagement engine — but it must happen *organically from realism*, never from us baiting it (§10 for the brand rules).

## The failure test
If a clip looks cinematic, sharp, high-dynamic-range, colour-graded — like a movie or an ad — **it failed**, no matter how good the performance is. The target is: an old-ish phone on a tripod in a real flat.

## 7a. Stage 1 — the generation prompt

**Camera block — paste into every organic prompt** (this is the locked v3.0 block from `iPhone_Camera_Spec.md`; the model applies the degradation language only weakly — that's why Stage 2 exists — but paste it anyway, it still shifts the output in the right direction and it fully controls framing/behaviour, which the model DOES follow):
```
Camera: shot on an iPhone from around 2012 (iPhone 4S/5 era), not a modern phone, mounted on a tripod, eye level, roughly 26mm-equivalent wide angle. Visibly lower dynamic range than modern phone video, noticeably more visible grain and noise especially in shadow areas, slightly flatter and cooler colour rendering than today's punchy computational-photography look, softer per-pixel detail, mild rolling-shutter wobble on quick movement, quality reads like compressed 1080p30 rather than crisp modern 4K. No added colour grading beyond the period-camera look itself. Subject fills roughly 65% of the frame, no portrait-mode background blur, slightly imperfect casual framing like a self-recorded creator video caught mid-task. [Resolve lighting per scene: "Natural window light only" for daytime / "warm practical lamp light from the side, no overhead light, more visible noise in low light" for evening — this line is a template slot, not verbatim.]
```
Never say: "cinematic", "bokeh", "studio lighting", "slow push in", "colour grade", or **"modern iPhone" / "iPhone 12/13/14/15/16"** (wrong generation — too sharp, too much dynamic range; a bare "shot on iPhone" defaults modern, so always keep the 2012-era wording).

**Element token placement convention:** the token opens the character sentence, which is the second sentence of the prompt (after the format line). Canonical character sentence:
```
<<<b40df106-df2c-4015-ab66-19fbd488d634>>> — a woman in her mid-20s, of Japanese and Thai heritage, born and raised in London, long dark softly-wavy hair, warm brown eyes, natural warm skin —
```

**Full worked prompt template** (assembled per this sheet; structure from the shipped, approved Script 011 v1.1):
> UGC-style self-recorded talking video, single continuous shot. `<<<b40df106-df2c-4015-ab66-19fbd488d634>>>` — a woman in her mid-20s, of Japanese and Thai heritage, born and raised in London, long dark softly-wavy hair, warm brown eyes, natural warm skin — is in a minimal London kitchen in daylight, wearing [OUTFIT from §6 unused list], [MID-TASK ACTIVITY], genuinely mid-task, not looking at camera at first. She pauses, half-turns as if a thought just interrupted her, then turns fully to camera, meeting it properly. [ACCENT PIN §5.] [WARMTH PIN §5 if mid-task/hurried.] She says exactly these words and nothing else: "[DIALOGUE, 25–35 words, ellipses only inside quotes]". [STAGING BEATS: quirks from §3b, product handling from §3d if any, the warm look at camera from §4 if opinion content, then the exit from §3e.] Accurate lip-sync, realistic blinking, natural human micro-movements, no exaggerated acting, no gesture toward camera, nothing performative — she is speaking the way someone speaks when they're genuinely just thinking out loud, not delivering a line.
>
> [CAMERA BLOCK above, lighting slot resolved.] [Scene dressing: lived-in details, §3c.]
>
> Audio: clean spoken voice with natural quiet room tone only — no music, no sound effects. Audio quality slightly boxier and more compressed than a modern phone microphone, consistent with the visual period, but the voice itself must stay clearly intelligible and in the accent described above.

**How to invoke (session-verified):** primary = Higgsfield MCP `generate_video` tool: model `seedance_2_0`, the prompt above, `aspect_ratio "9:16"`, `resolution "720p"`, `duration 10`, `mode "fast"`, `generate_audio true`, `declined_preset_id "24bae836-2c4a-48e0-89b6-49fcc0b21612"`; product reference images attach via the medias/image-references parameter. Fallback if the MCP is down = CLI: `higgsfield generate create seedance_2_0 --prompt "..." --image <product-uuid> --aspect_ratio 9:16 --resolution 720p --mode fast --duration 10 --generate_audio true --wait --wait-timeout 12m` (note: the CLI path has no scene/dialogue QA equivalent — flag that gap if used).

## 7b. Stage 2 — the MANDATORY ffmpeg realism grade (deterministic; this is what actually guarantees the look)
Every organic clip gets this pass before it's considered postable. Zero credits. ffmpeg absolute path on this machine (winget install doesn't always land on PATH):
`C:\Users\tensi\AppData\Local\Microsoft\WinGet\Packages\Gyan.FFmpeg_Microsoft.Winget.Source_8wekyb3d8bbwe\ffmpeg-8.1.2-full_build\bin\ffmpeg.exe`

```
ffmpeg -i "<raw-clip-url-or-file>" \
  -vf "scale=w=trunc(iw*0.55/2)*2:h=trunc(ih*0.55/2)*2:flags=bicubic,scale=w=trunc(iw/0.55/2)*2:h=trunc(ih/0.55/2)*2:flags=bicubic,eq=contrast=0.88:saturation=0.78:brightness=0.02:gamma=0.95,colorbalance=rs=-0.06:gs=0.0:bs=0.09:rm=-0.04:gm=0.0:bm=0.06,noise=alls=18:allf=t+u,gblur=sigma=0.5,vignette=PI/6" \
  -af "highpass=f=120,lowpass=f=8500,acompressor=threshold=-18dB:ratio=3:attack=5:release=50" \
  -c:v libx264 -crf 26 -preset medium -c:a aac -b:a 96k -movflags +faststart \
  "<script#>_graded.mp4" -y
```
What it does: softens per-pixel detail (down/up rescale) · flattens contrast + desaturates (kills the AI-punchy look) · cools shadows/mids (older-phone white balance) · adds visible grain · mild blur + vignette · boxier compressed audio · crf 26 adds real compression artifacting. Tuning knobs: `iPhone_Camera_Spec.md` v3.0.

**File naming convention:** `VIDEO\<script#>_raw.mp4` (optional local copy) → `VIDEO\<script#>_graded.mp4` (the master everything else derives from) → `<script#>_teaser.mp4`, `<script#>_still.jpg`, `<script#>_recap.mp4`.

## 7c. QA — pass criteria and retry protocol
Run `video_analysis_create` on the raw clip (cost ~0.1–0.4 credits — negligible, always do it). **Pass requires all of:**
1. Transcript word-perfect against the dialogue lock (no added/dropped/changed words).
2. No music or sound effects.
3. No formal product-reveal gesture; product handling matches the script's blocking.
4. Scene/wardrobe/location match the script.
5. Then the human listen: accent consistent London throughout, warmth reads as warm (not flat/indifferent), overall delivery matches the intended register.

**On failure:** ONE redo maximum, with strengthened prompt language targeting the specific failure (regenerating with an identical prompt is proven to fail the same way — 007 and 010 both needed language changes, not re-rolls). If the redo still fails, stop and escalate to the operator — do not burn a third generation unilaterally. (Precedent: 007 v2's residual body-turn was accepted rather than chasing a v3.)

## 7d. The full anti-AI-tell checklist (why each thing exists)
| Technique | AI tell it defeats |
|---|---|
| ffmpeg grade (grain/flat/soft/cool) | too-clean skin, hyper-sharp detail, punchy generative colour |
| **Force deep focus — "NO bokeh / NO shallow DOF / small old-phone sensor, everything equally sharp"** | **the model's #1 default tell for lifestyle clips: cinematic shallow depth-of-field that melts the background into bokeh and reads as a film shoot, not a phone. A polite "no portrait blur" line loses — repeat NO-bokeh several ways.** |
| **Selfie-held, face-led framing (subject ~78%, food/object incidental at frame edge)** | **hero-object staging: a fanned-out styled arrangement (food board, positioned props) reads as a commercial advert. A hand-held selfie physically can't compose one. Keep any product/food small, low, un-presented.** |
| **No live manipulation of food/soft objects (already-assembled, held still)** | **spreading jam, pouring, squishing — deforming-object physics is the model's weakest render; the hand/food/utensil boundary is the artifact zone. Show the after-state, not the action.** |
| Single continuous take, 10s | cuts expose face/lighting inconsistency between generations; short duration limits within-clip drift |
| Caught mid-task staging + camera fumble | "composed and camera-ready at frame one" reads as produced/synthetic |
| Slightly imperfect framing | perfect rule-of-thirds composition reads as staged |
| Lived-in set dressing (real mug, thrown throw, ordinary shelves) | sterile perfect interiors are a generative-model signature |
| Natural micro-movements, realistic blinking pinned in prompt | dead eyes / uncanny stillness |
| Small wrist-to-chest gestures only | large fast hand gestures invite hand-render artifacts |
| Wardrobe rotation | identical outfit across posts reads as reused AI footage |
| Native room-tone audio, no music, boxier EQ | pristine silence or generated music flags synthetic audio |
| No brand text rendered | garbled label text is a classic giveaway |
| Platform re-compression on top of the grade | works FOR us — each upload generation adds realism |

## Generation settings (locked)
| Context | Settings | Credits |
|---|---|---|
| **All organic content** | seedance_2_0 · 9:16 · **10s · 720p · fast** · native audio | **35** |
| Paid brand deliverables | see §9 — longer + 1080p, clean look, no vintage grade | 90+ |

720p is invisible after the grade + platform re-compression — and softness is the aesthetic anyway. Never generate organic at the old 15s/1080p/std (135 credits) rate.

## 7e. Finishing pass — music bed + burned captions (locked 2026-07-16)

**Pipeline:** raw clip → 2012 grade → music bed sidechain-ducked under her voice → burned
captions → export. One automated ffmpeg command — see `Pipeline_Tools/finishing_pass.sh` in
the future-finds-ops repo. Proven end-to-end on clip 015.

**Caption style: LOCKED to Style B — "Signal."** Word-by-word amber highlight (warm accent
from the brand's cool-logic-to-warm-humanity gradient) sweeping across the phrase as she speaks
it; base text off-white, thin/letter-spaced. Template: `Pipeline_Tools/style_B_signal.ass`.
Timing is derived from real silence-detection on the clip's own audio (natural phrase/pause
boundaries), not guessed — see the script for the method.

**Music beds — mood-matched by content type, not one-size-fits-all:**
| Content type | Bed | Status |
|---|---|---|
| Slow lifestyle / "morning routine" / "what I did today" (third-person, reflective) | **Easy Lemon** (Kevin MacLeod) | Locked 2026-07-16 |
| Hot takes / Type 7 engagement clips (e.g. 015) | TBD | Library candidates (Radio Martini variants, Cool Vibes, Chill) rejected as not distinctive enough. Moving to a custom ElevenLabs-generated track, "inspired by" user-supplied reference songs (described, not copied) — pending user's reference tracks + cost approval (separate ElevenLabs balance, not Higgsfield credits). |

**Rejected as a bed source:** Higgsfield's `sonilo_music` model — its own tool description
states it exists only for the game-generation pipeline and must not be used for standalone
audio. Do not use it here even though the backend doesn't hard-block the call.

---

# 8. REPURPOSING — MINIMUM POINTS, MAXIMUM OUTPUT

**The budget mindset: 1 generation → 3–4 posted pieces of content.** Credits are runway until UGC/affiliate income lands. Balance per `Production_Economics.md`: 3,918.8 checked 2026-07-12; ≈3,813 after the three Type 7 clips (2026-07-13). At 35/clip that's ~108 generations if discipline holds. QA adds ~0.1–0.4 credits/clip — immaterial.

**Everything below derives from `<script#>_graded.mp4` — NEVER from the raw CDN URL.** A teaser cut from ungraded footage posts the exact clean look that fails the §7 test.

From every graded master:
1. **The primary post** — full graded clip, per the weekly schedule in `CONTENT SCHEDULE\` (posting windows and cadence live there, not here).
2. **Teaser cut** — first 3–5s (the fumble/interruption beat) as a separate later post with a different caption. `ffmpeg -i "<script#>_graded.mp4" -t 5 -c:v libx264 -c:a aac <script#>_teaser.mp4 -y`
3. **Still frame** — for a carousel/Stories frame; pick a warm mid-expression moment, not mid-blink. `ffmpeg -ss <t> -i "<script#>_graded.mp4" -frames:v 1 -update 1 -q:v 2 <script#>_still.jpg -y` (this build needs `-update 1`)
4. **Re-caption repost** — same graded master **4–6 weeks later**, new burned-in hook text, once it's out of the algorithm's short memory window.

**Division of labour:** ffmpeg = the free deterministic layer (grade, cuts, frames). **CapCut = the manual creative layer** — burned-in text and caption styling (clean modern sans-serif, white/off-white only, upper or lower third, never covering the face, key words only — this style spec applies whichever tool burns the text; use CapCut when styling matters, ffmpeg drawtext for quick utility cuts), 1:1 recrops for paid work, stitching (paid/non-single-take formats ONLY, per §3f), and trending audio when used (organic only: her voice full volume, trending sound at 30–40%, beat drop timed to the pivot word — never generated in-model, never on paid work without clearance).

**Rights note:** we can freely recut our own organic content. Brands can NOT recut theirs — they buy variants (that's a deliberate revenue line). Never let a repurposing workflow blur into a brand deliverable.

---

# 9. AFFILIATE & UGC — BUSINESS RULES THAT BIND GENERATION

## Two tracks — never mix them
| | ORGANIC (affiliate/growth) | PAID BRAND WORK (UGC deals) |
|---|---|---|
| Settings | 10s/720p/fast | 15–45s runtime (rate card promise), generate 1080p, std mode if needed — **⚠ this deviates from the blanket "always 720p" directive and needs the operator's explicit sign-off; rationale: the rate card promises a 1:1 crop (720p master → only ~720×720) and brands buy against the sharp public demo reel** |
| Look | 2012-era grade, mandatory | **Clean, ad-native** — no vintage grade unless the brief asks |
| Aspect | 9:16 | 9:16 **+ 1:1 crop** (rate card promises both) |
| CTA | none spoken, link in bio | direct CTA allowed ("Link's below"), no brand names in spec ads |
| Music | never | only brand-supplied or cleared (terms-sheet warranty — model-generated music is uncleanable; the anti-music pin protects a contractual promise here) |
| QA | §7c | full golden-reference QA gate: face consistency, product accuracy vs brand reference image, frame-by-frame glitch check, human approval before client sees anything |

## Affiliate content rules (organic product clips)
- Product must pass the 6 gates first: ≥4.2★ with ≥150 reviews · in stock, Prime · under £200 · category fit (tech/lifestyle/home/wellness/aesthetic) · brand-safe · **photographs well** (G6).
- Audience sweet spot £15–80; links convert best under ~£50 on TikTok.
- **Exclusivity check — before ANY product appears in frame:** open `PRODUCTION SOP\Category_Exclusivity_Log.csv` (columns: category, brand, window terms, dates) and the NocoDB Deals table Status field. Rule: if the product's brand OR its product category has an active exclusivity window, or the brand's Deals row is Blocked — it does not go in frame, full stop; when ambiguous (adjacent category, expired-but-recent window), ask the operator. Snapshot as of 2026-07-13 (will go stale — check the log, not this line): Anker blocked; NEOM already featured twice (diffuser + candle — don't triple-expose the family).
- Product reference: import the real product image from the Amazon UK listing (MCP `media_import_url` / marketing-studio products fetch), attach it to the generation, and include *"matching the reference product exactly"* in the prompt. Beware multi-variant Amazon listings — verify the image is the right variant (the candle scrape pulled the wrong NEOM product once).
- Amazon links as amzn.to short links, confirmed live before posting; disclosure line in caption; bio link updated before the post goes up.
- The buying triggers her content activates: social proof, specific detail, discovery framing, aesthetic alignment, quiet authority, soft FOMO. Never manipulative, never "used it once" conviction-faking — one bad recommendation costs more than ten good ones earn.

## Whose audience is this
"The Discerning Discoverer": 22–34, ~65% female, UK-first, has taste, buys less-but-better, sceptical of influencer culture, wants to *discover* rather than be sold to. They follow Maruri because she doesn't feel fake, explains WHY, and is never desperate. They share content that makes them look like they have taste. Secondary: "The Aesthetic Guy" (visual-first, skips talky content, buys when triggered). **Explicitly not targeted: AI-curious novelty seekers** — which is exactly why the real-vs-AI play must stay subtle (§10).

---

# 10. THE REAL-VS-AI DEBATE — HOW TO PLAY IT WITHOUT BURNING THE BRAND

The goal: viewers argue in the comments about whether she's real. Done right, this is free engagement on every post. Done wrong, it torches the two moats (trust, and "she doesn't feel fake").

**The rules:**
1. **The debate is a byproduct, never the content.** Realism (§7) creates it. We never post "am I real?" bait, never tease it in captions, never make her origin the topic. The anti-persona doc is explicit: AI-novelty viewers don't monetise and the novelty burns off fast.
2. **Never confirm, never deny, never lie, in comments/DMs.** Vague-but-consistent, deflecting-but-warm, in character. Specificity creates contradiction risk. (A proper comment/DM canon Q&A is still an open build item — until it exists, less is more.)
3. **The ambiguity has a planned expiry.** UGC_Launch_Checklist 3.1 calls for a controlled AI-reveal statement — **still to be drafted, trigger still to be decided** (candidate triggers per the checklist: a follower milestone, or the first public callout with traction). Fuelling the debate accelerates whichever trigger gets chosen — fine, as long as everyone remembers the reveal should happen *on our terms* and the pitch doesn't change: people follow her taste, not her ontology.
4. **Paid work is already disclosed.** The terms sheet warrants to every brand, in writing, that Maruri is AI-generated, and brands may run her ads with platform AI labels. brand-pitch.html says it openly (kept unlisted, not secret). So the organic ambiguity is a *style choice*, not a secret to defend — never lie to protect it.
5. **The character never gets defensive about it.** If a commenter says "this is AI," the in-character energy is the same unbothered warmth as everything else. Being precious about it is the one response that both reads as fake AND feeds the callout.

---

# 11. MAINTAINING THIS SHEET
- New script → assign the next number (currently **014**), add its §6 rotation row when written, confirm the row when QA passes.
- Any material change to a source doc → update the matching section here and bump the version line.
- The §9 exclusivity snapshot and §8 credit balance go stale by design — always check the live log/balance; those lines exist as reminders, not data.

# 12. SUPERSEDED — do not use these older instructions
- `FUTURE_FINDS_MASTER_OVERVIEW.md` camera spec ("no film grain, no colour grading") → superseded by `iPhone_Camera_Spec.md` v3.0 (grain/flatness now deliberate: best-effort in-prompt, guaranteed via ffmpeg).
- The 2-clip hybrid format (Clip 1 hook / Clip 2 reveal, CapCut stitch) and all ElevenLabs voice stages → superseded by single-take seedance_2_0 with native audio. Spec Ad 001/002 docs describe the dead pipeline; only Spec Ad 003's doc reflects the real method.
- `PRODUCTION_PIPELINE_SOP.md` per-video stages that assume ElevenLabs + separate voice pass → the scoring gates and structure beats still apply; the production mechanics don't. Its 1080×1920 export spec applies to the *exported/posted* file (CapCut export upscales the graded 720p master — softness survives, which is the point), not to generation settings.
- "soul_cinema_studio" as the video model → that's the image flow. Video = `seedance_2_0` with the element token in the prompt text.
- Scripts 001–005 prompt language (cinematic, golden hour, push-ins, film-grain-as-style) → never reuse; it's the abandoned cinematic era. Scripts 006–010's "soft British accent" (unpinned) and clean-modern camera block → superseded by the pins and the v3.0 block.
- `CONTENT_SCORING_FRAMEWORK.md` anti-pattern "controversial opinions/hot takes (she's not a commentator)" → amended by Hook Type 7: low-stakes *taste* takes are now allowed under the two Type 7 guardrails; actual commentary/controversy remains banned.
- The coffee-quit timeline ("a year" vs "three months") → unresolved canon conflict; avoid specific durations until the operator picks one.

---

*v1.1 compiled 2026-07-13 from MASTER_CHARACTER_BIBLE.md, Hook_Playbook.md, iPhone_Camera_Spec.md v3.0, Production_Economics.md, FUTURE_FINDS_MASTER_OVERVIEW.md, AUDIENCE_PERSONA_ICP.md, CONTENT_SCORING_FRAMEWORK.md, PRODUCT_SELECTION_FRAMEWORK.md, PRODUCTION_PIPELINE_SOP.md, Usage_Rights_Terms_Sheet.md, UGC_Launch_Checklist.md, Agent_Operating_Procedures.md, rate-card.html, and all scripts 001–013 + spec ads — then adversarially verified against those sources (3-checker pass, 2026-07-13) and corrected. Update whenever a source changes materially.*
