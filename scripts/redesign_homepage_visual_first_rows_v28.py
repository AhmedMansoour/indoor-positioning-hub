from pathlib import Path
import re
import shutil

ROOT = Path('.')
INDEX = ROOT / 'index.html'
CSS = ROOT / 'assets' / 'css' / 'style.css'
ASSET_DST = ROOT / 'assets' / 'home' / 'pathways-v28'
BUNDLE_SRC = Path(__file__).resolve().parent.parent / 'bundle_assets' / 'pathways-v28'

if not INDEX.exists():
    raise SystemExit('index.html not found. Run this script from the repository root.')
if not CSS.exists():
    raise SystemExit('assets/css/style.css not found. Run this script from the repository root.')
if not BUNDLE_SRC.exists():
    raise SystemExit('bundle_assets/pathways-v28 not found. Extract the full zip into the repository root first.')

ASSET_DST.mkdir(parents=True, exist_ok=True)
for item in BUNDLE_SRC.iterdir():
    if item.is_file():
        shutil.copy2(item, ASSET_DST / item.name)

index_html = INDEX.read_text(encoding='utf-8', errors='ignore')
css = CSS.read_text(encoding='utf-8', errors='ignore')

# Remove older homepage thematic/pathway sections.
for pat in [
    r'\n\s*<!-- === Homepage key thematic extension v24 START === -->.*?<!-- === Homepage key thematic extension v24 END === -->\s*\n',
    r'\n\s*<!-- === Homepage problem tree v25 START === -->.*?<!-- === Homepage problem tree v25 END === -->\s*\n',
    r'\n\s*<!-- === Homepage structured pathways v26 START === -->.*?<!-- === Homepage structured pathways v26 END === -->\s*\n',
    r'\n\s*<!-- === Homepage visual problem rows v27 START === -->.*?<!-- === Homepage visual problem rows v27 END === -->\s*\n',
    r'\n\s*<!-- === Homepage visual-first rows v28 START === -->.*?<!-- === Homepage visual-first rows v28 END === -->\s*\n',
    r'\n\s*<section[^>]*id=["\']key-thematic-map["\'][^>]*>.*?</section>\s*\n',
]:
    index_html = re.sub(pat, '\n', index_html, flags=re.S | re.I)

