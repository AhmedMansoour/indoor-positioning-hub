from pathlib import Path
import re, html, json

ROOT = Path('.')
PAGE = ROOT / 'citation-resources.html'
PUBS = ROOT / 'publications.html'
CSS = ROOT / 'assets/css/style.css'
LLMS = ROOT / 'llms.txt'
SITE = 'https://ahmedmansoour.github.io/indoor-positioning-hub'

if not PAGE.exists():
    raise SystemExit('citation-resources.html not found. Run from repository root.')
if not CSS.exists():
    raise SystemExit('assets/css/style.css not found. Run from repository root.')

def clean(x):
    x = re.sub(r'<[^>]+>', ' ', x or '')
    return ' '.join(html.unescape(x).split())

def fm(pat, text):
    m = re.search(pat, text, flags=re.S | re.I)
    return m.group(1).strip() if m else ''

def parse_pubs():
    if not PUBS.exists():
        return []
    text = PUBS.read_text(encoding='utf-8', errors='ignore')
    cards = re.findall(r'<article\s+class="pub-visual-card"\s+id="([^"]+)">(.*?)(?:</article>)', text, flags=re.S | re.I)
    out = []
    for slug, body in cards:
        mh = re.search(r'<h2\s+class="pub-card-title">\s*<a\s+href="([^"]+)">(.*?)</a>\s*</h2>', body, flags=re.S | re.I)
        if not mh:
            continue
        year_text = clean(fm(r'<span\s+class="pub-year-type">(.*?)</span>', body))
        y = re.search(r'(\d{4})', year_text)
        doi = fm(r'<span\s+class="pub-badge\s+doi">.*?<a\s+href="(https://doi\.org/[^"]+)"', body)
        pdf = fm(r'<a\s+class="pub-action"\s+href="(paper-pdfs/[^"]+\.pdf)"', body)
        venue = clean(fm(r'<span\s+class="pub-badge\s+journal">.*?<strong>(.*?)</strong>.*?</span>', body))
        out.append({
            'slug': slug,
            'href': html.unescape(mh.group(1).strip()),
            'title': clean(mh.group(2)),
            'year': y.group(1) if y else '',
            'theme': clean(fm(r'<span\s+class="pub-theme-pill">(.*?)</span>', body)),
            'venue': venue,
            'doi': doi,
            'pdf': pdf or f'paper-pdfs/{slug}.pdf',
        })
    return out

pubs = parse_pubs()
old = PAGE.read_text(encoding='utf-8', errors='ignore')
old_header = fm(r'<body[^>]*>\s*(<header.*?</header>)', old)
old_footer = fm(r'(<footer.*?</footer>)', old)
header = old_header or '<header class="site-header"><a class="brand" href="index.html">Indoor Positioning Hub</a><nav class="site-nav" aria-label="Main navigation"><a href="index.html">Home</a><a href="publications.html">Publications</a><a href="research-themes.html">Research Themes</a><a href="resources.html">Datasets &amp; Code</a><a href="citation-resources.html" class="active">Citation Resources</a><a href="about.html">About</a></nav></header>'
footer = old_footer or '<footer class="site-footer"><div class="container"><p>&copy; <span id="year"></span> Ahmed Mansour. Indoor Positioning Research, Engineering, and Deployment Hub.</p></div></footer>'
header = re.sub(r'(<a href="citation-resources\.html")([^>]*)>', r'\1 class="active">', header, flags=re.I)
for page in ['index', 'publications', 'research-themes', 'resources', 'about']:
    header = re.sub(rf'(<a href="{page}\.html")\s+class="active"([^>]*)>', r'\1\2>', header, flags=re.I)

rows = []
for p in pubs:
    doi = f' · <a href="{html.escape(p["doi"])}">DOI</a>' if p['doi'] else ''
    pdf = f' · <a href="{html.escape(p["pdf"])}">PDF</a>' if p['pdf'] else ''
    theme = f'<em>{html.escape(p["theme"])}</em>' if p['theme'] else ''
    venue = f' <span>{html.escape(p["venue"])}</span>' if p['venue'] else ''
    rows.append(f'<li><a href="{html.escape(p["href"])}">{html.escape(p["title"])}</a> <strong>{html.escape(p["year"])}</strong>{venue}{theme}<small>{doi.lstrip(" · ")}{pdf}</small></li>')
