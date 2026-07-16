# FUTURE FINDS — MASTER PROJECT OVERVIEW
## AI Influencer Business · Complete Reference Document
## Version 1.0 · July 2026

---

# 1. THE CONCEPT

Future Finds is a fully AI-generated influencer business. The face of the brand is **Maruri Mori** — a fictitious AI influencer who recommends products she "discovers" through her curated lifestyle. She is generated entirely using AI tools: her face and body via Higgsfield, her voice via ElevenLabs, her scripts via Claude.

The business model is affiliate marketing — primarily Amazon Associates UK, with TikTok Shop as the high-priority secondary channel. Content is distributed on TikTok and Instagram, cross-posted simultaneously via Buffer, and monetised through tracked affiliate links in bio.

**The core insight:** The audience responds to her personality, her taste, and the quality of her recommendations — not her origin. The moat is trust, not novelty. **(Updated 2026-07-16 — superseded the original "the audience does not need to know she is AI" framing.** Maruri is now openly disclosed as an AI creator at the profile level on both TikTok and Instagram, with per-post AI-creator labels on Instagram. Disclosure and the trust-through-personality thesis are not in tension — see `MARURI_GENERATION_MASTER_REFERENCE.md` §10 and `UGC_Studio_Playbook.md` §1 for the reasoning: transparently-AI creators with deep lore build real followings; hiding it was never load-bearing for the strategy.)

---

# 2. THE BRAND

## 2.1 Brand Identity

| Field | Value |
|---|---|
| **Brand Name** | Future Finds |
| **Handles** | @futurefindsmedia (TikTok + Instagram) |
| **Tagline** | *Things worth finding.* |
| **Design Philosophy** | Void Signal — minimal, geometric, precision-tooled. Darkness as preparation, spectrum gradient as direction. |
| **Colour Language** | Deep black, cool-to-warm spectrum gradient (logic → humanity), clean white negative space |
| **Typography** | Two typefaces max — authority weight + refinement weight. Thin, open-spaced. |
| **Logo** | Geometric mark + wordmark. Scalable across all surfaces. |
| **Brand Voice** | Warm but not effusive. Specific but not clinical. Always sounds like a person. |

## 2.2 Brand Promise

> *Future Finds helps people discover products genuinely worth their attention, their money, and their time.*

Every piece of content is measured against: **"Would a smart, taste-conscious mid-20s Londoner actually care about this?"** (age corrected 2026-07-16 to match the locked character age — Maruri is mid-20s, not late-20s; see `MASTER_CHARACTER_BIBLE.md`.)

---

# 3. THE CHARACTER — MARURI MORI

## 3.1 Identity

| Field | Value |
|---|---|
| **Full Name** | Maruri Mori (Mah-roo-ree Mo-ree) |
| **Heritage** | Japanese father / Thai mother |
| **Born** | London, England |
| **Lives** | Westminster, London |
| **Age** | Mid-20s |
| **Career** | Product Designer at a tech company |
| **Archetype** | Soft-Spoken High-Value Woman |

## 3.2 Appearance

- **Face:** Soft, delicate East/Southeast Asian features — high cheekbones, warm expressive eyes, approachable elegance
- **Skin:** Clear, luminous, light to medium tone — reflects Japanese/Thai heritage
- **Hair:** Dark brown to black, straight or softly wavy. Default: down or relaxed half-up. Never over-styled.
- **Style:** "Off-duty tech designer" — neutrals, soft tones, quality fabrics, no loud branding. Clean and understated.
- **Never:** oversexualised, overly trendy, heavily branded

## 3.3 Personality

**Always on:** Calm, emotionally mature, observant, thoughtful, soft-spoken, warm, intelligent, grounded

**Revealed over time:** Playful, dry wit, teasing, subtly funny, genuinely cute in small moments

**She is NOT:** bubbly, loud, girlboss, preachy, self-deprecating for relatability, trend-reactive

## 3.4 Voice

