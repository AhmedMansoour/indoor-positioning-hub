#!/usr/bin/env python3
"""Promote the CV/profile page to the main Indoor Positioning Hub homepage.

Run from the repository root:
    python scripts/make_cv_homepage.py

This script is designed to be applied after hub-resume-visual-upgrade-v1.
It keeps the public CV PDF, but removes the separate CV page from navigation and
combines Research Themes with the Visual Research Atlas on the home page.
"""
from __future__ import annotations
from pathlib import Path
from datetime import date
import html
import json
import re

ROOT = Path.cwd()

BASE_URL = "https://ahmedmansoour.github.io/indoor-positioning-hub/"


def read(path: Path) -> str:
    return path.read_text(encoding="utf-8", errors="ignore") if path.exists() else ""


def write(path: Path, text: str) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(text, encoding="utf-8", newline="\n")


def replace_header(text: str, relative: bool = False) -> str:
    prefix = "../" if relative else ""
    nav = f'''<header class="site-header">
    <nav class="nav container">
      <a class="brand" href="{prefix}index.html">Indoor Positioning Hub</a>
      <button class="nav-toggle" aria-label="Toggle navigation">☰</button>
      <div class="nav-links">
        <a href="{prefix}publications.html">Publications</a>
        <a href="{prefix}research-themes.html">Research Themes</a>
        <a href="{prefix}resources.html">Datasets & Code</a>
        <a href="{prefix}citation-resources.html">Citation Resources</a>
        <a href="{prefix}about.html">About</a>
      </div>
    </nav>
  </header>'''
    if re.search(r"<header class=\"site-header\">.*?</header>", text, flags=re.S):
        return re.sub(r"<header class=\"site-header\">.*?</header>", nav, text, flags=re.S)
    return text.replace("<body>", "<body>\n" + nav, 1)


def strip_cv_nav_and_links(text: str, relative: bool = False) -> str:
    # Remove standalone CV nav links inserted by the previous upgrade.
    text = re.sub(r"\n\s*<a href=\"(?:\.\./)?cv\.html\">CV</a>", "", text)
    # Update common buttons/links that point to the old CV page.
    prefix = "../" if relative else ""
    text = text.replace('href="cv.html">Open CV</a>', f'href="{prefix}index.html">Open Indoor Positioning Hub</a>')
    text = text.replace('href="../cv.html">Open CV</a>', 'href="../index.html">Open Indoor Positioning Hub</a>')
    text = text.replace('href="cv.html">View CV page</a>', f'href="{prefix}index.html">View Indoor Positioning Hub</a>')
    text = text.replace('href="../cv.html">View CV page</a>', 'href="../index.html">View Indoor Positioning Hub</a>')
    text = text.replace('href="cv.html">CV</a>', f'href="{prefix}index.html">Indoor Positioning Hub</a>')
    text = text.replace('href="../cv.html">CV</a>', 'href="../index.html">Indoor Positioning Hub</a>')
    return text


def visual_data() -> list[dict[str, str]]:
    json_path = ROOT / "data" / "visual_research_figures.json"
    if json_path.exists():
        try:
            return json.loads(read(json_path))
        except Exception:
            pass
    # Fallback, used only if the visual registry is missing.
    return [
        {
            "file": "smart-building-positioning-system.webp",
            "title": "Smart building positioning system",
            "caption": "A building-level view of indoor positioning as infrastructure, sensing, routing, and spatial awareness working together."
        },
        {
            "file": "context-descriptor-atlas.webp",
            "title": "Context descriptor atlas",
            "caption": "A compact map of motion state, phone pose, vertical transitions, IOD gates, and session integrity indicators."
        },
        {
            "file": "smartphone-poses-trajectories.webp",
            "title": "Pose-aware smartphone trajectories",
            "caption": "Different carrying modes produce different motion and heading behavior, so positioning must remain robust under natural phone use."
        },
        {
            "file": "radio-map-reliability-write-back.webp",
            "title": "Reliability-governed radio-map updating",
            "caption": "Crowdsensed fingerprints should be checked before they are written back into a radio map."
        },
        {
            "file": "multisensor-session-log-stream.webp",
            "title": "Multi-sensor session logs",
            "caption": "Wi-Fi, IMU, magnetometer, barometer, GNSS, and app events become a synchronized log stream for context-aware positioning."
        },
        {
            "file": "skeleton-assembly-refinement.webp",
            "title": "Crowdsensed map assembly and refinement",
            "caption": "Local movement traces and fingerprints can be assembled into larger 3D indoor map structures."
        },
        {
            "file": "scaling-ips-principles.webp",
            "title": "Scaling IPS principles",
            "caption": "Scalable IPS needs user-centered design, self-healing data pipelines, generic infrastructure, and global applicability."
        },
    ]


