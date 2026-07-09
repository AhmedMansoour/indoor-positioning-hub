from pathlib import Path
import re

ROOT = Path(".")
PAGE = ROOT / "citation-resources.html"
CSS = ROOT / "assets/css/style.css"
ICON_DIR = ROOT / "assets/icons"

if not PAGE.exists():
    raise SystemExit("citation-resources.html not found. Run from repository root.")
if not CSS.exists():
    raise SystemExit("assets/css/style.css not found. Run from repository root.")

ICON_DIR.mkdir(parents=True, exist_ok=True)

icons = {
    "orcid.svg": {"bg":"#A6CE39","fg":"#ffffff","label":"iD","title":"ORCID"},
    "scopus.svg": {"bg":"#F36C21","fg":"#ffffff","label":"S","title":"Scopus"},
    "wos.svg": {"bg":"#5A67D8","fg":"#ffffff","label":"WoS","title":"Web of Science"},
    "google-scholar.svg": {"bg":"#4285F4","fg":"#ffffff","label":"GS","title":"Google Scholar"},
    "researchgate.svg": {"bg":"#00CCBB","fg":"#073d63","label":"RG","title":"ResearchGate"},
    "linkedin.svg": {"bg":"#0A66C2","fg":"#ffffff","label":"in","title":"LinkedIn"},
}

svg_template = """<svg xmlns="http://www.w3.org/2000/svg" width="96" height="96" viewBox="0 0 96 96" role="img" aria-label="{title}">
  <defs>
    <linearGradient id="g" x1="0" y1="0" x2="1" y2="1">
      <stop offset="0%" stop-color="{bg}" stop-opacity="1"/>
      <stop offset="100%" stop-color="{bg}" stop-opacity="0.88"/>
    </linearGradient>
  </defs>
  <rect x="4" y="4" width="88" height="88" rx="22" fill="url(#g)"/>
  <circle cx="48" cy="48" r="38" fill="rgba(255,255,255,0.15)"/>
  <text x="48" y="56" text-anchor="middle" font-family="Arial, Helvetica, sans-serif" font-size="{fs}" font-weight="700" fill="{fg}">{label}</text>
</svg>
"""
for name, meta in icons.items():
    fs = "28" if len(meta["label"]) <= 2 else "22"
    (ICON_DIR / name).write_text(svg_template.format(fs=fs, **meta), encoding="utf-8")

html = PAGE.read_text(encoding="utf-8", errors="ignore")

pattern = re.compile(r'(<section class="cit48-grid cit48-identifiers">)(.*?)(</section>)', flags=re.S)
if not pattern.search(html):
    raise SystemExit("Could not find identifier grid section in citation-resources.html")

new_section = """
<section class="cit48-grid cit48-identifiers">
  <article class="cit48-id-card">
    <div class="cit48-id-top"><img src="assets/icons/orcid.svg" alt="ORCID icon" class="cit48-id-icon"><strong>ORCID</strong></div>
    <a href="https://orcid.org/0000-0002-9840-7030">0000-0002-9840-7030</a>
  </article>
  <article class="cit48-id-card">
    <div class="cit48-id-top"><img src="assets/icons/scopus.svg" alt="Scopus icon" class="cit48-id-icon"><strong>Scopus Author ID</strong></div>
    <a href="https://www.scopus.com/authid/detail.uri?authorId=57948539100">57948539100</a>
  </article>
  <article class="cit48-id-card">
    <div class="cit48-id-top"><img src="assets/icons/wos.svg" alt="Web of Science icon" class="cit48-id-icon"><strong>Web of Science ResearcherID</strong></div>
    <a href="https://www.webofscience.com/wos/author/record/ABP-9962-2022">ABP-9962-2022</a>
  </article>
  <article class="cit48-id-card">
    <div class="cit48-id-top"><img src="assets/icons/google-scholar.svg" alt="Google Scholar icon" class="cit48-id-icon"><strong>Google Scholar</strong></div>
    <a href="https://scholar.google.com/citations?user=lFhcyh4AAAAJ&hl=en">Ahmed Mansour profile</a>
  </article>
  <article class="cit48-id-card">
    <div class="cit48-id-top"><img src="assets/icons/researchgate.svg" alt="ResearchGate icon" class="cit48-id-icon"><strong>ResearchGate</strong></div>
    <a href="https://www.researchgate.net/profile/Ahmed-Mansour-55">Ahmed Mansour profile</a>
  </article>
  <article class="cit48-id-card">
    <div class="cit48-id-top"><img src="assets/icons/linkedin.svg" alt="LinkedIn icon" class="cit48-id-icon"><strong>LinkedIn</strong></div>
    <a href="https://www.linkedin.com/in/ahmd-mansour/">Ahmed Mansour profile</a>
  </article>
</section>
"""
html = pattern.sub(new_section, html, count=1)
PAGE.write_text(html, encoding="utf-8")

css = CSS.read_text(encoding="utf-8", errors="ignore")
css = re.sub(r"/\* === Citation identifier icons v49 START === \*/.*?/\* === Citation identifier icons v49 END === \*/", "", css, flags=re.S)
css_block = """
/* === Citation identifier icons v49 START === */
.cit48-id-card{position:relative;overflow:hidden}
.cit48-id-top{display:flex;align-items:center;gap:14px;margin-bottom:.25rem}
.cit48-id-icon{width:48px;height:48px;flex:0 0 48px;border-radius:14px;box-shadow:0 8px 18px rgba(20,45,74,.10)}
.cit48-identifiers article strong{margin-bottom:0;font-size:1rem;line-height:1.25}
.cit48-identifiers article a{margin-left:62px}
@media(max-width:640px){
  .cit48-identifiers article a{margin-left:0}
}
/* === Citation identifier icons v49 END === */
"""
CSS.write_text(css.rstrip() + "\n\n" + css_block.strip() + "\n", encoding="utf-8")

print("Done: added local SVG identifier icons and visualized them on citation-resources.html.")
