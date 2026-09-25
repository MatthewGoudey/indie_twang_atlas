// Build V_Map.docx from work/master.jsonl, work/essays/*.json, work/sheets/{scenes,labels,paths}.json,
// work/borderline_log.jsonl and the figures in work/deliverables/figs/.
// Usage: node build_docx.js [out.docx]
const fs = require("fs");
const path = require("path");
const {
  Document, Packer, Paragraph, TextRun, HeadingLevel, AlignmentType, ImageRun, PageBreak,
  Table, TableRow, TableCell, WidthType, ShadingType, BorderStyle, PageOrientation, LevelFormat,
  TableOfContents, Footer, PageNumber, Header,
} = require("docx");

const W = "/home/claude/work";
const OUT = process.argv[2] || `${W}/deliverables/V_Map.docx`;
const readJSONL = (p) => fs.existsSync(p) ? fs.readFileSync(p, "utf8").split("\n").filter(Boolean).map(JSON.parse) : [];
const readJSON = (p, d) => fs.existsSync(p) ? JSON.parse(fs.readFileSync(p, "utf8")) : d;

const rows = readJSONL(`${W}/master.jsonl`);
const byId = Object.fromEntries(rows.map((r) => [r.id, r]));
const lanes = readJSON(`${W}/skeleton/lanes.json`, []);
const L = Object.fromEntries(lanes.map((l) => [l.id, l]));
const scenes = readJSON(`${W}/sheets/scenes.json`, []);
const labels = readJSON(`${W}/sheets/labels.json`, []);
const paths = readJSON(`${W}/sheets/paths.json`, []);
const blog = readJSONL(`${W}/borderline_log.jsonl`);
const appendix = readJSON(`${W}/essays/appendix.json`, null);
const intro = readJSON(`${W}/essays/intro.json`, null);
const essay = (id) => readJSON(`${W}/essays/${id}.json`, null);

const FONT = "Arial";
const missingIds = new Set();
const citedIds = new Set();

// ---------- text helpers
// Inline markup: *italic*, **bold**, and [A0123] album references (validated against master).
function runs(text, base = {}) {
  const out = [];
  const re = /(\*\*[^*]+\*\*|\*[^*]+\*|\[A\d{4}\])/g;
  let last = 0, m;
  while ((m = re.exec(text))) {
    if (m.index > last) out.push(new TextRun({ text: text.slice(last, m.index), font: FONT, ...base }));
    const t = m[0];
    if (t.startsWith("**")) out.push(new TextRun({ text: t.slice(2, -2), bold: true, font: FONT, ...base }));
    else if (t.startsWith("[A")) {
      const id = t.slice(1, -1);
      citedIds.add(id);
      if (!byId[id]) missingIds.add(id);
      out.push(new TextRun({ text: id, font: FONT, color: "7A4A1C", size: 18, ...base }));
    } else out.push(new TextRun({ text: t.slice(1, -1), italics: true, font: FONT, ...base }));
    last = m.index + t.length;
  }
  if (last < text.length) out.push(new TextRun({ text: text.slice(last), font: FONT, ...base }));
  return out;
}
const P = (text, opts = {}) => new Paragraph({ children: runs(text), spacing: { after: 140, line: 300 }, ...opts });
const H1 = (t) => new Paragraph({ heading: HeadingLevel.HEADING_1, children: [new TextRun({ text: t, font: FONT })], pageBreakBefore: true });
const H2 = (t) => new Paragraph({ heading: HeadingLevel.HEADING_2, children: [new TextRun({ text: t, font: FONT })] });
const H3 = (t) => new Paragraph({ heading: HeadingLevel.HEADING_3, children: [new TextRun({ text: t, font: FONT })] });
const bullet = (text) => new Paragraph({ numbering: { reference: "bul", level: 0 }, children: runs(text), spacing: { after: 60 } });
const numbered = (ref, text) => new Paragraph({ numbering: { reference: ref, level: 0 }, children: runs(text), spacing: { after: 80 } });
const albumRef = (id) => {
  const r = byId[id];
  citedIds.add(id);
  if (!r) { missingIds.add(id); return `[missing ${id}]`; }
  return `${r.artist} – *${r.album}* (${r.year}) [${id}]`;
};
function img(file, widthIn) {
  const p = `${W}/deliverables/figs/${file}`;
  const buf = fs.readFileSync(p);
  const w = buf.readUInt32BE(16), h = buf.readUInt32BE(20);
  const wpx = widthIn * 96, hpx = Math.round(wpx * h / w);
  return new Paragraph({ alignment: AlignmentType.CENTER, children: [new ImageRun({ type: "png", data: buf, transformation: { width: wpx, height: hpx }, altText: { title: file, description: file, name: file } })] });
}
const border = { style: BorderStyle.SINGLE, size: 4, color: "BBBBBB" };
const borders = { top: border, bottom: border, left: border, right: border };
function table(headers, data, widths, fills) {
  const total = widths.reduce((a, b) => a + b, 0);
  const cell = (t, w, head, fill) => new TableCell({
    borders, width: { size: w, type: WidthType.DXA },
    shading: head ? { fill: "3B4A5A", type: ShadingType.CLEAR, color: "auto" } : fill ? { fill, type: ShadingType.CLEAR, color: "auto" } : undefined,
    margins: { top: 60, bottom: 60, left: 100, right: 100 },
    children: [new Paragraph({ children: head ? [new TextRun({ text: t, bold: true, color: "FFFFFF", font: FONT, size: 18 })] : runs(String(t), { size: 18 }) })],
  });
  return new Table({
    width: { size: total, type: WidthType.DXA }, columnWidths: widths,
    rows: [new TableRow({ tableHeader: true, children: headers.map((h, i) => cell(h, widths[i], true)) }),
      ...data.map((row, j) => new TableRow({ children: row.map((c, i) => cell(c, widths[i], false, fills ? fills[j] : undefined)) }))],
  });
}
const ZFILL = { Core: "FCE9D9", V: "E3EEF8", Context: "EDEDED" };

