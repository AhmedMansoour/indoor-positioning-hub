from pathlib import Path
import re, shutil

INDEX = Path("index.html")
CSS = Path("assets/css/style.css")
ASSET_DST = Path("assets/home/research-area1-v30")
BUNDLE_SRC = Path(__file__).resolve().parent.parent / "bundle_assets" / "research-area1-v30"

if not INDEX.exists():
    raise SystemExit("index.html not found. Run from repository root.")
if not CSS.exists():
    raise SystemExit("assets/css/style.css not found. Run from repository root.")
if not BUNDLE_SRC.exists():
    raise SystemExit("bundle_assets/research-area1-v30 not found. Extract full zip first.")

ASSET_DST.mkdir(parents=True, exist_ok=True)
for item in BUNDLE_SRC.iterdir():
    if item.is_file():
        shutil.copy2(item, ASSET_DST / item.name)

html = INDEX.read_text(encoding="utf-8", errors="ignore")
css = CSS.read_text(encoding="utf-8", errors="ignore")

for pat in [
    r'\n\s*<!-- === Homepage key thematic extension v24 START === -->.*?<!-- === Homepage key thematic extension v24 END === -->\s*\n',
    r'\n\s*<!-- === Homepage problem tree v25 START === -->.*?<!-- === Homepage problem tree v25 END === -->\s*\n',
    r'\n\s*<!-- === Homepage structured pathways v26 START === -->.*?<!-- === Homepage structured pathways v26 END === -->\s*\n',
    r'\n\s*<!-- === Homepage visual problem rows v27 START === -->.*?<!-- === Homepage visual problem rows v27 END === -->\s*\n',
    r'\n\s*<!-- === Homepage visual-first rows v28 START === -->.*?<!-- === Homepage visual-first rows v28 END === -->\s*\n',
    r'\n\s*<!-- === Homepage inertial pathway v29 START === -->.*?<!-- === Homepage inertial pathway v29 END === -->\s*\n',
    r'\n\s*<!-- === Homepage research area 1 inertial v30 START === -->.*?<!-- === Homepage research area 1 inertial v30 END === -->\s*\n',
    r'\n\s*<section[^>]*id=["\']key-thematic-map["\'][^>]*>.*?</section>\s*\n',
]:
    html = re.sub(pat, "\n", html, flags=re.S | re.I)

section = """
<!-- === Homepage research area 1 inertial v30 START === -->
<section class="home-research-area-map" id="key-thematic-map">
  <div class="home-section-heading research-area-map-heading">
    <p class="eyebrow">Home · Key thematic pathways across the hub</p>
    <h2>Research areas across the hub</h2>
    <p>This section is built step by step. Each research area is presented with compact explanation, linked representative works, and large figures that communicate the technical idea quickly.</p>
  </div>

  <article class="research-area-one-card">
    <div class="research-area-header">
      <div class="research-area-label-row">
        <span class="research-area-index">Research Area 1</span>
        <span class="research-area-chip">Infrastructure-free positioning</span>
        <span class="research-area-chip">PDR and smartphone sensing</span>
      </div>
      <h3>Enhancing Inertial Positioning Performance</h3>
    </div>

    <div class="research-area-text-grid">
      <div class="research-area-text-box">
        <h4>Why it matters</h4>
        <p>Inertial positioning is infrastructure-free, low-cost, and available on commodity smartphones. It provides a relative navigation layer that can bridge outages in GNSS, Wi-Fi RSS, BLE, map matching, LiDAR, and image-based localization.</p>
      </div>

      <div class="research-area-text-box difficulty-box">
        <h4>Core difficulties</h4>
        <p>Initialization, body-to-platform frame inconsistency, heading drift, magnetic disturbance, pose changes, and long-term error accumulation.</p>
        <div class="research-area-small-tags">
          <span>initialization</span><span>heading drift</span><span>magnetic disturbance</span><span>pose changes</span><span>long-term error</span>
        </div>
      </div>
    </div>

    <div class="research-area-visual-grid">
      <figure class="research-area-visual main-visual">
        <img src="assets/home/research-area1-v30/inertial-multipose-route.webp" alt="Inertial positioning trajectories under holding, calling, swinging, mixed use, and in-pocket smartphone poses" loading="lazy" decoding="async">
      </figure>
      <figure class="research-area-visual side-visual">
        <img src="assets/home/research-area1-v30/inertial-floorplan-drift.webp" alt="Noisy inertial trajectory over a floor plan showing drift and map inconsistency" loading="lazy" decoding="async">
      </figure>
    </div>

    <div class="research-area-works-row">
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
<!-- === Homepage research area 1 inertial v30 END === -->
"""

for marker in ['<p class="eyebrow">Publication access</p>', '<h2>Find papers, PDFs, citation records, and visual explanations</h2>', '<footer']:
    pos = html.find(marker)
    if pos != -1:
        html = html[:pos] + section + "\n" + html[pos:]
        break
else:
    pos = html.rfind("</main>")
    html = html[:pos] + section + "\n" + html[pos:] if pos != -1 else html.rstrip() + "\n" + section

INDEX.write_text(html, encoding="utf-8")

