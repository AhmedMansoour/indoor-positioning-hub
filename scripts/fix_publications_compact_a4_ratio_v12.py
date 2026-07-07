from pathlib import Path
import re

ROOT = Path(__file__).resolve().parents[1]
pub = ROOT / "publications.html"
css = ROOT / "assets" / "css" / "style.css"

if not pub.exists():
    raise SystemExit("publications.html not found. Run this script from the repository scripts folder.")
if not css.exists():
    raise SystemExit("assets/css/style.css not found.")

html = pub.read_text(encoding="utf-8", errors="ignore")

# 1) Make every publication image wrapper a compact A4-ratio thumbnail frame.
#    This removes the earlier full-height/crop classes and replaces them with one clean class.
def fix_frame_class(match):
    cls = match.group(1)
    classes = cls.split()
    remove = {
        "pub-a4-page-frame",
        "pub-firstpage-crop-frame",
        "pub-crop-frame",
        "pub-tight-preview-frame",
        "pub-preview-tight-frame",
    }
    classes = [c for c in classes if c not in remove]
    if "pub-visual-frame" not in classes:
        classes.insert(0, "pub-visual-frame")
    if "pub-compact-a4-frame" not in classes:
        classes.append("pub-compact-a4-frame")
    return f'<div class="{" ".join(classes)}">'

html = re.sub(r'<div class="([^"]*\bpub-visual-frame\b[^"]*)">', fix_frame_class, html)

# 2) Use the normal first-page previews, not the cropped/zoomed tight previews.
#    The frame now handles the display ratio, so the image should remain the true first page.
html = html.replace("assets/previews-tight/", "assets/previews/")

# 3) Clean leftover accidental text inside <img> tags from earlier scripts.
html = re.sub(r'\s+Visual summary for [^>]+(?=></div>)', '', html)

# 4) Ensure no older wrapper class remains in the HTML.
html = re.sub(r'\s+pub-a4-page-frame', '', html)
html = re.sub(r'\s+pub-firstpage-crop-frame', '', html)

pub.write_text(html, encoding="utf-8")

css_text = css.read_text(encoding="utf-8", errors="ignore")

# Remove only the previous v11 override block if present, because it caused full-size A4 cards.
css_text = re.sub(
    r'/\* === Publications A4 first-page preview ratio v11 START === \*/.*?/\* === Publications A4 first-page preview ratio v11 END === \*/\s*',
    '',
    css_text,
    flags=re.S
)

# Remove v10 crop override block if present, to prevent hidden/zoomed thumbnails from fighting v12.
css_text = re.sub(
    r'/\* === Publications card preview height crop v10 START === \*/.*?/\* === Publications card preview height crop v10 END === \*/\s*',
    '',
    css_text,
    flags=re.S
)

v12 = """
/* === Publications compact A4 thumbnail ratio v12 START === */
/*
   Senior layout fix:
   The right-side preview is a compact paper thumbnail, not a full-size A4 page.
   The container preserves the A4 portrait ratio (210:297), but its width is
   intentionally capped so the publication card remains balanced.
*/

.pub-visual-card,
.publication-visual-card,
.pub-card {
  align-items: start !important;
}

/* Main two-column publication card layout */
.pub-visual-card {
  display: grid !important;
  grid-template-columns: minmax(0, 1fr) clamp(190px, 18vw, 255px) !important;
  gap: clamp(1.25rem, 2vw, 2.25rem) !important;
}

/* Right-side A4 thumbnail frame */
.pub-visual-frame.pub-compact-a4-frame,
.pub-compact-a4-frame {
  width: clamp(190px, 18vw, 255px) !important;
  max-width: 255px !important;
  aspect-ratio: 210 / 297 !important;
  height: auto !important;
  min-height: 0 !important;
  max-height: none !important;
  align-self: start !important;
  justify-self: end !important;
  display: block !important;
  box-sizing: border-box !important;
  padding: 10px !important;
  overflow: hidden !important;
  border-radius: 24px !important;
  background: linear-gradient(145deg, rgba(255,255,255,0.96), rgba(236,246,251,0.78)) !important;
  border: 1px solid rgba(124, 166, 190, 0.26) !important;
  box-shadow: 0 18px 45px rgba(15, 45, 70, 0.10) !important;
}

/* The image fills the compact A4 frame without becoming a huge column */
.pub-visual-frame.pub-compact-a4-frame img,
.pub-compact-a4-frame img {
  display: block !important;
  width: 100% !important;
  height: 100% !important;
  max-width: none !important;
  max-height: none !important;
  object-fit: cover !important;
  object-position: top center !important;
  border-radius: 16px !important;
  background: #fff !important;
  box-shadow: 0 8px 24px rgba(10, 33, 55, 0.10) !important;
}

/* Prevent older preview wrappers from stretching the card height */
.pub-visual-side,
.pub-preview-side,
.pub-card-visual,
.pub-visual-col {
  align-self: start !important;
  justify-self: end !important;
  height: auto !important;
  min-height: 0 !important;
  max-height: none !important;
}

/* Remove any caption space left by earlier versions */
.pub-visual-caption,
.pub-preview-caption {
  display: none !important;
}

/* Mobile layout: keep the A4 ratio but let the thumbnail sit under the text */
@media (max-width: 900px) {
  .pub-visual-card {
    grid-template-columns: 1fr !important;
  }

  .pub-visual-frame.pub-compact-a4-frame,
  .pub-compact-a4-frame {
    width: min(72vw, 260px) !important;
    max-width: 260px !important;
    justify-self: start !important;
    margin-top: 1rem !important;
  }

  .pub-visual-side,
  .pub-preview-side,
  .pub-card-visual,
  .pub-visual-col {
    justify-self: start !important;
  }
}
/* === Publications compact A4 thumbnail ratio v12 END === */
"""

if "Publications compact A4 thumbnail ratio v12 START" not in css_text:
    css_text = css_text.rstrip() + "\n\n" + v12 + "\n"

css.write_text(css_text, encoding="utf-8")

print("Applied v12 compact A4 thumbnail fix.")
print("Updated publications.html and assets/css/style.css.")
print("The preview frame now keeps A4 ratio, but its width is capped to a compact thumbnail size.")
