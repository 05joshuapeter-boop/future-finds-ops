# IPHONE CAMERA SPEC — STANDING HIGGSFIELD DIRECTIVE
## Future Finds / Maruri Mori
## Paste into every Higgsfield video prompt
## v2.0 · 2026-07-13 — supersedes the clean-modern-iPhone spec below (kept for reference, no longer the default)

---

## THE BRIEF

All Future Finds videos should look like Maruri filmed herself on an iPhone on a tripod. **Not a production shoot. Not cinematic.** This is intentional — the "real girl, real phone" aesthetic is what builds trust and performs on TikTok.

**Locked 2026-07-13 (operator decision, after a direct A/B test on Script 007):** the standard is now a **2012-era iPhone** (iPhone 4S/5 generation), not a modern one. Lower dynamic range, visible grain/noise, flatter and cooler colour than today's computational photography, softer per-pixel detail, mild rolling-shutter wobble on quick movement, quality reads like compressed 1080p30 rather than crisp modern 4K. The operator's own words: it "makes the clips look more natural and real, and that's exactly what we want" — the period imperfection reads as *more* authentic than a clean modern phone, not less. This inverts most of the old "what to avoid" table below (grain and flatter colour are now correct, not mistakes) — see the updated table.

---

## PASTE THIS BLOCK INTO EVERY HIGGSFIELD PROMPT

```
CAMERA SPEC: Shot on an iPhone from around 2012 (iPhone 4S/5 era), not a modern phone, mounted on a tripod, eye level. Wide angle lens (roughly 26mm equivalent) — no telephoto compression. Visibly lower dynamic range than modern phone video. Noticeably more visible grain and noise, especially in shadow areas. Slightly flatter and cooler colour rendering than today's punchy computational-photography look. Softer per-pixel detail, slightly less sharp than a modern phone. Mild rolling-shutter wobble on quick movement. Quality reads like compressed 1080p30 rather than crisp modern 4K. A touch of motion blur on faster gestures. Subject fills approximately 65% of the frame. Fixed tripod — steady, but framed like a real person set it up themselves, not a professional composition. No added colour grading beyond the period-camera look itself — this is the camera's own limitations, not a stylistic filter on top. Looks exactly like an old phone someone kept around and repurposed as a dedicated tripod camera, not a produced shoot.

LIGHTING: Natural window light only. Soft morning or afternoon daylight coming from one side — no ring light visible, no softboxes, no studio setup. Shadows are gentle and natural. The light, combined with the period camera's own limitations, makes her look real, not polished.

AUDIO: audio quality slightly boxier and more compressed than a modern phone microphone, consistent with the visual period — but the voice itself must stay clearly intelligible.
```

---

## VOICE CONSISTENCY — READ BEFORE EVERY GENERATION

QA on the Week 2 batch caught two clips drifting off Maruri's locked accent. This is a real, recurring risk, not a one-off — the model has some stochastic pull toward accent drift across generations. **Every prompt must explicitly pin the accent, every time, not just rely on the Character Bible being true in general:**

```
She speaks in a consistent soft London English accent throughout — the exact same accent from the first word to the last, never shifting, never drifting toward RP or any other regional accent.
```

Also pin warmth explicitly whenever the delivery could plausibly read as rushed, distracted, or indifferent (any Type 6/Type 7 script where she's mid-task) — a QA pass on Script 007 found the model reading "hurried" as "doesn't care" rather than "hurried but still warm." Add language like:

```
Even though she is [rushing / distracted / mid-task], her energy stays genuinely warm the whole time — not flat, not indifferent, not bored.
```

Give the clip a real listen after generation, not just a visual QA pass — accent drift and flat-affect delivery don't reliably show up in a scene-by-scene transcript summary.

---

## WHAT TO AVOID IN PROMPTS

| Don't say | Why |
|---|---|
| "Cinematic" | Makes it look like a film — loses authenticity |
| "Bokeh" / "shallow depth of field" | Too produced — iPhone portrait mode at most |
| "Studio lighting" | Immediately looks like an ad, not a creator |
| "Slow push in" | Camera should be fixed on tripod — no movement |
| "Modern iPhone" / "iPhone 12/13/14/15/16" | Wrong generation — too sharp, too much dynamic range for the locked 2012-era look |
| Unqualified "colour grade" / "warm lift" | Still over-processes — any colour direction should read as the period camera's own limits, not a stylistic filter |

**No longer avoid (deliberately part of the locked look now):** "film grain," "visible noise," "lower dynamic range," "flatter colour." These were on the old avoid-list when the standard was a clean modern iPhone — they're now correct.

---

## TRIPOD HEIGHT

Always specify: **"tripod at eye level"** — this is the most natural and flattering iPhone self-shoot angle. Slightly above eye level (looking slightly up at her) is acceptable for energy and engagement but use sparingly.

---

## WHEN TO VARY

| Situation | Adjustment |
|---|---|
| Outdoor content | "Natural outdoor daylight, overcast or golden hour" — still no studio |
| Evening / candle video | "Warm practical lamp light from the side — no overhead light. Period-camera low-light look, more visible noise than daylight shots." |
| Travel content | "Handheld iPhone, slight natural movement — like she's holding the phone herself" |

---

## SUPERSEDED — clean-modern-iPhone spec (pre-2026-07-13, kept for reference only)

Used for Scripts 001–010. No longer the default — do not paste this block into new prompts unless the operator explicitly asks for the clean modern look again.

```
CAMERA SPEC: Shot on iPhone on a tripod stand, eye level. Wide angle lens (26mm equivalent) — no telephoto compression. Natural autofocus — no dramatic cinematic depth of field. Subject fills approximately 65% of the frame. Background is slightly soft but not heavily blurred. Fixed tripod — steady, but framed like a real person set it up themselves, not a professional composition. No film grain. No colour grading — iPhone natural processing: clean, true-to-life skin tones, slightly punchy saturation. Looks exactly like a TikTok creator filming a self-recorded video at home.

LIGHTING: Natural window light only. Soft morning or afternoon daylight coming from one side — no ring light visible, no softboxes, no studio setup. Shadows are gentle and natural. The light makes her look real, not polished.
```
