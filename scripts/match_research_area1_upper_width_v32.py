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
    raise SystemExit("Research Area 1 HTML was not found in index.html. Run the v30 package first.")

css = CSS.read_text(encoding="utf-8", errors="ignore")

# Remove older width override if repeated.
css = re.sub(
    r'/\* === Homepage research area 1 full-width v32 START === \*/.*?/\* === Homepage research area 1 full-width v32 END === \*/',
    '',
    css,
    flags=re.S,
)

css_block = """
/* === Homepage research area 1 full-width v32 START === */
/* Match Research Area 1 width with the wide two-card section above it. */
.home-research-area-map{
  width:min(1580px,calc(100% - 16px)) !important;
  max-width:min(1580px,calc(100% - 16px)) !important;
  margin:54px auto 44px !important;
}
.research-area-map-heading{
  max-width:1180px !important;
}
.research-area-one-card{
  width:100% !important;
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
  }
  .research-area-text-grid,
  .research-area-visual-grid{
    grid-template-columns:1fr !important;
  }
  .research-area-visual.side-visual{
    max-width:100% !important;
  }
}
/* === Homepage research area 1 full-width v32 END === */
"""

CSS.write_text(css.rstrip() + "\n\n" + css_block.strip() + "\n", encoding="utf-8")
print("Done: Research Area 1 now uses the same wide page span as the upper two-card section.")
