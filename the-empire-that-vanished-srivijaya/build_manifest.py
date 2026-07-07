#!/usr/bin/env python3
"""Builds the asset URL table + review/download center for Episode 2 from MANIFEST below.
URL pattern: BASE + hf_20260707_{ts}_{jobid}.{ext}  (CloudFront; expires — job IDs are durable).
Run: python3 build_manifest.py   → writes review_center.html and prints the assets.md table.
"""
BASE = "https://d8j0ntlcm91z4.cloudfront.net/user_30b7CTGiTTJpfv3eHgP4QQtBJ1y/"
DAY = "20260707"

# label, timestamp, job_id, ext, short description
MANIFEST = [
 ("H1","025801","c72400e2-9b88-446d-8809-24e9c6cbb500","mp4","HERO A: diver's hand + gold ring, night torchlight"),
 ("H2","025803","5e29120f-80bd-42e8-8784-183493a65d38","mp4","HERO B: aerial wooden city on the river, golden hour"),
 ("H3","025805","ab245d3e-cb91-46c6-8118-0d9adf858ecf","mp4","HERO C: Chola war fleet in storm light"),
 ("H4","025806","669785a8-9337-41f2-911a-63b253fb03f3","mp4","HERO D: abandoned jetty in dawn mist"),
 ("H5","025808","316b3c54-f7d7-4dc3-a6df-9a60318c61e9","mp4","HERO E: 1910s scholar's desk, lamplight"),
 ("S1","025809","a8fde877-5032-4a86-aca0-3332ed3a6c80","png","STILL A: museum still life of river treasures"),
 ("S2","025811","a5606d60-9705-4160-8afc-078348d526db","png","STILL B: wooden capital vista at dusk"),
 ("S3","025813","5672ae1a-8146-4859-be9b-2b454601fd93","png","STILL C: burning harbour panorama"),
 ("S4","025814","312dbdd7-4a71-4ef2-874e-39b933c4437d","png","STILL D: empty overgrown riverbank"),
 ("S5","025816","63173332-6928-41b7-9b18-e4a6ea837b67","png","STILL E: gold emerging from black silt (key art)"),
 ("A1","025842","ed0dfe42-01c1-4a60-bca6-fb0861175c41","mp4","divers roll backwards off wooden boat, dawn"),
 ("A2","025845","fbb20b5a-a21d-404a-964e-36ffec140a20","mp4","underwater hand finds gold ring in silt"),
 ("A3","025846","fc6d0c39-bb35-4bf9-90b5-be20e62e9f35","mp4","gold rings + beads in weathered palm"),
 ("A4","025848","a3338a84-f630-451c-9a9e-f6d9989e5224","mp4","temple bell hauled dripping from river"),
 ("A5","025851","87dc9012-5d68-4e6b-ab89-405a821ad953","mp4","bronze Buddha on wet boat deck"),
 ("A6","025905","d1a7ea77-73ec-464d-a8f6-329732111130","mp4","jewelled sword hilt macro"),
 ("A7","025907","606f1622-ac49-4972-80a6-253c7652bf92","mp4","aerial: river snaking through jungle, dawn"),
 ("A8","025855","b2ab7b3c-5f13-4006-876c-1eabb511b7a8","mp4","dim archive, lamplight on stones + rubbings"),
 ("A9","025908","478a847b-a2f6-46e0-8259-89714f1d0a75","mp4","modern strait: cargo ships single file"),
 ("A10","025910","976f79b8-27d3-4069-a6cd-991812ca4466","mp4","ancient trading ship heeling under monsoon sky"),
 ("A11","025911","41994c6a-878a-453b-ad17-d06e42354d88","mp4","silk unrolled; saffron + cloves on scales"),
 ("A12","025913","a6206b1e-2f73-4888-bb09-0befca278eea","mp4","sails converging on narrowing channel, sunset"),
 ("A13","025915","a6c4cbc9-7f68-4fc3-9121-3c60663d40f8","mp4","jungle headland over the strait"),
 ("A14","025916","6e8d6199-f004-4583-8ce4-7319a36cc1be","mp4","hands counting coins into lacquered chest"),
 ("A15","025918","64008f88-f173-49d5-ba12-e173cc5aea16","mp4","watchtower silhouette with brazier, dusk"),
 ("B1","025949","e0cb5c1d-e164-491d-869f-c143cf3fa870","mp4","river bend, stilt houses, golden hour"),
 ("B2","025951","4ba535e2-cbe4-4bbc-b199-03bd100bc14c","mp4","floating raft market"),
 ("B3","025953","4ab3039d-19c0-4258-97ca-0669f30a4654","mp4","timber palace hall, torchlight"),
 ("B4","025956","2907f101-0012-47f7-88e7-0abbc2952bc0","mp4","canoes weaving between house stilts"),
 ("B5","025957","21c9bc19-472b-47e1-948b-f3078e59c06f","mp4","war canoes on patrol, spearmen at prows"),
 ("B6","025958","cbb12a95-fbcf-46ad-ab8f-6941252caafa","mp4","monsoon rain wall over harbour"),
 ("B7","025959","cdf72049-0318-46b0-a9b9-eda8ea150c5c","mp4","merchant fleet at anchor, waiting"),
 ("B8","030001","ed35e6e3-5610-46a6-8239-4eee8478f813","mp4","palms bending as the wind shifts"),
 ("B9","030032","b69a5bac-01e0-49b3-a9be-1553ac9ad4b4","mp4","gold panning in jungle stream"),
 ("B10","030010","e1cd02f7-08e2-47ab-a02d-8bc2f9b8be58","mp4","goldsmith at forge, sparks"),
 ("B11","030033","a8025783-84aa-4503-8238-5cb6dd4dfbd3","mp4","Chinese monk at ship's rail (Yijing)"),
 ("B12","030013","a9dedd00-f184-44a3-8024-b78ebca946ef","mp4","stylus inscribing palm-leaf manuscript"),
 ("B13","030016","bf5189a9-b985-471b-abbe-86b24d74a254","mp4","oil lamps along monastery terrace, night"),
 ("B14","030017","e36fd6ad-c5ec-452d-94f8-a2be1fecaf1a","mp4","monks chanting, incense + light shafts"),
 ("B15","030018","835fb891-684a-4fe6-9973-c279e92fef4e","mp4","harbour mast forest at dusk"),
 ("B16","030020","9e6827ec-82ce-4303-8f4a-44ee1fb1755a","mp4","child sprinting down boardwalk"),
 ("C1","030102","c1803a87-0bf1-4383-8353-bb255907e03b","mp4","tax chest sealed with wax"),
 ("C2","030103","b59690b6-497c-409d-becb-7e7b5170dae8","mp4","South Indian temple gopuram, sunrise"),
 ("C3","030105","4d0f7589-7e1d-402b-b318-732334b25111","mp4","shipwrights building massive hull"),
 ("C4","030107","63140700-63e7-41a4-8bef-d939b8890187","mp4","emperor silhouette over war banners"),
 ("C5","030109","fd737ff8-b75a-4a10-8a85-9601ecd837f6","mp4","war fleet cutting open ocean at dawn"),
 ("C6","030111","be662f41-e2c4-4729-a96a-a9e7474b9426","mp4","below deck: oars heaving to drumbeat"),
 ("C7","030113","ebca59ce-9fea-4f58-9365-575b089cb677","mp4","flaming arrows over black water"),
 ("C8","030115","3f196d68-4954-4381-8e2d-a7be6842a6aa","mp4","warehouse collapsing in flames"),
 ("C9","030117","097a9dc5-62d2-491b-ab6e-0116043f02eb","mp4","soldiers hauling treasure through smoke"),
 ("C10","030119","8f8949f6-66b5-48b5-b44a-3e0a0e53d7df","mp4","empty throne in smoke-hazed hall"),
 ("C11","030120","4112f02d-9213-4beb-90c1-e9ea609ab783","mp4","broken mast drifting on grey swell"),
 ("D1","030143","987af407-7f43-43d6-90a2-f80e9e2fb7da","mp4","rival Javanese port booming"),
 ("D2","030145","fabf4eeb-afd2-4f89-93c8-62eb7d803117","mp4","empty berths, weeds in the boardwalk"),
 ("D3","030147","9c46b428-aeb4-4728-9f38-9b7af3223370","mp4","Javanese war fleet enters river mouth (1377)"),
 ("D4","030149","43337dbb-a02e-4373-ae58-56f582f0ebc8","mp4","riverside raid at dusk, torches reflected"),
 ("D5","030151","9965bade-5851-44db-a3d5-a45eccb8cfe4","mp4","river delta aerial, silt plumes"),
 # C9, D6-D13, E1-E16 appended when collected
]

