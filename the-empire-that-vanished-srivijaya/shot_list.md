# SHOT LIST & FOOTAGE BUDGET — Episode 2 (Srivijaya)
### Built 2026-07-07 from MEASURED VO durations. Phase 3 (arithmetic, no spend yet).

## MEASURED VO (source of truth for all timing)
| Block | Content | Measured | Job ID |
|---|---|---|---|
| VO-A | Hook + Choke Point | **108.2s** (1:48) | `8014b01e…` |
| VO-B | The Floating Empire | **112.9s** (1:53) | `bf23bed2…` |
| VO-C | The Enemy from the West | **82.8s** (1:23) | `f76a2355…` |
| VO-D | The Vanishing | **93.4s** (1:33) | `da880b12…` |
| VO-E | The Resurrection + CTA | **109.4s** (1:49) | `a277723c…` |
| **TOTAL** | | **506.6s = 8:27** | |

## COVERAGE PLAN (every second covered at 1×, no stretched clips — Ep 1's lesson)
Maps are code-rendered (free, hold 15–20s animated). Stills hold ~10s Ken Burns. Clips are 5s.

| Block | VO | Map hold | Still | Hero | Reuse | B-roll needed |
|---|---|---|---|---|---|---|
| A | 108s | MAP1 20s | S1 10s | H1 5s | — | 73s → **15 clips** |
| B | 113s | MAP2 20s | S2 10s | H2 5s | — | 78s → **16 clips** |
| C | 83s | MAP3 15s | S3 10s | H3 5s | — | 53s → **11 clips** |
| D | 93s | MAP4 15s | S4 10s | H4 5s | — | 63s → **13 clips** |
| E | 109s | MAP2r 10s | S5 10s | H5 5s | H1r 5s | 79s → **16 clips** |

