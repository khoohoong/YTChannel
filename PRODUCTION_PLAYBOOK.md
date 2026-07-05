# PRODUCTION PLAYBOOK — YouTube documentary series
### How we make an episode. Written from what Episode 1 taught us.

> **The golden rule: lock each stage before spending on the next.** Almost every cost overrun in
> Episode 1 came from generating assets before the thing they depend on was final. Do these phases
> **in order.** Don't generate visuals before the VO exists. Don't write a timeline before the
> footage budget is known.

---

## PHASE 0 — Concept lock (no spend)
- [ ] One-line premise + why it's compelling for this channel's audience.
- [ ] Target runtime (be realistic — see Phase 2 note on VO pace).
- [ ] Segment structure (Ep 1 used 4). List the segments.
- [ ] **Fact-check the OUTLINE before writing the full script.** Cheapest place to catch errors.

## PHASE 1 — Script, fact-checked and locked
- [ ] Write full narration to the segment structure.
- [ ] **Verify every hard claim against live sources** (dates, numbers, superlatives, "firsts").
  Keep a fact-check log in the script file. (Ep 1 shipped a wrong Flores date through TWO passes —
  do it before generating, not after.)
- [ ] Soften absolute claims ("every" → "almost every") unless verified.
- [ ] Get explicit script approval. This is the source of truth; everything downstream depends on it.

## PHASE 2 — Voiceover FIRST, then measure  ⭐ the highest-leverage change
- [ ] Generate the full VO (voice + settings in SERIES_BIBLE.md) **before any visuals.**
- [ ] **Measure the actual duration of each segment file.** Do not estimate from word count —
  Ep 1's narrator read ~40% slower than the word-count estimate (est. 6:25 → real 9:06).
- [ ] Split VO into segment-aligned files so each maps cleanly to its footage block.

## PHASE 3 — Footage budget (arithmetic, no spend)  ⭐ prevents the reshoot
- [ ] For each segment: `clips_needed ≈ (segment_VO_seconds ÷ clip_length_seconds)`.
  Clips are 5s. A 160s segment needs ~32 slots, not "a handful."
- [ ] Add stills (Ken Burns can hold ~8–14s each) and any hero shots to the count.
- [ ] Decide reuse policy up front (intentional bookends/callbacks are fine; stretching a 5s clip
  over a 12s slot is NOT — that was Ep 1's headline bug).
- [ ] Write the shot list to the measured VO. Use `tools/shot_budget.py` to do the math.

## PHASE 4 — Generate, one clean batch
- [ ] Use the locked **style prefix** (SERIES_BIBLE.md) on every prompt for visual coherence.
- [ ] **Bake `declined_preset_id` into every dim/night/underwater prompt** so the "IN THE DARK"
  preset never interrupts the batch. (Ep 1 lost time to repeated preset retries.)
- [ ] Right tool for the job (see TOOL-FIT below). Do NOT generate maps/charts/on-screen text with
  a video model.
- [ ] Preflight credits (`balance`) before firing a big batch; know the cost (~7.5 credits/Kling clip).

## PHASE 5 — Review gate
- [ ] Watch every clip. Flag glitches/artefacts and regenerate before locking the timeline
  (Ep 1 had one glitched clip that slipped to near-final).
- [ ] Confirm map geography and any recreated scenes are plausible/respectful.

## PHASE 6 — Assemble & hand off
- [ ] Build the edit timeline against measured VO (every row = a real clip at its real length).
- [ ] Publish the **download center** (see templates) — the no-terminal delivery format.
- [ ] Update the episode README/assets.md so the work survives a pause or a new session.

---

## TOOL-FIT — what each tool is actually for
| Need | Use | NOT |
|---|---|---|
| Photoreal B-roll / hero shots | Kling / Seedance (Higgsfield) | — |
| Narration | ElevenLabs "Arthur" (see bible) | — |
| **Accurate maps / routes / territory** | **code renderer** (`.../maps/render_maps.py`) | ❌ any video model (hallucinates geography + text) |
| On-screen labels, titles, charts, numbers | your editor / motion graphics | ❌ video models (gibberish text) |
| Music | external library (licensed) | ❌ these tools don't generate music |
| Still images (diagrams, portraits) | Nano Banana Pro | — |

## RECURRING GOTCHAS (all bit us in Ep 1)
- VO reads slower than word-count estimates — **measure, don't estimate.**
- Every clip is a fixed 5s — **budget slots accordingly.**
- Video models can't do maps or legible text — **render maps in code, add labels in edit.**
- The "IN THE DARK" preset hijacks dim prompts — **pre-decline it.**
- CloudFront asset URLs can expire — **keep job IDs in assets.md to re-fetch.**
- Set git identity to `noreply@anthropic.com` at project start (commits show unverified otherwise).
- Deliver files in the user's format (download center), not raw links or shell scripts.

## WHAT'S REUSABLE ACROSS EPISODES (don't rebuild)
- Narrator: Arthur (SERIES_BIBLE.md has the ID/model).
- Visual style prefix for generations (SERIES_BIBLE.md).
- Map renderer (`the-true-origin-of-southeast-asia/maps/render_maps.py`) — works for any region.
- Download-center template + repo handoff structure.
- Music brief (mood spec) — reuse as a starting point per episode.
