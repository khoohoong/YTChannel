"""Builds edit_timeline_FINAL.md from the shot list + measured VO. Every row = a real asset at its real length."""
import json
p=json.load(open("gen/stills_prompts.json")); m={x["id"]:x for x in json.load(open("gen/motion.json"))}
VO=[("VO0","VO-0 Cold open",60.16),("VO1","VO-1 The legends",102.96),("VO2","VO-2 The soldiers",112.96),
    ("VO3","VO-3 Recipe kept changing",82.40),("VO3B","VO-3B Going global",55.28),("VO4","VO-4 The fight",58.48),("VO5","VO-5 Close",23.92)]
SDUR={"VO0-S1":10,"VO1-S1":10,"VO2-S1":13,"VO3-S1":9,"VO3B-S1":7,"VO4-S1":9}
MAPS={"VO1":("VO1-C12","MAP1_italy_naples_rome.mp4",8,"labels: Naples, Rome"),
      "VO2":("VO2-C10","MAP2_rome_riccione.mp4",10,"labels: Rome, Bologna, Riccione"),
      "VO3":(None,"MAP3_rome_chicago.mp4",8,"labels: Rome, Chicago"),
      "VO3B":("VO3B-C2","MAP4_goes_global.mp4",8,"labels: Rome, London, New York, Chicago, Tokyo, Sydney, Buenos Aires")}
OVER={"VO2-S1":"overlay: \"La Stampa · 26 July 1950\"","VO3-S1":"overlay cards: 1954 · 1960 · mid-1960s · 1990s",
      "VO3B-S1":"overlay: \"6 April — Carbonara Day\"","VO4-S1":"overlay: \"Financial Times, March 2023\"",
      "VO3B-C6":"optional labels: Alfredo · Lasagne · Carbonara"}
def fmt(t): return f"{int(t//60)}:{t%60:05.2f}"
L=["# ORIGIN PLATE Ep 1 — Carbonara · FINAL EDIT TIMELINE",
"**Runtime ≈ 8:21** (VO 496.2s + 6 × 0.75s music breaths) · 16:9 · 1080p · narrator Benji",
"","How to use: lay the VO files on the audio track in order with a 0.75s gap between them. Lay the",
"picture rows below back-to-back at their listed length. Clips are 5s; stills get a slow push-in (Ken Burns).",
"Trim the LAST picture row of each segment to land on the end of that segment's VO. Mute all clip audio;",
"music bed at −18 to −22 dB under VO. Filenames match the download page.","",
"Legend: CLIP = stop-motion 5s · STILL = prop still, push-in · MAP = code-rendered map (add labels)",""]
t=0.0; total_pic=0
for seg,name,dur in VO:
    L+= [f"## {name} — `E1_{seg}.mp3` ({dur:.2f}s) · starts {fmt(t)}","","| # | TC | Type | File | Len | Notes |","|---|---|---|---|---|---|"]
    rows=[]
    mp=MAPS.get(seg)
    if mp and mp[0] is None: rows.append(("MAP",f"maps/{mp[1]}",mp[2],mp[3]))
    for x in p:
        sid=x["id"]
        if not sid.startswith(seg+"-"): continue
        if "-S" in sid: rows.append(("STILL",f"E1_{sid}.png",SDUR[sid],OVER.get(sid,"")))
        else: rows.append(("CLIP",f"E1_{sid}.mp4",5,OVER.get(sid,"")))
        if mp and mp[0]==sid: rows.append(("MAP",f"maps/{mp[1]}",mp[2],mp[3]))
    if seg=="VO5": rows.append(("CARD","end card (Origin Plate logo + subscribe)",4,"to design"))
    st=t; n=0
    for k,(ty,f,ln,note) in enumerate(rows,1):
        L.append(f"| {k} | {fmt(st)} | {ty} | `{f}` | {ln}s | {note} |"); st+=ln; n+=ln
    L+=["",f"Picture total {n:.0f}s vs VO {dur:.1f}s → adjust the last row so it ends with the VO, then hold it through the 0.75s breath (Δ {n-dur:+.1f}s).",""]
    t+=dur+0.75; total_pic+=n
L+=[f"**Totals:** picture {total_pic:.0f}s · VO {sum(v[2] for v in VO):.1f}s · end ≈ {fmt(t-0.75)}"]
open("edit_timeline_FINAL.md","w").write("\n".join(L)+"\n"); print(fmt(t-0.75), total_pic)
