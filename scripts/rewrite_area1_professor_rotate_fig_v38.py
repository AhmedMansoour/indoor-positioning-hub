from pathlib import Path
import re, shutil

INDEX = Path("index.html")
CSS = Path("assets/css/style.css")
BUNDLE_SRC = Path(__file__).resolve().parent.parent / "bundle_assets" / "research-area1-v38"
ASSET_DST = Path("assets/home/research-area1-v38")

if not INDEX.exists():
    raise SystemExit("index.html not found. Run from repository root.")
if not CSS.exists():
    raise SystemExit("assets/css/style.css not found. Run from repository root.")
if not BUNDLE_SRC.exists():
    raise SystemExit("bundle_assets/research-area1-v38 not found. Extract the full zip first.")

ASSET_DST.mkdir(parents=True, exist_ok=True)
for item in BUNDLE_SRC.iterdir():
    if item.is_file():
        shutil.copy2(item, ASSET_DST / item.name)

html = INDEX.read_text(encoding="utf-8", errors="ignore")
css = CSS.read_text(encoding="utf-8", errors="ignore")

# Remove previous Research Area 1 blocks.
for pat in [
    r'\n\s*<!-- === Homepage research area 1 inertial v30 START === -->.*?<!-- === Homepage research area 1 inertial v30 END === -->\s*\n',
    r'\n\s*<!-- === Homepage research area 1 reorganized v37 START === -->.*?<!-- === Homepage research area 1 reorganized v37 END === -->\s*\n',
    r'\n\s*<!-- === Homepage research area 1 professor v38 START === -->.*?<!-- === Homepage research area 1 professor v38 END === -->\s*\n',
]:
    html = re.sub(pat, "\n", html, flags=re.S | re.I)

section = """
<!-- === Homepage research area 1 professor v38 START === -->
<section class="home-area1-v38" id="key-thematic-map">
  <div class="area1-v38-heading">
    <p class="eyebrow">Home · Key thematic pathways across the hub</p>
    <h2>Research areas across the hub</h2>
    <p>Indoor positioning is not a single sensing problem. It is a set of connected challenges: preserving motion continuity, controlling drift, handling user behavior, maintaining spatial references, and linking relative motion to absolute indoor location.</p>
  </div>

  <article class="area1-v38-card">
    <div class="area1-v38-title">
      <div class="area1-v38-labels">
        <span class="area1-index">Research Area 1</span>
        <span>Infrastructure-free positioning</span>
        <span>PDR and smartphone sensing</span>
      </div>
      <h3>Enhancing Inertial Positioning Performance</h3>
    </div>

    <div class="area1-v38-main">
      <div class="area1-v38-copy">
        <section class="area1-v38-box why-box">
          <h4>Why it matters</h4>
          <p>Smartphone inertial sensing is the most available motion source in pedestrian navigation. It requires no installed anchors, no prior radio visibility, and no dedicated infrastructure. Its value is strongest when other positioning cues become weak or unavailable: it can carry motion through GNSS outages, sparse Wi-Fi RSS or BLE coverage, temporary map-matching ambiguity, and interruptions in LiDAR or image-based localization.</p>
          <p>In this role, inertial positioning is not only a standalone method. It is the relative-motion backbone that keeps the trajectory alive between absolute updates from external or environmental cues.</p>
        </section>

        <section class="area1-v38-box difficulties-box">
          <h4>Core difficulties</h4>
          <ul>
            <li>Accurate position and heading initialization are required when PDR is expected to provide absolute positioning, because an initial offset shifts the whole trajectory.</li>
            <li>The phone frame must be related to the pedestrian body frame; otherwise, a correct sensor measurement can point in the wrong walking direction.</li>
            <li>Heading drift is the dominant long-term error source, as small gyroscope biases gradually integrate into large orientation errors.</li>
            <li>Magnetometer heading can provide absolute direction, but it is easily disturbed by steel structures, elevators, electronics, reinforced concrete, and local magnetic anomalies.</li>
            <li>Carrying modes such as holding, calling, swinging, and in-pocket use change the sensor pattern and weaken fixed assumptions about step events, stride length, and walking direction.</li>
            <li>Standalone inertial propagation needs periodic correction from GNSS, Wi-Fi, BLE, map constraints, vision, or other trusted observations to prevent long-term divergence.</li>
          </ul>
        </section>
      </div>

      <figure class="area1-v38-figure">
        <img src="assets/home/research-area1-v38/inertial-multipose-route-rotated.webp" alt="Rotated multi-pose inertial positioning trajectories showing holding, calling, swinging, mixed use, and in-pocket smartphone poses" loading="lazy" decoding="async">
      </figure>
    </div>

    <div class="area1-v38-works">
      <h4>Representative works</h4>
      <ul>
        <li><a href="publications/drift-control-pdr-long-period-navigation-smartphone-poses.html">Drift Control of Pedestrian Dead Reckoning for Long Period Navigation under Different Smartphone Poses</a> <span>(2021)</span></li>
        <li><a href="publications/enhancing-real-time-heading-estimation-deep-learning-smartphone-sensors.html">Enhancing Real-Time Heading Estimation for Pedestrian Navigation via Deep Learning and Smartphone Embedded Sensors</a> <span>(2025)</span></li>
        <li><a href="publications/hybrid-neural-network-pdr-multi-layer-heading-correction.html">Hybrid Neural Network-Based PDR with Multi-Layer Heading Correction Across Smartphone Carrying Modes</a> <span>(2026)</span></li>
        <li><a href="publications/gnss-positioning-aided-with-pdr-in-urban-areas.html">GNSS Positioning Aided with Pedestrian Dead Reckoning in Urban Areas</a> <span>(2026)</span></li>
        <li><a href="publications/tightly-coupled-bluetooth-enhanced-gnss-pdr-urban.html">Tightly Coupled Bluetooth Enhanced GNSS/PDR System for Pedestrian Navigation in Dense Urban Environments</a> <span>(2024)</span></li>
        <li><a href="publications/ac-hmm-azimuth-constrained-map-matching-urban-canyons.html">AC-HMM: Azimuth-Constrained Hidden Markov Model-Based Map Matching for Robust Pedestrian Positioning in Urban Canyons</a> <span>(2026)</span></li>
      </ul>
    </div>
  </article>
</section>
<!-- === Homepage research area 1 professor v38 END === -->
"""

