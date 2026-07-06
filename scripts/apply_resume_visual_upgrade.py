#!/usr/bin/env python3
from pathlib import Path
import shutil, json, re, html
from datetime import date

ROOT = Path.cwd()
PKG = Path(__file__).resolve().parents[1]

def read(p):
    return p.read_text(encoding='utf-8', errors='ignore')

def write(p, s):
    p.write_text(s, encoding='utf-8', newline='\n')

def copy_tree(src, dst):
    src = Path(src); dst = Path(dst)
    if not src.exists():
        return
    try:
        if src.resolve() == dst.resolve():
            return
    except Exception:
        pass
    for f in src.rglob('*'):
        if f.is_file():
            rel = f.relative_to(src)
            target = dst / rel
            target.parent.mkdir(parents=True, exist_ok=True)
            try:
                if f.resolve() == target.resolve():
                    continue
            except Exception:
                pass
            shutil.copy2(f, target)

def replace_between(text, start, end, new_block, before='</main>'):
    pattern = re.compile(re.escape(start) + r'.*?' + re.escape(end), re.S)
    block = start + '\n' + new_block.strip() + '\n' + end
    if pattern.search(text):
        return pattern.sub(block, text)
    idx = text.lower().rfind(before.lower())
    if idx != -1:
        return text[:idx] + '\n' + block + '\n' + text[idx:]
    return text + '\n' + block + '\n'

def add_nav_link(text, href, label):
    if f'href="{href}"' in text or f"href='{href}'" in text:
        return text
    candidates = [
        ('<a href="about.html">About</a>', f'<a href="about.html">About</a>\n        <a href="{href}">{label}</a>'),
        ('<a href="../about.html">About</a>', f'<a href="../about.html">About</a>\n        <a href="../{href}">{label}</a>'),
    ]
    for old, new in candidates:
        if old in text:
            return text.replace(old, new)
    return text

def build_nav(relative=False):
    prefix = '../' if relative else ''
    return f"""<header class="site-header">
    <nav class="nav container">
      <a class="brand" href="{prefix}index.html">Indoor Positioning Hub</a>
      <button class="nav-toggle" aria-label="Toggle navigation">☰</button>
      <div class="nav-links">
        <a href="{prefix}publications.html">Publications</a>
        <a href="{prefix}research-themes.html">Research Themes</a>
        <a href="{prefix}resources.html">Datasets & Code</a>
        <a href="{prefix}citation-resources.html">Citation Resources</a>
        <a href="{prefix}about.html">About</a>
        <a href="{prefix}cv.html">CV</a>
      </div>
    </nav>
  </header>"""

