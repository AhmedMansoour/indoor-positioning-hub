from pathlib import Path
import re, html

ROOT = Path(".")
PAGE = ROOT / "resources.html"
PUBS = ROOT / "publications.html"
CSS = ROOT / "assets/css/style.css"
LLMS = ROOT / "llms.txt"

if not PAGE.exists():
    raise SystemExit("resources.html not found. Run from repository root.")
if not CSS.exists():
    raise SystemExit("assets/css/style.css not found. Run from repository root.")

def clean(x):
    x = re.sub(r"<[^>]+>", " ", x or "")
    return " ".join(html.unescape(x).split())

def fm(pat, text):
    m = re.search(pat, text, flags=re.S | re.I)
    return m.group(1).strip() if m else ""

def parse_pubs():
    if not PUBS.exists():
        return []
    text = PUBS.read_text(encoding="utf-8", errors="ignore")
    cards = re.findall(r'<article\s+class="pub-visual-card"\s+id="([^"]+)">(.*?)(?:</article>)', text, flags=re.S | re.I)
    out = []
    for slug, body in cards:
        mh = re.search(r'<h2\s+class="pub-card-title">\s*<a\s+href="([^"]+)">(.*?)</a>\s*</h2>', body, flags=re.S | re.I)
        if not mh:
            continue
        year_text = clean(fm(r'<span\s+class="pub-year-type">(.*?)</span>', body))
        y = re.search(r"(\d{4})", year_text)
        doi = fm(r'<span\s+class="pub-badge\s+doi">.*?<a\s+href="(https://doi\.org/[^"]+)"', body)
        pdf = fm(r'<a\s+class="pub-action"\s+href="(paper-pdfs/[^"]+\.pdf)"', body)
        out.append({
            "slug": slug,
            "href": html.unescape(mh.group(1).strip()),
            "title": clean(mh.group(2)),
            "year": y.group(1) if y else "",
            "theme": clean(fm(r'<span\s+class="pub-theme-pill">(.*?)</span>', body)),
            "doi": doi,
            "pdf": pdf or f"paper-pdfs/{slug}.pdf",
        })
    return out

pubs = parse_pubs()
old = PAGE.read_text(encoding="utf-8", errors="ignore")
old_header = fm(r"<body[^>]*>\s*(<header.*?</header>)", old)
old_footer = fm(r"(<footer.*?</footer>)", old)

header = old_header or '<header class="site-header"><a class="brand" href="index.html">Indoor Positioning Hub</a><nav class="site-nav" aria-label="Main navigation"><a href="index.html">Home</a><a href="publications.html">Publications</a><a href="research-themes.html">Research Themes</a><a href="resources.html" class="active">Datasets &amp; Code</a><a href="citation-resources.html">Citation Resources</a><a href="about.html">About</a></nav></header>'
footer = old_footer or '<footer class="site-footer"><div class="container"><p>&copy; <span id="year"></span> Ahmed Mansour. Indoor Positioning Research, Engineering, and Deployment Hub.</p></div></footer>'

header = re.sub(r'(<a href="resources\.html")([^>]*)>', r'\1 class="active">', header, flags=re.I)
for page in ["index", "publications", "research-themes", "citation-resources", "about"]:
    header = re.sub(rf'(<a href="{page}\.html")\s+class="active"([^>]*)>', r'\1\2>', header, flags=re.I)

pdf_rows = []
for p in pubs:
    pdf_rows.append(
        '<li><a href="{pdf}">{title}</a> <span>{year}</span><em>{theme}</em>'
        '<small><a href="{href}">publication page</a>{doi}</small></li>'.format(
            pdf=html.escape(p["pdf"]), title=html.escape(p["title"]), year=html.escape(p["year"]),
            theme=html.escape(p["theme"]), href=html.escape(p["href"]),
            doi=(' · <a href="' + html.escape(p["doi"]) + '">DOI</a>') if p["doi"] else ""
        )
    )