// ---------- lane essay renderer
function laneSection(id, level) {
  const l = L[id];
  const e = essay(id);
  const out = [];
  out.push(level === 2 ? H2(`${id} · ${l.name}`) : H3(`${id} · ${l.name}`));
  const count = rows.filter((r) => r.primary_lane === id).length;
  out.push(new Paragraph({ children: [new TextRun({ text: `${l.zone} zone · main era ${l.era} · ${count} albums in the atlas · fed by ${l.parents.join(", ") || "—"}`, italics: true, color: "666666", font: FONT, size: 18 })], spacing: { after: 120 } }));
  if (!e) { out.push(P(`[Essay pending for ${id}.]`)); return out; }
  for (const para of e.paragraphs) out.push(P(para));
  if (e.essentials && e.essentials.length) {
    out.push(new Paragraph({ children: [new TextRun({ text: e.essentials_label || "Essential albums", bold: true, font: FONT })], spacing: { before: 120, after: 60 } }));
    for (const x of e.essentials) out.push(bullet(`${albumRef(x.id)}${x.note ? " — " + x.note : ""}`));
  }
  return out;
}

// ---------- document body
const body = [];
// Title
body.push(new Paragraph({ spacing: { before: 2400, after: 200 }, alignment: AlignmentType.CENTER, children: [new TextRun({ text: "The V", bold: true, size: 72, font: FONT })] }));
body.push(new Paragraph({ alignment: AlignmentType.CENTER, spacing: { after: 400 }, children: [new TextRun({ text: "A map of indie twang, slacker rock, and everything that fed them", size: 30, font: FONT, color: "555555" })] }));
body.push(new Paragraph({ alignment: AlignmentType.CENTER, children: [new TextRun({ text: `Companion to V_Album_Atlas.xlsx · ${rows.length.toLocaleString()} albums · 54 lanes · September 2026`, size: 20, font: FONT, color: "777777" })] }));
body.push(new Paragraph({ children: [new PageBreak()] }));
body.push(new Paragraph({ children: [new TextRun({ text: "Contents", bold: true, size: 32, font: FONT })], spacing: { after: 200 } }));
body.push(new TableOfContents("Contents", { hyperlink: true, headingStyleRange: "1-2" }));

