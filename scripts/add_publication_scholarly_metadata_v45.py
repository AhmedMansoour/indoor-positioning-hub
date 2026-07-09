from pathlib import Path
import re
import json
import html

ROOT = Path(".")
SITE_BASE = "https://ahmedmansoour.github.io/indoor-positioning-hub"
PUBLICATIONS_INDEX = ROOT / "publications.html"
PUBLICATION_DIR = ROOT / "publications"
CSS_FILE = ROOT / "assets" / "css" / "style.css"

if not PUBLICATIONS_INDEX.exists():
    raise SystemExit("publications.html not found. Run this script from the repository root.")
if not PUBLICATION_DIR.exists():
    raise SystemExit("publications/ folder not found. Run this script from the repository root.")
if not CSS_FILE.exists():
    raise SystemExit("assets/css/style.css not found. Run this script from the repository root.")

AREA_DEFS = {
    "area1": {
        "title": "Research Area 1: Enhancing Inertial Positioning Performance",
        "href": "../index.html#key-thematic-map",
        "short": "Infrastructure-free PDR, smartphone sensing, heading initialization, heading drift, pose changes, and inertial error control."
    },
    "area2": {
        "title": "Research Area 2: Scaling Wi-Fi Fingerprinting and Autonomous Radio-Map Generation",
        "href": "../index.html#research-area-2",
        "short": "Wi-Fi RSS fingerprinting, mobile crowdsensing, multisensor session logs, radio-map generation, and reliability-controlled map maintenance."
    },
    "area3": {
        "title": "Research Area 3: Seamless Indoor-Outdoor Positioning and Multi-Source Fusion",
        "href": "../index.html#research-area-3",
        "short": "Continuity across outdoor, transition, and indoor spaces using GNSS, PDR, Wi-Fi, BLE, barometer, maps, and source-reliability switching."
    },
    "area4": {
        "title": "Research Area 4: 3D Radio-Map Generation from Mobile Crowdsensing",
        "href": "../index.html#research-area-4",
        "short": "3D radio-map generation, floor-local skeletons, building-level assembly, vertical positioning, and floor recognition."
    },
}

AREA_MAP = {
    "drift-control-pdr-long-period-navigation-smartphone-poses": ["area1"],
    "enhancing-real-time-heading-estimation-deep-learning-smartphone-sensors": ["area1"],
    "hybrid-neural-network-pdr-multi-layer-heading-correction": ["area1"],
    "drift-resistant-heading-estimation-wifi-magnetic-stability": ["area1", "area2"],
    "gnss-positioning-aided-with-pdr-in-urban-areas": ["area1", "area3"],
    "tightly-coupled-bluetooth-enhanced-gnss-pdr-urban": ["area1", "area3"],
    "ac-hmm-azimuth-constrained-map-matching-urban-canyons": ["area1", "area3"],
    "reliability-governed-3d-radio-mapping-lifecycle-review": ["area2", "area4"],
    "towards-ubiquitous-ips-crowdsourced-data-accumulation": ["area2", "area4"],
    "leveraging-human-mobility-pervasive-smartphone-crowdsourcing": ["area2", "area4"],
    "everywhere-framework-ubiquitous-indoor-localization": ["area2"],
    "modular-prompting-ai-guided-user-engagement-crowd-powered-ips": ["area2"],
    "towards-scalable-ips-user-centric-crowd-powered-framework": ["area2"],
    "suns-seamless-ubiquitous-navigation-indoor-outdoor-awareness": ["area3"],
    "phd-thesis-indoor-localization-multi-sensor-crowdsourcing-collaboration": ["area4"],
}

EXTRA_THEMES = {
    "uncertainty-aware-risk-mapping-passive-wifi-bim-construction": {
        "title": "Related theme: Deployment and Spatial Safety",
        "href": "../research-themes.html",
        "short": "Passive Wi-Fi localization, BIM, uncertainty-aware risk mapping, and spatial safety decisions in construction environments."
    },
    "power-of-many-multi-user-collaborative-indoor-localization": {
        "title": "Related theme: Cooperative Positioning",
        "href": "../research-themes.html",
        "short": "Multi-user collaborative indoor localization and cooperative constraints that strengthen standalone smartphone-based positioning."
    },
}