- Soft British accent — London raised
- Medium-low pitch, deliberate tempo, warm texture
- Natural fillers used intentionally: *okay…*, *hmm…*, *wait…*, *honestly…*, *so…*
- Pauses before key moments. Warmth through tone, not volume.
- **(Updated 2026-07-16 — the ElevenLabs settings line above is stale and removed.** Voice is
  now generated as Seedance 2.0's native in-video audio, not a separate ElevenLabs TTS pass —
  see the Higgsfield Generation Spec below and `MARURI_GENERATION_MASTER_REFERENCE.md` §5 for
  the current voice pins: accent consistency, warmth, and the anti-music rule.)

## 3.5 Lore & Backstory

Maruri grew up in London, raised in a household where things were chosen with care. Her Japanese father gave her less-is-more sensibility. Her Thai mother gave her warmth and the belief that beauty should invite, not intimidate. She studied design in London, now works at a mid-size tech company. She started posting because she was tired of hollow recommendations from people who didn't use what they promoted.

**Hidden motivation:** prove that trust is more valuable than reach.

## 3.6 Higgsfield Generation Spec

**SUPERSEDED 2026-07-16 — this section described the original (abandoned) pipeline. The
current, authoritative generation spec lives in `MARURI_GENERATION_MASTER_REFERENCE.md`
(governs every prompt) and `iPhone_Camera_Spec.md` (camera/grade detail). Summary of what
actually changed, kept here only as a historical pointer:**

- **Model:** `seedance_2_0` (not `soul_cinema_studio`) — character consistency comes from a
  reference-element token embedded in the prompt, not the Soul ID (Soul ID is used for the
  separate image/photo pipeline only).
- **Camera spec:** locked to a 2012-era iPhone 4S/5 look (visible grain, lower dynamic range,
  flatter colour, no modern computational-photography sharpness) — the opposite of "natural
  iPhone processing, no film grain." A mandatory ffmpeg grade pass applies this deterministically
  after generation. See master sheet §7.
- **Format:** single continuous take, 10s, 720p, fast mode (35 credits) — not a 2-clip
  hook/reveal hybrid stitched in CapCut. No CapCut in the current pipeline; captions and music
  are burned in via an automated ffmpeg finishing pass (see `BUILD_PLAN_GAP_CLOSURE.md` Phase 0).
- **Target runtime:** 10 seconds (not 20–24).

---

# 4. THE AUDIENCE

## 4.1 Primary Persona — "The Discerning Discoverer"

| Field | Value |
|---|---|
| **Age** | 22–34 |
| **Gender** | ~65% Female / 35% Male |
| **Location** | UK primary, US/AU/CA secondary |
| **Income** | Entry-professional to mid-career — disposable income, selective spenders |
| **Mindset** | Quality over quantity. Aspires to a curated life. Slightly sceptical of influencers — but follows the rare ones they trust. |
| **Platform behaviour** | TikTok: discovery via FYP. Instagram: warmer, more intentional. |
| **Purchase sweet spot** | £15–£80 / $20–$100 |

**Why they follow Maruri:** She doesn't feel fake despite being polished. She explains *why* things are good. Her taste matches theirs. She feels like a stylish friend who researches things. She's never desperate for their attention.

## 4.2 Anti-Persona (Do Not Target)

Deal hunters, trend maximalists, 45+ demographics, AI-novelty chasers, pure entertainment seekers.

---

# 5. THE BUSINESS MODEL

## 5.1 Revenue Architecture

| Channel | Status | Details |
|---|---|---|
| **Amazon Associates UK** | ✅ LIVE | Store ID: `futurefindsmedia`. 180-day clock to 3 qualifying sales. Commission avg 4%, ranges 1–10%. |
| **TikTok Shop** | 🔄 Pending | Business account under review. Cannot confirm clickable link is live yet. |
| **Impact / ShareASale brands** | ⬜ Future | 8–25% commission, requires application |
| **LTK (LikeToKnowIt)** | ⬜ Future | Strong for lifestyle/fashion |
| **PartnerStack SaaS** | ⬜ Future Phase | 20–40% commission, software/app recommendations |
| **Brand sponsorships** | ⬜ Future | Direct brand deals once following established |

## 5.2 Affiliate Program Priority Stack