def combined_research_atlas_section() -> str:
    themes = [
        ("Smartphone sensing and PDR", "Understanding how motion, heading, phone pose, carrying mode, and inertial drift affect pedestrian navigation."),
        ("Wi-Fi fingerprinting and radio maps", "Turning wireless signal measurements into reusable indoor spatial knowledge while controlling drift, aging, and uncertainty."),
        ("Crowd-powered scalability", "Reducing manual surveying through ordinary user traces, passive sensing, and autonomous map generation or updating."),
        ("Indoor-outdoor and context awareness", "Recognizing transitions, gates, stairs, elevators, motion states, and session quality to support seamless positioning."),
        ("Reliability and deployment readiness", "Adding checks, gates, confidence scores, and decision layers before positioning outputs or new fingerprints are trusted."),
        ("Indoor spatial intelligence", "Moving from coordinates to usable spatial information for buildings, services, robots, digital twins, and smart environments."),
    ]
    theme_cards = []
    for title, body in themes:
        theme_cards.append(f'''<article class="combined-theme-card">
          <h3>{html.escape(title)}</h3>
          <p>{html.escape(body)}</p>
        </article>''')

    atlas_cards = []
    for item in visual_data():
        filename = html.escape(item.get("file", ""))
        title = html.escape(item.get("title", "Research visual"))
        caption = html.escape(item.get("caption", ""))
        atlas_cards.append(f'''<article class="visual-atlas-card">
          <img src="assets/img/research/{filename}" alt="{title}" loading="lazy">
          <div class="visual-atlas-caption">
            <h3>{title}</h3>
            <p>{caption}</p>
          </div>
        </article>''')

    return f'''<!-- BEGIN combined research themes atlas -->
    <section id="research-themes-and-visual-atlas" class="container combined-research-atlas-section">
      <p class="eyebrow">Research Themes and Visual Research Atlas</p>
      <h2>A thematic map of Ahmed Mansour's work across indoor positioning research, engineering, and deployment.</h2>
      <p class="section-lead">This section combines the research themes and the visual atlas in one place. The themes explain the intellectual structure of the work, while the figures show the systems view: people move through buildings, smartphones sense motion and signals, context explains transitions, radio maps evolve, and reliability gates decide what can be trusted.</p>

      <div class="combined-theme-grid">
        {''.join(theme_cards)}
      </div>

      <div class="combined-atlas-intro">
        <h3>Visual research atlas</h3>
        <p>The visual atlas makes the hub easy to scan before reading the papers. Each figure gives a quick mental model of one part of the research pipeline, from smart-building positioning and pose-aware PDR to reliability-governed radio-map updating and crowd-powered scalability.</p>
      </div>

      <div class="visual-atlas-grid">
        {''.join(atlas_cards)}
      </div>
    </section>
    <!-- END combined research themes atlas -->'''


def remove_existing_combined_block(text: str) -> str:
    text = re.sub(
        r"\s*<!-- BEGIN combined research themes atlas -->.*?<!-- END combined research themes atlas -->\s*",
        "\n",
        text,
        flags=re.S,
    )
    # Remove earlier home visual entry if present, because the homepage now fully integrates profile + atlas.
    text = re.sub(
        r"\s*<!-- BEGIN profile visual entry -->.*?<!-- END profile visual entry -->\s*",
        "\n",
        text,
        flags=re.S,
    )
    return text


