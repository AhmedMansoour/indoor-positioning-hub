from pathlib import Path
import re

ROOT = Path.cwd()
PUBS = ROOT / "publications.html"
CSS = ROOT / "assets" / "css" / "style.css"

MARKER_START = "/* === Publications card preview height crop v10 START === */"
MARKER_END = "/* === Publications card preview height crop v10 END === */"

CSS_BLOCK = f"""
{MARKER_START}
/*
  v10: The publication image column is a top-anchored paper-page preview,
  not a stretched card-height panel. The frame uses a controlled preview
  ratio and crops only the lower part of the page image, which removes the
  visual blank area while preserving the paper identity/title at the top.
*/
.pub-visual-card,
.publication-visual-card,
.publications-visual-page .pub-visual-card {{
  align-items: flex-start !important;
}}

@media (min-width: 960px) {{
  .pub-visual-card,
  .publication-visual-card,
  .publications-visual-page .pub-visual-card {{
    grid-template-columns: minmax(0, 1fr) minmax(215px, 270px) !important;
    gap: clamp(1.25rem, 2.1vw, 2.15rem) !important;
  }}
}}

.pub-visual-card > .pub-firstpage-crop-frame,
.publication-visual-card > .pub-firstpage-crop-frame,
.pub-firstpage-crop-frame,
.publications-visual-page .pub-firstpage-crop-frame {{
  align-self: flex-start !important;
  justify-self: stretch !important;
  display: block !important;
  box-sizing: border-box !important;
  width: 100% !important;
  min-width: 0 !important;
  height: auto !important;
  min-height: 0 !important;
  max-height: none !important;
  aspect-ratio: 0.82 / 1 !important;
  padding: 8px !important;
  line-height: 0 !important;
  overflow: hidden !important;
  border-radius: 22px !important;
  background: linear-gradient(180deg, #f8fbff 0%, #eef6ff 100%) !important;
  border: 1px solid rgba(78, 126, 184, 0.18) !important;
  box-shadow: 0 14px 32px rgba(15, 42, 75, 0.10) !important;
}}

.pub-firstpage-crop-frame > img,
.pub-firstpage-crop-frame img.pub-firstpage-preview-img,
.publications-visual-page .pub-firstpage-crop-frame > img {{
  display: block !important;
  width: 100% !important;
  height: 100% !important;
  min-height: 0 !important;
  max-height: none !important;
  object-fit: cover !important;
  object-position: top center !important;
  margin: 0 !important;
  padding: 0 !important;
  border-radius: 15px !important;
  background: #ffffff !important;
}}

.pub-firstpage-crop-frame .pub-visual-caption,
.pub-firstpage-crop-frame .pub-preview-caption,
.pub-visual-caption,
.pub-preview-caption {{
  display: none !important;
}}

@media (max-width: 959px) {{
  .pub-visual-card,
  .publication-visual-card,
  .publications-visual-page .pub-visual-card {{
    grid-template-columns: 1fr !important;
  }}
  .pub-firstpage-crop-frame,
  .publications-visual-page .pub-firstpage-crop-frame {{
    width: min(100%, 330px) !important;
    justify-self: start !important;
    aspect-ratio: 0.82 / 1 !important;
  }}
}}
{MARKER_END}
"""


def replace_or_append_block(text: str, block: str) -> str:
    pattern = re.compile(re.escape(MARKER_START) + r".*?" + re.escape(MARKER_END), re.S)
    if pattern.search(text):
        return pattern.sub(block.strip(), text)
    return text.rstrip() + "\n\n" + block.strip() + "\n"


def add_frame_and_img_classes(html: str) -> str:
    # Remove leftover invalid human-readable text that may have been inserted into img tags.
    html = re.sub(r'\s+Visual summary for [^>]+(?=>)', '', html)

    # Add a dedicated frame class to every first-page visual frame.
    html = re.sub(
        r'<div class="pub-visual-frame(?![^"]*pub-firstpage-crop-frame)"',
        '<div class="pub-visual-frame pub-firstpage-crop-frame"',
        html,
    )

    # Add a dedicated image class inside those frames, preserving existing attributes.
    def repl(match: re.Match) -> str:
        before = match.group(1)
        attrs = match.group(2)
        after = match.group(3)
        if 'class=' in attrs:
            attrs = re.sub(r'class="([^"]*)"', lambda m: 'class="' + m.group(1) + ' pub-firstpage-preview-img"' if 'pub-firstpage-preview-img' not in m.group(1) else m.group(0), attrs)
        else:
            attrs = ' class="pub-firstpage-preview-img"' + attrs
        return before + attrs + after

    html = re.sub(
        r'(<div class="pub-visual-frame pub-firstpage-crop-frame">\s*<img)([^>]*)(>)',
        repl,
        html,
        flags=re.S,
    )
    return html


def main():
    if not PUBS.exists():
        raise FileNotFoundError(f"Missing {PUBS}")
    if not CSS.exists():
        raise FileNotFoundError(f"Missing {CSS}")

    html = PUBS.read_text(encoding="utf-8", errors="ignore")
    html2 = add_frame_and_img_classes(html)
    PUBS.write_text(html2, encoding="utf-8")

    css = CSS.read_text(encoding="utf-8", errors="ignore")
    CSS.write_text(replace_or_append_block(css, CSS_BLOCK), encoding="utf-8")

    frame_count = html2.count("pub-firstpage-crop-frame")
    img_count = html2.count("pub-firstpage-preview-img")
    print(f"[OK] Updated {PUBS}")
    print(f"[OK] Added/updated v10 CSS in {CSS}")
    print(f"[INFO] pub-firstpage-crop-frame count: {frame_count}")
    print(f"[INFO] pub-firstpage-preview-img count: {img_count}")
    print("[DONE] Publication card preview height/crop fix v10 complete.")


if __name__ == "__main__":
    main()
