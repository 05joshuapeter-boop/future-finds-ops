# MUSIC BEDS — candidate library
## v1.0 · 2026-07-16 · Phase 0.1 of BUILD_PLAN_GAP_CLOSURE.md

## Source & license
Kevin MacLeod / incompetech.com, mirrored on the Internet Archive (`archive.org/details/Incompetech`).
**License: Creative Commons Attribution 4.0 (CC BY 4.0)** — free for commercial use, attribution
required. Standard attribution line (use in video descriptions / credits where the platform
allows, e.g. YouTube Shorts description):

> Music: "[Track Name]" by Kevin MacLeod (incompetech.com), licensed under CC BY 4.0
> https://creativecommons.org/licenses/by/4.0/

(TikTok/IG captions don't need this — attribution lives in the one place per track that's
practical, e.g. a pinned "credits" highlight or the YouTube Shorts description. Not a per-post
requirement.)

Rejected earlier: Higgsfield's `sonilo_music` model — its own tool documentation states it
exists only for the game-generation pipeline and must not be used for standalone audio. User
chose free libraries instead (2026-07-16).

## Candidates (pick 4 — needs a human listen, text QA can't judge music)

| Track | Length | Direct listen/download (browser-playable) | Read as |
|---|---|---|---|
| Ambiment | 22:53 | https://archive.org/download/Incompetech/mp3-royaltyfree/Ambiment.mp3 | long ambient loop bed, very neutral |
| At Rest | 3:27 | https://archive.org/download/Incompetech/mp3-royaltyfree/At%20Rest.mp3 | calm, minimal |
| Airport Lounge | 5:08 | https://archive.org/download/Incompetech/mp3-royaltyfree/Airport%20Lounge.mp3 | lounge/jazz-leaning, more character |
| Avec Soin | 2:25 | https://archive.org/download/Incompetech/mp3-royaltyfree/Avec%20Soin.mp3 | delicate, likely piano ("with care") |
| Bathed in the Light | 2:46 | https://archive.org/download/Incompetech/mp3-royaltyfree/Bathed%20in%20the%20Light.mp3 | warm, gentle |

Picked by title/genre-filter + reputation, not by ear — same as the video listen-flags pattern
used all session (e.g. 016's "mum/mom"). **User needs to click through and pick 4** (or swap any
out for a different Incompetech/library track). Each track is long enough to be trimmed to a
rotating ~10-20s excerpt per clip in the finishing pass, so final duration isn't a constraint.

## Decision — 2026-07-16
None of the 5 original candidates were good enough for the hot-take/engagement content
("Airport Lounge was good but not good enough"). A second, larger batch was sourced from a
Kevin MacLeod lounge-themed album (Radio Martini variants, Cool Vibes, Chill, Easy Lemon) — see
below. Verdict: **mood-match the bed to content type, not one bed for everything.**

- **Easy Lemon** → **LOCKED** for slow lifestyle / "morning routine" / "what I did today"
  third-person reflective content.
- **Hot takes (015-style):** none of the library candidates were distinctive enough. Moving to
  a **custom ElevenLabs-generated track**, described ("inspired by") from reference songs the
  user supplies — not a direct library pick. Pending: reference songs + cost approval (separate
  ElevenLabs balance).

## Second batch (Kevin MacLeod, "Radio Martini" lounge album — archive.org/details/kevin-mac-leod-radio-martini)
| Track | Listen | Verdict |
|---|---|---|
| Easy Lemon | https://archive.org/download/kevin-mac-leod-radio-martini/Kevin%20MacLeod%20-%20Easy%20Lemon.mp3 | **Locked — slow/routine content** |
| Radio Martini | https://archive.org/download/kevin-mac-leod-radio-martini/Kevin%20MacLeod%20-%20Radio%20Martini.mp3 | Rejected (not distinctive enough for hot takes) |
| Radio Martini (Slow) | https://archive.org/download/kevin-mac-leod-radio-martini/Kevin%20MacLeod%20-%20Radio%20Martini%20%28Slow%29.mp3 | Rejected |
| Radio Martini (Fast) | https://archive.org/download/kevin-mac-leod-radio-martini/Kevin%20MacLeod%20-%20Radio%20Martini%20%28Fast%29.mp3 | Rejected |
| Cool Vibes | https://archive.org/download/kevin-mac-leod-radio-martini/Kevin%20MacLeod%20-%20Cool%20Vibes.mp3 | Rejected |
| Chill | https://archive.org/download/kevin-mac-leod-radio-martini/Kevin%20MacLeod%20-%20Chill.mp3 | Rejected |

Same CC BY 4.0 license/attribution rule as the first batch (§ above).

## Pipeline default (superseded by the decision above — kept for history)
"At Rest" was used as a placeholder bed to build/prove the automated finishing pass (Phase 0.2)
before any bed was actually chosen. The pipeline takes the bed file as a parameter, so this
required zero pipeline rework to swap out.

## Storage
Per the "keep the PC clean, Drive is canonical" rule: these source tracks are NOT duplicated into
permanent local or Drive storage. The Internet Archive URLs above are stable and used as the
pull source each time a bed is needed for a render. Only the FINISHED graded/captioned video
(bed baked in) gets uploaded to Drive's `Published Videos` folder, per the existing video
pipeline pattern.
