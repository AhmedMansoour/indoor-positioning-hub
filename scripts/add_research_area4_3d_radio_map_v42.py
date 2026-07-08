from pathlib import Path
import re, shutil

INDEX = Path("index.html")
CSS = Path("assets/css/style.css")
BUNDLE_SRC = Path(__file__).resolve().parent.parent / "bundle_assets" / "research-area4-v42"
ASSET_DST = Path("assets/home/research-area4-v42")

if not INDEX.exists():
    raise SystemExit("index.html not found. Run from repository root.")
if not CSS.exists():
    raise SystemExit("assets/css/style.css not found. Run from repository root.")
if not BUNDLE_SRC.exists():
    raise SystemExit("bundle_assets/research-area4-v42 not found. Extract the full zip first.")

ASSET_DST.mkdir(parents=True, exist_ok=True)
for item in BUNDLE_SRC.iterdir():
    if item.is_file():
        shutil.copy2(item, ASSET_DST / item.name)

html = INDEX.read_text(encoding="utf-8", errors="ignore")
css = CSS.read_text(encoding="utf-8", errors="ignore")

html = re.sub(
    r'\n\s*<!-- === Homepage research area 4 3d radio map v42 START === -->.*?<!-- === Homepage research area 4 3d radio map v42 END === -->\s*\n',
    "\n", html, flags=re.S | re.I
)

section = """
<!-- === Homepage research area 4 3d radio map v42 START === -->
<section class="home-area4-v42" id="research-area-4">
  <article class="area4-v42-card">
    <div class="area4-v42-title">
      <div class="area4-v42-labels">
        <span class="area4-index">Research Area 4</span>
        <span>3D radio-map generation</span>
        <span>Vertical positioning</span>
        <span>Floor recognition</span>
        <span>Multi-level spatial context</span>
      </div>
      <h3>3D Radio-Map Generation from Mobile Crowdsensing</h3>
    </div>

    <div class="area4-v42-top">
      <section class="area4-v42-box why-box">
        <h4>Why it matters</h4>
        <p>Indoor positioning becomes operational only when the system understands the building as a multi-level spatial structure. A correct horizontal estimate is not enough in a multi-floor environment, because the same x–y location may correspond to different rooms, corridors, activities, or services on different floors.</p>
        <p>This research area addresses 3D radio-map generation from mobile crowdsensing. The aim is to convert ordinary walking sessions into floor-local map skeletons, assemble them into a building-level 3D representation, and refine the structure using reliable anchors such as gates, payment terminals, Wi-Fi access points, vertical transitions, and spatial constraints. The result is not only a set of fingerprints, but a 3D indoor spatial reference that supports floor recognition, vertical positioning, and deployment-ready localization.</p>
      </section>

      <figure class="area4-v42-figure">
        <img src="assets/home/research-area4-v42/skeleton-assembly-refinement.webp" alt="Three-stage 3D radio-map generation process from floor-local map skeletons to building-local 3D assembly and global refinement" loading="lazy" decoding="async">
      </figure>
    </div>

    <section class="area4-v42-box difficulties-box area4-v42-wide">
      <h4>Core difficulties</h4>
      <ul>
        <li>Floor-local traces must be reconstructed from noisy mobile sessions before they can be used as reliable spatial skeletons.</li>
        <li>Vertical positioning requires more than height-change detection; it must connect barometer trends, motion events, stairs, elevators, ramps, and building topology.</li>
        <li>Floor recognition is difficult when Wi-Fi and BLE signals leak across floors, especially near atriums, stairwells, open shafts, and dense access-point layouts.</li>
        <li>Building-level 3D assembly must align separate floor skeletons into one consistent spatial structure instead of treating each floor as an isolated map.</li>
        <li>Anchor objects and stable signal landmarks are needed to reduce accumulated distortion and connect the generated structure to real building coordinates.</li>
        <li>Global refinement must correct local errors while preserving floor connectivity, vertical transitions, and the physical constraints of the indoor environment.</li>
      </ul>
    </section>

    <div class="area4-v42-works">
      <h4>Representative works</h4>
      <ul>
        <li><a href="publications/reliability-governed-3d-radio-mapping-lifecycle-review.html">Reliability-Governed Scaling of Mobile Crowdsensing-Based 3D Radio Mapping for Ubiquitous Indoor Positioning</a> <span>(2026)</span></li>
        <li><a href="publications/towards-ubiquitous-ips-crowdsourced-data-accumulation.html">Towards Ubiquitous IPS: Leveraging Crowdsourced Data Accumulation Over Time to Alleviate Reliance on External Sources in Initial Fingerprinting Map Generation</a> <span>(2024)</span></li>
        <li><a href="publications/leveraging-human-mobility-pervasive-smartphone-crowdsourcing.html">Leveraging Human Mobility and Pervasive Smartphone Measurements-Based Crowdsourcing for Developing Self-Deployable and Ubiquitous Indoor Positioning Systems</a> <span>(2023)</span></li>
        <li><a href="publications/phd-thesis-indoor-localization-multi-sensor-crowdsourcing-collaboration.html">Indoor Localization Based on Multi-Sensor Fusion, Crowdsourcing, and Multi-User Collaboration</a> <span>(PhD thesis)</span></li>
      </ul>
    </div>
  </article>
</section>
<!-- === Homepage research area 4 3d radio map v42 END === -->
"""

