from pathlib import Path
import re

ROOT = Path('.')
CSS_PATH = ROOT / 'assets' / 'css' / 'style.css'
INDEX_PATH = ROOT / 'index.html'

NAV_ROOT = '''<nav class="site-nav" aria-label="Main navigation">
  <a href="index.html">Home</a>
  <a href="publications.html">Publications</a>
  <a href="research-themes.html">Research Themes</a>
  <a href="resources.html">Datasets &amp; Code</a>
  <a href="citation-resources.html">Citation Resources</a>
  <a href="about.html">About</a>
</nav>'''

NAV_SUB = '''<nav class="site-nav" aria-label="Main navigation">
  <a href="../index.html">Home</a>
  <a href="../publications.html">Publications</a>
  <a href="../research-themes.html">Research Themes</a>
  <a href="../resources.html">Datasets &amp; Code</a>
  <a href="../citation-resources.html">Citation Resources</a>
  <a href="../about.html">About</a>
</nav>'''

HOME_MAIN = r'''<main class="hub-home-v20" id="home">
  <section class="home-hero-v20" aria-label="Indoor Positioning Hub hero">
    <div class="home-hero-bg-v20" aria-hidden="true"></div>
    <div class="home-hero-grid-v20">
      <div class="home-hero-copy-v20">
        <p class="eyebrow-v20">Indoor Positioning Hub</p>
        <h1>Indoor positioning research, engineering, and deployment</h1>
        <p class="lead-v20">This hub presents the academic profile, publications, research themes, visual summaries, citation resources, and downloadable outputs of <strong>Ahmed Mansour, Ph.D.</strong>, with a focus on indoor localization, mobile crowdsensing, Wi-Fi fingerprinting, PDR, radio-map intelligence, indoor-outdoor awareness, and spatially aware built environments.</p>
        <div class="hero-actions-v20">
          <a class="btn primary" href="publications.html">Explore publications</a>
          <a class="btn secondary" href="research-themes.html">View research themes</a>
          <a class="btn ghost" href="about.html">Academic profile</a>
        </div>
        <div class="hero-meta-v20" aria-label="Research keywords">
          <span>Wi-Fi fingerprinting</span>
          <span>Pedestrian dead reckoning</span>
          <span>Mobile crowdsensing</span>
          <span>Indoor-outdoor positioning</span>
          <span>Deployment-ready IPS</span>
        </div>
      </div>
      <div class="home-hero-visual-v20">
        <img src="assets/home/indoor-navigation-office.webp" alt="Indoor navigation and positioning inside a smart building" loading="eager" decoding="async">
        <div class="floating-stat-v20 top"><strong>17+</strong><span>research outputs</span></div>
        <div class="floating-stat-v20 bottom"><strong>IPS</strong><span>signals, motion, maps, and context</span></div>
      </div>
    </div>
  </section>

  <section class="affiliation-strip-v20" aria-label="Affiliations and academic background">
    <div class="affiliation-card-v20">
      <img src="assets/home/polyu-logo.webp" alt="The Hong Kong Polytechnic University affiliation logo" loading="lazy" decoding="async">
      <div><strong>Research training and postdoctoral work</strong><span>Geomatics, indoor positioning, multi-sensor localization, and smart built environments.</span></div>
    </div>
    <div class="affiliation-card-v20 cairo-logo-card-v20">
      <img src="assets/home/cairo-university-logo.webp" alt="Cairo University logo" loading="lazy" decoding="async">
      <div><strong>Cairo University foundation</strong><span>Civil engineering, public works, geomatics, and surveying background.</span></div>
    </div>
  </section>

  <section class="home-section-v20 home-profile-v20" aria-label="Profile summary">
    <div class="section-heading-v20">
      <p class="eyebrow-v20">Academic profile</p>
      <h2>From positioning measurements to indoor spatial intelligence</h2>
      <p>The hub is organized to help readers move quickly from a research question to the relevant paper, method, dataset, figure, or citation entry. The work connects smartphone sensing, radio signals, human mobility, map information, and deployment constraints into practical positioning systems for buildings, campuses, cities, and smart built environments.</p>
    </div>
    <div class="profile-grid-v20">
      <article class="profile-card-v20">
        <img src="assets/home/positioning-icon.webp" alt="Indoor positioning icon" loading="lazy" decoding="async">
        <h3>Localization and navigation</h3>
        <p>Indoor positioning, seamless indoor-outdoor awareness, GNSS/PDR integration, collaborative localization, and smartphone-based pedestrian navigation.</p>
      </article>
      <article class="profile-card-v20">
        <img src="assets/home/building-pin-icon.webp" alt="Building positioning icon" loading="lazy" decoding="async">
        <h3>Buildings and deployment</h3>
        <p>Research designed around real indoor spaces, user burden, sensing availability, device constraints, map maintenance, and operational readiness.</p>
      </article>
      <article class="profile-card-v20">
        <img src="assets/home/campus-pin-icon.webp" alt="Campus positioning icon" loading="lazy" decoding="async">
        <h3>Spatial intelligence</h3>
        <p>Positioning outputs are framed as spatial information that can support safe movement, indoor services, digital buildings, and context-aware decisions.</p>
      </article>
    </div>
  </section>

  <section class="home-section-v20 research-atlas-v20" id="visual-research-atlas" aria-label="Research themes and visual research atlas">
    <div class="section-heading-v20 centered">
      <p class="eyebrow-v20">Research themes and visual research atlas</p>
      <h2>A thematic map of indoor positioning research, engineering, and deployment</h2>
      <p>These visual pathways summarize how the research moves from smartphone measurements and radio maps toward scalable, user-friendly, and deployment-aware indoor spatial intelligence.</p>
    </div>
    <div class="atlas-grid-v20">
      <article class="atlas-card-v20 large">
        <img src="assets/home/layered-building-positioning.webp" alt="Layered building positioning visualization" loading="lazy" decoding="async">
        <div class="atlas-card-body-v20">
          <h3>Smart indoor localization pipeline</h3>
          <p>Building-level localization depends on signals, sensors, motion traces, floor structure, and context. This theme connects Wi-Fi fingerprinting, PDR, and map-aware reasoning for practical indoor services.</p>
          <a href="publications.html">Open related publications</a>
        </div>
      </article>
      <article class="atlas-card-v20">
        <img src="assets/home/indoor-navigation-office.webp" alt="Indoor navigation in a modern building" loading="lazy" decoding="async">
        <div class="atlas-card-body-v20">
          <h3>Deployment-ready indoor navigation</h3>
          <p>Positioning systems must work under movement, crowds, device variation, and changing environments, not only in controlled test settings.</p>
          <a href="research-themes.html">Explore themes</a>
        </div>
      </article>
      <article class="atlas-card-v20 text-card-v20">
        <h3>Core research directions</h3>
        <ul>
          <li>Indoor positioning and localization</li>
          <li>Wi-Fi fingerprinting and autonomous radio maps</li>
          <li>Pedestrian dead reckoning and heading control</li>
          <li>Mobile crowdsensing and user-centered IPS</li>
          <li>Indoor-outdoor awareness and seamless positioning</li>
          <li>Spatial intelligence for smart built environments</li>
        </ul>
      </article>
    </div>
  </section>

  <section class="home-section-v20 publication-entry-v20" aria-label="Publication and citation access">
    <div class="section-heading-v20">
      <p class="eyebrow-v20">Publication access</p>
      <h2>Find papers, PDFs, citation records, and visual explanations</h2>
      <p>Each publication page includes a first-page preview, direct PDF access when available, DOI metadata, BibTeX, suggested citation context, long research-story summary, and selected visual explanations.</p>
    </div>
    <div class="entry-grid-v20">
      <a href="publications.html"><strong>Publication portfolio</strong><span>Visual cards with paper previews, DOI links, venues, and topic cues.</span></a>
      <a href="citation-resources.html"><strong>Citation resources</strong><span>BibTeX, citation-ready paper titles, and when-to-cite guidance.</span></a>
      <a href="resources.html"><strong>Datasets and code</strong><span>Shared resources, reproducibility links, and research materials.</span></a>
      <a href="about.html"><strong>About Ahmed Mansour</strong><span>Academic background, research focus, and contact links.</span></a>
    </div>
  </section>
</main>'''

