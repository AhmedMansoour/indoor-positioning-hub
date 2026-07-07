from pathlib import Path
import re
import shutil

ROOT = Path('.')
INDEX = ROOT / 'index.html'
CSS = ROOT / 'assets' / 'css' / 'style.css'
ASSET_DST = ROOT / 'assets' / 'home' / 'pathways-v27'
BUNDLE_SRC = Path(__file__).resolve().parent.parent / 'bundle_assets' / 'pathways-v27'

if not INDEX.exists():
    raise SystemExit('index.html not found. Run this script from the repository root.')
if not CSS.exists():
    raise SystemExit('assets/css/style.css not found. Run this script from the repository root.')
if not BUNDLE_SRC.exists():
    raise SystemExit('bundle_assets/pathways-v27 not found. Extract the full zip into the repository root first.')

ASSET_DST.mkdir(parents=True, exist_ok=True)
for item in BUNDLE_SRC.iterdir():
    if item.is_file():
        shutil.copy2(item, ASSET_DST / item.name)

index_html = INDEX.read_text(encoding='utf-8', errors='ignore')
css = CSS.read_text(encoding='utf-8', errors='ignore')

# Remove older homepage thematic/pathway blocks.
html_patterns = [
    r'\n\s*<!-- === Homepage key thematic extension v24 START === -->.*?<!-- === Homepage key thematic extension v24 END === -->\s*\n',
    r'\n\s*<!-- === Homepage problem tree v25 START === -->.*?<!-- === Homepage problem tree v25 END === -->\s*\n',
    r'\n\s*<!-- === Homepage structured pathways v26 START === -->.*?<!-- === Homepage structured pathways v26 END === -->\s*\n',
    r'\n\s*<!-- === Homepage visual problem rows v27 START === -->.*?<!-- === Homepage visual problem rows v27 END === -->\s*\n',
    r'\n\s*<section[^>]*id=["\']key-thematic-map["\'][^>]*>.*?</section>\s*\n',
]
for pat in html_patterns:
    index_html = re.sub(pat, '\n', index_html, flags=re.S | re.I)

