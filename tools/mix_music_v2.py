#!/usr/bin/env python3
"""Mix the 3 Suno tracks under the Ep 1 v2 no-music cut.

T1 mystery   : hook + before + legends          (S0-S2)
T2 swing     : 1944 -> Chicago -> 1954 magazine (S3-S5), looped once at the S4/S5 boundary
T3 warm folk : going global -> verdict          (S6-S9), timed so its own ending lands on the last frame
Music sits ~15 dB under the narration and is ducked a further ~6 dB while Benji speaks (sidechain),
so it lifts in the breaths between sections and on the 3 s tail. Output is normalised to -14 LUFS.
Usage: python3 tools/mix_music_v2.py origin-plate-ep01-carbonara
"""
import os, subprocess, sys
EP = sys.argv[1]
ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
V = os.path.join(ROOT, EP, "v2"); R = os.path.join(V, "render"); M = os.path.join(V, "music")
sys.path.insert(0, V)
import shots
FPS = 24
segs = list(shots.SHOTS); start = {}; t = 0.0
for s in segs:
    start[s] = t
    t += round((shots.SEG_DUR[s] + (shots.TAIL if s == segs[-1] else shots.BREATH)) * FPS) / FPS
END = t
B1, B2, B3 = start["S3"], start["S5"], start["S6"]      # T1->T2, T2 loop join, T2->T3
T1, T2, T3 = [os.path.join(M, f) for f in ("T1_mystery_village_well.mp3", "T2_trattoria_swing.m4a", "T3_sotto_il_sole_di_napoli.m4a")]
T2_LEN, T3_AUDIBLE = 172.04, 186.17
X = 3.0                                                  # crossfade length
GAIN = {"T1": -30 + 14.6, "T2": -30 + 15.7, "T3": -30 + 14.8}   # bring every track to about -30 LUFS first
BASE = -2.0                                              # then set the bed about 15 dB under the VO (-16.9 LUFS)

def piece(i, src_off, length, at, g, fin, fout):
    """input i trimmed [src_off, src_off+length], faded, gained, delayed to start at `at` seconds."""
    d = int(max(at, 0) * 1000)
    return (f"[{i}:a]atrim={src_off:.3f}:{src_off + length:.3f},asetpts=PTS-STARTPTS,aresample=48000,"
            f"aformat=channel_layouts=stereo,afade=t=in:d={fin},afade=t=out:st={length - fout:.3f}:d={fout},"
            f"volume={g + BASE:.1f}dB,adelay={d}|{d}[p{i}]")

p1 = piece(1, 0, B1 + X / 2, 0, GAIN["T1"], 1.0, X)
p2 = piece(2, 0, (B2 - B1) + X, B1 - X / 2, GAIN["T2"], X, X)
l3 = (B3 - B2) + X                                       # second pass of the swing track: its last minute
p3 = piece(3, T2_LEN - l3 - 3.0, l3, B2 - X / 2, GAIN["T2"], X, X)
t3_at = END - 1.0 - T3_AUDIBLE                           # track's own ending lands 1 s before the last frame
p4 = piece(4, 0, T3_AUDIBLE + 1.0, t3_at, GAIN["T3"], 2.0, 0.5)
fc = ";".join([p1, p2, p3, p4,
    "[p1][p2][p3][p4]amix=inputs=4:normalize=0:duration=longest[bed]",
    "[0:a]aresample=48000,aformat=channel_layouts=stereo,asplit=2[vo][key]",
    "[bed][key]sidechaincompress=threshold=0.02:ratio=4:attack=40:release=700:makeup=1[duck]",
    f"[vo][duck]amix=inputs=2:normalize=0:duration=first,atrim=0:{END:.3f},loudnorm=I=-14:TP=-1.5:LRA=11[out]"])
src = os.path.join(R, f"{EP}_v2_nomusic.mp4"); out = os.path.join(R, f"{EP}_v2_FINAL.mp4")
cmd = ["ffmpeg", "-y", "-i", src, "-i", T1, "-i", T2, "-i", T2, "-i", T3, "-filter_complex", fc,
       "-map", "0:v", "-map", "[out]", "-c:v", "copy", "-c:a", "aac", "-b:a", "256k", "-ar", "48000", "-movflags", "+faststart", out]
r = subprocess.run(cmd, stdout=subprocess.DEVNULL, stderr=subprocess.PIPE)
if r.returncode: sys.exit(r.stderr.decode()[-2000:])
f = lambda x: f"{int(x // 60)}:{x % 60:04.1f}"
print("DONE", out)
print(f"T1 0:00-{f(B1)} | T2 {f(B1)}-{f(B3)} (loop join {f(B2)}) | T3 {f(t3_at)}-{f(END)}")
