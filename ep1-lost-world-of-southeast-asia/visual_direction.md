# VISUAL DIRECTION — accurate artist-impression prompt library
# Episode 1 (reboot): The Lost World of Southeast Asia
# Priority per user: ACCURATE artist impressions. Every prompt below is detailed and fact-anchored.

> **Process note (playbook Phase 3):** final shot *counts* are set AFTER the VO is generated and
> measured — clips are a fixed **5s** each, so `clips_needed ≈ segment_seconds ÷ 5`. This file is the
> **prompt library** (the hard part the user asked for now); the shot-count math comes at budget time
> via `tools/shot_budget.py`. Don't fire a big batch before checking `balance`.

## Global rules
- **Style prefix (from SERIES_BIBLE.md), on every photoreal prompt:**
  > "Photorealistic cinematic [shot], [subject + action], [lighting], [camera move], high-end
  >  nature-documentary realism, 4K, no text."
- **Models:** hero = `seedance_2_0` (1080p, 5s, 16:9); B-roll = `kling3_0_turbo` (5s, 16:9);
  stills/artist-impressions = `nano_banana_pro` (16:9, great for detailed reconstructions).
- **Dim/cave/night/underwater/torch prompts →** always pass
  `declined_preset_id: 24bae836-2c4a-48e0-89b6-49fcc0b21612` (kills the "IN THE DARK" hijack).
- **Maps (Sundaland coastline, Taiwan→Pacific routes, Angkor location) → render in CODE**
  (`the-true-origin-of-southeast-asia/maps/render_maps.py` works for any region). NEVER a video model.
  Add all labels/place-names in the editor, not in the generation.
- **Accuracy > drama.** Notes below flag the mistakes a generic model will make. Bake the corrections
  into the prompt and reject takes that get them wrong (Phase 5 review gate).

---

## COLD OPEN
**H0 (hero, seedance):** Photorealistic cinematic aerial push-in, tropical Southeast Asian archipelago
at golden hour — turquoise shallow sea, scattered green jungle islands, coral reefs visible through
clear water, a slow descent toward the water surface, high-end nature-documentary realism, 4K, no text.
**Still S0a (nano_banana_pro):** artist impression, the SAME seascape but sea level dropped ~120 m —
exposed brown-green coastal plains and river channels where sea is now, dawn light. *This is the visual
"reveal" of Sundaland; keep it grounded, not fantasy.*

## SEGMENT 1 — SUNDALAND (the drowned land)
Accuracy notes: Sundaland was **lowland tropical plains + big river systems + rainforest**, joining
Malay Peninsula, Sumatra, Borneo, Java — NOT a desert, NOT snowy tundra, NOT a single volcano island.
Ice Age here = cooler & drier savanna-rainforest mosaic, megafauna present. No modern boats/buildings.
- **S1-a still:** artist impression map-view landscape of Sundaland ~20,000 years ago: vast green
  coastal plain, wide braided rivers, patches of rainforest and open grassland, distant herd of large
  Ice-Age animals, soft overcast light. No text, no modern structures.
- **S1-b B-roll (kling):** low aerial gliding over a wide Ice-Age river winding through tropical
  lowland forest, morning mist, birds lifting off the water, no people, no buildings.
- **S1-c B-roll:** ground level — a small band of Stone-Age hunter-gatherers (bare feet, simple hide
  wraps, wooden spears, dark hair, Southeast-Asian features) walking across open grassy plain toward
  a treeline. Documentary realism, natural overcast light. *No metal, no pottery, no farming.*
- **S1-d hero (seedance):** the sea rising — time-blend of a green plain slowly flooding into shallow
  sea, a lone hill becoming an island, slow high aerial, melancholy soft light. *Show the drowning.*
- **MAP1 (code):** Sundaland shelf highlighted vs modern coastline (present islands overlaid). Labels
  in edit: "Sundaland — Ice Age" / "Today."

