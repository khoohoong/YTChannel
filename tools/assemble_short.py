#!/usr/bin/env python3
"""Build a vertical 9:16 Short (YouTube Shorts / FB Reels) from an episode's existing clips + a short VO.
Layout 1080x1920: blurred full-bleed background, centred 4:5 crop of the shot, word-timed captions,
year tags, a hook title for the first seconds. Everything stays inside the Shorts/Reels safe zone.
Usage: python3 tools/assemble_short.py origin-plate-ep01-carbonara"""
import json, os, subprocess, sys
EP = sys.argv[1]
ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
E = os.path.join(ROOT, EP); SH = os.path.join(E, "short"); SRC = os.path.join(E, "render", "src"); T = os.path.join(SH, "tmp")
os.makedirs(T, exist_ok=True)
sys.path.insert(0, SH); from short_cues import CUES, CAPTIONS, TAGS, HOOK, TAIL
FF, FPS = "ffmpeg", 24
FONT = "/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf"
def run(c): subprocess.run(c, check=True, stdout=subprocess.DEVNULL, stderr=subprocess.PIPE)
def dur(p): return float(subprocess.run(["ffprobe","-v","error","-show_entries","format=duration","-of","csv=p=0",p],capture_output=True,text=True).stdout)
enc = ["-an", "-c:v", "libx264", "-preset", "veryfast", "-crf", "17", "-pix_fmt", "yuv420p"]

vo = os.path.join(SH, "short_vo.mp3"); total_f = round((dur(vo) + TAIL) * FPS)
starts = [round(c[0] * FPS) for c in CUES] + [total_f]
parts = []
for k, (t0, shot) in enumerate(CUES):
    slot = (starts[k + 1] - starts[k]) / FPS; out = os.path.join(T, f"{k:02d}.mp4")
    if "-S" in shot:   # still -> gentle push-in
        n = round(slot * FPS)
        run([FF, "-y", "-loop", "1", "-i", os.path.join(SRC, f"E1_{shot}.png"), "-t", f"{slot:.3f}", "-vf",
             f"scale=3840:-2,zoompan=z='1+0.06*on/{n}':x='iw/2-(iw/zoom/2)':y='ih/2-(ih/zoom/2)':d={n}:s=1920x1080:fps={FPS}", *enc, out])
    else:              # clip -> trim, or slow up to 1.5x, then hold last frame
        src = os.path.join(SRC, f"E1_{shot}.mp4"); L = dur(src)
        f = 1.0 if slot <= L else min(slot / L, 1.5)
        run([FF, "-y", "-i", src, "-vf", f"setpts={f:.4f}*PTS,scale=1920:1080,fps={FPS},tpad=stop_mode=clone:stop_duration=30,trim=duration={slot:.3f}", *enc, out])
    parts.append(out)
lst = os.path.join(T, "list.txt"); open(lst, "w").write("".join(f"file '{p}'\n" for p in parts))
wide = os.path.join(T, "wide.mp4"); run([FF, "-y", "-f", "concat", "-safe", "0", "-i", lst, "-c", "copy", wide])

def esc(s): return s.replace("\\", "\\\\").replace(":", r"\:").replace("'", "’").replace(",", r"\,")
def fade(a, b, d=0.25): return f"if(lt(t,{a:.2f}+{d}),(t-{a:.2f})/{d},if(gt(t,{b:.2f}-{d}),({b:.2f}-t)/{d},1))"
dt = []
# hook title (top of the picture)
a, b, lines = HOOK
for i, ln in enumerate(lines):
    dt.append(f"drawtext=fontfile={FONT}:text='{esc(ln)}':x=(w-text_w)/2:y={250 + i*92}:fontsize=74:fontcolor=white:borderw=6:bordercolor=0x26221D:enable='between(t,{a},{b})':alpha='{fade(a,b)}'")
# year tags (top-left of the picture)
for i, (a, txt) in enumerate(TAGS):
    b = min(a + 3.5, TAGS[i+1][0] - 0.2) if i + 1 < len(TAGS) else a + 3.5
    dt.append(f"drawtext=fontfile={FONT}:text='{esc(txt)}':x=70:y=190:fontsize=50:fontcolor=0xF6EBD9:box=1:boxcolor=0x26221D@0.65:boxborderw=16:enable='between(t,{a:.2f},{b:.2f})':alpha='{fade(a,b)}'")
# captions (lower third of the picture, inside the safe zone)
for i, (a, txt) in enumerate(CAPTIONS):
    b = CAPTIONS[i+1][0] if i + 1 < len(CAPTIONS) else a + 2.0
    dt.append(f"drawtext=fontfile={FONT}:text='{esc(txt)}':x=(w-text_w)/2:y=1250:fontsize=82:fontcolor=white:borderw=8:bordercolor=0x1B1814:enable='between(t,{a:.2f},{b:.2f})'")
fc = ("[0:v]split[a][b];"
      "[a]scale=-2:1920,crop=1080:1920,boxblur=30:3,eq=brightness=-0.18:saturation=0.8[bg];"
      "[b]crop=864:1080,scale=1080:1350[fg];"
      "[bg][fg]overlay=0:140," + ",".join(dt) + "[v]")
out = os.path.join(SH, f"{EP}_short_vertical_nomusic.mp4")
run([FF, "-y", "-i", wide, "-i", vo, "-filter_complex", fc + ";[1:a]apad[au]", "-map", "[v]", "-map", "[au]",
     "-t", f"{total_f / FPS:.3f}", "-c:v", "libx264", "-preset", "medium", "-crf", "19", "-pix_fmt", "yuv420p",
     "-c:a", "aac", "-b:a", "192k", "-movflags", "+faststart", out])
print("DONE", out, f"{total_f / FPS:.2f}s")
