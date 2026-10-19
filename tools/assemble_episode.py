#!/usr/bin/env python3
"""Assemble an Origin Plate episode into a finished MP4 (no music) with ffmpeg.

Reads the episode's gen/*.tsv + stills_prompts.json (same data as the download page), downloads every
asset into <episode>/render/src/, then builds:
  - each picture row normalised to 1920x1080 @ 24fps (clips as-is, stills/maps = slow push-in)
  - optional on-screen text overlays (map labels, dates)
  - picture trimmed/extended per segment to match the MEASURED VO + 0.75s breath
  - VO track with 0.75s gaps
Output: <episode>/render/<name>_nomusic.mp4
Usage: python3 tools/assemble_episode.py origin-plate-ep01-carbonara [--fake]   (--fake = placeholder media for a dry run)
"""
import json, os, subprocess, sys, urllib.request
EP = sys.argv[1]; FAKE = "--fake" in sys.argv
ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
E = os.path.join(ROOT, EP); G = os.path.join(E, "gen"); R = os.path.join(E, "render"); S = os.path.join(R, "src"); T = os.path.join(R, "tmp")
for d in (R, S, T): os.makedirs(d, exist_ok=True)
FF = "ffmpeg"; W, H, FPS, BREATH = 1920, 1080, 24, 0.75
FONT = "/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf"

def tsv(n): return dict(l.rstrip("\n").split("\t") for l in open(os.path.join(G, n)) if l.strip())
p = json.load(open(os.path.join(G, "stills_prompts.json")))
clip, still, vo = tsv("clipurls.tsv"), tsv("stillurls.tsv"), tsv("vourls.tsv")
SEG = [("VO0", 60.16), ("VO1", 102.96), ("VO2", 112.96), ("VO3", 82.40), ("VO3B", 55.28), ("VO4", 58.48), ("VO5", 23.92)]
SDUR = {"VO0-S1": 10, "VO1-S1": 10, "VO2-S1": 13, "VO3-S1": 9, "VO3B-S1": 7, "VO4-S1": 9}
MAPS = {"VO1": ("VO1-C12", "MAP1_italy_naples_rome.mp4", 8), "VO2": ("VO2-C10", "MAP2_rome_riccione.mp4", 10),
        "VO3": (None, "MAP3_rome_chicago.mp4", 8), "VO3B": ("VO3B-C2", "MAP4_goes_global.mp4", 8)}
# On-screen text: shot -> list of (text, x, y) in 1920x1080 px. Map positions match render_maps_ep01.py final frames.
TEXT = {
 "MAP1_italy_naples_rome.mp4": [("Naples", 1180, 600), ("Rome", 770, 440)],
 "MAP2_rome_riccione.mp4": [("Rome", 990, 760), ("Bologna", 560, 150), ("Riccione", 1040, 260)],
 "MAP3_rome_chicago.mp4": [("Chicago", 140, 470), ("Rome", 1700, 470)],
 "MAP4_goes_global.mp4": [("Rome", 900, 300), ("London", 700, 110), ("Chicago", 120, 190), ("New York", 330, 300),
                          ("Tokyo", 1560, 350), ("Sydney", 1620, 860), ("Buenos Aires", 470, 900)],
 "VO2-S1": [("La Stampa  ·  26 July 1950", None, 900)],
 "VO3-S1": [("1954  ·  1960  ·  mid-1960s  ·  1990s", None, 900)],
 "VO3B-S1": [("6 April  ·  Carbonara Day", None, 900)],
 "VO4-S1": [("Financial Times  ·  March 2023", None, 900)],
}
idx = {x["id"]: str(i) for i, x in enumerate(p)}

def run(cmd): subprocess.run(cmd, check=True, stdout=subprocess.DEVNULL, stderr=subprocess.PIPE)
def fetch(url, dst, kind):
    if os.path.exists(dst): return
    if FAKE:
        if kind == "audio": run([FF, "-y", "-f", "lavfi", "-i", "sine=f=220:d=5", dst])
        elif kind == "image": run([FF, "-y", "-f", "lavfi", "-i", f"testsrc2=s=2752x1536:d=1", "-frames:v", "1", dst])
        else: run([FF, "-y", "-f", "lavfi", "-i", f"testsrc2=s={W}x{H}:r={FPS}:d=5", dst])
        return
    subprocess.run(["curl", "-sSfL", "--retry", "3", "-o", dst, url], check=True)

def drawtext(items, start=0.0):
    f = []; en = f":enable='gte(t,{start:.2f})'" if start else ""
    for t, x, y in items:
        t = t.replace(":", r"\:").replace("'", "’")
        xs = "(w-text_w)/2" if x is None else str(x)
        f.append(f"drawtext=fontfile={FONT}:text='{t}':x={xs}:y={y}:fontsize=54:fontcolor=white:borderw=4:bordercolor=0x26221D{en}")
    return f

def norm(src, dst, length, kind, text):
    vf = []
    if kind == "still":
        n = int(length * FPS)
        vf.append(f"scale=3840:-2,zoompan=z='1+0.08*on/{n}':x='iw/2-(iw/zoom/2)':y='ih/2-(ih/zoom/2)':d={n}:s={W}x{H}:fps={FPS}")
        inp = ["-loop", "1", "-i", src]
    else:
        vf.append(f"scale={W}:{H}:force_original_aspect_ratio=decrease,pad={W}:{H}:(ow-iw)/2:(oh-ih)/2,fps={FPS}")
        inp = ["-i", src]
    # maps zoom/draw routes first: show labels only once they've settled (last 35% of the shot)
    vf += drawtext(text, length * 0.65 if kind == "map" else 0.0) + ["format=yuv420p"]
    run([FF, "-y", *inp, "-t", f"{length:.3f}", "-vf", ",".join(vf), "-an", "-c:v", "libx264", "-preset", "veryfast", "-crf", "18", dst])

