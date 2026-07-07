from pathlib import Path
import re

root = Path('.')
html_path = root / 'publications.html'
css_path = root / 'assets' / 'css' / 'style.css'

if not html_path.exists():
    raise SystemExit('ERROR: publications.html not found. Run this from the repository root.')
if not css_path.exists():
    raise SystemExit('ERROR: assets/css/style.css not found. Run this from the repository root.')

html = html_path.read_text(encoding='utf-8', errors='ignore')

# Normalize any previous preview-frame classes to one clean class.
# This cancels the older v10/v11/v12/v13/v14 frame variants in HTML.
html = re.sub(
    r'<div\s+class="[^"]*(?:pub-visual-frame|pub-firstpage-crop-frame|pub-a4-page-frame|pub-compact-a4-frame|pub-final-a4-thumb-frame)[^"]*">',
    '<div class="pub-visual-frame pub-a4-wide-frame">',
    html,
    flags=re.I,
)

# Clean malformed leftover text that may still appear inside image tags.
html = re.sub(r'(\bdecoding="async")\s+Visual summary for[^>]*', r'\1', html)
html = re.sub(r'\s+Visual summary for [^>]+(?=></div>)', '', html)

html_path.write_text(html, encoding='utf-8')

css = css_path.read_text(encoding='utf-8', errors='ignore')

# Remove previous copies of this exact v15 block if rerun.
css = re.sub(
    r'/\* === Publications wide A4 first-page preview v15 START === \*/.*?/\* === Publications wide A4 first-page preview v15 END === \*/',
    '',
    css,
    flags=re.S,
)

css_block = r'''
/* === Publications wide A4 first-page preview v15 START === */
:root {
  --pub-preview-wide: clamp(360px, 34vw, 460px);
}

/* Card layout: keep the left text readable and give the right A4 preview more area. */
.publication-card {
  display: grid !important;
  grid-template-columns: minmax(0, 1fr) var(--pub-preview-wide) !important;
  gap: clamp(1.5rem, 2.2vw, 2.25rem) !important;
  align-items: start !important;
  min-height: 0 !important;
}

.publication-card > * {
  min-width: 0 !important;
}

.pub-visual {
  width: 100% !important;
  max-width: var(--pub-preview-wide) !important;
  align-self: start !important;
  justify-self: end !important;
  display: block !important;
  margin: 0 !important;
  min-height: 0 !important;
}

/* Compact, larger A4-ratio thumbnail. This is a ratio box, not a full page-height panel. */
.pub-visual-frame.pub-a4-wide-frame,
.pub-visual-frame {
  width: 100% !important;
  aspect-ratio: 210 / 297 !important;
  height: auto !important;
  min-height: 0 !important;
  max-height: none !important;
  padding: 10px !important;
  box-sizing: border-box !important;
  display: flex !important;
  align-items: flex-start !important;
  justify-content: center !important;
  overflow: hidden !important;
  border-radius: 30px !important;
  background: linear-gradient(180deg, #f8fbff 0%, #eef5fb 100%) !important;
  border: 1px solid rgba(121, 157, 190, 0.28) !important;
  box-shadow: 0 16px 36px rgba(26, 55, 90, 0.11) !important;
}

/* Fill the A4-ratio frame. Top positioning avoids losing header/title information. */
.pub-visual-frame.pub-a4-wide-frame img,
.pub-visual-frame img {
  display: block !important;
  width: 100% !important;
  height: 100% !important;
  max-width: none !important;
  max-height: none !important;
  min-height: 0 !important;
  object-fit: cover !important;
  object-position: top center !important;
  border-radius: 20px !important;
  background: #ffffff !important;
  box-shadow: 0 8px 22px rgba(17, 38, 63, 0.08) !important;
}

/* Cancel old preview experiments that used full-height panels or small thumbnails. */
.pub-firstpage-crop-frame,
.pub-a4-page-frame,
.pub-compact-a4-frame,
.pub-final-a4-thumb-frame,
.pub-firstpage-crop-frame img,
.pub-a4-page-frame img,
.pub-compact-a4-frame img,
.pub-final-a4-thumb-frame img {
  height: auto;
  min-height: 0;
  max-height: none;
}

@media (max-width: 1180px) {
  :root {
    --pub-preview-wide: clamp(315px, 38vw, 390px);
  }
}

@media (max-width: 920px) {
  .publication-card {
    grid-template-columns: 1fr !important;
  }

  .pub-visual {
    width: min(100%, 390px) !important;
    max-width: 390px !important;
    justify-self: center !important;
    margin-top: 0.75rem !important;
  }
}
/* === Publications wide A4 first-page preview v15 END === */
'''

css = css.rstrip() + '\n\n' + css_block.strip() + '\n'
css_path.write_text(css, encoding='utf-8')

print('Done: publication previews now use a wider compact A4-ratio frame.')
print('Updated: publications.html')
print('Updated: assets/css/style.css')