section = '''
<!-- === Homepage visual-first rows v28 START === -->
<section class="home-visual-problem-map" id="key-thematic-map">
  <div class="home-section-heading visual-map-heading">
    <p class="eyebrow">Home · Key thematic pathways across the hub</p>
    <h2>Structured pathway map</h2>
    <p>Each row presents one indoor-positioning problem and links it to representative works. The layout is visual-first: figures occupy most of the row width so the technical message is easier to understand at a glance.</p>
  </div>

  <div class="visual-problem-list">

    <article class="visual-problem-row">
      <div class="visual-problem-text">
        <div class="visual-problem-meta"><span>01</span><em>🧭 Motion stability</em></div>
        <h3>Inertial positioning drift, heading instability, and multi-pose user behavior</h3>
        <div class="problem-compact"><strong>Problem.</strong> Pedestrian trajectories drift when heading error accumulates and the phone changes across holding, calling, swinging, pocket, and mixed carrying behaviors.</div>
        <div class="works-compact"><strong>Representative works</strong>
          <ul>
            <li><a href="publications/hybrid-neural-network-pdr-multi-layer-heading-correction.html">Hybrid Neural Network-Based PDR with Multi-Layer Heading Correction Across Smartphone Carrying Modes</a> <span>(2026)</span></li>
            <li><a href="publications/enhancing-real-time-heading-estimation-deep-learning-smartphone-sensors.html">Enhancing Real-Time Heading Estimation for Pedestrian Navigation Using Deep Learning and Smartphone Sensors</a> <span>(2025)</span></li>
            <li><a href="publications/drift-control-pdr-long-period-navigation-smartphone-poses.html">Drift Control of Pedestrian Dead Reckoning for Long-Period Navigation Under Different Smartphone Poses</a> <span>(2021)</span></li>
          </ul>
        </div>
      </div>
      <div class="visual-problem-figures figure-pair motion-layout">
        <figure class="visual-figure dominant"><img src="assets/home/pathways-v28/pose_route.webp" alt="Pose-dependent trajectories for holding, calling, swinging, and in-pocket smartphone usage" loading="lazy" decoding="async"></figure>
        <figure class="visual-figure supporting wide-strip"><img src="assets/home/pathways-v28/pose_peaks.webp" alt="Step peaks and valleys across multiple smartphone poses" loading="lazy" decoding="async"></figure>
      </div>
    </article>

    <article class="visual-problem-row">
      <div class="visual-problem-text">
        <div class="visual-problem-meta"><span>02</span><em>📶 Fingerprinting integrity</em></div>
        <h3>Fingerprint uncertainty, heading calibration, and robust Wi-Fi plus inertial fusion</h3>
        <div class="problem-compact"><strong>Problem.</strong> Fingerprint fixes are not equally reliable, and inertial heading must be calibrated carefully when Wi-Fi matches are unstable or intermittently trustworthy.</div>
        <div class="works-compact"><strong>Representative works</strong>
          <ul>
            <li><a href="publications/drift-resistant-heading-estimation-wifi-magnetic-stability.html">Drift-Resistant Heading Estimation for Smartphone-Based Indoor Positioning via Adaptive Calibration Using Wi-Fi Fingerprinting and Magnetic Stability</a> <span>(2026)</span></li>
            <li><a href="publications/everywhere-framework-ubiquitous-indoor-localization.html">Everywhere: A Framework for Ubiquitous Indoor Localization</a> <span>(2022)</span></li>
            <li><a href="publications/power-of-many-multi-user-collaborative-indoor-localization.html">The Power of Many: Multi-User Collaborative Indoor Localization</a> <span>(2023)</span></li>
          </ul>
        </div>
      </div>
      <div class="visual-problem-figures figure-pair equal-diagrams">
        <figure class="visual-figure"><img src="assets/home/pathways-v28/heading_calibration.webp" alt="Conceptual diagram of heading calibration using qualified Wi-Fi fingerprinting positions" loading="lazy" decoding="async"></figure>
        <figure class="visual-figure"><img src="assets/home/pathways-v28/heading_framework.webp" alt="System framework combining motion analysis and Wi-Fi fingerprinting for heading calibration" loading="lazy" decoding="async"></figure>
      </div>
    </article>

    <article class="visual-problem-row">
      <div class="visual-problem-text">
        <div class="visual-problem-meta"><span>03</span><em>🏢 3D scaling</em></div>
        <h3>3D indoor positioning, multi-floor detection, and scalable radio-map generation</h3>
        <div class="problem-compact"><strong>Problem.</strong> Building-scale IPS must connect floor-local tracks, infer vertical transitions, and generate usable radio maps without full manual surveys on every floor.</div>
        <div class="works-compact"><strong>Representative works</strong>
          <ul>
            <li><a href="publications/reliability-governed-3d-radio-mapping-lifecycle-review.html">Reliability-Governed Scaling of Mobile Crowdsensing-Based 3D Radio Mapping for Ubiquitous Indoor Positioning</a> <span>(2026)</span></li>
            <li><a href="publications/towards-ubiquitous-ips-crowdsourced-data-accumulation.html">Towards Ubiquitous IPS: Leveraging Crowdsourced Data Accumulation Over Time to Alleviate Reliance on External Sources in Initial Fingerprinting Map Generation</a> <span>(2024)</span></li>
            <li><a href="publications/leveraging-human-mobility-pervasive-smartphone-crowdsourcing.html">Leveraging Human Mobility and Pervasive Smartphone Measurements-Based Crowdsourcing for Developing Self-Deployable and Ubiquitous Indoor Positioning Systems</a> <span>(2023)</span></li>
          </ul>
        </div>
      </div>
      <div class="visual-problem-figures three-figures map-layout">
        <figure class="visual-figure big"><img src="assets/home/pathways-v28/layered_building.webp" alt="Layered building visualization for smart building positioning" loading="lazy" decoding="async"></figure>
        <figure class="visual-figure"><img src="assets/home/pathways-v28/radio_map_process.webp" alt="Illustration of crowdsourced radio-map generation processes" loading="lazy" decoding="async"></figure>
        <figure class="visual-figure"><img src="assets/home/pathways-v28/raw_crowd_radio_map.webp" alt="Raw crowdsourced data converted to a radio map" loading="lazy" decoding="async"></figure>
      </div>
    </article>

    <article class="visual-problem-row">
      <div class="visual-problem-text">
        <div class="visual-problem-meta"><span>04</span><em>🔄 Seamless continuity</em></div>
        <h3>Indoor-outdoor continuity, multisensor context, and seamless trajectory fusion</h3>
        <div class="problem-compact"><strong>Problem.</strong> Navigation traces cross indoor areas, outdoor legs, vertical transitions, and sensor gaps, so the system must preserve continuity across changing context and coverage.</div>
        <div class="works-compact"><strong>Representative works</strong>
          <ul>
            <li><a href="publications/suns-seamless-ubiquitous-navigation-indoor-outdoor-awareness.html">SUNS: Seamless Ubiquitous Navigation System Based on GNSS, Wi-Fi, and MEMS Sensors</a> <span>(2022)</span></li>
            <li><a href="publications/gnss-positioning-aided-with-pdr-in-urban-areas.html">GNSS Positioning Aided with Pedestrian Dead Reckoning in Urban Areas</a> <span>(2026)</span></li>
            <li><a href="publications/tightly-coupled-bluetooth-enhanced-gnss-pdr-urban.html">Tightly Coupled Bluetooth Enhanced GNSS/PDR System for Pedestrian Navigation in Dense Urban Environments</a> <span>(2024)</span></li>
            <li><a href="publications/ac-hmm-azimuth-constrained-map-matching-urban-canyons.html">AC-HMM: Azimuth-Constrained Hidden Markov Model-Based Map Matching for Robust Pedestrian Positioning in Urban Canyons</a> <span>(2026)</span></li>
          </ul>
        </div>
      </div>
      <div class="visual-problem-figures figure-pair seamless-layout">
        <figure class="visual-figure"><img src="assets/home/pathways-v28/context_descriptor.webp" alt="Context descriptor and multisensor session log stream for seamless positioning" loading="lazy" decoding="async"></figure>
        <figure class="visual-figure"><img src="assets/home/pathways-v28/seamless_tracks.webp" alt="Seamless positioning performance across different tracks" loading="lazy" decoding="async"></figure>
      </div>
    </article>

    <article class="visual-problem-row">
      <div class="visual-problem-text">
        <div class="visual-problem-meta"><span>05</span><em>🗺️ Geometric reconstruction</em></div>
        <h3>Path ambiguity, site geometry, and reconstruction of difficult trajectories</h3>
        <div class="problem-compact"><strong>Problem.</strong> Crowdsensed tracks are noisy and spatially ambiguous, especially in loops, intersections, and irregular corridors where map structure must be recovered from imperfect traces.</div>
        <div class="works-compact"><strong>Representative works</strong>
          <ul>
            <li><a href="publications/reliability-governed-3d-radio-mapping-lifecycle-review.html">Reliability-Governed Scaling of Mobile Crowdsensing-Based 3D Radio Mapping for Ubiquitous Indoor Positioning</a> <span>(2026)</span></li>
            <li><a href="publications/towards-ubiquitous-ips-crowdsourced-data-accumulation.html">Towards Ubiquitous IPS: Leveraging Crowdsourced Data Accumulation Over Time to Alleviate Reliance on External Sources in Initial Fingerprinting Map Generation</a> <span>(2024)</span></li>
            <li><a href="publications/leveraging-human-mobility-pervasive-smartphone-crowdsourcing.html">Leveraging Human Mobility and Pervasive Smartphone Measurements-Based Crowdsourcing for Developing Self-Deployable and Ubiquitous Indoor Positioning Systems</a> <span>(2023)</span></li>
          </ul>
        </div>
      </div>
      <div class="visual-problem-figures figure-pair geometry-layout">
        <figure class="visual-figure tall"><img src="assets/home/pathways-v28/trajectory_floorplan.webp" alt="Noisy crowdsensed trajectories overlaid on a building floor plan" loading="lazy" decoding="async"></figure>
        <figure class="visual-figure"><img src="assets/home/pathways-v28/radio_map_process.webp" alt="Structured process for turning tracks into radio-map components" loading="lazy" decoding="async"></figure>
      </div>
    </article>

    <article class="visual-problem-row">
      <div class="visual-problem-text">
        <div class="visual-problem-meta"><span>06</span><em>👥 Deployment scaling</em></div>
        <h3>User-centered scaling, privacy, energy limits, and real deployment constraints</h3>
        <div class="problem-compact"><strong>Problem.</strong> Large-scale IPS must remain usable under privacy preferences, battery constraints, sparse participation, and the variability of ordinary devices and user behavior.</div>
        <div class="works-compact"><strong>Representative works</strong>
          <ul>
            <li><a href="publications/towards-scalable-ips-user-centric-crowd-powered-framework.html">Towards Scalable IPS: User-Centric Challenges, Methods, and Recommendations for User-Friendly Crowd-Powered Schemes</a> <span>(2026)</span></li>
            <li><a href="publications/modular-prompting-ai-guided-user-engagement-crowd-powered-ips.html">A Modular Prompting Framework for AI-Guided Unobtrusive User Engagement in Crowd-Powered Indoor Positioning with Semantic Knowledge Graphs and GPT-4-Based LLMs</a> <span>(2025)</span></li>
            <li><a href="publications/everywhere-framework-ubiquitous-indoor-localization.html">Everywhere: A Framework for Ubiquitous Indoor Localization</a> <span>(2022)</span></li>
          </ul>
        </div>
      </div>
      <div class="visual-problem-figures figure-pair deployment-layout">
        <figure class="visual-figure"><img src="assets/home/pathways-v28/deployment_realities.webp" alt="Deployment realities including energy use, privacy, and building differences" loading="lazy" decoding="async"></figure>
        <figure class="visual-figure"><img src="assets/home/pathways-v28/scaling_principles.webp" alt="Principles for scaling indoor positioning systems" loading="lazy" decoding="async"></figure>
      </div>
    </article>

  </div>
</section>
<!-- === Homepage visual-first rows v28 END === -->
'''