CV_HTML = """<!doctype html>
<html lang="en">
<head>
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width, initial-scale=1">
  <title>Ahmed Mansour CV | Indoor Positioning Hub</title>
  <meta name="description" content="Public academic CV of Ahmed Mansour: indoor positioning, smartphone localization, Wi-Fi fingerprinting, PDR, mobile crowdsensing, multi-sensor fusion, and indoor spatial intelligence.">
  <meta name="author" content="Ahmed Mansour">
  <meta name="keywords" content="Ahmed Mansour CV, indoor positioning, indoor localization, Wi-Fi fingerprinting, PDR, mobile crowdsensing, geomatics, PolyU, Cairo University">
  <meta property="og:title" content="Ahmed Mansour CV">
  <meta property="og:description" content="Academic profile, CV, research expertise, publications, education, and service activity of Ahmed Mansour.">
  <meta property="og:type" content="profile">
  <link rel="stylesheet" href="assets/css/style.css">
  <script type="application/ld+json">
  {
    "@context": "https://schema.org",
    "@type": "Person",
    "name": "Ahmed Mansour",
    "honorificSuffix": "Ph.D.",
    "jobTitle": ["Postdoctoral Fellow", "Assistant Professor (Adjunct)"],
    "affiliation": [
      {"@type":"Organization", "name":"The Hong Kong Polytechnic University"},
      {"@type":"Organization", "name":"Cairo University"}
    ],
    "url": "https://ahmedmansoour.github.io/indoor-positioning-hub/cv.html",
    "sameAs": [
      "https://scholar.google.com/citations?user=lFhcyh4AAAAJ&hl=en",
      "https://orcid.org/0000-0002-9840-7030",
      "https://www.researchgate.net/profile/Ahmed-Mansour-55",
      "https://github.com/AhmedMansoour"
    ],
    "knowsAbout": ["indoor positioning", "Wi-Fi fingerprinting", "pedestrian dead reckoning", "mobile crowdsensing", "multi-sensor fusion", "indoor spatial intelligence"]
  }
  </script>
</head>
<body>
""" + build_nav(False) + """

  <main>
    <section class="container cv-hero resume-hero">
      <div class="resume-hero-text">
        <p class="eyebrow">Public academic profile</p>
        <h1>Ahmed Mansour, Ph.D.</h1>
        <p class="lead">Indoor positioning researcher working at the intersection of smartphone localization, Wi-Fi fingerprinting, pedestrian dead reckoning, mobile crowdsensing, multi-sensor fusion, and indoor spatial intelligence.</p>
        <div class="actions">
          <a class="button primary" href="assets/cv/ahmed-mansour-public-cv.pdf">Download public CV</a>
          <a class="button" href="publications.html">View publications</a>
          <a class="button" href="research-themes.html#visual-research-atlas">Visual research atlas</a>
        </div>
      </div>
      <figure class="resume-photo-card">
        <img src="assets/img/profile/ahmed-mansour-photo.webp" alt="Ahmed Mansour profile photo">
        <figcaption>Postdoctoral Fellow, The Hong Kong Polytechnic University<br>Assistant Professor (Adjunct), Cairo University</figcaption>
      </figure>
    </section>

    <section class="container resume-grid">
      <article class="card resume-card wide">
        <h2>Research profile</h2>
        <p>Ahmed Mansour develops positioning and sensing methods that help indoor and urban environments become spatially aware. His work connects wireless fingerprints, smartphone inertial signals, magnetic and barometric cues, user motion, and context-aware logic into practical pipelines for scalable indoor localization.</p>
        <p>The main research direction is deployment-ready indoor spatial intelligence: systems that can learn from ordinary mobile data, control drift, assess reliability, handle changing phone poses, and support seamless transitions between indoor and outdoor spaces.</p>
      </article>
      <article class="card resume-card">
        <h2>Academic links</h2>
        <ul class="link-list compact">
          <li><a href="https://scholar.google.com/citations?user=lFhcyh4AAAAJ&hl=en">Google Scholar</a></li>
          <li><a href="https://orcid.org/0000-0002-9840-7030">ORCID: 0000-0002-9840-7030</a></li>
          <li><a href="https://www.researchgate.net/profile/Ahmed-Mansour-55">ResearchGate</a></li>
          <li><a href="https://github.com/AhmedMansoour">GitHub</a></li>
          <li><a href="https://www.linkedin.com/in/ahmd-mansour/">LinkedIn</a></li>
        </ul>
      </article>
    </section>

    <section class="container resume-section">
      <h2>Academic appointments</h2>
      <div class="timeline-list">
        <article class="timeline-item"><span>2023 - Present</span><div><h3>Postdoctoral Fellow, The Hong Kong Polytechnic University</h3><p>Research on scalable indoor positioning systems, mobile crowdsensing, uncertainty-aware radio-map lifecycle management, hybrid positioning pipelines, multimodal sensing, and deployment-oriented IPS frameworks.</p></div></article>
        <article class="timeline-item"><span>2021 - 2023</span><div><h3>Research Associate, The Hong Kong Polytechnic University</h3><p>Research on drift-resilient heading estimation, Wi-Fi fingerprinting, magnetic stability, smartphone-based positioning, and deep learning for pedestrian navigation.</p></div></article>
        <article class="timeline-item"><span>2014 - 2017</span><div><h3>Lecturer and Teaching Assistant, Cairo University</h3><p>Teaching and laboratory instruction in geomatics, GNSS, surveying, field training, and geospatial data analysis.</p></div></article>
      </div>
    </section>

    <section class="container resume-section two-column-cv">
      <div>
        <h2>Education</h2>
        <div class="timeline-list compact-timeline">
          <article class="timeline-item"><span>2017 - 2023</span><div><h3>Ph.D. in Land Surveying and Geo-Informatics</h3><p>The Hong Kong Polytechnic University. Thesis: <em>Indoor Localization Based on Multi-Sensor Fusion, Crowdsourcing, and Multi-User Collaboration</em>. Coursework GPA: 3.75/4.00. Thesis grade: Excellent.</p></div></article>
          <article class="timeline-item"><span>2013 - 2017</span><div><h3>M.Sc. in Geomatics Engineering</h3><p>Cairo University. Thesis: <em>Performance of Real-Time Precise Point Positioning Using IGS Real-Time Service in Egypt</em>. Coursework GPA: 3.70/4.00. Thesis grade: Excellent.</p></div></article>
          <article class="timeline-item"><span>2008 - 2013</span><div><h3>B.Sc. in Civil Engineering</h3><p>Cairo University. Graduated with Distinction with Honors. GPA: 3.90/4.00, ranked 13th out of 400 students.</p></div></article>
        </div>
      </div>
      <div>
        <h2>Core expertise</h2>
        <ul class="tag-cloud-list">
          <li>Indoor positioning</li><li>Indoor localization</li><li>Wi-Fi fingerprinting</li><li>Pedestrian dead reckoning</li><li>Smartphone heading</li><li>Mobile crowdsensing</li><li>Radio-map updating</li><li>Reliability assessment</li><li>Multi-sensor fusion</li><li>BLE/GNSS/PDR integration</li><li>Machine learning</li><li>Indoor spatial intelligence</li>
        </ul>
      </div>
    </section>

    <section class="container resume-section">
      <h2>Selected contribution areas</h2>
      <div class="grid three visual-topic-grid">
        <article class="card mini-card"><h3>Scalable IPS</h3><p>Reducing manual survey effort through crowdsensed fingerprints, autonomous radio-map generation, and user-centered data collection.</p></article>
        <article class="card mini-card"><h3>Robust smartphone PDR</h3><p>Improving heading, step, and pose-aware navigation under handheld, pocket, swinging, calling, and mixed phone use.</p></article>
        <article class="card mini-card"><h3>Seamless navigation</h3><p>Connecting indoor and outdoor states through context-aware indicators, IOD decisions, and handover-ready positioning logic.</p></article>
      </div>
    </section>

    <section class="container resume-section">
      <h2>Professional service and skills</h2>
      <div class="resume-grid">
        <article class="card"><h3>Peer review</h3><p>Completed 71 peer reviews across scholarly venues including IEEE Transactions on Instrumentation and Measurement, IEEE Internet of Things Journal, IEEE Sensors Journal, IEEE Access, Measurement, Remote Sensing, Sensors, Electronics, and Applied Sciences.</p></article>
        <article class="card"><h3>Technical skills</h3><p>Python, Java, R, LaTeX, scientific visualization, data analysis, Wi-Fi/BLE/GNSS/PDR pipelines, machine learning, deep learning, Kalman filtering, spatial data processing, and reproducible research workflows.</p></article>
      </div>
    </section>
  </main>

  <footer class="site-footer">
    <div class="container"><p>© <span id="year"></span> Ahmed Mansour. Indoor Positioning Research, Engineering, and Deployment Hub.</p></div>
  </footer>
  <script src="assets/js/site.js"></script>
</body>
</html>
"""

