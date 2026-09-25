import json

rows = []

def add(**kw):
    rows.append(kw)

# --- Bonny Doon ---
add(artist="Bonny Doon", album="Bonny Doon", year=2017, type="LP", label="Salinas Records",
    primary_lane="C6", secondary_lanes=["C7"], style="Country folk", region="Chicago and the Midwest", base="Detroit, MI", scene="",
    descriptors=["hushed","fingerpicked acoustic","drawl","close harmonies","breezy"],
    description="Bonny Doon's debut is a gentle, unhurried collection of plainspoken country-folk songs built on loping tempos and warm, conversational vocal harmonies between Bill Lennox and Bobby Colombo. It's understated where their later records get looser and more rock-facing. It's for fans of hushed, front-porch songwriting.",
    lineage="Grows out of Detroit's indie scene (with ties to Waxahatchee, whose Saint Cloud the band would later back); sets up the more Woodsist-style slacker sound of Longwave.",
    lineage_basis="Documented", key_tracks=["Hospital Bed","Falling Out"], priority="Deep cut", start_here="", terry="",
    sources=["https://en.wikipedia.org/wiki/Bonny_Doon_(band)"], confidence="Medium", borderline_note="")

add(artist="Bonny Doon", album="Longwave", year=2018, type="LP", label="Woodsist",
    primary_lane="C7", secondary_lanes=["C6"], style="Slacker", region="Chicago and the Midwest", base="Detroit, MI", scene="",
    descriptors=["drawl","hushed","fingerpicked acoustic","breezy","close harmonies"],
    description="A warm, sleepy-eyed sophomore record that became a slow-burn cult favorite, pairing loose, unpolished guitar interplay with plainspoken lyrics about heartbreak and drift. Its patient tempos and conversational vocals put it squarely in the Woodsist label's slacker lineage. It's for fans who want comfort-food indie rock that never raises its voice.",
    lineage="Continues the band's hushed country-folk sound on the classic slacker label Woodsist, connecting them to the broader 2010s Kurt Vile/Real Estate axis.",
    lineage_basis="Documented", key_tracks=["I Am Nothing","A Lack of Oz"], priority="Recommended", start_here="", terry="",
    sources=["https://en.wikipedia.org/wiki/Bonny_Doon_(band)"], confidence="Medium", borderline_note="")

# --- King Tuff ---
add(artist="King Tuff", album="Smalltown Stardust", year=2023, type="LP", label="Sub Pop Records",
    primary_lane="C7", secondary_lanes=[], style="Power pop", region="The Northeast", base="Brattleboro, VT", scene="",
    descriptors=["jangle","synths","breezy","cosmic","anthemic"],
    description="A dreamier, more polished turn for the garage-glam lifer Kyle Thomas, trading his usual fuzzed-out riffs for jangly, synth-dusted power pop with a wide-eyed, sun-drenched feel. It's a gentler record than his 2010s output but keeps his knack for an instant hook. It's for fans who like their power pop with a cosmic-country glow.",
    lineage="King Tuff's catalog runs from 2000s garage-punk through Sub Pop glam-rock; Smalltown Stardust pulls him into the same jangly, twang-adjacent revival as his 2010s peers.",
    lineage_basis="Inferred", key_tracks=["Love Letters To Plants","Smalltown Stardust"], priority="Deep cut", start_here="", terry="",
    sources=["https://en.wikipedia.org/wiki/King_Tuff","https://kingtuff.bandcamp.com/album/smalltown-stardust"], confidence="High",
    borderline_note="King Tuff formed in 2006 and his sound is more garage/glam than jangle-pop; only this era-fitting, twangier LP is included per assignment as a borderline call.")