# Insert before the whole Publication Access section where possible.
pub = re.search(r'<p\s+class=["\']eyebrow["\']>\s*Publication access\s*</p>', html, flags=re.I)
inserted = False

if pub:
    section_start = html.rfind("<section", 0, pub.start())
    main_start = html.rfind("<main", 0, pub.start())
    if section_start != -1 and (main_start == -1 or section_start > main_start):
        html = html[:section_start] + "\n" + section + "\n\n" + html[section_start:]
        inserted = True

if not inserted:
    for marker in ["<footer", "</main>"]:
        pos = html.find(marker)
        if pos != -1:
            html = html[:pos] + "\n" + section + "\n" + html[pos:]
            inserted = True
            break

if not inserted:
    html = html.rstrip() + "\n" + section + "\n"

INDEX.write_text(html, encoding="utf-8")

# Remove previous CSS variants and append clean v38 CSS.
for pat in [
    r'/\* === Homepage research area 1 inertial v30 START === \*/.*?/\* === Homepage research area 1 inertial v30 END === \*/',
    r'/\* === Homepage research area 1 inertial v31 width refinement START === \*/.*?/\* === Homepage research area 1 inertial v31 width refinement END === \*/',
    r'/\* === Homepage research area 1 full-width v32 START === \*/.*?/\* === Homepage research area 1 full-width v32 END === \*/',
    r'/\* === Homepage research area 1 placement and width v33 START === \*/.*?/\* === Homepage research area 1 placement and width v33 END === \*/',
    r'/\* === Homepage research area 1 fullbleed v34 START === \*/.*?/\* === Homepage research area 1 fullbleed v34 END === \*/',
    r'/\* === Homepage research area 1 standalone wide v35 START === \*/.*?/\* === Homepage research area 1 standalone wide v35 END === \*/',
    r'/\* === Homepage research area 1 balanced width v36 START === \*/.*?/\* === Homepage research area 1 balanced width v36 END === \*/',
    r'/\* === Homepage research area 1 reorganized v37 START === \*/.*?/\* === Homepage research area 1 reorganized v37 END === \*/',
    r'/\* === Homepage research area 1 professor v38 START === \*/.*?/\* === Homepage research area 1 professor v38 END === \*/',
]:
    css = re.sub(pat, "", css, flags=re.S)

