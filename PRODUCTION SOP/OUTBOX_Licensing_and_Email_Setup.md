# OUTBOX — licensing confirmations + email deliverability fixes
## v1.0 · 2026-07-21 · everything here is ready to send/paste; each item is ~5 minutes
## These are the pre-outreach blockers from the gap audit. Do all three BEFORE the first cold send.

---

## 1. Higgsfield licensing email (SEND TODAY — the contract's clause 4 depends on it)

**To:** support@higgsfield.ai (or the in-app Help/Support widget if that's faster)
**From:** hello@futurefindsmedia.com
**Subject:** Commercial licensing question — third-party advertising use

> Hi,
>
> I'm on the Ultra plan (account: hello@futurefindsmedia.com). I understand from your Terms
> (§4.4) that I own the output generated on my account and can use it commercially.
>
> One specific confirmation for my records: **can video content generated on my account be
> licensed by me to third-party brands for use in their own paid advertising campaigns**
> (e.g. Meta/TikTok ads run from the brand's ad account)? The content features an original
> AI character created from text prompts on my account — no real person's likeness.
>
> A short written confirmation would be much appreciated — it's for my client contracts.
>
> Thanks,
> [name]

**Why:** we sell brands a license to run Maruri videos as ads. Higgsfield §4.4 says we own
output; this email turns "we believe" into "we have it in writing" before money changes hands.
File the reply in `PRODUCTION SOP/Rights_Verification_Notes.md` (it's the outstanding action
already flagged on line 23 there).

---

## 2. ElevenLabs music — commercial-use check (2 minutes, before any client render uses a bed)

The custom hot-take music bed will be generated with ElevenLabs Music. Before it lands in any
**client** deliverable:

1. Log into elevenlabs.io → check plan tier (Starter and up = commercial license; Free tier =
   NOT commercial).
2. Confirm the Music product specifically is covered by the commercial license on your tier
   (their Terms → "Commercial Use" / Music terms page).
3. If ambiguous, one-liner to their support: *"Does my [tier] plan's commercial license cover
   ElevenLabs Music output used in third-party brand advertising?"*

Note: for OUR organic clips this is low-risk either way; it only becomes contract-relevant
when a bed is baked into a paid client deliverable. Easy Lemon (Kevin MacLeod CC BY 4.0) is
already cleared for commercial use with attribution.

---

## 3. DMARC record (5 minutes at your DNS provider — deliverability gap found 2026-07-21)

Checked today: SPF ✓ (`v=spf1 include:_spf.google.com ~all`) · DKIM ✓ (google selector live)
· **DMARC ✗ missing** — cold-email receivers (Google/Microsoft especially) down-rank domains
without it, and bulk senders are increasingly required to have it.

Add ONE TXT record wherever futurefindsmedia.com's DNS lives:

| Host/Name | Type | Value |
|---|---|---|
| `_dmarc` | TXT | `v=DMARC1; p=none; rua=mailto:hello@futurefindsmedia.com; fo=1` |

- `p=none` = monitoring mode: nothing gets blocked, you just start collecting reports.
  After 2–4 weeks of clean outreach sending, tighten to `p=quarantine`.
- Verify after adding: `nslookup -type=TXT _dmarc.futurefindsmedia.com` should return the record.

**Outreach volume rule (from the deliverability audit):** when cold outreach starts, ramp
3/day → 5/day → 10/day over ~2 weeks. Never blast 10 on day one from a domain with no cold
history — a burned domain is semi-permanent.

---

## Status tracker
| Item | Done? | Evidence |
|---|---|---|
| Higgsfield licensing email sent | ☐ | reply filed in Rights_Verification_Notes.md |
| ElevenLabs commercial check | ☐ | tier + terms noted in MUSIC_BEDS.md |
| DMARC record added | ☐ | nslookup returns the record |
