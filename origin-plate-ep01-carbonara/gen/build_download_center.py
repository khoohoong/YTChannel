"""Builds download_center.html: every file in edit order, with fresh CDN links + job IDs + saved checkboxes."""
import json, html
p=json.load(open("gen/stills_prompts.json"))
clip=dict(l.split() for l in open("gen/clipurls.tsv"))
still=dict(l.split() for l in open("gen/stillurls.tsv"))
vo=dict(l.split() for l in open("gen/vourls.tsv"))
cj=dict(l.split() for l in open("gen/clipjobs.tsv")); sj=dict(l.split() for l in open("gen/jobs.tsv"))
VOJ={"VO0":"7a76c80d-4184-462c-af8e-52a4254cdf51","VO1":"e739da01-8f75-41a4-ada4-3f0696d1c125","VO2":"0d911ab3-d96d-41fe-aeb3-c7e5cc833763","VO3":"b4f4c79d-ac9e-4af3-b570-d5b4615eedaa","VO3B":"fefdd6d6-79c6-4c8d-9439-1cd303753ef4","VO4":"f6dd8549-f422-46e4-987d-b5a29bb940de","VO5":"9076a362-ab9f-4be4-8fab-67300ca6b5bd"}
SEG=[("VO0","Cold open",60.16),("VO1","The legends",102.96),("VO2","The soldiers",112.96),("VO3","The recipe that kept changing",82.40),("VO3B","Going global",55.28),("VO4","The fight",58.48),("VO5","Close",23.92)]
SDUR={"VO0-S1":10,"VO1-S1":10,"VO2-S1":13,"VO3-S1":9,"VO3B-S1":7,"VO4-S1":9}
MAPS={"VO1":("VO1-C12","MAP1_italy_naples_rome.mp4",8),"VO2":("VO2-C10","MAP2_rome_riccione.mp4",10),"VO3":(None,"MAP3_rome_chicago.mp4",8),"VO3B":("VO3B-C2","MAP4_goes_global.mp4",8)}
scene={x["id"]:x["prompt"].split("16:9. ")[1].split(". ")[0].split(" Food modelled")[0] for x in p}
idx={x["id"]:i for i,x in enumerate(p)}
def fmt(t): return f"{int(t//60)}:{int(t%60):02d}"
def row(kind,name,url,length,job,desc,tc):
    href=html.escape(url) if url else ""
    link=f'<a class="open" href="{href}" target="_blank" rel="noopener">Open</a>' if url else '<span class="pending">Rendering…</span>'
    return (f'<li class="row" data-id="{html.escape(name)}"><input type="checkbox" id="c-{html.escape(name)}" aria-label="Mark {html.escape(name)} as saved">'
            f'<span class="tc">{tc}</span><span class="kind k-{kind.lower()}">{kind}</span>'
            f'<div class="file"><button class="name" type="button" title="Copy filename">{html.escape(name)}</button><span class="desc">{html.escape(desc)}</span></div>'
            f'<span class="len">{length}</span>{link}<span class="job" title="Higgsfield job ID — use it to re-fetch if the link expires">{job[:8] if job else "code"}</span></li>')
secs=[]; t=0.0; total=0
for seg,title,dur in SEG:
    rows=[row("VO",f"E1_{seg}.mp3",vo[seg],f"{dur:.1f}s",VOJ[seg],"Narration (Benji) — audio track",fmt(t))]; total+=1
    items=[]; mp=MAPS.get(seg)
    if mp and mp[0] is None: items.append(("MAP",mp[1],f"maps/{mp[1]}",mp[2],"","Code-rendered map — add city labels"))
    for x in p:
        sid=x["id"]
        if not sid.startswith(seg+"-"): continue
        i=str(idx[sid])
        if "-S" in sid: items.append(("STILL",f"E1_{sid}.png",still.get(i),SDUR[sid],sj[i],scene[sid]))
        else: items.append(("CLIP",f"E1_{sid}.mp4",clip.get(i),5,cj.get(i,""),scene[sid]))
        if mp and mp[0]==sid: items.append(("MAP",mp[1],f"maps/{mp[1]}",mp[2],"","Code-rendered map — add city labels"))
    st=t
    for k,n,u,l,j,d in items:
        rows.append(row(k,n,u,f"{l}s",j,d,fmt(st))); st+=l; total+=1
    secs.append(f'<section><header><h2>{html.escape(title)}</h2><span class="meta">{seg.replace("VO","Part ")} · starts {fmt(t)} · {dur:.0f}s of narration</span></header><ol class="rows">{"".join(rows)}</ol></section>')
    t+=dur+0.75
tpl=open("gen/download_center_template.html").read()
open("download_center.html","w").write(tpl.replace("{{SECTIONS}}","\n".join(secs)).replace("{{TOTAL}}",str(total)))
print(total, "files")
