
from pathlib import Path
import re
import shutil

ROOT = Path(".")
INDEX = ROOT / "index.html"
CSS = ROOT / "assets" / "css" / "style.css"
ASSET_DST = ROOT / "assets" / "home" / "inertial-v29"
BUNDLE_SRC = Path(__file__).resolve().parent.parent / "bundle_assets" / "inertial-v29"

if not INDEX.exists():
    raise SystemExit("index.html not found. Run this script from the repository root.")
if not CSS.exists():
    raise SystemExit("assets/css/style.css not found. Run this script from the repository root.")
if not BUNDLE_SRC.exists():
    raise SystemExit("bundle_assets/inertial-v29 not found. Extract the full zip into the repository root first.")

ASSET_DST.mkdir(parents=True, exist_ok=True)
for item in BUNDLE_SRC.iterdir():
    if item.is_file():
        shutil.copy2(item, ASSET_DST / item.name)

index_html = INDEX.read_text(encoding="utf-8", errors="ignore")
css = CSS.read_text(encoding="utf-8", errors="ignore")

html_patterns = [
    r'\n\s*<!-- === Homepage key thematic extension v24 START === -->.*?<!-- === Homepage key thematic extension v24 END === -->\s*\n',
    r'\n\s*<!-- === Homepage problem tree v25 START === -->.*?<!-- === Homepage problem tree v25 END === -->\s*\n',
    r'\n\s*<!-- === Homepage structured pathways v26 START === -->.*?<!-- === Homepage structured pathways v26 END === -->\s*\n',
    r'\n\s*<!-- === Homepage visual problem rows v27 START === -->.*?<!-- === Homepage visual problem rows v27 END === -->\s*\n',
    r'\n\s*<!-- === Homepage visual-first rows v28 START === -->.*?<!-- === Homepage visual-first rows v28 END === -->\s*\n',
    r'\n\s*<!-- === Homepage inertial pathway v29 START === -->.*?<!-- === Homepage inertial pathway v29 END === -->\s*\n',
    r'\n\s*<section[^>]*id=["\']key-thematic-map["\'][^>]*>.*?</section>\s*\n',
]
for pat in html_patterns:
    index_html = re.sub(pat, "\n", index_html, flags=re.S | re.I)

section = """
<!-- === Homepage inertial pathway v29 START === -->
<section class="home-inertial-pathway" id="key-thematic-map">
  <div class="home-section-heading inertial-pathway-heading">
    <p class="eyebrow">Home · Key thematic pathways across the hub</p>
    <h2>1. Enhancing inertial positioning performance</h2>
    <p>A focused pathway on infrastructure-free pedestrian navigation, inertial drift control, smartphone pose effects, and the role of PDR as a relative positioning layer when other technologies become intermittent.</p>
  </div>

  <article class="inertial-pathway-card">
    <div class="inertial-pathway-text">
      <div class="inertial-pathway-labels">
        <span>Problem 01</span>
        <span>Infrastructure-free positioning</span>
        <span>PDR and smartphone sensing</span>
      </div>

      <h3>Enhancing inertial positioning performance</h3>

      <p class="inertial-lead">Inertial positioning is an infrastructure-free, off-the-shelf, and low-cost solution for pedestrian navigation. It is especially valuable as a relative positioning layer that can bridge outages and complement GNSS, Wi-Fi RSS, BLE, map matching, LiDAR, and image-based localization.</p>

      <div class="inertial-detail-box">
        <h4>Why it is difficult</h4>
        <p>Practical inertial positioning is limited by initialization sensitivity, body-frame to platform-frame inconsistency, step and motion variability, and accumulated heading drift. Long-term gyroscope errors gradually distort orientation, while short-term compass heading can be corrupted by magnetic disturbances, steel structures, elevators, electronics, and indoor environmental interference. These issues become more severe when the phone changes pose, such as holding, calling, swinging, mixed use, or in-pocket carrying.</p>
      </div>

      <div class="inertial-chips" aria-label="Key challenges">
        <span>initialization</span>
        <span>body-to-platform frame</span>
        <span>gyro drift</span>
        <span>compass disturbance</span>
        <span>pose changes</span>
        <span>step variability</span>
        <span>long-term drift</span>
        <span>sensor fusion</span>
      </div>

      <div class="inertial-works">
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
    </div>

    <div class="inertial-visual-mosaic" aria-label="Visual examples of inertial positioning performance">
      <figure class="inertial-figure inertial-figure-main">
        <img src="assets/home/inertial-v29/inertial-multipose-route.webp" alt="Inertial positioning trajectories under holding, calling, swinging, mixed use, and in-pocket smartphone poses" loading="lazy" decoding="async">
        <figcaption>Smartphone pose changes strongly affect PDR trajectory behavior and heading stability.</figcaption>
      </figure>
      <figure class="inertial-figure inertial-figure-side">
        <img src="assets/home/inertial-v29/inertial-floorplan-drift.webp" alt="Noisy inertial trajectory over a floor plan showing drift and map inconsistency" loading="lazy" decoding="async">
        <figcaption>Long trajectories show how inertial drift and map inconsistency accumulate without correction.</figcaption>
      </figure>
    </div>
  </article>
</section>
<!-- === Homepage inertial pathway v29 END === -->
"""