section = '''
<!-- === Homepage visual problem rows v27 START === -->
<section class="home-pathway-rows" id="key-thematic-map">
  <div class="home-section-heading pathway-rows-heading">
    <p class="eyebrow">Home · Key thematic pathways across the hub</p>
    <h2>Structured pathway map</h2>
    <p>This visual pathway map is organized around recurring indoor-positioning problems. Each row highlights one challenge and the representative works connected to it, while the figures carry most of the visual message.</p>
  </div>

  <div class="problem-row-list">

    <article class="problem-row-card">
      <div class="problem-row-copy">
        <div class="problem-row-meta"><span class="problem-row-no">01</span><span class="problem-row-tag">🧭 Motion stability</span></div>
        <h3>Inertial positioning drift, heading instability, and multi-pose user behavior</h3>
        <div class="problem-mini-box">
          <h4>Problem</h4>
          <p>Pedestrian trajectories drift when heading error accumulates and the phone changes across holding, calling, swinging, pocket, and mixed carrying behaviors.</p>
        </div>
        <div class="works-mini-box">
          <h4>Representative works</h4>
          <ul>
            <li><a href="publications/hybrid-neural-network-pdr-multi-layer-heading-correction.html">Hybrid Neural Network-Based PDR with Multi-Layer Heading Correction Across Smartphone Carrying Modes</a> <span>(2026)</span></li>
            <li><a href="publications/enhancing-real-time-heading-estimation-deep-learning-smartphone-sensors.html">Enhancing Real-Time Heading Estimation for Pedestrian Navigation Using Deep Learning and Smartphone Sensors</a> <span>(2025)</span></li>
            <li><a href="publications/drift-control-pdr-long-period-navigation-smartphone-poses.html">Drift Control of Pedestrian Dead Reckoning for Long-Period Navigation Under Different Smartphone Poses</a> <span>(2021)</span></li>
          </ul>
        </div>
      </div>
      <div class="problem-row-visuals two-visuals">
        <figure class="pathway-shot landscape"><img src="assets/home/pathways-v27/pose_route.webp" alt="Pose-dependent trajectories for holding, calling, swinging, and in-pocket smartphone usage" loading="lazy" decoding="async"></figure>
        <figure class="pathway-shot landscape"><img src="assets/home/pathways-v27/pose_peaks.webp" alt="Step peaks and valleys across multiple smartphone poses" loading="lazy" decoding="async"></figure>
      </div>
    </article>

    <article class="problem-row-card">
      <div class="problem-row-copy">
        <div class="problem-row-meta"><span class="problem-row-no">02</span><span class="problem-row-tag">📶 Fingerprinting integrity</span></div>
        <h3>Fingerprint uncertainty, heading calibration, and robust Wi-Fi plus inertial fusion</h3>
        <div class="problem-mini-box">
          <h4>Problem</h4>
          <p>Fingerprint fixes are not equally reliable, and inertial heading must be calibrated carefully when Wi-Fi matches are unstable or intermittently trustworthy.</p>
        </div>
        <div class="works-mini-box">
          <h4>Representative works</h4>
          <ul>
            <li><a href="publications/drift-resistant-heading-estimation-wifi-magnetic-stability.html">Drift-Resistant Heading Estimation for Smartphone-Based Indoor Positioning via Adaptive Calibration Using Wi-Fi Fingerprinting and Magnetic Stability</a> <span>(2026)</span></li>
            <li><a href="publications/everywhere-framework-ubiquitous-indoor-localization.html">Everywhere: A Framework for Ubiquitous Indoor Localization</a> <span>(2022)</span></li>
            <li><a href="publications/power-of-many-multi-user-collaborative-indoor-localization.html">The Power of Many: Multi-User Collaborative Indoor Localization</a> <span>(2023)</span></li>
          </ul>
        </div>
      </div>
      <div class="problem-row-visuals two-visuals">
        <figure class="pathway-shot landscape"><img src="assets/home/pathways-v27/heading_calibration.webp" alt="Conceptual diagram of heading calibration using qualified Wi-Fi fingerprinting positions" loading="lazy" decoding="async"></figure>
        <figure class="pathway-shot landscape"><img src="assets/home/pathways-v27/heading_framework.webp" alt="System framework combining motion analysis and Wi-Fi fingerprinting for heading calibration" loading="lazy" decoding="async"></figure>
      </div>
    </article>

    <article class="problem-row-card">
      <div class="problem-row-copy">
        <div class="problem-row-meta"><span class="problem-row-no">03</span><span class="problem-row-tag">🏢 3D scaling</span></div>
        <h3>3D indoor positioning, multi-floor detection, and scalable radio-map generation</h3>
        <div class="problem-mini-box">
          <h4>Problem</h4>
          <p>Building-scale IPS must connect floor-local tracks, infer vertical transitions, and generate usable radio maps without full manual surveys on every floor.</p>
        </div>
        <div class="works-mini-box">
          <h4>Representative works</h4>
          <ul>
            <li><a href="publications/reliability-governed-3d-radio-mapping-lifecycle-review.html">Reliability-Governed Scaling of Mobile Crowdsensing-Based 3D Radio Mapping for Ubiquitous Indoor Positioning</a> <span>(2026)</span></li>
            <li><a href="publications/towards-ubiquitous-ips-crowdsourced-data-accumulation.html">Towards Ubiquitous IPS: Leveraging Crowdsourced Data Accumulation Over Time to Alleviate Reliance on External Sources in Initial Fingerprinting Map Generation</a> <span>(2024)</span></li>
            <li><a href="publications/leveraging-human-mobility-pervasive-smartphone-crowdsourcing.html">Leveraging Human Mobility and Pervasive Smartphone Measurements-Based Crowdsourcing for Developing Self-Deployable and Ubiquitous Indoor Positioning Systems</a> <span>(2023)</span></li>
          </ul>
        </div>
      </div>
      <div class="problem-row-visuals three-visuals">
        <figure class="pathway-shot portraitish"><img src="assets/home/pathways-v27/layered_building.webp" alt="Layered building visualization for smart building positioning" loading="lazy" decoding="async"></figure>
        <figure class="pathway-shot landscape"><img src="assets/home/pathways-v27/radio_map_process.webp" alt="Illustration of crowdsourced radio-map generation processes" loading="lazy" decoding="async"></figure>
        <figure class="pathway-shot landscape"><img src="assets/home/pathways-v27/raw_crowd_radio_map.webp" alt="Raw crowdsourced data converted to a radio map" loading="lazy" decoding="async"></figure>
      </div>
    </article>

    <article class="problem-row-card">
      <div class="problem-row-copy">
        <div class="problem-row-meta"><span class="problem-row-no">04</span><span class="problem-row-tag">🔄 Seamless continuity</span></div>
        <h3>Indoor-outdoor continuity, multisensor context, and seamless trajectory fusion</h3>
        <div class="problem-mini-box">
          <h4>Problem</h4>
          <p>Navigation traces cross indoor areas, outdoor legs, vertical transitions, and sensor gaps, so the system must preserve continuity across changing context and coverage.</p>
        </div>
        <div class="works-mini-box">
          <h4>Representative works</h4>
          <ul>
            <li><a href="publications/suns-seamless-ubiquitous-navigation-indoor-outdoor-awareness.html">SUNS: Seamless Ubiquitous Navigation System Based on GNSS, Wi-Fi, and MEMS Sensors</a> <span>(2022)</span></li>
            <li><a href="publications/gnss-positioning-aided-with-pdr-in-urban-areas.html">GNSS Positioning Aided with Pedestrian Dead Reckoning in Urban Areas</a> <span>(2026)</span></li>
            <li><a href="publications/tightly-coupled-bluetooth-enhanced-gnss-pdr-urban.html">Tightly Coupled Bluetooth Enhanced GNSS/PDR System for Pedestrian Navigation in Dense Urban Environments</a> <span>(2024)</span></li>
            <li><a href="publications/ac-hmm-azimuth-constrained-map-matching-urban-canyons.html">AC-HMM: Azimuth-Constrained Hidden Markov Model-Based Map Matching for Robust Pedestrian Positioning in Urban Canyons</a> <span>(2026)</span></li>
          </ul>
        </div>
      </div>
      <div class="problem-row-visuals two-visuals">
        <figure class="pathway-shot landscape"><img src="assets/home/pathways-v27/context_descriptor.webp" alt="Context descriptor and multisensor session log stream for seamless positioning" loading="lazy" decoding="async"></figure>
        <figure class="pathway-shot landscape"><img src="assets/home/pathways-v27/seamless_tracks.webp" alt="Seamless positioning performance across different tracks" loading="lazy" decoding="async"></figure>
      </div>
    </article>

    <article class="problem-row-card">
      <div class="problem-row-copy">
        <div class="problem-row-meta"><span class="problem-row-no">05</span><span class="problem-row-tag">🗺️ Geometric reconstruction</span></div>
        <h3>Path ambiguity, site geometry, and reconstruction of difficult trajectories</h3>
        <div class="problem-mini-box">
          <h4>Problem</h4>
          <p>Crowdsensed tracks are noisy and spatially ambiguous, especially in loops, intersections, and irregular corridors where map structure must be recovered from imperfect traces.</p>
        </div>
        <div class="works-mini-box">
          <h4>Representative works</h4>
          <ul>
            <li><a href="publications/reliability-governed-3d-radio-mapping-lifecycle-review.html">Reliability-Governed Scaling of Mobile Crowdsensing-Based 3D Radio Mapping for Ubiquitous Indoor Positioning</a> <span>(2026)</span></li>
            <li><a href="publications/towards-ubiquitous-ips-crowdsourced-data-accumulation.html">Towards Ubiquitous IPS: Leveraging Crowdsourced Data Accumulation Over Time to Alleviate Reliance on External Sources in Initial Fingerprinting Map Generation</a> <span>(2024)</span></li>
            <li><a href="publications/leveraging-human-mobility-pervasive-smartphone-crowdsourcing.html">Leveraging Human Mobility and Pervasive Smartphone Measurements-Based Crowdsourcing for Developing Self-Deployable and Ubiquitous Indoor Positioning Systems</a> <span>(2023)</span></li>
          </ul>
        </div>
      </div>
      <div class="problem-row-visuals two-visuals">
        <figure class="pathway-shot portraitish"><img src="assets/home/pathways-v27/trajectory_floorplan.webp" alt="Noisy crowdsensed trajectories overlaid on a building floor plan" loading="lazy" decoding="async"></figure>
        <figure class="pathway-shot landscape"><img src="assets/home/pathways-v27/radio_map_process.webp" alt="Structured process for turning tracks into radio-map components" loading="lazy" decoding="async"></figure>
      </div>
    </article>

    <article class="problem-row-card">
      <div class="problem-row-copy">
        <div class="problem-row-meta"><span class="problem-row-no">06</span><span class="problem-row-tag">👥 Deployment scaling</span></div>
        <h3>User-centered scaling, privacy, energy limits, and real deployment constraints</h3>
        <div class="problem-mini-box">
          <h4>Problem</h4>
          <p>Large-scale IPS must remain usable under privacy preferences, battery constraints, sparse participation, and the variability of ordinary devices and user behavior.</p>
        </div>
        <div class="works-mini-box">
          <h4>Representative works</h4>
          <ul>
            <li><a href="publications/towards-scalable-ips-user-centric-crowd-powered-framework.html">Towards Scalable IPS: User-Centric Challenges, Methods, and Recommendations for User-Friendly Crowd-Powered Schemes</a> <span>(2026)</span></li>
            <li><a href="publications/modular-prompting-ai-guided-user-engagement-crowd-powered-ips.html">A Modular Prompting Framework for AI-Guided Unobtrusive User Engagement in Crowd-Powered Indoor Positioning with Semantic Knowledge Graphs and GPT-4-Based LLMs</a> <span>(2025)</span></li>
            <li><a href="publications/everywhere-framework-ubiquitous-indoor-localization.html">Everywhere: A Framework for Ubiquitous Indoor Localization</a> <span>(2022)</span></li>
          </ul>
        </div>
      </div>
      <div class="problem-row-visuals two-visuals">
        <figure class="pathway-shot landscape"><img src="assets/home/pathways-v27/deployment_realities.webp" alt="Deployment realities including energy use, privacy, and building differences" loading="lazy" decoding="async"></figure>
        <figure class="pathway-shot landscape"><img src="assets/home/pathways-v27/scaling_principles.webp" alt="Principles for scaling indoor positioning systems" loading="lazy" decoding="async"></figure>
      </div>
    </article>

  </div>
</section>
<!-- === Homepage visual problem rows v27 END === -->
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
css = re.sub(r'/\* === Homepage visual problem rows v27 START === \*/.*?/\* === Homepage visual problem rows v27 END === \*/', '', css, flags=re.S)

css_block = '''
/* === Homepage visual problem rows v27 START === */
.home-pathway-rows {
  width: min(1180px, calc(100% - 28px));
  margin: 56px auto 42px;
}
.pathway-rows-heading {
  max-width: 960px;
  margin: 0 auto 22px;
  text-align: center;
}
.pathway-rows-heading h2 {
  margin: 0.2rem 0 0.55rem;
  font-size: clamp(1.9rem, 2.9vw, 2.7rem);
  letter-spacing: -0.04em;
}
.pathway-rows-heading p:not(.eyebrow) {
  color: #617488;
  line-height: 1.7;
}
.problem-row-list {
  display: grid;
  gap: 18px;
}
.problem-row-card {
  position: relative;
  display: grid;
  grid-template-columns: minmax(280px, 0.9fr) minmax(420px, 1.55fr);
  gap: 18px;
  align-items: stretch;
  padding: 20px;
  border-radius: 30px;
  background: linear-gradient(180deg, rgba(255,255,255,0.96), rgba(248,251,255,0.98));
  border: 1px solid rgba(129, 161, 190, 0.24);
  box-shadow: 0 18px 40px rgba(19, 43, 74, 0.08);
  overflow: hidden;
}
.problem-row-card::before {
  content: '';
  position: absolute;
  inset: 0 auto 0 0;
  width: 4px;
  background: linear-gradient(180deg, #5ad1d0, #8b6ff3);
}
.problem-row-copy {
  display: grid;
  gap: 12px;
  align-content: start;
}
.problem-row-meta {
  display: flex;
  align-items: center;
  gap: 10px;
  flex-wrap: wrap;
}
.problem-row-no {
  display: grid;
  place-items: center;
  width: 42px;
  height: 42px;
  border-radius: 14px;
  background: linear-gradient(135deg, rgba(99, 205, 216, 0.18), rgba(141, 112, 244, 0.15));
  border: 1px solid rgba(112, 158, 194, 0.28);
  color: #0b5679;
  font-size: 0.9rem;
  font-weight: 800;
}
.problem-row-tag {
  display: inline-flex;
  align-items: center;
  gap: 0.35rem;
  padding: 0.44rem 0.8rem;
  border-radius: 999px;
  background: rgba(83, 197, 213, 0.10);
  border: 1px solid rgba(95, 167, 194, 0.22);
  color: #0a647e;
  font-size: 0.8rem;
  font-weight: 700;
}
.problem-row-card h3 {
  margin: 0;
  color: #083d63;
  font-size: clamp(1.14rem, 1.55vw, 1.45rem);
  line-height: 1.28;
  letter-spacing: -0.02em;
}
.problem-mini-box,
.works-mini-box {
  border-radius: 18px;
  padding: 13px 14px;
  border: 1px solid rgba(128, 158, 183, 0.18);
}
.problem-mini-box {
  background: linear-gradient(180deg, rgba(236,245,251,0.92), rgba(247,250,253,0.96));
}
.works-mini-box {
  background: linear-gradient(180deg, rgba(244,241,255,0.90), rgba(250,248,255,0.96));
}
.problem-mini-box h4,
.works-mini-box h4 {
  margin: 0 0 0.35rem;
  color: #0b5073;
  font-size: 0.88rem;
}
.problem-mini-box p,
.works-mini-box li,
.works-mini-box span {
  color: #617489;
  font-size: 0.84rem;
  line-height: 1.55;
}
.works-mini-box ul {
  margin: 0;
  padding-left: 1rem;
  display: grid;
  gap: 0.25rem;
}
.works-mini-box a,
.works-mini-box a:visited {
  color: #035082;
  text-decoration: none;
  font-weight: 400 !important;
}
.works-mini-box a:hover { color: #00709c; text-decoration: underline; }
.problem-row-visuals {
  min-width: 0;
  display: grid;
  gap: 12px;
  align-self: stretch;
}
.problem-row-visuals.two-visuals {
  grid-template-columns: repeat(2, minmax(0, 1fr));
}
.problem-row-visuals.three-visuals {
  grid-template-columns: 0.86fr 1fr 1fr;
}
.pathway-shot {
  margin: 0;
  border-radius: 22px;
  overflow: hidden;
  border: 1px solid rgba(127, 160, 186, 0.22);
  background: linear-gradient(180deg, rgba(255,255,255,0.98), rgba(248,250,253,0.98));
  box-shadow: 0 10px 24px rgba(20, 44, 74, 0.06);
}
.pathway-shot img {
  display: block;
  width: 100%;
  height: 100%;
  object-fit: cover;
  background: #ffffff;
}
.pathway-shot.landscape {
  min-height: 250px;
}
.pathway-shot.portraitish {
  min-height: 250px;
}
.problem-row-card:nth-child(1) .pathway-shot img,
.problem-row-card:nth-child(2) .pathway-shot img,
.problem-row-card:nth-child(6) .pathway-shot img {
  object-fit: contain;
  padding: 6px;
}
.problem-row-card:nth-child(3) .pathway-shot.portraitish {
  min-height: 265px;
}
.problem-row-card:nth-child(5) .pathway-shot.portraitish {
  min-height: 280px;
}
@media (max-width: 1100px) {
  .problem-row-card {
    grid-template-columns: 1fr;
  }
  .problem-row-copy { order: 2; }
  .problem-row-visuals { order: 1; }
}
@media (max-width: 760px) {
  .home-pathway-rows {
    width: min(100%, calc(100% - 18px));
    margin: 40px auto 28px;
  }
  .problem-row-card {
    padding: 16px;
    border-radius: 24px;
  }
  .problem-row-visuals.two-visuals,
  .problem-row-visuals.three-visuals {
    grid-template-columns: 1fr;
  }
  .pathway-shot.landscape,
  .pathway-shot.portraitish {
    min-height: 210px;
  }
}
/* === Homepage visual problem rows v27 END === */
'''

CSS.write_text(css.rstrip() + '\n\n' + css_block.strip() + '\n', encoding='utf-8')
print('Done: inserted the visual-first one-row-per-problem homepage pathway layout (v27).')
