"""Ep 1 v2 (full remake) — word-synced shot list. Times = Whisper word starts in v2/vo_words.json.
Row: (start_s, id, scene for the clay still, motion for the stop-motion clip). "MAP:<file>" rows reuse code maps."""
N = "a cheerful plump clay Italian grandmother with grey bun, round glasses and floral apron"
C = "a friendly clay historian with short dark beard, round glasses and brown tweed jacket"
K = "a young clay Italian cook in white jacket and chef's cap"
G = "clay 1940s American soldiers in olive uniforms"
SHOTS = {
"S0": [
 (0.00,"a", f"{N} proudly presenting a plate of spaghetti carbonara in a rustic Roman kitchen", "She lifts the plate proudly and nods"),
 (3.48,"b", "close-up of clay hands cracking a golden egg into a bowl of yolks", "The egg cracks and the yolk drops in"),
 (4.06,"c", "close-up of crisp guanciale strips sizzling in a small iron pan", None),
 (5.00,"d", "a wedge of pecorino being grated into a snowy pile", None),
 (6.28,"e", "a wooden pepper mill grinding black pepper over spaghetti carbonara", None),
 (7.50,"f", f"{N} recoiling in horror from a carton of cream on the counter, hands up", "She recoils and pushes the cream carton away"),
 (10.98,"g", "a clay kitchen wall covered in old framed portraits of generations of Italian grandmothers, a plate of carbonara on the table below", "Slow push in, the portraits wobble slightly"),
 (14.80,"h", f"{C} opening a huge dusty old cookbook in a library, the pages completely blank", "He opens the book, dust puffs up, he looks surprised"),
 (21.40,"i", "an empty white plate on a wooden table with a large red clay question-mark sculpture standing on it", "The question mark wobbles"),
 (23.54,"j", f"{G} riding in a jeep past ochre Roman buildings", "The jeep rolls forward"),
 (25.42,"k", "a small 1950s paperback guidebook with a plain blank cover lying on an American diner counter next to a coffee cup", "Steam rises from the coffee, slow push in"),
 (27.50,"l", f"{C} smiling nervously while an angry clay crowd behind him waves forks", "The crowd shakes their forks, he shrugs"),
],
"S1": [
 (0.00,"a", f"portrait of {C} in a cosy study lined with old cookbooks, holding a book", "He adjusts his glasses and smiles"),
 (3.94,"b", f"{C} examining different pasta shapes laid out on a wooden table with a magnifying glass", "He moves the magnifying glass over the pasta"),
 (7.66,"c", f"{C} climbing a tall library ladder beside towering shelves of old books", "He climbs one rung and reaches for a book"),
 (10.74,"d", "a tall wobbly stack of antique leather cookbooks on a desk, one open on top with blank pages, a candle beside", "A page turns, the candle flickers"),
 (15.64,"e", "an old Italian farmhouse kitchen, clay hands mixing beaten eggs and grated cheese into a bowl of hot pasta", "The hands toss the pasta"),
 (20.10,"MAP:MAP1_italy_naples_rome.mp4", None, None),
 (26.26,"f", "a clay 19th-century Neapolitan nobleman in a frock coat tossing pasta with eggs and cheese in an elegant old kitchen", "He tosses the pasta with a flourish"),
 (30.44,"g", f"close-up of {C} raising one eyebrow knowingly at the camera, holding an old recipe book", "He raises an eyebrow and taps the book"),
 (32.50,"h", "green hills outside Rome with a small stone shepherd's hut, a clay shepherd cooking pasta in a pan outside", "The shepherd stirs the pan, smoke rises"),
 (36.26,"i", "a slab of cured pork jowl, a wedge of pecorino and a pepper mill lined up on a rustic board", None),
 (40.36,"j", "a ripe tomato dropping into a pan of pasta with guanciale, sauce turning red", "The tomato drops in and the sauce turns red"),
 (44.06,"k", "a clay hand holding an egg above a pan of pasta with guanciale and pecorino, about to crack it", "The hand hovers the egg and pauses"),
 (48.56,"l", "a nearly complete jigsaw puzzle on a table whose pieces show an egg, pork, cheese, pepper and pasta, one piece missing", "A piece slides toward the gap but stops"),
 (52.22,"m", f"{C} flipping through an old cookbook at a desk looking puzzled, more books piled around", "He flips pages and scratches his head"),
 (57.98,"n", "a blank recipe card, a blank restaurant menu and a blank open cookbook laid side by side on a table", "Slow push in"),
 (63.00,"o", "a 1930s Roman kitchen, a clay housewife reading a thick cookbook at the table", "She turns a page"),
 (69.94,"p", "the 1930s clay housewife running her finger down a blank index page and shrugging", "She runs her finger down the page and shrugs"),
 (71.78,"q", "a shiny silver spoon resting on a thick 1950s cookbook with a plain cover on a kitchen shelf", "Light glints on the spoon, slow push in"),
 (76.90,"r", f"{C} closing a thick cookbook with a sigh, dust rising", "He closes the book, dust puffs"),
 (78.66,"s", "clay medieval monks at a long refectory table comically eating spaghetti, like an imagined legend", "The monks twirl spaghetti"),
],
"S2": [
 (0.00,"a", f"{N} telling a story to wide-eyed clay children by a fireplace", "She gestures as she tells the story"),
 (3.78,"b", "clay woodsmen beside a smouldering charcoal mound in a mountain forest", "Smoke curls up, a woodsman wipes his brow"),
 (7.76,"c", "clay charcoal burners cooking a pot of pasta over a campfire in the mountains", "They stir the pot, the fire flickers"),
 (13.60,"d", "hooded clay figures in 19th-century coats meeting secretly around a candlelit table", "They lean in, candles flicker"),
 (17.80,"e", "two hooded clay conspirators sharing a plate of pasta by candlelight", "They clink forks"),
 (21.06,"f", "extreme close-up of black pepper flakes falling onto pasta like specks of coal dust", None),
 (26.20,"g", "three closed fairy-tale storybooks stacked on a table with a blank recipe card resting on top", "Slow push in on the blank card"),
 (29.60,"h", f"{C} at his desk looking up thoughtfully, a clay question mark floating above an empty plate", "He looks up and the question mark wobbles"),
],
"S3": [
 (0.00,"a", "a miniature clay Rome skyline with domes at dawn, early summer light", "Slow push in, birds drift"),
 (2.94,"b", "clay army jeeps rolling down a Roman street past cheering clay crowds", "The jeeps roll forward, the crowd waves"),
 (5.08,"c", "clay Roman townspeople gathering around an army truck handing out food", "People reach up, a soldier hands down a loaf"),
 (9.06,"d", f"{G} unloading plain wooden supply crates from a truck", "A soldier sets a crate down"),
 (10.88,"e", "an opened plain wooden crate packed with slabs of bacon", "The lid lifts to reveal the bacon"),
 (14.34,"f", "a slab of bacon beside a plain unlabeled tin with yellow powdered egg spilling out", None),
 (17.98,"g", "a grinning clay American soldier with a breakfast plate of bacon and fried eggs in a mess tent", "He lifts his fork happily"),
 (20.24,"h", "a puzzled clay Italian family looking at a plate of bacon and eggs placed next to a bowl of plain pasta", "They look from one plate to the other"),
 (25.80,"i", f"{K} standing in a small Roman trattoria kitchen, thinking", "He taps his chin"),
 (28.40,"j", f"hungry {G} peeking through a trattoria doorway", "They lean in and sniff the air"),
 (30.20,"k", "a big pot of spaghetti boiling on an old stove, steam rising", None),
 (32.14,"l", "a pile of bacon and a bowl of eggs on a trattoria counter next to dry spaghetti", None),
 (34.66,"m", f"{K} tossing spaghetti with egg and bacon in a pan, a glowing clay light bulb above his head", "He tosses the pan, the bulb flickers on"),
 (38.26,"n", "a finished plate of carbonara between an Italian copper pan and a plain wooden army crate", "Steam rises, slow push in"),
],
"S4": [
 (0.00,"MAP:MAP2_rome_riccione.mp4", None, None),
 (5.12,"a", "a young clay chef in whites standing proudly on a 1940s Adriatic seaside promenade", "He straightens his cap, waves roll behind"),
 (9.72,"b", "clay British and American officers seated at a long white lunch table on a seaside villa terrace", "They chat and raise glasses"),
 (14.24,"c", "an elderly clay chef in an armchair telling a story with big gestures", "He gestures grandly"),
 (18.32,"d", "bacon, a jug of cream, a wedge of cheese and a tin of powdered egg yolk lined up on a table", None),
 (23.76,"e", "the young clay chef tossing pasta in a pan and grinding black pepper over it in a villa kitchen", "He tosses the pan and grinds pepper"),
 (27.86,"f", f"{C} reading a thick memoir with a magnifying glass, looking doubtful", "He moves the magnifying glass and frowns"),
 (31.56,"g", "a 1940s lunch table set with roast meat, soup and dessert but no pasta, an empty space in the middle", "Slow push in on the empty space"),
 (34.86,"h", "a storybook closing by itself on a table, a red clay question mark resting on its cover", "The book closes, the question mark wobbles"),
 (38.00,"i", "calendar pages flying off a wall calendar in a breeze, pages blank", "Pages flutter away"),
 (40.96,"j", "a folded 1950 newspaper with blank grey placeholder columns on a café table beside an espresso", "Steam rises, slow push in"),
 (43.68,"k", "a clay newsboy in a cap holding up newspapers on a 1950 street with arcades", "He waves a newspaper"),
 (45.54,"l", "a narrow cobbled Trastevere street at dusk with hanging lanterns and laundry lines", "Lanterns sway"),
 (49.68,"m", "a cosy clay trattoria front in Trastevere with warm windows and a blank sign", "The door swings open"),
 (51.70,"n", f"{G} officers at a trattoria doorway asking the waiter for something", "An officer gestures, the waiter nods"),
 (55.38,"o", "a clay waiter presenting a plate of spaghetti carbonara with a flourish", "He presents the plate"),
 (57.92,"p", "a magnifying glass over a newspaper column of blank grey blocks", "The magnifying glass slides along"),
 (63.02,"q", f"{G} happily eating spaghetti at a table while {N} watches through the window with arms folded", "The soldiers eat, she taps her foot"),
 (66.46,"r", "a detective cork board with a blank newspaper clipping pinned and red string leading away", "The string tightens"),
 (68.58,"s", "a clay ocean liner crossing blue felt waves with a giant pasta pot strapped on deck", "The ship bobs across the waves"),
 (72.04,"t", "an old printing press printing blank booklets", "The press stamps and a booklet slides out"),
 (75.10,"MAP:MAP3_rome_chicago.mp4", None, None),
 (82.46,"u", "a small 1950s paperback guidebook with a plain cover on a diner counter, a hand opening it", "The hand opens the cover"),
 (85.30,"v", "a cosy 1950s Italian restaurant storefront in Chicago with striped awning and blank sign, overhead railway behind", "The door opens, warm light spills out"),
 (90.18,"w", "a clay Italian-American couple, restaurant owners in aprons, proudly standing by a framed picture of Tuscan hills", "They smile and nod"),
 (92.86,"x", "a nest of thin egg noodles, strips of bacon, a wedge of parmesan and three eggs lined up on a diner counter", None),
 (98.44,"y", "a piece of guanciale and a wedge of pecorino standing sadly behind a red velvet rope", "They slump"),
 (101.14,"z", "an open guidebook showing a picture of a pasta dish and blank placeholder lines, a plate of bacon-and-egg noodles beside it", "Slow push in"),
],
"S5": [
 (0.00,"a", "a paper airmail envelope flying over clay ocean waves towards Italy", "The envelope glides across"),
 (3.34,"b", "a 1950s Italian newsstand with rows of magazines with plain covers", "The vendor hangs up a magazine"),
 (5.38,"c", "a clay 1950s Italian woman opening a food magazine at her kitchen table", "She opens the magazine"),
 (9.48,"d", "the clay 1950s woman looking surprised at the magazine, eyebrows raised", "Her eyebrows shoot up"),
 (12.54,"e", "cubes of pancetta on a wooden board", None),
 (14.46,"f", "a single garlic clove on a wooden board, spotlight", None),
 (16.24,"g", "a wedge of Swiss Gruyère cheese on a board with a tiny red-and-white cross toothpick flag", None),
 (19.26,"h", "a 1950s magazine office, clay editors proudly holding up a plain-cover magazine", "They hold it up proudly"),
 (22.70,"i", "a happy clay 1950s Italian family eating pasta together, everyone smiling", "They eat and laugh"),
 (27.88,"j", "a wall clock with spinning hands in a kitchen that is half 1950s and half modern", "The clock hands spin"),
 (31.82,"k", f"{C} cooking in a modern kitchen with a smartphone on a tripod filming him", "He stirs a pan and glances at the phone"),
 (35.56,"l", "a smartphone on a tripod recording a pan of pasta with garlic and Swiss cheese, red record light", "The record light blinks"),
 (36.98,"m", "a smartphone lying on a table with clay heart and eye icons bursting out of the screen", "Icons pop out one after another"),
 (40.20,"n", "an angry clay crowd of Italians waving forks and wooden spoons", "They shake their forks"),
 (42.50,"o", "clay smartphones buzzing with angry red speech bubbles containing little flame icons", "The bubbles pop up angrily"),
 (44.82,"p", f"{N} holding up a garlic clove in outrage", "She shakes the garlic"),
 (47.42,"q", f"{N} fainting onto a chair at the sight of a holey Swiss cheese wedge", "She sways and faints into the chair"),
 (51.72,"r", f"{C} calmly shrugging, holding an old magazine in one hand", "He shrugs with a small smile"),
 (56.00,"s", "an old open magazine beside a plate of pasta with pancetta, garlic and melted Swiss cheese", "Steam rises, slow push in"),
],
"S6": [
 (0.00,"a", "a clay 1950s British woman writer at a desk with a typewriter and a plate of pasta", "She types"),
 (4.20,"b", "a plain-cover cookbook on an English kitchen table beside a teapot and a plate of spaghetti", "Steam rises from the teapot"),
 (7.54,"c", "a vintage suitcase with a pasta pot strapped on top arriving at a foreign harbour", "The suitcase rolls along the dock"),
 (10.06,"d", "a big jug of cream pouring generously into a pan of pasta", None),
 (12.92,"MAP:MAP4_goes_global.mp4", None, None),
 (19.38,"e", "clay tourists with cameras ordering at an outdoor Roman trattoria", "They point at the menu, the waiter nods"),
 (23.98,"f", "three pasta plates on a small winners podium: fettuccine Alfredo on top, lasagne second, carbonara third", "A spotlight sweeps across"),
 (26.96,"g", "a blank paper wall calendar in a kitchen with a carbonara plate drawn as a simple clay magnet", "Slow push in"),
 (30.54,"h", "a clay street party with blank bunting, people cheering around a giant plate of carbonara, confetti", "Confetti falls, people cheer"),
 (34.06,"i", "two clay people on a sofa scowling at their phones, cream carton and egg icons in speech bubbles", "They tap furiously, bubbles pop up"),
],
"S7": [
 (0.00,"a", "blank recipe cards hanging on a clothesline across an Italian kitchen", "The cards flutter"),
 (3.00,"b", "a slab of guanciale stepping onto a tiny stage beside a thick 1960s cookbook, spotlight", "The guanciale hops into the spotlight"),
 (8.52,"c", "a white wedge of pecorino pushing a golden wedge of parmesan off a cheese board", "The pecorino nudges the parmesan off"),
 (11.62,"d", "a jug of cream sitting innocently on a 1970s Italian kitchen counter", None),
 (12.76,"e", "a 1970s Italian kitchen, a clay cook pouring cream into a pan of carbonara", "The cook pours the cream"),
 (16.54,"f", f"{N} covering her eyes with both hands", "She covers her eyes and peeks"),
 (18.90,"g", "a distinguished elderly clay chef in a very tall white toque in an elegant restaurant kitchen", "He adjusts his toque proudly"),
 (24.26,"h", "the distinguished clay chef in tall toque receiving applause in a grand dining room", "Diners applaud, he bows slightly"),
 (27.46,"i", "the distinguished clay chef in tall toque pouring a large jug of cream into a pan of spaghetti", "He pours the cream generously"),
 (31.06,"j", f"{N} with her jaw dropped, watching", "Her jaw drops"),
 (33.98,"k", "the distinguished clay chef presenting a creamy plate of carbonara with a bow", "He bows with the plate"),
 (36.56,"l", "a clay boot kicking a carton of cream out of a kitchen door", "The boot kicks the carton out"),
 (39.32,"m", "a clay stone tablet being chiselled with four simple pictograms: egg, pork, cheese, pepper", "The chisel taps, dust falls"),
 (43.22,"n", "an egg, a piece of guanciale, a wedge of pecorino and a pepper mill lined up proudly on a table", None),
 (48.06,"o", "a plate of carbonara with birthday candles stuck in it, clay party hats around", "The candles flicker"),
],
"S8": [
 (0.00,"a", f"{N} guarding a plate of carbonara with a rolling pin", "She raises the rolling pin protectively"),
 (2.90,"b", "a clay professor with grey beard speaking at a lectern", "He gestures as he speaks"),
 (6.86,"c", "a salmon-pink newspaper with blank placeholder columns on a desk", "Slow push in"),
 (8.38,"d", "a plate of carbonara with a tiny star-spangled toothpick flag stuck in it", "The flag wobbles"),
 (11.92,"e", "clay officials in suits carrying a huge thick dossier up the steps of a grand building", "They heave the dossier up a step"),
 (16.44,"f", "the clay professor and the clay officials bumping into each other on the steps, papers flying", "They collide, papers fly"),
 (18.96,"g", "a slice of tiramisù and a panettone side by side looking shocked, with little clay eyes", "They jump in surprise"),
 (25.36,"h", "clay Italian farmers in a field protesting with forks of spaghetti", "They wave their forks"),
 (31.04,"i", "a generic clay politician in a suit gesturing at a podium with microphones, no flags", "He gestures passionately"),
 (33.24,"j", "a clay TV news studio, the screen behind the presenter showing a plate of pasta", "The presenter gestures to the screen"),
 (37.32,"k", "a grand international assembly hall with clay delegates applauding", "The delegates applaud"),
 (41.06,"l", "a long banquet table covered with dozens of different Italian dishes glowing in warm light", "Slow push along the table"),
 (45.48,"m", "a small plate of carbonara among many other Italian dishes, unlabelled, one of the crowd", "Steam rises"),
 (49.40,"n", f"a seesaw with {N} on one side and {C} on the other, perfectly balanced", "The seesaw tips gently back and forth"),
],
"S9": [
 (0.00,"a", f"{N} and {C} shaking hands over a plate of carbonara", "They shake hands and smile"),
 (1.70,"b", "close-up of clay hands tossing spaghetti into a silky golden egg-and-cheese sauce", "The hands toss the pasta"),
 (3.96,"c", "an 1800s Italian kitchen, a clay cook tossing pasta with eggs and cheese by candlelight", "The cook tosses the pasta"),
 (7.90,"d", f"{K} and a clay 1940s American soldier cooking together at a stove", "The cook stirs, the soldier hands him bacon"),
 (11.82,"e", "a plain army crate of bacon and eggs being set down next to an Italian copper pan of pasta", "The crate is set down beside the pan"),
 (14.94,"f", "a clay Italian woman food writer at a desk with notebook and a plate of carbonara", "She writes and smiles"),
 (18.44,"g", f"{K} shaking hands with a clay 1940s American soldier over a plate of carbonara", "They shake hands warmly"),
 (21.80,"h", "clay grandparents smiling at a plate of carbonara that has one birthday candle", "They smile, the candle flickers"),
 (25.76,"i", "a tableau on a table: an army helmet, a small guidebook, an old magazine and two crossed forks around a plate of carbonara", "Slow push in"),
 (31.28,"j", f"{C} closing his last book with a satisfied smile, tall stacks of books behind", "He closes the book and smiles"),
 (34.06,"k", f"{N} tasting a forkful of carbonara and smiling, {C} beside her", "She tastes it and gives a thumbs up"),
 (37.36,"l", "wide shot of a whole miniature clay diorama: Roman kitchen, trattoria street with lanterns, tiny figures sharing pasta", "Tiny figures move, lanterns flicker"),
],
}
# Year / place tags (seg -> [(local_s, text)])
TAGS = {
 "S1": [(20.10,"Naples  ·  late 1830s"), (63.00,"Rome  ·  1930"), (71.78,"1950")],
 "S2": [(15.06,"Italy  ·  1800s")],
 "S3": [(0.00,"Rome  ·  June 1944")],
 "S4": [(9.72,"Riccione  ·  September 1944"), (40.96,"La Stampa  ·  26 July 1950"), (77.34,"Chicago  ·  1952"), (83.84,"“Vittles and Vice”")],
 "S5": [(3.34,"Italy  ·  August 1954"), (29.60,"December 2023"), (53.24,"“It’s not my fault if that was the carbonara recipe!”  — Luca Cesari")],
 "S6": [(1.06,"Britain  ·  1954"), (27.52,"Since 2017"), (30.54,"6 April  ·  Carbonara Day")],
 "S7": [(4.32,"1960"), (10.42,"Mid-1960s"), (19.00,"1989"), (37.82,"1990s")],
 "S8": [(2.96,"Financial Times  ·  March 2023"), (37.42,"UNESCO  ·  December 2025")],
 "S9": [(18.44,"“Italian genius and American resources”  — Eleonora Cozzella")],
}
SEG_DUR = {"S0":31.086,"S1":84.036,"S2":33.646,"S3":41.639,"S4":105.796,"S5":59.951,"S6":38.922,"S7":51.409,"S8":53.473,"S9":39.001}
BREATH, TAIL = 0.6, 3.0

