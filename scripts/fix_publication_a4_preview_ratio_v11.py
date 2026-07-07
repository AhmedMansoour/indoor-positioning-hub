from pathlib import Path
import re

ROOT = Path(__file__).resolve().parents[1]
html_path = ROOT / "publications.html"
css_path = ROOT / "assets" / "css" / "style.css"

if not html_path.exists():
    raise SystemExit(f"Missing {html_path}. Run this script from the repository root structure.")
if not css_path.exists():
    raise SystemExit(f"Missing {css_path}. Run this script after extracting the package into the repository root.")

html = html_path.read_text(encoding="utf-8", errors="ignore")

# Use a single stable class for the paper-page preview frame.
html = html.replace("pub-firstpage-crop-frame", "pub-a4-page-frame")
html = html.replace("pub-visual-frame", "pub-a4-page-frame")

# Restore full first-page previews instead of cropped/tight previews.
# The container now has the A4 aspect ratio, so the image should not need artificial cropping.
html = html.replace("assets/previews-tight/", "assets/previews/")
html = re.sub(r'src="assets/previews/([^".]+)\.webp"', r'src="assets/previews/\1.png"', html)

# Remove leftover broken text accidentally left inside img tags by earlier patches.
html = re.sub(r'\s+Visual summary for [^>]+(?=></div>)', '', html)
html = re.sub(r'\s+Visual summary for [^>]+(?=>)', '', html)

html_path.write_text(html, encoding="utf-8")

css = css_path.read_text(encoding="utf-8", errors="ignore")

# Remove earlier v10/v11 blocks if they exist, then append one authoritative final block.
css = re.sub(r"/\* === Publications card preview height crop v10 START === \*/.*?/\* === Publications card preview height crop v10 END === \*/\s*", "", css, flags=re.S)
css = re.sub(r"/\* === Publications A4 first-page preview ratio v11 START === \*/.*?/\* === Publications A4 first-page preview ratio v11 END === \*/\s*", "", css, flags=re.S)

css_block = r'''
/* === Publications A4 first-page preview ratio v11 START === */
/*
   Final publication-card preview behavior:
   - the right-side figure box is a real A4 portrait thumbnail, 210:297;
   - the box height is determined by its width, not by the full card height;
   - the first page fills the box without the stretched white panel underneath;
   - the image is not zoomed out by a tall frame.
*/
.pub-visual-card,
.pub-card.pub-visual-card {
  align-items: start !important;
  grid-template-columns: minmax(0, 1fr) clamp(245px, 24vw, 330px) !important;
  column-gap: clamp(1.2rem, 2.2vw, 2.1rem) !important;
}

.pub-visual-side,
.pub-card-visual,
.pub-card-media,
.pub-figure-panel,
.pub-preview-side {
  align-self: start !important;
  min-height: 0 !important;
  height: auto !important;
  display: flex !important;
  justify-content: center !important;
  align-items: flex-start !important;
}

.pub-a4-page-frame,
.pub-visual-frame,
.pub-firstpage-crop-frame {
  width: 100% !important;
  max-width: 330px !important;
  aspect-ratio: 210 / 297 !important;
  height: auto !important;
  min-height: 0 !important;
  max-height: none !important;
  padding: 0 !important;
  margin: 0 !important;
  overflow: hidden !important;
  display: block !important;
  background: #ffffff !important;
  border: 1px solid rgba(37, 99, 235, 0.16) !important;
  border-radius: 18px !important;
  box-shadow: 0 18px 40px rgba(15, 23, 42, 0.12) !important;
}

.pub-a4-page-frame img,
.pub-visual-frame img,
.pub-firstpage-crop-frame img {
  width: 100% !important;
  height: 100% !important;
  display: block !important;
  object-fit: cover !important;
  object-position: top center !important;
  margin: 0 !important;
  padding: 0 !important;
  border: 0 !important;
  border-radius: inherit !important;
  background: #ffffff !important;
}

/* Neutralize older preview-frame stretching rules. */
.pub-visual-frame::before,
.pub-firstpage-crop-frame::before,
.pub-a4-page-frame::before,
.pub-visual-caption,
.pub-preview-caption {
  display: none !important;
}

@media (max-width: 900px) {
  .pub-visual-card,
  .pub-card.pub-visual-card {
    grid-template-columns: 1fr !important;
  }

  .pub-a4-page-frame,
  .pub-visual-frame,
  .pub-firstpage-crop-frame {
    width: min(100%, 330px) !important;
    margin: 0 auto !important;
  }
}
/* === Publications A4 first-page preview ratio v11 END === */
'''

css = css.rstrip() + "\n\n" + css_block.lstrip()
css_path.write_text(css, encoding="utf-8")

print("Applied v11 A4 preview-ratio fix.")
print("- publications.html now uses assets/previews/<slug>.png")
print("- preview frame class is pub-a4-page-frame")
print("- CSS forces a 210:297 A4 portrait box with no full-card-height stretching")
