# PRODUCTION ECONOMICS — HIGGSFIELD CREDIT DISCIPLINE
## Locked 2026-07-12 — operator directive: minimum point usage, maximum output

---

## Why this exists

No UGC deal or affiliate income has landed yet. Higgsfield credits are a depleting
balance (Ultra plan, checked 2026-07-12: **3,918.8 credits remaining**), not free —
every clip generated is real spend against a runway that has to last until revenue
starts. This doc is the standing constraint on all future generation work: **default
to the cheapest settings that still work, and get more than one piece of content out
of every clip that does get generated.**

## What a generation actually costs (confirmed via `get_cost`, 2026-07-12)

`seedance_2_0`, 9:16, native audio on — cost scales with duration/resolution/mode:

| Duration | Resolution | Mode | Credits | vs. baseline |
|---|---|---|---|---|
| 15s | 1080p | std | **135** | baseline (what every clip this session used) |
| 10s | 1080p | std | 90 | −33% |
| 15s | 720p | fast | 52.5 | −61% |
| **10s** | **720p** | **fast** | **35** | **−74%** |

Everything else is nearly free by comparison — `video_analysis` QA checks cost
~0.1–0.4 credits each (confirmed from real transaction history), product-image
imports and manual product creation cost nothing. **The only thing worth economizing
is the Seedance generation call itself.**

## New default generation settings

Unless a script genuinely needs more runtime or a client deliverable specifically
requires 1080p, generate at **10s / 720p / fast mode** going forward, not the
15s/1080p/std used for the first Week 2 batch. Rationale, not just cost:

- TikTok/Reels/Shorts re-compress everything on upload anyway — 1080p buys nothing
  the viewer can perceive on a phone screen.
- "Fast" mode's slightly less polished render arguably reads *more* authentically
  "shot on a real iPhone" than std mode's cleaner output, which fits this pipeline's
  whole aesthetic thesis better, not worse.
- Every script produced so far actually delivers its full line in 10–12s once the
  camera-fumble beats are trimmed slightly — 15s was headroom that wasn't being used.

At 35 credits/clip instead of 135, the same 3,918.8 credit balance stretches to
~112 generations instead of ~29. That gap is the entire point of this change.

## Reduce the redo rate (the other real cost driver)

Two of the five Week 2 clips needed a full redo (270 extra credits, on top of the
270 those two clips already cost) — one for a product-reveal gesture violation, one
for unwanted background music the model added despite an explicit "no music"
instruction. Both are now fixed in the locked prompt language (see
`Hook_Playbook.md` and the generation prompts in `SCRIPTS/`) — **reuse that stronger
phrasing verbatim in every future script**, don't relax it back to the softer
original wording. A redo costs as much as the original — avoiding it is the single
biggest lever after the resolution/mode change above.

## Repurposing: turn one paid generation into multiple posts

There is no ready-made MCP connector for video editing/repurposing (checked the MCP
registry, 2026-07-12 — nothing available). The right tool is **local ffmpeg**
(free, one-time install, zero marginal cost per use — installed on this machine
2026-07-12). Every generated master clip should be cut into as many pieces of
content as the footage actually supports before moving on to the next generation:

1. **Post the full clip as-is** — the primary post, per the content schedule.
2. **Cut a shorter teaser/hook-only clip** (first 3–5s, the fumble/interruption beat)
   as a second, separate post later in the week — the hook alone often works as a
   standalone piece, and reposting the same beat with a different caption reads as
   new content, not a repeat.
3. **Extract a still frame** (via `ffmpeg -ss <t> -frames:v 1`) for a feed/carousel
   post or a Stories frame — zero additional generation cost.
4. **Re-caption and repost** the same master clip weeks later once it's cycled out
   of the algorithm's short memory window, with a different on-screen caption/hook
   text burned in via `ffmpeg drawtext` — different enough to not read as a duplicate,
   free to produce.

None of this requires touching Higgsfield again. Budget mentally for **1 generation
→ up to 3–4 pieces of actual posted content**, not 1:1.

**Verified working 2026-07-12** — ffmpeg reads directly from Higgsfield's CDN URLs,
no download step needed. Install path on this machine (winget doesn't always land
on PATH inside this tool's shell — use the absolute path if `ffmpeg` isn't found):
`C:\Users\tensi\AppData\Local\Microsoft\WinGet\Packages\Gyan.FFmpeg_Microsoft.Winget.Source_8wekyb3d8bbwe\ffmpeg-8.1.2-full_build\bin\ffmpeg.exe`

Still-frame extraction (this ffmpeg build needs `-update 1` for single-image output,
older guides online omit it and will error):
```
ffmpeg -ss <seconds> -i "<clip-url>" -frames:v 1 -update 1 -q:v 2 "out.jpg" -y
```

Teaser cut (first N seconds, re-encoded so it's a clean standalone file):
```
ffmpeg -i "<clip-url>" -t <seconds> -c:v libx264 -c:a aac "teaser.mp4" -y
```

## Practical budget going forward

At 35 credits/clip: a 5-clip week (matching the current posting cadence) costs
175 credits, not the 945 this week actually cost. That's roughly **22 weeks of
runway** at the current balance if the new default settings and lower redo rate
both hold — call it a hard ceiling to watch, not a target to spend down to.

*Production Economics · v1.0 · 2026-07-12*
