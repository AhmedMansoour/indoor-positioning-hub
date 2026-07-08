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
m = re.search(area_pat, html, flags=re.S)
if not m:
    raise SystemExit("Research Area 1 v30 block was not found. Run the v30 package first, then run this v34 fix.")

area_block = m.group(1).strip()

# Undo the v33 placement change: remove Research Area 1 from wherever it is now.
html = re.sub(area_pat, "\n", html, flags=re.S)

# Put it back in the original v30-style position, just before the Publication Access content marker.
# The CSS full-bleed technique below will allow it to visually match the upper wide area.
inserted = False
for marker in ['<p class="eyebrow">Publication access</p>', '<h2>Find papers, PDFs, citation records, and visual explanations</h2>', '<footer']:
    pos = html.find(marker)
    if pos != -1:
        html = html[:pos] + "\n" + area_block + "\n" + html[pos:]
        inserted = True
        break

if not inserted:
    pos = html.rfind("</main>")
    html = html[:pos] + "\n" + area_block + "\n" + html[pos:] if pos != -1 else html.rstrip() + "\n" + area_block + "\n"

INDEX.write_text(html, encoding="utf-8")

# Remove broken/old override blocks. Keep the approved v30 design block.
for pat in [
    r'/\* === Homepage research area 1 inertial v31 width refinement START === \*/.*?/\* === Homepage research area 1 inertial v31 width refinement END === \*/',
    r'/\* === Homepage research area 1 full-width v32 START === \*/.*?/\* === Homepage research area 1 full-width v32 END === \*/',
    r'/\* === Homepage research area 1 placement and width v33 START === \*/.*?/\* === Homepage research area 1 placement and width v33 END === \*/',
    r'/\* === Homepage research area 1 fullbleed v34 START === \*/.*?/\* === Homepage research area 1 fullbleed v34 END === \*/',
]:
    css = re.sub(pat, "", css, flags=re.S)

css_block = """
/* === Homepage research area 1 fullbleed v34 START === */
/* Keep the approved v30 design, remove v33 placement damage, and make the area visually match the wide upper homepage section. */
.home-research-area-map{
  width:min(1580px,calc(100vw - 16px)) !important;
  max-width:min(1580px,calc(100vw - 16px)) !important;
  margin-top:54px !important;
  margin-bottom:44px !important;
  margin-left:50% !important;
  margin-right:0 !important;
  transform:translateX(-50%) !important;
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
  grid-template-columns:minmax(0,1.82fr) minmax(300px,.72fr) !important;
}
.research-area-visual.side-visual{
  max-width:440px !important;
}
@media(max-width:960px){
  .home-research-area-map{
    width:min(100%,calc(100% - 18px)) !important;
    max-width:min(100%,calc(100% - 18px)) !important;
    margin-left:auto !important;
    margin-right:auto !important;
    transform:none !important;
  }
  .research-area-text-grid,
  .research-area-visual-grid{
    grid-template-columns:1fr !important;
  }
  .research-area-visual.side-visual{
    max-width:100% !important;
  }
}
/* === Homepage research area 1 fullbleed v34 END === */
"""

CSS.write_text(css.rstrip() + "\n\n" + css_block.strip() + "\n", encoding="utf-8")
print("Done: removed the v33 placement change and applied a safe full-width visual fix for Research Area 1.")