sys.path.insert(0, G)
from cuesheet import CUES   # word-synced shot list (see gen/cuesheet.py)
LEAD = 0.12                  # cut a hair before the word so picture leads the voice

def src_len(path):
    out = subprocess.run(["ffprobe", "-v", "error", "-show_entries", "format=duration", "-of", "csv=p=0", path], capture_output=True, text=True).stdout
    return float(out.strip())

def fit_video(src, dst, slot, pingpong_ok):
    """Retime a clip/map to exactly `slot` seconds: trim if longer; slow down up to 1.5x if a bit short;
    ping-pong (forward+reverse) ambient clips if much shorter; finally hold the last frame if still short."""
    L = src_len(src); chain = []
    if slot <= L:
        chain = [f"trim=duration={slot:.3f}", "setpts=PTS-STARTPTS"]
    elif slot <= 1.5 * L or not pingpong_ok:
        f = min(slot / L, 1.5); chain = [f"setpts={f:.4f}*PTS"]
    else:
        f = min(slot / (2 * L), 1.5)
        flt = f"[0:v]split[a][b];[b]reverse[r];[a][r]concat=n=2:v=1:a=0,setpts={f:.4f}*PTS,fps={FPS},tpad=stop_mode=clone:stop_duration=30,trim=duration={slot:.3f}[o]"
        run([FF, "-y", "-i", src, "-filter_complex", flt, "-map", "[o]", "-an", "-c:v", "libx264", "-preset", "veryfast", "-crf", "18", dst]); return
    chain += [f"fps={FPS}", "tpad=stop_mode=clone:stop_duration=30", f"trim=duration={slot:.3f}"]
    run([FF, "-y", "-i", src, "-vf", ",".join(chain), "-an", "-c:v", "libx264", "-preset", "veryfast", "-crf", "18", dst])

seg_files = []; vo_files = []
for seg, dur in SEG:
    target = dur + BREATH if seg != "VO5" else dur + 3.0
    cues = CUES[seg]
    starts = [max(0.0, c[0] - LEAD) if i else 0.0 for i, c in enumerate(cues)]
    parts = []
    for k, (t0, shot, _anchor, overlay) in enumerate(cues):
        slot = (starts[k + 1] if k + 1 < len(cues) else target) - starts[k]
        out = os.path.join(T, f"{seg}_{k:02d}.mp4")
        if shot.startswith("MAP:"):
            name = shot[4:]; src = os.path.join(E, "maps", "map_clips", name)
            fitted = out + ".fit.mp4"; fit_video(src, fitted, slot, pingpong_ok=False)
            norm(fitted, out, slot, "map", TEXT.get(name, []))
        elif "-S" in shot:
            src = os.path.join(S, f"E1_{shot}.png"); fetch(still[idx[shot]], src, "image")
            norm(src, out, slot, "still", [(overlay, None, 900)] if overlay else [])
        else:
            src = os.path.join(S, f"E1_{shot}.mp4"); fetch(clip[idx[shot]], src, "video")
            fitted = out + ".fit.mp4"; fit_video(src, fitted, slot, pingpong_ok=True)
            norm(fitted, out, slot, "clip", [(overlay, None, 900)] if overlay else [])
        parts.append(out)
    lst = os.path.join(T, f"{seg}.txt"); open(lst, "w").write("".join(f"file '{x}'\n" for x in parts))
    sf = os.path.join(T, f"{seg}.mp4"); run([FF, "-y", "-f", "concat", "-safe", "0", "-i", lst, "-c", "copy", sf]); seg_files.append(sf)
    vsrc = os.path.join(S, f"E1_{seg}.mp3"); fetch(vo[seg], vsrc, "audio")
    vpad = os.path.join(T, f"{seg}_vo.wav")
    run([FF, "-y", "-i", vsrc, "-af", f"apad=whole_dur={target:.3f}", "-ar", "48000", "-ac", "2", vpad]); vo_files.append(vpad)
    print(f"{seg}: {len(cues)} shots, {target:.2f}s", flush=True)

lst = os.path.join(T, "all.txt"); open(lst, "w").write("".join(f"file '{x}'\n" for x in seg_files))
pic = os.path.join(T, "picture.mp4"); run([FF, "-y", "-f", "concat", "-safe", "0", "-i", lst, "-c", "copy", pic])
alst = os.path.join(T, "vo.txt"); open(alst, "w").write("".join(f"file '{x}'\n" for x in vo_files))
aud = os.path.join(T, "vo.wav"); run([FF, "-y", "-f", "concat", "-safe", "0", "-i", alst, "-c", "copy", aud])
out = os.path.join(R, f"{EP}_nomusic{'_FAKE' if FAKE else ''}.mp4")
run([FF, "-y", "-i", pic, "-i", aud, "-map", "0:v", "-map", "1:a", "-c:v", "copy", "-c:a", "aac", "-b:a", "192k", "-shortest", "-movflags", "+faststart", out])
print("DONE", out)