if not pdf_rows:
    pdf_rows = ['<li><a href="publications.html">Open the publication portfolio</a><span>PDFs, DOI links, BibTeX, and paper records.</span></li>']

head = '''<head>
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width, initial-scale=1">
  <!-- === Resources page SEO metadata v47 START === -->
  <title>Resources, PDFs, Metadata, and Reproducibility | Indoor Positioning Hub | Ahmed Mansour</title>
  <meta name="description" content="Resources page for Ahmed Mansour's Indoor Positioning Hub, including publication PDFs, BibTeX, JSON metadata, reproducibility notes, code and dataset status, responsible sharing policy, sitemap, and llms.txt.">
  <meta name="author" content="Ahmed Mansour">
  <meta name="keywords" content="indoor positioning resources, indoor localization datasets, Wi-Fi fingerprinting code, radio map generation, PDR reproducibility, mobile crowdsensing data, publication PDFs, BibTeX, JSON metadata, llms.txt, Ahmed Mansour">
  <link rel="canonical" href="https://ahmedmansoour.github.io/indoor-positioning-hub/resources.html">
  <meta property="og:title" content="Resources, PDFs, Metadata, and Reproducibility | Indoor Positioning Hub">
  <meta property="og:description" content="Publication PDFs, metadata, BibTeX, reproducibility notes, code and dataset status, and machine-readable resources for indoor positioning research.">
  <meta property="og:type" content="website">
  <meta property="og:url" content="https://ahmedmansoour.github.io/indoor-positioning-hub/resources.html">
  <meta property="og:image" content="https://ahmedmansoour.github.io/indoor-positioning-hub/assets/home/research-area2-v40/multisensor-session-log-stream.webp">
  <meta name="twitter:card" content="summary_large_image">
  <script type="application/ld+json">{"@context":"https://schema.org","@type":"CollectionPage","name":"Resources, PDFs, Metadata, and Reproducibility | Indoor Positioning Hub","url":"https://ahmedmansoour.github.io/indoor-positioning-hub/resources.html","description":"A resource index for Ahmed Mansour's indoor positioning publications, PDFs, metadata, BibTeX, reproducibility notes, code and dataset status, and machine-readable files.","isPartOf":{"@type":"WebSite","name":"Indoor Positioning Hub","url":"https://ahmedmansoour.github.io/indoor-positioning-hub/"},"about":["Publication PDFs","BibTeX","JSON metadata","Indoor positioning reproducibility","Wi-Fi fingerprinting","Pedestrian dead reckoning","Mobile crowdsensing","3D radio-map generation"]}</script>
  <!-- === Resources page SEO metadata v47 END === -->
  <link rel="stylesheet" href="assets/css/style.css">
</head>'''

