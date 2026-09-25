import json

rows = []

def add(**kw):
    rows.append(kw)

add(artist="Bullseye", album="Bullseye", year=2026, type="LP", label="Ever/Never Records",
    primary_lane="C7", secondary_lanes=[], style="Punk", region="The Northeast", base="New York, NY", scene="",
    descriptors=["rowdy","jangle","shouted","anthemic","short songs (under 2 minutes)"],
    description="This New York quartet's self-titled debut is a hooky, jangly and twangy power-pop rock record with blistering riffs and meaty choruses, released by the fast-rising Ever/Never label. It's punchy and immediate, favoring rock and roll swagger over polish. It's for fans who want the twang-adjacent side of the current power-pop wave.",
    lineage="Signed to Ever/Never, the same New York label behind Ryan Davis & the Roadhouse Band and National Photo Committee, tying the band into the current DIY jangle/twang underground.",
    lineage_basis="Documented", key_tracks=["Bullseye"], priority="Deep cut", start_here="", terry="https://www.noexpectations.fyi/p/hana-stretton-neptunes-core-bullseye-mallory-hawk",
    sources=["https://www.noexpectations.fyi/p/hana-stretton-neptunes-core-bullseye-mallory-hawk"], confidence="Medium", borderline_note="")

add(artist="FOOTBALLHEAD", album="Overthinking Everything", year=2024, type="LP", label="Tiny Engines",
    primary_lane="C7", secondary_lanes=[], style="Power pop", region="The South", base="Unknown, US", scene="",
    descriptors=["jangle","anthemic","short songs (under 2 minutes)","breezy","funny-sad"],
    description="An early-2024 power-pop full-length released on the emo/indie label Tiny Engines, part of a wave of DIY guitar-pop records flagged in Josh Terry's most-anticipated list that year. Details on its sound are limited, but its label and placement put it squarely in the jangle/power-pop underground. It's a deep-cut pick for listeners exploring Tiny Engines' current roster.",
    lineage="Released on Tiny Engines, a label historically associated with emo and twangy emo crossovers, connecting it to the C9 emo-crossover lane as well as straight power pop.",
    lineage_basis="Inferred", key_tracks=["Overthinking Everything"], priority="Deep cut", start_here="", terry="https://www.noexpectations.fyi/p/the-most-anticipated-albums-of-2024",
    sources=["https://www.noexpectations.fyi/p/the-most-anticipated-albums-of-2024"], confidence="Medium", borderline_note="Limited sound detail available; included on the strength of label/scene placement in Terry's list.")

add(artist="The Belair Lip Bombs", album="Again", year=2025, type="LP", label="Third Man Records",
    primary_lane="C7", secondary_lanes=[], style="Power pop", region="Australia and New Zealand", base="Melbourne, Australia", scene="",
    descriptors=["jangle","harmonized guitars","anthemic","breezy","pop-culture references"],
    description="Produced by Rolling Blackouts Coastal Fever's Joe White, this sophomore LP from Melbourne's the Belair Lip Bombs is frenetic, interlocking power pop fronted by the commanding Maisie Everett. The guitars careen and lock together in a way that recalls Australia's jangle-rock lineage while the choruses aim straight for arenas. It's among the strongest straight power-pop records of its year.",
    lineage="Connects Melbourne's jangle-rock scene (via producer Joe White of Rolling Blackouts C.F.) to Third Man Records' wider power-pop and garage-rock roster.",
    lineage_basis="Documented", key_tracks=["Don't Let Them Tell You (It's Fair)","Smiling"], priority="Recommended", start_here="", terry="https://www.noexpectations.fyi/p/liam-kazar-astrachan-zook-h-pruz-belair-lip-bombs",
    sources=["https://www.noexpectations.fyi/p/liam-kazar-astrachan-zook-h-pruz-belair-lip-bombs"], confidence="Medium", borderline_note="")

