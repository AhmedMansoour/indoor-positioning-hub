from pathlib import Path
import re, shutil, json
ROOT=Path(".")
ABOUT=ROOT/"about.html"
CSS=ROOT/"assets"/"css"/"style.css"
LLMS=ROOT/"llms.txt"
SRC=Path(__file__).resolve().parent.parent/"bundle_about_v53"
IMG_DIR=ROOT/"assets"/"about-v53"
SITE="https://ahmedmansoour.github.io/indoor-positioning-hub"

if not ABOUT.exists():
    raise SystemExit("about.html not found. Run from repository root.")
if not CSS.exists():
    raise SystemExit("assets/css/style.css not found. Run from repository root.")
if not (SRC/"ahmed-ipin-2024.webp").exists():
    raise SystemExit("Bundled image missing.")

IMG_DIR.mkdir(parents=True, exist_ok=True)
shutil.copy2(SRC/"ahmed-ipin-2024.webp", IMG_DIR/"ahmed-ipin-2024.webp")

old = ABOUT.read_text(encoding="utf-8", errors="ignore")
def first(pattern, text):
    m = re.search(pattern, text, flags=re.S|re.I)
    return m.group(1).strip() if m else ""

header = first(r"<body[^>]*>\s*(<header.*?</header>)", old)
footer = first(r"(<footer.*?</footer>)", old)

if not header:
    header = """<header class="site-header">
  <a class="brand" href="index.html">Indoor Positioning Hub</a>
  <nav class="site-nav" aria-label="Main navigation">
    <a href="index.html">Home</a>
    <a href="publications.html">Publications</a>
    <a href="research-themes.html">Research Themes</a>
    <a href="resources.html">Datasets &amp; Code</a>
    <a href="citation-resources.html">Citation Resources</a>
    <a href="about.html" class="active">About</a>
  </nav>
</header>"""

if not footer:
    footer = """<footer class="site-footer"><div class="container"><p>&copy; <span id="year"></span> Ahmed Mansour. Indoor Positioning Research, Engineering, and Deployment Hub.</p></div></footer>"""

header = re.sub(r'(<a href="about\.html")([^>]*)>', r'\1 class="active">', header, flags=re.I)
for page in ["index","publications","research-themes","resources","citation-resources"]:
    header = re.sub(rf'(<a href="{page}\.html")\s+class="active"([^>]*)>', r'\1\2>', header, flags=re.I)

person_json = {
    "@context":"https://schema.org",
    "@type":"Person",
    "name":"Ahmed Mansour",
    "alternateName":"Ahmed M. Mansour",
    "url":SITE + "/about.html",
    "image":SITE + "/assets/about-v53/ahmed-ipin-2024.webp",
    "email":"mailto:mnsoour.a@gmail.com",
    "jobTitle":"Indoor positioning and navigation researcher",
    "affiliation":[{"@type":"Organization","name":"The Hong Kong Polytechnic University"},{"@type":"Organization","name":"Cairo University"}],
    "alumniOf":[{"@type":"CollegeOrUniversity","name":"The Hong Kong Polytechnic University"},{"@type":"CollegeOrUniversity","name":"Cairo University"}],
    "knowsAbout":["Indoor positioning","Indoor localization","Indoor navigation","Pedestrian dead reckoning","Wi-Fi fingerprinting","Mobile crowdsensing","Autonomous radio-map generation","GNSS/PDR integration","3D indoor spatial context","Spatial intelligence"],
    "sameAs":["https://orcid.org/0000-0002-9840-7030","https://scholar.google.com/citations?user=lFhcyh4AAAAJ&hl=en","https://www.scopus.com/authid/detail.uri?authorId=57948539100","https://www.webofscience.com/wos/author/record/ABP-9962-2022","https://www.researchgate.net/profile/Ahmed-Mansour-55","https://www.linkedin.com/in/ahmd-mansour/","https://github.com/AhmedMansoour"]
}
jsonld = json.dumps(person_json, ensure_ascii=False, indent=2)

