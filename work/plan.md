# The V — Album Atlas: working plan

Project root: /home/claude/work (staging, checkpoints, logs, sources, tools).
Deliverables go to /mnt/user-data/outputs/ (V_Album_Atlas.xlsx, V_Map.docx) and are also copied under work/deliverables/.

## Inputs
- User prompt (§0–§10) — the spec. Copied to work/spec_notes.md (key rules only).
- Field guide: work/sources/Slacker_Rock_Alt_Country_Field_Guide.xlsx (156 artist rows incl. 3 Unplaced; Roots sheet, Labels sheet). Never modified.
- No Expectations archive index: work/sources/noexpectations_index.json (172 posts, 2022-11-22 → 2026-09-24; 164 public, 8 paid).

## Controlled vocabularies (from the field guide + spec)
- Regions (10 + Elsewhere): The Carolinas; Philadelphia; Chicago and the Midwest; Texas and Oklahoma; The Northeast; Burlington, Vermont; The South; The West; Australia and New Zealand; The UK, Ireland and Canada; Elsewhere.
- Styles: Crossover, Alt-country, Cosmic country, Slacker, Slowcore, Lo-fi, Jangle, Power pop, Indie folk, Punk, Noise, Shoegaze, Southern rock, Honky-tonk, Cowpunk, Country folk + extensions Country rock, Outlaw, Classic country, Mainstream country, Bluegrass, Heartland rock, Emo, Post-punk, Folk rock, Dream pop.
- Lanes: C1–C9 (Core), V1–V30 + R1 (V), X1–X14 (Context). Definitions in work/skeleton/lanes.json.
- Tags: work/skeleton/tags.json.

## Layers (by year): L1 2014–2026 · L2 1998–2013 · L3 1987–1997 · L4 1978–1986 · L5 1965–1977 · L6 <1965

## Phases and sub-agent split
- Phase 0 Setup (done by orchestrator): folders, plan, state, fieldguide_mapping.csv, agent brief, staging validator.
- Phase 1 Skeleton (orchestrator + lane agents' notes): lanes.json, scenes.json, labels.json, tags.json. Exit: every Core lane traces to L5/L6.
- Phase 2 Core harvest:
  - 2a: 6 No Expectations crawl agents (by date slice) → staging/terry_leads_*.jsonl (leads with URL, not full rows).
  - 2b: 9 Core-lane agents (C1..C9) → staging/core_C*.jsonl full rows; anchor-artist agent (Lenderman, Wednesday, Hartzman, Villagerrr, Big Thief/Lenker/Meek, Greg Freeman) → staging/core_anchors.jsonl.
  - 2c: network pass agents (labels: Dear Life, Sophomore Lounge, Curation, Keeled Scales, Lame-O, Exploding in Sound, Fire Talk, Paradise of Bachelors; Terry-leads sweep; field-guide completion).
  - QA loop.
- Phase 3 L2 Bridge: V1, V2 (1998+), V3, V4, V5, V6, V7 (2012+), V8 (1998+) + L2 tails of older lanes (V20 Neil 1998+, V13, V16, V17, V18, V10, V11, V12 late).
- Phase 4 L3 Nineties: V9, V10, V11, V12, V13, V2 (1990–97), V16 (1987–91), V17 (1987–95), V18 (1987–95), V19, V20, V1 (1996–97), V3 (1996–97).
- Phase 5 L4 Underground: V14, V15, V16, V17, V18, V19, V20, V8, V11 (1985–86), V24, V26, V13 (1986).
- Phase 6 L5 Classic + R1: V20, V21, V22, V23, V24, V25, V26, V27, V28, V29, V30, V8, R1.
- Phase 7 Context: X1–X14 (4 agents).
- Phase 8 Global QA; Phase 9 xlsx; Phase 10 docx; Phase 11 audit.

## Staging schema
One JSON object per line (JSONL). See work/agent_brief.md and work/tools/validate_staging.py.

## Merge rules
- Orchestrator merges staging → work/master.jsonl, dedups on (normalized artist, normalized title), assigns IDs A0001+ in order of merge, computes Layer from Year, checks Zone = lane zone.
- Checkpoints: work/checkpoints/master_phaseN.jsonl after every phase.

## Deliverable format change (user request, session 3)
The V Map is now authored as Markdown: `deliverables/V_Map.md` (+ `deliverables/figs/`), built by `tools/build_md.py`
from master.jsonl, essays/*.json and sheets/*.json, and converted to PDF with `tools/md_to_pdf.py V_Map.md`
(python-markdown → print-styled HTML → headless Chromium; `pandoc V_Map.md -o V_Map.pdf` also works where LaTeX is installed).
Future iterations: produce V_Map.md + V_Map.pdf; the .docx (tools/build_docx.js) is legacy and optional.