def insert_combined_section(text: str) -> str:
    block = combined_research_atlas_section()
    text = remove_existing_combined_block(text)
    patterns = [
        r"<section class=\"container resume-section\">\s*<h2>Professional service and skills</h2>",
        r"<section class=\"container resume-section\">\s*<h2>Selected contribution areas</h2>",
    ]
    for pat in patterns:
        matches = list(re.finditer(pat, text, flags=re.I))
        if matches:
            # For selected contribution areas, place after that section if possible.
            if "Selected contribution" in pat:
                m = matches[0]
                end = text.find("</section>", m.end())
                if end != -1:
                    end += len("</section>")
                    return text[:end] + "\n\n" + block + "\n" + text[end:]
            else:
                m = matches[0]
                return text[:m.start()] + block + "\n\n" + text[m.start():]
    idx = text.lower().rfind("</main>")
    if idx != -1:
        return text[:idx] + "\n" + block + "\n" + text[idx:]
    return text + "\n" + block + "\n"


def make_index_from_cv() -> None:
    cv = ROOT / "cv.html"
    idx = ROOT / "index.html"
    source = read(cv) if cv.exists() else read(idx)
    if not source:
        raise SystemExit("[ERROR] Could not find cv.html or index.html.")

    text = source
    text = replace_header(text, relative=False)
    text = strip_cv_nav_and_links(text, relative=False)

    # SEO and visible naming: the page is the hub homepage, not a separate CV page.
    text = re.sub(r"<title>.*?</title>", "<title>Indoor Positioning Hub | Ahmed Mansour</title>", text, flags=re.S | re.I)
    text = re.sub(
        r'<meta name="description" content="[^"]*">',
        '<meta name="description" content="Indoor Positioning Hub by Ahmed Mansour: public academic profile, publication pages, PDFs, visual research atlas, citation resources, and research themes in indoor positioning, Wi-Fi fingerprinting, PDR, mobile crowdsensing, and indoor spatial intelligence.">',
        text,
        flags=re.I,
    )
    text = re.sub(r'<meta property="og:title" content="[^"]*">', '<meta property="og:title" content="Indoor Positioning Hub">', text, flags=re.I)
    text = re.sub(
        r'<meta property="og:description" content="[^"]*">',
        '<meta property="og:description" content="Public academic profile, research themes, visual atlas, publication pages, PDFs, and citation resources for Ahmed Mansour\'s work on indoor positioning and indoor spatial intelligence.">',
        text,
        flags=re.I,
    )
    text = text.replace('"url": "https://ahmedmansoour.github.io/indoor-positioning-hub/cv.html"', '"url": "https://ahmedmansoour.github.io/indoor-positioning-hub/"')
    text = text.replace('Public academic profile', 'Indoor Positioning Hub')
    text = text.replace('href="research-themes.html#visual-research-atlas">Visual research atlas</a>', 'href="#research-themes-and-visual-atlas">Research themes and visual atlas</a>')
    text = text.replace('href="publications.html">View publications</a>', 'href="publications.html">View publications</a>')
    text = text.replace('Ahmed Mansour CV | Indoor Positioning Hub', 'Indoor Positioning Hub | Ahmed Mansour')
    text = text.replace('Public academic CV of Ahmed Mansour:', 'Indoor Positioning Hub by Ahmed Mansour:')
    text = text.replace('Academic profile, CV, research expertise, publications, education, and service activity of Ahmed Mansour.', 'Academic profile, publication hub, research themes, visual atlas, and citation resources for Ahmed Mansour.')

    text = insert_combined_section(text)
    write(idx, text)


