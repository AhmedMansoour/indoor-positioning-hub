from pathlib import Path
import re, shutil

INDEX = Path("index.html")
CSS = Path("assets/css/style.css")
BUNDLE_SRC = Path(__file__).resolve().parent.parent / "bundle_assets" / "research-area3-v41"
ASSET_DST = Path("assets/home/research-area3-v41")

if not INDEX.exists():
    raise SystemExit("index.html not found. Run from repository root.")
if not CSS.exists():
    raise SystemExit("assets/css/style.css not found. Run from repository root.")
if not BUNDLE_SRC.exists():
    raise SystemExit("bundle_assets/research-area3-v41 not found. Extract the full zip first.")

ASSET_DST.mkdir(parents=True, exist_ok=True)
for item in BUNDLE_SRC.iterdir():
    if item.is_file():
        shutil.copy2(item, ASSET_DST / item.name)

html = INDEX.read_text(encoding="utf-8", errors="ignore")
css = CSS.read_text(encoding="utf-8", errors="ignore")

# Remove any previous Area 3 block to avoid duplicates.
for pat in [
    r'\n\s*<!-- === Homepage research area 3 seamless fusion v41 START === -->.*?<!-- === Homepage research area 3 seamless fusion v41 END === -->\s*\n',
]:
    html = re.sub(pat, "\n", html, flags=re.S | re.I)

section = """
<!-- === Homepage research area 3 seamless fusion v41 START === -->
<section class="home-area3-v41" id="research-area-3">
  <article class="area3-v41-card">
    <div class="area3-v41-title">
      <div class="area3-v41-labels">
        <span class="area3-index">Research Area 3</span>
        <span>Indoor–outdoor transition</span>
        <span>Multi-source fusion</span>
        <span>Seamless positioning</span>
      </div>
      <h3>Seamless Indoor–Outdoor Positioning and Multi-Source Fusion</h3>
    </div>

    <div class="area3-v41-top">
      <section class="area3-v41-box why-box">
        <h4>Why it matters</h4>
        <p>Indoor positioning should not break at the building entrance. Real users move through streets, entrances, semi-open spaces, corridors, elevators, staircases, lobbies, and indoor rooms, while the available positioning sources change continuously.</p>
        <p>GNSS provides an outdoor absolute reference, but it degrades near dense buildings and often fails indoors. Inertial positioning preserves motion continuity during signal outages, while Wi-Fi, BLE, barometer readings, map constraints, and indoor–outdoor awareness provide correction and context. This research area connects the relative-motion layer from inertial positioning with the absolute indoor reference from radio mapping to maintain a continuous trajectory across outdoor, transition, and indoor spaces.</p>
      </section>

      <figure class="area3-v41-figure">
        <img src="assets/home/research-area3-v41/seamless-indoor-outdoor-transition.webp" alt="Seamless outdoor, transition, and indoor positioning using GNSS, smartphone sensing, and indoor context across a building entrance" loading="lazy" decoding="async">
      </figure>
    </div>

    <section class="area3-v41-box difficulties-box area3-v41-wide">
      <h4>Core difficulties</h4>
      <ul>
        <li>GNSS degradation near buildings can introduce large position errors before the user reaches an indoor entrance.</li>
        <li>Indoor–outdoor transition is gradual, because covered entrances, semi-open spaces, lobbies, and corridors create mixed signal conditions.</li>
        <li>Sensor availability changes along the trajectory, since GNSS, Wi-Fi, BLE, IMU, barometer, and map constraints become useful at different moments.</li>
        <li>Fusion must judge source reliability, because a strong measurement is not always a trustworthy positioning cue.</li>
        <li>Vertical movement requires explicit handling when users pass through stairs, elevators, ramps, and multi-level indoor spaces.</li>
        <li>Seamless navigation requires transition awareness and source switching logic, not only point-by-point localization accuracy.</li>
      </ul>
    </section>

    <div class="area3-v41-works">
      <h4>Representative works</h4>
      <ul>
        <li><a href="publications/suns-seamless-ubiquitous-navigation-indoor-outdoor-awareness.html">SUNS: Seamless Ubiquitous Navigation System Based on GNSS, Wi-Fi, and MEMS Sensors</a> <span>(2022)</span></li>
        <li><a href="publications/gnss-positioning-aided-with-pdr-in-urban-areas.html">GNSS Positioning Aided with Pedestrian Dead Reckoning in Urban Areas</a> <span>(2026)</span></li>
        <li><a href="publications/tightly-coupled-bluetooth-enhanced-gnss-pdr-urban.html">Tightly Coupled Bluetooth Enhanced GNSS/PDR System for Pedestrian Navigation in Dense Urban Environments</a> <span>(2024)</span></li>
        <li><a href="publications/ac-hmm-azimuth-constrained-map-matching-urban-canyons.html">AC-HMM: Azimuth-Constrained Hidden Markov Model-Based Map Matching for Robust Pedestrian Positioning in Urban Canyons</a> <span>(2026)</span></li>
      </ul>
    </div>
  </article>
</section>
<!-- === Homepage research area 3 seamless fusion v41 END === -->
"""