paper_rows = '\n'.join(rows) if rows else '<li><a href="publications.html">Open publication portfolio</a></li>'

item_list = [{'@type':'ListItem','position':i,'name':p['title'],'url':f'{SITE}/{p["href"]}'} for i,p in enumerate(pubs[:30],1)]
jsonld = json.dumps({
    '@context':'https://schema.org',
    '@type':'CollectionPage',
    'name':'Citation Resources and AI Search Guide | Indoor Positioning Hub',
    'url':f'{SITE}/citation-resources.html',
    'description':'Citation toolkit for Ahmed Mansour indoor positioning publications, including author identifiers, DOI links, BibTeX, metadata, research-area guidance, and AI-search prompts.',
    'isPartOf':{'@type':'WebSite','name':'Indoor Positioning Hub','url':f'{SITE}/'},
    'about':['Indoor positioning citations','Wi-Fi fingerprinting','Pedestrian dead reckoning','Mobile crowdsensing','3D radio mapping','GNSS/PDR integration'],
    'mainEntity':{'@type':'ItemList','itemListElement':item_list}
}, ensure_ascii=False)

head = '''<head>
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width, initial-scale=1">
  <!-- === Citation resources SEO metadata v48 START === -->
  <title>Citation Resources and AI Search Guide | Indoor Positioning Hub | Ahmed Mansour</title>
  <meta name="description" content="Citation toolkit for Ahmed Mansour's indoor positioning publications, including author identifiers, DOI links, BibTeX, metadata files, research-area guidance, paper-use notes, and AI-search prompts.">
  <meta name="author" content="Ahmed Mansour">
  <meta name="keywords" content="Ahmed Mansour citations, indoor positioning citations, Wi-Fi fingerprinting paper, PDR paper, mobile crowdsensing IPS, radio map generation, GNSS/PDR integration, BibTeX, ORCID, Scopus Author ID, Google Scholar, AI search prompts">
  <link rel="canonical" href="https://ahmedmansoour.github.io/indoor-positioning-hub/citation-resources.html">
  <meta property="og:title" content="Citation Resources and AI Search Guide | Indoor Positioning Hub">
  <meta property="og:description" content="Author identifiers, paper-use guidance, DOI links, BibTeX, metadata, and AI-search prompts for Ahmed Mansour's indoor positioning publications.">
  <meta property="og:type" content="website">
  <meta property="og:url" content="https://ahmedmansoour.github.io/indoor-positioning-hub/citation-resources.html">
  <meta property="og:image" content="https://ahmedmansoour.github.io/indoor-positioning-hub/assets/home/research-area1-v38/inertial-multipose-route-rotated.webp">
  <meta name="twitter:card" content="summary_large_image">
  <script type="application/ld+json">''' + jsonld + '''</script>
  <!-- === Citation resources SEO metadata v48 END === -->
  <link rel="stylesheet" href="assets/css/style.css">
</head>'''