def research_atlas_section():
    data = json.loads((ROOT / 'data/visual_research_figures.json').read_text(encoding='utf-8'))
    cards = []
    for item in data:
        cards.append(f"""<article class="visual-atlas-card">
          <img src="assets/img/research/{html.escape(item['file'])}" alt="{html.escape(item['title'])}">
          <div class="visual-atlas-caption">
            <h3>{html.escape(item['title'])}</h3>
            <p>{html.escape(item['caption'])}</p>
          </div>
        </article>""")
    return """<section id="visual-research-atlas" class="container visual-atlas-section">
      <p class="eyebrow">Visual research atlas</p>
      <h2>Indoor positioning research, shown as a system</h2>
      <p class="section-lead">These figures make the hub easier to scan. They show the core logic behind Ahmed Mansour's research: users move, phones sense, signals change, context explains the movement, and reliability gates decide what can be trusted.</p>
      <div class="visual-atlas-grid">
        """ + '\n'.join(cards) + """
      </div>
    </section>"""

def home_visual_section():
    return """<section id="profile-visual-entry" class="container home-visual-entry">
      <div class="home-visual-copy">
        <p class="eyebrow">Profile, CV, and visual research map</p>
        <h2>From publication list to research identity</h2>
        <p>This hub now works as both a publication resource and a compact academic website. Readers can move from Ahmed Mansour's CV to research themes, visual explanations, paper summaries, PDFs, BibTeX entries, and citation notes.</p>
        <div class="actions">
          <a class="button primary" href="cv.html">Open CV</a>
          <a class="button" href="research-themes.html#visual-research-atlas">Explore visual atlas</a>
        </div>
      </div>
      <figure class="home-visual-figure">
        <img src="assets/img/research/smart-building-positioning-system.webp" alt="Smart building positioning system visual">
        <figcaption>Smart building positioning system, connecting indoor geometry, smartphones, wireless signals, and route intelligence.</figcaption>
      </figure>
    </section>"""