inserted = False
for marker in ['<p class="eyebrow">Publication access</p>', '<h2>Find papers, PDFs, citation records, and visual explanations</h2>', '<footer']:
    pos = index_html.find(marker)
    if pos != -1:
        index_html = index_html[:pos] + section + '\n' + index_html[pos:]
        inserted = True
        break
if not inserted:
    pos = index_html.rfind('</main>')
    if pos != -1:
        index_html = index_html[:pos] + section + '\n' + index_html[pos:]
    else:
        index_html = index_html.rstrip() + '\n' + section + '\n'

INDEX.write_text(index_html, encoding='utf-8')

# Remove older CSS blocks.
for pat in [
    r'/\* === Homepage key thematic extension v24 START === \*/.*?/\* === Homepage key thematic extension v24 END === \*/',
    r'/\* === Homepage problem tree v25 START === \*/.*?/\* === Homepage problem tree v25 END === \*/',
    r'/\* === Homepage structured pathways v26 START === \*/.*?/\* === Homepage structured pathways v26 END === \*/',
    r'/\* === Homepage visual problem rows v27 START === \*/.*?/\* === Homepage visual problem rows v27 END === \*/',
    r'/\* === Homepage visual-first rows v28 START === \*/.*?/\* === Homepage visual-first rows v28 END === \*/',
]:
    css = re.sub(pat, '', css, flags=re.S)