inserted = False
for marker in [
    "<!-- === Homepage research area 3 seamless fusion v41 END === -->",
    "<!-- === Homepage research area 2 fullwidth difficulties v40 END === -->",
    "<!-- === Homepage research area 2 session radio v39 END === -->",
]:
    pos = html.find(marker)
    if pos != -1:
        html = html[:pos + len(marker)] + "\n\n" + section + html[pos + len(marker):]
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

css = re.sub(
    r'/\* === Homepage research area 4 3d radio map v42 START === \*/.*?/\* === Homepage research area 4 3d radio map v42 END === \*/',
    "", css, flags=re.S
)

css_block = """
/* === Homepage research area 4 3d radio map v42 START === */
.home-area4-v42{width:min(1180px,calc(100% - 56px));max-width:min(1180px,calc(100% - 56px));margin:28px auto 42px;box-sizing:border-box}
.area4-v42-card{display:grid;gap:18px;padding:22px;border-radius:30px;background:radial-gradient(circle at 80% 18%,rgba(79,196,211,.13),transparent 35%),linear-gradient(180deg,rgba(255,255,255,.98),rgba(248,252,255,.98));border:1px solid rgba(130,165,194,.25);box-shadow:0 20px 46px rgba(20,45,74,.08)}
.area4-v42-labels{display:flex;flex-wrap:wrap;gap:8px;align-items:center;margin-bottom:.75rem}
.area4-v42-labels span{display:inline-flex;align-items:center;min-height:30px;padding:.42rem .74rem;border-radius:999px;background:rgba(83,197,213,.10);border:1px solid rgba(79,159,187,.24);color:#0b6380;font-size:.76rem;font-weight:700;line-height:1}
.area4-v42-labels .area4-index{background:linear-gradient(135deg,rgba(84,202,213,.20),rgba(149,118,246,.12));color:#084f72;font-weight:800}
.area4-v42-title h3{margin:0;color:#073d63;font-size:clamp(1.52rem,2.28vw,2.08rem);line-height:1.12;letter-spacing:-.04em}
.area4-v42-top{display:grid;grid-template-columns:minmax(0,.93fr) minmax(470px,1.07fr);gap:18px;align-items:start}
.area4-v42-box{padding:16px 17px;border-radius:20px;border:1px solid rgba(127,160,186,.21)}
.area4-v42-box h4,.area4-v42-works h4{margin:0 0 .55rem;color:#0b5074;font-size:.94rem;line-height:1.25}
.area4-v42-box p{margin:0 0 .65rem;color:#405b71;font-size:.92rem;line-height:1.58}
.area4-v42-box p:last-child{margin-bottom:0}
.area4-v42 .why-box{background:linear-gradient(180deg,rgba(239,247,251,.96),rgba(249,252,255,.98))}
.area4-v42 .difficulties-box{background:linear-gradient(180deg,rgba(245,242,255,.92),rgba(251,249,255,.98));border-color:rgba(148,132,200,.18)}
.area4-v42-wide{width:100%;box-sizing:border-box}
.area4-v42 .difficulties-box ul{margin:0;padding-left:1.08rem;columns:2;column-gap:2.2rem}
.area4-v42 .difficulties-box li{break-inside:avoid;margin:0 0 .5rem;color:#405b71;font-size:.89rem;line-height:1.47}
.area4-v42-figure{margin:0;overflow:hidden;border-radius:24px;background:#fff;border:1px solid rgba(126,159,186,.22);box-shadow:0 14px 30px rgba(19,45,74,.075)}
.area4-v42-figure img{display:block;width:100%;height:auto;background:#fff}
.area4-v42-works{padding:15px 17px;border-radius:20px;background:linear-gradient(180deg,rgba(255,255,255,.86),rgba(247,250,253,.95));border:1px solid rgba(127,160,186,.18)}
.area4-v42-works ul{margin:0;padding-left:1.05rem;columns:2;column-gap:2rem}
.area4-v42-works li{break-inside:avoid;margin:0 0 .36rem;color:#607488;font-size:.82rem;line-height:1.42}
.area4-v42-works a,.area4-v42-works a:visited{color:#035083;text-decoration:none;font-weight:400!important}
.area4-v42-works a:hover{color:#00709c;text-decoration:underline}
.area4-v42-works span{color:#7f90a2}
@media(max-width:980px){.home-area4-v42{width:min(100%,calc(100% - 22px));max-width:min(100%,calc(100% - 22px))}.area4-v42-top{grid-template-columns:1fr}.area4-v42 .difficulties-box ul,.area4-v42-works ul{columns:1}}
@media(max-width:640px){.home-area4-v42{width:min(100%,calc(100% - 18px));margin:28px auto 30px}.area4-v42-card{padding:16px;border-radius:24px}.area4-v42-figure{border-radius:18px}}
/* === Homepage research area 4 3d radio map v42 END === */
"""

CSS.write_text(css.rstrip() + "\n\n" + css_block.strip() + "\n", encoding="utf-8")
print("Done: added Research Area 4 for 3D radio-map generation below Research Area 3.")