add(artist="Feller", album="Sound Colored Penny", year=2026, type="LP", label="Angel Tapes",
    primary_lane="C7", secondary_lanes=[], style="Power pop", region="The Northeast", base="New York, NY", scene="",
    descriptors=["jangle","rowdy","anthemic","short songs (under 2 minutes)","cracked or yelping"],
    description="This trio's debut full-length tightens the raucous energy of their 2024 EP into hook-forward, dynamic indie rock, packing frantic energy and earworm melodies into a lean 25 minutes. Delicate falsetto verses give way to explosive, unrelenting choruses across the tracklist. It's for fans who want their power pop with real teeth.",
    lineage="Released via Fire Talk's Angel Tapes imprint, connecting the band to the current New York DIY guitar-pop underground alongside labelmates in the same scene.",
    lineage_basis="Documented", key_tracks=["Penny Farthing","Marys Perfume"], priority="Deep cut", start_here="", terry="https://www.noexpectations.fyi/p/feller-nilza-costa-momoko-gill-tomeka-reid",
    sources=["https://www.noexpectations.fyi/p/feller-nilza-costa-momoko-gill-tomeka-reid"], confidence="Medium", borderline_note="")

add(artist="Daughter of Swords", album="Alex", year=2025, type="LP", label="Psychic Hotline",
    primary_lane="C5", secondary_lanes=["C7"], style="Indie folk", region="The Carolinas", base="Durham, NC", scene="",
    descriptors=["fingerpicked acoustic","hushed","funny-sad","breezy","storytelling"],
    description="Mountain Man's Alexandra Sauser-Monnig's sophomore solo record is her most playful, writing kinetic, off-kilter pop songs that evoke Talking Heads, Finom, and Sheryl Crow rather than straight folk. Her lyrics stay conversational and perceptive even as the arrangements get bouncier. It's for fans who want folk-rooted songwriting that takes unexpected pop turns.",
    lineage="Grows out of the Mountain Man/Big Thief-adjacent folk circle, pushing outward into twangy indie pop territory that overlaps with the jangle revival.",
    lineage_basis="Documented", key_tracks=["Money Hits","Strange"], priority="Recommended", start_here="", terry="https://www.noexpectations.fyi/p/reviews-pry-blasucci-lifeguard-daughter-swords-niemi",
    sources=["https://www.noexpectations.fyi/p/reviews-pry-blasucci-lifeguard-daughter-swords-niemi"], confidence="Medium",
    borderline_note="Closer to twangy indie folk (C5) than straight jangle/power-pop; listed secondary in C7 per assignment mention.")

add(artist="Frog", album="1000 Variations On the Same Song", year=2025, type="LP", label="Self-released",
    primary_lane="C7", secondary_lanes=["C2"], style="Lo-fi", region="The Northeast", base="New York, NY", scene="",
    descriptors=["lo-fi","funny-sad","piano","banjo","pop-culture references"],
    description="Cult New York duo Frog's sixth album is folky, lo-fi and scrappy, described by Stereogum's Chris Deville as though Modest Mouse made a Pinegrove album. Highlights include the piano-led opener and a banjo-anchored lead single, with aching lyrics wrapped in charmingly unadorned production. It's for fans who want deadpan, funny-sad songwriting without any studio gloss.",
    lineage="Frog has been active since 2012 in New York's DIY scene, connecting Drag City-style funny-sad songwriting to the jangle/lo-fi Bandcamp underground.",
    lineage_basis="Documented", key_tracks=["Stillwell Theme","Mixtape Liner Notes Var. VII"], priority="Recommended", start_here="", terry="https://www.noexpectations.fyi/p/dead-gowns-horsegirl-frog-goose-winter-tour",
    sources=["https://heyitsfrog.bandcamp.com/album/1000-variations-on-the-same-song","https://www.noexpectations.fyi/p/dead-gowns-horsegirl-frog-goose-winter-tour"], confidence="High", borderline_note="")

