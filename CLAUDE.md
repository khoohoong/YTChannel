# CLAUDE.md — read this first, every session

This repo produces an AI-assisted **YouTube documentary series**. A new chat starts with no memory
of past sessions — **all continuity lives in these files.** Read them before doing anything:

1. **`PRODUCTION_PLAYBOOK.md`** — the ordered pipeline and every hard-won lesson. Follow the phase
   order; it exists because doing things out of order cost real time and credits on Episode 1.
2. **`SERIES_BIBLE.md`** — locked reusable settings: narrator voice ID + model, the generation
   style prefix, model choices, map palette, naming conventions, git identity.
3. The latest episode folder (e.g. `the-true-origin-of-southeast-asia/`) — its `README.md` is the
   handoff/status for that episode.

## The one rule that matters most
**Lock each stage before spending on the next:** script (fact-checked) → voiceover → **measure real
durations** → budget footage to that number (`tools/shot_budget.py`) → generate → review → assemble.
Never generate visuals before the VO exists and is measured.

## Tool-fit (don't repeat Episode 1's mistakes)
- Photoreal B-roll/hero → Kling / Seedance. Narration → ElevenLabs "Arthur" (bible has the ID).
- **Maps / routes / anything with on-screen text or accurate geography → render in CODE**
  (`the-true-origin-of-southeast-asia/maps/render_maps.py`), NOT a video model. Video models
  hallucinate coastlines and produce gibberish text. Add labels in the editor.
- Thumbnails with headlines → composite in code (crisp text) or Nano Banana Pro (image model, ok at
  text); never bake headline text with a video model. Example: `.../thumbnails/thumbnail_build.py`.
- Music is NOT generatable here — the user sources it externally (brief is in SERIES_BIBLE.md).

## How the user likes to work (preferences)
- **Not comfortable with the terminal or git.** Deliver finished files, not commands. Use the
  download-center HTML pattern (a click-through page with per-file "Save Link As" + progress), or
  send files directly. Don't hand over raw shell scripts as the primary delivery.
- Wants **accurate facts** — fact-check hard claims against live sources *before* writing/generating,
  and keep a fact-check log in the script.
- Reviews visuals before the timeline is locked; flag glitches and regenerate.
- Prefers options with a clear recommendation over open-ended menus.
- Check Higgsfield credit `balance` before a big generation batch and state the rough cost.

## Gotchas that will bite you (all happened in Ep 1)
- VO reads ~40% slower than word-count estimates → measure, don't estimate.
- Every generated clip is a fixed 5s → budget slot counts accordingly (`tools/shot_budget.py`).
- The "IN THE DARK" preset hijacks dim/night prompts → pass
  `declined_preset_id: 24bae836-2c4a-48e0-89b6-49fcc0b21612`.
- CloudFront asset URLs expire → keep Higgsfield **job IDs** in `assets.md` to re-fetch.
- This sandbox's network **blocks the Higgsfield CDN** (`d8j0ntlcm91z4.cloudfront.net`), so you
  can't `curl` generated assets here — deliver URLs to the user, who downloads on their own machine.
- Set git identity `noreply@anthropic.com` / `Claude` at the start or commits show as unverified.

## Status
- **Episode 1** — "The TRUE Origin of Southeast Asia" (~9:06) — delivered. Assets, timeline, maps,
  thumbnails, and YouTube packaging are all in its folder.
- **Episode 2** — not started. To begin: confirm topic, then run Phase 0 → 1 of the playbook
  (outline → fact-check → script) before any generation.

## Starting a new episode
Say: *"Read the playbook and bible, then start Episode 2 on [topic]."* Reuse Arthur, the style
prefix, the map renderer, and the download-center pattern. Create a new episode folder; don't touch
Episode 1's.