COMMON_KEYWORDS = [
    "Ahmed Mansour",
    "indoor positioning",
    "indoor localization",
    "indoor navigation",
    "Wi-Fi fingerprinting",
    "PDR",
    "smartphone sensing",
    "mobile crowdsensing",
    "radio map",
    "GNSS/PDR integration",
    "spatial intelligence",
]

def clean_text(value: str) -> str:
    value = re.sub(r"<[^>]+>", " ", value or "")
    value = html.unescape(value)
    return " ".join(value.split())

def escape_attr(value: str) -> str:
    return html.escape(value or "", quote=True)

def first_match(pattern: str, text: str, flags=re.S|re.I) -> str:
    m = re.search(pattern, text, flags)
    return m.group(1).strip() if m else ""

def parse_publications_index() -> dict:
    text = PUBLICATIONS_INDEX.read_text(encoding="utf-8", errors="ignore")
    cards = re.findall(r'<article\s+class="pub-visual-card"\s+id="([^"]+)">(.*?)(?:</article>)', text, flags=re.S|re.I)
    meta = {}
    for slug, body in cards:
        title_href = re.search(r'<h2\s+class="pub-card-title">\s*<a\s+href="([^"]+)">(.*?)</a>\s*</h2>', body, flags=re.S|re.I)
        if not title_href:
            continue
        href = html.unescape(title_href.group(1).strip())
        title = clean_text(title_href.group(2))
        year_type = clean_text(first_match(r'<span\s+class="pub-year-type">(.*?)</span>', body))
        year_m = re.search(r'(\d{4})', year_type)
        year = year_m.group(1) if year_m else ""
        pub_type = year_type.split("·", 1)[1].strip() if "·" in year_type else ""
        theme = clean_text(first_match(r'<span\s+class="pub-theme-pill">(.*?)</span>', body))
        authors = clean_text(first_match(r'<p\s+class="pub-authors">(.*?)</p>', body))
        venue = clean_text(first_match(r'<span\s+class="pub-badge\s+journal">.*?<strong>(.*?)</strong>.*?</span>', body))
        doi_url = first_match(r'<span\s+class="pub-badge\s+doi">.*?<a\s+href="(https://doi\.org/[^"]+)"', body)
        doi = doi_url.replace("https://doi.org/", "") if doi_url else ""
        lens = clean_text(first_match(r'<p\s+class="pub-paper-lens">(.*?)</p>', body))
        keywords = [clean_text(x) for x in re.findall(r'<span\s+class="pub-keyword">(.*?)</span>', body, flags=re.S|re.I)]
        pdf_href = first_match(r'<a\s+class="pub-action"\s+href="(paper-pdfs/[^"]+\.pdf)"', body)
        preview = first_match(r'<img[^>]+src="(assets/previews/[^"]+)"', body)
        meta[slug] = {
            "slug": slug,
            "href": href,
            "title": title,
            "year": year,
            "type": pub_type,
            "theme": theme,
            "authors": authors,
            "venue": venue,
            "doi_url": doi_url,
            "doi": doi,
            "lens": lens,
            "keywords": keywords,
            "pdf_href": pdf_href,
            "preview": preview,
        }
    return meta

def split_authors(authors_text: str):
    if not authors_text:
        return ["Ahmed Mansour"]
    text = authors_text.replace(" and ", ", ")
    parts = [p.strip().strip(".") for p in text.split(",") if p.strip()]
    return parts or ["Ahmed Mansour"]