// 1. How to read this
body.push(H1("1. How to read this"));
if (intro) for (const p of intro.paragraphs) body.push(P(p));
const layerRows = [["L1 Now", "2014–2026"], ["L2 Bridge", "1998–2013"], ["L3 Nineties", "1987–1997"], ["L4 Underground", "1978–1986"], ["L5 Classic", "1965–1977"], ["L6 Roots", "before 1965"]];
const cnt = (ly, z) => rows.filter((r) => r.layer === ly.split(" ")[0] && r.zone === z).length;
body.push(H2("Layers and zones"));
body.push(table(["Layer", "Years", "Core", "V", "Context"], layerRows.map(([a, b]) => [a, b, cnt(a, "Core"), cnt(a, "V"), cnt(a, "Context")]), [2200, 2000, 1600, 1600, 1960]));
body.push(P(""));
body.push(table(["Zone", "What it means", "Depth"], [
  ["Core", "The bottom of the V: the scenes happening now (lanes C1–C9).", "Completionist"],
  ["V", "Direct ancestors and close siblings of the Core (V1–V30, plus the thin roots lane R1).", "Deep"],
  ["Context", "Popular branches whose main line leads outside the V (X1–X14).", "Landmarks only"]], [1600, 5760, 2000], [ZFILL.Core, ZFILL.V, ZFILL.Context]));
body.push(P(""));
body.push(P("Album IDs such as [A0001] refer to rows on the Albums sheet of V_Album_Atlas.xlsx; filter the sheet by ID, lane or artist to find the full entry, descriptors, key tracks and sources."));

// 2. The V diagram
body.push(H1("2. The V diagram"));
body.push(P("The chart on the next page shows every lane as a box, placed in the layer where it is centred and coloured by zone. Arrows run from parent to child: from what fed a sound to what it fed. Dashed arrows touch a Context lane. The shape is the argument of this whole document: many roots at the top, narrowing through the '80s and '90s to a small set of scenes at the bottom."));
const diagramSection = { properties: { page: { size: { width: 12240, height: 15840, orientation: PageOrientation.LANDSCAPE }, margin: { top: 720, bottom: 720, left: 720, right: 720 } } },
  children: [img("v_lineage.png", 13.0), new Paragraph({ children: [new PageBreak()] }), H2("The eight trunk lines"), img("trunk_lines.png", 12.5),
    P("Each trunk line is one of the eight routes by which an older sound reaches the Core. The eight: (1) Neil Young & Crazy Horse guitar; (2) country played by punk and indie kids; (3) deadpan, funny-sad songwriting; (4) Southern storytelling rock; (5) slow, sad and noisy textures; (6) the DIY network; (7) Cosmic American Music; (8) folk songwriting.")] };

// 3. Core
const s3 = [H1("3. The bottom of the V: the Core lanes")];
const core3 = essay("core_intro"); if (core3) for (const p of core3.paragraphs) s3.push(P(p));
for (const id of ["C1", "C2", "C3", "C4", "C5", "C6", "C7", "C8", "C9"]) s3.push(...laneSection(id, 2));

// 4. Climbing the V
const s4 = [H1("4. Climbing the V")];
const climb = essay("climb_intro"); if (climb) for (const p of climb.paragraphs) s4.push(P(p));
const groups = [
  ["L1–L2 · The bridge and the siblings (1996–now)", ["V1", "V2", "V3", "V4", "V5", "V6", "V7"]],
  ["L3 · The Nineties (1987–1997)", ["V9", "V10", "V11", "V12", "V13"]],
  ["L4 · The Underground (1978–1986)", ["V14", "V15", "V16", "V17", "V18", "V19"]],
  ["L5 · The Classic era (1965–1977)", ["V20", "V21", "V22", "V23", "V24", "V25", "V26", "V27", "V28", "V29", "V30", "V8"]],
  ["L6 · Roots (before 1965)", ["R1"]],
];
for (const [title, ids] of groups) { s4.push(H2(title)); for (const id of ids) s4.push(...laneSection(id, 3)); }

// 5. Context
const s5 = [H1("5. Off the edges: the Context lanes")];
const ctx = essay("context_intro"); if (ctx) for (const p of ctx.paragraphs) s5.push(P(p));
for (let i = 1; i <= 14; i++) s5.push(...laneSection(`X${i}`, 3));