def plan():
    """-> list of dicts with seg, id, slot, kind ('still'|'clip'|'map'), clip_len."""
    out=[]
    segs=list(SHOTS)
    for seg in segs:
        rows=SHOTS[seg]; end=SEG_DUR[seg]+(TAIL if seg==segs[-1] else BREATH)
        for i,(t,sid,scene,motion) in enumerate(rows):
            slot=(rows[i+1][0] if i+1<len(rows) else end)-t
            if sid.startswith("MAP:"): kind,cl="map",0
            elif motion is None or slot<=2.6: kind,cl="still",0
            else:
                kind="clip"; cl=3 if slot<=3.8 else 4 if slot<=5.0 else 5
            out.append(dict(seg=seg,id=f"{seg}{sid}" if not sid.startswith("MAP:") else sid,t=t,slot=round(slot,2),kind=kind,clip_len=cl,scene=scene,motion=motion))
    return out
if __name__=="__main__":
    p=plan(); import collections
    c=collections.Counter(x["kind"] for x in p)
    stills=sum(1 for x in p if x["kind"]!="map"); secs=sum(x["clip_len"] for x in p)
    print(c, "| shots:",len(p)); print("stills to generate:",stills,"=",stills*2,"cr | clip seconds:",secs,"=",secs*2,"cr | total ≈",stills*2+secs*2)
    print("longest slots:",sorted([(x["slot"],x["id"]) for x in p])[-6:]); print("shortest:",sorted([(x["slot"],x["id"]) for x in p])[:6])