def description_for(m: dict) -> str:
    pieces = []
    if m.get("year"):
        pieces.append(m["year"])
    if m.get("venue"):
        pieces.append(m["venue"])
    desc = f"{m['title']}."
    if pieces:
        desc += " " + " · ".join(pieces) + "."
    if m.get("lens"):
        desc += " " + m["lens"]
    elif m.get("keywords"):
        desc += " Topics: " + ", ".join(m["keywords"][:6]) + "."
    else:
        desc += " Publication page with DOI, PDF, BibTeX, summary, and research-area links."
    desc = " ".join(desc.split())
    if len(desc) > 285:
        desc = desc[:282].rsplit(" ", 1)[0] + "..."
    return desc

def keywords_for(m: dict) -> str:
    kws = []
    for k in (m.get("keywords") or []) + [m.get("theme", ""), m.get("venue", "")] + COMMON_KEYWORDS:
        k = clean_text(k)
        if k and k.lower() not in [x.lower() for x in kws]:
            kws.append(k)
    return ", ".join(kws[:28])

def json_ld_for(m: dict) -> str:
    url = f"{SITE_BASE}/{m['href']}"
    pdf_url = f"{SITE_BASE}/{m['pdf_href']}" if m.get("pdf_href") else ""
    image_url = f"{SITE_BASE}/{m['preview']}" if m.get("preview") else ""
    authors = [{"@type": "Person", "name": a} for a in split_authors(m.get("authors", ""))]
    data = {
        "@context": "https://schema.org",
        "@type": "ScholarlyArticle",
        "headline": m["title"],
        "name": m["title"],
        "author": authors,
        "creator": authors,
        "datePublished": m.get("year", ""),
        "url": url,
        "mainEntityOfPage": url,
        "description": description_for(m),
        "keywords": m.get("keywords") or COMMON_KEYWORDS,
        "about": (m.get("keywords") or [])[:12] + ([m.get("theme", "")] if m.get("theme") else []),
        "isPartOf": {"@type": "Periodical", "name": m.get("venue", "")} if m.get("venue") else None,
        "identifier": m.get("doi_url") or url,
        "sameAs": [m["doi_url"]] if m.get("doi_url") else [],
        "encoding": {"@type": "MediaObject", "contentUrl": pdf_url, "encodingFormat": "application/pdf"} if pdf_url else None,
        "image": image_url or None,
        "inLanguage": "en",
        "publisher": {"@type": "Organization", "name": m.get("venue", "Indoor Positioning Hub")},
    }
    data = {k: v for k, v in data.items() if v not in (None, "", [], {})}
    return json.dumps(data, ensure_ascii=False, indent=2)

def build_head_block(m: dict) -> str:
    url = f"{SITE_BASE}/{m['href']}"
    image_url = f"{SITE_BASE}/{m['preview']}" if m.get("preview") else f"{SITE_BASE}/assets/home/indoor-navigation-office.webp"
    pdf_url = f"{SITE_BASE}/{m['pdf_href']}" if m.get("pdf_href") else ""
    desc = description_for(m)
    keywords = keywords_for(m)
    title = f"{m['title']} | Indoor Positioning Hub | Ahmed Mansour"

    citation_bits = [f'  <meta name="citation_title" content="{escape_attr(m["title"])}">']
    for a in split_authors(m.get("authors","")):
        citation_bits.append(f'  <meta name="citation_author" content="{escape_attr(a)}">')
    if m.get("year"):
        citation_bits.append(f'  <meta name="citation_publication_date" content="{escape_attr(m["year"])}">')
    if m.get("venue"):
        citation_bits.append(f'  <meta name="citation_journal_title" content="{escape_attr(m["venue"])}">')
    if m.get("doi"):
        citation_bits.append(f'  <meta name="citation_doi" content="{escape_attr(m["doi"])}">')
    if pdf_url:
        citation_bits.append(f'  <meta name="citation_pdf_url" content="{escape_attr(pdf_url)}">')
    citation_html = "\n".join(citation_bits)

    article_time = f'  <meta property="article:published_time" content="{escape_attr(m.get("year",""))}">' if m.get("year") else ""
    json_ld = json_ld_for(m)

    return f'''<!-- === Publication SEO and ScholarlyArticle metadata v45 START === -->
  <title>{escape_attr(title)}</title>
  <meta name="description" content="{escape_attr(desc)}">
  <meta name="keywords" content="{escape_attr(keywords)}">
  <meta name="author" content="Ahmed Mansour">
  <link rel="canonical" href="{escape_attr(url)}">
  <meta property="og:title" content="{escape_attr(title)}">
  <meta property="og:description" content="{escape_attr(desc)}">
  <meta property="og:type" content="article">
  <meta property="og:url" content="{escape_attr(url)}">
  <meta property="og:image" content="{escape_attr(image_url)}">
  <meta name="twitter:card" content="summary_large_image">
  <meta name="twitter:title" content="{escape_attr(title)}">
  <meta name="twitter:description" content="{escape_attr(desc)}">
  <meta name="twitter:image" content="{escape_attr(image_url)}">
{article_time}
{citation_html}
  <script type="application/ld+json">{json_ld}</script>
<!-- === Publication SEO and ScholarlyArticle metadata v45 END === -->'''