CSS_BLOCK = r'''
/* === Homepage logo/background redesign v20 START === */
:root {
  --hub-ink: #0b2239;
  --hub-blue: #0b5c7b;
  --hub-cyan: #39b9d3;
  --hub-soft: #eef7fb;
  --hub-card: rgba(255, 255, 255, 0.82);
  --hub-border: rgba(70, 130, 165, 0.22);
  --hub-shadow: 0 24px 70px rgba(8, 30, 55, 0.12);
}

body {
  background:
    radial-gradient(circle at top left, rgba(50, 188, 211, 0.18), transparent 36rem),
    linear-gradient(135deg, #f5fbff 0%, #ffffff 46%, #eef6fb 100%) !important;
}

body > header,
.site-header {
  position: sticky !important;
  top: 0 !important;
  z-index: 50 !important;
  display: flex !important;
  align-items: center !important;
  justify-content: space-between !important;
  gap: 1.25rem !important;
  padding: 0.72rem clamp(1rem, 4vw, 3rem) !important;
  background: rgba(255, 255, 255, 0.88) !important;
  backdrop-filter: blur(18px) !important;
  border-bottom: 1px solid rgba(60, 118, 150, 0.14) !important;
  box-shadow: 0 12px 30px rgba(8, 28, 48, 0.06) !important;
}

body > header > :first-child,
.site-title,
.site-brand,
.logo {
  font-weight: 900 !important;
  color: var(--hub-ink) !important;
  letter-spacing: -0.02em !important;
}

.site-nav,
body > header nav {
  margin-left: auto !important;
  display: flex !important;
  flex-wrap: wrap !important;
  justify-content: flex-end !important;
  align-items: center !important;
  gap: 0.35rem !important;
}

.site-nav a,
body > header nav a {
  display: inline-flex !important;
  align-items: center !important;
  min-height: 2.1rem !important;
  padding: 0.45rem 0.72rem !important;
  border-radius: 999px !important;
  color: #0d4e70 !important;
  text-decoration: none !important;
  font-weight: 750 !important;
  font-size: 0.94rem !important;
  transition: background 0.2s ease, transform 0.2s ease, color 0.2s ease !important;
}

.site-nav a:first-child,
body > header nav a:first-child {
  color: white !important;
  background: linear-gradient(135deg, #0b6e8f, #21a9c7) !important;
  box-shadow: 0 10px 25px rgba(13, 122, 155, 0.20) !important;
}

.site-nav a:hover,
body > header nav a:hover {
  background: rgba(30, 164, 195, 0.12) !important;
  transform: translateY(-1px) !important;
}

.hub-home-v20 {
  overflow: hidden;
}

.home-hero-v20 {
  position: relative;
  margin: 0 auto;
  padding: clamp(3rem, 7vw, 6rem) clamp(1rem, 4vw, 3.5rem) 2.5rem;
  max-width: 1440px;
}

.home-hero-bg-v20 {
  position: absolute;
  inset: 1.2rem clamp(0.5rem, 2vw, 1.5rem) auto;
  height: min(62vw, 690px);
  background:
    linear-gradient(90deg, rgba(245, 251, 255, 0.97), rgba(245, 251, 255, 0.70), rgba(255, 255, 255, 0.92)),
    url('../home/abstract-lines-bg.webp') center/cover no-repeat;
  border-radius: 38px;
  border: 1px solid rgba(80, 142, 170, 0.14);
  box-shadow: var(--hub-shadow);
  z-index: -1;
}

.home-hero-grid-v20 {
  display: grid;
  grid-template-columns: minmax(0, 0.92fr) minmax(360px, 1.08fr);
  gap: clamp(1.5rem, 4vw, 4rem);
  align-items: center;
}

.eyebrow-v20 {
  margin: 0 0 0.9rem;
  color: #087c82;
  text-transform: uppercase;
  letter-spacing: 0.16em;
  font-weight: 900;
  font-size: 0.83rem;
}

.home-hero-copy-v20 h1 {
  margin: 0;
  max-width: 11.5em;
  color: var(--hub-ink);
  font-size: clamp(3rem, 7vw, 6.8rem);
  line-height: 0.88;
  letter-spacing: -0.075em;
}

.lead-v20 {
  margin: 1.4rem 0 0;
  max-width: 780px;
  color: #4d6478;
  font-size: clamp(1.05rem, 1.6vw, 1.32rem);
  line-height: 1.78;
}

.hero-actions-v20,
.hero-meta-v20 {
  display: flex;
  flex-wrap: wrap;
  gap: 0.75rem;
  margin-top: 1.55rem;
}

.btn {
  display: inline-flex;
  align-items: center;
  justify-content: center;
  min-height: 2.8rem;
  padding: 0.72rem 1.05rem;
  border-radius: 999px;
  font-weight: 850;
  text-decoration: none;
  border: 1px solid rgba(14, 85, 120, 0.18);
}

.btn.primary { background: linear-gradient(135deg, #0a6688, #25bdd7); color: white; box-shadow: 0 16px 28px rgba(21, 129, 160, 0.22); }
.btn.secondary { background: white; color: #0d5876; }
.btn.ghost { background: rgba(255,255,255,0.58); color: #24465c; }

.hero-meta-v20 span {
  padding: 0.5rem 0.72rem;
  border-radius: 999px;
  background: rgba(255,255,255,0.76);
  border: 1px solid rgba(67, 136, 165, 0.16);
  color: #315368;
  font-weight: 760;
  font-size: 0.86rem;
}

.home-hero-visual-v20 {
  position: relative;
  border-radius: 34px;
  overflow: hidden;
  border: 1px solid rgba(60, 120, 154, 0.20);
  box-shadow: 0 30px 80px rgba(8, 35, 60, 0.18);
  background: #eaf5fb;
}

.home-hero-visual-v20 img {
  display: block;
  width: 100%;
  aspect-ratio: 16 / 10;
  object-fit: cover;
}

.floating-stat-v20 {
  position: absolute;
  display: grid;
  gap: 0.05rem;
  padding: 0.8rem 1rem;
  border-radius: 20px;
  background: rgba(255,255,255,0.82);
  backdrop-filter: blur(14px);
  border: 1px solid rgba(82, 142, 170, 0.20);
  box-shadow: 0 16px 35px rgba(10, 35, 55, 0.14);
}
.floating-stat-v20.top { top: 1.1rem; left: 1.1rem; }
.floating-stat-v20.bottom { right: 1.1rem; bottom: 1.1rem; }
.floating-stat-v20 strong { color: #08344f; font-size: 1.45rem; line-height: 1; }
.floating-stat-v20 span { color: #4d6679; font-weight: 700; font-size: 0.82rem; }

.affiliation-strip-v20,
.home-section-v20 {
  max-width: 1340px;
  margin: 0 auto;
  padding: 1.4rem clamp(1rem, 4vw, 3.5rem);
}

.affiliation-strip-v20 {
  display: grid;
  grid-template-columns: 1fr 1fr;
  gap: 1rem;
}

.affiliation-card-v20 {
  display: grid;
  grid-template-columns: 136px minmax(0, 1fr);
  align-items: center;
  gap: 1rem;
  padding: 1rem;
  border-radius: 26px;
  background: rgba(255,255,255,0.82);
  border: 1px solid var(--hub-border);
  box-shadow: 0 18px 45px rgba(18, 60, 90, 0.08);
}

.affiliation-card-v20 img {
  width: 100%;
  max-height: 86px;
  object-fit: contain;
  border-radius: 16px;
  background: white;
}

.affiliation-card-v20 strong { display: block; color: var(--hub-ink); font-size: 1.02rem; }
.affiliation-card-v20 span { display: block; margin-top: 0.25rem; color: #5b7080; line-height: 1.5; }

.section-heading-v20 { max-width: 900px; }
.section-heading-v20.centered { text-align: center; margin: 0 auto 1.5rem; }
.section-heading-v20 h2 { margin: 0; color: var(--hub-ink); font-size: clamp(2rem, 4vw, 4rem); line-height: 1; letter-spacing: -0.055em; }
.section-heading-v20 p:not(.eyebrow-v20) { color: #5b7080; font-size: 1.08rem; line-height: 1.75; }

.profile-grid-v20,
.entry-grid-v20 {
  display: grid;
  grid-template-columns: repeat(3, 1fr);
  gap: 1rem;
  margin-top: 1.5rem;
}

.profile-card-v20,
.entry-grid-v20 a,
.atlas-card-v20 {
  background: var(--hub-card);
  border: 1px solid var(--hub-border);
  border-radius: 28px;
  box-shadow: 0 18px 50px rgba(20, 60, 85, 0.08);
}

.profile-card-v20 { padding: 1.2rem; }
.profile-card-v20 img { width: 86px; height: 86px; object-fit: cover; border-radius: 22px; }
.profile-card-v20 h3,
.atlas-card-body-v20 h3 { color: var(--hub-ink); margin: 0.9rem 0 0.35rem; }
.profile-card-v20 p,
.atlas-card-body-v20 p { color: #5c7080; line-height: 1.65; }

.research-atlas-v20 { padding-top: 3rem; }
.atlas-grid-v20 { display: grid; grid-template-columns: 1.2fr 0.8fr; gap: 1rem; }
.atlas-card-v20 { overflow: hidden; }
.atlas-card-v20.large { grid-row: span 2; }
.atlas-card-v20 img { width: 100%; aspect-ratio: 16 / 9; object-fit: cover; display: block; }
.atlas-card-v20.large img { aspect-ratio: 16 / 10; }
.atlas-card-body-v20 { padding: 1.15rem; }
.atlas-card-body-v20 a,
.entry-grid-v20 a { color: #0b6789; font-weight: 850; text-decoration: none; }
.text-card-v20 { padding: 1.25rem; }
.text-card-v20 h3 { margin: 0 0 0.7rem; color: var(--hub-ink); }
.text-card-v20 ul { margin: 0; padding-left: 1.1rem; color: #536b7d; line-height: 1.8; }

.publication-entry-v20 { padding-bottom: 4rem; }
.entry-grid-v20 { grid-template-columns: repeat(4, 1fr); }
.entry-grid-v20 a { display: grid; gap: 0.35rem; padding: 1.1rem; }
.entry-grid-v20 strong { color: var(--hub-ink); }
.entry-grid-v20 span { color: #5b7080; line-height: 1.55; }

@media (max-width: 1050px) {
  .home-hero-grid-v20,
  .affiliation-strip-v20,
  .atlas-grid-v20,
  .profile-grid-v20,
  .entry-grid-v20 { grid-template-columns: 1fr; }
  .home-hero-bg-v20 { height: 85%; }
}

@media (max-width: 720px) {
  body > header,
  .site-header { align-items: flex-start !important; flex-direction: column !important; }
  .site-nav,
  body > header nav { justify-content: flex-start !important; }
  .home-hero-copy-v20 h1 { font-size: clamp(2.7rem, 16vw, 4rem); }
  .affiliation-card-v20 { grid-template-columns: 92px minmax(0, 1fr); }
}
/* === Homepage logo/background redesign v20 END === */
'''