inserted = False
for marker in ['<p class="eyebrow">Publication access</p>', '<h2>Find papers, PDFs, citation records, and visual explanations</h2>', '<footer']:
    pos = index_html.find(marker)
    if pos != -1:
        index_html = index_html[:pos] + section + "\n" + index_html[pos:]
        inserted = True
        break

if not inserted:
    pos = index_html.rfind("</main>")
    if pos != -1:
        index_html = index_html[:pos] + section + "\n" + index_html[pos:]
    else:
        index_html = index_html.rstrip() + "\n" + section + "\n"

INDEX.write_text(index_html, encoding="utf-8")

css_patterns = [
    r'/\* === Homepage key thematic extension v24 START === \*/.*?/\* === Homepage key thematic extension v24 END === \*/',
    r'/\* === Homepage problem tree v25 START === \*/.*?/\* === Homepage problem tree v25 END === \*/',
    r'/\* === Homepage structured pathways v26 START === \*/.*?/\* === Homepage structured pathways v26 END === \*/',
    r'/\* === Homepage visual problem rows v27 START === \*/.*?/\* === Homepage visual problem rows v27 END === \*/',
    r'/\* === Homepage visual-first rows v28 START === \*/.*?/\* === Homepage visual-first rows v28 END === \*/',
    r'/\* === Homepage inertial pathway v29 START === \*/.*?/\* === Homepage inertial pathway v29 END === \*/',
]
for pat in css_patterns:
    css = re.sub(pat, "", css, flags=re.S)