body = '''<body class="citation-v48-page">
{header}

<main class="citation-v48">
  <section class="cit48-hero">
    <p class="cit48-eyebrow">Citation Resources and AI Search Guide</p>
    <h1>Find, cite, and connect Ahmed Mansour's indoor positioning publications</h1>
    <p class="cit48-lead">This page helps readers identify which paper fits a specific indoor positioning question, copy citation resources, verify author identifiers, and test discovery through Google, Google Scholar, Semantic Scholar-style systems, OpenAlex, Elicit, SciSpace, Perplexity, and AI-assisted web search.</p>
    <div class="cit48-actions"><a href="publications.html">Publication portfolio</a><a href="papers/publications.bib">BibTeX</a><a href="data/publications.json">Metadata JSON</a><a href="research-themes.html">Research areas</a><a href="resources.html">Resources</a></div>
  </section>

  <section class="cit48-grid cit48-identifiers">
    <article><strong>ORCID</strong><a href="https://orcid.org/0000-0002-9840-7030">0000-0002-9840-7030</a></article>
    <article><strong>Scopus Author ID</strong><a href="https://www.scopus.com/authid/detail.uri?authorId=57948539100">57948539100</a></article>
    <article><strong>Web of Science ResearcherID</strong><a href="https://www.webofscience.com/wos/author/record/ABP-9962-2022">ABP-9962-2022</a></article>
    <article><strong>Google Scholar</strong><a href="https://scholar.google.com/citations?user=lFhcyh4AAAAJ&hl=en">Ahmed Mansour profile</a></article>
    <article><strong>ResearchGate</strong><a href="https://www.researchgate.net/profile/Ahmed-Mansour-55">Ahmed Mansour profile</a></article>
    <article><strong>LinkedIn</strong><a href="https://www.linkedin.com/in/ahmd-mansour/">Ahmed Mansour profile</a></article>
  </section>

  <section class="cit48-section"><div class="cit48-section-head"><p class="cit48-eyebrow">Citation identity</p><h2>Core research identity</h2><p>Ahmed Mansour's work focuses on indoor positioning, smartphone positioning, pedestrian positioning, Wi-Fi fingerprinting, mobile crowdsensing, autonomous radio-map generation, seamless indoor-outdoor positioning, PDR, GNSS/PDR integration, cooperative positioning, and deployment-ready indoor spatial intelligence.</p></div></section>

  <section class="cit48-section">
    <div class="cit48-section-head"><p class="cit48-eyebrow">When to cite which work</p><h2>Research-area citation guide</h2><p>Use the four research areas to choose the most relevant paper for a specific argument, literature review, method comparison, or background section.</p></div>
    <div class="cit48-area-guide">
      <article><span>Area 1</span><h3>Inertial positioning and PDR</h3><p>Cite these papers for smartphone PDR, heading drift control, carrying-mode robustness, inertial sensing, and GNSS/PDR-aided pedestrian navigation.</p><a href="research-themes.html#area-inertial">Open area</a></article>
      <article><span>Area 2</span><h3>Wi-Fi fingerprinting and radio-map scaling</h3><p>Cite these papers for Wi-Fi fingerprinting, mobile crowdsensing, radio-map generation, autonomous map updating, and reliability-governed IPS scaling.</p><a href="research-themes.html#area-radio-map">Open area</a></article>
      <article><span>Area 3</span><h3>Seamless indoor-outdoor fusion</h3><p>Cite these papers for GNSS, Wi-Fi, MEMS, BLE, PDR, indoor-outdoor awareness, source switching, and transition-aware navigation.</p><a href="research-themes.html#area-seamless">Open area</a></article>
      <article><span>Area 4</span><h3>3D indoor spatial context</h3><p>Cite these papers for 3D radio maps, multi-floor positioning, floor recognition, vertical positioning, building-level assembly, and spatial context.</p><a href="research-themes.html#area-3d">Open area</a></article>
    </div>
  </section>

  <section class="cit48-section">
    <div class="cit48-section-head"><p class="cit48-eyebrow">Paper finder</p><h2>Publication pages, DOI links, and PDFs</h2><p>The publication page is the best citation entry point because it links title, year, venue, DOI, PDF, summary, and research-area connection.</p></div>
    <ul class="cit48-paper-list">{paper_rows}</ul>
  </section>

  <section class="cit48-section">
    <div class="cit48-section-head"><p class="cit48-eyebrow">AI-search prompts</p><h2>Discovery test queries</h2><p>Use these prompts to test whether the hub and individual publication pages are discoverable by conventional search engines and AI-assisted search tools.</p></div>
    <div class="cit48-prompts">
      <code>Find Ahmed Mansour papers on scalable crowdsourcing-based indoor positioning systems.</code>
      <code>Find review papers on autonomous 3D radio-map generation for Wi-Fi fingerprinting.</code>
      <code>Find Ahmed Mansour work on smartphone heading drift correction for indoor positioning.</code>
      <code>Find papers on seamless indoor-outdoor positioning using GNSS, Wi-Fi, and MEMS sensors.</code>
      <code>Find papers on GNSS/PDR integration for pedestrian navigation in dense urban environments.</code>
      <code>Find work on mobile crowdsensing for self-deployable indoor positioning systems.</code>
      <code>Find papers connecting passive Wi-Fi localization, BIM, and construction safety.</code>
      <code>Find papers on multi-user collaborative indoor localization and cooperative positioning.</code>
    </div>
  </section>

  <section class="cit48-section">
    <div class="cit48-section-head"><p class="cit48-eyebrow">Machine-readable citation resources</p><h2>Metadata files for citation and indexing</h2><p>These files support citation managers, search engines, AI systems, and reproducibility workflows.</p></div>
    <div class="cit48-machine-grid">
      <a href="papers/publications.bib"><strong>publications.bib</strong><span>BibTeX entries for manuscript and citation-manager workflows.</span></a>
      <a href="data/publications.json"><strong>publications.json</strong><span>Structured publication metadata used by the hub.</span></a>
      <a href="llms.txt"><strong>llms.txt</strong><span>AI-readable guide to the site, research areas, and publication pages.</span></a>
      <a href="sitemap.xml"><strong>sitemap.xml</strong><span>Crawlable URL map for search engines and indexing tools.</span></a>
      <a href="resources.html"><strong>Resources page</strong><span>PDFs, metadata, reproducibility notes, code and dataset status.</span></a>
      <a href="about.html"><strong>About page</strong><span>Author identity, academic profile, affiliations, and profile links.</span></a>
    </div>
  </section>

  <section class="cit48-section"><div class="cit48-section-head"><p class="cit48-eyebrow">Citation note</p><h2>Use DOI and official publication metadata when available</h2><p>For formal manuscripts, cite the published version of record whenever a DOI is available. Use this hub as a discovery, reading, PDF-access, and citation-guidance layer. For papers with publisher restrictions, use DOI links rather than redistributing restricted PDFs.</p></div></section>
</main>

{footer}
<script src="assets/js/site.js"></script>
</body>
</html>
'''.format(header=header, footer=footer, paper_rows=paper_rows)

