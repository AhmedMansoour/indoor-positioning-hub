from __future__ import annotations

import re
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
PUB_HTML = ROOT / "publications.html"
CSS_PATH = ROOT / "assets" / "css" / "style.css"
REDESIGN_SCRIPT = ROOT / "scripts" / "redesign_publications_page.py"

CSS_MARKER = "/* === Publications layout polish v6 === */"
CSS_BLOCK = r'''
/* === Publications layout polish v6 === */
/* Header and page-level polish for the visual publications portfolio. */
:root {
  --hub-ink: #0b1b2e;
  --hub-muted: #5d6b7a;
  --hub-blue: #045f8c;
  --hub-cyan: #007d8d;
  --hub-line: rgba(35, 75, 110, 0.13);
  --hub-soft: #f6f9fc;
}

html { scroll-behavior: smooth; }
body {
  margin: 0;
  background: linear-gradient(180deg, #f7fafc 0%, #ffffff 42%, #f8fbfd 100%);
  color: var(--hub-ink);
}

.site-header {
  position: sticky;
  top: 0;
  z-index: 50;
  display: flex;
  align-items: center;
  justify-content: space-between;
  gap: 1.25rem;
  min-height: 68px;
  padding: 0.55rem clamp(1.1rem, 4vw, 3.3rem);
  border-bottom: 1px solid rgba(16, 44, 70, 0.12);
  background: rgba(255, 255, 255, 0.92);
  backdrop-filter: blur(16px);
  box-shadow: 0 10px 28px rgba(9, 39, 64, 0.06);
}

.site-header .brand,
.brand {
  display: inline-flex;
  align-items: center;
  gap: 0.5rem;
  color: #0b2136;
  text-decoration: none;
  font-size: clamp(1.02rem, 1.2vw, 1.18rem);
  font-weight: 950;
  letter-spacing: -0.02em;
  white-space: nowrap;
}
.site-header .brand::before,
.brand::before {
  content: "";
  width: 0.72rem;
  height: 0.72rem;
  border-radius: 999px;
  background: linear-gradient(135deg, #00a0aa, #4f7ef7);
  box-shadow: 0 0 0 5px rgba(0, 160, 170, 0.10);
}

.site-nav {
  display: flex;
  align-items: center;
  justify-content: flex-end;
  flex-wrap: wrap;
  gap: clamp(0.25rem, 1vw, 0.75rem);
}
.site-nav a {
  display: inline-flex;
  align-items: center;
  min-height: 36px;
  padding: 0.35rem 0.62rem;
  border-radius: 999px;
  color: #17445f;
  text-decoration: none;
  font-weight: 750;
  font-size: 0.95rem;
  line-height: 1;
}
.site-nav a:hover,
.site-nav a:focus {
  color: #05314e;
  background: rgba(0, 140, 160, 0.09);
}
.nav-toggle {
  display: none;
  border: 1px solid rgba(20, 70, 100, 0.16);
  background: #fff;
  color: #11344f;
  border-radius: 12px;
  padding: 0.45rem 0.6rem;
  font-weight: 900;
}

.container {
  width: min(1200px, calc(100% - 48px));
  margin-inline: auto;
  padding: 2.25rem 0 4rem;
}

.hero.compact {
  max-width: 860px;
  margin: 0 auto 1.45rem;
  padding: clamp(2.1rem, 5vw, 4.2rem) 0 1.15rem;
}
.hero.compact .eyebrow,
.eyebrow {
  color: #007d74;
  font-size: 0.78rem;
  font-weight: 950;
  letter-spacing: 0.24em;
  text-transform: uppercase;
}
.hero.compact h1 {
  margin: 0.15rem 0 0.55rem;
  color: #0d1b2c;
  font-size: clamp(3rem, 7vw, 5.3rem);
  line-height: 0.95;
  letter-spacing: -0.07em;
}
.hero.compact .lead {
  color: #647184;
  font-size: clamp(1.05rem, 1.8vw, 1.33rem);
  line-height: 1.65;
}
.hero-note {
  color: #203248;
  font-size: 1rem;
  line-height: 1.7;
}
.publications-note-card {
  width: min(980px, 100%);
  margin: 0 auto 1.65rem;
}
.publications-showcase {
  margin-top: 1.2rem;
}

/* Make publication cards feel like designed research objects. */
.pub-visual-card {
  grid-template-columns: minmax(0, 1.24fr) minmax(330px, 0.76fr) !important;
  gap: 1.05rem !important;
  padding: 1.05rem !important;
  border-radius: 28px !important;
}
.pub-card-main {
  padding: 0.25rem 0.35rem 0.25rem 0.5rem !important;
}
.pub-card-title {
  max-width: 880px;
}
.pub-venue-strip .pub-badge strong,
.pub-badge.journal strong {
  font-weight: 950;
}

/* Figure panel: no captions, image fills the whole rounded box. */
.pub-visual-panel {
  align-self: stretch;
  justify-content: stretch !important;
  gap: 0 !important;
  padding: 0.42rem !important;
  border-radius: 26px !important;
  background: linear-gradient(135deg, rgba(238, 248, 252, 0.95), rgba(246, 245, 255, 0.96)) !important;
}
.pub-visual-frame {
  width: 100% !important;
  height: 100% !important;
  min-height: 290px !important;
  aspect-ratio: 16 / 10;
  border-radius: 22px !important;
  overflow: hidden !important;
  background: #eaf4f8 !important;
  box-shadow: inset 0 0 0 1px rgba(255,255,255,0.55), 0 14px 34px rgba(15, 55, 85, 0.08);
}
.pub-visual-frame img {
  width: 100% !important;
  height: 100% !important;
  max-width: none !important;
  max-height: none !important;
  object-fit: cover !important;
  object-position: center center !important;
  display: block !important;
}
.pub-visual-caption {
  display: none !important;
}

@media (max-width: 980px) {
  .site-header {
    align-items: flex-start;
    flex-direction: column;
    gap: 0.35rem;
  }
  .site-nav {
    justify-content: flex-start;
  }
  .container {
    width: min(100% - 32px, 980px);
    padding-top: 1.6rem;
  }
  .pub-visual-card {
    grid-template-columns: 1fr !important;
  }
  .pub-visual-panel {
    order: -1;
  }
  .pub-visual-frame {
    min-height: 240px !important;
  }
}

@media (max-width: 600px) {
  .site-header {
    padding-inline: 1rem;
  }
  .site-nav a {
    padding: 0.32rem 0.48rem;
    font-size: 0.88rem;
  }
  .hero.compact h1 {
    font-size: clamp(2.35rem, 15vw, 3.3rem);
  }
  .pub-visual-frame {
    min-height: 210px !important;
    aspect-ratio: 4 / 3;
  }
}
'''


