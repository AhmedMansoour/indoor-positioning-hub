from __future__ import annotations

import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
PUB_HTML = ROOT / "publications.html"
CSS_PATH = ROOT / "assets" / "css" / "style.css"
PREVIEWS_DIR = ROOT / "assets" / "previews"
PDF_DIR = ROOT / "paper-pdfs"
REDESIGN_SCRIPT = ROOT / "scripts" / "redesign_publications_page.py"

HERO_BLOCK = '''<section class="hero compact">
    <p class="eyebrow">Publication portfolio</p>
    <h1>Publications</h1>
    <p class="lead">This page brings together Ahmed Mansour's peer-reviewed publications, thesis work, and conference outputs in indoor positioning and indoor spatial intelligence. The papers are organized around Wi-Fi fingerprinting, smartphone PDR, mobile crowdsensing, autonomous 3D radio mapping, indoor--outdoor awareness, GNSS/PDR integration, cooperative localization, and deployment-aware positioning for smart buildings, construction sites, and urban environments.</p>
    <p class="hero-note">Each card works as a quick reading guide. The first-page preview identifies the paper at a glance, the highlighted author name shows Ahmed Mansour's role, the venue, ranking, and DOI badges support citation, and the symbol and keyword cues summarize the problem setting, sensing data, method family, and deployment context.</p>
  </section>'''

NOTE_BLOCK = '''<section class="publications-note-card">
    <strong>17 research outputs are organized for fast reading, citation, and thematic discovery.</strong> Use this page to locate papers by research problem, sensor modality, method, environment, and application. The cards connect each title to its DOI, PDF, publication page, technical descriptors, and short reading lens. Journal impact factors, quartiles, and local tier labels are editable display metadata in <code>data/publication_display_metadata.json</code> and can be updated whenever ranking sources change.
  </section>'''

CSS_BLOCK = r'''
/* === Publications first-page cards v8 === */
/* Force every publication-card visual to use the paper first-page preview. */
.hero.compact {
  max-width: 980px;
  padding-top: 3.1rem;
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
  grid-template-columns: minmax(0, 1.34fr) minmax(250px, 0.52fr) !important;
}
.pub-visual-panel {
  padding: 0.62rem !important;
  border-radius: 28px !important;
  background:
    linear-gradient(135deg, rgba(244, 250, 253, 0.98), rgba(247, 247, 255, 0.98)) !important;
  border: 1px solid rgba(55, 110, 148, 0.14) !important;
  box-shadow: inset 0 0 0 1px rgba(255,255,255,0.68), 0 16px 38px rgba(14, 54, 84, 0.075) !important;
  align-self: stretch;
  display: flex;
}
.pub-visual-frame {
  width: 100% !important;
  height: 100% !important;
  min-height: 340px !important;
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
  object-fit: contain !important;
  object-position: top center !important;
  display: block !important;
  background: #fff !important;
}
.pub-visual-caption {
  display: none !important;
}
.pub-paper-lens,
.pub-insight-box {
  color: #626f7f;
  font-size: 0.96rem;
  line-height: 1.76;
}
@media (max-width: 980px) {
  .pub-visual-card {
    grid-template-columns: 1fr !important;
  }
  .pub-visual-panel {
    max-width: 380px;
    margin-inline: auto;
    order: -1;
  }
  .pub-visual-frame {
    min-height: 0 !important;
  }
}
@media (max-width: 560px) {
  .pub-visual-panel {
    max-width: 290px;
  }
}
'''


def read(path: Path) -> str:
    return path.read_text(encoding="utf-8", errors="ignore")


def write(path: Path, text: str) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(text, encoding="utf-8")


def rel_path(p: Path) -> str:
    return p.relative_to(ROOT).as_posix()


def extract_articles(html: str) -> list[tuple[str, str, str]]:
    """Return [(slug, title, article_html)]."""
    out: list[tuple[str, str, str]] = []
    pattern = re.compile(r'(<article class="pub-visual-card" id="(?P<slug>[^"]+)">.*?</article>)', re.S)
    for m in pattern.finditer(html):
        block = m.group(1)
        slug = m.group('slug')
        title_match = re.search(r'<h2[^>]*>\s*<a[^>]*>(.*?)</a>\s*</h2>', block, re.S)
        title = re.sub(r'<.*?>', '', title_match.group(1)).strip() if title_match else slug.replace('-', ' ')
        out.append((slug, title, block))
    return out


def render_preview_from_pdf(slug: str, overwrite: bool = False) -> bool:
    preview = PREVIEWS_DIR / f"{slug}.png"
    pdf = PDF_DIR / f"{slug}.pdf"
    if preview.exists() and not overwrite:
        return True
    if not pdf.exists():
        return False
    try:
        import fitz  # PyMuPDF
    except Exception:
        print("[WARN] PyMuPDF is not installed, so missing previews cannot be rendered. Run: pip install pymupdf")
        return False
    try:
        PREVIEWS_DIR.mkdir(parents=True, exist_ok=True)
        doc = fitz.open(str(pdf))
        page = doc.load_page(0)
        # 150 dpi keeps files light but readable for webpage cards.
        pix = page.get_pixmap(matrix=fitz.Matrix(150 / 72, 150 / 72), alpha=False)
        pix.save(str(preview))
        doc.close()
        print(f"[OK] Rendered first-page preview: {rel_path(preview)}")
        return True
    except Exception as exc:
        print(f"[WARN] Could not render {pdf}: {exc}")
        return False


