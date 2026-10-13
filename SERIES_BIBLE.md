# SERIES BIBLE — locked creative + technical settings
### Reuse these across every episode so the channel feels like one thing.

## NARRATOR — food-history channel (2026-10-13)
- **Arthur is retired for the food channel** (user: too close to a famous documentary narrator; want
  friendlier). Auditioning replacements — same test line, `text2speech_v2` / `elevenlabs` / preset:
  | Voice | voice_id | audition job |
  |---|---|---|
  | Benji (m) | `e6f9b893-51b1-51d3-afe9-9e0482cb7ac1` | `03f03dab-938a-45c1-a5db-27f6f9d895ca` |
  | Miles (m) | `e18664a7-ee4f-5273-acf8-533eb24cd366` | `38a5a932-f8a5-49a4-a6eb-6db5df6b39e1` |
  | Jasper (m) | `a7b8abe9-47f1-553e-a9df-87945a7e5bc8` | `aed36c36-0828-4940-8e9e-06fe017499ec` |
  | Daisy (f) | `032386ec-491b-5bdc-81ac-49e9a6a2c89d` | `3bca6d09-fc57-4703-8f62-51c6d612054a` |
  | Juno (f) | `a3ce02fe-4d3e-55bc-b4d4-a4801b9acdb4` | `8c536277-4ac1-4868-aa83-5b883f5af985` |
  | Chloe (f) | `e9cfbbf0-4476-46be-b396-596eb774b165` | `24358fdb-2333-4719-a729-04592e7f211b` |
  - **🔒 LOCKED (final, 2026-10-13): Benji (m)** — `voice_id: e6f9b893-51b1-51d3-afe9-9e0482cb7ac1`,
    `voice_type: preset`, `model: text2speech_v2`, `variant: elevenlabs`. Real pace on Ep 1 ≈ **150 wpm**.
  - ~~Marcus (m)~~ — briefly picked, replaced by Benji before VO: — `voice_id: 6f98d3dd-324f-4845-8c28-c1d1647a06cd`, `voice_type: preset`,
    `model: text2speech_v2`, `variant: elevenlabs`. Audition job `ee19eb19-cc57-46fb-a18b-3c025e30b865`
    (46 words → 18.64s ≈ **148 wpm** incl. pauses — still measure every VO).

## VISUAL LOOK — food-history channel (2026-10-13)
- **🔒 LOCKED: simple 3D clay/diorama look, animated as stop-motion** (user picked motion test
  clip 1 = `56e2aaa5-6f64-46f3-bb9d-0f6f2a23a737`, made from still `e55d8400-964e-486a-99a5-bff5e436fba2`).
  Not photoreal — avoids the "AI slop" look.
- **Style prefix (stills):** "Simple stylised 3D render, soft clay / diorama look, rounded shapes,
  matte materials, warm soft studio lighting, tilt-shift miniature feel. [scene]. Food modelled
  accurately and appetisingly. No text."
- **Motion prefix (Kling i2v):** "Stop-motion animation shot on twos, about 12 frames per second,
  slightly choppy handmade movement. [action]. Camera locked off. Miniature diorama, consistent
  characters, no morphing, no text." Use the clay still as `start_image`.
- Stills: `nano_banana_pro` with a claymation style prefix; motion: `kling3_0_turbo` image-to-video
  prompted "stop-motion, shot on twos (~12 fps), slightly choppy handmade movement, camera locked
  off, no morphing". The choppy look hides small AI motion glitches — that's the point.
- Always pass `declined_preset_id: 24bae836-2c4a-48e0-89b6-49fcc0b21612` on Kling (the IN THE DARK
  preset fired on a plain kitchen prompt).
- Style test jobs: clay still `e55d8400-964e-486a-99a5-bff5e436fba2`, claymation cook
  `0a15e54b-6d28-4c00-ae84-0a0f7a2a9b89`, claymation map diorama `1eeb5c3c-d423-432a-a051-495c3f7db166`,
  motion tests `56e2aaa5-6f64-46f3-bb9d-0f6f2a23a737`, `ea6c8747-c78a-4f5e-a929-e832cf402ff8`.

## NARRATOR — Episode 1 (Southeast Asia series, legacy)
- **Voice:** Arthur (deep, measured, documentary).
- Engine: ElevenLabs via Higgsfield `generate_audio`.
- `model: text2speech_v2` · `variant: elevenlabs` · `voice_type: preset`
- `voice_id: 30fc8796-ceb6-4a66-b3a7-4a145ef7f346`
- Deliver VO as **one file per segment** (not one long file) — makes measuring + editing clean.
- ⚠️ Arthur reads ~130–140 wpm effective — **measure actual duration, never trust word count.**

## VISUAL GENERATION (Higgsfield)
- **Hero shots:** `seedance_2_0`, 1080p, 5s, 16:9. One signature shot per segment.
- **B-roll:** `kling3_0_turbo`, 5s, 16:9.
- **Stills:** `nano_banana_pro`, 16:9 (Ken Burns in edit; hold 8–14s).
- **Shared style prefix** — put on every photoreal prompt for coherence:
  > "Photorealistic cinematic [shot], [subject + action], [lighting], [camera move],
  >  high-end nature-documentary realism, 4K, no text."
- **Always mute** the generated clip audio in the edit; VO + music bed only.
- **Preset trap:** dim/night/underwater/fire/candle/star prompts trigger the "IN THE DARK" preset.
  Pass `declined_preset_id: 24bae836-2c4a-48e0-89b6-49fcc0b21612` on those from the start.
- Cost (checked 2026-10-13): Kling 3.0 Turbo 5s = **10 cr @1080p** / 7.5 cr @720p; Nano Banana Pro still = 2 cr. Check `balance` before a big batch.

## MAPS & INFOGRAPHICS
- **Never** generate maps with a video model. Use the code renderer:
  `the-true-origin-of-southeast-asia/maps/render_maps.py` (matplotlib + Natural Earth 50m geojson).
- Map palette (matches the film grade):
  - Ocean `#0E272E` · Land `#5C4A33` · Coast `#243A40` · Graticule `#16323A`
  - Route/accent Amber `#E0A44E` · Highlight Gold `#F4CE86`
- Render clean (no text); add labels as overlays in the editor.

## MUSIC (sourced externally — tools can't generate it)
- Brief: cinematic ancient-mystery score, ~60–75 BPM building; low strings/drones, soft world
  percussion, regional flute/bamboo texture; full swell for the finale.
- Duck to −18 to −22 dB under VO. Per-segment dynamic arc (eerie → hopeful → tension → resolve).

## EDIT / DELIVERY CONVENTIONS
- 16:9, match VO sample rate; hard cuts on stressed VO beats; ½–1s music-only breath between segments.
- **Asset naming:** `H#` hero, `S#` still, `OB#`/`N#`/`P#` b-roll, `VO-X` narration, `MAP#` maps.
- **Every episode folder gets:** `script.md` (with fact-check log), `assets.md` (URLs **+ job IDs**),
  `edit_timeline_FINAL.md`, a download center, and a `maps/` folder if it has maps.
- Keep Higgsfield **job IDs** in assets.md — CloudFront URLs expire; job IDs let us re-fetch.

## REPO / GIT
- Git identity: `noreply@anthropic.com` / `Claude` (set at project start; else commits show unverified).
- One folder per episode at repo root. Series-wide docs (this file, the playbook, `tools/`) live at root.

## EPISODE LOG
| Ep | Title | Runtime | Status |
|---|---|---|---|
| 1 | The TRUE Origin of Southeast Asia | ~9:06 | Delivered |
| 2 | _tbd_ | — | Planning |
