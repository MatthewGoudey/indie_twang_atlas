# Web access override (session 3) — READ THIS; it replaces §6 of agent_brief.md

The Firecrawl CLI cannot reach the network from this container (egress proxy returns 403), and curl/wget/python web access is also blocked. The built-in WebSearch/WebFetch are rate-limited and forbidden. The ONLY working web access is the **Firecrawl connector tools**:

- `mcp__Firecrawl__firecrawl_scrape`
- `mcp__Firecrawl__firecrawl_search`

If they are not in your tool list, load them first with ToolSearch: `select:mcp__Firecrawl__firecrawl_scrape,mcp__Firecrawl__firecrawl_search`.
Do NOT load the firecrawl-research skill (its CLI instructions do not work here).

## How to use them (keep context small)

1. **Discography / fact extraction (preferred, compact):** scrape with
   `formats: ["query"]`, `onlyMainContent: true`, and
   `queryOptions: {"prompt": "List every studio album, EP and live album with its release year and record label, exactly as stated on the page.", "mode": "freeform"}`.
   Adapt the prompt when you need something else (e.g. "track listing of <album>", "year and label of <album>", "which albums are listed in this year-end list with their artists"). This costs 5 credits and returns only the answer. Credits are plentiful; context is not.
2. **Full page** (only when you truly need prose, e.g. a review for description details): `formats: ["markdown"]`, `onlyMainContent: true`. Avoid on long pages.
3. **Search:** `firecrawl_search` with `sources: ["web"]`, `limit: 5`, `domainTools: false`. Use it only when you do not know the URL. Wikipedia URL patterns (`https://en.wikipedia.org/wiki/Artist_Name`, `..._discography`, `..._(band)`, `..._(musician)`) are usually safe to try directly. Bandcamp: `https://<artist>.bandcamp.com/music`.
4. A result with `"statusCode": 404` means the page does not exist — try the other pattern once, then search.

## Cache rules (unchanged in spirit)

- Before any scrape, grep `/home/claude/work/research/` for the URL (other lanes' files count). If a file exists, read it instead.
- After every successful scrape, immediately save what you got with the Write tool to `/home/claude/work/research/<lane>/<slug>.md` with this header, then the answer/markdown you received (for query results, save the answer text verbatim):
```
---
url: <url>
title: <page title>
fetched: 2026-09-25
lane: <lane>
why: <one line>
mode: query | markdown
---
```
- Keep `/home/claude/work/research/<lane>/notes.md` (album | year | label | source slug | n sources).
- Any error, 429, timeout: do not retry; append `- [<lane>] <url> | <error> | needed for: <what>` to `/home/claude/work/research/gaps.md`.

## Budget

Your prompt states a budget as searches / scrapes. Count query-mode scrapes as scrapes. Stop when spent.

## Sources field

The URL in each row's `sources` must be a page you (or another agent, per the cache) actually scraped. The url in the research file header is what you cite.
