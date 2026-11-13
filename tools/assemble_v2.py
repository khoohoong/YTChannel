#!/usr/bin/env python3
"""Assemble the Ep 1 v2 remake (word-synced) into an MP4 with ffmpeg.

Data: <episode>/v2/shots.py (SHOTS, TAGS, SEG_DUR, plan()), v2/still_jobs.tsv, v2/clip_urls.tsv,
v2/src/VO_S*.mp3, <episode>/maps/map_clips/*.mp4.
Usage: python3 tools/assemble_v2.py origin-plate-ep01-carbonara [--draft]
  --draft = use the still (slow push-in) wherever a clip has not been downloaded yet.
Output: <episode>/v2/render/<episode>_v2_nomusic.mp4
"""
import os, subprocess, sys
EP = sys.argv[1]; DRAFT = "--draft" in sys.argv
ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
E = os.path.join(ROOT, EP); V = os.path.join(E, "v2"); R = os.path.join(V, "render"); T = os.path.join(R, "tmp")
ST = os.path.join(V, "stills"); CL = os.path.join(V, "clips")
for d in (R, T, ST, CL): os.makedirs(d, exist_ok=True)
sys.path.insert(0, V)
import shots
FF = "ffmpeg"; W, H, FPS, LEAD = 1920, 1080, 24, 0.12
FONT = "/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf"
MAPTEXT = {
 "MAP1_italy_naples_rome.mp4": [("Naples", 1180, 600), ("Rome", 770, 440)],
 "MAP2_rome_riccione.mp4": [("Rome", 990, 760), ("Bologna", 560, 150), ("Riccione", 1040, 260)],
 "MAP3_rome_chicago.mp4": [("Chicago", 140, 470), ("Rome", 1700, 470)],
 "MAP4_goes_global.mp4": [("Rome", 900, 300), ("London", 700, 110), ("Chicago", 120, 190), ("New York", 330, 300),
                          ("Tokyo", 1560, 350), ("Sydney", 1620, 860), ("Buenos Aires", 470, 900)],
}

def run(cmd):
    r = subprocess.run(cmd, stdout=subprocess.DEVNULL, stderr=subprocess.PIPE)
    if r.returncode: sys.exit("ffmpeg failed: " + " ".join(cmd[:12]) + "\n" + r.stderr.decode()[-1500:])
def rows(name):
    p = os.path.join(V, name)
    return [l.rstrip("\n").split("\t") for l in open(p)] if os.path.exists(p) else []
def fetch(url, dst):
    if not os.path.exists(dst) or os.path.getsize(dst) < 1000:
        subprocess.run(["curl", "-sSfL", "--retry", "3", "-o", dst, url], check=True)
def src_len(path):
    return float(subprocess.run(["ffprobe", "-v", "error", "-show_entries", "format=duration", "-of", "csv=p=0", path],
                                capture_output=True, text=True).stdout.strip())
ENC = ["-an", "-c:v", "libx264", "-preset", "veryfast", "-crf", "17", "-pix_fmt", "yuv420p"]
SCALE = f"scale={W}:{H}:force_original_aspect_ratio=decrease,pad={W}:{H}:(ow-iw)/2:(oh-ih)/2"

still = {r[1]: (int(r[0]), r[3]) for r in rows("still_jobs.tsv")}
clip = {r[1]: r[2] for r in rows("clip_urls.tsv")}          # id -> url

def make_still(sid, dst, slot, k):
    i, url = still[sid]; src = os.path.join(ST, f"{i:03d}_{sid}.png"); fetch(url, src)
    n = max(2, round(slot * FPS))
    z = f"1+0.07*on/{n}" if k % 2 == 0 else f"1.07-0.07*on/{n}"      # alternate push-in / pull-out
    vf = f"scale=3840:-2,zoompan=z='{z}':x='iw/2-(iw/zoom/2)':y='ih/2-(ih/zoom/2)':d={n}:s={W}x{H}:fps={FPS}"
    run([FF, "-y", "-loop", "1", "-i", src, "-vf", vf, "-frames:v", str(n), *ENC, dst])

def make_clip(sid, dst, slot):
    i, _ = still[sid]; src = os.path.join(CL, f"{i:03d}_{sid}.mp4"); fetch(clip[sid], src)
    L = src_len(src); n = round(slot * FPS)
    if slot <= L:            # use the whole action when only slightly long: gentle speed-up, else trim
        f = slot / L
        chain = [f"setpts={f:.4f}*PTS"] if f >= 0.8 else [f"trim=duration={slot:.3f}", "setpts=PTS-STARTPTS"]
    else:
        chain = [f"setpts={min(slot / L, 1.5):.4f}*PTS"]
    chain += [SCALE, f"fps={FPS}", "tpad=stop_mode=clone:stop_duration=30"]
    run([FF, "-y", "-i", src, "-vf", ",".join(chain), "-frames:v", str(n), *ENC, dst])

