QA14 verification notes - Discogs master/release searches used as independent cross-check for
Wikipedia-sourced rows; Wikipedia used as independent cross-check for Bandcamp-sourced rows where
a Wikipedia page existed; otherwise the row's own cited Bandcamp page was re-scraped (independent=false).

Key finding 1 (FIX): A2409 Sunday Mourners "A-Rhythm Absolute" - row says label "Self-released" but
the album's own Bandcamp page states label "Curation Records". Year (2026) and track listing confirmed correct.

Key finding 2 (note, ok): A2430 Remember Sports "Sunchokes" (2014) - Discogs master lists this album
credited to the artist name "Sports" (2014), the band's name before they renamed to "Remember Sports".
Album title and year are correct; same continuous band/release, so kept as "ok" with a note.

Everything else checked (Mac DeMarco, RBCF, Nap Eyes, Snail Mail, Soccer Mommy, Real Estate, Speedy Ortiz,
Swearin', Radiator Hospital, Pardoner, Parquet Courts, Twerps, Terry, NE-HI, This Is Lorelei, Twin Peaks,
Zook, Video Age, The Tubs, Dan Wriggins, Tre Burt, Real Companion, Jobi Riccio, Ruston Kelly, and the full
X9-X13 lane: MBV, Slowdive, Ride, Cocteau Twins, Swirlies, Lush, Chapterhouse, Pale Saints, Wire, Mission of
Burma, Big Black, Fugazi, Protomartyr, Indigo De Souza, Blackberry Smoke, Whiskey Myers, Allman Betts Band,
Steel Woods, Larkin Poe, Kacey Musgraves, Orville Peck, CMAT, Beyoncé, Mitski, Post Malone, Joni Mitchell,
CSN, Jackson Browne, Eagles, Linda Ronstadt, Harry Nilsson) matched on title, year, label and type against
Discogs master/release search pages (direct URL, no firecrawl_search calls used).

No gaps/errors/429s encountered. All scrapes returned 200 except one expected 404 (Pardoner band wiki page,
worked around via Discogs).