## SEGMENT 2 — SULAWESI CAVE ART (oldest story)
Accuracy notes: the real Leang Karampuang panel = a **large red/maroon naturalistic wild pig**
(Sulawesi warty pig, standing in profile) with **three small human-like figures** near/reaching
toward it. Pigment is **red ochre / dark mulberry-red**, hand-painted, on grey-tan limestone with
calcite "popcorn" texture. Do NOT render European-style horses/bison, black charcoal outlines, or
legible letters. It's figurative but simple, not photorealistic animals.
- **S2-a hero (seedance):** slow push through a limestone cave mouth in a green karst tower landscape
  (Maros-Pangkep style jagged limestone hills, Sulawesi), warm daylight shaft entering the cave.
  Pass `declined_preset_id`.
- **S2-b still (nano_banana_pro):** ACCURATE close reconstruction of the cave painting — a red-ochre
  naturalistic wild pig in profile on tan limestone, three small stylized human-like figures beside it
  reaching toward the pig, faded weathered pigment, calcite crust. "artist impression of the 51,000-year-old
  Leang Karampuang panel." No text, no modern art style.
- **S2-c B-roll (kling):** a Stone-Age human hand pressing/dabbing red ochre pigment onto a cave wall
  by dim natural light, close-up, dust in the air. Pass `declined_preset_id`.
- **S2-d B-roll:** karst-tower Sulawesi landscape exterior at dawn, mist between limestone spires,
  slow aerial. (Establishes place before the reveal.)

## SEGMENT 3 — FLORES / THE HOBBITS (Homo floresiensis)
Accuracy notes: *H. floresiensis* = **~1 m tall, small braincase (~grapefruit), no chin, flatter
nose, longer arms, human-like but not modern.** Skin brown, dark hair, mostly hairless body, simple
tools. NOT a fairytale "hobbit" with big hairy feet, NOT a chimp, NOT a modern short person. Dwarf
Stegodon = elephant-relative shrunk to ~pony/cow size, with tusks. Cave = Liang Bua, tall limestone
chamber. Landscape = Flores tropical hills, monsoon forest.
- **S3-a hero (seedance):** interior of a large limestone cave (Liang Bua), excavation light, layered
  earth floor, small skeleton faintly visible in a dig pit, reverent slow dolly. Pass `declined_preset_id`.
- **S3-b still (nano_banana_pro):** ACCURATE paleo-artist impression, full body, a *Homo floresiensis*
  adult standing ~1 m tall beside a normal-height modern human silhouette for scale — small braincase,
  no prominent chin, brown skin, dark hair, holding a simple stone flake tool, neutral museum-reconstruction
  style, soft daylight. Emphasize: realistic hominin, NOT a costume, NOT cute.
- **S3-c B-roll (kling):** two or three of these small humans hunting a **dwarf Stegodon** (cow-sized
  elephant relative with short tusks) at the edge of a monsoon forest, spears of sharpened wood/stone,
  dawn light, documentary realism.
- **S3-d B-roll:** Flores landscape — green volcanic hills, monsoon rainforest, a river valley,
  slow aerial, no modern structures.
- **S3-e still:** the small skull (grapefruit-sized) held in gloved hands, scientific/neutral, studio
  light. (For the "skull the size of a grapefruit" beat.)

## SEGMENT 4 — AUSTRONESIAN VOYAGERS
Accuracy notes: boats = **outrigger canoe** (single hull + one lateral float on booms) and
**double-hull canoe** (two hulls joined, crab-claw sail). Sailors = Austronesian/Island-SE-Asian &
Pacific peoples, brown skin, dark hair, simple woven/bark cloth, tattoos plausible. NOT European
tall ships, NOT Viking longships, NOT lateen dhows, NOT modern yachts. Open ocean, star navigation.
- **S4-a hero (seedance):** wide cinematic shot of a **double-hull outrigger sailing canoe with a
  crab-claw sail** crossing open Pacific ocean at dawn, small crew of Austronesian voyagers, spray off
  the hulls, hopeful forward motion, low camera near the waterline. High-end realism, no text.
