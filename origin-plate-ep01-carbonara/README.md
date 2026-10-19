# Origin Plate — Ep 1: "Carbonara Isn't As Italian As You Think"

## Status (2026-10-13)
- [x] Phase 0 — concept + outline, fact-checked
- [x] Phase 1 — script approved (v1.2 adds Seg 3B — needs user OK)
- [x] Phase 2 — VO with **Benji**, 7 files, measured **8:16** (`vo_and_shotlist.md`)
- [x] Phase 3 — shot list: 80 clips + 7 stills + 4 maps, ~1,100 cr @1080p — **awaiting spend approval**
- [x] Phase 4 — 86 clay stills (172 cr), 80 stop-motion clips (800 cr, 1080p), 4 code maps. Job IDs in `assets.md`.
- [ ] Phase 5 — **user reviews clips**, flag glitches → regenerate
- [~] Phase 6 — `edit_timeline_FINAL.md` + download page published: https://claude.ai/artifact/NokbtDPHzxqXrCpdhPZheS (regenerate with `gen/build_download_center.py` when links expire)
- [ ] Still to do: thumbnail, title/description, Shorts cuts, end card

## Notes
- First 6 VO files measured 7:21 → added Seg 3B "going global" (55s) → 8:16.
- Maps (Rome, Riccione, Chicago) → code renderer, restyled to the clay palette. No AI-generated text.
- Next episode tease in the close: fortune cookies.

## Render (2026-10-18)
- Full cut assembled in code: `python3 tools/assemble_episode.py origin-plate-ep01-carbonara` → `render/origin-plate-ep01-carbonara_nomusic.mp4` (8:24, 1080p, 137 MB, no music). Sent to user directly. Render folder is git-ignored; re-run the script to rebuild.
- Needs the sandbox network to allow `d8j0ntlcm91z4.cloudfront.net` (user enabled it 2026-10-18).
- **v2 (2026-10-19):** user flagged picture/VO mismatch (esp. first minute). Fixed by syncing every cut to the
  narration: Whisper word timestamps (`gen/transcribe_vo.py` → `gen/vo_words.json`), hand-authored cue sheet
  (`gen/cuesheet.py`), assembler retimes clips (trim / ≤1.5× slow / ping-pong / hold) and frame-aligns slots.
  Picture 503.71s = audio 503.70s. Sent to user.
