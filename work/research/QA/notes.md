# QAanchor lane notes (independent re-verification of batch_anchor.jsonl)
Checked 48 rows across MJ Lenderman/Wednesday/Big Thief/Adrianne Lenker/Buck Meek/villagerrr/Greg Freeman (+related Snocaps, Diva Sweetly).
Result: 34 ok, 13 fix, 0 fail, 1 unchecked.
Full source list and per-row notes are in /home/claude/work/qa/result_anchor.jsonl.
Key finding pattern: several rows used the ALBUM/EP TITLE as a "key track" when no song of that name
actually appears on the release (Guttering, yep definitely, Wednesday EP, Mowing the Leaves..., Snocaps,
In The Living Room, a-sides, b-sides). Also found two apparent cross-album track swaps for MJ Lenderman
(Ghost of Your Guitar Solo <-> Boat Songs) and Wednesday (I Was Trying to Describe You to Someone got
tracks that belong to Twin Plagues / Rat Saw God).
