from __future__ import annotations

import json
import re
from html import escape
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
PUBLICATIONS_JSON = ROOT / "data" / "publications.json"
DISPLAY_JSON = ROOT / "data" / "publication_display_metadata.json"
OUT_HTML = ROOT / "publications.html"
CSS_PATH = ROOT / "assets" / "css" / "style.css"

SITE_TITLE = "Indoor Positioning Hub"
USER_NAME = "Ahmed Mansour"

THEME_SYMBOLS = {
    "Autonomous radio mapping": ["📡", "🗺️", "🧭", "✅"],
    "Scalable IPS and crowdsensing": ["🏢", "📱", "👥", "♻️"],
    "PDR and smartphone sensing": ["🚶", "📱", "🧭", "〰️"],
    "Urban and seamless positioning": ["🛰️", "🚶", "🏙️", "🧭"],
    "IOD and seamless navigation": ["🚪", "🌐", "📱", "🔁"],
    "Cooperative positioning": ["👥", "📍", "🤝", "📶"],
    "AI-guided crowd-powered IPS": ["🧠", "💬", "🗺️", "📡"],
    "Deployment and spatial safety": ["🏗️", "🛡️", "📡", "📊"],
    "Wi-Fi fingerprinting and heading reliability": ["📶", "🧭", "🧲", "✅"],
    "Research foundation": ["🎓", "📚", "📡", "🧭"],
}

THEME_TONES = {
    "Autonomous radio mapping": "radio maps, crowdsensed fingerprints, uncertainty checks, and safe map updating",
    "Scalable IPS and crowdsensing": "user behavior, mobile crowdsensing, deployment cost, and the practical scaling of IPS",
    "PDR and smartphone sensing": "smartphone motion, pose changes, heading drift, and robust pedestrian tracking",
    "Urban and seamless positioning": "GNSS, PDR, BLE, map constraints, and continuous pedestrian navigation",
    "IOD and seamless navigation": "indoor–outdoor awareness, transition detection, and positioning-mode switching",
    "Cooperative positioning": "multi-user collaboration, temporary anchors, and relative constraints",
    "AI-guided crowd-powered IPS": "semantic prompting, spatial feedback, knowledge graphs, and AI-guided user engagement",
    "Deployment and spatial safety": "passive localization, BIM, uncertainty-aware safety decisions, and spatial risk mapping",
    "Wi-Fi fingerprinting and heading reliability": "Wi-Fi fingerprints, magnetic stability, heading calibration, and scan-level reliability",
    "Research foundation": "multi-sensor fusion, crowdsourcing, PDR, Wi-Fi fingerprinting, and collaborative localization",
}