1. **TikTok Shop** (5–20%) — highest priority, lowest friction, in-app purchase
2. **Amazon Associates** (1–10%) — widest selection, easiest setup, already live
3. **Impact/ShareASale** (8–25%) — higher yield, requires application
4. **LTK** — lifestyle discovery plays
5. **PartnerStack** — Phase 2, software angle

## 5.3 Product Selection Criteria

**Gate system — product fails on ANY of these:**
- G1: Amazon rating ≥ 4.2 stars, min 150 reviews
- G2: In stock, ships Prime
- G3: Under £200 / $250
- G4: Tech, lifestyle, home, wellness, aesthetic goods
- G5: No brand controversy or questionable sourcing
- G6: Photographs well, visually interesting on camera

**Scoring (5 dimensions, 50 max):**
- D1 Usefulness (0–10)
- D2 Wow Factor / Shareability (0–10)
- D3 Viral Potential (0–10)
- D4 Trust Score (0–10)
- D5 Monetization Potential (0–10)

**Thresholds:** 42–50 = Priority. 35–41 = Strong. Below 35 = defer or reject.

---

# 6. CONTENT STRATEGY

## 6.1 Content Pillars (Locked)

| Pillar | Weight | Purpose |
|---|---|---|
| **Product Discovery** | 40% | Monetisation — affiliate revenue |
| **Viral Lifestyle** | 40% | Growth — reach, shares, new followers |
| **Personal / Lore** | 20% | Trust — emotional depth, retention |

## 6.2 The Hook Formula — "The Maruri Formula"

Every video hook follows this structure:

```
PERSONAL CONFESSION → CURIOSITY GAP → CLIFFHANGER
```

She never opens with the product. She opens with herself — a fact, behaviour, or feeling. Then withholds. Then cliffhangers into Clip 2.

**Proven examples:**
- Script 004: "I've been completely caffeine free for three months. And I feel fine — like, genuinely fine. How??"
- Script 003: "People always ask me what my flat smells like. It's one thing. That's it. I'll show you."

## 6.3 Hook Type Rankings (from OpusClip, 1.95M clips)

| Rank | Hook Type | Volume | Verdict |
|------|-----------|--------|---------|
| 1 | Direct Address / Question / Intrigue | 952,227 | ✅ Core weapon |
| 2 | Shock / Surprise | 618,469 | ✅ Proven |
| 3 | Story / Anecdote Teaser | 145,309 | ✅ Core weapon |
| 4 | Problem / Solution Setup | 108,866 | ✅ Use sparingly |
| 6 | Product / Service Introduction | 23,163 | ❌ Never open with product |

**The 1.7-second rule:** Everything in the first line must count. The window closes before 2 seconds on mobile.

## 6.4 Posting Cadence

| Phase | TikTok | Instagram |
|---|---|---|
| **Launch (Week 1)** | 1/day for 7 days | 1 Reel every 2 days |
| **Steady State** | 4–5/week | 3 Reels/week + Stories 5x/week |

**Optimal posting times (UK):** 7–9am BST / 12–2pm BST / 7–9pm BST

**Current schedule:** All videos via Buffer at **8:00am BST**, cross-posting TikTok + Instagram simultaneously.

---

# 7. THE PRODUCTION STACK

## 7.1 Tools

**SUPERSEDED 2026-07-16 — updated to the current stack. ElevenLabs and CapCut are no longer
part of the pipeline (voice is native to the Seedance generation; grading/music/captions are
one automated ffmpeg pass — see `BUILD_PLAN_GAP_CLOSURE.md` Phase 0).**

| Tool | Role | Notes |
|---|---|---|
| **Higgsfield** | AI video generation — Maruri's visual performance + native voice | Model: `seedance_2_0`, character consistency via reference-element token (not Soul ID — Soul ID is the separate photo pipeline). 9:16, 10s, 720p, fast (35 credits). |
| **Claude** | Script writing, production direction, strategy, automated finishing pass | This session |
| **ffmpeg (automated finishing pass)** | 2012-era grade + royalty-free music bed (ducked under voice) + burned captions, all in one script | Replaces ElevenLabs + CapCut entirely |
| **Buffer** | Social scheduling — cross-posts TikTok + Instagram | 8am BST daily |
| **Amazon Associates** | Affiliate link generation via SiteStripe | Store ID: `futurefindsmedia` |