**TO GENERATE: 71 Kling B-roll + 5 Seedance heroes + 5 Nano Banana stills. 4 maps rendered in code.**
**Rough cost: 71 × 7.5 ≈ 533 credits (Kling) + 5 heroes + 5 stills ≈ ~575–650 credits total.**
(Balance at check: 4,862 — comfortable. Preflight each model's exact cost with `get_cost` before firing.)

---

## MAPS — render in code (`../the-true-origin-of-southeast-asia/maps/render_maps.py`, bible palette, NO text; labels in edit)
- **MAP1** (VO-A): Strait of Malacca choke point; amber trade-route arcs China↔India converging into the strait.
- **MAP2** (VO-B, reprised VO-E): Srivijaya network at height — gold glow on Palembang + port nodes along Sumatra/Malay Peninsula coasts.
- **MAP3** (VO-C): Chola strike — amber fleet vector crossing the Bay of Bengal from south India to the strait ports.
- **MAP4** (VO-D): the network dimming node by node; Majapahit glow rising from Java; arrow to Palembang (1377).

## HERO SHOTS — Seedance 2.0, 1080p, 5s, 16:9. Style prefix (bible) on all. ⚠ = add `declined_preset_id`
- **H1** (A, reprise E) ⚠: diver's hand bursting from dark river water clutching a gold ring, torchlight from a wooden boat above, night.
- **H2** (B): sweeping aerial at golden hour over a vast wooden city on water — stilt houses, raft markets, hundreds of sails on a brown river.
- **H3** (C): massive medieval Indian war fleet bearing down through storm light, sails full, spray off the bows.
- **H4** (D): abandoned wooden jetty dissolving into jungle river mist at dawn, rotting pilings, absolute stillness.
- **H5** (E) ⚠: lamplit 1910s scholar's desk covered in stone rubbings and manuscripts, slow push-in, dust motes in the light.

## STILLS — Nano Banana Pro, 16:9 (Ken Burns ~10s each)
- **S1** (A): recovered river treasures laid on dark cloth — rings, beads, small bells — museum-lit.
- **S2** (B): grand wide vista of the wooden capital at dusk, monastery lamps beginning to glow.
- **S3** (C): panoramic burning harbour at night seen from the water, reflections of fire. ⚠ mood
- **S4** (D): overgrown empty riverbank where a city once stood — a single carved post remains.
- **S5** (E): key art — golden artifacts emerging from black river silt, one shaft of light.

## B-ROLL — Kling 3.0 turbo, 5s, 16:9. Style prefix on all. ⚠ = bake in `declined_preset_id: 24bae836-2c4a-48e0-89b6-49fcc0b21612`

### Block A (15) — divers & the choke point
- A1 ⚠ murky brown river surface at first light, small wooden boat, two divers rolling backwards into the water
- A2 ⚠ underwater in near-zero visibility, a hand feeling through silt closes on a gold ring
- A3 macro: mud-crusted gold rings and beads rolling in a weathered open palm
- A4 bronze temple bell hauled dripping from river mud on a rope
- A5 small bronze Buddha figure set gently on a wet boat deck, river bokeh behind
- A6 close-up jewelled sword hilt turning in the light, water beading off gold
- A7 slow aerial: an immense brown river snaking through green jungle at dawn
- A8 ⚠ dim archive room, lamplight over old inscribed stones and paper rubbings
- A9 high aerial of a modern strait shipping lane, giant vessels in a single-file line to the horizon
- A10 ancient lateen-sailed trading ship heeling under monsoon clouds
- A11 close-ups: bolts of silk unrolled, saffron and cloves poured across a merchant's scale
- A12 dozens of period sails converging toward a narrowing channel at sunset
- A13 jungle headland overlooking the strait, waves breaking far below
- A14 hands counting silver coins into a lacquered chest on a wooden wharf
- A15 ⚠ silhouette of a wooden watchtower over dark water at dusk, brazier flame

### Block B (16) — the floating empire
- B1 wide river bend at golden hour, stilt houses lining both banks
- B2 raft market: fruit, fish and rice changing hands boat-to-boat
- B3 ⚠ carved timber palace interior, torchlight on gilded wood
- B4 slender canoes weaving between house stilts, paddles flashing
- B5 war canoes in formation on patrol, spearmen silhouetted at the prows
- B6 a wall of monsoon rain advancing across a harbour
- B7 a fleet of merchant ships riding at anchor, sails furled, waiting
- B8 palms bending as the wind shifts, clouds racing in a changing sky
- B9 gold panning in a jungle stream, glittering dust swirling in the pan
- B10 ⚠ goldsmith at a forge hammering a bracelet, sparks in the dark
- B11 a robed Chinese monk at a ship's rail, robes and prayer beads in the wind
- B12 stylus inscribing palm-leaf manuscript, close on the strokes
- B13 ⚠ hundreds of oil lamps flickering along a riverside monastery at night
- B14 rows of monks chanting in incense haze, shafts of morning light
- B15 ⚠ harbour panorama at dusk — a forest of masts against the afterglow
- B16 a child sprinting down a long boardwalk between stilt houses, pure daily life

### Block C (11) — the Chola strike
- C1 a tax chest of coins slammed shut and sealed with wax
- C2 towering South Indian temple gopuram at sunrise, birds circling
- C3 shipwrights swarming a massive hull, mallets driving pegs
- C4 an emperor's silhouette on a palace balcony above war banners
- C5 a war fleet cutting open ocean at dawn, bows throwing spray
- C6 ⚠ below deck: oars heaving in unison to a drumbeat in the dark
- C7 ⚠ night battle: flaming arrows arcing over black water
- C8 ⚠ a harbour warehouse collapsing in fire, embers spiralling up
- C9 soldiers hauling treasure chests through drifting smoke
- C10 ⚠ an empty carved throne in a smoke-hazed hall
- C11 a single broken mast drifting on grey morning swell

### Block D (13) — the vanishing
- D1 a rival port bustling — cranes of timber, new warehouses, crowds
- D2 empty berths and a sparse market, weeds between boardwalk planks
- D3 a Javanese war fleet entering a wide river mouth, banners streaming
- D4 ⚠ raid at dusk: torch flames and spear silhouettes reflected in the water
- D5 aerial of a river delta, brown sediment plumes curling into the sea
- D6 waterline far from old dock pilings, mudflats where harbour was
- D7 a rotting pier sagging into green water, moss on every beam
- D8 vines tightening over a carved wooden post, time-worn
- D9 macro: sodden woodgrain crumbling to fibres and mud
- D10 tropical rain dissolving a mud bank into a swollen river
- D11 modern kids fishing off a concrete jetty on the Musi, laughing, unaware
- D12 dawn mist lying on a completely silent river
- D13 a single blackened pillar stump alone in a tidal mudflat

### Block E (16) — the resurrection
- E1 ⚠ imperial Chinese archive: scroll unrolled under lantern light, brush characters
- E2 an inscribed stone stele in a jungle clearing, raking golden light on the script
- E3 paper pressed over carved letters, charcoal rubbing bringing them up
- E4 ⚠ a 1910s study at night: green-shaded lamp, magnifier over documents
- E5 overhead: hands arranging paper fragments until edges align
- E6 close on a scholar's eyes widening behind round spectacles (generic figure, no likeness)
- E7 ⚠ dredging crane silhouetted on the river at dusk, bucket rising
- E8 diver back-rolling off a narrow wooden boat into brown water
- E9 a hand breaking the surface holding a coin, sun flaring through droplets
- E10 gloved hands laying rings, beads and bells onto a museum tray
- E11 ⚠ macro: a gold artifact rotating against black, catching a single light
- E12 ⚠ wide dusk shot: modern Palembang lights reflected on the Musi
- E13 ⚠ lantern boats drifting on dark water
- E14 ⚠ an ancient brick tower silhouette against a blood-red dusk sky (Champa tease)
- E15 a wave sliding up sand, erasing lines of writing scratched there
- E16 a child holding a tiny gold bead up to the sun, wonder on their face

## EDIT ORDER NOTE
Every row of the eventual timeline = one real asset at its real length (5s clips, 10s stills,
15–20s maps). Intentional reuse ONLY: H1 reprise + MAP2 reprise in VO-E. Timeline built in
Phase 6 after Phase 5 review.
