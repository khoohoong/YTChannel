# SERIES BIBLE — locked creative + technical settings
### Reuse these across every episode so the channel feels like one thing.

## NARRATOR
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
- **Preset trap:** dim/night/underwater/fire/candle/star prompts trigger the "IN THE DARK" preset —
  and in Ep 2 even "glittering gold dust" and "monk at a ship's rail" triggered it. **Pass
  `declined_preset_id: 24bae836-2c4a-48e0-89b6-49fcc0b21612` on EVERY video prompt,
  unconditionally.** It has zero downside.
- **People prompts must state ethnicity explicitly** (Ep 2 review catch): models default to
  Western-looking people. Locals in this series → "Southeast Asian Malay/Indonesian, dark hair,
  brown skin"; specify period dress too. Only omit when the character *should* be foreign
  (e.g. the French scholar, a Chola emperor — still say so explicitly).
- **Held objects need a holder** (Ep 2 catch): "a magnifier moving across documents" animates the
  object moving BY ITSELF. Write "a hand holding/moving the [object]".
- **The "no text" style suffix makes documents/papers render BLANK** (Ep 2 catch): for shots that
  need visible writing, drop "no text" and write "covered in faint illegible ancient script,
  blurred and unreadable" instead — you get texture without gibberish.
- Cost ≈ 7.5 credits per Kling 5s clip. Check `balance` before a big batch.

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
| 2 | The Empire That VANISHED for 600 Years (Srivijaya) — Vanished Kingdoms 1/3 | **8:27 measured** | VO done; awaiting go for visuals batch |
| 3 | Champa — Vanished Kingdoms 2/3 | — | Series plan only |
| 4 | Majapahit — Vanished Kingdoms 3/3 | — | Series plan only |
