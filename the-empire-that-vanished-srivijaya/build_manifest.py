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
 # C9-C11, D1-D13, E1-E16 appended when collected
]

MAPS = [
 ("MAP1","maps/map_clips/MAP1_strait_routes.mp4","20s — trade routes converge on the strait"),
 ("MAP2","maps/map_clips/MAP2_srivijaya_network.mp4","20s — the port network lights up (reprise in VO-E)"),
 ("MAP3","maps/map_clips/MAP3_chola_strike.mp4","15s — 1025 Chola fleet vector"),
 ("MAP4","maps/map_clips/MAP4_fall_majapahit.mp4","15s — network dims; Majapahit rises"),
]

def url(ts, jid, ext): return f"{BASE}hf_{DAY}_{ts}_{jid}.{ext}"

if __name__ == "__main__":
    for label, ts, jid, ext, desc in MANIFEST:
        print(f"| {label} | {desc} | `{jid}` | {url(ts,jid,ext)} |")
