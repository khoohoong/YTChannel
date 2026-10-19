"""Word-level timestamps for each VO file -> gen/vo_words.json (used to sync shots to narration)."""
import json, glob, os, subprocess
import numpy as np
from faster_whisper import WhisperModel
m = WhisperModel("small.en", device="cpu", compute_type="int8")
out = {}
for f in sorted(glob.glob("render/src/E1_VO*.mp3")):
    seg = os.path.basename(f)[3:-4]
    raw = subprocess.run(["ffmpeg", "-v", "error", "-i", f, "-f", "f32le", "-ac", "1", "-ar", "16000", "-"], capture_output=True, check=True).stdout
    segs, _ = m.transcribe(np.frombuffer(raw, np.float32), word_timestamps=True, language="en")
    out[seg] = [{"w": w.word.strip(), "s": round(w.start, 2), "e": round(w.end, 2)} for s in segs for w in s.words]
    print(seg, len(out[seg]), "words, last ends", out[seg][-1]["e"], flush=True)
json.dump(out, open("gen/vo_words.json", "w"), indent=0)
