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

seg_files = []; vo_files = []
for seg, dur in SEG:
    rows = []; mp = MAPS.get(seg)
    if mp and mp[0] is None: rows.append(("map", mp[1], mp[2]))
    for x in p:
        sid = x["id"]
        if not sid.startswith(seg + "-"): continue
        rows.append(("still", sid, SDUR[sid]) if "-S" in sid else ("clip", sid, 5))
        if mp and mp[0] == sid: rows.append(("map", mp[1], mp[2]))
    target = dur + BREATH if seg != "VO5" else dur + 3.0   # last segment: 3s tail for end card / music out
    total = sum(r[2] for r in rows); rows[-1] = (rows[-1][0], rows[-1][1], rows[-1][2] + (target - total))
    parts = []
    for k, (kind, name, ln) in enumerate(rows):
        if kind == "map":
            src = os.path.join(E, "maps", "map_clips", name)
        elif kind == "still":
            src = os.path.join(S, f"E1_{name}.png"); fetch(still[idx[name]], src, "image")
        else:
            src = os.path.join(S, f"E1_{name}.mp4"); fetch(clip[idx[name]], src, "video")
        out = os.path.join(T, f"{seg}_{k:02d}.mp4")
        # a clip shorter than its slot holds its last frame (tpad) instead of stretching
        if kind != "still":
            tmp = out + ".pad.mp4"
            run([FF, "-y", "-i", src, "-vf", f"tpad=stop_mode=clone:stop_duration=10", "-an", "-c:v", "libx264", "-preset", "veryfast", "-crf", "18", tmp]); src = tmp
        norm(src, out, ln, kind, TEXT.get(name, []))
        parts.append(out)
    lst = os.path.join(T, f"{seg}.txt"); open(lst, "w").write("".join(f"file '{x}'\n" for x in parts))
    sf = os.path.join(T, f"{seg}.mp4"); run([FF, "-y", "-f", "concat", "-safe", "0", "-i", lst, "-c", "copy", sf]); seg_files.append(sf)
    vsrc = os.path.join(S, f"E1_{seg}.mp3"); fetch(vo[seg], vsrc, "audio")
    vpad = os.path.join(T, f"{seg}_vo.wav")
    run([FF, "-y", "-i", vsrc, "-af", f"apad=whole_dur={target:.3f}", "-ar", "48000", "-ac", "2", vpad]); vo_files.append(vpad)
    print(f"{seg}: {len(rows)} shots, {target:.2f}s", flush=True)

lst = os.path.join(T, "all.txt"); open(lst, "w").write("".join(f"file '{x}'\n" for x in seg_files))
pic = os.path.join(T, "picture.mp4"); run([FF, "-y", "-f", "concat", "-safe", "0", "-i", lst, "-c", "copy", pic])
alst = os.path.join(T, "vo.txt"); open(alst, "w").write("".join(f"file '{x}'\n" for x in vo_files))
aud = os.path.join(T, "vo.wav"); run([FF, "-y", "-f", "concat", "-safe", "0", "-i", alst, "-c", "copy", aud])
out = os.path.join(R, f"{EP}_nomusic{'_FAKE' if FAKE else ''}.mp4")
run([FF, "-y", "-i", pic, "-i", aud, "-map", "0:v", "-map", "1:a", "-c:v", "copy", "-c:a", "aac", "-b:a", "192k", "-shortest", "-movflags", "+faststart", out])
print("DONE", out)
