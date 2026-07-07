from pathlib import Path
import re
import sys

ROOT = Path.cwd()
CSS_PATH = ROOT / "assets" / "css" / "style.css"
PUBS_PATH = ROOT / "publications.html"
PREVIEW_DIR = ROOT / "assets" / "previews"
TIGHT_DIR = ROOT / "assets" / "previews-tight"
MARKER_START = "/* === Publications first-page preview whitespace fix v9 START === */"
MARKER_END = "/* === Publications first-page preview whitespace fix v9 END === */"

CSS_BLOCK = f"""
{MARKER_START}
/*
   Makes each publication-card preview behave like a paper-page thumbnail,
   not a stretched decorative panel. The right visual column now hugs the
   image height, and the image starts at the top of its rounded frame.
*/
.publications-visual-page .pub-visual-card,
.pub-visual-card,
.publication-visual-card {{
  align-items: start !important;
}}

.publications-visual-page .pub-visual-media,
.publications-visual-page .pub-visual-panel,
.publications-visual-page .pub-card-visual,
.publications-visual-page .pub-preview-panel,
.publications-visual-page .pub-visual-right,
.pub-visual-media,
.pub-visual-panel,
.pub-card-visual,
.pub-preview-panel,
.pub-visual-right {{
  align-self: start !important;
  height: auto !important;
  min-height: 0 !important;
  max-height: none !important;
}}

.publications-visual-page .pub-visual-frame,
.publications-visual-page .pub-preview-frame,
.publications-visual-page .pub-card-preview,
.publications-visual-page .pub-figure-frame,
.pub-visual-frame,
.pub-preview-frame,
.pub-card-preview,
.pub-figure-frame {{
  display: block !important;
  height: auto !important;
  min-height: 0 !important;
  max-height: none !important;
  align-items: flex-start !important;
  justify-content: flex-start !important;
  padding: clamp(10px, 1.15vw, 18px) !important;
  overflow: hidden !important;
}}

.publications-visual-page .pub-visual-frame img,
.publications-visual-page .pub-preview-frame img,
.publications-visual-page .pub-card-preview img,
.publications-visual-page .pub-figure-frame img,
.publications-visual-page .pub-visual-media img,
.publications-visual-page img.pub-visual-image,
.pub-visual-frame img,
.pub-preview-frame img,
.pub-card-preview img,
.pub-figure-frame img,
.pub-visual-media img,
img.pub-visual-image {{
  display: block !important;
  width: 100% !important;
  height: auto !important;
  max-height: none !important;
  object-fit: contain !important;
  object-position: top center !important;
  margin: 0 !important;
  border-radius: 16px !important;
}}

.publications-visual-page .pub-visual-caption,
.publications-visual-page .pub-preview-caption,
.pub-visual-caption,
.pub-preview-caption {{
  display: none !important;
}}

@media (min-width: 980px) {{
  .publications-visual-page .pub-visual-card,
  .pub-visual-card,
  .publication-visual-card {{
    grid-template-columns: minmax(0, 1fr) minmax(270px, 0.34fr) !important;
  }}
}}
{MARKER_END}
"""


def replace_block(text: str, block: str) -> str:
    pattern = re.compile(re.escape(MARKER_START) + r".*?" + re.escape(MARKER_END), re.S)
    if pattern.search(text):
        return pattern.sub(block.strip(), text)
    return text.rstrip() + "\n\n" + block.strip() + "\n"


def append_css():
    if not CSS_PATH.exists():
        raise FileNotFoundError(f"Missing {CSS_PATH}")
    text = CSS_PATH.read_text(encoding="utf-8", errors="ignore")
    CSS_PATH.write_text(replace_block(text, CSS_BLOCK), encoding="utf-8")
    print(f"[OK] CSS preview layout overrides written to {CSS_PATH}")


def find_bottom_content_row(img):
    """Return bottom row index containing meaningful non-white content."""
    rgb = img.convert("RGB")
    w, h = rgb.size
    pix = rgb.load()
    # A row must have enough non-white pixels, not only one noise pixel.
    min_count = max(10, int(w * 0.0025))
    # Text and journal logos are usually much darker than white. 248 keeps light gray rules.
    white_threshold = 248
    last = h - 1
    for y in range(h - 1, -1, -1):
        count = 0
        # Step by 2 for speed on large PNGs.
        for x in range(0, w, 2):
            r, g, b = pix[x, y]
            if r < white_threshold or g < white_threshold or b < white_threshold:
                count += 1
                if count >= min_count:
                    return y
    return last


def crop_previews(overwrite: bool = False):
    try:
        from PIL import Image
    except ImportError:
        print("[WARN] Pillow is not installed, so previews were not cropped.")
        print("       Run: python -m pip install pillow")
        print("       Then rerun: python scripts\\fix_publication_preview_whitespace_v9.py --crop")
        return []

    if not PREVIEW_DIR.exists():
        print(f"[WARN] Preview directory not found: {PREVIEW_DIR}")
        return []

    TIGHT_DIR.mkdir(parents=True, exist_ok=True)
    written = []
    for src in sorted(PREVIEW_DIR.glob("*.png")):
        out = TIGHT_DIR / f"{src.stem}.webp"
        if out.exists() and not overwrite:
            written.append(out)
            continue
        try:
            with Image.open(src) as im:
                im = im.convert("RGB")
                w, h = im.size
                bottom = find_bottom_content_row(im)
                # Keep a small paper margin after the last meaningful content row.
                pad = max(28, int(h * 0.035))
                new_bottom = min(h, bottom + pad)
                # Avoid over-cropping unusual first pages.
                if new_bottom < int(h * 0.52):
                    new_bottom = int(h * 0.52)
                if h - new_bottom < max(60, int(h * 0.05)):
                    # Nothing meaningful to crop.
                    cropped = im
                else:
                    cropped = im.crop((0, 0, w, new_bottom))
                cropped.save(out, "WEBP", quality=90, method=6)
                written.append(out)
                print(f"[OK] {src.name}: {w}x{h} -> {cropped.size[0]}x{cropped.size[1]}")
        except Exception as exc:
            print(f"[WARN] Could not crop {src}: {exc}")
    return written


def update_publications_html(cropped_files):
    if not PUBS_PATH.exists():
        raise FileNotFoundError(f"Missing {PUBS_PATH}")
    if not cropped_files:
        print("[INFO] No cropped preview files available; HTML image paths were not changed.")
        return

    text = PUBS_PATH.read_text(encoding="utf-8", errors="ignore")
    changed = 0
    for out in cropped_files:
        slug = out.stem
        candidates = [
            f"assets/previews/{slug}.png",
            f"./assets/previews/{slug}.png",
            f"/assets/previews/{slug}.png",
            f"assets/previews/{slug}.jpg",
            f"assets/previews/{slug}.jpeg",
        ]
        replacement = f"assets/previews-tight/{slug}.webp"
        for cand in candidates:
            if cand in text:
                text = text.replace(cand, replacement)
                changed += 1
    PUBS_PATH.write_text(text, encoding="utf-8")
    print(f"[OK] Updated {changed} publication preview references in {PUBS_PATH}")


def main():
    crop = "--no-crop" not in sys.argv
    overwrite = "--overwrite" in sys.argv or "--overwrite-previews" in sys.argv
    append_css()
    if crop:
        files = crop_previews(overwrite=overwrite)
        update_publications_html(files)
    print("[DONE] Publication preview whitespace fix v9 complete.")


if __name__ == "__main__":
    main()