body = '''<body class="resources-v47-page">
{header}

<main class="resources-v47">
  <section class="res47-hero">
    <p class="res47-eyebrow">Resources, PDFs, Metadata, and Reproducibility</p>
    <h1>Research resources for indoor positioning, radio mapping, and spatial intelligence</h1>
    <p class="res47-lead">This page collects reusable materials connected to the Indoor Positioning Hub: publication PDFs, citation files, machine-readable metadata, reproducibility notes, code and dataset status, and responsible sharing rules. It gives readers, collaborators, reviewers, students, and AI-assisted search systems a clear entry point to the technical resources behind the publication portfolio.</p>
    <div class="res47-actions"><a href="publications.html">Publication portfolio</a><a href="papers/publications.bib">BibTeX</a><a href="data/publications.json">Metadata JSON</a><a href="llms.txt">llms.txt</a></div>
  </section>

  <section class="res47-overview">
    <a href="publications.html"><strong>Publication pages</strong><span>Paper summaries, DOI links, PDFs, BibTeX, and research-area connections.</span></a>
    <a href="papers/publications.bib"><strong>BibTeX</strong><span>Citation-ready records for the publication portfolio.</span></a>
    <a href="data/publications.json"><strong>JSON metadata</strong><span>Machine-readable publication data for indexing and reuse.</span></a>
    <a href="sitemap.xml"><strong>Sitemap</strong><span>Crawlable URL map for pages, PDFs, and metadata resources.</span></a>
    <a href="llms.txt"><strong>llms.txt</strong><span>AI-readable guide to the hub, research areas, and publication pages.</span></a>
    <a href="assets/cv/ahmed-mansour-public-cv.pdf"><strong>Public CV</strong><span>Academic profile, identifiers, and publication record.</span></a>
  </section>

  <section class="res47-section">
    <div class="res47-section-head"><p class="res47-eyebrow">Downloadable resources</p><h2>Publication PDFs and paper-level records</h2><p>Each publication page is the preferred entry point because it connects the PDF, DOI, BibTeX, summary, visual preview, and research-area context. Direct PDF links are listed here for fast access when redistribution is allowed.</p></div>
    <ul class="res47-pdf-list">{pdf_list}</ul>
  </section>

  <section class="res47-section">
    <div class="res47-section-head"><p class="res47-eyebrow">Reproducibility by research area</p><h2>How the resources map to the research program</h2><p>The hub is organized around four research areas. These notes explain which types of implementation details and reproducibility material are most relevant to each area.</p></div>
    <div class="res47-area-grid">
      <article><span>Area 1</span><h3>Inertial positioning and PDR</h3><p>Smartphone inertial processing, heading estimation, carrying-mode descriptions, PDR correction logic, and implementation notes.</p><a href="research-themes.html#area-inertial">Open area</a></article>
      <article><span>Area 2</span><h3>Wi-Fi fingerprinting and radio maps</h3><p>Fingerprinting metadata, crowdsensing session descriptions, radio-map generation diagrams, and reliability-governed updating concepts.</p><a href="research-themes.html#area-radio-map">Open area</a></article>
      <article><span>Area 3</span><h3>Seamless indoor-outdoor fusion</h3><p>GNSS/PDR integration, transition figures, BLE-enhanced positioning records, and source-switching explanations.</p><a href="research-themes.html#area-seamless">Open area</a></article>
      <article><span>Area 4</span><h3>3D radio-map generation</h3><p>Floor-local skeletons, building-level assembly, vertical positioning, floor recognition, and 3D indoor spatial-reference material.</p><a href="research-themes.html#area-3d">Open area</a></article>
    </div>
  </section>

  <section class="res47-section">
    <div class="res47-section-head"><p class="res47-eyebrow">Code and dataset status</p><h2>Availability and sharing notes</h2><p>The status is stated directly so readers know what is available now, what is planned, and what may require permission or request-based access.</p></div>
    <div class="res47-status-grid">
      <article><strong>Available now</strong><ul><li>Publication pages with DOI links, PDFs when allowed, and citation material.</li><li>Machine-readable publication metadata in JSON.</li><li>BibTeX file for citation workflows.</li><li>Figures and visual research-area explanations embedded in the website.</li></ul></article>
      <article><strong>Planned resources</strong><ul><li>Wi-Fi fingerprinting reliability benchmarks.</li><li>Autonomous 3D radio-map generation scripts.</li><li>PDR and heading-estimation implementation notes.</li><li>IOD and seamless-positioning supplementary tables and search strings.</li></ul></article>
      <article><strong>Request-based or restricted</strong><ul><li>Indoor trajectories that contain privacy-sensitive location traces.</li><li>Raw mobile crowdsensing sessions with user or device identifiers.</li><li>Publisher-restricted PDFs, where DOI links are used instead of direct redistribution.</li><li>Project-specific datasets controlled by collaborators, institutions, or venue policies.</li></ul></article>
    </div>
  </section>

  <section class="res47-section"><div class="res47-section-head"><p class="res47-eyebrow">Responsible sharing policy</p><h2>Open where possible, careful where necessary</h2><p>Indoor positioning resources can include sensitive location traces, Wi-Fi scans, device identifiers, building layouts, and movement patterns. The hub separates public academic material from restricted or request-based data. Open-access papers, accepted manuscripts, BibTeX, metadata, and explanatory figures are shared directly when permitted. Restricted publisher files, privacy-sensitive datasets, and collaboration-controlled materials are linked or described without exposing data that should not be redistributed.</p></div></section>

  <section class="res47-section">
    <div class="res47-section-head"><p class="res47-eyebrow">Machine-readable resources</p><h2>Files for search engines, AI systems, and citation workflows</h2><p>These files help machines discover the site structure, publication records, and research-area relationships.</p></div>
    <div class="res47-machine-grid"><a href="llms.txt"><strong>llms.txt</strong><span>AI-readable guide to the hub and research areas.</span></a><a href="sitemap.xml"><strong>sitemap.xml</strong><span>Crawlable index of website URLs.</span></a><a href="robots.txt"><strong>robots.txt</strong><span>Search-engine access and sitemap pointer.</span></a><a href="data/publications.json"><strong>publications.json</strong><span>Structured publication metadata.</span></a><a href="papers/publications.bib"><strong>publications.bib</strong><span>BibTeX entries for citation workflows.</span></a><a href="citation-resources.html"><strong>Citation Resources</strong><span>Author identifiers and paper-use guidance.</span></a></div>
  </section>
</main>

{footer}
<script src="assets/js/site.js"></script>
</body>
</html>
'''.format(header=header, footer=footer, pdf_list="\n".join(pdf_rows))

