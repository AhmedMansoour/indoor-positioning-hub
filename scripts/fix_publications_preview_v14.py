from pathlib import Path
import re

root = Path('.')
css_path = root / 'assets' / 'css' / 'style.css'
html_path = root / 'publications.html'

if not css_path.exists():
    raise FileNotFoundError(f'Cannot find {css_path}. Run this script from the repository root.')
if not html_path.exists():
    raise FileNotFoundError(f'Cannot find {html_path}. Run this script from the repository root.')

css_block = r'''

/* === Publications preview natural-height fix v14 START === */
/*
   Goal:
   - Keep the paper first-page preview as a compact portrait thumbnail.
   - Do not stretch the preview frame to the full card height.
   - Let the image set the frame height naturally.
   - Increase the right-column preview width slightly for better readability.
*/
.publication-card {
  display: grid !important;
  grid-template-columns: minmax(0, 1fr) clamp(260px, 27vw, 335px) !important;
  gap: 1.75rem !important;
  align-items: start !important;
}

.pub-visual {
  align-self: start !important;
  justify-self: center !important;
  display: flex !important;
  justify-content: center !important;
  width: 100% !important;
  min-height: 0 !important;
  height: auto !important;
}

.pub-visual-frame,
.pub-final-a4-thumb-frame,
.pub-compact-a4-frame,
.pub-a4-page-frame,
.pub-firstpage-crop-frame {
  width: 100% !important;
  max-width: 335px !important;
  height: auto !important;
  min-height: 0 !important;
  max-height: none !important;
  aspect-ratio: auto !important;
  padding: 14px !important;
  border-radius: 28px !important;
  overflow: hidden !important;
  background: linear-gradient(180deg, #f7fbff 0%, #f2f6fb 100%) !important;
  border: 1px solid rgba(130, 160, 190, 0.22) !important;
  box-shadow: 0 10px 28px rgba(22, 48, 84, 0.08) !important;
  display: block !important;
}

.pub-visual-frame img,
.pub-final-a4-thumb-frame img,
.pub-compact-a4-frame img,
.pub-a4-page-frame img,
.pub-firstpage-crop-frame img {
  display: block !important;
  width: 100% !important;
  height: auto !important;
  min-height: 0 !important;
  max-height: none !important;
  aspect-ratio: auto !important;
  object-fit: contain !important;
  object-position: top center !important;
  border-radius: 18px !important;
  background: #ffffff !important;
}

/* Remove old pseudo/fixed preview behavior if previous patches left it active. */
.pub-visual-frame::before,
.pub-final-a4-thumb-frame::before,
.pub-compact-a4-frame::before,
.pub-a4-page-frame::before,
.pub-firstpage-crop-frame::before {
  content: none !important;
  display: none !important;
}

@media (max-width: 1100px) {
  .publication-card {
    grid-template-columns: 1fr !important;
  }

  .pub-visual {
    width: min(100%, 350px) !important;
    margin: 0 auto !important;
  }

  .pub-visual-frame,
  .pub-final-a4-thumb-frame,
  .pub-compact-a4-frame,
  .pub-a4-page-frame,
  .pub-firstpage-crop-frame {
    max-width: 350px !important;
  }
}
/* === Publications preview natural-height fix v14 END === */
'''

# Append clean CSS override block at the end. Remove existing v14 block if rerun.
css = css_path.read_text(encoding='utf-8', errors='ignore')
css = re.sub(
    r'/\* === Publications preview natural-height fix v14 START === \*/.*?/\* === Publications preview natural-height fix v14 END === \*/',
    '',
    css,
    flags=re.S,
)
css = css.rstrip() + '\n\n' + css_block.strip() + '\n'
css_path.write_text(css, encoding='utf-8')

# Clean malformed image tags left from older visual-summary versions.
html = html_path.read_text(encoding='utf-8', errors='ignore')
html = re.sub(r'(\bdecoding="async")\s+Visual summary for[^>]*', r'\1', html)
html = re.sub(r'\s+Visual summary for [^>]+(?=></div>)', '', html)

# Normalize older frame class names back to the simple common frame class.
html = html.replace('pub-final-a4-thumb-frame', 'pub-visual-frame')
html = html.replace('pub-compact-a4-frame', 'pub-visual-frame')
html = html.replace('pub-a4-page-frame', 'pub-visual-frame')
html = html.replace('pub-firstpage-crop-frame', 'pub-visual-frame')

html_path.write_text(html, encoding='utf-8')

print('Done: applied v14 natural-height compact preview fix.')
print('Next: check publications.html in browser, then commit and push.')
