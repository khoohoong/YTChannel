# MAP INFOGRAPHICS — Build Spec (accurate geography)
### For "The TRUE Origin of Southeast Asia" · 6 animated map shots

**Why this sheet exists:** AI video models (Kling, Seedance, etc.) can't render real geography or
legible labels — they hallucinate coastlines and gibberish text. These six shots must be built
over **real map data** instead. This spec gives you exact coordinates, camera moves, and overlay
directions so the maps are accurate and the labels are crisp.

**Tools (all free / standard):**
- **Google Earth Studio** (studio.google.com/earth) — free, browser-based. Does the camera
  flyovers/zooms over real satellite Earth. Best for the camera motion + accurate geography.
- **After Effects** (or DaVinci Resolve Fusion) — for the overlays GES can't do: animated route
  lines, glowing markers, and text labels. GES has a one-click **"Export for After Effects"** that
  brings the camera + 3D track points in, so labels/routes stick to the right spot on the globe.
- No AE? A motion designer can execute this whole sheet in a couple of hours; it's standard work.

---

## GLOBAL STYLE (keep all 6 consistent)
| Element | Spec |
|---|---|
| **Grade** | Desaturate + darken the Earth basemap ~20–30% so warm routes/markers pop. Deepen ocean toward teal. |
| **Accent** | Warm amber `#E0A44E` → gold `#F0C271` for routes, markers, highlights. |
| **Labels** | Clean sans (match video's caption font), UPPERCASE, ~2–4% letter-spacing, subtle soft shadow, thin leader line/tick to the point. Fade in over ~0.5s. |
| **Route lines** | 2–3px amber with soft outer glow, animated draw-on (AE "Trim Paths"). Optional small moving dot at the leading tip. |
| **Markers** | Amber dot with 2–3 pulsing concentric rings radiating out. |
| **Motion** | Slow, eased (ease-in/ease-out on every camera keyframe). No linear moves. |
| **Format** | 3840×2160 (or 1920×1080), 16:9, matched to the rest of the cut. |

**Reusable coordinate table** (lat, lon — negative = S/W):
| Place | Lat | Lon |
|---|---|---|
| Liang Bua cave, Flores | −8.5314 | 120.4439 |
| Taiwan (east-coast origin) | 22.80 | 121.15 |
| Luzon, Philippines (Cagayan) | 17.60 | 121.70 |
| Borneo (center) | 0.50 | 114.00 |
| Java (center) | −7.50 | 110.00 |
| Malay Peninsula (KL) | 3.14 | 101.70 |
| Madagascar (center) | −18.90 | 46.90 |
| Rapa Nui / Easter Is. | −27.12 | −109.37 |
| Hawaiʻi (Big Island) | 19.60 | −155.50 |
| Aotearoa / NZ (North Is.) | −39.00 | 175.00 |
| Fiji | −17.70 | 178.00 |
| Samoa | −13.80 | −172.00 |
| Angkor | 13.412 | 103.867 |
| Tonlé Sap (center) | 12.90 | 104.00 |

> In Google Earth Studio, set the **camera Target** to the lat/lon below and control framing with
> **Distance** (range from target) + **Tilt**. "Distance" values are approximate — eyeball to taste.

---

## SHOT 1 — "This is Southeast Asia… stranger than you think"
**Duration:** 6s · **Tool:** Google Earth Studio only (+ optional vignette in AE)
**Move:** Start on the whole globe, spin + descend to frame Southeast Asia.
- **Keyframe A (0s):** Target `5, 115` · Distance ~20,000 km · Tilt 0° · heading rotated so the Pacific/Asia face is turning into view.
- **Keyframe B (6s):** Target `5, 115` · Distance ~4,000 km · Tilt 0–15°. SE Asia fills frame.
- **Overlay:** none needed (this is the establishing "reveal"). Optional: a soft amber glow blooms
  over the SE Asia region as you settle. No labels.

## SHOT 2 — "the remote Indonesian island of Flores, Liang Bua cave"
**Duration:** 6s · **Tool:** GES camera + AE marker & label
**Move:** From the Indonesian archipelago, push in and settle on Flores.
- **Keyframe A (0s):** Target `−4, 118` · Distance ~2,500 km · Tilt 15°. (Whole archipelago in view.)
- **Keyframe B (6s):** Target `−8.5314, 120.4439` (Liang Bua) · Distance ~40 km · Tilt 45°.
- **Overlays (AE, appear in last ~3s):**
  - Pulsing amber marker locked to Liang Bua coordinates.
  - Label: **FLORES** (larger) fading in ~0.5s after the island fills frame; then **LIANG BUA CAVE**
    (smaller) with a short leader line to the marker.

## SHOT 3 — "From Taiwan… pushed out into the open ocean… outrigger canoes"
**Duration:** 6s · **Tool:** GES basemap (static-ish) + AE route animation
**Frame:** Hold on Taiwan + the northern Philippines / ISEA.
- **Camera:** Target `18, 121` · Distance ~3,000 km · Tilt 10°. Very slow push-in only.
- **Overlays (AE):**
  - Pulsing marker on **Taiwan** (`22.8, 121.15`), label **TAIWAN** fades in first.
  - 3–4 amber route lines **draw on** curving southward from Taiwan → Luzon → Borneo/Java, staggered
    ~0.3s apart, each with a small moving tip-dot (the "canoes").
  - Keep labels minimal here (TAIWAN only) so it doesn't get busy.

## SHOT 4 — "Madagascar to Rapa Nui… almost every habitable island"
**Duration:** 7s · **Tool:** GES globe + AE route animation (the hero map)
**Frame:** Globe/hemisphere view spanning Indian → Pacific Oceans, centered so both Madagascar and
Rapa Nui are visible (center roughly on `−10, 150`, Distance ~18,000 km, slight rotate).
- **Overlays (AE), animate outward from Island SE Asia:**
  - **Westward arc:** ISEA → **Madagascar** (`−18.9, 46.9`).
  - **Eastward arcs (staggered):** ISEA → Fiji → Samoa → **Rapa Nui** (`−27.12, −109.37`); a branch
    north to **Hawaiʻi** (`19.6, −155.5`); a branch south to **Aotearoa/NZ** (`−39, 175`).
  - Small light-points **ignite** on islands as each route passes them.
  - Labels fade in at the far endpoints only: **MADAGASCAR**, **HAWAIʻI**, **RAPA NUI**,
    **AOTEAROA**. Time each to land as its route arrives.

## SHOT 5 — "ancestors of the Malay, Javanese, Filipino, Polynesian peoples"
**Duration:** 6s · **Tool:** GES basemap + AE region glow & labels
**Frame:** Maritime SE Asia. Target `0, 112` · Distance ~4,000 km · Tilt 10°. Slow drift.
- **Overlays (AE):** four regions gently glow/pulse **one after another**, each with a label fading
  in as it lights:
  1. **MALAY** — Malay Peninsula (`3.14, 101.70`)
  2. **JAVANESE** — Java (`−7.5, 110`)
  3. **FILIPINO** — Philippines (`12.8, 122`)
  4. **POLYNESIAN** — an arrow/line continuing east off-frame toward the Pacific.
  - Optional thin light-lines linking the islands into a "network."

## SHOT 6 — "the Khmer Empire ruled most of mainland Southeast Asia"
**Duration:** 6s · **Tool:** GES basemap + AE territory fill & capital marker
**Frame:** Mainland SE Asia. Target `14, 104` · Distance ~3,500 km · Tilt 10°. Slow push toward Angkor.
- **Overlays (AE):**
  - A warm translucent amber **territory fill spreads/grows** to cover modern Cambodia + much of
    Thailand + southern Laos + southern Vietnam (rough 12th–13th c. Khmer extent). Animate it
    expanding outward over ~3s.
  - Bright radiant **capital marker** pulses at **Angkor** (`13.412, 103.867`) beside **Tonlé Sap**.
  - Labels: **KHMER EMPIRE** (over the territory) and **ANGKOR** (at the marker).

---

## GOOGLE EARTH STUDIO — QUICK-START (if you're new to it)
1. Go to **studio.google.com/earth**, sign in with a Google account, **New Project**, set 16:9 + your
   resolution + frame rate (match the cut, e.g. 24fps) + duration.
2. Move the view to your **Keyframe A** framing → click the small **diamond** on the camera
   attributes to set a keyframe at frame 0.
3. Scrub to the end, move to **Keyframe B** framing → set another keyframe. GES tweens the move.
   Right-click keyframes → **Ease In/Ease Out** for smooth motion.
4. **Render** → choose **Image Sequence** (best quality) *and* tick **Export for After Effects** →
   this gives a `.json` you import in AE via the GES importer so the camera + track points line up.
5. In AE: parent your **markers / labels / route lines** to the imported **3D track nulls** so they
   stick to the correct geographic spot as the camera moves. Style per the GLOBAL STYLE table above.
6. Export each shot as its own clip (5–7s), drop into the timeline where the matching VO line plays.

**Don't want to learn GES/AE?** Hand this sheet to any motion-graphics freelancer — it's a standard
"animated documentary map" job and every coordinate + move is already specified here.

---

## TIMELINE PLACEMENT (where each map goes in the cut)
| Shot | VO line | Segment |
|---|---|---|
| 1 | "This is Southeast Asia… stranger than you think" | A — cold open |
| 2 | "island of Flores… Liang Bua cave" | A — Flores |
| 3 | "From Taiwan… outrigger canoes" | B — Austronesian |
| 4 | "Madagascar to Rapa Nui" | B — Austronesian |
| 5 | "Malay, Javanese, Filipino, Polynesian" | B — Austronesian |
| 6 | "Khmer Empire ruled most of mainland SE Asia" | D — Angkor |

These replace the six failed AI map clips. In `edit_timeline_FINAL.md` they slot alongside the
existing B-roll at those VO beats (use a map shot as the lead visual for the line, then cut to the
photoreal B-roll).