# --- Casper Skulls ---
add(artist="Casper Skulls", album="Lips & Skull", year=2016, type="EP", label="Buzz Records",
    primary_lane="C7", secondary_lanes=[], style="Jangle", region="The UK, Ireland and Canada", base="Toronto, Canada", scene="",
    descriptors=["jangle","deadpan","storytelling","harmonized guitars","breezy"],
    description="Casper Skulls' debut EP introduces the Toronto band's dual-vocal, college-rock-indebted guitar pop, drawing on Pavement and R.E.M.-style jangle with conversational, story-driven lyrics. It's shorter and scrappier than their later full-lengths but sets the band's voice from the start. It's for fans who want the earliest version of their sound.",
    lineage="Part of Toronto's Buzz Records jangle-pop roster alongside acts like Weaves; a direct forerunner to Mercy Works and Knows No Kindness.",
    lineage_basis="Documented", key_tracks=["Lips and Skull","Dying in Eight Verses"], priority="Deep cut", start_here="", terry="",
    sources=["https://en.wikipedia.org/wiki/Casper_Skulls"], confidence="Medium", borderline_note="")

add(artist="Casper Skulls", album="Mercy Works", year=2017, type="LP", label="Buzz Records",
    primary_lane="C7", secondary_lanes=[], style="Jangle", region="The UK, Ireland and Canada", base="Toronto, Canada", scene="",
    descriptors=["jangle","deadpan","storytelling","harmonized guitars","anthemic"],
    description="Casper Skulls' full-length debut expands their college-radio jangle into bigger, more anthemic arrangements while keeping the dual-vocal chemistry between Melanie St-Pierre and Neil Bednis at the center. The lyrics lean into storytelling and small-scale drama over ringing, layered guitars. It's for fans of R.E.M.-descended Canadian indie rock.",
    lineage="Follows directly from Lips & Skull on Buzz Records, continuing Toronto's jangle-pop lineage into a fuller studio sound.",
    lineage_basis="Documented", key_tracks=["Lingua Franca","Colour of the Outside"], priority="Recommended", start_here="", terry="",
    sources=["https://en.wikipedia.org/wiki/Casper_Skulls"], confidence="Medium", borderline_note="")

add(artist="Casper Skulls", album="Knows No Kindness", year=2021, type="LP", label="Buzz Records",
    primary_lane="C7", secondary_lanes=[], style="Jangle", region="The UK, Ireland and Canada", base="Toronto, Canada", scene="",
    descriptors=["jangle","deadpan","storytelling","harmonized guitars","breezy"],
    description="A more confident, dynamically varied record than their debut, still anchored by ringing guitar interplay and dual-vocal storytelling but pushing into denser arrangements and darker lyrical territory. It's the sound of a band settling comfortably into its own identity within Toronto's jangle-pop scene. It's for fans who followed the band from their Buzz Records beginnings.",
    lineage="The most developed entry in Casper Skulls' Buzz Records run, later followed by Kit-Cat on Next Door Records.",
    lineage_basis="Documented", key_tracks=["Onward","Quality of Life"], priority="Recommended", start_here="", terry="",
    sources=["https://en.wikipedia.org/wiki/Casper_Skulls"], confidence="Medium", borderline_note="")

add(artist="Casper Skulls", album="Kit-Cat", year=2025, type="LP", label="Next Door Records",
    primary_lane="C7", secondary_lanes=[], style="Jangle", region="The UK, Ireland and Canada", base="Toronto, Canada", scene="",
    descriptors=["jangle","deadpan","storytelling","harmonized guitars","funny-sad"],
    description="Casper Skulls' latest LP has the dual-vocal chemistry and college-radio jangle of a band drawing on Pavement, R.E.M., and Superchunk, described by Josh Terry as full of lived-in warmth. Guitars ring and interlock while the vocal trade-offs keep the songs feeling conversational. It's for longtime fans of the band's steady evolution.",
    lineage="Continues the jangle-pop lineage established on Buzz Records, now on Next Door Records with a warmer, more assured sound.",
    lineage_basis="Documented", key_tracks=["Spindletop","Roddy Piper"], priority="Recommended", start_here="", terry="https://www.noexpectations.fyi/p/brown-horse-mamalarky-neu-blume-finnish-postcard-casper-skulls",
    sources=["https://casperskulls.bandcamp.com/album/kit-cat"], confidence="Medium", borderline_note="")

