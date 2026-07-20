# THE LOST WORLD OF SOUTHEAST ASIA — Episode Status / Handoff

> **Series reboot — this is the new Episode 1.** Self-contained. No callbacks to any other episode,
> no "like & subscribe." Written in the **Bright Side** style (warm, curious, simple) and pitched so a
> **5th grader** can follow it. New narrator voice for the reboot (Arthur retired here — see below).
>
> Read `CLAUDE.md`, `PRODUCTION_PLAYBOOK.md`, `SERIES_BIBLE.md` at repo root first.

## 🎯 THE VIDEO
- **Working title:** *The Lost World of Southeast Asia* (alt hooks below)
- **Format:** curiosity-driven history/prehistory, Bright Side tone, 16:9
- **Structure:** cold open + **5 segments** + outro
  1. Sundaland — the drowned land under the sea
  2. Sulawesi cave art — the oldest story on Earth (51,200 yrs)
  3. Flores "Hobbits" — the tiny people (*Homo floresiensis*)
  4. The Austronesians — the greatest sea journey ever
  5. Angkor — the city the jungle ate
- **Script:** `script.md` — **fact-checked against live sources (2026-07-20), with fact-check log.**
- **Visual prompts:** `visual_direction.md` — detailed, accuracy-first artist-impression prompt library.

## ✅ WHERE WE ARE (Phase 0 + 1 done)
- [x] Concept + segment structure locked (Phase 0)
- [x] Full narration written to structure (Phase 1)
- [x] Every hard claim fact-checked against live sources; fact-check log in `script.md`
- [x] Accuracy-focused visual prompt library written (`visual_direction.md`)
- [x] **Script approved by user** (2026-07-20)
- [x] **Narrator voice picked: Mark** (`27c04473-84a9-4b60-a41f-c8e8458bd4f1`) — locked in SERIES_BIBLE
- [x] On-screen text plan written (`onscreen_text_plan.md`) — titles/dates/place-names timed to VO beats
- [x] Phase 2: VO generated in **Mark** and **measured** → 7 files, **total ~8:55** (see `assets.md`)
- [x] Phase 3 math done: full 1× coverage ≈ **95 clips + 7 stills ≈ 712 credits** (`shot_budget.py`)
- [ ] **Decide visual coverage level** (full vs smart ~60–70 clips) ← spend decision, waiting on user
- [ ] Phase 4: generate visuals (check `balance` first) · Phase 5: review · Phase 6: assemble + download center

**Measured VO durations:** cold open 39.1s · S1 76.8s · S2 74.9s · S3 95.4s · S4 111.5s · S5 104.2s · outro 33.0s.
- [ ] Phase 3: shot budget to measured VO (`tools/shot_budget.py`)
- [ ] Phase 4: generate visuals (check `balance` first) · Phase 5: review · Phase 6: assemble + download center

## 🎙️ NARRATOR VOICE — LOCKED: Mark
- **Mark** (`27c04473-84a9-4b60-a41f-c8e8458bd4f1`), `voice_type: preset` — warm, friendly, Bright-Side energy.
- Engine: ElevenLabs via `generate_audio`: `model: text2speech_v2` · `variant: elevenlabs`.
- Now the reboot narrator in `SERIES_BIBLE.md` (Arthur kept as legacy voice).

## 🧾 ALT TITLES / HOOKS (for thumbnail + packaging later)
- "The Lost World of Southeast Asia"
- "Southeast Asia's Craziest Origin Story"
- "A Whole Continent Is Hidden Under This Sea"
- "The Oldest Story on Earth Is Painted in This Cave"

## ⚠️ DO-NOT-MESS-UP NOTES
- **Stands alone.** No "last time," no "subscribe," no cross-episode references anywhere.
- **Keep it 5th-grade simple.** Short sentences, explain every big word, lots of "you."
- **Accuracy of artist impressions matters most** — see the review checklist at the bottom of
  `visual_direction.md`. Reject takes with wrong boats/temple/hominin/cave-art.
- **Maps in code, not video** (`render_maps.py`). Add all on-screen text in the editor.
- **Pre-decline "IN THE DARK"** on cave/night/underwater prompts (`declined_preset_id` in bible).
- **Measure VO, don't estimate.** Every 5s clip is one slot — budget with `tools/shot_budget.py`.
- **Check `balance`** before any big generation batch; state the rough credit cost first.
- This sandbox can't `curl` the Higgsfield CDN — deliver URLs/download-center to the user.

## 📁 Files
- `script.md` — narration + fact-check log (source of truth once approved)
- `visual_direction.md` — accuracy-first prompt library + Phase-5 accuracy checklist
- `README.md` — this handoff