MAPS = [
 ("MAP1","maps/map_clips/MAP1_strait_routes.mp4","20s — trade routes converge on the strait"),
 ("MAP2","maps/map_clips/MAP2_srivijaya_network.mp4","20s — the port network lights up (reprise in VO-E)"),
 ("MAP3","maps/map_clips/MAP3_chola_strike.mp4","15s — 1025 Chola fleet vector"),
 ("MAP4","maps/map_clips/MAP4_fall_majapahit.mp4","15s — network dims; Majapahit rises"),
]

def url(ts, jid, ext): return f"{BASE}hf_{DAY}_{ts}_{jid}.{ext}"

BLOCK_NAMES = {
 "H":"HERO SHOTS (Seedance, 720p — approved keepers get upscaled)",
 "S":"STILLS (Nano Banana, 2K)",
 "A":"BLOCK A — Hook + The Choke Point (VO-A, 1:48)",
 "B":"BLOCK B — The Floating Empire (VO-B, 1:53)",
 "C":"BLOCK C — The Enemy from the West (VO-C, 1:23)",
 "D":"BLOCK D — The Vanishing (VO-D, 1:33)",
 "E":"BLOCK E — The Resurrection + CTA (VO-E, 1:49)",
}

def block_of(label):
    return label[0] if label[0] in "HS" else label[0]