css_block = """
/* === Homepage research area 1 professor v38 START === */
.home-area1-v38{
  width:min(1180px,calc(100% - 56px));
  max-width:min(1180px,calc(100% - 56px));
  margin:52px auto 42px;
  box-sizing:border-box;
}
.area1-v38-heading{
  max-width:900px;
  margin:0 auto 22px;
  text-align:center;
}
.area1-v38-heading h2{
  margin:.12rem 0 .5rem;
  color:#082d49;
  font-size:clamp(1.78rem,2.55vw,2.42rem);
  line-height:1.12;
  letter-spacing:-.04em;
}
.area1-v38-heading p:not(.eyebrow){
  color:#607589;
  font-size:.96rem;
  line-height:1.65;
}
.area1-v38-card{
  display:grid;
  gap:18px;
  padding:22px;
  border-radius:30px;
  background:radial-gradient(circle at 80% 18%,rgba(79,196,211,.13),transparent 35%),linear-gradient(180deg,rgba(255,255,255,.98),rgba(248,252,255,.98));
  border:1px solid rgba(130,165,194,.25);
  box-shadow:0 20px 46px rgba(20,45,74,.08);
}
.area1-v38-labels{
  display:flex;
  flex-wrap:wrap;
  gap:8px;
  align-items:center;
  margin-bottom:.75rem;
}
.area1-v38-labels span{
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
.area1-v38-labels .area1-index{
  background:linear-gradient(135deg,rgba(84,202,213,.20),rgba(149,118,246,.12));
  color:#084f72;
  font-weight:800;
}
.area1-v38-title h3{
  margin:0;
  color:#073d63;
  font-size:clamp(1.52rem,2.28vw,2.08rem);
  line-height:1.12;
  letter-spacing:-.04em;
}
.area1-v38-main{
  display:grid;
  grid-template-columns:minmax(0,1.12fr) minmax(300px,.62fr);
  gap:18px;
  align-items:start;
}
.area1-v38-copy{
  display:grid;
  gap:14px;
}
.area1-v38-box{
  padding:16px 17px;
  border-radius:20px;
  border:1px solid rgba(127,160,186,.21);
}
.area1-v38-box h4,
.area1-v38-works h4{
  margin:0 0 .55rem;
  color:#0b5074;
  font-size:.94rem;
  line-height:1.25;
}
.area1-v38-box p{
  margin:0 0 .65rem;
  color:#405b71;
  font-size:.92rem;
  line-height:1.58;
}
.area1-v38-box p:last-child{
  margin-bottom:0;
}
.why-box{
  background:linear-gradient(180deg,rgba(239,247,251,.96),rgba(249,252,255,.98));
}
.difficulties-box{
  background:linear-gradient(180deg,rgba(245,242,255,.92),rgba(251,249,255,.98));
  border-color:rgba(148,132,200,.18);
}
.difficulties-box ul{
  margin:0;
  padding-left:1.08rem;
  display:grid;
  gap:.48rem;
}
.difficulties-box li{
  color:#405b71;
  font-size:.89rem;
  line-height:1.47;
}
.area1-v38-figure{
  margin:0;
  overflow:hidden;
  border-radius:24px;
  background:#fff;
  border:1px solid rgba(126,159,186,.22);
  box-shadow:0 14px 30px rgba(19,45,74,.075);
}
.area1-v38-figure img{
  display:block;
  width:100%;
  max-height:720px;
  object-fit:contain;
  background:#fff;
}
.area1-v38-works{
  padding:15px 17px;
  border-radius:20px;
  background:linear-gradient(180deg,rgba(255,255,255,.86),rgba(247,250,253,.95));
  border:1px solid rgba(127,160,186,.18);
}
.area1-v38-works ul{
  margin:0;
  padding-left:1.05rem;
  columns:2;
  column-gap:2rem;
}
.area1-v38-works li{
  break-inside:avoid;
  margin:0 0 .36rem;
  color:#607488;
  font-size:.82rem;
  line-height:1.42;
}
.area1-v38-works a,
.area1-v38-works a:visited{
  color:#035083;
  text-decoration:none;
  font-weight:400!important;
}
.area1-v38-works a:hover{
  color:#00709c;
  text-decoration:underline;
}
.area1-v38-works span{
  color:#7f90a2;
}
@media(max-width:980px){
  .home-area1-v38{
    width:min(100%,calc(100% - 22px));
    max-width:min(100%,calc(100% - 22px));
  }
  .area1-v38-main{
    grid-template-columns:1fr;
  }
  .area1-v38-figure img{
    max-height:none;
  }
  .area1-v38-works ul{
    columns:1;
  }
}
@media(max-width:640px){
  .home-area1-v38{
    width:min(100%,calc(100% - 18px));
    margin:40px auto 30px;
  }
  .area1-v38-card{
    padding:16px;
    border-radius:24px;
  }
  .area1-v38-figure{
    border-radius:18px;
  }
}
/* === Homepage research area 1 professor v38 END === */
"""

CSS.write_text(css.rstrip() + "\n\n" + css_block.strip() + "\n", encoding="utf-8")
print("Done: rotated the inertial figure clockwise and rewrote Research Area 1 in a more direct academic style.")