def clean_head(head: str) -> str:
    head = re.sub(r'\s*<!-- === Publication SEO and ScholarlyArticle metadata v45 START === -->.*?<!-- === Publication SEO and ScholarlyArticle metadata v45 END === -->', '', head, flags=re.S)
    patterns = [
        r'\s*<title>.*?</title>',
        r'\s*<meta\s+name="description"\s+content="[^"]*"\s*/?>',
        r'\s*<meta\s+name="keywords"\s+content="[^"]*"\s*/?>',
        r'\s*<meta\s+name="author"\s+content="[^"]*"\s*/?>',
        r'\s*<link\s+rel="canonical"\s+href="[^"]*"\s*/?>',
        r'\s*<meta\s+property="og:(?:title|description|type|url|image)"\s+content="[^"]*"\s*/?>',
        r'\s*<meta\s+name="twitter:(?:card|title|description|image)"\s+content="[^"]*"\s*/?>',
        r'\s*<meta\s+property="article:published_time"\s+content="[^"]*"\s*/?>',
        r'\s*<meta\s+name="citation_[^"]+"\s+content="[^"]*"\s*/?>',
    ]
    for p in patterns:
        head = re.sub(p, '', head, flags=re.S|re.I)
    return head

def research_area_block(slug: str) -> str:
    areas = [AREA_DEFS[a] for a in AREA_MAP.get(slug, []) if a in AREA_DEFS]
    extra = EXTRA_THEMES.get(slug)
    if not areas and extra:
        areas = [extra]
    if not areas:
        areas = [{
            "title": "Related theme: Indoor Positioning Research",
            "href": "../research-themes.html",
            "short": "This publication contributes to the broader indoor positioning, localization, navigation, and spatial-intelligence research program."
        }]

    card_html = []
    for a in areas:
        card_html.append(
            '<a class="paper-area-chip" href="{href}">'
            '<strong>{title}</strong>'
            '<span>{short}</span>'
            '</a>'.format(
                href=escape_attr(a["href"]),
                title=escape_attr(a["title"]),
                short=escape_attr(a["short"]),
            )
        )

    return '''
<!-- === Publication research-area index v45 START === -->
<section class="paper-research-area-index" id="research-area-connection">
  <h2>Research-area connection</h2>
  <p>This page is connected to the homepage research-area map so readers can move from the individual paper to the broader research program.</p>
  <div class="paper-area-chip-grid">
    {cards}
  </div>
</section>
<!-- === Publication research-area index v45 END === -->
'''.format(cards="\n    ".join(card_html))

