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
    raise SystemExit("The Research Area 1 v30 HTML block was not found in index.html. Run the v30 script first, then run this width patch.")

css = CSS.read_text(encoding="utf-8", errors="ignore")

css_block = """
/* === Homepage research area 1 inertial v31 width refinement START === */
.home-research-area-map{
  width:min(1180px,calc(100% - 28px));
  margin:54px auto 44px;
}
.research-area-map-heading{
  max-width:980px;
  margin:0 auto 22px;
  text-align:center;
}
.research-area-map-heading h2{
  margin:.15rem 0 .5rem;
  color:#082d49;
  font-size:clamp(1.85rem,2.7vw,2.55rem);
  line-height:1.12;
  letter-spacing:-.04em;
}
.research-area-map-heading p:not(.eyebrow){
  color:#607589;
  font-size:.98rem;
  line-height:1.68;
}
.research-area-one-card{
  display:grid;
  gap:18px;
  padding:clamp(18px,2vw,24px);
  border-radius:30px;
  background:radial-gradient(circle at 82% 16%,rgba(79,196,211,.13),transparent 34%),linear-gradient(180deg,rgba(255,255,255,.98),rgba(248,252,255,.98));
  border:1px solid rgba(130,165,194,.25);
  box-shadow:0 20px 46px rgba(20,45,74,.08);
}
.research-area-label-row{
  display:flex;
  flex-wrap:wrap;
  gap:8px;
  align-items:center;
  margin-bottom:.72rem;
}
.research-area-index,.research-area-chip{
  display:inline-flex;
  align-items:center;
  min-height:30px;
  padding:.42rem .74rem;
  border-radius:999px;
  border:1px solid rgba(79,159,187,.24);
  line-height:1;
}
.research-area-index{
  background:linear-gradient(135deg,rgba(84,202,213,.20),rgba(149,118,246,.12));
  color:#084f72;
  font-size:.78rem;
  font-weight:800;
}
.research-area-chip{
  background:rgba(83,197,213,.10);
  color:#0b6380;
  font-size:.76rem;
  font-weight:700;
}
.research-area-one-card h3{
  margin:0;
  color:#073d63;
  font-size:clamp(1.55rem,2.45vw,2.3rem);
  line-height:1.12;
  letter-spacing:-.04em;
}
.research-area-text-grid{
  display:grid;
  grid-template-columns:minmax(0,1.12fr) minmax(0,.88fr);
  gap:14px;
}
.research-area-text-box{
  padding:15px 16px;
  border-radius:20px;
  background:linear-gradient(180deg,rgba(239,247,251,.96),rgba(249,252,255,.98));
  border:1px solid rgba(127,160,186,.21);
}
.research-area-text-box.difficulty-box{
  background:linear-gradient(180deg,rgba(245,242,255,.92),rgba(251,249,255,.98));
  border-color:rgba(148,132,200,.18);
}
.research-area-text-box h4,.research-area-works-row h4{
  margin:0 0 .45rem;
  color:#0b5074;
  font-size:.92rem;
  line-height:1.25;
}
.research-area-text-box p{
  margin:0;
  color:#4c6378;
  font-size:.92rem;
  line-height:1.58;
}
.research-area-small-tags{
  display:flex;
  flex-wrap:wrap;
  gap:7px;
  margin-top:.75rem;
}
.research-area-small-tags span{
  padding:.32rem .58rem;
  border-radius:999px;
  background:rgba(232,239,245,.92);
  border:1px solid rgba(147,171,192,.18);
  color:#51677a;
  font-size:.72rem;
  font-weight:600;
}
.research-area-visual-grid{
  display:grid;
  grid-template-columns:minmax(0,1.74fr) minmax(280px,.76fr);
  gap:14px;
  align-items:start;
}
.research-area-visual{
  margin:0;
  overflow:hidden;
  border-radius:24px;
  background:#fff;
  border:1px solid rgba(126,159,186,.22);
  box-shadow:0 14px 30px rgba(19,45,74,.075);
}
.research-area-visual img{
  display:block;
  width:100%;
  height:auto;
  background:#fff;
}
.research-area-visual.side-visual{
  max-width:390px;
}
.research-area-works-row{
  padding:14px 16px;
  border-radius:20px;
  background:linear-gradient(180deg,rgba(255,255,255,.84),rgba(247,250,253,.94));
  border:1px solid rgba(127,160,186,.18);
}
.research-area-works-row ul{
  margin:0;
  padding-left:1.05rem;
  columns:2;
  column-gap:2rem;
}
.research-area-works-row li{
  break-inside:avoid;
  margin:0 0 .35rem;
  color:#607488;
  font-size:.82rem;
  line-height:1.42;
}
.research-area-works-row a,.research-area-works-row a:visited{
  color:#035083;
  text-decoration:none;
  font-weight:400!important;
}
.research-area-works-row a:hover{
  color:#00709c;
  text-decoration:underline;
}
.research-area-works-row span{
  color:#7f90a2;
}
@media(max-width:960px){
  .research-area-text-grid,.research-area-visual-grid{grid-template-columns:1fr}
  .research-area-visual.side-visual{max-width:100%}
  .research-area-works-row ul{columns:1}
}
@media(max-width:640px){
  .home-research-area-map{width:min(100%,calc(100% - 18px));margin:40px auto 30px}
  .research-area-one-card{border-radius:24px}
  .research-area-visual{border-radius:18px}
}
/* === Homepage research area 1 inertial v31 width refinement END === */
"""

# Remove both the old v30 block and any previous v31 block, then append v31.
css = re.sub(
    r'/\* === Homepage research area 1 inertial v30 START === \*/.*?/\* === Homepage research area 1 inertial v30 END === \*/',
    '',
    css,
    flags=re.S,
)
css = re.sub(
    r'/\* === Homepage research area 1 inertial v31 width refinement START === \*/.*?/\* === Homepage research area 1 inertial v31 width refinement END === \*/',
    '',
    css,
    flags=re.S,
)

CSS.write_text(css.rstrip() + "\n\n" + css_block.strip() + "\n", encoding="utf-8")
print("Done: widened Research Area 1 container to match the main homepage width.")
