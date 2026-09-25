import json,sys
lanes={l['id']:l for l in json.load(open('/home/claude/work/skeleton/lanes.json'))}
asg=json.load(open('/home/claude/work/lane_assignments.json'))
def prompt(lane_id):
    l=lanes[lane_id]; a=asg[lane_id]
    return f"""Read /home/claude/work/agent_brief.md first and follow it exactly (schema, vocabularies, verification rules, own-words descriptions, INCREMENTAL appends in batches of ~10 rows).

YOUR ASSIGNMENT — lane {lane_id}: {l['name']} (zone: {l['zone']}; era: {l['era']}).
Definition: {l['definition']}
Parent lanes: {', '.join(l['parents']) or 'none'}. Child lanes: {', '.join(l['children']) or 'none'}.
Layers to cover: {a['layers']}.
Target: about {a['target']} verified albums (a floor, not a cap — keep going while you find records that fit and can be verified; stop when new searches mostly return albums you already have).
Seed artists and records (starting points, NOT verified facts — verify everything, drop what you cannot verify, and add artists the seeds miss): {a['seeds']}
Discovery and verification sources: {a['sources']}
Notes: {a['notes']}

Output file: /home/claude/work/staging/lane_{lane_id}.jsonl (JSON Lines, schema in the brief). primary_lane must be "{lane_id}" for every row unless an album clearly belongs to another lane — in that case set the right primary_lane and add a borderline_note. Mark 1–2 albums start_here="Y". Give every row 3–6 descriptors from the tag list, a 2–4 sentence own-words description, a lineage sentence naming artists, 1–3 real key tracks, and 1–3 verification URLs you actually opened. Use discography pages to verify many albums per fetch. Then run: python3 /home/claude/work/tools/validate_staging.py /home/claude/work/staging/lane_{lane_id}.jsonl and fix every problem until it prints OK.

Reply with a SHORT summary only (no rows): row count, needs_verification count, artists covered, judgment calls, up to 10 artists that belong in OTHER lanes (with lane id), and scene/label facts worth recording."""
if __name__=="__main__":
    print(prompt(sys.argv[1]))