# --- Jon McKiel ---
add(artist="Jon McKiel", album="Bobby Joe Hope", year=2020, type="LP", label="You've Changed Records",
    primary_lane="C7", secondary_lanes=["C6"], style="Lo-fi", region="The UK, Ireland and Canada", base="Baie Verte, New Brunswick, Canada", scene="",
    descriptors=["lo-fi","fingerpicked acoustic","hushed","cosmic","drawl"],
    description="Written in response to ghostly samples McKiel found on a used reel-to-reel tape, this record blends hushed, fingerpicked songwriting with warped found-sound textures into something inventive and haunting. It's a quieter, more experimental turn than straightforward jangle-pop but keeps a strong melodic core. It's for fans of Canadian DIY songwriting with a spectral edge.",
    lineage="Part of the You've Changed Records roster connecting Maritime Canada's indie scene to the wider lo-fi/jangle underground; feeds into Hex's continued collaboration with Jay Crocker.",
    lineage_basis="Documented", key_tracks=["Mourning Dove","Sun's Out"], priority="Recommended", start_here="", terry="https://www.noexpectations.fyi/p/five-lps-donald-byrd-hftrr-kglw-gizz-gbv",
    sources=["https://en.wikipedia.org/wiki/Jon_McKiel","https://jonmckiel.bandcamp.com/album/bobby-joe-hope"], confidence="High", borderline_note="")

add(artist="Jon McKiel", album="Hex", year=2024, type="LP", label="You've Changed Records",
    primary_lane="C7", secondary_lanes=["C6"], style="Lo-fi", region="The UK, Ireland and Canada", base="Baie Verte, New Brunswick, Canada", scene="",
    descriptors=["lo-fi","synths","hushed","cosmic","fingerpicked acoustic"],
    description="A second collaboration with producer Jay Crocker, this record folds more synths and studio texture into McKiel's hushed songwriting without losing the strange, homemade intimacy of Bobby Joe Hope. It's a favorite of Josh Terry's that he never got around to writing about on release. It's for fans of understated, atmosphere-first Canadian indie rock.",
    lineage="Continues the Crocker/McKiel partnership begun on Bobby Joe Hope, part of the same You've Changed Records lineage.",
    lineage_basis="Documented", key_tracks=["Popular Music","Hex"], priority="Recommended", start_here="", terry="https://www.noexpectations.fyi/p/lily-seabird-hollow-hand-angela-autumn-crying-laughing-jon-mckiel",
    sources=["https://en.wikipedia.org/wiki/Jon_McKiel"], confidence="Medium", borderline_note="")

# --- Chook Race ---
add(artist="Chook Race", album="Around the House", year=2016, type="LP", label="Trouble in Mind Records",
    primary_lane="C7", secondary_lanes=[], style="Jangle", region="Australia and New Zealand", base="Melbourne, Australia", scene="",
    descriptors=["jangle","lo-fi","breezy","deadpan","short songs (under 2 minutes)"],
    description="A shambling, K Records-worthy set of hooky, unhurried indie pop from this Melbourne trio, all ringing guitars and plainspoken vocals over loping tempos. It's cheap, cheerful, and unfussy in a way that recalls the DIY jangle-pop of decades past. It's for fans of Flying Nun-descended guitar pop with an Australian slacker drawl.",
    lineage="Part of the Melbourne DIY jangle-pop scene that also produced Dick Diver and Terry, distributed internationally by the American slacker-rock label Trouble in Mind.",
    lineage_basis="Documented", key_tracks=["Hard to Clean","Eggshells"], priority="Recommended", start_here="", terry="",
    sources=["https://chookrace.bandcamp.com/album/around-the-house"], confidence="Medium", borderline_note="")