// 6. Scenes and labels
const s6 = [H1("6. Scenes and labels")];
s6.push(H2("Scenes"));
for (const s of scenes) {
  const n = rows.filter((r) => r.scene === s.scene).length;
  s6.push(new Paragraph({ spacing: { after: 100 }, children: [new TextRun({ text: `${s.scene}`, bold: true, font: FONT }), new TextRun({ text: ` · ${s.place} · ${s.years}${n ? ` · ${n} albums tagged` : ""}. `, font: FONT, color: "666666", size: 18 }), ...runs(`${s.note} Key artists: ${s.key_artists}.${s.key_labels ? " Labels: " + s.key_labels + "." : ""}`)] }));
}
s6.push(H2("Labels"));
for (const l of labels) {
  s6.push(new Paragraph({ spacing: { after: 100 }, children: [new TextRun({ text: l.label, bold: true, font: FONT }), new TextRun({ text: `${l.base ? " · " + l.base : ""}${l.years_active ? " · " + l.years_active : ""}. `, font: FONT, color: "666666", size: 18 }), ...runs(l.why)] }));
}

// 7. Listening paths
const s7 = [H1("7. Listening paths")];
const pint = essay("paths_intro"); if (pint) for (const p of pint.paragraphs) s7.push(P(p));
paths.forEach((p, k) => {
  s7.push(H2(`Path ${k + 1}: ${p.path}`));
  if (p.intro) s7.push(P(p.intro));
  p.steps.forEach((st) => s7.push(numbered(`path${k}`, `${albumRef(st.id)} — ${st.connection}`)));
});

// 8. Appendix
const s8 = [H1("8. Appendix: the borderline decisions")];
if (appendix) {
  for (const p of appendix.paragraphs || []) s8.push(P(p));
  for (const d of appendix.decisions || []) s8.push(bullet(`**${d.item}.** ${d.text}`));
}

const numbering = { config: [
  { reference: "bul", levels: [{ level: 0, format: LevelFormat.BULLET, text: "•", alignment: AlignmentType.LEFT, style: { paragraph: { indent: { left: 540, hanging: 270 } } } }] },
  ...paths.map((_, k) => ({ reference: `path${k}`, levels: [{ level: 0, format: LevelFormat.DECIMAL, text: "%1.", alignment: AlignmentType.LEFT, style: { paragraph: { indent: { left: 540, hanging: 360 } } } }] })),
] };
const portrait = { page: { size: { width: 12240, height: 15840 }, margin: { top: 1300, bottom: 1300, left: 1300, right: 1300 } } };
const footer = { default: new Footer({ children: [new Paragraph({ alignment: AlignmentType.CENTER, children: [new TextRun({ children: [PageNumber.CURRENT], font: FONT, size: 16, color: "888888" })] })] }) };
const doc = new Document({
  creator: "The V Album Atlas", title: "The V — V Map",
  styles: {
    default: { document: { run: { font: FONT, size: 21 } } },
    paragraphStyles: [
      { id: "Heading1", name: "Heading 1", basedOn: "Normal", next: "Normal", quickFormat: true, run: { size: 36, bold: true, font: FONT, color: "2B3A4A" }, paragraph: { spacing: { before: 240, after: 240 }, outlineLevel: 0 } },
      { id: "Heading2", name: "Heading 2", basedOn: "Normal", next: "Normal", quickFormat: true, run: { size: 28, bold: true, font: FONT, color: "7A4A1C" }, paragraph: { spacing: { before: 280, after: 120 }, outlineLevel: 1 } },
      { id: "Heading3", name: "Heading 3", basedOn: "Normal", next: "Normal", quickFormat: true, run: { size: 24, bold: true, font: FONT, color: "2B3A4A" }, paragraph: { spacing: { before: 240, after: 80 }, outlineLevel: 2 } },
    ],
  },
  numbering,
  sections: [
    { properties: portrait, footers: footer, children: body },
    { ...diagramSection, footers: footer },
    { properties: portrait, footers: footer, children: [...s3, ...s4, ...s5, ...s6, ...s7, ...s8] },
  ],
});
Packer.toBuffer(doc).then((buf) => {
  fs.mkdirSync(path.dirname(OUT), { recursive: true });
  fs.writeFileSync(OUT, buf);
  console.log(`wrote ${OUT}; cited ${citedIds.size} album IDs; missing: ${[...missingIds].join(", ") || "none"}`);
  fs.writeFileSync(`${W}/deliverables/docx_cited_ids.json`, JSON.stringify({ cited: [...citedIds], missing: [...missingIds] }));
});
