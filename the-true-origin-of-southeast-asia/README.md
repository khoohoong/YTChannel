# THE TRUE ORIGIN OF SOUTHEAST ASIA — Project Status / Handoff

> **READ THIS FIRST before doing any work next session.**
> This is a YouTube documentary project produced with Higgsfield (MCP).
> Work paused **2026-06-25** because the Higgsfield credit balance ran low.
> Resume **next month** once credits refill.

---

## 🎯 THE VIDEO
- **Title:** *The TRUE Origin of Southeast Asia*
- **Target runtime:** ~6:25 (≈385s)
- **Format:** cinematic history/prehistory documentary, 16:9
- **Structure:** 4 segments — (1) Hobbits of Flores, (2) Austronesian Expansion, (3) The Naga, (4) Angkor
- **Narration script:** `script.md` — **FACT-CHECKED & CORRECTED, locked, approved by user.**

## ✅ DECISIONS LOCKED (do not re-litigate)
- **Voice:** **Arthur** (deep male documentary). ElevenLabs.
  - model: `text2speech_v2_elevenlabs` · `voice_type: preset` · `voice_id: 30fc8796-ceb6-4a66-b3a7-4a145ef7f346`
- **Hero shots:** Seedance 2.0 (`seedance_2_0`), 1080p, 5s, 16:9, photoreal documentary style, "no text".
- **Stills:** Nano Banana Pro (`nano_banana_pro`), 16:9.
- **B-roll:** Kling (`kling3_0_turbo`), 5s, 16:9. (Note: prompts may trigger a preset suggestion e.g. "IN THE DARK" — decline with `declined_preset_id` and retry literal.)
- **Script tone & content:** approved as in `script.md`. Mute hero clips' built-in audio in the edit; VO + music only.
- **Music:** CANNOT be generated with these tools (TTS only). User sources a music bed externally. A music brief exists (see "Music brief" below).

## 📌 WHERE WE ARE
The project began as a short **1:46 teaser** ("The Forgotten Worlds of Southeast Asia") and was then **upgraded to the full 6:25 video**. The 12 teaser assets + 100s VO already exist (see `assets.md`) and are **reusable as a subset** of the full video — but they are NOT the whole thing.

### DONE
- [x] 4 hero shots (Seedance) — one per segment
- [x] 4 stills (Nano Banana Pro) — one per segment
- [x] 4 B-roll clips (Kling) — one per segment
- [x] Teaser VO (Arthur, 100.7s) — **SUPERSEDED** by the full 6:25 script; regenerate.
- [x] Full 6:25 script written, **fact-checked against live sources, corrected, user-approved**
- [x] Teaser edit timeline (`edit_timeline_short_v1.md`) — for the 1:46 cut only; reference, not final.

### PROGRESS (updated 2026-07-03)
1. [x] **Full ~6:25 Arthur VO** generated — 4 segment-aligned files (see `assets.md`, "FULL 6:25 PRODUCTION"). Model form is `text2speech_v2` + `variant: elevenlabs`.
2. [x] **18 new B-roll clips** generated (Standard coverage) — reuse existing 8 videos + 4 stills; stills kept minimal per user.
3. [x] **BUG FOUND & FIXED (2026-07-03):** every clip is a fixed **5 seconds**, but v2 of the
   timeline assigned single clips to 8–15s slots — impossible without slowing them down. User
   caught this. Fix chosen: **full 1× coverage**, not slow-mo.
4. [x] **39 more B-roll clips generated** (third batch) — 85 visuals total now, enough to cover
   the full 547s runtime with real 5s cuts and only light, intentional reuse (hero bookends +
   a handful of atmospheric repeats). See `assets.md` "THIRD B-ROLL BATCH".
5. [x] **N1a (Flores aerial) regenerated** — original had a visual glitch, replaced 2026-07-03.
   `download_assets_full.sh` and `assets.md` point at the new URL.
6. [x] **Timeline rebuilt as v3** — `edit_timeline_FINAL.md` now lists every clip at its real 5s
   length, back-to-back, instead of stretching one clip across a long slot. This is the
   authoritative timeline; `edit_timeline_full_v2.md` is superseded/kept for reference only.
7. [ ] (Optional, user offered later) Draft YouTube **title / description / thumbnail** concept.

**RUNTIME NOTE:** Arthur reads slower than estimated — final VO is **~9:06**, not 6:25. User chose to KEEP the ~9 min cut (2026-07-02). VO durations: A 2:41 · B 2:05 · C 1:43 · D 2:38.

Coverage: 85 visuals total (46 original + 39 batch-3), full 1× coverage achieved. Not slow-mo.
Everything to assemble the ~9 min cut now exists. Downloader: `download_assets_full.sh` (92 files).

## ⚠️ DO-NOT-MESS-UP NOTES
- The **teaser VO (100s) is obsolete** — the full script is the source of truth. Don't ship the 100s track as the final.
- **Flores dating was wrong in the first draft and is now fixed** (60k–100k yrs, extinction ~50k yrs ago — NOT 18,000). Do not revert to the 18,000-year figure.
- Other corrected figures: Austronesians left Taiwan ~4,000 ya; Angkor pop. 700k–900k (not "a million"); London ~20k in 12th c.; barays "traced from the air" (not "seen from space"). See `script.md` — it already contains the corrected text.
- **Check credits first** (`balance` tool) before firing a generation batch — that's why we paused.
- Higgsfield asset URLs (CloudFront) may expire; assets also live in the Higgsfield workspace under Generations. Re-fetch via `job_display` with the job IDs in `assets.md` if a link 404s.

## 🎵 Music brief (for external sourcing)
Cinematic ancient-mystery documentary score; slow ~60–75 BPM building; low sustained strings/drones, soft world percussion (frame drum, gamelan mallets), SE-Asian flute/bamboo texture; full string/brass swell for the Angkor finale. ~6:30 length. Duck to −18 to −22 dB under VO. Per-segment arc: Flores = eerie/minimal; Austronesian = hopeful/forward motion; Naga = tension/low brass; Angkor = full swell then resolve.

## 📁 Files in this folder
- `script.md` — corrected, approved 6:25 narration (source of truth)
- `assets.md` — all asset URLs + Higgsfield job IDs (46 original + 39 batch-3 + N1a fix)
- `download_assets.sh` — downloads only the original 12 teaser visuals + teaser VO (superseded)
- `download_assets_full.sh` — downloads all 92 files for the full ~9:07 cut (use this one)
- `edit_timeline_FINAL.md` — **v3, authoritative.** Real 5s-per-clip coverage, no impossible slots.
- `edit_timeline_full_v2.md` — superseded (had the 8–15s-slot bug); kept for reference only
- `edit_timeline_short_v1.md` — the 1:46 teaser timeline (early template, reference only)
- `new_broll_batch3_jobids.md` — raw job-ID scratch notes from generating the third batch