## 7.2 Production Pipeline (Per Video)

```
RESEARCH → SCORING → SCRIPT → VIDEO (Higgsfield, native audio, single take) → FINISHING PASS
(ffmpeg: grade + bed + captions) → SCHEDULE (Buffer) → ANALYSE
```

**Weekly time budget:** to be re-measured under the new pipeline (the old 10–18h estimate
assumed manual CapCut editing per video, which no longer exists in the workflow).

## 7.3 iPhone Camera Spec (ALL Higgsfield Prompts)

**SUPERSEDED 2026-07-16 — this was the pre-realism-fix spec and is now the OPPOSITE of current
policy.** "No film grain, natural iPhone processing" was found to read as too clean/modern —
exactly the "looks AI generated" failure mode. Current spec locks to a 2012-era iPhone 4S/5
look instead (visible grain, lower dynamic range, flatter colour), reinforced by a mandatory
ffmpeg grade pass. Full current spec lives in `iPhone_Camera_Spec.md` and
`MARURI_GENERATION_MASTER_REFERENCE.md` §7 — do not use the quote below.

~~*Shot on iPhone on a tripod stand at eye level. Wide angle lens (26mm equivalent), natural autofocus, no cinematic depth of field. No film grain. No colour grading — iPhone natural processing. Natural window light only.*~~ (retired)

## 7.4 2-Clip Hybrid Format

**SUPERSEDED 2026-07-16 — the pipeline no longer uses 2-clip hook/reveal stitching.** Current
format is a single continuous 10s take per video (see §3.6 and §7.2 above). Kept here only as a
historical record of the original (abandoned) format.

---

# 8. CONTENT SCHEDULE — WEEK 1

| Video | Script | Product | Post Date | Status |
|---|---|---|---|---|
| 001 | BeforeYouScroll | Intro / no product | Pre-launch | ✅ |
| 004 | QuietFirst Matcha | Matcha powder | Tue 8 Jul, 8am BST | ✅ Posted |
| 003 | MorningFind NEOM | NEOM Wellbeing Diffuser | Thu 10 Jul, 8am BST | 🔄 In production |
| 005 | MadeWell Pen | Lamy Safari Fountain Pen | Fri 11 Jul, 8am BST | ⬜ Script ready, no Production v2 |

## Affiliate Links — Week 1

| Product | Link | Status |
|---|---|---|
| Matcha powder | (confirmed in script) | ✅ |
| NEOM Diffuser | https://amzn.to/4wpyfnb | ✅ |
| Lamy Safari Pen | https://amzn.to/4y67Nkb | ✅ |

---

# 9. CONTENT SCHEDULE — WEEK 2

| Video | Script | Product | Target Date | Status |
|---|---|---|---|---|
| 006 | AlwaysLit | NEOM Happiness Candle (Travel Size) | TBC | ⬜ Affiliate link live, script needs writing against actual product |
| 007 | JustThisBag | KALIDI Foldable Tote | TBC | ⬜ Affiliate link live, script needs writing against actual product |

**Note (2026-07-10):** Original product targets (Paddywax candle, Baggu tote) were swapped — SiteStripe links came back for NEOM's "Happiness" travel candle and a KALIDI foldable waterproof tote instead. No script content existed yet for either video, so nothing to rewrite — but when 006/007 get scripted, write them against these actual products, not the original brand names.

## Affiliate Links — Week 2

| Product | Link | Status |
|---|---|---|
| NEOM Happiness Candle (Travel Size) | https://amzn.to/3SVaRzt | ✅ |
| KALIDI Foldable Tote | https://amzn.to/4eQiiAw | ✅ |
| Owala FreeSip Bottle (008) | https://amzn.to/3RgQHPN | ✅ |
| ZIMASILK Silk Pillowcase (009) | https://amzn.to/4fiEd2a | ✅ |
| Brentfords Weighted Blanket (010) | https://amzn.to/4w49UmV | ✅ |

