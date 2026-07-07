from pathlib import Path
import re

root = Path('.')
css_path = root / 'assets' / 'css' / 'style.css'
html_path = root / 'publications.html'

if not css_path.exists():
    raise FileNotFoundError(f'Missing {css_path}')
if not html_path.exists():
    raise FileNotFoundError(f'Missing {html_path}')

css = css_path.read_text(encoding='utf-8', errors='ignore')
html = html_path.read_text(encoding='utf-8', errors='ignore')

# Remove older copies of this exact patch if rerun.
css = re.sub(
    r"/\* === Publications 60-40 first-page preview layout v17 START === \*/.*?/\* === Publications 60-40 first-page preview layout v17 END === \*/",
    "",
    css,
    flags=re.S,
)

# Clean malformed image tags left by older generated versions.
html = re.sub(r'(\bdecoding="async")\s+Visual summary for[^>]*', r'\1', html)
html = re.sub(r'\s+Visual summary for [^>]+(?=></div>)', '', html)

css_block = r'''
/* === Publications 60-40 first-page preview layout v17 START === */
/* Senior layout intent:
   - left information column: 60%
   - right first-page preview column: 40%
   - preserve the natural A4/page ratio of the image
   - make the preview use the full right column width
   - do not crop the paper page and do not force a tall empty frame
*/

@media (min-width: 1080px) {
  .publication-card {
    display: grid !important;
    grid-template-columns: minmax(0, 60%) minmax(0, 40%) !important;
    column-gap: clamp(24px, 2.4vw, 46px) !important;
    align-items: start !important;
  }

  .publication-card > *:first-child,
  .pub-card-main,
  .pub-main,
  .pub-info,
  .pub-content {
    min-width: 0 !important;
    max-width: none !important;
  }

  .pub-visual {
    justify-self: stretch !important;
    align-self: start !important;
    width: 100% !important;
    max-width: none !important;
    display: flex !important;
    justify-content: center !important;
  }
}

/* Cover all frame class names introduced by previous versions. */
.pub-visual-frame,
.pub-firstpage-crop-frame,
.pub-a4-page-frame,
.pub-compact-a4-frame,
.pub-final-a4-thumb-frame,
.pub-a4-wide-frame,
.pub-final-a4-frame,
.pub-a4-frame,
.pub-preview-frame {
  box-sizing: border-box !important;
  width: 100% !important;
  max-width: none !important;
  height: auto !important;
  min-height: 0 !important;
  max-height: none !important;
  aspect-ratio: auto !important;
  padding: clamp(12px, 1.1vw, 18px) !important;
  border-radius: 30px !important;
  overflow: hidden !important;
  background: linear-gradient(180deg, #f7fbff 0%, #eef6fb 100%) !important;
  border: 1px solid rgba(118, 160, 190, 0.26) !important;
  box-shadow: 0 18px 45px rgba(20, 54, 86, 0.11) !important;
}

.pub-visual-frame img,
.pub-firstpage-crop-frame img,
.pub-a4-page-frame img,
.pub-compact-a4-frame img,
.pub-final-a4-thumb-frame img,
.pub-a4-wide-frame img,
.pub-final-a4-frame img,
.pub-a4-frame img,
.pub-preview-frame img,
.publication-card .pub-visual img {
  display: block !important;
  width: 100% !important;
  height: auto !important;
  min-height: 0 !important;
  max-width: none !important;
  max-height: none !important;
  object-fit: contain !important;
  object-position: top center !important;
  aspect-ratio: auto !important;
  border-radius: 20px !important;
  background: #ffffff !important;
}

/* Keep the layout readable on medium screens while still giving the preview space. */
@media (min-width: 1080px) and (max-width: 1320px) {
  .publication-card {
    grid-template-columns: minmax(0, 58%) minmax(0, 42%) !important;
    column-gap: 24px !important;
  }
}

@media (max-width: 1079px) {
  .publication-card {
    grid-template-columns: 1fr !important;
  }

  .pub-visual {
    width: min(100%, 520px) !important;
    max-width: 520px !important;
    margin: 0 auto !important;
  }
}
/* === Publications 60-40 first-page preview layout v17 END === */
'''

css = css.rstrip() + "\n\n" + css_block.strip() + "\n"

css_path.write_text(css, encoding='utf-8')
html_path.write_text(html, encoding='utf-8')

print('Done: applied v17 60/40 publication-card layout and enlarged first-page preview area.')