def about_cv_teaser():
    return """<section id="cv-profile-card" class="container cv-profile-card-section">
      <div class="card cv-profile-card">
        <img src="assets/img/profile/ahmed-mansour-photo.webp" alt="Ahmed Mansour profile photo">
        <div>
          <p class="eyebrow">Academic CV</p>
          <h2>Ahmed Mansour, Ph.D.</h2>
          <p>Postdoctoral Fellow at The Hong Kong Polytechnic University and Assistant Professor (Adjunct) at Cairo University. Research focus: indoor positioning, Wi-Fi fingerprinting, PDR, mobile crowdsensing, multi-sensor fusion, and indoor spatial intelligence.</p>
          <div class="actions compact-actions">
            <a class="button primary" href="cv.html">View CV page</a>
            <a class="button" href="assets/cv/ahmed-mansour-public-cv.pdf">Download public CV</a>
          </div>
        </div>
      </div>
    </section>"""

def paper_figures_section(slug, figures):
    cards = []
    for fig in figures:
        cards.append(f"""<figure class="paper-visual-card">
          <img src="{html.escape(fig['file'])}" alt="{html.escape(fig['title'])}" loading="lazy">
          <figcaption><strong>{html.escape(fig['title'])}.</strong> {html.escape(fig['caption'])}</figcaption>
        </figure>""")
    return """<section id="paper-visuals" class="paper-visuals-section card">
      <h2>Key visual explanation</h2>
      <p>These selected visuals help readers understand the method quickly before reading the full paper.</p>
      <div class="paper-visual-grid">
        """ + '\n'.join(cards) + """
      </div>
    </section>"""

def insert_before_section(text, section_html, preferred_patterns):
    for pat in preferred_patterns:
        m = re.search(pat, text, re.I)
        if m:
            return text[:m.start()] + section_html + '\n' + text[m.start():]
    idx = text.lower().rfind('</main>')
    if idx != -1:
        return text[:idx] + section_html + '\n' + text[idx:]
    return text + '\n' + section_html

def update_publication_figures():
    reg_path = ROOT / 'data/publication_figures.json'
    if not reg_path.exists():
        return
    registry = json.loads(reg_path.read_text(encoding='utf-8'))
    for slug, figs in registry.items():
        p = ROOT / 'publications' / f'{slug}.html'
        if not p.exists():
            continue
        text = read(p)
        start = '<!-- BEGIN paper visual explanation -->'
        end = '<!-- END paper visual explanation -->'
        block = paper_figures_section(slug, figs)
        text = re.sub(re.escape(start) + r'.*?' + re.escape(end), '', text, flags=re.S)
        text = re.sub(r'\n?\s*<section[^>]+id="paper-visuals".*?</section>\s*\n?', '\n', text, flags=re.S | re.I)
        wrapped = start + '\n' + block + '\n' + end + '\n'
        text = insert_before_section(text, wrapped, [
            r'<section[^>]*class="[^"]*when-to-cite',
            r'<section[^>]*id="when-to-cite',
            r'<section[^>]*class="[^"]*bibtex',
            r'<h2>When to cite</h2>',
            r'<h2>BibTeX</h2>'
        ])
        write(p, text)

copy_tree(PKG / 'assets', ROOT / 'assets')
copy_tree(PKG / 'data', ROOT / 'data')

for p in list(ROOT.glob('*.html')) + list((ROOT / 'publications').glob('*.html')):
    if p.exists():
        t = read(p)
        if p.parent.name == 'publications':
            t = add_nav_link(t, '../cv.html', 'CV')
        else:
            t = add_nav_link(t, 'cv.html', 'CV')
        write(p, t)

write(ROOT / 'cv.html', CV_HTML)