PAGE.write_text("<!doctype html>\n<html lang=\"en\">\n" + head + "\n" + body, encoding="utf-8")

css = CSS.read_text(encoding="utf-8", errors="ignore")
css = re.sub(r"/\* === Resources page v47 START === \*/.*?/\* === Resources page v47 END === \*/", "", css, flags=re.S)
css_block = '''
/* === Resources page v47 START === */
.resources-v47{width:min(1180px,calc(100% - 56px));margin:0 auto 48px}
.res47-hero{margin:36px 0 22px;padding:32px;border-radius:32px;background:radial-gradient(circle at 82% 10%,rgba(79,196,211,.16),transparent 35%),linear-gradient(180deg,rgba(255,255,255,.98),rgba(246,251,255,.98));border:1px solid rgba(130,165,194,.25);box-shadow:0 22px 50px rgba(20,45,74,.08)}
.res47-eyebrow{margin:0 0 .55rem;color:#0b6380;text-transform:uppercase;letter-spacing:.12em;font-size:.75rem;font-weight:800}
.res47-hero h1{margin:0 0 .85rem;color:#073d63;font-size:clamp(2rem,4vw,3.55rem);line-height:1.02;letter-spacing:-.055em}
.res47-lead{max-width:980px;margin:0;color:#405b71;font-size:1.04rem;line-height:1.68}
.res47-actions{display:flex;flex-wrap:wrap;gap:.6rem;margin-top:1.35rem}
.res47-actions a,.res47-overview a,.res47-machine-grid a,.res47-area-grid a{color:#084f72;text-decoration:none}
.res47-actions a{display:inline-flex;padding:.62rem .85rem;border-radius:999px;background:rgba(83,197,213,.10);border:1px solid rgba(79,159,187,.24);font-weight:700;font-size:.85rem}
.res47-overview{display:grid;grid-template-columns:repeat(3,1fr);gap:14px;margin:0 0 24px}
.res47-overview a,.res47-machine-grid a{display:block;padding:17px;border-radius:22px;background:linear-gradient(180deg,rgba(255,255,255,.96),rgba(248,252,255,.98));border:1px solid rgba(127,160,186,.20);box-shadow:0 10px 24px rgba(20,45,74,.045)}
.res47-overview strong,.res47-machine-grid strong{display:block;color:#073d63;margin-bottom:.35rem}
.res47-overview span,.res47-machine-grid span{display:block;color:#607488;font-size:.88rem;line-height:1.45}
.res47-section{margin:24px 0;padding:22px;border-radius:30px;background:linear-gradient(180deg,rgba(255,255,255,.98),rgba(248,252,255,.98));border:1px solid rgba(130,165,194,.23);box-shadow:0 16px 38px rgba(20,45,74,.065)}
.res47-section-head h2{margin:0 0 .65rem;color:#073d63;font-size:clamp(1.45rem,2.5vw,2.2rem);line-height:1.1;letter-spacing:-.04em}
.res47-section-head p:not(.res47-eyebrow){margin:0;max-width:980px;color:#405b71;font-size:.98rem;line-height:1.65}
.res47-pdf-list{margin:18px 0 0;padding-left:1.08rem;columns:2;column-gap:2.2rem}
.res47-pdf-list li{break-inside:avoid;margin:0 0 .7rem;color:#607488;font-size:.86rem;line-height:1.42}
.res47-pdf-list a{color:#035083;text-decoration:none}.res47-pdf-list a:hover{text-decoration:underline}
.res47-pdf-list span{color:#7f90a2}.res47-pdf-list em{display:block;color:#6b7d91;font-style:normal;font-size:.78rem;margin-top:.12rem}.res47-pdf-list small{display:block;margin-top:.1rem;color:#7f90a2}
.res47-area-grid,.res47-status-grid,.res47-machine-grid{display:grid;grid-template-columns:repeat(3,1fr);gap:14px;margin-top:18px}
.res47-area-grid{grid-template-columns:repeat(4,1fr)}
.res47-area-grid article,.res47-status-grid article{padding:17px;border-radius:22px;background:linear-gradient(180deg,rgba(239,247,251,.96),rgba(249,252,255,.98));border:1px solid rgba(79,159,187,.17)}
.res47-status-grid article{background:linear-gradient(180deg,rgba(245,242,255,.92),rgba(251,249,255,.98));border-color:rgba(148,132,200,.18)}
.res47-area-grid article>span{display:inline-flex;margin-bottom:.55rem;padding:.32rem .55rem;border-radius:999px;background:rgba(83,197,213,.12);color:#084f72;font-size:.72rem;font-weight:800}
.res47-area-grid h3{margin:0 0 .45rem;color:#073d63;font-size:1rem}
.res47-area-grid p{margin:0 0 .7rem;color:#607488;font-size:.86rem;line-height:1.5}
.res47-area-grid a{font-weight:700;font-size:.84rem}.res47-status-grid strong{display:block;color:#073d63;margin-bottom:.55rem}.res47-status-grid ul{margin:0;padding-left:1.08rem}.res47-status-grid li{margin:0 0 .48rem;color:#405b71;font-size:.88rem;line-height:1.45}
@media(max-width:980px){.resources-v47{width:min(100%,calc(100% - 22px))}.res47-overview,.res47-area-grid,.res47-status-grid,.res47-machine-grid{grid-template-columns:1fr 1fr}.res47-pdf-list{columns:1}}
@media(max-width:640px){.resources-v47{width:min(100%,calc(100% - 18px))}.res47-hero,.res47-section{padding:17px;border-radius:24px}.res47-overview,.res47-area-grid,.res47-status-grid,.res47-machine-grid{grid-template-columns:1fr}}
/* === Resources page v47 END === */
'''
CSS.write_text(css.rstrip() + "\n\n" + css_block.strip() + "\n", encoding="utf-8")

if LLMS.exists():
    llms = LLMS.read_text(encoding="utf-8", errors="ignore")
    add = "\n## Resources and reproducibility page\n\n- Resources page: https://ahmedmansoour.github.io/indoor-positioning-hub/resources.html\n- Purpose: a dedicated index for publication PDFs, BibTeX, JSON metadata, reproducibility notes, code and dataset status, responsible sharing policy, sitemap, robots.txt, and llms.txt.\n"
    if "## Resources and reproducibility page" not in llms:
        anchor = "## Citation and machine-readable resources"
        llms = llms.replace(anchor, add + "\n" + anchor) if anchor in llms else llms.rstrip() + "\n" + add + "\n"
        LLMS.write_text(llms, encoding="utf-8")

print(f"Done: upgraded resources.html with {len(pubs)} publication PDF records.")