def make_map(name, dst, slot):
    src = os.path.join(E, "maps", "map_clips", name); L = src_len(src); n = round(slot * FPS)
    chain = [f"setpts={slot / L:.4f}*PTS", SCALE, f"fps={FPS}", "tpad=stop_mode=clone:stop_duration=30"]
    for t, x, y in MAPTEXT.get(name, []):
        chain.append(f"drawtext=fontfile={FONT}:text='{t}':x={x}:y={y}:fontsize=54:fontcolor=white:borderw=4:"
                     f"bordercolor=0x26221D:enable='gte(t,{slot * 0.65:.2f})'")
    run([FF, "-y", "-i", src, "-vf", ",".join(chain), "-frames:v", str(n), *ENC, dst])

plan = shots.plan(); segs = list(shots.SHOTS)
seg_files, vo_files, seg_start, t_acc, missing = [], [], {}, 0.0, []
for seg in segs:
    ps = [p for p in plan if p["seg"] == seg]
    target_f = round((shots.SEG_DUR[seg] + (shots.TAIL if seg == segs[-1] else shots.BREATH)) * FPS)
    starts = [round(max(0.0, p["t"] - LEAD) * FPS) if i else 0 for i, p in enumerate(ps)] + [target_f]
    parts = []
    for k, p in enumerate(ps):
        slot = (starts[k + 1] - starts[k]) / FPS; out = os.path.join(T, f"{seg}_{k:02d}.mp4")
        if p["kind"] == "map": make_map(p["id"][4:], out, slot)
        elif p["kind"] == "clip" and p["id"] in clip: make_clip(p["id"], out, slot)
        else:
            if p["kind"] == "clip":
                missing.append(p["id"])
                if not DRAFT: sys.exit(f"clip missing for {p['id']} (use --draft to fall back to the still)")
            make_still(p["id"], out, slot, k)
        parts.append(out)
    lst = os.path.join(T, f"{seg}.txt"); open(lst, "w").write("".join(f"file '{x}'\n" for x in parts))
    sf = os.path.join(T, f"{seg}.mp4"); run([FF, "-y", "-f", "concat", "-safe", "0", "-i", lst, "-c", "copy", sf]); seg_files.append(sf)
    vpad = os.path.join(T, f"{seg}_vo.wav")
    run([FF, "-y", "-i", os.path.join(V, "src", f"VO_{seg}.mp3"), "-af", f"apad=whole_dur={target_f / FPS:.4f}", "-ar", "48000", "-ac", "2", vpad])
    vo_files.append(vpad); seg_start[seg] = t_acc; t_acc += target_f / FPS
    print(f"{seg}: {len(ps)} shots, {target_f / FPS:.2f}s", flush=True)

lst = os.path.join(T, "all.txt"); open(lst, "w").write("".join(f"file '{x}'\n" for x in seg_files))
pic = os.path.join(T, "picture.mp4"); run([FF, "-y", "-f", "concat", "-safe", "0", "-i", lst, "-c", "copy", pic])
alst = os.path.join(T, "vo.txt"); open(alst, "w").write("".join(f"file '{x}'\n" for x in vo_files))
aud = os.path.join(T, "vo.wav"); run([FF, "-y", "-f", "concat", "-safe", "0", "-i", alst, "-c", "copy", aud])

# year / place / quote tags, lower-left, faded in and out (text via textfile so quotes and colons are safe)
tags = sorted((seg_start[s] + t0, txt) for s, lst_ in shots.TAGS.items() for t0, txt in lst_)
vf = []
for i, (a0, txt) in enumerate(tags):
    hold = 5.5 if len(txt) > 30 else 4.0
    b0 = min(a0 + hold, tags[i + 1][0] - 0.2) if i + 1 < len(tags) else a0 + hold
    tf = os.path.join(T, f"tag_{i:02d}.txt"); open(tf, "w").write(txt)
    fs = 52 if len(txt) <= 30 else 40
    al = f"if(lt(t,{a0:.2f}+0.35),(t-{a0:.2f})/0.35,if(gt(t,{b0:.2f}-0.35),({b0:.2f}-t)/0.35,1))"
    vf.append(f"drawtext=fontfile={FONT}:textfile='{tf}':x=80:y=h-150:fontsize={fs}:fontcolor=0xF6EBD9:"
              f"box=1:boxcolor=0x26221D@0.6:boxborderw=18:enable='between(t,{a0:.2f},{b0:.2f})':alpha='{al}'")
out = os.path.join(R, f"{EP}_v2_nomusic{'_DRAFT' if missing else ''}.mp4")
run([FF, "-y", "-i", pic, "-i", aud, "-map", "0:v", "-map", "1:a", "-vf", ",".join(vf), "-c:v", "libx264", "-preset", "medium",
     "-crf", "19", "-pix_fmt", "yuv420p", "-c:a", "aac", "-b:a", "192k", "-shortest", "-movflags", "+faststart", out])
print("DONE", out, f"{t_acc:.1f}s", "missing clips:", missing)
