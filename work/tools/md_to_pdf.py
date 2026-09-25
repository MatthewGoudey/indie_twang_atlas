#!/usr/bin/env python3
"""Convert a Markdown file (e.g. V_Map.md) to PDF: Markdown -> styled HTML -> headless Chromium print.
Usage: python3 md_to_pdf.py V_Map.md [V_Map.pdf]
Needs: pip install markdown; Node with playwright (or any Chromium). Alternatively: pandoc V_Map.md -o V_Map.pdf."""
import sys, os, re, subprocess, markdown

src = os.path.abspath(sys.argv[1])
pdf = os.path.abspath(sys.argv[2]) if len(sys.argv) > 2 else re.sub(r"\.md$", ".pdf", src)
text = open(src, encoding="utf-8").read()
text = re.sub(r"^---\n.*?\n---\n", "", text, flags=re.S)  # drop YAML front matter
body = markdown.markdown(text, extensions=["tables", "sane_lists", "attr_list", "md_in_html"])
css = """
@page { size: Letter; margin: 0.8in 0.85in; @bottom-center { content: counter(page); font: 9pt Arial; color: #888; } }
@page wide { size: Letter landscape; margin: 0.4in; }
body { font-family: Arial, Helvetica, sans-serif; font-size: 10.5pt; line-height: 1.45; color: #1f2328; }
h1 { font-size: 21pt; color: #2B3A4A; margin: 0 0 12pt; }
h2 { font-size: 14.5pt; color: #7A4A1C; margin: 18pt 0 6pt; break-after: avoid; }
h3 { font-size: 12.5pt; color: #2B3A4A; margin: 14pt 0 4pt; break-after: avoid; }
p { margin: 0 0 8pt; } li { margin-bottom: 3pt; }
code { font-family: Arial, sans-serif; font-size: 8.5pt; color: #7A4A1C; background: none; }
em { font-style: italic; }
table { border-collapse: collapse; margin: 6pt 0 12pt; font-size: 9.5pt; }
th { background: #3B4A5A; color: #fff; text-align: left; padding: 4pt 8pt; }
td { border: 1px solid #ccc; padding: 4pt 8pt; }
img { max-width: 100%; }
.pagebreak { break-after: page; }
.landscape { page: wide; } .landscape img { width: 100%; }
"""
html = f"<!doctype html><html><head><meta charset='utf-8'><title>The V</title><style>{css}</style></head><body>{body}</body></html>"
tmp = re.sub(r"\.pdf$", ".html", pdf)
open(tmp, "w", encoding="utf-8").write(html)
js = f"""
const {{ chromium }} = require('playwright');
(async () => {{
  const b = await chromium.launch();
  const p = await b.newPage();
  await p.goto('file://{tmp}', {{ waitUntil: 'load' }});
  await p.pdf({{ path: '{pdf}', preferCSSPageSize: true, printBackground: true,
    displayHeaderFooter: true, headerTemplate: '<span></span>',
    footerTemplate: '<div style="font:9px Arial;color:#888;width:100%;text-align:center"><span class="pageNumber"></span></div>',
    margin: {{ top: '0.8in', bottom: '0.8in', left: '0.85in', right: '0.85in' }} }});
  await b.close();
}})();
"""
node_root = subprocess.run(["npm", "root", "-g"], capture_output=True, text=True).stdout.strip()
subprocess.run(["node", "-e", js], check=True, env={**os.environ, "NODE_PATH": node_root})
os.remove(tmp)
print("wrote", pdf)
