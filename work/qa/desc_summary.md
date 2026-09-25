# Description review: sample results (spec §8 step 6)

Sample: 285 rows (`desc_sample.jsonl`). Per-row results are in `desc_result.jsonl`.

| Verdict | Count |
|---|---|
| ok | 166 |
| rewrite | 110 |
| flag | 9 |

**Rows with problems: 119 of 285 (41.8%).** 110 are fixed with supplied rewrites. 9 are flagged because they need research.

## Most common problem types (counted per problem; one row can have several)

1. **Factual errors (64).** These are wrong dates or sequences, wrong credits or members, tracks placed on the wrong album, anachronistic lineage, and internal contradictions. Examples:
   - A0286: Chesnutt died the same year as the album, not the year after.
   - A1204: the Winkler case happened in Tennessee, not Alabama. Tucker left in 2012.
   - A1355: 'Mykonos' is not on the LP.
   - A0058: Wurster did not play on the record.
   - A0912: Glaser did not co-write 'Good Hearted Woman'.
   - A0784: Barn did not win a Grammy.
2. **Unsupported hard facts (32).** These are awards, chart claims, press praise and personnel the row cannot support, plus unverifiable quotes. Examples:
   - A1753: a Christgau quote.
   - A0350: a Dolly Parton quote.
   - A1629: year-end lists and a TV slot.
   - A1976: a string arranger who is probably invented.
3. **Lineage basis (29).** These are resemblance-only claims ("draws on", "same lineage as", "X-indebted") marked Documented. They are reset to Inferred, or to Both where a documented part is also present.
4. **Source leakage (13).** The critic "Josh Terry" / "Terry" is cited as the authority in the prose, sometimes with no full name and once with a personal-friendship claim (A1780).
5. Minor issues: typos and formatting (6), one-sentence descriptions that are too short (5), and thin or non-specific text (2: A2226, A2760).

No row reads as pasted review text, and no quote is over 10 words. The quote problems are about whether the quotes are real, not how long they are.

## Example ids
- **A1204** (rewrite): wrong state for the true-crime song and wrong year for a member leaving.
- **A0784** (rewrite): Grammy win that did not happen.
- **A1780** (rewrite): critic name and a personal biography claim in the description. Resemblance lineage marked Documented.
- **A1753** (rewrite): unverifiable attributed Christgau quote, plus resemblance lineage marked Documented.
- **A0503** (flag): Guy Picciotto as co-producer of Jamboree is doubtful, and the lineage depends on it.

## Flagged (need research)
A0706, A1041, A0675, A2226, A2760, A0503, A1712, A0624, A1899.

## Recommendation
An error rate of about 42% in the sample suggests similar problems across the full set. Before publishing:
- Strip all "Terry" references.
- Scan for award, chart, "critics called" and "reportedly" claims.
- Re-check lineage_basis wherever the lineage text uses "draws on", "indebted", "same lineage as" or "descendant".