css_block = """
/* === Homepage inertial pathway v29 START === */
.home-inertial-pathway {
  width: min(1180px, calc(100% - 28px));
  margin: 56px auto 44px;
}

.inertial-pathway-heading {
  max-width: 980px;
  margin: 0 auto 22px;
  text-align: center;
}

.inertial-pathway-heading h2 {
  margin: 0.15rem 0 0.55rem;
  color: #082d49;
  font-size: clamp(1.9rem, 3vw, 2.85rem);
  line-height: 1.12;
  letter-spacing: -0.045em;
}

.inertial-pathway-heading p:not(.eyebrow) {
  color: #607589;
  font-size: 1rem;
  line-height: 1.68;
}

.inertial-pathway-card {
  display: grid;
  grid-template-columns: minmax(330px, 0.82fr) minmax(560px, 1.55fr);
  gap: 22px;
  align-items: start;
  padding: 22px;
  border-radius: 32px;
  background:
    radial-gradient(circle at 80% 12%, rgba(86, 203, 213, 0.14), transparent 34%),
    linear-gradient(180deg, rgba(255,255,255,0.97), rgba(248,252,255,0.98));
  border: 1px solid rgba(130, 165, 194, 0.26);
  box-shadow: 0 20px 46px rgba(20, 45, 74, 0.085);
}

.inertial-pathway-text {
  display: grid;
  gap: 14px;
  align-content: start;
}

.inertial-pathway-labels {
  display: flex;
  flex-wrap: wrap;
  gap: 8px;
}

.inertial-pathway-labels span {
  display: inline-flex;
  align-items: center;
  padding: 0.42rem 0.72rem;
  border-radius: 999px;
  background: rgba(83, 197, 213, 0.12);
  border: 1px solid rgba(79, 159, 187, 0.24);
  color: #0b6380;
  font-size: 0.76rem;
  font-weight: 700;
  line-height: 1;
}

.inertial-pathway-text h3 {
  margin: 0;
  color: #073d63;
  font-size: clamp(1.35rem, 1.95vw, 1.85rem);
  line-height: 1.18;
  letter-spacing: -0.032em;
}

.inertial-lead {
  margin: 0;
  color: #364f65;
  font-size: 0.98rem;
  line-height: 1.62;
}

.inertial-detail-box {
  padding: 14px 15px;
  border-radius: 20px;
  background: linear-gradient(180deg, rgba(239,247,251,0.96), rgba(249,252,255,0.98));
  border: 1px solid rgba(127, 160, 186, 0.22);
}

.inertial-detail-box h4,
.inertial-works h4 {
  margin: 0 0 0.45rem;
  color: #0b5074;
  font-size: 0.9rem;
  line-height: 1.25;
}

.inertial-detail-box p {
  margin: 0;
  color: #607488;
  font-size: 0.88rem;
  line-height: 1.58;
}

.inertial-chips {
  display: flex;
  flex-wrap: wrap;
  gap: 7px;
}

.inertial-chips span {
  padding: 0.34rem 0.62rem;
  border-radius: 999px;
  background: rgba(232, 239, 245, 0.92);
  border: 1px solid rgba(147, 171, 192, 0.20);
  color: #51677a;
  font-size: 0.73rem;
  font-weight: 600;
}

.inertial-works {
  padding: 14px 15px;
  border-radius: 20px;
  background: linear-gradient(180deg, rgba(245,242,255,0.92), rgba(251,249,255,0.98));
  border: 1px solid rgba(148, 132, 200, 0.18);
}

.inertial-works ul {
  margin: 0;
  padding-left: 1.05rem;
  display: grid;
  gap: 0.34rem;
}

.inertial-works li {
  color: #607488;
  font-size: 0.82rem;
  line-height: 1.45;
}

.inertial-works a,
.inertial-works a:visited {
  color: #035083;
  text-decoration: none;
  font-weight: 400 !important;
}

.inertial-works a:hover {
  color: #00709c;
  text-decoration: underline;
}

.inertial-works span {
  color: #7f90a2;
}

.inertial-visual-mosaic {
  display: grid;
  grid-template-columns: minmax(0, 1.52fr) minmax(220px, 0.88fr);
  gap: 14px;
  align-items: start;
}

.inertial-figure {
  margin: 0;
  overflow: hidden;
  border-radius: 24px;
  background: #ffffff;
  border: 1px solid rgba(126, 159, 186, 0.22);
  box-shadow: 0 14px 30px rgba(19, 45, 74, 0.075);
}

.inertial-figure img {
  display: block;
  width: 100%;
  height: auto;
  background: #ffffff;
}

.inertial-figure figcaption {
  margin: 0;
  padding: 10px 13px 12px;
  color: #66798d;
  font-size: 0.75rem;
  line-height: 1.42;
  background: linear-gradient(180deg, rgba(250,253,255,0.92), rgba(245,249,252,0.98));
}

.inertial-figure-main {
  align-self: start;
}

.inertial-figure-side {
  align-self: start;
}

@media (max-width: 1120px) {
  .inertial-pathway-card {
    grid-template-columns: 1fr;
  }

  .inertial-visual-mosaic {
    grid-template-columns: minmax(0, 1.35fr) minmax(220px, 0.75fr);
    order: -1;
  }
}

@media (max-width: 760px) {
  .home-inertial-pathway {
    width: min(100%, calc(100% - 18px));
    margin: 40px auto 30px;
  }

  .inertial-pathway-card {
    padding: 16px;
    border-radius: 24px;
  }

  .inertial-visual-mosaic {
    grid-template-columns: 1fr;
  }

  .inertial-figure {
    border-radius: 18px;
  }
}
/* === Homepage inertial pathway v29 END === */
"""

CSS.write_text(css.rstrip() + "\n\n" + css_block.strip() + "\n", encoding="utf-8")
print("Done: added Problem 01, Enhancing inertial positioning performance, with a visual-first two-figure layout.")