add(artist="Diners", album="DOMINO", year=2023, type="LP", label="Bar/None Records",
    primary_lane="C7", secondary_lanes=[], style="Power pop", region="The West", base="Los Angeles, CA", scene="",
    descriptors=["jangle","breezy","harmonized guitars","pop-culture references","anthemic"],
    description="Blue Broderick's Diners project goes full power-pop on this impeccably written, breezy guitar-pop record produced by Mo Troper, with clear DNA from Tom Petty, Big Star, and Fountains of Wayne. There's no filler across the ten tracks, each one built for maximum hum-along appeal. It's for fans who want classic power-pop songcraft filtered through a bedroom-pop sensibility.",
    lineage="Connects Broderick's earlier lo-fi Diners records to the wider Bandcamp power-pop revival via producer Mo Troper, a key figure in that scene.",
    lineage_basis="Documented", key_tracks=["Domino","Working On My Dreams"], priority="Recommended", start_here="", terry="https://www.noexpectations.fyi/p/new-albums-jeff-rosenstock-diners-buck-meek",
    sources=["https://diners.bandcamp.com/album/domino","https://www.noexpectations.fyi/p/new-albums-jeff-rosenstock-diners-buck-meek"], confidence="High", borderline_note="")

add(artist="Golomb", album="Love", year=2024, type="EP", label="Self-released",
    primary_lane="C7", secondary_lanes=[], style="Punk", region="Chicago and the Midwest", base="Columbus, OH", scene="",
    descriptors=["rowdy","shouted","noise wall","short songs (under 2 minutes)","feedback"],
    description="This Columbus power trio's three-song EP is pummeling, loud, and varied, with each track sounding markedly different but united by an animated heaviness, per Josh Terry, who calls the band the future of indie rock. Fronted by a husband-and-wife duo plus a drummer, it's a live-wire document of a genuinely ferocious band. It's for fans of noisy Midwestern guitar rock that hits hard in short bursts.",
    lineage="Part of the current Midwest DIY noise-rock underground that overlaps with the slacker/jangle scene at its loudest, rowdiest edge.",
    lineage_basis="Documented", key_tracks=["Sixth Sense","Dare You To Cry"], priority="Deep cut", start_here="", terry="https://www.noexpectations.fyi/p/new-lps-robber-robber-sinai-vessel-ben-seretan",
    sources=["https://golomb.bandcamp.com/album/love","https://www.noexpectations.fyi/p/new-lps-robber-robber-sinai-vessel-ben-seretan"], confidence="High", borderline_note="")

add(artist="Joe Glass", album="Slither", year=2022, type="LP", label="Self-released",
    primary_lane="C7", secondary_lanes=[], style="Power pop", region="Chicago and the Midwest", base="Rockford, IL / Chicago, IL", scene="",
    descriptors=["jangle","drawl","pop-culture references","breezy","cracked or yelping"],
    description="Joe Glass's debut showcases his knack for an airtight hook across a dozen slightly twangy, ramshackle rockers pulling from Nuggets-style garage pop and '90s indie rock. Josh Terry has said it would have been a newsletter favorite had he heard it upon release. It's the record that predates his work alongside bandmate Kai Slater in Sharp Pins.",
    lineage="Part of the Chicago/Rockford DIY power-pop underground surrounding Lifeguard and Sharp Pins, feeding into Glass's later, more polished Snakewards.",
    lineage_basis="Documented", key_tracks=["Slither"], priority="Deep cut", start_here="", terry="https://www.noexpectations.fyi/p/otto-benson-joe-glass-jana-horn-winged-wheel",
    sources=["https://www.noexpectations.fyi/p/otto-benson-joe-glass-jana-horn-winged-wheel"], confidence="Medium", borderline_note="")

