import sys,re,os
W="/home/claude/work"
HEAD=("FIRST: read {W}/agent_web_override.md — web access is ONLY via the Firecrawl connector tools "
 "(mcp__Firecrawl__firecrawl_scrape / mcp__Firecrawl__firecrawl_search; load them with ToolSearch if needed). "
 "Do not load the firecrawl-research skill, do not use the CLI, WebSearch or WebFetch. You are lane agent \"{L}\". "
 "Budget: {S} searches, {P} scrapes. Stop when spent. Save sources to {W}/research/{L}/, facts to {W}/research/{L}/notes.md, "
 "failures to {W}/research/gaps.md prefixed [{L}]. Check {W}/research/ for an existing file before every scrape. Do not retry errors.\n\n"
 "SECOND: read {W}/agent_brief.md and follow it exactly EXCEPT its §6 (replaced by the override).\n\n")
def build(lane, S=10, P=40, extra="", src=None):
    body=open(src or f"{W}/prompts/prompt_{lane}.txt").read()
    body=re.sub(r"^FIRST:.*?\n\nSECOND:.*?\n\n","",body,flags=re.S)
    body=re.sub(r"^Read /home/claude/work/agent_brief.md first.*?\n\n","",body,flags=re.S)
    body=body.replace("the firecrawl","the Firecrawl")
    return HEAD.format(W=W,L=lane,S=S,P=P)+(extra+"\n\n" if extra else "")+body
if __name__=="__main__":
    lane=sys.argv[1]; S=int(sys.argv[2]); P=int(sys.argv[3]); extra=open(sys.argv[4]).read() if len(sys.argv)>4 else ""
    out=build(lane,S,P,extra); open(f"{W}/prompts3/{lane}.txt","w").write(out); print(len(out))