# --- Dick Diver ---
add(artist="Dick Diver", album="Calendar Days", year=2013, type="LP", label="Chapter Music",
    primary_lane="C7", secondary_lanes=[], style="Jangle", region="Australia and New Zealand", base="Melbourne, Australia", scene="",
    descriptors=["jangle","drawl","breezy","deadpan","hushed"],
    description="Recorded at a beach house on Phillip Island, this second Dick Diver LP is loose, warm, and conversational, built on ringing guitars and half-sung, half-spoken vocals in the vein of the Go-Betweens and the Clean. It's a defining record of the early-2010s Melbourne jangle-pop revival. It's for fans who want the sound that inspired a wave of Australian slacker-pop bands.",
    lineage="Grew out of Melbourne's Chapter Music scene alongside Boomgates and Twerps; directly influenced Chook Race and the broader countrygaze/jangle revival abroad.",
    lineage_basis="Documented", key_tracks=["Water Damage","Alice"], priority="Essential", start_here="", terry="",
    sources=["https://www.facebook.com/dickdiverband/","https://dickdiver.bandcamp.com/music"], confidence="High", borderline_note="")

# --- Beach Bunny ---
add(artist="Beach Bunny", album="Prom Queen", year=2018, type="EP", label="Mom + Pop",
    primary_lane="C7", secondary_lanes=[], style="Power pop", region="Chicago and the Midwest", base="Chicago, IL", scene="",
    descriptors=["jangle","breezy","short songs (under 2 minutes)","anthemic","cracked or yelping"],
    description="Lili Trifilio's breakout EP pairs bright, hooky power-pop guitars with plainspoken lyrics about body image and self-doubt, catching viral attention that pushed Beach Bunny from bedroom project to touring band. The songs are short, direct, and instantly catchy. It's for fans of Chicago's guitar-pop scene at its most immediate.",
    lineage="Grows out of Chicago's DIY guitar-pop scene alongside acts like Dehd; connects 2010s bedroom-pop songwriting to a more festival-scale power-pop sound on Blame Game.",
    lineage_basis="Documented", key_tracks=["Prom Queen","Deer Head"], priority="Recommended", start_here="", terry="",
    sources=["https://en.wikipedia.org/wiki/Beach_Bunny_(band)"], confidence="Medium",
    borderline_note="Poppier and more pop-punk-adjacent than strict jangle/power-pop revival, but Terry's newsletter counts it among the scene; included per assignment.")

add(artist="Beach Bunny", album="Blame Game", year=2021, type="EP", label="Mom + Pop",
    primary_lane="C7", secondary_lanes=[], style="Power pop", region="Chicago and the Midwest", base="Chicago, IL", scene="",
    descriptors=["jangle","anthemic","breezy","cracked or yelping","short songs (under 2 minutes)"],
    description="A tighter, more polished EP than Prom Queen, with Beach Bunny's power-pop hooks pushed toward arena-ready choruses while the lyrics stay pointed and personal. It's a bridge between their scrappier early singles and their more produced full-length work. It's for fans who want the band's most immediate, radio-ready songwriting.",
    lineage="Continues the Chicago guitar-pop lineage of Prom Queen, sharpening the hooks as the band's audience grew.",
    lineage_basis="Documented", key_tracks=["Good Girls (Don't Get Used)","Blame Game"], priority="Recommended", start_here="", terry="",
    sources=["https://en.wikipedia.org/wiki/Beach_Bunny_(band)"], confidence="Medium", borderline_note="")

with open("/home/claude/work/staging/lane_SW4.jsonl", "a", encoding="utf-8") as f:
    for r in rows:
        f.write(json.dumps(r, ensure_ascii=False) + "\n")

print(f"wrote {len(rows)} rows")
