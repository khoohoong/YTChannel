# Animated map infographics — accurate, code-rendered

Six animated map clips for the documentary, rendered from **real Natural Earth coordinate data**
(not AI video). Geography is accurate; there is intentionally **no text** — add clean labels in
your editor where they'll be crisp and correctly timed.

## The clips (`clips/`, 1920×1080)
| File | Script moment | Segment | Length |
|---|---|---|---|
| `MAP1_sea_reveal.mp4` | "This is Southeast Asia… stranger than you think" | A cold open | 6s |
| `MAP2_flores_zoom.mp4` | "island of Flores… Liang Bua cave" (pulsing marker on Flores) | A | 6s |
| `MAP3_taiwan_routes.mp4` | "From Taiwan… outrigger canoes" (routes fan south) | B | 6s |
| `MAP4_ocean_spread.mp4` | "Madagascar to Rapa Nui" (routes across two oceans) | B | 7s |
| `MAP5_maritime_peoples.mp4` | "Malay, Javanese, Filipino, Polynesian" (regions glow) | B | 6s |
| `MAP6_khmer_empire.mp4` | "Khmer Empire ruled mainland SE Asia" (territory + Angkor) | D | 6s |

## Style
Dark teal ocean, warm land, faint graticule, amber/gold routes + markers — tuned to sit alongside
the photoreal B-roll. Add labels (FLORES, TAIWAN, MADAGASCAR, ANGKOR, etc.) as overlays in the edit.

## Re-rendering / tweaking
Everything is reproducible:
```
pip install matplotlib numpy imageio imageio-ffmpeg
python3 render_maps.py all      # or a single shot: python3 render_maps.py 4
```
- `render_maps.py` — the renderer. Colors are constants near the top (OCEAN/LAND/AMBER/GOLD…);
  each shot is its own function (`shot1`…`shot6`) with camera framing, routes, and timing.
- `ne_50m.geojson` — Natural Earth 1:50m country boundaries (the accurate geometry). Source:
  https://github.com/nvkelso/natural-earth-vector (public domain).
- Output lands in `map_clips/` next to the script; copy into `clips/` to keep the committed set.

Common tweaks: change a shot's `ax.set_xlim/ylim` to reframe; edit the `dests` lists in shot3/shot4
to change route endpoints; adjust `terr` in shot6 for the empire extent; change durations via the
`N=int(<seconds>*FPS)` line in each shot.
