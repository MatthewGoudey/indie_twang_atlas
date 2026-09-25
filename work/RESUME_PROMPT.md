# Resume prompt — "The V" Album Atlas (paste this into the new session)

You are resuming a large, partly finished research-and-build project. Everything you need is in the attached bundle. Unpack it into your working directory so that the folder `work/` sits at the top level (e.g. `tar xzf V_atlas_handoff.tar.gz`). The user's original field guide is at `work/sources/Slacker_Rock_Alt_Country_Field_Guide.xlsx` — read it, never modify it.

## 1. Read these first, in this order

1. `work/spec.md` — the full original specification (§0–§10). It is the contract: lanes, layers, zones, floors, deliverable specs, phases, error-correction loop, writing rules, final report. Follow it exactly. Do not stop to ask the user questions; decide judgment calls using its §2–§4, log them, and keep going.
2. `work/state.json` — per-phase status, `web_access` notes, and `resume_instructions`. You are resuming from the last unfinished phase, not starting over.
3. `work/logs/` — short logs of what happened in the previous session (read `progress_2.md` and `progress_interrupt.md`).
4. `work/plan.md` — the working plan and merge rules.
5. `work/agent_brief.md` — the brief every research sub-agent reads (row schema, controlled vocabularies, verification and writing rules, Firecrawl-only web access). Keep using it as-is.
6. `work/skeleton/lanes.json`, `tags.json`, `vocab.json` — the 54 lanes with definitions/parents/children, the 50-tag descriptor vocabulary, and the controlled vocab (regions, styles, types, priorities).
7. `work/lane_assignments.json` — per-lane research specs (targets, layers, seeds, sources, notes) for V1–V30 and R1. Core (C1–C9) and Context (X1–X14) specs still need to be written in the same shape; use the spec's §3 seed lists plus `work/sources/terry_by_lane/<lane>.txt`.
8. Your xlsx and docx skills (read their SKILL.md before Phases 9–10, as the spec requires).

## 2. Web access — read this carefully

The built-in WebSearch and WebFetch tools are rate-limited at the account level and broke the previous session. Do not use them. Use the `anthropic-skills:firecrawl-research` skill (load it with the Skill tool). It carries the Firecrawl CLI setup, the API key export line, budgets, file conventions, and the multi-agent wave rules. Verified plan facts: Standard plan, 50 concurrent browsers, ~100k credits/month (about 101k remaining at handoff), 1 credit per scraped page, 2 per 5-result search.

Operating rules that worked:
- Every research sub-agent loads the skill itself, then reads `work/agent_brief.md`, then its assignment file in `work/prompts/`.
- Give each lane agent an explicit budget: default 10 searches / 40 scrapes / 20 map calls; raise to 12 / 60 for big lanes (V4, V6, C5, C6, C7).
- Launch agents in waves of 5–6 (never more than 8) and wait for a wave to finish before the next. If any agent reports a Firecrawl 429, drop the next wave to 3.
- Sonnet-class sub-agents did this work well and cheaply; keep using them for lane research. Use your strongest model for triage, QA re-checks, and the essays.
- Agents write pages to `work/research/<lane>/`, facts to `work/research/<lane>/notes.md`, failures to `work/research/gaps.md`. Before any scrape, grep `work/research/` for the URL — never fetch a page twice. The cache already holds ~250 pages (V1, V4, V5, V6, V8, V9, V11 folders).
- Agents append rows to `work/staging/lane_<ID>.jsonl` incrementally (batches of ~10) and run `python3 work/tools/validate_staging.py <file>` until it prints OK. They never touch `work/master.jsonl`.

## 3. Where the project stands (as of handoff)

Done:
- Phase 0 and Phase 1 skeleton (lanes, tags, vocab, `fieldguide_mapping.csv` with all 156 field-guide artists → draft lanes).
- No Expectations: full archive indexed (`sources/noexpectations_index.json`, 172 posts) and crawled (`staging/terry_leads_*.jsonl`, 2,925 leads; `sources/terry_albums_distinct.json`, 1,011 distinct albums; every one triaged to a lane in `sources/terry_triage_output.tsv`; per-lane must-consider lists in `sources/terry_by_lane/`). The Core agents must treat their lane's file there as a checklist and fill the `terry` field.
- Lane research staged (rows / needs_verification): V20 65, V21 55, V22 36, V23 51, V24 48, V25 48, V26 72, V27 23, V28 40, V29 29, V30 28, R1 32/3, V8 51/1, V14 49, V15 34, V16 96/6, V17 61, V18 49/8, V19 38/2, V13 72/6, V10 77/26, V12 73, V2 69/12, V11 68, V3 63/19, V9 69, V4 47, V5 58, V1 14.
- `work/master.jsonl`: 1,511 merged, deduplicated rows with provisional IDs (A0001+). Layer×zone so far: L1 Core 3, L1 V 91, L2 V 320, L3 V 437, L4 V 229, L5 V 384, L6 V 47. `work/needs_verification.jsonl`: 84 candidates.
- One resolved gap not yet applied: Chuck Johnson – Blood Moon Boulder (2015, Scissor Tail Editions; see `work/research/notes.md`) and Michael Chapman – Rainmaker (1969, Harvest; `work/research/V8/wikipedia-michael-chapman-singer.md`) can be promoted from needs_verification to V8/V30 rows.

