from __future__ import annotations

import re
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
PUB_HTML = ROOT / "publications.html"
CSS_PATH = ROOT / "assets" / "css" / "style.css"
REDESIGN_SCRIPT = ROOT / "scripts" / "redesign_publications_page.py"

HERO_BLOCK = '''<section class="hero compact">
    <p class="eyebrow">Publication portfolio</p>
    <h1>Publications</h1>
    <p class="lead">This page brings together Ahmed Mansour's peer-reviewed publications and thesis outputs in indoor positioning and indoor spatial intelligence. The work spans Wi-Fi fingerprinting, smartphone PDR, mobile crowdsensing, autonomous 3D radio mapping, indoor–outdoor awareness, GNSS/PDR integration, cooperative localization, and deployment-aware positioning for smart buildings and urban environments.</p>
    <p class="hero-note">Each publication card is designed as a quick reading guide: a first-page preview, the full citation title, author information with Ahmed Mansour highlighted, venue and DOI metadata, impact and ranking labels where relevant, key technical symbols, and a short reading lens that explains what the paper contributes and when it is useful to cite.</p>
  </section>'''

NOTE_BLOCK = '''<section class="publications-note-card">
    <strong>17 research outputs are organized for quick review, citation, and discovery.</strong> The cards use clear research vocabulary, first-page previews, DOI-level links, and concise technical descriptors so readers, citation tools, and academic search systems can connect each paper to its methods, datasets, and deployment context. Journal impact factors, quartiles, and local tier labels are editable display metadata in <code>data/publication_display_metadata.json</code> and can be updated whenever ranking sources change.
  </section>'''

CSS_BLOCK = r'''
/* === Publications first-page preview and reading text v7 === */
/* Use the first page of each paper as the visual anchor in the publications portfolio. */
.hero.compact {
  max-width: 980px;
}
.hero.compact .lead {
  color: #5e6d80;
  font-size: clamp(1.08rem, 1.55vw, 1.34rem);
  line-height: 1.72;
  letter-spacing: -0.01em;
}
.hero-note {
  max-width: 980px;
  color: #163049;
  font-size: 1.02rem;
  line-height: 1.78;
}
.publications-note-card {
  width: min(1080px, 100%);
  margin: 0 auto 1.7rem;
  padding: 1.08rem 1.25rem;
  border-radius: 25px;
  background:
    radial-gradient(circle at 0% 0%, rgba(0, 151, 167, 0.10), transparent 38%),
    linear-gradient(135deg, rgba(238, 249, 253, 0.96), rgba(248, 247, 255, 0.96));
  border: 1px solid rgba(50, 107, 145, 0.16);
  color: #394b60;
  line-height: 1.72;
}
.publications-note-card strong {
  color: #0a3b5b;
}
.pub-visual-card {
  grid-template-columns: minmax(0, 1.34fr) minmax(245px, 0.52fr) !important;
}
.pub-visual-panel {
  padding: 0.62rem !important;
  border-radius: 28px !important;
  background:
    linear-gradient(135deg, rgba(244, 250, 253, 0.98), rgba(247, 247, 255, 0.98)) !important;
  border: 1px solid rgba(55, 110, 148, 0.14) !important;
  box-shadow: inset 0 0 0 1px rgba(255,255,255,0.68), 0 16px 38px rgba(14, 54, 84, 0.075) !important;
}
.pub-visual-frame {
  width: 100% !important;
  height: auto !important;
  min-height: 0 !important;
  aspect-ratio: 210 / 297 !important;
  border-radius: 22px !important;
  overflow: hidden !important;
  background: #ffffff !important;
  box-shadow: 0 16px 36px rgba(14, 54, 84, 0.13), inset 0 0 0 1px rgba(19, 69, 105, 0.10) !important;
}
.pub-visual-frame img {
  width: 100% !important;
  height: 100% !important;
  max-width: none !important;
  max-height: none !important;
  object-fit: cover !important;
  object-position: top center !important;
  display: block !important;
  background: #fff !important;
}
.pub-visual-caption {
  display: none !important;
}
.pub-paper-lens {
  color: #626f7f;
  font-size: 0.96rem;
  line-height: 1.76;
}
@media (max-width: 980px) {
  .pub-visual-card {
    grid-template-columns: 1fr !important;
  }
  .pub-visual-panel {
    max-width: 360px;
    margin-inline: auto;
    order: -1;
  }
}
@media (max-width: 560px) {
  .pub-visual-panel {
    max-width: 280px;
  }
}
'''