def make_cv_redirect() -> None:
    redirect = '''<!doctype html>
<html lang="en">
<head>
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width, initial-scale=1">
  <title>Indoor Positioning Hub | Ahmed Mansour</title>
  <meta name="robots" content="noindex,follow">
  <link rel="canonical" href="https://ahmedmansoour.github.io/indoor-positioning-hub/">
  <meta http-equiv="refresh" content="0; url=index.html">
  <link rel="stylesheet" href="assets/css/style.css">
</head>
<body>
  <main class="container" style="padding:3rem 0;">
    <h1>Indoor Positioning Hub</h1>
    <p>The main profile and CV content has moved to the homepage.</p>
    <p><a class="button primary" href="index.html">Open Indoor Positioning Hub</a></p>
  </main>
</body>
</html>
'''
    write(ROOT / "cv.html", redirect)


def update_research_themes_page() -> None:
    p = ROOT / "research-themes.html"
    if not p.exists():
        return
    t = read(p)
    t = replace_header(t, relative=False)
    t = strip_cv_nav_and_links(t, relative=False)
    t = t.replace('<p class="eyebrow">Visual research atlas</p>', '<p class="eyebrow">Research Themes and Visual Research Atlas</p>')
    t = t.replace('<h2>Indoor positioning research, shown as a system</h2>', '<h2>A thematic map of Ahmed Mansour\'s work across indoor positioning research, engineering, and deployment.</h2>')
    t = re.sub(
        r'<p class="section-lead">These figures make the hub easier to scan\..*?</p>',
        '<p class="section-lead">This page keeps the thematic map and visual atlas together. The themes explain the main research directions, while the figures show how indoor positioning becomes a system: smartphones sense movement and signals, context explains transitions, radio maps evolve, and reliability checks support deployment-ready decisions.</p>',
        t,
        flags=re.S,
    )
    write(p, t)


def update_all_headers_and_links() -> None:
    for p in ROOT.glob("*.html"):
        if p.name in {"index.html", "cv.html", "research-themes.html"}:
            continue
        t = read(p)
        t = replace_header(t, relative=False)
        t = strip_cv_nav_and_links(t, relative=False)
        write(p, t)
    pub_dir = ROOT / "publications"
    if pub_dir.exists():
        for p in pub_dir.glob("*.html"):
            t = read(p)
            t = replace_header(t, relative=True)
            t = strip_cv_nav_and_links(t, relative=True)
            write(p, t)


def update_about_teaser() -> None:
    p = ROOT / "about.html"
    if not p.exists():
        return
    t = read(p)
    t = t.replace('View CV page', 'View Indoor Positioning Hub')
    t = t.replace('href="cv.html"', 'href="index.html"')
    t = t.replace('href="../cv.html"', 'href="../index.html"')
    write(p, t)


def update_sitemap() -> None:
    p = ROOT / "sitemap.xml"
    if not p.exists():
        return
    t = read(p)
    today = date.today().isoformat()
    # Remove cv.html from sitemap because it is now only a compatibility redirect.
    t = re.sub(r"\s*<url>\s*<loc>https://ahmedmansoour\.github\.io/indoor-positioning-hub/cv\.html</loc>.*?</url>", "", t, flags=re.S)
    # Make sure root URL has a fresh lastmod where possible.
    root_loc = BASE_URL.rstrip('/') + '/'
    if root_loc in t:
        t = re.sub(
            r"(<loc>https://ahmedmansoour\.github\.io/indoor-positioning-hub/</loc>\s*<lastmod>)[^<]+(</lastmod>)",
            rf"\g<1>{today}\g<2>",
            t,
            flags=re.S,
        )
    write(p, t)