# Insert Area 3 directly after Area 2.
area2_markers = [
    "<!-- === Homepage research area 2 fullwidth difficulties v40 END === -->",
    "<!-- === Homepage research area 2 session radio v39 END === -->",
]
inserted = False

for marker in area2_markers:
    pos = html.find(marker)
    if pos != -1:
        insert_at = pos + len(marker)
        html = html[:insert_at] + "\n\n" + section + html[insert_at:]
        inserted = True
        break

if not inserted:
    area1_markers = [
        "<!-- === Homepage research area 1 professor v38 END === -->",
        "<!-- === Homepage research area 1 reorganized v37 END === -->",
        "<!-- === Homepage research area 1 inertial v30 END === -->",
    ]
    for marker in area1_markers:
        pos = html.find(marker)
        if pos != -1:
            insert_at = pos + len(marker)
            html = html[:insert_at] + "\n\n" + section + html[insert_at:]
            inserted = True
            break

if not inserted:
    pub = re.search(r'<p\s+class=["\']eyebrow["\']>\s*Publication access\s*</p>', html, flags=re.I)
    if pub:
        section_start = html.rfind("<section", 0, pub.start())
        if section_start != -1:
            html = html[:section_start] + "\n" + section + "\n\n" + html[section_start:]
        else:
            html = html[:pub.start()] + "\n" + section + "\n" + html[pub.start():]
    else:
        main_end = html.rfind("</main>")
        html = html[:main_end] + "\n" + section + "\n" + html[main_end:] if main_end != -1 else html.rstrip() + "\n" + section + "\n"

INDEX.write_text(html, encoding="utf-8")

# Remove previous Area 3 CSS and append v41.
for pat in [
    r'/\* === Homepage research area 3 seamless fusion v41 START === \*/.*?/\* === Homepage research area 3 seamless fusion v41 END === \*/',
]:
    css = re.sub(pat, "", css, flags=re.S)

