from pathlib import Path
import re

INDEX = Path("index.html")
CSS = Path("assets/css/style.css")

if not INDEX.exists():
    raise SystemExit("index.html not found. Run this script from the repository root.")
if not CSS.exists():
    raise SystemExit("assets/css/style.css not found. Run this script from the repository root.")

html = INDEX.read_text(encoding="utf-8", errors="ignore")
css = CSS.read_text(encoding="utf-8", errors="ignore")

area_pat = r'\n?\s*(<!-- === Homepage research area 1 inertial v30 START === -->.*?<!-- === Homepage research area 1 inertial v30 END === -->)\s*\n?'
match = re.search(area_pat, html, flags=re.S)

if not match:
    raise SystemExit("Research Area 1 block was not found. Run the v30 package first, then run this v33 fix.")

area_block = match.group(1).strip()

# Remove the current block wherever it was inserted.
html_without_area = re.sub(area_pat, "\n", html, flags=re.S)

# The previous scripts could insert Research Area 1 inside the Publication Access section,
# because they searched for the heading text. That prevents the section from growing beyond
# the parent container. This script inserts it BEFORE the whole Publication Access section.
pub_pos = html_without_area.lower().find("publication access")

if pub_pos != -1:
    section_start = html_without_area.rfind("<section", 0, pub_pos)
    if section_start != -1:
        html_fixed = html_without_area[:section_start] + "\n" + area_block + "\n\n" + html_without_area[section_start:]
    else:
        html_fixed = html_without_area[:pub_pos] + "\n" + area_block + "\n\n" + html_without_area[pub_pos:]
else:
    main_end = html_without_area.rfind("</main>")
    if main_end != -1:
        html_fixed = html_without_area[:main_end] + "\n" + area_block + "\n" + html_without_area[main_end:]
    else:
        html_fixed = html_without_area.rstrip() + "\n" + area_block + "\n"

INDEX.write_text(html_fixed, encoding="utf-8")

# Remove older override blocks and append the final one.
for pat in [
    r'/\* === Homepage research area 1 inertial v31 width refinement START === \*/.*?/\* === Homepage research area 1 inertial v31 width refinement END === \*/',
    r'/\* === Homepage research area 1 full-width v32 START === \*/.*?/\* === Homepage research area 1 full-width v32 END === \*/',
    r'/\* === Homepage research area 1 placement and width v33 START === \*/.*?/\* === Homepage research area 1 placement and width v33 END === \*/',
]:
    css = re.sub(pat, "", css, flags=re.S)

css_block = """
/* === Homepage research area 1 placement and width v33 START === */
/* v33 fixes the real issue: Research Area 1 must be a standalone section,
   not nested inside Publication Access. These widths then apply correctly. */
.home-research-area-map{
  width:min(1580px,calc(100% - 16px)) !important;
  max-width:min(1580px,calc(100% - 16px)) !important;
  margin:54px auto 44px !important;
  box-sizing:border-box !important;
}
.research-area-map-heading{
  max-width:1180px !important;
}
.research-area-one-card{
  width:100% !important;
  max-width:none !important;
  box-sizing:border-box !important;
}
.research-area-text-grid{
  grid-template-columns:minmax(0,1.12fr) minmax(0,.88fr) !important;
}
.research-area-visual-grid{
  grid-template-columns:minmax(0,1.85fr) minmax(320px,.72fr) !important;
}
.research-area-visual.side-visual{
  max-width:460px !important;
}
@media(max-width:960px){
  .home-research-area-map{
    width:min(100%,calc(100% - 18px)) !important;
    max-width:min(100%,calc(100% - 18px)) !important;
  }
  .research-area-text-grid,
  .research-area-visual-grid{
    grid-template-columns:1fr !important;
  }
  .research-area-visual.side-visual{
    max-width:100% !important;
  }
}
/* === Homepage research area 1 placement and width v33 END === */
"""

CSS.write_text(css.rstrip() + "\n\n" + css_block.strip() + "\n", encoding="utf-8")
print("Done: moved Research Area 1 outside Publication Access and matched its width to the upper wide section.")
