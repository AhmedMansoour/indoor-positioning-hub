from pathlib import Path
import re
import shutil

ROOT = Path('.')
INDEX = ROOT / 'index.html'
CSS = ROOT / 'assets' / 'css' / 'style.css'
ASSET_DST = ROOT / 'assets' / 'home' / 'pathways-v26'
BUNDLE_SRC = Path(__file__).resolve().parent.parent / 'bundle_assets' / 'pathways-v26'

if not INDEX.exists():
    raise SystemExit('index.html not found. Run this script from the repository root.')
if not CSS.exists():
    raise SystemExit('assets/css/style.css not found. Run this script from the repository root.')
if not BUNDLE_SRC.exists():
    raise SystemExit('bundle_assets/pathways-v26 not found. Extract the full zip into the repository root first.')

ASSET_DST.mkdir(parents=True, exist_ok=True)
for item in BUNDLE_SRC.iterdir():
    if item.is_file():
        shutil.copy2(item, ASSET_DST / item.name)

index_html = INDEX.read_text(encoding='utf-8', errors='ignore')
css = CSS.read_text(encoding='utf-8', errors='ignore')

html_patterns = [
    r'\n\s*<!-- === Homepage key thematic extension v24 START === -->.*?<!-- === Homepage key thematic extension v24 END === -->\s*\n',
    r'\n\s*<!-- === Homepage problem tree v25 START === -->.*?<!-- === Homepage problem tree v25 END === -->\s*\n',
    r'\n\s*<!-- === Homepage structured pathways v26 START === -->.*?<!-- === Homepage structured pathways v26 END === -->\s*\n',
    r'\n\s*<section[^>]*id=["\']key-thematic-map["\'][^>]*>.*?<h2>\s*Key thematic pathways across the hub\s*</h2>.*?</section>\s*\n',
]
for pat in html_patterns:
    index_html = re.sub(pat, '\n', index_html, flags=re.S | re.I)