CSS_BLOCK = r"""

/* === Publications visual-card redesign v5 === */
.publications-showcase {
  display: grid;
  gap: 1.45rem;
  margin-top: 1.3rem;
}
.pub-visual-card {
  position: relative;
  display: grid;
  grid-template-columns: minmax(0, 1.38fr) minmax(260px, 0.82fr);
  gap: 1.1rem;
  align-items: stretch;
  padding: 1.15rem;
  border-radius: 26px;
  border: 1px solid rgba(78, 112, 146, 0.18);
  background:
    radial-gradient(circle at 98% 0%, rgba(34, 134, 176, 0.11), transparent 32%),
    linear-gradient(135deg, rgba(255,255,255,0.98), rgba(246,250,254,0.96));
  box-shadow: 0 18px 50px rgba(18, 52, 76, 0.09);
  overflow: hidden;
}
.pub-visual-card::before {
  content: "";
  position: absolute;
  inset: 0 auto 0 0;
  width: 7px;
  background: linear-gradient(180deg, #0097a7, #4f7ef7, #8a63d2);
  opacity: 0.78;
}
.pub-card-main {
  padding: 0.15rem 0.3rem 0.1rem 0.35rem;
  min-width: 0;
}
.pub-card-topline {
  display: flex;
  flex-wrap: wrap;
  gap: 0.45rem;
  align-items: center;
  margin-bottom: 0.55rem;
}
.pub-year-type {
  color: #5d6b7a;
  font-size: 0.93rem;
  font-weight: 700;
  letter-spacing: 0.01em;
}
.pub-theme-pill {
  display: inline-flex;
  align-items: center;
  gap: 0.3rem;
  padding: 0.22rem 0.62rem;
  border-radius: 999px;
  color: #075d74;
  background: rgba(0, 151, 167, 0.10);
  border: 1px solid rgba(0, 151, 167, 0.18);
  font-size: 0.82rem;
  font-weight: 700;
}
.pub-card-title {
  margin: 0.15rem 0 0.72rem;
  font-size: clamp(1.05rem, 1.3vw, 1.42rem);
  line-height: 1.38;
  letter-spacing: -0.015em;
}
.pub-card-title a {
  color: #063b63;
  text-decoration: none;
}
.pub-card-title a:hover {
  color: #007f9a;
  text-decoration: underline;
  text-decoration-thickness: 0.09em;
  text-underline-offset: 0.16em;
}
.pub-authors {
  margin: 0.35rem 0 0.65rem;
  color: #29394a;
  font-size: 0.97rem;
  line-height: 1.65;
}
.author-highlight {
  display: inline-block;
  padding: 0.02rem 0.22rem;
  border-radius: 0.42rem;
  color: #061b2b;
  background: linear-gradient(180deg, rgba(255, 239, 153, 0.78), rgba(255, 224, 100, 0.58));
  font-weight: 900;
}
.pub-venue-strip {
  display: flex;
  flex-wrap: wrap;
  gap: 0.48rem;
  margin: 0.7rem 0 0.8rem;
}
.pub-badge {
  display: inline-flex;
  align-items: center;
  gap: 0.28rem;
  min-height: 30px;
  padding: 0.25rem 0.62rem;
  border-radius: 999px;
  font-size: 0.82rem;
  font-weight: 800;
  border: 1px solid rgba(41, 86, 120, 0.14);
  background: rgba(255,255,255,0.78);
  color: #22445e;
  box-shadow: 0 8px 24px rgba(44, 72, 95, 0.05);
}
.pub-badge.journal {
  background: #ecf8ff;
  color: #0a4d72;
}
.pub-badge.if {
  background: #f1f7ed;
  color: #355f10;
}
.pub-badge.rank {
  background: #fff6d8;
  color: #765306;
}
.pub-badge.tier {
  background: #f2eaff;
  color: #55318d;
}
.pub-badge.doi {
  background: #eef3ff;
  color: #254d8b;
}
.pub-badge.doi a {
  color: inherit;
  text-decoration: none;
}
.pub-badge.doi a:hover {
  text-decoration: underline;
}
.pub-insight-box {
  display: grid;
  grid-template-columns: auto 1fr;
  gap: 0.75rem;
  align-items: start;
  margin: 0.75rem 0 0.9rem;
  padding: 0.75rem 0.82rem;
  border-radius: 18px;
  background: linear-gradient(135deg, rgba(236, 248, 255, 0.80), rgba(247, 244, 255, 0.82));
  border: 1px solid rgba(88, 129, 164, 0.15);
}
.pub-symbols {
  display: flex;
  flex-wrap: wrap;
  width: 5.4rem;
  gap: 0.3rem;
}
.pub-symbol {
  display: inline-grid;
  place-items: center;
  width: 2.24rem;
  height: 2.24rem;
  border-radius: 13px;
  background: rgba(255,255,255,0.82);
  box-shadow: inset 0 0 0 1px rgba(46, 86, 118, 0.10), 0 7px 16px rgba(25, 60, 90, 0.06);
  font-size: 1.08rem;
}
.pub-paper-lens {
  margin: 0;
  color: #66717e;
  font-size: 0.94rem;
  line-height: 1.68;
  font-style: italic;
}
.pub-keywords {
  display: flex;
  flex-wrap: wrap;
  gap: 0.38rem;
  margin: 0.7rem 0 0.9rem;
}
.pub-keyword {
  display: inline-block;
  padding: 0.18rem 0.54rem;
  border-radius: 999px;
  background: rgba(8, 65, 100, 0.06);
  color: #395064;
  font-size: 0.78rem;
  font-weight: 700;
}
.pub-actions {
  display: flex;
  flex-wrap: wrap;
  gap: 0.55rem;
  margin-top: 0.6rem;
}
.pub-action {
  display: inline-flex;
  align-items: center;
  gap: 0.34rem;
  padding: 0.52rem 0.78rem;
  border-radius: 12px;
  color: #073a5b;
  background: rgba(255,255,255,0.72);
  border: 1px solid rgba(30, 84, 125, 0.16);
  text-decoration: none;
  font-size: 0.88rem;
  font-weight: 850;
}
.pub-action:hover {
  background: #fff;
  transform: translateY(-1px);
  box-shadow: 0 10px 22px rgba(20, 65, 98, 0.09);
}
.pub-visual-panel {
  display: flex;
  flex-direction: column;
  justify-content: center;
  gap: 0.65rem;
  min-width: 0;
  border-radius: 24px;
  background:
    linear-gradient(180deg, rgba(255,255,255,0.84), rgba(233,243,250,0.72));
  border: 1px solid rgba(57, 105, 137, 0.13);
  padding: 0.7rem;
  box-shadow: inset 0 0 0 1px rgba(255,255,255,0.55);
}
.pub-visual-frame {
  position: relative;
  min-height: 220px;
  display: grid;
  place-items: center;
  border-radius: 20px;
  overflow: hidden;
  background: #f6fbff;
}
.pub-visual-frame img {
  width: 100%;
  height: 100%;
  max-height: none;
  object-fit: cover;
  display: block;
}
.pub-visual-caption {
  margin: 0;
  color: #657486;
  font-size: 0.82rem;
  line-height: 1.45;
  text-align: center;
  font-style: italic;
}
.publications-note-card {
  border-radius: 24px;
  padding: 1rem 1.1rem;
  background: linear-gradient(135deg, rgba(232,246,250,0.95), rgba(247,244,255,0.92));
  border: 1px solid rgba(48, 103, 139, 0.14);
  color: #405166;
}
.publications-note-card strong {
  color: #173b57;
}
@media (max-width: 920px) {
  .pub-visual-card {
    grid-template-columns: 1fr;
  }
  .pub-visual-panel {
    order: -1;
  }
  .pub-visual-frame {
    min-height: 180px;
  }
}
@media (max-width: 560px) {
  .pub-insight-box {
    grid-template-columns: 1fr;
  }
  .pub-symbols {
    width: auto;
  }
  .pub-visual-card {
    padding: 0.9rem;
    border-radius: 20px;
  }
}
"""