def replace_hero_and_note(html: str) -> str:
    html = re.sub(r'<section class="hero compact">.*?</section>', HERO_BLOCK, html, flags=re.S, count=1)
    html = re.sub(r'<section class="publications-note-card">.*?</section>', NOTE_BLOCK, html, flags=re.S, count=1)
    return html


def use_first_page_previews(html: str) -> tuple[str, int]:
    pattern = re.compile(
        r'(<article class="pub-visual-card" id="(?P<slug>[^"]+)">(?:(?!</article>).)*?<div class="pub-visual-frame"><img src=")(?P<src>[^"]+)(")',
        re.S,
    )
    count = 0

    def repl(m: re.Match) -> str:
        nonlocal count
        slug = m.group('slug')
        preview_rel = f"assets/previews/{slug}.png"
        # Prefer the generated first-page preview. If a local preview is missing, keep the original image.
        if (ROOT / preview_rel).exists():
            count += 1
            return m.group(1) + preview_rel + m.group(3)
        return m.group(0)

    return pattern.sub(repl, html), count


def append_css_once(css: str) -> str:
    css = re.sub(r'\n?/\* === Publications first-page preview and reading text v7 === \*/.*?(?=\n/\* === |\Z)', '', css, flags=re.S)
    return css.rstrip() + "\n\n" + CSS_BLOCK.strip() + "\n"


def patch_redesign_script(text: str) -> str:
    # Make future reruns rebuild publications.html with first-page previews by default.
    if 'def choose_visual(slug: str, display: dict) -> str:' in text and 'v7: first-page preview is the default publication-card visual' not in text:
        text = text.replace(
            'def choose_visual(slug: str, display: dict) -> str:\n',
            'def choose_visual(slug: str, display: dict) -> str:\n'
            '    # v7: first-page preview is the default publication-card visual.\n'
            '    preview = ROOT / "assets" / "previews" / f"{slug}.png"\n'
            '    if preview.exists():\n'
            '        return rel(str(preview.relative_to(ROOT)))\n',
            1,
        )
    text = text.replace('object-fit: contain;', 'object-fit: cover;')
    text = text.replace('object-position: center center;', 'object-position: top center;')
    return text


def main() -> None:
    if not PUB_HTML.exists():
        raise SystemExit(f"Missing {PUB_HTML}. Run from the repository root.")

    html = PUB_HTML.read_text(encoding='utf-8', errors='ignore')
    html = replace_hero_and_note(html)
    html, n = use_first_page_previews(html)
    # Keep captions removed even if an older generation script added them.
    html = re.sub(r'\n\s*<p class="pub-visual-caption">.*?</p>', '', html, flags=re.S)
    PUB_HTML.write_text(html, encoding='utf-8')

    CSS_PATH.parent.mkdir(parents=True, exist_ok=True)
    css = CSS_PATH.read_text(encoding='utf-8', errors='ignore') if CSS_PATH.exists() else ''
    CSS_PATH.write_text(append_css_once(css), encoding='utf-8')

    if REDESIGN_SCRIPT.exists():
        rs = REDESIGN_SCRIPT.read_text(encoding='utf-8', errors='ignore')
        REDESIGN_SCRIPT.write_text(patch_redesign_script(rs), encoding='utf-8')
        print('[OK] Patched scripts/redesign_publications_page.py so future reruns prefer first-page previews.')

    print('[OK] Updated publications hero and note text.')
    print(f'[OK] Switched {n} publication-card visual(s) to assets/previews/<slug>.png where preview files exist.')
    print('[OK] Added v7 CSS for portrait first-page preview panels.')
    print('[CHECK] Open publications.html locally, then push and use ?v=publications-v7-firstpage')


if __name__ == '__main__':
    main()