idx = ROOT / 'index.html'
if idx.exists():
    t = read(idx)
    if 'href="cv.html"' not in t:
        t = t.replace('<a class="button" href="citation-resources.html">Citation Resources</a>', '<a class="button" href="citation-resources.html">Citation Resources</a>\n        <a class="button" href="cv.html">CV</a>')
    t = replace_between(t, '<!-- BEGIN profile visual entry -->', '<!-- END profile visual entry -->', home_visual_section())
    write(idx, t)

ap = ROOT / 'about.html'
if ap.exists():
    t = read(ap)
    t = replace_between(t, '<!-- BEGIN CV profile card -->', '<!-- END CV profile card -->', about_cv_teaser())
    write(ap, t)

rp = ROOT / 'research-themes.html'
if rp.exists():
    t = read(rp)
    t = replace_between(t, '<!-- BEGIN visual research atlas -->', '<!-- END visual research atlas -->', research_atlas_section())
    write(rp, t)

update_publication_figures()

css_path = ROOT / 'assets/css/style.css'
css_path.parent.mkdir(parents=True, exist_ok=True)
css = read(css_path) if css_path.exists() else ''
css_block = r'''
/* ============================================================
   Resume, CV, visual research atlas, and publication figures
   Added by scripts/apply_resume_visual_upgrade.py
   ============================================================ */
.resume-hero,
.home-visual-entry {
  display: grid;
  grid-template-columns: minmax(0, 1.15fr) minmax(280px, 0.85fr);
  gap: 2rem;
  align-items: center;
}
.resume-hero { padding-top: 3rem; padding-bottom: 2rem; }
.resume-photo-card,
.home-visual-figure {
  background: var(--card, #fff);
  border: 1px solid var(--border, #dfe7ea);
  border-radius: 22px;
  overflow: hidden;
  box-shadow: 0 20px 45px rgba(13, 45, 55, 0.10);
}
.resume-photo-card img { width: 100%; max-height: 420px; object-fit: cover; object-position: top center; display: block; }
.home-visual-figure img { width: 100%; display: block; }
.resume-photo-card figcaption,
.home-visual-figure figcaption,
.paper-visual-card figcaption,
.visual-atlas-caption p {
  color: var(--muted-foreground, #56646b);
  font-size: 0.93rem;
  line-height: 1.55;
}
.resume-photo-card figcaption,
.home-visual-figure figcaption { padding: 1rem 1.1rem; }
.resume-grid,
.two-column-cv {
  display: grid;
  grid-template-columns: minmax(0, 1fr) minmax(280px, 0.68fr);
  gap: 1.25rem;
}
.resume-card.wide { min-height: 100%; }
.resume-section { padding-top: 1.4rem; padding-bottom: 1.4rem; }
.timeline-list { display: grid; gap: 0.9rem; }
.timeline-item {
  display: grid;
  grid-template-columns: 130px minmax(0, 1fr);
  gap: 1rem;
  padding: 1rem;
  background: var(--card, #fff);
  border: 1px solid var(--border, #dfe7ea);
  border-radius: 16px;
}
.timeline-item span { font-weight: 700; color: var(--primary, #0d6f7e); font-size: 0.9rem; }
.timeline-item h3 { margin: 0 0 0.35rem; }
.timeline-item p { margin: 0; color: var(--muted-foreground, #56646b); }
.tag-cloud-list { list-style: none; padding: 0; margin: 0; display: flex; flex-wrap: wrap; gap: 0.55rem; }
.tag-cloud-list li {
  padding: 0.46rem 0.7rem;
  border-radius: 999px;
  background: rgba(13, 111, 126, 0.08);
  border: 1px solid rgba(13, 111, 126, 0.15);
  color: var(--primary, #0d6f7e);
  font-weight: 650;
  font-size: 0.88rem;
}
.link-list.compact { padding-left: 1.1rem; }
.compact-actions { gap: 0.6rem; flex-wrap: wrap; }
.cv-profile-card {
  display: grid;
  grid-template-columns: 150px minmax(0, 1fr);
  gap: 1.2rem;
  align-items: center;
}
.cv-profile-card img { width: 150px; height: 150px; object-fit: cover; object-position: top center; border-radius: 18px; }
.visual-atlas-section { padding-top: 2rem; padding-bottom: 2.5rem; }
.section-lead { max-width: 850px; color: var(--muted-foreground, #56646b); font-size: 1.05rem; line-height: 1.7; }
.visual-atlas-grid {
  display: grid;
  grid-template-columns: repeat(2, minmax(0, 1fr));
  gap: 1.25rem;
  margin-top: 1.25rem;
}
.visual-atlas-card {
  background: var(--card, #fff);
  border: 1px solid var(--border, #dfe7ea);
  border-radius: 20px;
  overflow: hidden;
  box-shadow: 0 16px 34px rgba(13, 45, 55, 0.08);
}
.visual-atlas-card img { width: 100%; display: block; background: #fff; }
.visual-atlas-caption { padding: 1rem 1.1rem 1.15rem; }
.visual-atlas-caption h3 { margin: 0 0 0.45rem; }
.home-visual-entry { padding-top: 2rem; padding-bottom: 2rem; }
.paper-visuals-section { margin-top: 1.25rem; }
.paper-visual-grid { display: grid; grid-template-columns: repeat(2, minmax(0, 1fr)); gap: 1rem; margin-top: 1rem; }
.paper-visual-card {
  margin: 0;
  background: #fff;
  border: 1px solid var(--border, #dfe7ea);
  border-radius: 16px;
  overflow: hidden;
}
.paper-visual-card img { width: 100%; display: block; background: #fff; }
.paper-visual-card figcaption { padding: 0.9rem 1rem 1rem; }
.mini-card h3 { margin-top: 0; }
@media (max-width: 850px) {
  .resume-hero,
  .home-visual-entry,
  .resume-grid,
  .two-column-cv,
  .visual-atlas-grid,
  .paper-visual-grid,
  .cv-profile-card { grid-template-columns: 1fr; }
  .timeline-item { grid-template-columns: 1fr; }
  .cv-profile-card img { width: 120px; height: 120px; }
}
'''
if 'Resume, CV, visual research atlas, and publication figures' not in css:
    css = css.rstrip() + '\n\n' + css_block.strip() + '\n'
    write(css_path, css)