head = f"""<head>
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width, initial-scale=1">
  <!-- === About page SEO metadata v53 START === -->
  <title>About Ahmed Mansour | Indoor Positioning Hub</title>
  <meta name="description" content="Academic profile of Ahmed Mansour, indoor positioning and navigation researcher working on smartphone sensing, Wi-Fi fingerprinting, PDR, mobile crowdsensing, GNSS/PDR integration, 3D radio-map generation, and deployment-ready indoor spatial intelligence.">
  <meta name="author" content="Ahmed Mansour">
  <meta name="keywords" content="Ahmed Mansour, indoor positioning, indoor localization, indoor navigation, Wi-Fi fingerprinting, pedestrian dead reckoning, PDR, mobile crowdsensing, GNSS/PDR integration, 3D radio map, The Hong Kong Polytechnic University, Cairo University">
  <link rel="canonical" href="{SITE}/about.html">
  <meta property="og:title" content="About Ahmed Mansour | Indoor Positioning Hub">
  <meta property="og:description" content="Academic profile, research identity, timeline, identifiers, CV, and contact information for Ahmed Mansour.">
  <meta property="og:type" content="profile">
  <meta property="og:url" content="{SITE}/about.html">
  <meta property="og:image" content="{SITE}/assets/about-v53/ahmed-ipin-2024.webp">
  <meta name="twitter:card" content="summary_large_image">
  <meta name="twitter:title" content="About Ahmed Mansour | Indoor Positioning Hub">
  <meta name="twitter:description" content="Academic profile and research identity for indoor positioning, Wi-Fi fingerprinting, PDR, mobile crowdsensing, and spatial intelligence.">
  <meta name="twitter:image" content="{SITE}/assets/about-v53/ahmed-ipin-2024.webp">
  <script type="application/ld+json">{jsonld}</script>
  <!-- === About page SEO metadata v53 END === -->
  <link rel="stylesheet" href="assets/css/style.css">
</head>"""
body = '<body class="about-v53-page">\n{header}\n\n<main class="about-v53">\n  <section class="about53-hero">\n    <div class="about53-copy">\n      <p class="about53-eyebrow">About the researcher</p>\n      <h1>Ahmed Mansour</h1>\n      <p class="about53-role">Indoor positioning, smartphone sensing, Wi-Fi fingerprinting, PDR, mobile crowdsensing, and deployment-ready indoor spatial intelligence.</p>\n      <p class="about53-lead">Ahmed Mansour is a civil engineering and geomatics researcher whose work focuses on reliable indoor positioning and navigation in complex indoor and urban environments. His research connects inertial positioning, Wi-Fi fingerprinting, autonomous radio-map generation, mobile crowdsensing, GNSS/PDR integration, indoor-outdoor transition awareness, and multi-floor spatial context.</p>\n      <div class="about53-actions">\n        <a href="publications.html">Publications</a>\n        <a href="research-themes.html">Research areas</a>\n        <a href="assets/cv/ahmed-mansour-public-cv.pdf">Download CV</a>\n        <a href="mailto:mnsoour.a@gmail.com">Contact</a>\n      </div>\n    </div>\n    <figure class="about53-photo">\n      <img src="assets/about-v53/ahmed-ipin-2024.webp" alt="Ahmed Mansour presenting indoor positioning research at IPIN 2024" loading="eager" decoding="async">\n      <figcaption>Presenting indoor positioning research at IPIN 2024.</figcaption>\n    </figure>\n  </section>\n\n  <section class="about53-section about53-identity">\n    <div class="about53-section-head">\n      <p class="about53-eyebrow">Research identity</p>\n      <h2>From positioning signals to indoor spatial intelligence</h2>\n      <p>The hub presents Ahmed Mansour\'s research as a connected pipeline: inertial sensing preserves relative motion, Wi-Fi fingerprinting and radio maps provide indoor reference information, multi-source fusion supports continuity across outdoor and indoor spaces, and 3D spatial context connects positioning outputs to floor-aware and building-level services.</p>\n    </div>\n    <div class="about53-area-grid">\n      <a href="research-themes.html#area-inertial"><span>Area 1</span><strong>Inertial positioning and PDR</strong><small>Heading drift, carrying modes, smartphone sensing, and correction sources.</small></a>\n      <a href="research-themes.html#area-radio-map"><span>Area 2</span><strong>Wi-Fi fingerprinting and radio maps</strong><small>Mobile crowdsensing, autonomous map generation, and reliability-governed updating.</small></a>\n      <a href="research-themes.html#area-seamless"><span>Area 3</span><strong>Seamless indoor-outdoor fusion</strong><small>GNSS, PDR, Wi-Fi, BLE, barometer, maps, and transition awareness.</small></a>\n      <a href="research-themes.html#area-3d"><span>Area 4</span><strong>3D indoor spatial context</strong><small>Floor recognition, vertical positioning, 3D radio maps, and multi-level indoor structure.</small></a>\n    </div>\n  </section>\n\n  <section class="about53-section">\n    <div class="about53-section-head">\n      <p class="about53-eyebrow">Academic timeline</p>\n      <h2>Education and research path</h2>\n    </div>\n    <div class="about53-timeline">\n      <article><span>2013</span><strong>B.Sc. in Civil Engineering and Geomatics</strong><p>Cairo University, Egypt.</p></article>\n      <article><span>2017</span><strong>M.Sc. in Civil Engineering and Geomatics</strong><p>Cairo University, Egypt.</p></article>\n      <article><span>2023</span><strong>Ph.D. in Land Surveying and Geo-Informatics</strong><p>The Hong Kong Polytechnic University. Thesis: <em>Indoor Localization Based on Multi-Sensor Fusion, Crowdsourcing, and Multi-User Collaboration</em>.</p></article>\n      <article><span>2024-2025</span><strong>Postdoctoral and research appointments</strong><p>Research work at The Hong Kong Polytechnic University on indoor positioning, radio mapping, and smartphone-based navigation.</p></article>\n    </div>\n  </section>\n\n  <section class="about53-section">\n    <div class="about53-section-head">\n      <p class="about53-eyebrow">Research outputs</p>\n      <h2>Publication and resource entry points</h2>\n      <p>Use these pages to move from the author profile to papers, citation records, machine-readable metadata, PDFs, and reproducibility notes.</p>\n    </div>\n    <div class="about53-link-grid">\n      <a href="publications.html"><strong>Publication portfolio</strong><span>Visual paper cards, DOI links, PDFs, BibTeX, summaries, and research-area connections.</span></a>\n      <a href="research-themes.html"><strong>Research areas</strong><span>Four-area map connecting methods, sensing sources, deployment problems, and linked papers.</span></a>\n      <a href="resources.html"><strong>Resources</strong><span>PDF index, metadata files, code and dataset status, responsible sharing notes, and reproducibility material.</span></a>\n      <a href="citation-resources.html"><strong>Citation resources</strong><span>Author identifiers, paper finder, DOI links, AI-search prompts, and citation guidance.</span></a>\n      <a href="llms.txt"><strong>llms.txt</strong><span>AI-readable guide to the website, publication pages, research areas, and visual assets.</span></a>\n      <a href="sitemap.xml"><strong>Sitemap</strong><span>Crawlable site map for search engines and indexing tools.</span></a>\n    </div>\n  </section>\n\n  <section class="about53-section">\n    <div class="about53-section-head">\n      <p class="about53-eyebrow">Profiles and identifiers</p>\n      <h2>Academic and professional links</h2>\n    </div>\n    <div class="about53-profile-grid">\n      <a href="https://orcid.org/0000-0002-9840-7030"><strong>ORCID</strong><span>0000-0002-9840-7030</span></a>\n      <a href="https://scholar.google.com/citations?user=lFhcyh4AAAAJ&hl=en"><strong>Google Scholar</strong><span>Ahmed Mansour profile</span></a>\n      <a href="https://www.scopus.com/authid/detail.uri?authorId=57948539100"><strong>Scopus Author ID</strong><span>57948539100</span></a>\n      <a href="https://www.webofscience.com/wos/author/record/ABP-9962-2022"><strong>Web of Science ResearcherID</strong><span>ABP-9962-2022</span></a>\n      <a href="https://www.researchgate.net/profile/Ahmed-Mansour-55"><strong>ResearchGate</strong><span>Ahmed Mansour profile</span></a>\n      <a href="https://www.linkedin.com/in/ahmd-mansour/"><strong>LinkedIn</strong><span>Ahmed Mansour profile</span></a>\n      <a href="https://github.com/AhmedMansoour"><strong>GitHub</strong><span>AhmedMansoour</span></a>\n      <a href="mailto:mnsoour.a@gmail.com"><strong>Email</strong><span>mnsoour.a@gmail.com</span></a>\n    </div>\n  </section>\n\n  <section class="about53-section about53-contact">\n    <div>\n      <p class="about53-eyebrow">Contact and collaboration</p>\n      <h2>Research collaboration and citation inquiries</h2>\n      <p>For questions about indoor positioning, Wi-Fi fingerprinting, pedestrian dead reckoning, mobile crowdsensing, 3D radio-map generation, or citation use of the published papers, use the contact link or start from the publication and citation-resource pages.</p>\n    </div>\n    <div class="about53-contact-actions">\n      <a href="mailto:mnsoour.a@gmail.com">Email Ahmed Mansour</a>\n      <a href="citation-resources.html">Citation guide</a>\n      <a href="assets/cv/ahmed-mansour-public-cv.pdf">Public CV</a>\n    </div>\n  </section>\n</main>\n\n{footer}\n<script src="assets/js/site.js"></script>\n</body>\n</html>'.format(header=header, footer=footer)
ABOUT.write_text("<!doctype html>\n<html lang=\"en\">\n" + head + "\n" + body, encoding="utf-8")
css = CSS.read_text(encoding="utf-8", errors="ignore")
css = re.sub(r"/\* === About page v53 START === \*/.*?/\* === About page v53 END === \*/", "", css, flags=re.S)
CSS.write_text(css.rstrip() + '\n\n' + '/* === About page v53 START === */\n.about-v53{width:min(1180px,calc(100% - 56px));margin:0 auto 48px}\n.about53-hero{display:grid;grid-template-columns:1.05fr .95fr;gap:22px;align-items:stretch;margin:36px 0 24px}\n.about53-copy{padding:32px;border-radius:32px;background:radial-gradient(circle at 78% 12%,rgba(79,196,211,.14),transparent 35%),linear-gradient(180deg,rgba(255,255,255,.98),rgba(246,251,255,.98));border:1px solid rgba(130,165,194,.25);box-shadow:0 22px 50px rgba(20,45,74,.08)}\n.about53-eyebrow{margin:0 0 .55rem;color:#0b6380;text-transform:uppercase;letter-spacing:.12em;font-size:.75rem;font-weight:800}\n.about53-copy h1{margin:0 0 .65rem;color:#073d63;font-size:clamp(2.25rem,5vw,4.4rem);line-height:1;letter-spacing:-.06em}\n.about53-role{margin:0 0 1rem;color:#0b6380;font-weight:800;font-size:1rem;line-height:1.45}\n.about53-lead{margin:0;color:#405b71;font-size:1.04rem;line-height:1.68}\n.about53-actions{display:flex;flex-wrap:wrap;gap:.6rem;margin-top:1.35rem}\n.about53-actions a,.about53-contact-actions a{display:inline-flex;padding:.62rem .85rem;border-radius:999px;background:rgba(83,197,213,.10);border:1px solid rgba(79,159,187,.24);color:#084f72;font-weight:700;text-decoration:none;font-size:.85rem}\n.about53-photo{margin:0;border-radius:32px;overflow:hidden;background:#fff;border:1px solid rgba(130,165,194,.25);box-shadow:0 22px 50px rgba(20,45,74,.08)}\n.about53-photo img{display:block;width:100%;height:100%;min-height:430px;object-fit:cover}\n.about53-photo figcaption{padding:12px 15px;color:#607488;font-size:.84rem;background:#fff}\n.about53-section{margin:24px 0;padding:22px;border-radius:30px;background:linear-gradient(180deg,rgba(255,255,255,.98),rgba(248,252,255,.98));border:1px solid rgba(130,165,194,.23);box-shadow:0 16px 38px rgba(20,45,74,.065)}\n.about53-section-head h2,.about53-contact h2{margin:0 0 .65rem;color:#073d63;font-size:clamp(1.45rem,2.5vw,2.2rem);line-height:1.1;letter-spacing:-.04em}\n.about53-section-head p:not(.about53-eyebrow),.about53-contact p:not(.about53-eyebrow){margin:0;max-width:980px;color:#405b71;font-size:.98rem;line-height:1.65}\n.about53-area-grid,.about53-link-grid,.about53-profile-grid{display:grid;grid-template-columns:repeat(4,1fr);gap:14px;margin-top:18px}\n.about53-area-grid a,.about53-link-grid a,.about53-profile-grid a{display:block;padding:17px;border-radius:22px;background:linear-gradient(180deg,rgba(255,255,255,.96),rgba(248,252,255,.98));border:1px solid rgba(127,160,186,.20);box-shadow:0 10px 24px rgba(20,45,74,.045);text-decoration:none}\n.about53-area-grid span{display:inline-flex;margin-bottom:.55rem;padding:.32rem .55rem;border-radius:999px;background:rgba(83,197,213,.12);color:#084f72;font-size:.72rem;font-weight:800}\n.about53-area-grid strong,.about53-link-grid strong,.about53-profile-grid strong{display:block;color:#073d63;margin-bottom:.35rem}\n.about53-area-grid small,.about53-link-grid span,.about53-profile-grid span{display:block;color:#607488;font-size:.85rem;line-height:1.45}\n.about53-timeline{display:grid;grid-template-columns:repeat(4,1fr);gap:14px;margin-top:18px}\n.about53-timeline article{padding:17px;border-radius:22px;background:linear-gradient(180deg,rgba(239,247,251,.96),rgba(249,252,255,.98));border:1px solid rgba(79,159,187,.17)}\n.about53-timeline span{display:inline-flex;margin-bottom:.55rem;padding:.32rem .55rem;border-radius:999px;background:rgba(83,197,213,.12);color:#084f72;font-size:.72rem;font-weight:800}\n.about53-timeline strong{display:block;color:#073d63;margin-bottom:.35rem}\n.about53-timeline p{margin:0;color:#607488;font-size:.86rem;line-height:1.48}\n.about53-contact{display:grid;grid-template-columns:1fr auto;gap:22px;align-items:center}\n.about53-contact-actions{display:flex;flex-direction:column;gap:.6rem;align-items:flex-start}\n@media(max-width:980px){.about-v53{width:min(100%,calc(100% - 22px))}.about53-hero{grid-template-columns:1fr}.about53-area-grid,.about53-link-grid,.about53-profile-grid,.about53-timeline{grid-template-columns:1fr 1fr}.about53-contact{grid-template-columns:1fr}.about53-photo img{min-height:0}}\n@media(max-width:640px){.about-v53{width:min(100%,calc(100% - 18px))}.about53-copy,.about53-photo,.about53-section{border-radius:24px}.about53-copy,.about53-section{padding:17px}.about53-area-grid,.about53-link-grid,.about53-profile-grid,.about53-timeline{grid-template-columns:1fr}}\n/* === About page v53 END === */' + '\n', encoding='utf-8')

if LLMS.exists():
    llms = LLMS.read_text(encoding="utf-8", errors="ignore")
    add = """
## About Ahmed Mansour

- About page: https://ahmedmansoour.github.io/indoor-positioning-hub/about.html
- Purpose: academic profile, research identity, timeline, profile identifiers, CV link, contact, and Person JSON-LD metadata for Ahmed Mansour.
- Profile image: assets/about-v53/ahmed-ipin-2024.webp
"""
    if "## About Ahmed Mansour" not in llms:
        marker = "## Citation resources and AI-search guide"
        llms = llms.replace(marker, add + "\n" + marker) if marker in llms else llms.rstrip() + "\n" + add + "\n"
        LLMS.write_text(llms, encoding="utf-8")

print("Done: upgraded about.html with academic profile, image, timeline, identifiers, SEO, and Person JSON-LD.")