Not done (in order):
1. **Top-ups** (append to existing files; read them first; do not duplicate): V1 (14 → ~40), V4 (47 → ~100), V5 (58 → ~65), V9 (69 → ~85), V10 (resolve its 26 needs_verification lines and add the unreached seed artists: Stephen Malkmus, Beulah, The Minders, Pedro the Lion, Death Cab, The Shins, 764-HERO, Van Pelt, etc.), V2 (12 nv), V3 (19 nv — Sarah Shook belongs in V6, Lee Bains III, Austin Lucas, later Lucero).
2. **V6** — fresh run (the previous agent errored before writing anything). **V7** — not started. Prompts exist: `work/prompts/prompt_V6.txt`, `prompt_V7.txt`.
3. **Core C1–C9** — write assignments in the same shape as `lane_assignments.json` (targets: C1 ~80, C2 ~45, C3 ~75, C4 ~30, C5 ~90, C6 ~90, C7 ~110, C8 ~35, C9 ~25). Each Core agent must (a) work through `sources/terry_by_lane/C<n>.txt`, (b) cover every field-guide artist mapped to its lane in `fieldguide_mapping.csv`, (c) complete each artist's discography within the lane, (d) use Bandcamp/label pages for verification.
4. **Anchor-artist completion** (one agent): MJ Lenderman, Wednesday, Karly Hartzman, Villagerrr, Big Thief + Adrianne Lenker + Buck Meek, Greg Freeman — every studio album, notable EP, live album, side project. (Neil Young is already complete in V20.)
5. **Network pass** (one or two agents): label catalogs (Dear Life, Sophomore Lounge, Curation, Keeled Scales, Lame-O, Exploding in Sound, Fire Talk, Paradise of Bachelors, Ruination, Orindal, Run for Cover's twangier end), side projects, pedal-steel session players (Xandy Chelmis, Red PK, Spencer Cullum), "for fans of" chains; plus the 26 "?" and any relevant OUT items in the Terry triage.
6. **Context X1–X14** (3–4 agents, 8–20 albums per lane, each with a Lineage note on where the branch diverges). Field-guide scene-not-sound artists go here: Indigo De Souza, Robber Robber → X10; Swirlies, My Bloody Valentine → X9; CMAT → X12.
7. **Needs Verification resolution** (one agent with Firecrawl): work through `work/needs_verification.jsonl`; promote what verifies, keep the rest for the Needs Verification sheet.
8. **Error-correction loop** per phase (spec §8): facts, independent 15% + all-Medium re-check by an agent that did not write the rows, dedup/normalize, consistency, coverage vs canon sources, description review. Log each run for the QA Log sheet.
9. **Phase 8 global QA**, then **Phase 9** build `V_Album_Atlas.xlsx` (spec §7.1, 12 sheets, dropdowns, formulas, recalc with the xlsx skill's `recalc.py`), **Phase 10** write `V_Map.docx` (spec §7.2; graphviz is available for the lineage diagrams; delegate lane essays to agents in groups with the album lists and IDs, then assemble with docx-js), **Phase 11** audit, then the chat report in spec §10.

Merge procedure (orchestrator only): after each wave, re-run the merge in `work/logs/progress_2.md` style — read all `staging/lane_*.jsonl`, drop needs_verification lines to `needs_verification.jsonl`, dedupe on normalized (artist, album) keeping the first occurrence, assign IDs A0001+ in file order, set layer from year (R1 always L6), set zone from the primary lane, write `master.jsonl`, checkpoint to `work/checkpoints/`, update `state.json`, append to `work/logs/`. IDs become final only at Phase 8.

## 4. Things learned that save time

- The staging validator flags any double-quoted span over 60 characters in descriptions; agents should put song titles in single quotes.
- Substack's archive JSON (`/api/v1/archive?sort=new&offset=N&limit=12`) enumerates No Expectations; post pages are fetchable but long year-end lists get truncated by summarizing fetchers — Firecrawl `scrape -o` to disk avoids that.
- Wikipedia "<Artist> discography" pages verify a whole catalog in one credit; Bandcamp artist pages do the same for Core artists.
- Region vocabulary is the field guide's: The Carolinas; Philadelphia; Chicago and the Midwest; Texas and Oklahoma; The Northeast; Burlington, Vermont; The South; The West; Australia and New Zealand; The UK, Ireland and Canada; plus Elsewhere. Neil Young is filed under "The UK, Ireland and Canada" because the field guide does that.
- Known cross-lane duplicates dropped at merge (keep first): The Connells – Boylan Heights (V16/V17), Bobby Charles (V21/V22), Nanci Griffith ×2 (V19/V24).
- Rulings applied so far worth keeping: Purple Mountains → C2 (spec ruling); Low's Double Negative and Duster's 2019 reunion → C8 primary / V12 secondary; Cowboy Junkies → V12 with V9 secondary; Michael Hurley's 1970s records → V2 with a year borderline note; Wild Pink Still Coming Down → C1 by sound; Weezer, Radiohead, Vampire Weekend, King Gizzard, jam-band live shows → OUT.

Deliverables go to `/mnt/user-data/outputs/` (or wherever the new session delivers files) and a copy under `work/deliverables/`. Finish with the final report described in spec §10.