JSON_LD = r'''<script type="application/ld+json" id="home-person-schema-v20">
{
  "@context": "https://schema.org",
  "@type": "Person",
  "name": "Ahmed Mansour",
  "givenName": "Ahmed",
  "familyName": "Mansour",
  "jobTitle": "Researcher in indoor positioning, geomatics, and spatial intelligence",
  "url": "https://ahmedmansoour.github.io/indoor-positioning-hub/",
  "knowsAbout": [
    "indoor positioning",
    "indoor localization",
    "Wi-Fi fingerprinting",
    "pedestrian dead reckoning",
    "mobile crowdsensing",
    "radio map generation",
    "indoor-outdoor detection",
    "GNSS/PDR integration",
    "spatial intelligence"
  ]
}
</script>'''


def replace_nav(html: str, prefix: str) -> str:
    nav = NAV_SUB if prefix == '../' else NAV_ROOT
    if re.search(r'<nav\b[^>]*>.*?</nav>', html, flags=re.I | re.S):
        return re.sub(r'<nav\b[^>]*>.*?</nav>', nav, html, count=1, flags=re.I | re.S)
    if re.search(r'</header>', html, flags=re.I):
        return re.sub(r'</header>', nav + '\n</header>', html, count=1, flags=re.I)
    return html


def update_navs():
    root_pages = [
        'index.html', 'publications.html', 'research-themes.html', 'resources.html',
        'citation-resources.html', 'about.html', 'cv.html'
    ]
    for name in root_pages:
        p = ROOT / name
        if p.exists():
            s = p.read_text(encoding='utf-8', errors='ignore')
            s2 = replace_nav(s, '')
            if s2 != s:
                p.write_text(s2, encoding='utf-8')
                print('updated nav:', p)
    pub_dir = ROOT / 'publications'
    if pub_dir.exists():
        for p in pub_dir.glob('*.html'):
            s = p.read_text(encoding='utf-8', errors='ignore')
            s2 = replace_nav(s, '../')
            if s2 != s:
                p.write_text(s2, encoding='utf-8')
                print('updated nav:', p)


