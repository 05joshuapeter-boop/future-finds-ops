# IPHONE CAMERA SPEC — STANDING HIGGSFIELD DIRECTIVE
## Future Finds / Maruri Mori
## Paste into every Higgsfield video prompt, then run every clip through the mandatory grade below
## v3.0 · 2026-07-13 — pivots the vintage look from prompt-only to prompt + mandatory ffmpeg post-process (see "THE PIPELINE, NOW TWO STAGES" below); supersedes v2.0's assumption that the prompt block alone would deliver it

---

## THE BRIEF

All Future Finds videos should look like Maruri filmed herself on an iPhone on a tripod. **Not a production shoot. Not cinematic.** This is intentional — the "real girl, real phone" aesthetic is what builds trust and performs on TikTok.

**Locked 2026-07-13 (operator decision, after a direct A/B test on Script 007):** the standard is now a **2012-era iPhone** (iPhone 4S/5 generation), not a modern one. Lower dynamic range, visible grain/noise, flatter and cooler colour than today's computational photography, softer per-pixel detail, mild rolling-shutter wobble on quick movement, quality reads like compressed 1080p30 rather than crisp modern 4K. The operator's own words: it "makes the clips look more natural and real, and that's exactly what we want" — the period imperfection reads as *more* authentic than a clean modern phone, not less. This inverts most of the old "what to avoid" table below (grain and flatter colour are now correct, not mistakes) — see the updated table.

---

## THE PIPELINE, NOW TWO STAGES (added 2026-07-13)

**Why:** the v2.0 approach (paste the vintage-camera description into the generation prompt and hope the model honours it) was tested on Scripts 011, 012, and 013 — three separate generations, same result each time: the model applies the period-camera language weakly and inconsistently. Frame-level comparison against `before.jpg`/`after_v1.jpg` test renders confirms it plainly — the raw Seedance output stays clean, sharp, high-dynamic-range, and warmly saturated regardless of how strongly the prompt asks for grain and flatness. This is a real, repeatable limitation, not bad luck: a generative video model is free to weight a style instruction against everything else it's balancing (character consistency, lip-sync, dialogue accuracy, motion realism), so there's no way to force pixel-level compliance purely through adjectives, no matter how the prompt is worded.

**The fix:** stop asking the model to do something it won't reliably do, and do it deterministically instead. ffmpeg pixel filters are not probabilistic — the same filter chain produces the exact same grain, contrast, and colour shift on every single clip, every time. So the pipeline is now:

1. **Generation prompt** (the pasteable block below) still matters — it's what actually controls framing, staging, tripod-mounted composition, and "not a produced shoot" behavioural cues, which the model *does* follow reliably. Keep pasting it.
2. **Mandatory ffmpeg grade, run on every clip before it's considered postable** — this is what actually delivers the grain/flatness/cooler-colour/softer-detail look. Not optional, not "nice to have if there's time" — the generation prompt alone will not produce it.

**Verified working command (tested on Script 013, 2026-07-13 — before/after frames confirmed visually, not just by description):**

```
ffmpeg -i "<clip-url-or-file>" \
  -vf "scale=w=trunc(iw*0.55/2)*2:h=trunc(ih*0.55/2)*2:flags=bicubic,scale=w=trunc(iw/0.55/2)*2:h=trunc(ih/0.55/2)*2:flags=bicubic,eq=contrast=0.88:saturation=0.78:brightness=0.02:gamma=0.95,colorbalance=rs=-0.06:gs=0.0:bs=0.09:rm=-0.04:gm=0.0:bm=0.06,noise=alls=18:allf=t+u,gblur=sigma=0.5,vignette=PI/6" \
  -af "highpass=f=120,lowpass=f=8500,acompressor=threshold=-18dB:ratio=3:attack=5:release=50" \
  -c:v libx264 -crf 26 -preset medium -c:a aac -b:a 96k -movflags +faststart \
  "<output>.mp4" -y
```

What each piece does: the double `scale` down-then-up softens per-pixel detail (simulates the lower sensor resolution/sharpness of a 2012 phone) · `eq` flattens contrast and pulls saturation down (lower dynamic range, less punchy colour) · `colorbalance` pushes shadows/midtones cooler and slightly blue (period white-balance) · `noise` adds visible luma grain · `gblur` at a very low sigma softens further without looking smeared · `vignette` adds mild lens falloff · the audio chain narrows the frequency band and adds gentle compression for a boxier, less-modern-mic sound · `-crf 26` (rather than a cleaner low value) adds a touch of real compression artifacting on top.

Use the absolute ffmpeg path from `Production_Economics.md` if `ffmpeg` isn't found on PATH. Reads directly from Higgsfield CDN URLs — no download step needed, same as the other repurposing commands.

**Tuning knobs, if the operator wants it pushed harder or pulled back after watching in motion** (a still frame is a proxy, not the final word — platform re-compression on top of this will also soften it further, which is expected and fine): raise `noise=alls=18` for more visible grain, raise `gblur=sigma=0.5` for more softness, lower `saturation=0.78` for a flatter/more washed-out look, lower `crf 26` toward `22` to reduce compression artifacting if it starts looking degraded rather than vintage.

**Not simulated by this pass:** rolling-shutter wobble on fast motion — that's a geometry/timing artifact, not a pixel filter, and would need per-frame warping to fake convincingly. Left out as not worth the complexity; the grain/flatness/softness combination is doing most of the perceptual work anyway.

**Cost: zero Higgsfield credits.** This is a local, free, deterministic post-process — it can be applied to already-generated clips (011, 012, 013, and any earlier Week 2 clips) without spending anything, unlike a regeneration.

---

## PASTE THIS BLOCK INTO EVERY HIGGSFIELD PROMPT

Still worth including even though it no longer has to carry the whole vintage look on its own — it's the part of this spec that reliably controls framing and behaviour (tripod composition, "not a produced shoot," casual imperfect framing). Treat its grain/dynamic-range/colour language as best-effort flavour the model may or may not fully apply; the ffmpeg pass above is what actually guarantees it.

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