def load_json(path: Path):
    return json.loads(path.read_text(encoding="utf-8"))


def h(text: str) -> str:
    return escape(text or "", quote=True)


def rel(path: str) -> str:
    return path.replace("\\", "/")


def choose_visual(slug: str, display: dict) -> str:
    prefs = display.get("visual_preferences", {}).get(slug, [])
    for candidate in prefs:
        if (ROOT / candidate).exists():
            return candidate
    folder = ROOT / "assets" / "figures" / slug
    if folder.exists():
        preferred_words = ("concept", "atlas", "write", "skeleton", "poses", "trajectory", "scaling", "deployment", "fig_01", "fig_02")
        figures = sorted(folder.glob("*.webp")) + sorted(folder.glob("*.png")) + sorted(folder.glob("*.jpg"))
        figures = sorted(figures, key=lambda p: (0 if any(w in p.name.lower() for w in preferred_words) else 1, p.name))
        if figures:
            return rel(str(figures[0].relative_to(ROOT)))
    preview = ROOT / "assets" / "previews" / f"{slug}.png"
    if preview.exists():
        return rel(str(preview.relative_to(ROOT)))
    return "assets/img/research/smart-building-positioning-system.webp"


def venue_metrics(pub: dict, display: dict) -> dict:
    venue = pub.get("venue", "")
    metrics = display.get("venue_metrics", {})
    if venue in metrics:
        return metrics[venue]
    # Soft matching for venue strings that contain extra wording.
    for key, val in metrics.items():
        if key.lower() in venue.lower() or venue.lower() in key.lower():
            return val
    return {"impact_factor": "n/a", "quartile": pub.get("type", "publication"), "tier": "peer-reviewed output", "metric_note": "edit metadata if needed"}


