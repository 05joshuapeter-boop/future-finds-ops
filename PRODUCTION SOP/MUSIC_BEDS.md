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

## Working default for pipeline development
**"At Rest"** is being used as the placeholder bed while building/proving the automated
finishing pass (Phase 0.2) — this does NOT lock it in as a final choice. The pipeline takes the
bed file as a parameter, so swapping the final 4 in later requires zero pipeline rework.

## Storage
Per the "keep the PC clean, Drive is canonical" rule: these source tracks are NOT duplicated into
permanent local or Drive storage. The Internet Archive URLs above are stable and used as the
pull source each time a bed is needed for a render. Only the FINISHED graded/captioned video
(bed baked in) gets uploaded to Drive's `Published Videos` folder, per the existing video
pipeline pattern.