def write_html(path="review_center.html"):
    import html as H
    groups = {}
    for row in MANIFEST:
        groups.setdefault(block_of(row[0]), []).append(row)
    parts = ["""<!DOCTYPE html><html><head><meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>EP2 Srivijaya — Review &amp; Download Center</title>
<style>
 body{background:#0E272E;color:#F4CE86;font-family:Georgia,serif;margin:0;padding:24px;}
 h1{font-size:22px} h2{color:#E0A44E;border-bottom:1px solid #243A40;padding-bottom:6px;margin-top:36px}
 .grid{display:grid;grid-template-columns:repeat(auto-fill,minmax(320px,1fr));gap:16px}
 .card{background:#122E36;border:1px solid #243A40;border-radius:10px;padding:10px}
 .card video,.card img{width:100%;border-radius:6px;background:#000}
 .lbl{font-weight:bold;color:#F4CE86} .desc{font-size:13px;color:#cbb37a;margin:6px 0}
 a{color:#E0A44E} .dl{font-size:13px}
 .note{background:#16323A;padding:12px 16px;border-radius:8px;font-size:14px;line-height:1.5}
</style></head><body>
<h1>THE EMPIRE THAT VANISHED — Episode 2 visual review</h1>
<div class="note">How to review: play each clip. Anything with a glitch, wrong era, gibberish
text, or a broken face — note its label (e.g. "B7 bad") and send the list back. Approved heroes
(H1–H5) get upscaled to full HD before the edit. To save a file: right-click the download link →
"Save Link As…". Links expire after a while — if one dies, the job ID in assets.md re-fetches it.</div>"""]
    for key in ["H","S","A","B","C","D","E"]:
        if key not in groups: continue
        parts.append(f"<h2>{H.escape(BLOCK_NAMES[key])}</h2><div class='grid'>")
        for label, ts, jid, ext, desc in groups[key]:
            u = url(ts, jid, ext)
            media = (f"<video src='{u}' controls muted preload='none'></video>" if ext=="mp4"
                     else f"<img src='{u}' loading='lazy'>")
            parts.append(f"<div class='card'><div class='lbl'>{label}</div>{media}"
                         f"<div class='desc'>{H.escape(desc)}</div>"
                         f"<div class='dl'><a href='{u}' download>download {label}.{ext}</a></div></div>")
        parts.append("</div>")
    parts.append("""<h2>MAPS (rendered in code — also in the repo under maps/map_clips/)</h2>
<div class="note">Maps are local repo files, not CloudFront links — they never expire. Geography
verified against Natural Earth data. Labels get added in the edit.</div>""")
    parts.append("<ul>")
    for name, path_, desc in MAPS:
        parts.append(f"<li><b>{name}</b> — {desc} — <code>{path_}</code></li>")
    parts.append("</ul></body></html>")
    open(path,"w").write("\n".join(parts))
    print(f"wrote {path} ({len(MANIFEST)} assets)")

if __name__ == "__main__":
    for label, ts, jid, ext, desc in MANIFEST:
        print(f"| {label} | {desc} | `{jid}` | {url(ts,jid,ext)} |")
    write_html()
