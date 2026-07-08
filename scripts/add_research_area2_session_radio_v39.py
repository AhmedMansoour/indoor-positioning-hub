from pathlib import Path
import re, shutil

INDEX = Path("index.html")
CSS = Path("assets/css/style.css")
BUNDLE_SRC = Path(__file__).resolve().parent.parent / "bundle_assets" / "research-area2-v39"
ASSET_DST = Path("assets/home/research-area2-v39")

if not INDEX.exists():
    raise SystemExit("index.html not found. Run from repository root.")
if not CSS.exists():
    raise SystemExit("assets/css/style.css not found. Run from repository root.")
if not BUNDLE_SRC.exists():
    raise SystemExit("bundle_assets/research-area2-v39 not found. Extract the full zip first.")

ASSET_DST.mkdir(parents=True, exist_ok=True)
for item in BUNDLE_SRC.iterdir():
    if item.is_file():
        shutil.copy2(item, ASSET_DST / item.name)

html = INDEX.read_text(encoding="utf-8", errors="ignore")
css = CSS.read_text(encoding="utf-8", errors="ignore")

# Remove any previous Area 2 block to avoid duplicates.
for pat in [
    r'\n\s*<!-- === Homepage research area 2 session radio v39 START === -->.*?<!-- === Homepage research area 2 session radio v39 END === -->\s*\n',
]:
    html = re.sub(pat, "\n", html, flags=re.S | re.I)

section = """
<!-- === Homepage research area 2 session radio v39 START === -->
<section class="home-area2-v39" id="research-area-2">
  <article class="area2-v39-card">
    <div class="area2-v39-title">
      <div class="area2-v39-labels">
        <span class="area2-index">Research Area 2</span>
        <span>Wi-Fi fingerprinting</span>
        <span>Multisensor session logs</span>
        <span>Radio-map scaling</span>
      </div>
      <h3>Scaling Wi-Fi Fingerprinting and Autonomous Radio-Map Generation</h3>
    </div>

    <div class="area2-v39-main">
      <div class="area2-v39-copy">
        <section class="area2-v39-box why-box">
          <h4>Why it matters</h4>
          <p>Wi-Fi fingerprinting provides the absolute indoor reference that inertial positioning cannot maintain by itself. A fingerprint links a wireless observation to a physical indoor location, making it useful for correcting PDR drift, recognizing floors, initializing trajectories, and supporting building-scale indoor services where GNSS is unavailable.</p>
          <p>The central challenge is no longer only how to match an RSS vector to a point. The harder deployment question is how to generate, update, and trust radio maps when the data arrive from ordinary mobile sessions rather than controlled survey campaigns.</p>
        </section>

        <section class="area2-v39-box difficulties-box">
          <h4>Core difficulties</h4>
          <ul>
            <li>Manual radio-map surveying is expensive and difficult to repeat when buildings, access points, or service requirements change.</li>
            <li>Crowdsourced trajectories are uneven, because users move freely, pause, turn, change floors, and carry phones in different ways.</li>
            <li>RSS measurements vary across devices, time, human blockage, furniture layout, access-point configuration, and environmental dynamics.</li>
            <li>Multifloor radio mapping requires vertical interpretation from barometer, motion, building topology, and wireless evidence, not only horizontal fingerprint matching.</li>
            <li>Session logs must synchronize Wi-Fi scans, IMU samples, magnetometer readings, barometer pressure, GNSS fixes, and app events into one coherent spatial record.</li>
            <li>Radio-map updating needs reliability control, because writing back unreliable fingerprints can degrade the map instead of improving it.</li>
          </ul>
        </section>
      </div>

      <figure class="area2-v39-figure">
        <img src="assets/home/research-area2-v39/multisensor-session-log-stream.webp" alt="Multisensor session log stream integrating Wi-Fi RSS, IMU, magnetometer, barometer, GNSS fixes, app events, and wireless fingerprints across buildings and floors" loading="lazy" decoding="async">
      </figure>
    </div>

    <div class="area2-v39-works">
      <h4>Representative works</h4>
      <ul>
        <li><a href="publications/reliability-governed-3d-radio-mapping-lifecycle-review.html">Reliability-Governed Scaling of Mobile Crowdsensing-Based 3D Radio Mapping for Ubiquitous Indoor Positioning</a> <span>(2026)</span></li>
        <li><a href="publications/towards-ubiquitous-ips-crowdsourced-data-accumulation.html">Towards Ubiquitous IPS: Leveraging Crowdsourced Data Accumulation Over Time to Alleviate Reliance on External Sources in Initial Fingerprinting Map Generation</a> <span>(2024)</span></li>
        <li><a href="publications/leveraging-human-mobility-pervasive-smartphone-crowdsourcing.html">Leveraging Human Mobility and Pervasive Smartphone Measurements-Based Crowdsourcing for Developing Self-Deployable and Ubiquitous Indoor Positioning Systems</a> <span>(2023)</span></li>
        <li><a href="publications/everywhere-framework-ubiquitous-indoor-localization.html">Everywhere: A Framework for Ubiquitous Indoor Localization</a> <span>(2022)</span></li>
      </ul>
    </div>
  </article>
</section>
<!-- === Homepage research area 2 session radio v39 END === -->
"""

# Insert Area 2 directly after Area 1, if Area 1 exists. Otherwise before Publication Access.
area1_end_marker = "<!-- === Homepage research area 1 professor v38 END === -->"
pos = html.find(area1_end_marker)
if pos != -1:
    insert_at = pos + len(area1_end_marker)
    html = html[:insert_at] + "\n\n" + section + html[insert_at:]
