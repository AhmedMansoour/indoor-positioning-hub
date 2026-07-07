from pathlib import Path
import re

root = Path('.')
css_path = root / 'assets' / 'css' / 'style.css'
html_path = root / 'publications.html'

if not css_path.exists():
    raise SystemExit('ERROR: assets/css/style.css was not found. Run this script from the repository root.')
if not html_path.exists():
    raise SystemExit('ERROR: publications.html was not found. Run this script from the repository root.')

css = css_path.read_text(encoding='utf-8', errors='ignore')
html = html_path.read_text(encoding='utf-8', errors='ignore')

# Remove malformed leftover text inside image tags, if any old script left it there.
html = re.sub(r'(\bdecoding="async")\s+Visual summary for[^>]*', r'\1', html)
html = re.sub(r'\s+Visual summary for [^>]+(?=></div>)', '', html)

# Ensure right-side publication preview frames use one common class too.
# This does not remove existing classes, it only adds a stable override class.
def add_true_preview_class(match: re.Match) -> str:
    cls = match.group(1)
    if 'pub-preview-true-40-frame' in cls:
        return match.group(0)
    return f'class="{cls} pub-preview-true-40-frame"'

html = re.sub(
    r'class="([^"]*\b(?:pub-visual-frame|pub-a4-wide-frame|pub-compact-a4-frame|pub-final-a4-thumb-frame|pub-a4-page-frame|pub-firstpage-crop-frame)\b[^"]*)"',
    add_true_preview_class,
    html,
)

html_path.write_text(html, encoding='utf-8')

block = r'''
/* === Publications true 40 percent preview layout v18 START === */
/*
   Purpose:
   - Give the first-page preview real space on the right side.
   - Stop older max-width rules from capping the preview at a small size.
   - Keep the preview as a portrait paper thumbnail using the A4 page ratio.
   - Reduce the left text column without compressing the content too much.
*/

@media (min-width: 1180px) {
  .publication-card {
    display: grid !important;
    grid-template-columns: minmax(0, 1.22fr) minmax(460px, 1fr) !important;
    column-gap: clamp(1.4rem, 2.4vw, 2.8rem) !important;
    align-items: start !important;
  }

  .publication-card > :first-child {
    min-width: 0 !important;
  }

  .publication-card .pub-visual,
  .pub-visual {
    width: 100% !important;
    max-width: none !important;
    min-width: 0 !important;
    align-self: start !important;
    justify-self: stretch !important;
    display: flex !important;
    justify-content: center !important;
  }

  .publication-card .pub-preview-true-40-frame,
  .publication-card .pub-visual-frame,
  .publication-card .pub-a4-wide-frame,
  .publication-card .pub-compact-a4-frame,
  .publication-card .pub-final-a4-thumb-frame,
  .publication-card .pub-a4-page-frame,
  .publication-card .pub-firstpage-crop-frame {
    box-sizing: border-box !important;
    width: 100% !important;
    max-width: none !important;
    min-width: 0 !important;
    height: auto !important;
    max-height: none !important;
    aspect-ratio: 210 / 297 !important;
    padding: clamp(12px, 1.1vw, 18px) !important;
    overflow: hidden !important;
    border-radius: 30px !important;
    background: linear-gradient(180deg, #f7fbff 0%, #eef6fb 100%) !important;
    border: 1px solid rgba(113, 151, 187, 0.28) !important;
    box-shadow: 0 16px 38px rgba(20, 51, 83, 0.11) !important;
  }

  .publication-card .pub-preview-true-40-frame img,
  .publication-card .pub-visual-frame img,
  .publication-card .pub-a4-wide-frame img,
  .publication-card .pub-compact-a4-frame img,
  .publication-card .pub-final-a4-thumb-frame img,
  .publication-card .pub-a4-page-frame img,
  .publication-card .pub-firstpage-crop-frame img {
    display: block !important;
    width: 100% !important;
    height: 100% !important;
    max-width: none !important;
    max-height: none !important;
    object-fit: contain !important;
    object-position: top center !important;
    border-radius: 20px !important;
    background: #ffffff !important;
  }
}

@media (min-width: 1500px) {
  .publication-card {
    grid-template-columns: minmax(0, 1.12fr) minmax(540px, 1fr) !important;
  }
}

@media (min-width: 1780px) {
  .publication-card {
    grid-template-columns: minmax(0, 1.05fr) minmax(600px, 1fr) !important;
  }
}

@media (max-width: 1179px) {
  .publication-card {
    grid-template-columns: 1fr !important;
  }

  .publication-card .pub-visual,
  .pub-visual {
    width: min(100%, 420px) !important;
    margin: 0 auto !important;
  }

  .publication-card .pub-preview-true-40-frame,
  .publication-card .pub-visual-frame,
  .publication-card .pub-a4-wide-frame,
  .publication-card .pub-compact-a4-frame,
  .publication-card .pub-final-a4-thumb-frame,
  .publication-card .pub-a4-page-frame,
  .publication-card .pub-firstpage-crop-frame {
    width: 100% !important;
    aspect-ratio: 210 / 297 !important;
  }
}
/* === Publications true 40 percent preview layout v18 END === */
'''

# Replace previous v18 block if rerun.
css = re.sub(
    r'/\* === Publications true 40 percent preview layout v18 START === \*/.*?/\* === Publications true 40 percent preview layout v18 END === \*/',
    '',
    css,
    flags=re.S,
).rstrip() + '\n\n' + block.strip() + '\n'

css_path.write_text(css, encoding='utf-8')

print('Done: publication cards now allocate a real larger right-side A4 preview column.')
print('Updated: publications.html')
print('Updated: assets/css/style.css')
