# No Expectations crawl — agent brief

You are crawling one slice of Josh Terry's newsletter *No Expectations* (noexpectations.fyi) to harvest album leads for an album atlas of indie twang, slacker rock, alt-country, cosmic country, indie folk, slowcore, jangle/power pop, and their ancestors (Neil Young, No Depression, Drag City, SST-era college rock, country rock, outlaw country, etc.). Read `/home/claude/work/skeleton/lanes.json` once so you know the 54 lane ids.

## What to do
1. Read your slice file (a JSON list of posts with date, title, url). Open EVERY post in it with WebFetch. Use a prompt like: "List every album (artist — title, year if given, label if given) that the author recommends, reviews, ranks, or discusses, with the section it appears in (year-end list rank, weekly 'What I listened to' / new-album reviews, playlist, interview, discography deep dive, taste profile, albums-I-missed). For each, give one sentence on what he says about the sound. Also list any older artists or albums named as influences or comparisons." Paid-only posts may show only a preview; capture what is visible and mark `paywalled: true`.
2. For each album lead, decide whether it plausibly belongs anywhere in the V (Core, V, or Context lanes). Include everything from the indie rock / folk / country / roots / slacker / slowcore / jangle / psych-country sphere. Exclude clearly out-of-scope genres (rap, jazz, electronic, metal, mainstream pop, jam bands like Goose/Phish/Dead & Company shows, King Gizzard) unless the post explicitly frames them as twangy, folky, or slacker. When unsure, include with `lane_guess: "?"`.
3. Write leads as JSON Lines to your assigned output file. One object per (album, post) pair — the same album can appear in several posts; write a line for each post it appears in.

## Lead schema
```
{"artist": "Wednesday", "album": "Rat Saw God", "year": 2023, "label": "Dead Oceans",
 "terry_url": "https://www.noexpectations.fyi/p/the-60-best-albums-of-2023", "post_date": "2023-12-07",
 "context": "Year-end list #1",            # e.g. "Year-end list #12", "Mid-year list", "New album review", "Playlist", "Interview", "Taste Profile", "Albums I missed", "Discography deep dive", "Passing mention"
 "note": "one sentence in YOUR OWN words summarizing what Terry says about the sound (no quotes over 10 words)",
 "lane_guess": "C4",                        # lane id, "?" if unsure, "OUT" if clearly outside the V but you still logged it
 "influences_named": ["Neil Young", "Drive-By Truckers"],   # upstream artists/albums the post names as reference points, else []
 "paywalled": false}
```
Year and label may be null if the post does not state them and you did not verify them — do NOT guess. (Verification happens later; your job is coverage of the archive.)

## Rules
- Do not skip posts. Every URL in your slice must be opened. If a fetch fails, retry once, then log it in a final line `{"fetch_failed": true, "terry_url": "..."}`.
- No invented albums: only log what the post actually names.
- Also produce, at the end of your file, one line per post: `{"post_summary": true, "terry_url": "...", "post_date": "...", "kind": "year-end list | mid-year list | weekly | playlist | interview | taste profile | deep dive | essay", "album_count": N}`.
- Reply with a SHORT summary: posts opened, posts failed/paywalled, total leads, and the 15 most-recurring artists in your slice. Do not paste the rows.