sitemap = ROOT / 'sitemap.xml'
base_url = 'https://ahmedmansoour.github.io/indoor-positioning-hub/'
if sitemap.exists():
    s = read(sitemap)
    today = date.today().isoformat()
    for u in ['cv.html', 'assets/cv/ahmed-mansour-public-cv.pdf']:
        loc = base_url + u
        if loc not in s:
            entry = f'  <url>\n    <loc>{loc}</loc>\n    <lastmod>{today}</lastmod>\n  </url>\n'
            s = s.replace('</urlset>', entry + '</urlset>')
    write(sitemap, s)

llms = ROOT / 'llms.txt'
if llms.exists():
    t = read(llms)
    start = '<!-- BEGIN CV_VISUAL_UPGRADE -->'
    end = '<!-- END CV_VISUAL_UPGRADE -->'
    block = """## Ahmed Mansour profile, CV, and visual research atlas
- CV page: /cv.html
- Public CV PDF: /assets/cv/ahmed-mansour-public-cv.pdf
- Visual research atlas: /research-themes.html#visual-research-atlas
- Research visual assets: /assets/img/research/
- Publication-level visual explanations: /assets/figures/

The CV and visual atlas describe Ahmed Mansour's work in indoor positioning, Wi-Fi fingerprinting, pedestrian dead reckoning, smartphone sensing, mobile crowdsensing, radio-map reliability, indoor-outdoor awareness, and indoor spatial intelligence. Dedicated funds and research-project sections are intentionally not included in the public CV page at this stage."""
    pattern = re.compile(re.escape(start) + r'.*?' + re.escape(end), re.S)
    repl = start + '\n' + block + '\n' + end
    if pattern.search(t):
        t = pattern.sub(repl, t)
    else:
        t = t.rstrip() + '\n\n' + repl + '\n'
    write(llms, t)

print('[OK] Resume/CV and visual research upgrade applied.')
print('[OK] Added cv.html, public CV PDF, profile image, research atlas images, and publication visual sections.')
print('[NEXT] Review locally, then run:')
print('      git add cv.html assets data publications index.html about.html research-themes.html sitemap.xml llms.txt scripts/apply_resume_visual_upgrade.py')
print('      git commit -m "Add CV page and visual research atlas"')
print('      git push')