add(artist="Astrachan", album="Signs", year=2025, type="LP", label="Self-released",
    primary_lane="C7", secondary_lanes=[], style="Power pop", region="Chicago and the Midwest", base="Chicago, IL", scene="",
    descriptors=["anthemic","cosmic","breezy","pop-culture references","funny-sad"],
    description="Chicago songwriter Ben Astrachan's solo debut is maximalist and ambitious, packing each of its 13 tracks with wailing guitars and a multitude of '60s-and-'70s-indebted melodic twists. It's conceptual rock music delivered in an off-kilter, deliriously infectious way rather than as straight pastiche. It's for fans of Chicago's current crop of ebullient, detail-obsessed guitar-pop songwriters.",
    lineage="Emerges from the same Chicago scene as Smushie and Shoulderbird, connecting classic-rock revivalism to the current power-pop/jangle underground.",
    lineage_basis="Documented", key_tracks=["Dana Divine","Picture of Doubt"], priority="Deep cut", start_here="", terry="https://www.noexpectations.fyi/p/liam-kazar-astrachan-zook-h-pruz-belair-lip-bombs",
    sources=["https://astrachanmusic.bandcamp.com/album/signs","https://www.noexpectations.fyi/p/liam-kazar-astrachan-zook-h-pruz-belair-lip-bombs"], confidence="High", borderline_note="")

add(artist="Graham Hunt", album="If You Knew Would You Believe It?", year=2022, type="LP", label="Self-released",
    primary_lane="C7", secondary_lanes=[], style="Power pop", region="Chicago and the Midwest", base="Madison, WI", scene="",
    descriptors=["jangle","pop-culture references","cracked or yelping","cosmic","breezy"],
    description="A guitar-forward home-recorded record with hooky choruses that slides between snotty rock, stargazing psych, and introspective folk, part of Graham Hunt's prolific self-released catalog out of Madison, Wisconsin. It leans on a '90s alt-rock sensibility while still sounding distinctly homemade. It's for fans of one-person bedroom rock records with real songwriting range.",
    lineage="Part of Hunt's ongoing self-released Bandcamp catalog that runs from lo-fi power pop through to the more studio-polished American Pyramid.",
    lineage_basis="Documented", key_tracks=["If You Knew Would You Believe It?"], priority="Deep cut", start_here="", terry="https://www.noexpectations.fyi/p/no-expectations-043-bad-summer",
    sources=["https://grahamhunt.bandcamp.com/music","https://www.noexpectations.fyi/p/no-expectations-043-bad-summer"], confidence="High", borderline_note="")

add(artist="Graham Hunt", album="Try Not To Laugh", year=2023, type="LP", label="Self-released",
    primary_lane="C7", secondary_lanes=[], style="Power pop", region="Chicago and the Midwest", base="Madison, WI", scene="",
    descriptors=["jangle","pop-culture references","breezy","cracked or yelping","anthemic"],
    description="A self-released Wisconsin power-pop record with effortless hooks and a '90s rock sensibility, continuing Graham Hunt's steady run of home-recorded guitar-pop albums. The songwriting is direct and unfussy, favoring melody over studio polish. It's for fans who want deep-catalog power pop from outside the usual coastal scenes.",
    lineage="Sits between If You Knew Would You Believe It? and Timeless World Forever in Hunt's self-released discography.",
    lineage_basis="Documented", key_tracks=["Try Not To Laugh"], priority="Deep cut", start_here="", terry="https://www.noexpectations.fyi/p/radiohead-albums-ranked-the-smile-kid-a",
    sources=["https://grahamhunt.bandcamp.com/music","https://www.noexpectations.fyi/p/radiohead-albums-ranked-the-smile-kid-a"], confidence="High", borderline_note="")