else:
    area1_old_end = "<!-- === Homepage research area 1 reorganized v37 END === -->"
    pos = html.find(area1_old_end)
    if pos != -1:
        insert_at = pos + len(area1_old_end)
        html = html[:insert_at] + "\n\n" + section + html[insert_at:]
    else:
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

# Remove any previous Area 2 CSS and append clean style.
for pat in [
    r'/\* === Homepage research area 2 session radio v39 START === \*/.*?/\* === Homepage research area 2 session radio v39 END === \*/',
]:
    css = re.sub(pat, "", css, flags=re.S)

css_block = """
/* === Homepage research area 2 session radio v39 START === */
.home-area2-v39{
  width:min(1180px,calc(100% - 56px));
  max-width:min(1180px,calc(100% - 56px));
  margin:28px auto 42px;
  box-sizing:border-box;
}
.area2-v39-card{
  display:grid;
  gap:18px;
  padding:22px;
  border-radius:30px;
  background:radial-gradient(circle at 80% 18%,rgba(79,196,211,.13),transparent 35%),linear-gradient(180deg,rgba(255,255,255,.98),rgba(248,252,255,.98));
  border:1px solid rgba(130,165,194,.25);
  box-shadow:0 20px 46px rgba(20,45,74,.08);
}
.area2-v39-labels{
  display:flex;
  flex-wrap:wrap;
  gap:8px;
  align-items:center;
  margin-bottom:.75rem;
}
.area2-v39-labels span{
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
.area2-v39-labels .area2-index{
  background:linear-gradient(135deg,rgba(84,202,213,.20),rgba(149,118,246,.12));
  color:#084f72;
  font-weight:800;
}
.area2-v39-title h3{
  margin:0;
  color:#073d63;
  font-size:clamp(1.52rem,2.28vw,2.08rem);
  line-height:1.12;
  letter-spacing:-.04em;
}
.area2-v39-main{
  display:grid;
  grid-template-columns:minmax(0,1.05fr) minmax(430px,.92fr);
  gap:18px;
  align-items:start;
}
.area2-v39-copy{
  display:grid;
  gap:14px;
}
.area2-v39-box{
  padding:16px 17px;
  border-radius:20px;
  border:1px solid rgba(127,160,186,.21);
}
.area2-v39-box h4,
.area2-v39-works h4{
  margin:0 0 .55rem;
  color:#0b5074;
  font-size:.94rem;
  line-height:1.25;
}
.area2-v39-box p{
  margin:0 0 .65rem;
  color:#405b71;
  font-size:.92rem;
  line-height:1.58;
}
.area2-v39-box p:last-child{
  margin-bottom:0;
}
.area2-v39 .why-box{
  background:linear-gradient(180deg,rgba(239,247,251,.96),rgba(249,252,255,.98));
}
.area2-v39 .difficulties-box{
  background:linear-gradient(180deg,rgba(245,242,255,.92),rgba(251,249,255,.98));
  border-color:rgba(148,132,200,.18);
}
.area2-v39 .difficulties-box ul{
  margin:0;
  padding-left:1.08rem;
  display:grid;
  gap:.48rem;
}
.area2-v39 .difficulties-box li{
  color:#405b71;
  font-size:.89rem;
  line-height:1.47;
}
.area2-v39-figure{
  margin:0;
  overflow:hidden;
  border-radius:24px;
  background:#fff;
  border:1px solid rgba(126,159,186,.22);
  box-shadow:0 14px 30px rgba(19,45,74,.075);
}
.area2-v39-figure img{
  display:block;
  width:100%;
  height:auto;
  background:#fff;
}
.area2-v39-works{
  padding:15px 17px;
  border-radius:20px;
  background:linear-gradient(180deg,rgba(255,255,255,.86),rgba(247,250,253,.95));
  border:1px solid rgba(127,160,186,.18);
}
.area2-v39-works ul{
  margin:0;
  padding-left:1.05rem;
  columns:2;
  column-gap:2rem;
}
.area2-v39-works li{
  break-inside:avoid;
  margin:0 0 .36rem;
  color:#607488;
  font-size:.82rem;
  line-height:1.42;
}
.area2-v39-works a,
.area2-v39-works a:visited{
  color:#035083;
  text-decoration:none;
  font-weight:400!important;
}
.area2-v39-works a:hover{
  color:#00709c;
  text-decoration:underline;
}
.area2-v39-works span{
  color:#7f90a2;
}
@media(max-width:980px){
  .home-area2-v39{
    width:min(100%,calc(100% - 22px));
    max-width:min(100%,calc(100% - 22px));
  }
  .area2-v39-main{
    grid-template-columns:1fr;
  }
  .area2-v39-works ul{
    columns:1;
  }
}
@media(max-width:640px){
  .home-area2-v39{
    width:min(100%,calc(100% - 18px));
    margin:28px auto 30px;
  }
  .area2-v39-card{
    padding:16px;
    border-radius:24px;
  }
  .area2-v39-figure{
    border-radius:18px;
  }
}
/* === Homepage research area 2 session radio v39 END === */
"""

CSS.write_text(css.rstrip() + "\n\n" + css_block.strip() + "\n", encoding="utf-8")
print("Done: added Research Area 2 below Research Area 1 using the multisensor session-log figure.")