def author_html(authors: list[str]) -> str:
    out = []
    for a in authors:
        if a.strip().lower() == USER_NAME.lower():
            out.append(f'<strong class="author-highlight">{h(a)}</strong>')
        else:
            out.append(h(a))
    return ", ".join(out)


def doi_badge(doi: str) -> str:
    if not doi:
        return '<span class="pub-badge doi">🔗 DOI: n/a</span>'
    doi_text = h(doi)
    return f'<span class="pub-badge doi">🔗 DOI: <a href="https://doi.org/{doi_text}">{doi_text}</a></span>'


def paper_lens(pub: dict) -> str:
    theme = pub.get("theme", "")
    tone = THEME_TONES.get(theme, "positioning data, sensing context, algorithms, and deployment value")
    summary = pub.get("summary", "")
    return f"This paper sits at the intersection of {tone}. {summary}"


def symbols(pub: dict) -> list[str]:
    theme = pub.get("theme", "")
    base = THEME_SYMBOLS.get(theme, ["📍", "📡", "🧭", "✅"])
    return base[:4]


def keyword_chips(pub: dict, limit: int = 7) -> str:
    kws = pub.get("keywords", [])[:limit]
    return "".join(f'<span class="pub-keyword">{h(k)}</span>' for k in kws)


def card(pub: dict, display: dict) -> str:
    slug = pub["slug"]
    title = pub.get("title", "Untitled")
    year = pub.get("year", "")
    typ = pub.get("type", "")
    venue = pub.get("venue", "")
    theme = pub.get("theme", "")
    doi = pub.get("doi", "")
    m = venue_metrics(pub, display)
    image = choose_visual(slug, display)
    image_alt = f"Visual summary for {title}"
    pub_page = f"publications/{slug}.html"
    pdf = f"paper-pdfs/{slug}.pdf"
    sym_html = "".join(f'<span class="pub-symbol" aria-hidden="true">{s}</span>' for s in symbols(pub))
    # For thesis/proceedings, show relevant labels without pretending they are journals.
    venue_label = "Journal" if "journal" in typ.lower() or m.get("impact_factor") not in ("n/a", "", None) else "Venue"
    if "thesis" in typ.lower():
        venue_label = "Thesis"
    return f"""
<article class="pub-visual-card" id="{h(slug)}">
  <div class="pub-card-main">
    <div class="pub-card-topline">
      <span class="pub-year-type">{h(year)} · {h(typ)}</span>
      <span class="pub-theme-pill">{h(theme)}</span>
    </div>
    <h2 class="pub-card-title"><a href="{h(pub_page)}">{h(title)}</a></h2>
    <p class="pub-authors">{author_html(pub.get('authors', []))}.</p>
    <div class="pub-venue-strip">
      <span class="pub-badge journal">🏛️ {venue_label}: <strong>{h(venue)}</strong></span>
      <span class="pub-badge if">📈 IF: <strong>{h(m.get('impact_factor','n/a'))}</strong></span>
      <span class="pub-badge rank">⭐ <strong>{h(m.get('quartile',''))}</strong></span>
      <span class="pub-badge tier">🏅 {h(m.get('tier',''))}</span>
      {doi_badge(doi)}
    </div>
    <div class="pub-insight-box">
      <div class="pub-symbols">{sym_html}</div>
      <p class="pub-paper-lens">{h(paper_lens(pub))}</p>
    </div>
    <div class="pub-keywords">{keyword_chips(pub)}</div>
    <div class="pub-actions">
      <a class="pub-action" href="{h(pub_page)}">📄 Publication page</a>
      <a class="pub-action" href="{h(pdf)}">⬇️ PDF</a>
      {f'<a class="pub-action" href="https://doi.org/{h(doi)}">🔗 DOI</a>' if doi else ''}
    </div>
  </div>
  <aside class="pub-visual-panel" aria-label="Publication visual preview">
    <div class="pub-visual-frame"><img src="{h(image)}" alt="{h(image_alt)}" loading="lazy"></div>
  </aside>
</article>"""