---

# 10. SCRIPTS LIBRARY

| # | Title | Product | Pillar | Score | Status |
|---|---|---|---|---|---|
| 001 | BeforeYouScroll | Intro / no product | Lore | — | ✅ Written |
| 002a | OneSpot Home/Desk | Anker (amended) | Tech | — | ✅ Written |
| 002b | PackLess Travel | Anker (amended) | Travel | — | ✅ Written |
| 003 | MorningFind | NEOM Diffuser | Morning | — | ✅ Production v2 ready |
| 004 | QuietFirst Matcha | Matcha powder | Morning | 44/50 | ✅ Posted |
| 005 | MadeWell Pen | Lamy Safari | Desk & Tech | 42/50 | ⬜ Needs Production v2 |
| 006 | AlwaysLit | Paddywax Candle | Home & Life | 41/50 | ⬜ Needs affiliate link + Production v2 |
| 007 | JustThisBag | Baggu Tote | Carry & Travel | — | ⬜ Script draft only |

---

# 11. OPERATIONAL LINKS & ACCOUNTS

## Active Platforms

| Platform | Handle / Link | Status |
|---|---|---|
| TikTok | @futurefindsmedia | ✅ Live. Business account under review. |
| Instagram | @futurefindsmedia | ✅ Live |
| Buffer | Cross-post scheduler | ✅ Connected |
| Amazon Associates UK | Store ID: `futurefindsmedia` | ✅ Live. 180-day clock active. Need 3 qualifying sales. |

## Future Website Requirements

The brand requires a public-facing web presence to support:

1. **Amazon Associates compliance** — storefront / disclosure page required
2. **Link-in-bio landing page** — centralised hub for all affiliate links
3. **Brand credibility** — when brand partners vet the account, a clean domain is essential
4. **SEO/content plays** — future blog or product round-ups for organic traffic
5. **TikTok Shop integration** — storefront link may require verified domain
6. **Email capture** — newsletter for converting followers to owned audience (future phase)

### Links the website will need to manage (future state):
- Per-video affiliate links (new link every post — 4–5/week)
- Amazon storefront embed or curated product list
- TikTok Shop storefront link
- "About Maruri" / brand story page
- Disclosure / affiliate disclaimer (legally required)
- Contact / brand partnerships inquiry form
- Privacy policy (required for EU/UK visitors)
- Archive of past finds (shoppable lookbook style)

### Domain suggestion:
`futurefinds.co.uk` (primary) or `futurefinds.co` (cleaner)

---

# 12. KEY BRAND RULES (NON-NEGOTIABLE)

1. **She never opens with the product.** Hook = her, not the thing.
2. **She never says "Buy Now", "OMG", or "You NEED this."** Wrong register.
3. **Every Higgsfield prompt includes the iPhone camera spec.** No exceptions.
4. **Trust is the moat.** One bad recommendation costs more than ten good ones earn.
5. **Character consistency trumps content volume.** One drift ruins the whole character.
6. **The 2-clip format is locked for product content.** Clip 1 = Hook+Build. Clip 2 = Reveal+CTA.
7. **Maruri's AI nature is not disclosed in content.** It's not hidden, but it's not the point.
8. **All content passes the ICP test first:** "Would a taste-conscious 22–34 year-old in London stop scrolling for this?"

---

# 13. METRICS TO TRACK

| Metric | Target | Red Flag |
|---|---|---|
| Watch Time % | 60%+ | < 40% = hook or pacing problem |
| Saves | 3%+ of views | < 2% = not useful enough |
| Shares | 1.5%+ of views | < 1% = shareability issue |
| Profile Visits | Growing week-on-week | Flat = content is too generic |
| Affiliate Link Clicks | Growing week-on-week | Flat = CTA or product problem |
| Amazon Qualifying Sales | 3 within 180 days | **CRITICAL — account at risk if missed** |

---

# 14. OPEN ACTION ITEMS

