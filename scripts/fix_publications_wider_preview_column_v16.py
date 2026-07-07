from pathlib import Path
import re

ROOT = Path('.')
HTML_PATH = ROOT / 'publications.html'
CSS_PATH = ROOT / 'assets' / 'css' / 'style.css'

CSS_START = '/* === Publications wider preview column v16 FIXED START === */'
CSS_END = '/* === Publications wider preview column v16 FIXED END === */'

CSS_BLOCK = r'''
/* === Publications wider preview column v16 FIXED START === */
/* Wider right-side first-page previews, compact A4 ratio, narrower text column. */
.publication-card {
  display: grid !important;
  grid-template-columns: minmax(0, 0.78fr) minmax(360px, clamp(380px, 34vw, 485px)) !important;
  gap: clamp(1.25rem, 2.2vw, 2rem) !important;
  align-items: start !important;
}

.publication-card > .pub-main,
.publication-card > .pub-content,
.publication-card > .pub-info,
.publication-card > .publication-content {
  min-width: 0 !important;
}

.pub-visual {
  align-self: start !important;
  justify-self: end !important;
  width: 100% !important;
  max-width: 485px !important;
  min-width: 0 !important;
  margin: 0 !important;
}

.pub-visual-frame,
.pub-wide-a4-frame,
.pub-a4-wide-frame,
.pub-final-a4-thumb-frame,
.pub-compact-a4-frame,
.pub-a4-page-frame,
.pub-firstpage-crop-frame {
  width: 100% !important;
  aspect-ratio: 210 / 297 !important;
  height: auto !important;
  max-height: none !important;
  min-height: 0 !important;
  box-sizing: border-box !important;
  padding: 12px !important;
  border-radius: 26px !important;
  overflow: hidden !important;
  background: linear-gradient(180deg, #f7fbff 0%, #eef5fb 100%) !important;
  border: 1px solid rgba(120, 150, 185, 0.24) !important;
  box-shadow: 0 14px 32px rgba(22, 48, 84, 0.10) !important;
}

.pub-visual-frame img,
.pub-wide-a4-frame img,
.pub-a4-wide-frame img,
.pub-final-a4-thumb-frame img,
.pub-compact-a4-frame img,
.pub-a4-page-frame img,
.pub-firstpage-crop-frame img {
  display: block !important;
  width: 100% !important;
  height: 100% !important;
  max-height: none !important;
  min-height: 0 !important;
  object-fit: contain !important;
  object-position: top center !important;
  border-radius: 18px !important;
  background: #ffffff !important;
}

/* Reduce the visual weight of the left text side so the preview becomes the visual anchor. */
.publication-card h2,
.publication-card h3,
.pub-title {
  max-width: 100% !important;
}

.publication-card .pub-actions,
.publication-card .pub-links,
.publication-card .paper-actions {
  gap: 0.45rem !important;
}

@media (max-width: 1180px) {
  .publication-card {
    grid-template-columns: minmax(0, 1fr) minmax(320px, 410px) !important;
  }

  .pub-visual {
    max-width: 410px !important;
  }
}

@media (max-width: 900px) {
  .publication-card {
    grid-template-columns: 1fr !important;
  }

  .pub-visual {
    justify-self: center !important;
    width: min(100%, 390px) !important;
    max-width: 390px !important;
    margin-top: 0.75rem !important;
  }
}
/* === Publications wider preview column v16 FIXED END === */
'''.strip()


def replace_or_append_css(css: str) -> str:
    pattern = re.compile(
        r"/\* === Publications wider preview column v16(?: FIXED)? START === \*/.*?/\* === Publications wider preview column v16(?: FIXED)? END === \*/",
        re.S,
    )
    css = pattern.sub('', css)
    return css.rstrip() + '\n\n' + CSS_BLOCK + '\n'


def normalize_preview_frame_classes(html: str) -> str:
    # Normalize all known earlier preview-frame variants to one stable class pair.
    known = [
        'pub-visual-frame',
        'pub-wide-a4-frame',
        'pub-a4-wide-frame',
        'pub-final-a4-thumb-frame',
        'pub-compact-a4-frame',
        'pub-a4-page-frame',
        'pub-firstpage-crop-frame',
    ]

    def repl(match: re.Match) -> str:
        class_value = match.group(1)
        if any(k in class_value for k in known):
            return '<div class="pub-visual-frame pub-wide-a4-frame">'
        return match.group(0)

    html = re.sub(r'<div\s+class="([^"]*)">', repl, html)

    # Remove malformed leftover text that may appear inside img tags from older patches.
    html = re.sub(r'(\bdecoding="async")\s+Visual summary for[^>]*', r'\1', html)
    html = re.sub(r'\s+Visual summary for [^>]+(?=></div>)', '', html)
    return html


def main() -> None:
    if not HTML_PATH.exists():
        raise FileNotFoundError(f'Missing {HTML_PATH}')
    if not CSS_PATH.exists():
        raise FileNotFoundError(f'Missing {CSS_PATH}')

    html = HTML_PATH.read_text(encoding='utf-8', errors='ignore')
    html = normalize_preview_frame_classes(html)
    HTML_PATH.write_text(html, encoding='utf-8')

    css = CSS_PATH.read_text(encoding='utf-8', errors='ignore')
    css = replace_or_append_css(css)
    CSS_PATH.write_text(css, encoding='utf-8')

    print('Done: publication cards now use a narrower text column and wider A4-ratio preview column.')
    print('Updated:', HTML_PATH)
    print('Updated:', CSS_PATH)


if __name__ == '__main__':
    main()
