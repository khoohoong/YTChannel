"""Builds edit_timeline_FINAL.md from gen/cuesheet.py (word-synced) + measured VO."""
import sys; sys.path.insert(0, "gen")
from cuesheet import CUES
SEG=[("VO0","Cold open",60.16),("VO1","The legends",102.96),("VO2","The soldiers",112.96),("VO3","The recipe that kept changing",82.40),("VO3B","Going global",55.28),("VO4","The fight",58.48),("VO5","Close",23.92)]
def fmt(t): return f"{int(t//60)}:{t%60:05.2f}"
L=["# ORIGIN PLATE Ep 1 — Carbonara · EDIT TIMELINE (v2, word-synced)",
"Every cut lands on the narration word it illustrates (Whisper word timestamps of the measured VO, cut 0.12s early).",
"Rendered automatically by `tools/assemble_episode.py`; this file is the human-readable version.",""]
t=0.0
for seg,name,dur in SEG:
    L+=[f"## {name} — `E1_{seg}.mp3` ({dur:.2f}s) · starts {fmt(t)}","","| TC | Shot | On the words | Overlay |","|---|---|---|---|"]
    for t0,shot,anchor,ov in CUES[seg]:
        L.append(f"| {fmt(t+t0)} | `{shot}` | “{anchor}” | {ov or ''} |")
    L.append(""); t+=dur+0.75
open("edit_timeline_FINAL.md","w").write("\n".join(L)+"\n")