def remove_caption_from_html(text: str) -> str:
    # Remove the generated visual-caption paragraph from every publication card.
    text = re.sub(r"\n\s*<p class=\"pub-visual-caption\">.*?</p>", "", text, flags=re.S)
    # Remove empty vertical whitespace before closing aside if present.
    text = re.sub(r"(</div>)\s*\n\s*(</aside>)", r"\1\n  \2", text)
    return text


def append_css_once(css_text: str) -> str:
    # Remove older v6 block, then append the newest one.
    css_text = re.sub(r"\n?/\* === Publications layout polish v6 === \*/.*?(?=\n/\* === |\Z)", "", css_text, flags=re.S)
    return css_text.rstrip() + "\n\n" + CSS_BLOCK.strip() + "\n"


def patch_redesign_script(text: str) -> str:
    # Make future reruns of redesign_publications_page.py caption-free and fill-image by default.
    text = text.replace('    <p class="pub-visual-caption">Visual anchor for the paper: method, data, deployment context, or first-page preview.</p>\n', '')
    text = text.replace('object-fit: contain;', 'object-fit: cover;')
    text = text.replace('max-height: 260px;', 'max-height: none;')
    return text


def main() -> None:
    if not PUB_HTML.exists():
        raise SystemExit(f"Missing {PUB_HTML}. Run this script from the repository root after applying the visual publications page patch.")
    html = PUB_HTML.read_text(encoding="utf-8", errors="ignore")
    old_html = html
    html = remove_caption_from_html(html)
    PUB_HTML.write_text(html, encoding="utf-8")

    CSS_PATH.parent.mkdir(parents=True, exist_ok=True)
    css = CSS_PATH.read_text(encoding="utf-8", errors="ignore") if CSS_PATH.exists() else ""
    CSS_PATH.write_text(append_css_once(css), encoding="utf-8")

    if REDESIGN_SCRIPT.exists():
        script_text = REDESIGN_SCRIPT.read_text(encoding="utf-8", errors="ignore")
        REDESIGN_SCRIPT.write_text(patch_redesign_script(script_text), encoding="utf-8")
        print("[OK] Patched scripts/redesign_publications_page.py for future reruns.")

    removed = old_html.count('pub-visual-caption') - html.count('pub-visual-caption')
    print(f"[OK] Removed visual captions from publications.html: {removed} occurrence(s).")
    print("[OK] Added v6 header, spacing, card, and figure-fill CSS.")
    print("[CHECK] Open publications.html locally, then push and use ?v=publications-v6-fix")


if __name__ == "__main__":
    main()
