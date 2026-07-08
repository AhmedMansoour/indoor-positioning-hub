from pathlib import Path
import re

CSS = Path("assets/css/style.css")
INDEX = Path("index.html")

if not CSS.exists():
    raise SystemExit("assets/css/style.css not found. Run this script from the repository root.")
if not INDEX.exists():
    raise SystemExit("index.html not found. Run this script from the repository root.")

html = INDEX.read_text(encoding="utf-8", errors="ignore")
if "Homepage research area 1 inertial v30 START" not in html:
    raise SystemExit("Research Area 1 block was not found. Run the v30/v35 package first.")

css = CSS.read_text(encoding="utf-8", errors="ignore")

# Remove previous v36 if repeated.
css = re.sub(
    r'/\* === Homepage research area 1 balanced width v36 START === \*/.*?/\* === Homepage research area 1 balanced width v36 END === \*/',
    "",
    css,
    flags=re.S,
)

css_block = """
/* === Homepage research area 1 balanced width v36 START === */
/* v36 reduces the v35 wide layout so Research Area 1 aligns better with the upper homepage blocks. */
.home-research-area-map{
  width:min(1480px,calc(100% - 56px)) !important;
  max-width:min(1480px,calc(100% - 56px)) !important;
  margin-left:auto !important;
  margin-right:auto !important;
}
.research-area-map-heading{
  max-width:1080px !important;
}
.research-area-visual-grid{
  grid-template-columns:minmax(0,1.72fr) minmax(280px,.76fr) !important;
}
.research-area-visual.side-visual{
  max-width:410px !important;
}
@media(max-width:960px){
  .home-research-area-map{
    width:min(100%,calc(100% - 18px)) !important;
    max-width:min(100%,calc(100% - 18px)) !important;
  }
  .research-area-visual-grid{
    grid-template-columns:1fr !important;
  }
  .research-area-visual.side-visual{
    max-width:100% !important;
  }
}
/* === Homepage research area 1 balanced width v36 END === */
"""

CSS.write_text(css.rstrip() + "\n\n" + css_block.strip() + "\n", encoding="utf-8")
print("Done: reduced Research Area 1 width from the very-wide v35 layout to a balanced page width.")