def update_index():
    if not INDEX_PATH.exists():
        raise FileNotFoundError('index.html not found')
    html = INDEX_PATH.read_text(encoding='utf-8', errors='ignore')
    html = re.sub(r'<title>.*?</title>', '<title>Indoor Positioning Hub | Ahmed Mansour</title>', html, count=1, flags=re.I | re.S)
    if '<title>' not in html.lower():
        html = html.replace('</head>', '<title>Indoor Positioning Hub | Ahmed Mansour</title>\n</head>')
    meta_desc = '<meta name="description" content="Indoor Positioning Hub by Ahmed Mansour: indoor positioning, Wi-Fi fingerprinting, PDR, mobile crowdsensing, radio maps, indoor-outdoor awareness, publication pages, PDFs, and citation resources.">'
    if 'name="description"' in html:
        html = re.sub(r'<meta\s+name="description"\s+content="[^"]*"\s*/?>', meta_desc, html, count=1, flags=re.I)
    else:
        html = html.replace('</head>', meta_desc + '\n</head>')
    html = re.sub(r'<script type="application/ld\+json" id="home-person-schema-v20">.*?</script>\s*', '', html, flags=re.I | re.S)
    html = html.replace('</head>', JSON_LD + '\n</head>')
    if re.search(r'<main\b[^>]*>.*?</main>', html, flags=re.I | re.S):
        html = re.sub(r'<main\b[^>]*>.*?</main>', HOME_MAIN, html, count=1, flags=re.I | re.S)
    elif re.search(r'</header>', html, flags=re.I):
        html = re.sub(r'</header>', '</header>\n' + HOME_MAIN, html, count=1, flags=re.I)
    else:
        html = html.replace('<body>', '<body>\n' + HOME_MAIN)
    INDEX_PATH.write_text(html, encoding='utf-8')
    print('updated homepage:', INDEX_PATH)


def update_css():
    if not CSS_PATH.exists():
        raise FileNotFoundError('assets/css/style.css not found')
    css = CSS_PATH.read_text(encoding='utf-8', errors='ignore')
    css = re.sub(r'/\* === Homepage logo/background redesign v20 START === \*/.*?/\* === Homepage logo/background redesign v20 END === \*/', '', css, flags=re.S)
    css = css.rstrip() + '\n\n' + CSS_BLOCK.strip() + '\n'
    CSS_PATH.write_text(css, encoding='utf-8')
    print('updated css:', CSS_PATH)


if __name__ == '__main__':
    update_navs()
    update_index()
    update_css()
    print('Done: homepage logo/background redesign v20 applied.')