add(artist="Graham Hunt", album="Timeless World Forever", year=2025, type="LP", label="Self-released",
    primary_lane="C7", secondary_lanes=[], style="Power pop", region="Chicago and the Midwest", base="Madison, WI", scene="",
    descriptors=["jangle","pop-culture references","breezy","cracked or yelping","cosmic"],
    description="Another entry in Graham Hunt's prolific self-released catalog, continuing his blend of hooky, home-recorded power pop with wide-ranging classic-rock and psych touches. It appeared on Josh Terry's 2025 longlist among the year's most worthwhile guitar-pop records. It's for listeners tracking his steady, low-key discography.",
    lineage="Part of Hunt's ongoing solo catalog that runs directly into American Pyramid's bigger studio sound.",
    lineage_basis="Documented", key_tracks=["Timeless World Forever"], priority="Deep cut", start_here="", terry="https://www.noexpectations.fyi/p/the-100-best-albums-of-2025",
    sources=["https://grahamhunt.bandcamp.com/music","https://www.noexpectations.fyi/p/the-100-best-albums-of-2025"], confidence="High", borderline_note="")

add(artist="Graham Hunt", album="American Pyramid", year=2026, type="LP", label="Self-released",
    primary_lane="C7", secondary_lanes=[], style="Power pop", region="Chicago and the Midwest", base="Madison, WI", scene="",
    descriptors=["jangle","pop-culture references","cosmic","anthemic","cracked or yelping"],
    description="Hunt's sixth full-length is his most maximalist yet, recorded at Minnesota's Pachyderm Studios after years of home recording, with frantic late-'90s pop-rock hooks, autotuned detours, and euphoric grooves recalling Screamadelica. Josh Terry calls it cutting-edge while somehow still sounding instantly familiar. It's the fullest studio treatment his songwriting has gotten to date.",
    lineage="The culmination of Hunt's self-released catalog, moving from bedroom recording to a proper studio while keeping the same playful, hook-heavy songwriting.",
    lineage_basis="Documented", key_tracks=["Waiting for You to Come Home","Guardian Angel's Arms"], priority="Recommended", start_here="", terry="https://www.noexpectations.fyi/p/convinced-friend-dos-santos-graham-hunt",
    sources=["https://www.noexpectations.fyi/p/convinced-friend-dos-santos-graham-hunt","https://grahamhunt.bandcamp.com/music"], confidence="High", borderline_note="")

add(artist="Hiding Places", album="The Secret To Good Living", year=2026, type="LP", label="Keeled Scales",
    primary_lane="C7", secondary_lanes=["C4"], style="Punk", region="Philadelphia", base="Brooklyn, NY (formerly North Carolina)", scene="",
    descriptors=["rowdy","duets","storytelling","harmonized guitars","anthemic"],
    description="This Brooklyn band's debut, originally formed in North Carolina, eschews the twang-and-shoegaze sound of their home-state peers for something more its own: brutal, pounding riffs paired with dual lead vocals and patiently pastoral arrangement shifts. Released by the Texas label Keeled Scales, it stands apart from the countrygaze pack while sharing its scene. It's for fans who want the loudest, least twangy corner of the current DIY guitar-rock underground.",
    lineage="Formed within North Carolina's twang-and-shoegaze scene before relocating to Brooklyn, giving it ties to both C4 countrygaze and straighter jangle/power-pop rock.",
    lineage_basis="Documented", key_tracks=["The Secret To Good Living"], priority="Deep cut", start_here="", terry="https://www.noexpectations.fyi/p/abbey-blackwell-robber-robber-hiding-places-john-andrews-yawns",
    sources=["https://www.noexpectations.fyi/p/abbey-blackwell-robber-robber-hiding-places-john-andrews-yawns"], confidence="Medium",
    borderline_note="Band explicitly avoids the twang/shoegaze sound of its scene; placed in C7 as closest fit with C4 noted secondary given shared scene ties.")

with open("/home/claude/work/staging/lane_SW4.jsonl", "a", encoding="utf-8") as f:
    for r in rows:
        f.write(json.dumps(r, ensure_ascii=False) + "\n")

print(f"wrote {len(rows)} rows")