def update_publication_page(path: Path, m: dict) -> bool:
    text = path.read_text(encoding="utf-8", errors="ignore")
    original = text

    head_m = re.search(r'<head>(.*?)</head>', text, flags=re.S|re.I)
    if head_m:
        head = clean_head(head_m.group(1))
        new_head = "<head>" + head.rstrip() + "\n" + build_head_block(m) + "\n</head>"
        text = text[:head_m.start()] + new_head + text[head_m.end():]
    else:
        text = text.replace("<body", "<head>\n" + build_head_block(m) + "\n</head>\n<body", 1)

    text = re.sub(r'\n?\s*<!-- === Publication research-area index v45 START === -->.*?<!-- === Publication research-area index v45 END === -->\s*\n?', '\n', text, flags=re.S|re.I)
    block = research_area_block(m["slug"])

    main_end = re.search(r'</main>', text, flags=re.I)
    if main_end:
        text = text[:main_end.start()] + block + "\n" + text[main_end.start():]
    else:
        footer = re.search(r'<footer', text, flags=re.I)
        if footer:
            text = text[:footer.start()] + block + "\n" + text[footer.start():]
        else:
            text += block

    if text != original:
        path.write_text(text, encoding="utf-8")
        return True
    return False

def update_css():
    css = CSS_FILE.read_text(encoding="utf-8", errors="ignore")
    css = re.sub(r'/\* === Publication research-area index v45 START === \*/.*?/\* === Publication research-area index v45 END === \*/', '', css, flags=re.S)
    block = '''
/* === Publication research-area index v45 START === */
.paper-research-area-index{
  margin:2rem 0 1.2rem;
  padding:1.15rem;
  border-radius:22px;
  background:linear-gradient(180deg,rgba(255,255,255,.94),rgba(247,251,255,.97));
  border:1px solid rgba(127,160,186,.22);
  box-shadow:0 12px 28px rgba(18,44,73,.06);
}
.paper-research-area-index h2{
  margin:0 0 .45rem;
  color:#073d63;
  font-size:1.2rem;
  letter-spacing:-.02em;
}
.paper-research-area-index p{
  margin:0 0 .85rem;
  color:#5e7286;
  line-height:1.6;
}
.paper-area-chip-grid{
  display:grid;
  grid-template-columns:repeat(auto-fit,minmax(240px,1fr));
  gap:.75rem;
}
.paper-area-chip{
  display:block;
  padding:.85rem .95rem;
  border-radius:17px;
  background:linear-gradient(180deg,rgba(239,247,251,.96),rgba(249,252,255,.98));
  border:1px solid rgba(79,159,187,.20);
  text-decoration:none;
}
.paper-area-chip strong{
  display:block;
  color:#084f72;
  font-size:.92rem;
  line-height:1.3;
  margin-bottom:.28rem;
}
.paper-area-chip span{
  display:block;
  color:#607488;
  font-size:.82rem;
  line-height:1.45;
}
.paper-area-chip:hover{
  transform:translateY(-1px);
  box-shadow:0 10px 22px rgba(20,45,74,.08);
}
@media(max-width:700px){
  .paper-area-chip-grid{grid-template-columns:1fr}
}
/* === Publication research-area index v45 END === */
'''
    CSS_FILE.write_text(css.rstrip() + "\n\n" + block.strip() + "\n", encoding="utf-8")

def main():
    metadata = parse_publications_index()
    if not metadata:
        raise SystemExit("No publication cards were parsed from publications.html.")

    changed = []
    missing = []
    for slug, m in metadata.items():
        page = PUBLICATION_DIR / f"{slug}.html"
        if not page.exists():
            missing.append(slug)
            continue
        if update_publication_page(page, m):
            changed.append(page.as_posix())

    update_css()

    print(f"Parsed {len(metadata)} publication cards from publications.html.")
    print(f"Updated {len(changed)} publication pages with SEO metadata, ScholarlyArticle JSON-LD, citation meta tags, and research-area links.")
    if missing:
        print("Missing publication pages:")
        for x in missing:
            print(" -", x)
    print("Updated assets/css/style.css with research-area index styling.")
    print("Done.")

if __name__ == "__main__":
    main()
