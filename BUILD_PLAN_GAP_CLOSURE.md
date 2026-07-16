# BUILD PLAN — GAP CLOSURE
## Future Finds / Maruri · aligning the project with the proven AI-creator playbook
## v1.0 · 2026-07-16 · authored by Fable (strategy pass) for Sonnet (execution)
## Read first: MARURI_GENERATION_MASTER_REFERENCE.md governs ALL generation. This doc governs WHAT to build and in what order.

---

## 0. WHY THIS PLAN EXISTS (context for the executing agent)

Benchmarked against the creators who actually pulled this off (Aitana López / The Clueless,
Lil Miquela, Kenza Layli, the AI-UGC studio economy), the project's **craft is ahead of the
field but its strategy had two inversions**:

1. **Revenue inversion** — we led with audience-side affiliate (slowest line, 6–12 months to
   meaningful money at current size) and gated the B2B/UGC studio line (fastest, follower-
   independent, 30–60 days to first money) behind "someday."
2. **Content inversion** — ~70% product/catalog content, when winners run ~70% "her life."
   The proven rule (The Clueless, verbatim): **"people follow lives, not images."**

Plus the biggest unused asset: **stills.** Aitana's following was built on photos; video was
the garnish. We have a Soul ID and have generated zero photo content. Stills are ~5–10x
cheaper per post than our 35-credit videos and are the format AI renders most reliably.

Sequencing principle for everything below: **the audience is the portfolio; brands are the
customer; stills are the growth engine; video is the premium format.**

---

## PHASE 0 — PRODUCTION KEYSTONE (this weekend · already user-approved · prerequisite for all)

Status of decisions already locked with the user — do not re-litigate:
hybrid audio (auto-baked royalty-free bed default, ~15–20 credits approved for 4 custom
Higgsfield beds) · auto-burned ASS captions (styles need user approval, see 0.3) · Drive as
the storage hub (Raw Videos folder `10E_kIactL4KtPBjWbva44nBe6x0nkwB4`, Published Videos
folder `1zLh8JGa64TyUo9iLQFoYRbSu1sNjF7Sr`) · local disk kept clean · quarterly xlsx tracker
maintained locally, uploaded to Drive, user deletes old copy.

- [ ] **0.1 Music beds.** Generate 4 subtle on-brand beds (lo-fi/ambient, no melody hooks that
      fight speech) via Higgsfield audio. User approves vibe once. Store in Drive + local ref.
- [ ] **0.2 Finishing pass v1.** One scripted ffmpeg pipeline: 2012 grade → bed ducked under
      voice (sidechain, bed ≈ −22dB under speech) → burned captions → export. Prove on 015.
- [ ] **0.3 Caption styles.** Mock 2–3 ASS styles on the same clip (soft-premium, not
      MrBeast-loud; brand fonts/colours per Design Philosophy). User picks one → lock in the
      master reference sheet as §7e.
- [ ] **0.4 Drive wiring.** Raw → `Raw Videos`, final → `Published Videos`, verify first video
      upload integrity (download + play back before trusting the pipe). Wipe local temp after.
- [ ] **0.5 Tracker v2.** Build Q3-2026 xlsx: Content Type (Affiliate/Engagement/Story-Still) ·
      Clip ID · Topic/Product · Amazon Link · Caption · Drive Link · Platforms · Scheduled ·
      Status · Notes. Upload to Drive tracker folder (`19yvKnrN8J0PYoFstXaYPumIICZp0svYE`).
- [ ] **0.6 QA log.** `QA_LOG.md` — one row per generation: job id, verdict, failure reason,
      rule extracted (if any) → feeds master sheet. This closes the silent-approve/reject gap.
- [ ] **0.7 Batch 2–3 weeks of content** through the new pipeline (mix per Phase 1 ratios
      below, not the old 70% product mix) and record credit burn → validates runway math.

**DoD:** one command takes a raw clip → posted-ready file in Drive; tracker + QA log live;
user schedules a full week on Buffer in one sitting.

---

## PHASE 1 — GROWTH ENGINE REBUILD (weeks 1–2)