section = '''
<!-- === Homepage structured pathways v26 START === -->
<section class="home-structured-pathways" id="key-thematic-map">
  <div class="home-section-heading pathways-heading">
    <p class="eyebrow">Home · Key thematic pathways across the hub</p>
    <h2>Structured pathway map</h2>
    <p>This section reorganizes the hub around recurring indoor-positioning problems and the representative works that address them. It is designed as a compact visual pathway map, so readers can move from challenge to relevant papers with less scrolling and clearer thematic structure.</p>
  </div>

  <div class="pathway-grid">
    <article class="pathway-card">
      <div class="pathway-titlebar">
        <span class="pathway-badge">01</span>
        <div>
          <p class="pathway-kicker">🧭 Motion stability pathway</p>
          <h3>Inertial positioning drift, heading instability, and multi-pose user behavior</h3>
        </div>
      </div>
      <div class="pathway-panels">
        <div class="pathway-panel problem-panel">
          <h4>Problem</h4>
          <p>Pedestrian trajectories drift when heading accumulates error and the phone moves across holding, calling, swinging, pocket, and mixed carrying modes.</p>
        </div>
        <div class="pathway-panel works-panel">
          <h4>Representative works</h4>
          <ul>
            <li><a href="publications/hybrid-neural-network-pdr-multi-layer-heading-correction.html">Hybrid Neural Network-Based PDR with Multi-Layer Heading Correction Across Smartphone Carrying Modes</a> <span>(2026)</span></li>
            <li><a href="publications/enhancing-real-time-heading-estimation-deep-learning-smartphone-sensors.html">Enhancing Real-Time Heading Estimation for Pedestrian Navigation Using Deep Learning and Smartphone Sensors</a> <span>(2025)</span></li>
            <li><a href="publications/drift-control-pdr-long-period-navigation-smartphone-poses.html">Drift Control of Pedestrian Dead Reckoning for Long-Period Navigation Under Different Smartphone Poses</a> <span>(2021)</span></li>
          </ul>
        </div>
      </div>
      <div class="pathway-visuals two-up">
        <figure class="pathway-visual"><img src="assets/home/pathways-v26/pose_route.webp" alt="Pose-dependent trajectories for holding, calling, swinging, and in-pocket smartphone usage" loading="lazy" decoding="async"><figcaption>Pose-dependent trajectory behavior.</figcaption></figure>
        <figure class="pathway-visual"><img src="assets/home/pathways-v26/pose_peaks.webp" alt="Step peaks and valleys across multiple smartphone poses" loading="lazy" decoding="async"><figcaption>Step signatures across carrying modes.</figcaption></figure>
      </div>
    </article>

    <article class="pathway-card">
      <div class="pathway-titlebar">
        <span class="pathway-badge">02</span>
        <div>
          <p class="pathway-kicker">📶 Fingerprinting integrity pathway</p>
          <h3>Fingerprint uncertainty, heading calibration, and robust Wi-Fi plus inertial fusion</h3>
        </div>
      </div>
      <div class="pathway-panels">
        <div class="pathway-panel problem-panel">
          <h4>Problem</h4>
          <p>Fingerprint fixes are not equally reliable, and inertial heading must be calibrated carefully when Wi-Fi matches are unstable or only intermittently trustworthy.</p>
        </div>
        <div class="pathway-panel works-panel">
          <h4>Representative works</h4>
          <ul>
            <li><a href="publications/drift-resistant-heading-estimation-wifi-magnetic-stability.html">Drift-Resistant Heading Estimation for Smartphone-Based Indoor Positioning via Adaptive Calibration Using Wi-Fi Fingerprinting and Magnetic Stability</a> <span>(2026)</span></li>
            <li><a href="publications/everywhere-framework-ubiquitous-indoor-localization.html">Everywhere: A Framework for Ubiquitous Indoor Localization</a> <span>(2022)</span></li>
            <li><a href="publications/power-of-many-multi-user-collaborative-indoor-localization.html">The Power of Many: Multi-User Collaborative Indoor Localization</a> <span>(2023)</span></li>
          </ul>
        </div>
      </div>
      <div class="pathway-visuals two-up">
        <figure class="pathway-visual"><img src="assets/home/pathways-v26/heading_calibration.webp" alt="Conceptual diagram of heading calibration using qualified Wi-Fi fingerprinting positions" loading="lazy" decoding="async"><figcaption>Qualified Wi-Fi fixes for heading calibration.</figcaption></figure>
        <figure class="pathway-visual"><img src="assets/home/pathways-v26/heading_framework.webp" alt="System framework combining motion analysis and Wi-Fi fingerprinting for heading calibration" loading="lazy" decoding="async"><figcaption>Fusion logic for calibrated heading estimation.</figcaption></figure>
      </div>
    </article>

    <article class="pathway-card">
      <div class="pathway-titlebar">
        <span class="pathway-badge">03</span>
        <div>
          <p class="pathway-kicker">🏢 3D scaling pathway</p>
          <h3>3D indoor positioning, multi-floor detection, and scalable radio-map generation</h3>
        </div>
      </div>
      <div class="pathway-panels">
        <div class="pathway-panel problem-panel">
          <h4>Problem</h4>
          <p>Building-scale IPS must connect floor-local tracks, infer vertical transitions, and generate usable radio maps without full manual surveys on every floor.</p>
        </div>
        <div class="pathway-panel works-panel">
          <h4>Representative works</h4>
          <ul>
            <li><a href="publications/reliability-governed-3d-radio-mapping-lifecycle-review.html">Reliability-Governed Scaling of Mobile Crowdsensing-Based 3D Radio Mapping for Ubiquitous Indoor Positioning</a> <span>(2026)</span></li>
            <li><a href="publications/towards-ubiquitous-ips-crowdsourced-data-accumulation.html">Towards Ubiquitous IPS: Leveraging Crowdsourced Data Accumulation Over Time to Alleviate Reliance on External Sources in Initial Fingerprinting Map Generation</a> <span>(2024)</span></li>
            <li><a href="publications/leveraging-human-mobility-pervasive-smartphone-crowdsourcing.html">Leveraging Human Mobility and Pervasive Smartphone Measurements-Based Crowdsourcing for Developing Self-Deployable and Ubiquitous Indoor Positioning Systems</a> <span>(2023)</span></li>
          </ul>
        </div>
      </div>
      <div class="pathway-visuals three-up">
        <figure class="pathway-visual"><img src="assets/home/pathways-v26/layered_building.webp" alt="Layered building visualization for smart building positioning" loading="lazy" decoding="async"><figcaption>Building-scale 3D positioning view.</figcaption></figure>
        <figure class="pathway-visual"><img src="assets/home/pathways-v26/radio_map_process.webp" alt="Illustration of crowdsourced radio-map generation processes" loading="lazy" decoding="async"><figcaption>Crowdsourced map-generation process.</figcaption></figure>
        <figure class="pathway-visual"><img src="assets/home/pathways-v26/raw_crowd_radio_map.webp" alt="Raw crowdsourced data converted to a radio map" loading="lazy" decoding="async"><figcaption>Raw trajectories turned into radio-map structure.</figcaption></figure>
      </div>
    </article>

    <article class="pathway-card">
      <div class="pathway-titlebar">
        <span class="pathway-badge">04</span>
        <div>
          <p class="pathway-kicker">🔄 Seamless continuity pathway</p>
          <h3>Indoor-outdoor continuity, multisensor context, and seamless trajectory fusion</h3>
        </div>
      </div>
      <div class="pathway-panels">
        <div class="pathway-panel problem-panel">
          <h4>Problem</h4>
          <p>Navigation traces cross indoor areas, outdoor legs, vertical transitions, and sensor gaps, so the system must preserve continuity across changing context and coverage.</p>
        </div>
        <div class="pathway-panel works-panel">
          <h4>Representative works</h4>
          <ul>
            <li><a href="publications/suns-seamless-ubiquitous-navigation-indoor-outdoor-awareness.html">SUNS: Seamless Ubiquitous Navigation System Based on GNSS, Wi-Fi, and MEMS Sensors</a> <span>(2022)</span></li>
            <li><a href="publications/gnss-positioning-aided-with-pdr-in-urban-areas.html">GNSS Positioning Aided with Pedestrian Dead Reckoning in Urban Areas</a> <span>(2026)</span></li>
            <li><a href="publications/tightly-coupled-bluetooth-enhanced-gnss-pdr-urban.html">Tightly Coupled Bluetooth Enhanced GNSS/PDR System for Pedestrian Navigation in Dense Urban Environments</a> <span>(2024)</span></li>
            <li><a href="publications/ac-hmm-azimuth-constrained-map-matching-urban-canyons.html">AC-HMM: Azimuth-Constrained Hidden Markov Model-Based Map Matching for Robust Pedestrian Positioning in Urban Canyons</a> <span>(2026)</span></li>
          </ul>
        </div>
      </div>
      <div class="pathway-visuals two-up">
        <figure class="pathway-visual"><img src="assets/home/pathways-v26/context_descriptor.webp" alt="Context descriptor and multisensor session log stream for seamless positioning" loading="lazy" decoding="async"><figcaption>Multisensor context descriptor.</figcaption></figure>
        <figure class="pathway-visual"><img src="assets/home/pathways-v26/seamless_tracks.webp" alt="Seamless positioning performance across different tracks" loading="lazy" decoding="async"><figcaption>Trajectory fusion across challenging tracks.</figcaption></figure>
      </div>
    </article>

    <article class="pathway-card">
      <div class="pathway-titlebar">
        <span class="pathway-badge">05</span>
        <div>
          <p class="pathway-kicker">🗺️ Geometric reconstruction pathway</p>
          <h3>Path ambiguity, site geometry, and reconstruction of difficult trajectories</h3>
        </div>
      </div>
      <div class="pathway-panels">
        <div class="pathway-panel problem-panel">
          <h4>Problem</h4>
          <p>Crowdsensed tracks are noisy and spatially ambiguous, especially in loops, intersections, and irregular corridors where map structure must be recovered from imperfect traces.</p>
        </div>
        <div class="pathway-panel works-panel">
          <h4>Representative works</h4>
          <ul>
            <li><a href="publications/reliability-governed-3d-radio-mapping-lifecycle-review.html">Reliability-Governed Scaling of Mobile Crowdsensing-Based 3D Radio Mapping for Ubiquitous Indoor Positioning</a> <span>(2026)</span></li>
            <li><a href="publications/towards-ubiquitous-ips-crowdsourced-data-accumulation.html">Towards Ubiquitous IPS: Leveraging Crowdsourced Data Accumulation Over Time to Alleviate Reliance on External Sources in Initial Fingerprinting Map Generation</a> <span>(2024)</span></li>
            <li><a href="publications/leveraging-human-mobility-pervasive-smartphone-crowdsourcing.html">Leveraging Human Mobility and Pervasive Smartphone Measurements-Based Crowdsourcing for Developing Self-Deployable and Ubiquitous Indoor Positioning Systems</a> <span>(2023)</span></li>
          </ul>
        </div>
      </div>
      <div class="pathway-visuals two-up">
        <figure class="pathway-visual"><img src="assets/home/pathways-v26/trajectory_floorplan.webp" alt="Noisy crowdsensed trajectories overlaid on a building floor plan" loading="lazy" decoding="async"><figcaption>Noisy trajectories before structural recovery.</figcaption></figure>
        <figure class="pathway-visual"><img src="assets/home/pathways-v26/radio_map_process.webp" alt="Structured process for turning tracks into radio-map components" loading="lazy" decoding="async"><figcaption>Structure recovery and anchor inference.</figcaption></figure>
      </div>
    </article>

    <article class="pathway-card">
      <div class="pathway-titlebar">
        <span class="pathway-badge">06</span>
        <div>
          <p class="pathway-kicker">👥 Deployment pathway</p>
          <h3>User-centered scaling, privacy, energy limits, and real deployment constraints</h3>
        </div>
      </div>
      <div class="pathway-panels">
        <div class="pathway-panel problem-panel">
          <h4>Problem</h4>
          <p>Large-scale IPS must remain usable under privacy preferences, battery constraints, sparse participation, and the variability of ordinary devices and user behavior.</p>
        </div>
        <div class="pathway-panel works-panel">
          <h4>Representative works</h4>
          <ul>
            <li><a href="publications/towards-scalable-ips-user-centric-crowd-powered-framework.html">Towards Scalable IPS: User-Centric Challenges, Methods, and Recommendations for User-Friendly Crowd-Powered Schemes</a> <span>(2026)</span></li>
            <li><a href="publications/modular-prompting-ai-guided-user-engagement-crowd-powered-ips.html">A Modular Prompting Framework for AI-Guided Unobtrusive User Engagement in Crowd-Powered Indoor Positioning with Semantic Knowledge Graphs and GPT-4-Based LLMs</a> <span>(2025)</span></li>
            <li><a href="publications/everywhere-framework-ubiquitous-indoor-localization.html">Everywhere: A Framework for Ubiquitous Indoor Localization</a> <span>(2022)</span></li>
          </ul>
        </div>
      </div>
      <div class="pathway-visuals two-up">
        <figure class="pathway-visual"><img src="assets/home/pathways-v26/deployment_realities.webp" alt="Deployment realities including energy use, privacy, and building differences" loading="lazy" decoding="async"><figcaption>Real deployment constraints.</figcaption></figure>
        <figure class="pathway-visual"><img src="assets/home/pathways-v26/scaling_principles.webp" alt="Principles for scaling indoor positioning systems" loading="lazy" decoding="async"><figcaption>Principles for scalable user-centered IPS.</figcaption></figure>
      </div>
    </article>
  </div>
</section>
<!-- === Homepage structured pathways v26 END === -->
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

css = re.sub(r'/\* === Homepage key thematic extension v24 START === \*/.*?/\* === Homepage key thematic extension v24 END === \*/', '', css, flags=re.S)
css = re.sub(r'/\* === Homepage problem tree v25 START === \*/.*?/\* === Homepage problem tree v25 END === \*/', '', css, flags=re.S)
css = re.sub(r'/\* === Homepage structured pathways v26 START === \*/.*?/\* === Homepage structured pathways v26 END === \*/', '', css, flags=re.S)

css_block = '''
/* === Homepage structured pathways v26 START === */
.home-structured-pathways {
  width: min(1180px, calc(100% - 32px));
  margin: 56px auto 40px;
}
.pathways-heading {
  max-width: 960px;
  margin: 0 auto 24px;
  text-align: center;
}
.pathways-heading h2 {
  margin: 0.2rem 0 0.6rem;
  font-size: clamp(1.8rem, 2.8vw, 2.7rem);
  letter-spacing: -0.04em;
}
.pathways-heading p:not(.eyebrow) {
  color: #5f7287;
  font-size: 0.98rem;
  line-height: 1.7;
}
.pathway-grid {
  display: grid;
  grid-template-columns: repeat(2, minmax(0, 1fr));
  gap: 18px;
}
.pathway-card {
  position: relative;
  display: grid;
  gap: 14px;
  padding: 20px;
  border-radius: 28px;
  background: linear-gradient(180deg, rgba(255,255,255,0.96), rgba(249,252,255,0.98));
  border: 1px solid rgba(135, 164, 191, 0.26);
  box-shadow: 0 18px 42px rgba(17, 45, 74, 0.08);
  overflow: hidden;
}
.pathway-card::before {
  content: '';
  position: absolute;
  inset: 0 auto 0 0;
  width: 4px;
  background: linear-gradient(180deg, #59cbd3, #8a6cf6);
}
.pathway-titlebar {
  display: grid;
  grid-template-columns: 54px minmax(0, 1fr);
  gap: 12px;
  align-items: start;
}
.pathway-badge {
  width: 46px;
  height: 46px;
  border-radius: 16px;
  display: grid;
  place-items: center;
  color: #0a5576;
  font-weight: 800;
  background: linear-gradient(135deg, rgba(104, 207, 216, 0.18), rgba(152, 109, 255, 0.14));
  border: 1px solid rgba(111, 163, 202, 0.34);
}
.pathway-kicker {
  margin: 0 0 0.2rem;
  color: #0a627f;
  font-size: 0.82rem;
  font-weight: 700;
  letter-spacing: 0.01em;
}
.pathway-card h3 {
  margin: 0;
  color: #083d63;
  font-size: clamp(1.08rem, 1.45vw, 1.35rem);
  line-height: 1.25;
  letter-spacing: -0.02em;
}
.pathway-panels {
  display: grid;
  grid-template-columns: 1fr 1fr;
  gap: 12px;
}
.pathway-panel {
  border-radius: 18px;
  padding: 14px 15px;
  border: 1px solid rgba(132, 160, 184, 0.20);
}
.problem-panel {
  background: linear-gradient(180deg, rgba(235,245,251,0.90), rgba(247,250,253,0.95));
}
.works-panel {
  background: linear-gradient(180deg, rgba(244,241,255,0.88), rgba(250,248,255,0.95));
}
.pathway-panel h4 {
  margin: 0 0 6px;
  color: #0b4f74;
  font-size: 0.9rem;
  line-height: 1.25;
}
.pathway-panel p,
.pathway-panel li {
  color: #5d7084;
  font-size: 0.86rem;
  line-height: 1.55;
}
.works-panel ul {
  margin: 0;
  padding-left: 1rem;
  display: grid;
  gap: 0.3rem;
}
.works-panel a,
.works-panel a:visited {
  color: #035083;
  text-decoration: none;
  font-weight: 400 !important;
}
.works-panel a:hover {
  color: #006c96;
  text-decoration: underline;
}
.works-panel span {
  color: #7a8a9d;
}
.pathway-visuals {
  display: grid;
  gap: 10px;
}
.pathway-visuals.two-up {
  grid-template-columns: repeat(2, minmax(0, 1fr));
}
.pathway-visuals.three-up {
  grid-template-columns: 1.15fr 1fr 1fr;
}
.pathway-visual {
  margin: 0;
  border-radius: 18px;
  overflow: hidden;
  background: #f6fafc;
  border: 1px solid rgba(134, 163, 188, 0.24);
  box-shadow: inset 0 1px 0 rgba(255,255,255,0.82);
}
.pathway-visual img {
  display: block;
  width: 100%;
  aspect-ratio: 16 / 9;
  object-fit: cover;
  background: #ffffff;
}
.pathway-card:nth-child(1) .pathway-visual img,
.pathway-card:nth-child(2) .pathway-visual img,
.pathway-card:nth-child(6) .pathway-visual img {
  object-fit: contain;
  padding: 6px;
  background: #ffffff;
}
.pathway-card:nth-child(3) .pathway-visuals.three-up .pathway-visual:first-child img {
  aspect-ratio: 4 / 3;
}
.pathway-visual figcaption {
  padding: 8px 10px 10px;
  color: #697d91;
  font-size: 0.72rem;
  line-height: 1.4;
}
@media (max-width: 1120px) {
  .pathway-grid {
    grid-template-columns: 1fr;
  }
}
@media (max-width: 760px) {
  .home-structured-pathways {
    width: min(100%, calc(100% - 20px));
    margin: 40px auto 28px;
  }
  .pathway-card {
    padding: 16px;
  }
  .pathway-panels,
  .pathway-visuals.two-up,
  .pathway-visuals.three-up {
    grid-template-columns: 1fr;
  }
  .pathway-titlebar {
    grid-template-columns: 48px minmax(0, 1fr);
  }
}
/* === Homepage structured pathways v26 END === */
'''

CSS.write_text(css.rstrip() + '\n\n' + css_block.strip() + '\n', encoding='utf-8')
print('Done: replaced the long homepage pathway block with a compact structured pathway map (v26).')