PAGE.write_text('<!doctype html>\n<html lang="en">\n' + head + '\n' + body, encoding='utf-8')

css = CSS.read_text(encoding='utf-8', errors='ignore')
css = re.sub(r'/\* === Citation resources page v48 START === \*/.*?/\* === Citation resources page v48 END === \*/', '', css, flags=re.S)
css_block = '''
/* === Citation resources page v48 START === */
.citation-v48{width:min(1180px,calc(100% - 56px));margin:0 auto 48px}.cit48-hero{margin:36px 0 22px;padding:32px;border-radius:32px;background:radial-gradient(circle at 82% 10%,rgba(79,196,211,.16),transparent 35%),linear-gradient(180deg,rgba(255,255,255,.98),rgba(246,251,255,.98));border:1px solid rgba(130,165,194,.25);box-shadow:0 22px 50px rgba(20,45,74,.08)}.cit48-eyebrow{margin:0 0 .55rem;color:#0b6380;text-transform:uppercase;letter-spacing:.12em;font-size:.75rem;font-weight:800}.cit48-hero h1{margin:0 0 .85rem;color:#073d63;font-size:clamp(2rem,4vw,3.55rem);line-height:1.02;letter-spacing:-.055em}.cit48-lead{max-width:980px;margin:0;color:#405b71;font-size:1.04rem;line-height:1.68}.cit48-actions{display:flex;flex-wrap:wrap;gap:.6rem;margin-top:1.35rem}.cit48-actions a,.cit48-grid a,.cit48-area-guide a,.cit48-machine-grid a{color:#084f72;text-decoration:none}.cit48-actions a{display:inline-flex;padding:.62rem .85rem;border-radius:999px;background:rgba(83,197,213,.10);border:1px solid rgba(79,159,187,.24);font-weight:700;font-size:.85rem}.cit48-grid{display:grid;grid-template-columns:repeat(3,1fr);gap:14px;margin:0 0 24px}.cit48-grid article,.cit48-machine-grid a{display:block;padding:17px;border-radius:22px;background:linear-gradient(180deg,rgba(255,255,255,.96),rgba(248,252,255,.98));border:1px solid rgba(127,160,186,.20);box-shadow:0 10px 24px rgba(20,45,74,.045)}.cit48-grid strong,.cit48-machine-grid strong{display:block;color:#073d63;margin-bottom:.35rem}.cit48-grid a,.cit48-machine-grid span{display:block;color:#607488;font-size:.88rem;line-height:1.45}.cit48-section{margin:24px 0;padding:22px;border-radius:30px;background:linear-gradient(180deg,rgba(255,255,255,.98),rgba(248,252,255,.98));border:1px solid rgba(130,165,194,.23);box-shadow:0 16px 38px rgba(20,45,74,.065)}.cit48-section-head h2{margin:0 0 .65rem;color:#073d63;font-size:clamp(1.45rem,2.5vw,2.2rem);line-height:1.1;letter-spacing:-.04em}.cit48-section-head p:not(.cit48-eyebrow){margin:0;max-width:980px;color:#405b71;font-size:.98rem;line-height:1.65}.cit48-area-guide{display:grid;grid-template-columns:repeat(4,1fr);gap:14px;margin-top:18px}.cit48-area-guide article{padding:17px;border-radius:22px;background:linear-gradient(180deg,rgba(239,247,251,.96),rgba(249,252,255,.98));border:1px solid rgba(79,159,187,.17)}.cit48-area-guide span{display:inline-flex;margin-bottom:.55rem;padding:.32rem .55rem;border-radius:999px;background:rgba(83,197,213,.12);color:#084f72;font-size:.72rem;font-weight:800}.cit48-area-guide h3{margin:0 0 .45rem;color:#073d63;font-size:1rem}.cit48-area-guide p{margin:0 0 .7rem;color:#607488;font-size:.86rem;line-height:1.5}.cit48-area-guide a{font-weight:700;font-size:.84rem}.cit48-paper-list{margin:18px 0 0;padding-left:1.08rem;columns:2;column-gap:2.2rem}.cit48-paper-list li{break-inside:avoid;margin:0 0 .72rem;color:#607488;font-size:.86rem;line-height:1.42}.cit48-paper-list a{color:#035083;text-decoration:none}.cit48-paper-list a:hover{text-decoration:underline}.cit48-paper-list strong{color:#7f90a2;font-weight:700}.cit48-paper-list span{color:#7f90a2}.cit48-paper-list em{display:block;color:#6b7d91;font-style:normal;font-size:.78rem;margin-top:.12rem}.cit48-paper-list small{display:block;margin-top:.1rem;color:#7f90a2}.cit48-prompts{display:grid;grid-template-columns:repeat(2,1fr);gap:12px;margin-top:18px}.cit48-prompts code{display:block;white-space:normal;padding:14px 15px;border-radius:18px;background:#f4f8fb;border:1px solid rgba(127,160,186,.20);color:#294a61;font-size:.86rem;line-height:1.45}.cit48-machine-grid{display:grid;grid-template-columns:repeat(3,1fr);gap:14px;margin-top:18px}@media(max-width:980px){.citation-v48{width:min(100%,calc(100% - 22px))}.cit48-grid,.cit48-area-guide,.cit48-machine-grid,.cit48-prompts{grid-template-columns:1fr 1fr}.cit48-paper-list{columns:1}}@media(max-width:640px){.citation-v48{width:min(100%,calc(100% - 18px))}.cit48-hero,.cit48-section{padding:17px;border-radius:24px}.cit48-grid,.cit48-area-guide,.cit48-machine-grid,.cit48-prompts{grid-template-columns:1fr}}
/* === Citation resources page v48 END === */
'''
CSS.write_text(css.rstrip() + '\n\n' + css_block.strip() + '\n', encoding='utf-8')

if LLMS.exists():
    llms = LLMS.read_text(encoding='utf-8', errors='ignore')
    add = '\n## Citation resources and AI-search guide\n\n- Citation Resources page: https://ahmedmansoour.github.io/indoor-positioning-hub/citation-resources.html\n- Purpose: a citation and discovery guide with author identifiers, research-area citation guidance, publication page links, DOI and PDF links, BibTeX, JSON metadata, AI-search prompts, and machine-readable resource links.\n'
    if '## Citation resources and AI-search guide' not in llms:
        anchor = '## Resources and reproducibility page'
        llms = llms.replace(anchor, add + '\n' + anchor) if anchor in llms else llms.rstrip() + '\n' + add + '\n'
        LLMS.write_text(llms, encoding='utf-8')

print(f'Done: upgraded citation-resources.html with {len(pubs)} publication citation records.')