### 1.1 Stills engine (highest-leverage new build)
- Soul ID (`e047f76e-91cb-44df-8492-15ec1d47e09a`) photo pipeline for: candid lifestyle
  stills (coffee run, tube, desk, golden-hour walk), Story frames (polls, this-or-that,
  morning window shot), and product-in-life stills (product incidental, never hero — §7d
  rules apply to stills too).
- Establish cost-per-still, a light realism grade for photos (grain + slight softness — a
  2012-era *photo* look consistent with the video canon), and 3 reusable shot templates.
- Wardrobe/location continuity: pull from the master sheet §6 rotation so stills and videos
  read as the same life.
- **Charming/aspirational, never thirst-trap** (user's explicit guardrail — cute is fine,
  bait poisons the brand and the UGC credibility).
- **DoD:** 10 approved stills banked; cost table written into Production_Economics.md.

### 1.2 Life calendar (the narrative machine)
- New doc `LIFE_CALENDAR.md`: a rolling 4-week episodic plan of small story beats consistent
  with the Bible — mum arc (post-016 "team mum" is already live canon), work-in-design
  beats, the flat, London seasonal moments. Each beat tagged with format (video/still/story).
- **Target mix: ~70% life/engagement (hot takes, candids, stories, lore beats) / ~30%
  product.** 5 feed posts + 3–5 stories per week. Hard rule kept: never two hot-takes
  back-to-back.
- **DoD:** 4 weeks of beats written; tracker rows created; next batch generated FROM this
  calendar, not ad-hoc.

### 1.3 Community ops (closes the open item)
- `COMMENT_CANON.md`: reply playbook for the recurring comment types (agree / disagree /
  "is this AI?" — never confirm, never deny, deflect warmly / "where's that from?" /
  compliments / creeps). Plus per-post: 1 pre-written pinned first comment + 2–3 seeded
  replies, delivered alongside every caption in the tracker.
- Outward engagement routine (10 min/day, phone): Maruri hearts/replies in-niche on adjacent
  UK lifestyle accounts. Human-executed; agent pre-writes nothing here beyond tone rules.
- **DoD:** doc exists, first week's pinned comments written, user has the phone routine.

### 1.4 Distribution expansion (free reach)
- YouTube Shorts channel (same handle) added to the Buffer cross-post so every 9:16 goes to
  a third algorithm. Pinterest board for product stills (high purchase intent) — batch,
  low-effort.
- **DoD:** both live; posting flow unchanged for the user (Buffer does the work).

### 1.5 Measurement loop
- `PERFORMANCE_LOG.md`: baseline row = IG 21 followers / 7 posts (2026-07-15, pre-hot-takes).
  Weekly Chrome-assisted readout (user logged in; read-only) → log → one steering decision
  per week ("double down on X, drop Y"). This is the routine the user approved as a weekly
  Claude task.
- **DoD:** log exists with baseline; first weekly readout scheduled for the weekly session.

### 1.6 Doc reconciliation + compliance sweep (do early — Sonnet must not build from stale canon)
- FUTURE_FINDS_MASTER_OVERVIEW.md: **delete/replace the "audience does not need to know she
  is AI" claim** (user has disclosed on both platforms — that is now brand canon and legally
  smart); replace the stale 2-clip/CapCut/ElevenLabs format spec with the current
  single-take native-audio Seedance + finishing-pass reality; correct age drift anywhere it
  survives ("28-year-old" → mid-20s).