def replace_hero_and_note(html: str) -> str:
    html = re.sub(r'<section class="hero compact">.*?</section>', HERO_BLOCK, html, flags=re.S, count=1)
    html = re.sub(r'<section class="publications-note-card">.*?</section>', NOTE_BLOCK, html, flags=re.S, count=1)
    return html


def force_first_page_images(html: str, overwrite_render: bool = False) -> tuple[str, int, list[str]]:
    missing: list[str] = []
    changed = 0

    def patch_article(m: re.Match) -> str:
        nonlocal changed
        block = m.group(1)
        slug = m.group('slug')
        title_match = re.search(r'<h2[^>]*>\s*<a[^>]*>(.*?)</a>\s*</h2>', block, re.S)
        title = re.sub(r'<.*?>', '', title_match.group(1)).strip() if title_match else slug.replace('-', ' ')
        ok = render_preview_from_pdf(slug, overwrite=overwrite_render)
        preview = PREVIEWS_DIR / f"{slug}.png"
        if not ok and not preview.exists():
            missing.append(slug)
            return block
        src = f"assets/previews/{slug}.png"
        alt = f"First page preview of {title}".replace('"', '&quot;')

        # Replace the first img tag inside the publication visual frame, whatever the old source was.
        new_block, n = re.subn(
            r'(<div class="pub-visual-frame">\s*<img\s+)([^>]*?)(/?>)',
            lambda im: replace_img_tag(im.group(1), im.group(2), im.group(3), src, alt),
            block,
            count=1,
            flags=re.S,
        )
        if n:
            changed += 1
            # Remove any visual caption in this article.
            new_block = re.sub(r'\s*<p class="pub-visual-caption">.*?</p>', '', new_block, flags=re.S)
            return new_block
        return block

    def replace_img_tag(prefix: str, attrs: str, suffix: str, src: str, alt: str) -> str:
        attrs = re.sub(r'\s*src="[^"]*"', '', attrs, flags=re.S)
        attrs = re.sub(r'\s*alt="[^"]*"', '', attrs, flags=re.S)
        attrs = re.sub(r'\s*loading="[^"]*"', '', attrs, flags=re.S)
        attrs = re.sub(r'\s*decoding="[^"]*"', '', attrs, flags=re.S)
        attrs = attrs.strip()
        extra = (" " + attrs) if attrs else ""
        return f'{prefix}src="{src}" alt="{alt}" loading="lazy" decoding="async"{extra}{suffix}'

    pattern = re.compile(r'(<article class="pub-visual-card" id="(?P<slug>[^"]+)">.*?</article>)', re.S)
    html = pattern.sub(patch_article, html)
    # Safety: remove any leftover captions globally.
    html = re.sub(r'\s*<p class="pub-visual-caption">.*?</p>', '', html, flags=re.S)
    return html, changed, missing


def append_css_once(css: str) -> str:
    css = re.sub(r'\n?/\* === Publications first-page cards v8 === \*/.*?(?=\n/\* === |\Z)', '', css, flags=re.S)
    # Remove older v7 first-page block so it cannot override v8.
    css = re.sub(r'\n?/\* === Publications first-page preview and reading text v7 === \*/.*?(?=\n/\* === |\Z)', '', css, flags=re.S)
    return css.rstrip() + "\n\n" + CSS_BLOCK.strip() + "\n"


def patch_redesign_script(text: str) -> str:
    # Make future reruns prefer first-page previews and keep the rewritten intro.
    if 'def choose_visual(slug: str, display: dict) -> str:' in text and 'v8: first-page preview must be the publication-card visual' not in text:
        text = text.replace(
            'def choose_visual(slug: str, display: dict) -> str:\n',
            'def choose_visual(slug: str, display: dict) -> str:\n'
            '    # v8: first-page preview must be the publication-card visual.\n'
            '    preview = ROOT / "assets" / "previews" / f"{slug}.png"\n'
            '    if preview.exists():\n'
            '        return rel(str(preview.relative_to(ROOT)))\n',
            1,
        )
    text = re.sub(r'<p class="pub-visual-caption">.*?</p>', '', text, flags=re.S)
    text = text.replace('object-fit: cover;', 'object-fit: contain;')
    text = text.replace('object-position: center center;', 'object-position: top center;')
    return text


def main() -> None:
    if not PUB_HTML.exists():
        raise SystemExit(f"Missing {PUB_HTML}. Run this script from the repository root.")

    overwrite = "--overwrite-previews" in sys.argv
    html = read(PUB_HTML)
    html = replace_hero_and_note(html)
    articles = extract_articles(html)
    html, changed, missing = force_first_page_images(html, overwrite_render=overwrite)
    write(PUB_HTML, html)

    css = read(CSS_PATH) if CSS_PATH.exists() else ""
    write(CSS_PATH, append_css_once(css))

    if REDESIGN_SCRIPT.exists():
        write(REDESIGN_SCRIPT, patch_redesign_script(read(REDESIGN_SCRIPT)))
        print("[OK] Patched scripts/redesign_publications_page.py so future reruns keep first-page previews.")

    print(f"[OK] Found {len(articles)} publication card(s).")
    print(f"[OK] Forced {changed} card image(s) to assets/previews/<slug>.png.")
    if missing:
        print("[WARN] Missing PDF/preview for these slug(s), so their current image was kept:")
        for slug in missing:
            print(f"  - {slug}")
        print("[TIP] Add paper-pdfs/<slug>.pdf, then rerun: python scripts\\force_publication_firstpage_cards_v8.py")
    print("[OK] Updated the top website text and note card in natural reading-guide language.")
    print("[CHECK] Run: findstr /N /C:\"assets/previews/\" publications.html")


if __name__ == "__main__":
    main()