css_block = '''
/* === Homepage visual-first rows v28 START === */
.home-visual-problem-map {
  width: min(1180px, calc(100% - 28px));
  margin: 56px auto 42px;
}
.visual-map-heading {
  max-width: 960px;
  margin: 0 auto 22px;
  text-align: center;
}
.visual-map-heading h2 {
  margin: 0.2rem 0 0.55rem;
  font-size: clamp(1.9rem, 2.9vw, 2.7rem);
  letter-spacing: -0.04em;
}
.visual-map-heading p:not(.eyebrow) {
  color: #617488;
  line-height: 1.7;
}
.visual-problem-list {
  display: grid;
  gap: 18px;
}
.visual-problem-row {
  position: relative;
  display: grid;
  grid-template-columns: minmax(280px, 0.82fr) minmax(0, 1.78fr);
  gap: 18px;
  align-items: start;
  padding: 18px;
  border-radius: 30px;
  background: linear-gradient(180deg, rgba(255,255,255,0.97), rgba(248,251,255,0.99));
  border: 1px solid rgba(129, 161, 190, 0.24);
  box-shadow: 0 18px 40px rgba(19, 43, 74, 0.08);
  overflow: hidden;
}
.visual-problem-row::before {
  content: '';
  position: absolute;
  inset: 0 auto 0 0;
  width: 4px;
  background: linear-gradient(180deg, #5ad1d0, #8b6ff3);
}
.visual-problem-text {
  display: grid;
  gap: 11px;
  align-content: start;
  min-width: 0;
}
.visual-problem-meta {
  display: flex;
  align-items: center;
  gap: 10px;
  flex-wrap: wrap;
}
.visual-problem-meta span {
  display: grid;
  place-items: center;
  width: 40px;
  height: 40px;
  border-radius: 14px;
  background: linear-gradient(135deg, rgba(99,205,216,0.18), rgba(141,112,244,0.15));
  border: 1px solid rgba(112,158,194,0.28);
  color: #0b5679;
  font-size: 0.88rem;
  font-weight: 800;
}
.visual-problem-meta em {
  display: inline-flex;
  align-items: center;
  padding: 0.42rem 0.76rem;
  border-radius: 999px;
  background: rgba(83,197,213,0.10);
  border: 1px solid rgba(95,167,194,0.22);
  color: #0a647e;
  font-size: 0.78rem;
  font-style: normal;
  font-weight: 700;
}
.visual-problem-row h3 {
  margin: 0;
  color: #083d63;
  font-size: clamp(1.08rem, 1.5vw, 1.42rem);
  line-height: 1.28;
  letter-spacing: -0.02em;
}
.problem-compact,
.works-compact {
  border-radius: 18px;
  padding: 12px 13px;
  border: 1px solid rgba(128,158,183,0.18);
}
.problem-compact {
  background: linear-gradient(180deg, rgba(236,245,251,0.92), rgba(247,250,253,0.96));
  color: #617489;
  font-size: 0.84rem;
  line-height: 1.55;
}
.works-compact {
  background: linear-gradient(180deg, rgba(244,241,255,0.90), rgba(250,248,255,0.96));
}
.problem-compact strong,
.works-compact strong {
  color: #0b5073;
  font-size: 0.86rem;
}
.works-compact ul {
  margin: 0.35rem 0 0;
  padding-left: 1rem;
  display: grid;
  gap: 0.22rem;
}
.works-compact li,
.works-compact span {
  color: #617489;
  font-size: 0.82rem;
  line-height: 1.48;
}
.works-compact a,
.works-compact a:visited {
  color: #035082;
  text-decoration: none;
  font-weight: 400 !important;
}
.works-compact a:hover {
  color: #00709c;
  text-decoration: underline;
}
.visual-problem-figures {
  min-width: 0;
  display: grid;
  gap: 12px;
  align-items: start;
}
.figure-pair {
  grid-template-columns: repeat(2, minmax(0, 1fr));
}
.three-figures {
  grid-template-columns: 0.95fr 1.1fr 0.95fr;
}
.visual-figure {
  margin: 0;
  border-radius: 22px;
  overflow: hidden;
  border: 1px solid rgba(127,160,186,0.22);
  background: #ffffff;
  box-shadow: 0 10px 24px rgba(20,44,74,0.06);
}
.visual-figure img {
  display: block;
  width: 100%;
  height: auto !important;
  max-height: none !important;
  object-fit: unset !important;
  padding: 0 !important;
  background: #ffffff;
}
.motion-layout {
  grid-template-columns: minmax(0, 1.05fr) minmax(0, 0.95fr);
}
.motion-layout .wide-strip {
  align-self: start;
}
.equal-diagrams,
.seamless-layout,
.deployment-layout {
  grid-template-columns: repeat(2, minmax(0, 1fr));
}
.map-layout .big {
  grid-row: span 1;
}
.geometry-layout {
  grid-template-columns: minmax(0, 0.85fr) minmax(0, 1.15fr);
}
@media (max-width: 1120px) {
  .visual-problem-row {
    grid-template-columns: 1fr;
  }
  .visual-problem-figures {
    order: 1;
  }
  .visual-problem-text {
    order: 2;
  }
}
@media (max-width: 760px) {
  .home-visual-problem-map {
    width: min(100%, calc(100% - 18px));
    margin: 40px auto 28px;
  }
  .visual-problem-row {
    padding: 15px;
    border-radius: 24px;
  }
  .figure-pair,
  .three-figures,
  .motion-layout,
  .equal-diagrams,
  .seamless-layout,
  .deployment-layout,
  .geometry-layout {
    grid-template-columns: 1fr;
  }
}
/* === Homepage visual-first rows v28 END === */
'''

CSS.write_text(css.rstrip() + '\n\n' + css_block.strip() + '\n', encoding='utf-8')
print('Done: inserted the visual-first natural-dimension homepage problem rows (v28).')
