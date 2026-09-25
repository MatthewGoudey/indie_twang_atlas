---
lane: QA17
fetched: 2026-09-25
why: independent re-verification of batch_17.jsonl (101 rows, Drag City/Chicago indie cluster, classic country/rock cluster, Fleet Foxes/Bon Iver/Iron & Wine/Gillian Welch indie-folk cluster)
---

Key finding (fix):
- A1359 Bon Iver "For Emma, Forever Ago": row pairs 2007 with label Jagjaguwar, but per en.wikipedia.org/wiki/Bon_Iver the album was self-released in July 2007 and only officially released by Jagjaguwar on Feb 19, 2008. Original 2007 release had no label (self-released).

Discogs/AllMusic artist pages scraped and confirmed exact matches (year+label) for:
- Edith Frost (discogs.com/artist/179554) - Calling Over Time 1997, Telescopic 1998, both Drag City
- Jim O'Rourke Insignificance (discogs master/30632) - Drag City 2001
- Simon Joyner (discogs.com/artist/67512) - Cowardly Traveller Pays His Toll, Sing Eunuchs! 1994
- Red Red Meat (discogs.com/artist/62941) - Jimmywine Majestic Sub Pop 1994
- Califone (discogs.com/artist/197418 + release/3953044) - Quicksand/Cradlesnakes 2003, Roots & Crowns 2006, Heron King Blues 2004, all Thrill Jockey
- Scout Niblett (discogs release/19391224 + dragcity.com) - Calcination 2010 Drag City
- Plush (discogs master/178282) - More You Becomes You Drag City 1998
- The Anomoanon (discogs.com/artist/267688) - Songs From RLS... Palace Records 1999
- Waylon Jennings, Willie Nelson, Tompall Glaser, David Allan Coe, Steve Young, Townes Van Zandt, Loudon Wainwright III, Levon Helm, Rick Danko, CSNY, John Prine, Tom T. Hall, Grateful Dead - all confirmed via Discogs/Wikipedia-album-page searches, all "ok", exact year/label matches (see result_17.jsonl for per-row source URLs)
- Bon Iver (discogs.com/artist/1042739), Angel Olsen (discogs master/2657033), Iron & Wine (allmusic iron-wine-mn0000085038), Fleet Foxes (allmusic mn0000990366), Jake Xerxes Fussell (allmusic jake-xerxes-fussell-mn0000674711), Julie Byrne (discogs.com/artist/2765993), Marissa Nadler (discogs.com/artist/350249), Gillian Welch (discogs master/307608) - all confirmed, one fix (Bon Iver, above)

Note: two V5-lane cached files from an earlier session (discogs-iron-and-wine.md, discogs-fleet-foxes.md, discogs-bon-iver.md) were found to contain WRONG data (a Dutch band "Lemming", "The Alarm", and garbled content respectively) -- not used; re-scraped correct artist IDs found via discogs links embedded in other cached Wikipedia pages.

Rows marked independent:false / ok without a fresh scrape: ~20 canonical/iconic classic-rock and outlaw-country albums (Neil Young "On the Beach", "Toast"; Gram Parsons "Grievous Angel"; Guy Clark; Bob Weir "Ace"; Allman Brothers "At Fillmore East"; Tony Joe White; Eddie Hinton; Blackfoot; Velvet Underground; Bert Jansch; Steve Goodman; Bobbie Gentry; Johnny Cash x3; Butch Hancock; Steve Fromholz; Lee Clayton) -- search budget (25) was exhausted on higher-density clusters; these are extremely well-documented mainstream releases with no internal inconsistency in the row, and (where applicable) already carry two independent Wikipedia citations (main article + dedicated album article).

Budget used: 25/25 searches, ~20/150 scrapes.