- ASA presenter-rule pass over affiliate script templates: shift personal-testimony framing
  ("I use this every day", "changed my life") → curator/presenter framing ("this is
  beautifully made", "38K reviews and the mechanism is clever"). Applies to future scripts;
  do not retro-edit already-posted content.
- **DoD:** grep for the stale claims returns nothing; Hook_Playbook gains a short "claims
  framing" subsection; changes pushed to future-finds-ops repo.

---

## PHASE 2 — UGC STUDIO ACTIVATION (weeks 3–6 · pulled forward from "someday")

Gate: Phase 0 proven (pipeline reliably produces finished video in <48h wall-clock).
Full detail lives in `UGC_Studio_Playbook.md` — this is the execution order:

- [ ] **2.1** Three mock SaaS ads through the new pipeline (pain-point / curiosity / listicle
      hooks; brand-supplied-style screen recordings as B-roll — no fake physical products).
      These double as the pipeline stress test and the portfolio.
- [ ] **2.2** Reframe `brand-pitch.html` → "Future Finds Media: Performance UGC Studio"
      (lead with performance; disclose the AI plainly; keep Maruri's consumer identity
      untouched everywhere else).
- [ ] **2.3** Contract template with the two non-negotiable clauses (disclosure
      indemnification; no-training/likeness protection). Deliver finished MP4s only.
- [ ] **2.4** Prospecting: Meta Ad Library + TikTok Creative Center fatigue-scrape (same
      creative ≥3 weeks = warm lead). Build a 50-lead list, UK SaaS/apps/digital-first.
- [ ] **2.5** Outreach engine: 10 personalised sends/day (email + LinkedIn), free 3-hook
      sample offer, £150 hook-test bundle → £400/mo retainer ladder. Verify Ramdam's actual
      AI-creator policy before investing in any marketplace.
- **Target: first paid deal by day 60 of this plan.**

---

## PHASE 3 — FLYWHEEL (ongoing, from week 4)

- [ ] **3.1 Paid seed test:** £50–100 boost on the single best-performing organic post
      (decided from PERFORMANCE_LOG, not vibes). Measure follower-per-£. Repeat only if
      CAC is sane. (Pattern-matched to the e.l.f. Spark Ads case, 3.1x ROAS.)
- [ ] **3.2 Milestone unlocks:** at ~1K followers → apply Amazon Influencer Program
      (storefront + onsite commissions = the real affiliate prize). At 5K → re-evaluate
      TikTok Shop honestly (identity verification is a likely hard blocker for an AI
      creator — investigate, don't assume).
- [ ] **3.3 Monthly strategy review:** metrics vs. this plan; kill or double each content
      family; credit-runway check (balance was 3,533.8 on 2026-07-15; stills strategy
      should stretch it 5–10x per post vs. video-only).

---

## GUARDRAILS FOR THE EXECUTING AGENT (Sonnet — these are binding)

1. **Generation canon:** MARURI_GENERATION_MASTER_REFERENCE.md v1.1+ governs every prompt —
   2012-era camera, §7d anti-AI-tell rules (deep focus / no hero staging / no live food
   manipulation), tone §4 (WITH-not-AT), voice pins, 720p/fast/35-credit organic settings.
2. **Credit discipline:** 1 regen max then stop and change the prompt language, not the dice;
   judge the GRADED clip; best-of-2 for hard clips; log every spend in QA_LOG.
3. **Approvals that stay human:** the user approves scripts, still styles, caption style,
   bed vibe, all outreach sends, any paid spend, and anything posted. Buffer clicks are the
   user's. Comment replies are the user's (agent pre-writes, never sends).
4. **Never:** log into user accounts · confirm/deny AI status in Maruri's voice in comments ·
   personal-testimony claims in scripts (ASA presenter rule) · thirst-trap content · sell a
   turnaround the pipeline hasn't demonstrated · send raw files/voice params/character
   parameters to anyone.
5. **Two revenue lines, one factory:** organic/affiliate (slow compounding) and UGC studio
   (fast B2B) share the same production system. When they conflict for resources, the studio
   line wins until first revenue, then rebalance.

---

## SOURCES (strategy benchmarks)
- Aitana López / The Clueless: Euronews, Forbes, Entrepreneur, Fast Company (350K followers,
  €3K avg/€10K peak monthly; "people follow lives, not images"; lore-first; team-run)
- Kenza Layli × Hyundai via Pixel.ai: 20x ROI campaign (MediaCat/impact.com trend reports)
- e.l.f. TikTok Shop program: micro-creators + Spark Ads whitelisting, 3.1x ROAS (iqfluence)
- AI-UGC creator economics 2026: $50–150/video entry → $300–500 mid → retainers (Tomoson,
  Hyperbeam, Toptal Creator)
- TikTok affiliate CTR ~5.2% vs <2% IG link-in-bio (Outfy/Sprout Social)