| Priority | Action | Owner | Deadline |
|---|---|---|---|
| 🔴 URGENT | Generate Higgsfield clips for Script 003 (yoga outfit, diffuser in bg) | JP | Thu 10 Jul |
| 🔴 URGENT | Build Script 005 Production v2 (Lamy Pen, 2-clip format) | Next session | Fri 11 Jul |
| 🔴 URGENT | Get 3 Amazon qualifying sales before 180-day deadline | JP | Rolling |
| 🟡 HIGH | Get SiteStripe affiliate links for Paddywax + Baggu | JP | This week |
| 🟡 HIGH | Confirm TikTok Business Account clickable link is live | JP | ASAP |
| 🟡 HIGH | Add phone number backup to TikTok (Settings → Security) | JP | Before Google Workspace trial ends |
| 🟠 MED | Build Production v2 for Script 006 (Candle) | Next session | Week 2 |
| 🟠 MED | Build Production v2 for Script 007 (Tote) | Next session | Week 2 |
| 🟠 MED | Create public-facing website with link hub + compliance pages | Next session | Before 3rd video posts |
| ⬜ FUTURE | Apply to TikTok Shop affiliate program | JP | Month 1 |
| ⬜ FUTURE | Apply to Impact/ShareASale for higher-commission brands | JP | Month 2 |
| ⬜ FUTURE | Set up email capture / newsletter | Phase 2 | Month 2–3 |
| ⬜ FUTURE | Build Instagram Stories cadence (5x/week) | Phase 2 | Month 2 |
| ⬜ FUTURE | Scale to 4–5 TikToks/week + 3 Reels/week steady state | Phase 2 | Month 2 |

---

# 15. FUTURE VISION

## Phase 1 — Foundation (Now → Month 3)
- Establish consistent posting cadence (4–5 TikToks/week)
- Hit 3 Amazon qualifying sales → unlock full Associates account
- Build TikTok to 1,000 followers (algorithm unlock)
- Test 2–3 different hook types to identify highest-converting formula

## Phase 2 — Monetisation (Month 3 → Month 6)
- TikTok Shop integration (once account approved)
- Apply to Impact/ShareASale for 10–25% commission brands
- Instagram Stories cadence — closer Maruri relationship with audience
- Launch email capture — newsletter "Things Worth Finding This Week"
- Revenue target: £500–£2,000/month affiliate income

## Phase 3 — Brand Authority (Month 6 → Month 12)
- Direct brand partnership pitches (£500–£5,000/deal)
- Launch shoppable website — curated product archive
- LTK integration for fashion/lifestyle discovery
- PartnerStack SaaS affiliate plays — software recommendations
- Begin Maruri lore content series (deeper character building)
- Revenue target: £3,000–£10,000/month combined

## Phase 4 — Expansion (Year 2+)
- Multiple AI characters under the Future Finds umbrella (different niches)
- YouTube Shorts pipeline
- Licensing Maruri's character/brand architecture to brands directly
- SaaS possibility: productise the AI influencer production system

---

# 16. DOCUMENT LIBRARY

| Document | Purpose | Location |
|---|---|---|
| MASTER_CHARACTER_BIBLE.md | Override authority for all character decisions | /Maruri Higgsfield/ |
| AUDIENCE_PERSONA_ICP.md | Who we're building for, behavioural triggers | /Maruri Higgsfield/ |
| PRODUCT_SELECTION_FRAMEWORK.md | Gate + scoring system for every product | /Maruri Higgsfield/ |
| CONTENT_SCORING_FRAMEWORK.md | Prioritisation system for every content idea | /Maruri Higgsfield/ |
| PRODUCTION_PIPELINE_SOP.md | End-to-end workflow: Research → Analyse | /Maruri Higgsfield/ |
| Future_Finds_Design_Philosophy.md | Void Signal aesthetic language | /Maruri Higgsfield/ |
| Hook_Playbook.md | 40+ hooks, data-backed type rankings, The Maruri Formula | /PRODUCTION SOP/ |
| iPhone_Camera_Spec.md | Mandatory camera spec for all Higgsfield prompts | /PRODUCTION SOP/ |
| SCRIPTS/ | All production scripts + Higgsfield prompts | /SCRIPTS/ |

---

*Future Finds · Master Overview v1.0 · July 2026 · Confidential*