css_block = """
/* === Homepage research area 3 seamless fusion v41 START === */
.home-area3-v41{
  width:min(1180px,calc(100% - 56px));
  max-width:min(1180px,calc(100% - 56px));
  margin:28px auto 42px;
  box-sizing:border-box;
}
.area3-v41-card{
  display:grid;
  gap:18px;
  padding:22px;
  border-radius:30px;
  background:radial-gradient(circle at 80% 18%,rgba(79,196,211,.13),transparent 35%),linear-gradient(180deg,rgba(255,255,255,.98),rgba(248,252,255,.98));
  border:1px solid rgba(130,165,194,.25);
  box-shadow:0 20px 46px rgba(20,45,74,.08);
}
.area3-v41-labels{
  display:flex;
  flex-wrap:wrap;
  gap:8px;
  align-items:center;
  margin-bottom:.75rem;
}
.area3-v41-labels span{
  display:inline-flex;
  align-items:center;
  min-height:30px;
  padding:.42rem .74rem;
  border-radius:999px;
  background:rgba(83,197,213,.10);
  border:1px solid rgba(79,159,187,.24);
  color:#0b6380;
  font-size:.76rem;
  font-weight:700;
  line-height:1;
}
.area3-v41-labels .area3-index{
  background:linear-gradient(135deg,rgba(84,202,213,.20),rgba(149,118,246,.12));
  color:#084f72;
  font-weight:800;
}
.area3-v41-title h3{
  margin:0;
  color:#073d63;
  font-size:clamp(1.52rem,2.28vw,2.08rem);
  line-height:1.12;
  letter-spacing:-.04em;
}
.area3-v41-top{
  display:grid;
  grid-template-columns:minmax(0,.96fr) minmax(450px,1.04fr);
  gap:18px;
  align-items:start;
}
.area3-v41-box{
  padding:16px 17px;
  border-radius:20px;
  border:1px solid rgba(127,160,186,.21);
}
.area3-v41-box h4,
.area3-v41-works h4{
  margin:0 0 .55rem;
  color:#0b5074;
  font-size:.94rem;
  line-height:1.25;
}
.area3-v41-box p{
  margin:0 0 .65rem;
  color:#405b71;
  font-size:.92rem;
  line-height:1.58;
}
.area3-v41-box p:last-child{
  margin-bottom:0;
}
.area3-v41 .why-box{
  background:linear-gradient(180deg,rgba(239,247,251,.96),rgba(249,252,255,.98));
}
.area3-v41 .difficulties-box{
  background:linear-gradient(180deg,rgba(245,242,255,.92),rgba(251,249,255,.98));
  border-color:rgba(148,132,200,.18);
}
.area3-v41-wide{
  width:100%;
  box-sizing:border-box;
}
.area3-v41 .difficulties-box ul{
  margin:0;
  padding-left:1.08rem;
  columns:2;
  column-gap:2.2rem;
}
.area3-v41 .difficulties-box li{
  break-inside:avoid;
  margin:0 0 .5rem;
  color:#405b71;
  font-size:.89rem;
  line-height:1.47;
}
.area3-v41-figure{
  margin:0;
  overflow:hidden;
  border-radius:24px;
  background:#fff;
  border:1px solid rgba(126,159,186,.22);
  box-shadow:0 14px 30px rgba(19,45,74,.075);
}
.area3-v41-figure img{
  display:block;
  width:100%;
  height:auto;
  background:#fff;
}
.area3-v41-works{
  padding:15px 17px;
  border-radius:20px;
  background:linear-gradient(180deg,rgba(255,255,255,.86),rgba(247,250,253,.95));
  border:1px solid rgba(127,160,186,.18);
}
.area3-v41-works ul{
  margin:0;
  padding-left:1.05rem;
  columns:2;
  column-gap:2rem;
}
.area3-v41-works li{
  break-inside:avoid;
  margin:0 0 .36rem;
  color:#607488;
  font-size:.82rem;
  line-height:1.42;
}
.area3-v41-works a,
.area3-v41-works a:visited{
  color:#035083;
  text-decoration:none;
  font-weight:400!important;
}
.area3-v41-works a:hover{
  color:#00709c;
  text-decoration:underline;
}
.area3-v41-works span{
  color:#7f90a2;
}
@media(max-width:980px){
  .home-area3-v41{
    width:min(100%,calc(100% - 22px));
    max-width:min(100%,calc(100% - 22px));
  }
  .area3-v41-top{
    grid-template-columns:1fr;
  }
  .area3-v41 .difficulties-box ul,
  .area3-v41-works ul{
    columns:1;
  }
}
@media(max-width:640px){
  .home-area3-v41{
    width:min(100%,calc(100% - 18px));
    margin:28px auto 30px;
  }
  .area3-v41-card{
    padding:16px;
    border-radius:24px;
  }
  .area3-v41-figure{
    border-radius:18px;
  }
}
/* === Homepage research area 3 seamless fusion v41 END === */
"""

CSS.write_text(css.rstrip() + "\n\n" + css_block.strip() + "\n", encoding="utf-8")
print("Done: added Research Area 3 below Research Area 2 using the seamless indoor-outdoor figure.")