def update_llms() -> None:
    p = ROOT / "llms.txt"
    if not p.exists():
        return
    t = read(p)
    start = "<!-- BEGIN MAIN_HUB_PROFILE_ATLAS -->"
    end = "<!-- END MAIN_HUB_PROFILE_ATLAS -->"
    block = """## Indoor Positioning Hub homepage
- Main profile and CV page: /
- Public CV PDF: /assets/cv/ahmed-mansour-public-cv.pdf
- Combined research themes and visual atlas: /#research-themes-and-visual-atlas
- Research themes page: /research-themes.html
- Publication pages: /publications.html

The homepage is the main academic profile and Indoor Positioning Hub for Ahmed Mansour. It combines CV-style academic information, selected expertise, publication navigation, a public CV PDF, research themes, and a visual research atlas. Funds and detailed research-project sections are intentionally not included at this stage."""
    repl = start + "\n" + block + "\n" + end
    t = re.sub(r"\n?<!-- BEGIN CV_VISUAL_UPGRADE -->.*?<!-- END CV_VISUAL_UPGRADE -->\n?", "\n", t, flags=re.S)
    if re.search(re.escape(start) + r".*?" + re.escape(end), t, flags=re.S):
        t = re.sub(re.escape(start) + r".*?" + re.escape(end), repl, t, flags=re.S)
    else:
        t = t.rstrip() + "\n\n" + repl + "\n"
    write(p, t)


def update_css() -> None:
    p = ROOT / "assets" / "css" / "style.css"
    css = read(p)
    block = r'''
/* ============================================================
   Main hub homepage with combined research themes and visual atlas
   Added by scripts/make_cv_homepage.py
   ============================================================ */
.combined-research-atlas-section {
  padding-top: 2.4rem;
  padding-bottom: 2.6rem;
}
.combined-theme-grid {
  display: grid;
  grid-template-columns: repeat(3, minmax(0, 1fr));
  gap: 1rem;
  margin-top: 1.25rem;
  margin-bottom: 1.5rem;
}
.combined-theme-card {
  background: var(--card, #fff);
  border: 1px solid var(--border, #dfe7ea);
  border-radius: 18px;
  padding: 1rem 1.05rem;
  box-shadow: 0 12px 28px rgba(13, 45, 55, 0.07);
}
.combined-theme-card h3 {
  margin: 0 0 0.45rem;
  font-size: 1.02rem;
}
.combined-theme-card p {
  margin: 0;
  color: var(--muted-foreground, #56646b);
  line-height: 1.6;
}
.combined-atlas-intro {
  margin: 1.4rem 0 0.3rem;
  padding: 1.05rem 1.15rem;
  border-radius: 18px;
  background: linear-gradient(135deg, rgba(13,111,126,0.09), rgba(70,153,170,0.05));
  border: 1px solid rgba(13,111,126,0.13);
}
.combined-atlas-intro h3 {
  margin: 0 0 0.35rem;
}
.combined-atlas-intro p {
  margin: 0;
  color: var(--muted-foreground, #56646b);
  line-height: 1.65;
}
@media (max-width: 950px) {
  .combined-theme-grid { grid-template-columns: repeat(2, minmax(0, 1fr)); }
}
@media (max-width: 650px) {
  .combined-theme-grid { grid-template-columns: 1fr; }
}
'''
    if "Main hub homepage with combined research themes and visual atlas" not in css:
        css = css.rstrip() + "\n\n" + block.strip() + "\n"
        write(p, css)


def main() -> None:
    make_index_from_cv()
    make_cv_redirect()
    update_research_themes_page()
    update_all_headers_and_links()
    update_about_teaser()
    update_sitemap()
    update_llms()
    update_css()
    print("[OK] index.html is now the main Indoor Positioning Hub profile/CV homepage.")
    print("[OK] The separate cv.html page is now only a compatibility redirect to index.html.")
    print("[OK] Research Themes and Visual Research Atlas are combined on the homepage.")
    print("[OK] Navigation no longer shows a separate CV item.")
    print("[NEXT] Review locally, then run:")
    print("      git add index.html cv.html about.html research-themes.html publications *.html sitemap.xml llms.txt assets/css/style.css scripts/make_cv_homepage.py")
    print('      git commit -m "Make Indoor Positioning Hub the main profile homepage"')
    print("      git push origin main")


if __name__ == "__main__":
    main()