def build_html(pubs: list[dict], display: dict) -> str:
    pubs = sorted(pubs, key=lambda p: (int(p.get("year", "0") or 0), p.get("title", "")), reverse=True)
    cards = "\n".join(card(pub, display) for pub in pubs)
    total = len(pubs)
    return f"""<!doctype html>
<html lang="en">
<head>
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width, initial-scale=1">
  <title>Publications | {SITE_TITLE} | Ahmed Mansour</title>
  <meta name="description" content="Visual, citation-ready publication list for Ahmed Mansour's work on indoor positioning, Wi-Fi fingerprinting, crowdsensing, radio maps, PDR, IOD, GNSS/PDR integration, and spatial intelligence.">
  <link rel="stylesheet" href="assets/css/style.css">
</head>
<body>
<header class="site-header">
  <a class="brand" href="index.html">Indoor Positioning Hub</a>
  <button class="nav-toggle" aria-label="Toggle navigation">☰</button>
  <nav class="site-nav">
    <a href="publications.html">Publications</a>
    <a href="research-themes.html">Research Themes</a>
    <a href="resources.html">Datasets & Code</a>
    <a href="citation-resources.html">Citation Resources</a>
    <a href="about.html">About</a>
  </nav>
</header>

<main class="container">
  <section class="hero compact">
    <p class="eyebrow">Publication portfolio</p>
    <h1>Publications</h1>
    <p class="lead">A visual, citation-ready map of Ahmed Mansour's research across indoor positioning, Wi-Fi fingerprinting, mobile crowdsensing, autonomous radio mapping, PDR, indoor–outdoor awareness, GNSS/PDR integration, and deployment-oriented spatial intelligence.</p>
    <p class="hero-note">Each card combines a paper visual, full title, highlighted author position, venue and DOI metadata, ranking badges, keyword cues, and a short italic reading lens to help researchers quickly decide when to cite the work.</p>
  </section>

  <section class="publications-note-card">
    <strong>{total} research outputs are shown.</strong> Journal metrics are display metadata and can be updated in <code>data/publication_display_metadata.json</code> whenever impact factors, quartiles, or local ranking labels change.
  </section>

  <section class="publications-showcase" aria-label="Visual publication cards">
{cards}
  </section>
</main>

<footer class="site-footer">
  <p>© Ahmed Mansour. Indoor Positioning Research, Engineering, and Deployment Hub.</p>
</footer>
<script src="assets/js/main.js"></script>
</body>
</html>
"""


def append_css_once():
    CSS_PATH.parent.mkdir(parents=True, exist_ok=True)
    old = CSS_PATH.read_text(encoding="utf-8", errors="ignore") if CSS_PATH.exists() else ""
    marker = "/* === Publications visual-card redesign v5 === */"
    if marker in old:
        old = re.sub(r"\n/\* === Publications visual-card redesign v5 === \*/.*$", "", old, flags=re.S)
    CSS_PATH.write_text(old.rstrip() + "\n" + CSS_BLOCK.strip() + "\n", encoding="utf-8")


def main():
    if not PUBLICATIONS_JSON.exists():
        raise SystemExit(f"Missing {PUBLICATIONS_JSON}. Run from the repository after keeping data/publications.json in place.")
    if not DISPLAY_JSON.exists():
        raise SystemExit(f"Missing {DISPLAY_JSON}. Copy data/publication_display_metadata.json first.")
    pubs = load_json(PUBLICATIONS_JSON)
    display = load_json(DISPLAY_JSON)
    html = build_html(pubs, display)
    if OUT_HTML.exists():
        backup = OUT_HTML.with_suffix(".visual-v5-backup.html")
        backup.write_text(OUT_HTML.read_text(encoding="utf-8", errors="ignore"), encoding="utf-8")
        print(f"[OK] Backup written: {backup}")
    OUT_HTML.write_text(html, encoding="utf-8")
    append_css_once()
    print(f"[OK] Redesigned {OUT_HTML.name} with {len(pubs)} visual publication cards.")
    print("[OK] CSS updated in assets/css/style.css")
    print("[CHECK] Open publications.html locally or push and use ?v=visual-publications-v5")


if __name__ == "__main__":
    main()