for pat in [
    r'/\* === Homepage key thematic extension v24 START === \*/.*?/\* === Homepage key thematic extension v24 END === \*/',
    r'/\* === Homepage problem tree v25 START === \*/.*?/\* === Homepage problem tree v25 END === \*/',
    r'/\* === Homepage structured pathways v26 START === \*/.*?/\* === Homepage structured pathways v26 END === \*/',
    r'/\* === Homepage visual problem rows v27 START === \*/.*?/\* === Homepage visual problem rows v27 END === \*/',
    r'/\* === Homepage visual-first rows v28 START === \*/.*?/\* === Homepage visual-first rows v28 END === \*/',
    r'/\* === Homepage inertial pathway v29 START === \*/.*?/\* === Homepage inertial pathway v29 END === \*/',
    r'/\* === Homepage research area 1 inertial v30 START === \*/.*?/\* === Homepage research area 1 inertial v30 END === \*/',
]:
    css = re.sub(pat, "", css, flags=re.S)

css_block = """
/* === Homepage research area 1 inertial v30 START === */
.home-research-area-map{width:min(1120px,calc(100% - 28px));margin:54px auto 44px}
.research-area-map-heading{max-width:900px;margin:0 auto 22px;text-align:center}
.research-area-map-heading h2{margin:.15rem 0 .5rem;color:#082d49;font-size:clamp(1.85rem,2.7vw,2.55rem);line-height:1.12;letter-spacing:-.04em}
.research-area-map-heading p:not(.eyebrow){color:#607589;font-size:.98rem;line-height:1.68}
.research-area-one-card{display:grid;gap:18px;padding:clamp(18px,2vw,24px);border-radius:30px;background:radial-gradient(circle at 82% 16%,rgba(79,196,211,.13),transparent 34%),linear-gradient(180deg,rgba(255,255,255,.98),rgba(248,252,255,.98));border:1px solid rgba(130,165,194,.25);box-shadow:0 20px 46px rgba(20,45,74,.08)}
.research-area-label-row{display:flex;flex-wrap:wrap;gap:8px;align-items:center;margin-bottom:.72rem}
.research-area-index,.research-area-chip{display:inline-flex;align-items:center;min-height:30px;padding:.42rem .74rem;border-radius:999px;border:1px solid rgba(79,159,187,.24);line-height:1}
.research-area-index{background:linear-gradient(135deg,rgba(84,202,213,.20),rgba(149,118,246,.12));color:#084f72;font-size:.78rem;font-weight:800}
.research-area-chip{background:rgba(83,197,213,.10);color:#0b6380;font-size:.76rem;font-weight:700}
.research-area-one-card h3{margin:0;color:#073d63;font-size:clamp(1.55rem,2.45vw,2.3rem);line-height:1.12;letter-spacing:-.04em}
.research-area-text-grid{display:grid;grid-template-columns:minmax(0,1.1fr) minmax(0,.9fr);gap:14px}
.research-area-text-box{padding:15px 16px;border-radius:20px;background:linear-gradient(180deg,rgba(239,247,251,.96),rgba(249,252,255,.98));border:1px solid rgba(127,160,186,.21)}
.research-area-text-box.difficulty-box{background:linear-gradient(180deg,rgba(245,242,255,.92),rgba(251,249,255,.98));border-color:rgba(148,132,200,.18)}
.research-area-text-box h4,.research-area-works-row h4{margin:0 0 .45rem;color:#0b5074;font-size:.92rem;line-height:1.25}
.research-area-text-box p{margin:0;color:#4c6378;font-size:.92rem;line-height:1.58}
.research-area-small-tags{display:flex;flex-wrap:wrap;gap:7px;margin-top:.75rem}
.research-area-small-tags span{padding:.32rem .58rem;border-radius:999px;background:rgba(232,239,245,.92);border:1px solid rgba(147,171,192,.18);color:#51677a;font-size:.72rem;font-weight:600}
.research-area-visual-grid{display:grid;grid-template-columns:minmax(0,1.68fr) minmax(260px,.78fr);gap:14px;align-items:start}
.research-area-visual{margin:0;overflow:hidden;border-radius:24px;background:#fff;border:1px solid rgba(126,159,186,.22);box-shadow:0 14px 30px rgba(19,45,74,.075)}
.research-area-visual img{display:block;width:100%;height:auto;background:#fff}
.research-area-visual.side-visual{max-width:360px}
.research-area-works-row{padding:14px 16px;border-radius:20px;background:linear-gradient(180deg,rgba(255,255,255,.84),rgba(247,250,253,.94));border:1px solid rgba(127,160,186,.18)}
.research-area-works-row ul{margin:0;padding-left:1.05rem;columns:2;column-gap:2rem}
.research-area-works-row li{break-inside:avoid;margin:0 0 .35rem;color:#607488;font-size:.82rem;line-height:1.42}
.research-area-works-row a,.research-area-works-row a:visited{color:#035083;text-decoration:none;font-weight:400!important}
.research-area-works-row a:hover{color:#00709c;text-decoration:underline}
.research-area-works-row span{color:#7f90a2}
@media(max-width:960px){.research-area-text-grid,.research-area-visual-grid{grid-template-columns:1fr}.research-area-visual.side-visual{max-width:100%}.research-area-works-row ul{columns:1}}
@media(max-width:640px){.home-research-area-map{width:min(100%,calc(100% - 18px));margin:40px auto 30px}.research-area-one-card{border-radius:24px}.research-area-visual{border-radius:18px}}
/* === Homepage research area 1 inertial v30 END === */
"""
CSS.write_text(css.rstrip() + "\n\n" + css_block.strip() + "\n", encoding="utf-8")
print("Done: added Research Area 1 with a cleaner visual-first layout and compact wording.")
