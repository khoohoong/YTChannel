"""Builds the Ep 1 clay-still prompt list from the shot list (vo_and_shotlist.md)."""
import json
PRE = ("Simple stylised 3D render, soft clay / diorama look, rounded shapes, matte materials, "
       "warm soft studio lighting, tilt-shift miniature feel, 16:9. ")
POST = (" Food modelled accurately and appetisingly. Match the style of the reference image. "
        "No text, no letters, no numbers, no logos, no signage.")
NONNA = "a cheerful plump clay Italian grandmother with grey bun, apron and round glasses"
COOK = "a young clay Italian cook in white jacket and chef's cap"
GI = "clay 1940s American soldiers in olive uniforms"
S = {
 "VO0": [
  ("C1", f"{NONNA} wagging a finger beside a pan on a stove in a rustic Roman kitchen"),
  ("C2", "close-up of clay hands cracking a golden egg into a ceramic bowl of yolks"),
  ("C3", "close-up of crisp strips of guanciale sizzling in a small iron pan"),
  ("C4", "a wedge of pecorino cheese being grated into a snowy pile on a wooden board"),
  ("C5", "a wooden pepper mill above a plate of spaghetti carbonara, black pepper falling"),
  ("C6", f"{NONNA} shocked, pushing away a carton of cream on the kitchen counter"),
  ("S1", "a miniature clay Colosseum diorama at golden hour, tiny cypress trees"),
  ("C7", "a clay historian with tweed jacket and glasses opening a huge dusty old cookbook in a library"),
  ("C8", "close-up of an old cookbook with completely empty pages, dust in the light"),
  ("C9", "a small tumbleweed on an empty wooden kitchen table, an empty plate, comic emptiness"),
  ("C10","strips of bacon floating down on tiny parachutes towards a plate of spaghetti"),
 ],
 "VO1": [
  ("C1", "clay woodsmen beside a smouldering charcoal mound in a mountain forest, smoke rising"),
  ("C2", "clay woodsmen cooking a pot of pasta over a small campfire in the Apennine woods"),
  ("C3", "a clay woodsman sprinkling black pepper over a bowl of pasta by the fire"),
  ("C4", "steam rising from a rustic bowl of pasta on a log, forest at dusk behind"),
  ("C5", "the forest campfire scene with a giant red clay question mark standing in the middle"),
  ("C6", "hooded clay figures in 19th-century coats meeting by candlelight around a wooden table"),
  ("C7", "two hooded clay conspirators shaking hands secretly by candlelight"),
  ("C8", "hooded clay figures shrugging at a plate of pasta in the middle of their secret table"),
  ("C9", "extreme macro of black pepper flecks on glossy carbonara like specks of charcoal"),
  ("C10","extreme macro of a pepper mill grinding, dark flakes falling like charcoal dust"),
  ("S1", "an antique 1830s leather cookbook open on a wooden lectern, blank yellowed pages, candle"),
  ("C11","a clay 19th-century Neapolitan nobleman in a frock coat cooking pasta in an elegant kitchen"),
  ("C12","pasta being tossed with beaten eggs and grated cheese in a copper pan, clay hands"),
  ("C13","a countryside kitchen near Rome, a clay shepherd cooking pasta with guanciale and pecorino"),
  ("C14","a rustic plate of pasta alla gricia with crisp guanciale, pecorino and black pepper"),
  ("C15","a whimsical clay family tree whose branches hold little plates of pasta like fruit"),
  ("C16","a loaf of bread and a piece of meat side by side on a plate, clearly not a hamburger, humorous"),
  ("C17","a 1940s army helmet dropped onto a rustic kitchen table next to a pasta pot"),
 ],
 "VO2": [
  ("C1", f"1944 miniature Roman street, clay army jeeps rolling past cheering clay crowds"),
  ("C2", f"{GI} driving a jeep under a Roman arch, people waving from balconies"),
  ("C3", "a clay Roman piazza crowded with soldiers and locals celebrating, warm light"),
  ("C4", "a wooden army supply crate opened, packed with bacon slabs and tins, no markings"),
  ("C5", "blank tins of powdered egg and wrapped bacon stacked on a crate"),
  ("C6", "a classic American breakfast plate of bacon and fried eggs on a diner counter"),
  ("C7", f"{COOK} looking puzzled at a slab of bacon in one hand and spaghetti in the other"),
  ("C8", f"{COOK} with a glowing light bulb above his head, kitchen around him"),
  ("C9", f"{COOK} serving plates of pasta to {GI} in a small Roman trattoria"),
  ("C10",f"{GI} smiling and eating spaghetti at a checkered tablecloth"),
  ("C11","a 1940s seaside villa terrace on the Adriatic, clay officers seated at a long lunch table"),
  ("C12","clay British and American officers at a lunch table raising glasses, sea behind"),
  ("C13",f"{COOK} plating pasta and cracking black pepper over it in a villa kitchen"),
  ("C14","the villa lunch scene in faded sepia tones with a large clay question mark"),
  ("C15","a narrow Trastevere street at night with hanging lanterns and ivy, clay restaurant door"),
  ("C16",f"{GI} officers queuing outside a cosy Trastevere trattoria at night"),
  ("S1", "a 1950 newspaper lying on a café table, columns of blank grey placeholder blocks"),
  ("C17","a clay officer pointing at a blank chalkboard menu inside a trattoria"),
  ("C18","a single plate of spaghetti carbonara on a checkered tablecloth, candle, hero shot"),
 ],
 "VO3": [
  ("C1", "a 1950s Chicago street diorama with an elevated train and brick buildings"),
  ("C2", "a 1950s Chicago elevated train passing over a clay street at dusk"),
  ("C3", "a cosy 1950s Italian restaurant storefront in Chicago with an awning, blank sign"),
  ("C4", "a clay 1950s woman writer typing at a typewriter with notes and a plate of pasta"),
  ("C5", "a 1950s Italian food magazine lying open on a kitchen counter, blank pages with pictures"),
  ("C6", "cubes of pancetta, garlic cloves and a holey wedge of Gruyère cheese lined up on a board"),
  ("C7", "a Gruyère cheese wedge with characteristic holes sliding into a pan of pasta"),
  ("C8", f"{NONNA} fainting dramatically onto a chair in her kitchen"),
  ("S1", "four blank recipe cards pinned in a row on a cork board with string, warm light"),
  ("C9", "a slice of guanciale pushing a piece of pancetta off a cutting board, playful"),
  ("C10","a wedge of pecorino nudging a wedge of parmesan off a cheese board"),
  ("C11","cream pouring from a jug into a pan of carbonara"),
  ("C12","a clay boot kicking a carton of cream out of a kitchen door"),
  ("C13","egg, guanciale, pecorino and a pepper mill lined up like proud performers on a table"),
 ],
 "VO3B": [
  ("C1", "a 1950s English kitchen, a clay woman in a cardigan reading a cookbook, teapot"),
  ("C2", "a vintage suitcase covered in travel stickers rolling along a road, a pasta pot strapped on top"),
  ("C3", "a jug of cream glugging generously into pasta in a pan"),
  ("C4", "a thick, pale, very creamy plate of pasta with mushrooms, abroad-style"),
  ("C5", "clay tourists with cameras ordering at a Roman trattoria table outdoors"),
  ("C6", "three pasta plates on a small winners' podium: fettuccine Alfredo top, lasagne second, carbonara third"),
  ("S1", "a blank paper wall calendar on a kitchen wall next to hanging pans"),
  ("C7", "two clay people on a sofa staring angrily at their glowing phones"),
  ("C8", "clay phones with speech bubbles containing little cream cartons and crossed eggs, no text"),
 ],
 "VO4": [
  ("C1", "a clay professor at a lectern holding a newspaper, lecture hall"),
  ("C2", "clay Italian farmers in a field angrily waving forks with spaghetti"),
  ("C3", "a generic clay politician in a suit gesturing at a podium with microphones"),
  ("C4", "a clay family arguing over dinner, forks pointing across the table"),
  ("S1", "a messy stack of newspapers on a desk, blank grey placeholder columns"),
  ("C5", "a brass balance scale with an egg on one side and bacon on the other"),
  ("C6", "close-up of clay hands tossing spaghetti into a silky golden egg sauce in a pan"),
  ("C7", "glossy silky carbonara twirled on a fork, steam"),
  ("C8", "a wooden army crate and an Italian copper pan side by side on a table"),
  ("C9", f"{COOK} shaking hands with a clay 1940s American soldier over a plate of carbonara"),
  ("C10","the handshake scene in a warm wider shot, kitchen and table visible"),
 ],
 "VO5": [
  ("C1", f"{NONNA} and a clay 1940s American soldier sharing a plate of carbonara at a table"),
  ("C2", "steam curling up from a plate of carbonara, dark warm background"),
  ("C3", "a fortune cookie on a small plate, cracked open, paper slip blank"),
  ("C4", "a wide shot of the whole miniature diorama of a Roman kitchen and trattoria"),
 ],
}
out=[]
for seg, shots in S.items():
    for sid, scene in shots:
        out.append({"id": f"{seg}-{sid}", "prompt": PRE + scene + "." + POST})
json.dump(out, open("stills_prompts.json","w"), indent=1)
print(len(out))
