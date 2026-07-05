#!/usr/bin/env python3
"""Footage budget calculator — the arithmetic that prevents Episode 1's coverage bug.

Given each segment's MEASURED voiceover length, tells you how many 5s clips (and stills) you
actually need, so you never write a timeline slot longer than the footage that fills it.

Usage:
    python3 shot_budget.py                 # runs the built-in Episode-1 example
    python3 shot_budget.py 161 125 103 158 # pass measured VO seconds per segment

Notes:
- clip_len defaults to 5s (our generated clips). Change with --clip.
- A still held via Ken Burns counts as ~10s of coverage by default (--still).
- Assumes ~1 clip per slot at 1x speed. If you plan intentional reuse, subtract those.
"""
import sys

def budget(seg_seconds, clip_len=5.0, still_hold=10.0, stills_per_seg=1):
    total = sum(seg_seconds)
    print(f"{'SEG':>4} {'VO(s)':>7} {'clips':>6} {'stills':>7} {'covered(s)':>11}")
    print("-" * 40)
    grand_clips = 0
    for i, s in enumerate(seg_seconds, 1):
        still_cov = stills_per_seg * still_hold
        remaining = max(0.0, s - still_cov)
        clips = -(-int(remaining) // int(clip_len))  # ceil
        grand_clips += clips
        covered = clips * clip_len + still_cov
        print(f"{i:>4} {s:>7.0f} {clips:>6} {stills_per_seg:>7} {covered:>11.0f}")
    print("-" * 40)
    total_stills = stills_per_seg * len(seg_seconds)
    print(f"TOTAL VO: {total:.0f}s ({total/60:.1f} min)")
    print(f"NEED: ~{grand_clips} clips + {total_stills} stills "
          f"(at {clip_len:.0f}s/clip, stills held {still_hold:.0f}s)")
    print(f"Rough credit cost @7.5/clip: ~{grand_clips*7.5:.0f} credits")
    print("\nReminder: if you plan hero-bookends or an outro montage, those are reuse — "
          "subtract them from the clip count above.")

if __name__ == "__main__":
    args = [a for a in sys.argv[1:] if not a.startswith("--")]
    clip = 5.0
    for a in sys.argv[1:]:
        if a.startswith("--clip="): clip = float(a.split("=")[1])
    if args:
        segs = [float(x) for x in args]
    else:
        print("(no args — using Episode 1's measured VO as an example)\n")
        segs = [161, 125, 103, 158]   # Ep1 segment VO seconds (A/B/C/D)
    budget(segs, clip_len=clip)
