from pathlib import Path
import re

root = Path.cwd()
html_path = root / 'publications.html'
css_path = root / 'assets' / 'css' / 'style.css'

if not html_path.exists():
    raise SystemExit('ERROR: publications.html not found. Run this from the repository root.')
if not css_path.exists():
    raise SystemExit('ERROR: assets/css/style.css not found. Run this from the repository root.')

html = html_path.read_text(encoding='utf-8', errors='ignore')

# Use the original first-page previews, not the tight/crop variants.
html = html.replace('assets/previews-tight/', 'assets/previews/')
html = re.sub(r'(src="assets/previews/[^".]+)\.webp"', r'\1.png"', html)

# Remove malformed leftover text that earlier scripts accidentally left inside <img> tags.
html = re.sub(r'\s+Visual summary for [^>]+(?=></div>)', '', html)
html = re.sub(r'\s+Visual summary for [^>]+(?=>)', '', html)

# Normalize every publication preview frame to one final class.
html = re.sub(
    r'class="(?:pub-visual-frame|pub-firstpage-crop-frame|pub-a4-page-frame|pub-compact-a4-frame)(?:\s+[^\"]*)?"',
    'class="pub-visual-frame pub-final-a4-thumb-frame"',
    html,
)

# Make sure img alt text describes first-page preview, not a generic visual summary.
html = html.replace('alt="Visual summary for ', 'alt="First page preview of ')

html_path.write_text(html, encoding='utf-8')

css = css_path.read_text(encoding='utf-8', errors='ignore')
# Remove earlier v13 block if rerun.
css = re.sub(
    r'\n?/\* === Publications final compact A4 thumbnail v13 START === \*/.*?/\* === Publications final compact A4 thumbnail v13 END === \*/\n?',
    '\n',
    css,
    flags=re.S,
)

final_css = r'''

/* === Publications final compact A4 thumbnail v13 START ===
   Final design rule:
   - The paper preview is a COMPACT thumbnail.
   - The thumbnail keeps the A4 portrait aspect ratio, 210:297.
   - The preview frame does not stretch to the full card height.
   - The original first-page preview image is contained inside the A4 frame.
   - This block intentionally overrides earlier v9, v10, v11, and v12 attempts.
*/

.pub-visual-card,
.publication-card,
.pub-card {
  height: auto !important;
  min-height: 0 !important;
  align-items: flex-start !important;
}

.pub-visual-card {
  display: grid !important;
  grid-template-columns: minmax(0, 1fr) clamp(230px, 19vw, 275px) !important;
  column-gap: clamp(1.4rem, 2.4vw, 2.4rem) !important;
  row-gap: 1.2rem !important;
  align-items: start !important;
}

.pub-visual-side,
.pub-card-visual,
.pub-visual-preview,
.pub-card-media,
.pub-preview-side,
.pub-media,
.pub-thumbnail {
  align-self: start !important;
  justify-self: center !important;
  display: flex !important;
  justify-content: center !important;
  align-items: flex-start !important;
  width: 100% !important;
  height: auto !important;
  min-height: 0 !important;
  max-height: none !important;
}

.pub-visual-frame,
.pub-visual-frame.pub-final-a4-thumb-frame,
.pub-final-a4-thumb-frame,
.pub-firstpage-crop-frame,
.pub-a4-page-frame,
.pub-compact-a4-frame {
  width: clamp(230px, 19vw, 275px) !important;
  aspect-ratio: 210 / 297 !important;
  height: auto !important;
  min-height: 0 !important;
  max-height: none !important;
  padding: 0.72rem !important;
  margin: 0 auto !important;
  box-sizing: border-box !important;
  overflow: hidden !important;
  border-radius: 1.45rem !important;
  border: 1px solid rgba(148, 163, 184, 0.28) !important;
  background:
    linear-gradient(145deg, rgba(255,255,255,0.98), rgba(241,245,249,0.92)) !important;
  box-shadow:
    0 18px 42px rgba(15, 23, 42, 0.10),
    inset 0 1px 0 rgba(255, 255, 255, 0.85) !important;
}

.pub-visual-frame img,
.pub-visual-frame.pub-final-a4-thumb-frame img,
.pub-final-a4-thumb-frame img,
.pub-firstpage-crop-frame img,
.pub-a4-page-frame img,
.pub-compact-a4-frame img {
  display: block !important;
  width: 100% !important;
  height: 100% !important;
  max-width: none !important;
  max-height: none !important;
  object-fit: contain !important;
  object-position: top center !important;
  border-radius: 1.05rem !important;
  background: #ffffff !important;
  box-shadow: 0 8px 20px rgba(15, 23, 42, 0.12) !important;
}

.pub-visual-caption,
.pub-preview-caption,
.pub-card-caption,
.pub-visual-frame figcaption,
.pub-final-a4-thumb-frame figcaption {
  display: none !important;
}

@media (max-width: 980px) {
  .pub-visual-card {
    grid-template-columns: 1fr !important;
  }
  .pub-visual-frame,
  .pub-visual-frame.pub-final-a4-thumb-frame,
  .pub-final-a4-thumb-frame,
  .pub-firstpage-crop-frame,
  .pub-a4-page-frame,
  .pub-compact-a4-frame {
    width: min(72vw, 275px) !important;
  }
}

/* === Publications final compact A4 thumbnail v13 END === */
'''
css = css.rstrip() + final_css + '\n'
css_path.write_text(css, encoding='utf-8')

print('Updated publications.html and assets/css/style.css')
print('Final frame: compact A4 ratio thumbnail, not full-page height')