- **S4-b B-roll (kling):** close on the **outrigger float and booms** cutting through blue water,
  water detail, rope lashings (no metal fittings).
- **S4-c still (nano_banana_pro):** night scene — a navigator at the stern reading the **stars**,
  pointing, crew resting, bioluminescent wake, accurate starfield. Pass `declined_preset_id`.
  *Artist impression of wayfinding; keep the boat design correct.*
- **S4-d B-roll:** seabirds (frigatebirds/terns) flying low over the canoe toward the horizon at
  sunset — the "follow the birds home" beat.
- **S4-e B-roll:** hands reading ocean **swells** — POV over the side, patterned wave sets bending,
  midday light.
- **MAP2 (code):** Taiwan → Island SE Asia → Pacific fan-out to Rapa Nui, and westward arrow to
  Madagascar. Amber route lines on the bible palette. Labels in edit only.

## SEGMENT 5 — ANGKOR (the city the jungle ate)
Accuracy notes: **Angkor Wat = five lotus-bud towers (a quincunx), long moat, western causeway,
sandstone grey, bas-relief galleries.** Don't render a generic Hindu/Thai temple, gold onion domes,
or a step-pyramid. City = sprawling low wooden houses + huge rectangular **barays** (reservoirs) +
canals, NOT stone skyscrapers. Decline = strangler-fig roots over stone (Ta Prohm look). Khmer people,
period dress.
- **S5-a hero (seedance):** grand slow aerial approach to **Angkor Wat at sunrise** — five lotus-bud
  towers, wide reflecting moat, stone causeway, jungle beyond, golden mist. Iconic and accurate.
- **S5-b still (nano_banana_pro):** artist impression of Greater Angkor **at its height ~800 years
  ago** — a vast city of wooden stilt houses and canals around the great temples, huge rectangular
  reservoir (baray) shining, markets, thousands of people, elephants, aerial view. Alive and busy.
- **S5-c B-roll (kling):** ground level in the living city — Khmer people in period dress at a canal-side
  market, temple towers behind, warm daylight, documentary realism.
- **S5-d B-roll:** camera glides along a **bas-relief gallery wall** — carved rows of figures, armies,
  dancers (apsaras), raking side light. (For "carvings that stretch for miles.")
- **S5-e hero (seedance):** the abandonment — a temple tower being overtaken by **strangler-fig roots**
  (Ta Prohm style), vines, moss, shafts of green jungle light, slow reverent push-in.
- **S5-f B-roll:** modern-day empty Angkor Wat in the forest, still standing, dawn, no tourists —
  the "still waiting in the forest" closing image.
- **MAP3 (code):** small locator — Cambodia/Angkor on the SE Asia mainland. Label in edit.

## OUTRO
- Reuse H0 / S5-f as bookends (intentional callback within the episode — allowed).
- **S-out still:** the warm turquoise sea from the cold open, camera tilting down toward the water —
  visually rhymes with "the next discovery might be waiting under that sea right now."

---

## ACCURACY REVIEW CHECKLIST (Phase 5 gate — reject takes that fail)
- [ ] Sundaland looks like tropical lowland plains + rivers, not desert/tundra/single volcano.
- [ ] Cave painting is a RED pig + small human figures on limestone — not European cave art, no text.
- [ ] *H. floresiensis* reads as a real small hominin (small braincase, no chin), not a costume/chimp/child.
- [ ] Dwarf Stegodon is elephant-like with tusks, cow/pony-sized — not a full mammoth, not a tapir.
- [ ] Boats are outrigger / double-hull canoes with crab-claw sails — no European/Viking/dhow ships.
- [ ] Angkor Wat has 5 lotus towers + moat + causeway; city has barays + wooden houses, not stone high-rises.
- [ ] All on-screen text, place names, dates, and maps are added in the EDITOR, never generated.
