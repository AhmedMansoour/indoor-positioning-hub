from pathlib import Path
import re
import shutil

ROOT = Path('.')
INDEX = ROOT / 'index.html'
CSS = ROOT / 'assets' / 'css' / 'style.css'
ASSET_DST = ROOT / 'assets' / 'home' / 'problem-tree-v25'
BUNDLE_SRC = Path(__file__).resolve().parent.parent / 'bundle_assets' / 'problem-tree'

if not INDEX.exists():
    raise SystemExit('index.html not found. Run this script from the repository root.')
if not CSS.exists():
    raise SystemExit('assets/css/style.css not found. Run this script from the repository root.')
if not BUNDLE_SRC.exists():
    raise SystemExit('bundle_assets/problem-tree not found. Extract the full zip into the repository root first.')

ASSET_DST.mkdir(parents=True, exist_ok=True)
for item in BUNDLE_SRC.iterdir():
    if item.is_file():
        shutil.copy2(item, ASSET_DST / item.name)

index_html = INDEX.read_text(encoding='utf-8', errors='ignore')
css = CSS.read_text(encoding='utf-8', errors='ignore')

patterns = [
    r'\n\s*<!-- === Homepage key thematic extension v24 START === -->.*?<!-- === Homepage key thematic extension v24 END === -->\s*\n',
    r'\n\s*<!-- === Homepage problem tree v25 START === -->.*?<!-- === Homepage problem tree v25 END === -->\s*\n',
    r'\n\s*<section[^>]*id=["\']key-thematic-map["\'][^>]*>.*?<h2>\s*Key thematic pathways across the hub\s*</h2>.*?</section>\s*\n',
]
for pat in patterns:
    index_html = re.sub(pat, '\n', index_html, flags=re.S | re.I)

section = '''
<!-- === Homepage problem tree v25 START === -->
<section class="home-problem-tree" id="key-thematic-map">
  <div class="home-section-heading problem-tree-heading">
    <p class="eyebrow">Home · Key thematic pathways across the hub</p>
    <h2>From recurring indoor-positioning challenges to research responses</h2>
    <p>This section reorganizes the hub as a structured pathway map. Each row starts from a practical problem, shows the research direction used to address it, and links directly to the most relevant papers.</p>
  </div>

  <div class="problem-tree-list">
    <article class="problem-tree-row">
      <div class="problem-tree-index"><span>01</span></div>
      <div class="problem-tree-card">
        <div class="problem-tree-top">
          <div class="problem-tree-copy">
            <div class="problem-tree-kicker"><span class="problem-tree-symbol">🧭</span> Challenge pathway</div>
            <h3>Inertial positioning drift, heading instability, and multi-pose behavior</h3>
            <div class="problem-tree-tags"><span>PDR</span><span>heading correction</span><span>smartphone poses</span><span>step logic</span></div>
            <div class="problem-tree-flow">
              <div class="flow-box flow-problem">
                <h4>Problem</h4>
                <p>Pedestrian trajectories degrade when heading drifts and the device shifts between holding, calling, swinging, pocket, or mixed carrying modes.</p>
              </div>
              <div class="flow-arrow">→</div>
              <div class="flow-box flow-response">
                <h4>Research response</h4>
                <p>Use motion-context awareness, carrying-mode recognition, adaptive heading correction, and robust step extraction to stabilize inertial navigation.</p>
              </div>
            </div>
            <div class="problem-tree-papers">
              <h4>Representative works</h4>
              <ul>
                <li><a href="publications/hybrid-neural-network-pdr-multi-layer-heading-correction.html">Hybrid Neural Network-Based PDR with Multi-Layer Heading Correction Across Smartphone Carrying Modes</a> <span>(2026)</span></li>
                <li><a href="publications/enhancing-real-time-heading-estimation-deep-learning-smartphone-sensors.html">Enhancing Real-Time Heading Estimation for Pedestrian Navigation Using Deep Learning and Smartphone Sensors</a> <span>(2025)</span></li>
                <li><a href="publications/drift-resistant-heading-estimation-wifi-magnetic-stability.html">Drift-Resistant Heading Estimation for Smartphone-Based Indoor Positioning via Adaptive Calibration Using Wi-Fi Fingerprinting and Magnetic Stability</a> <span>(2026)</span></li>
                <li><a href="publications/drift-control-pdr-long-period-navigation-smartphone-poses.html">Drift Control of Pedestrian Dead Reckoning for Long-Period Navigation Under Multiple Smartphone Poses</a> <span>(2021)</span></li>
              </ul>
            </div>
          </div>
          <figure class="problem-tree-figure">
            <img src="assets/home/problem-tree-v25/multi_pose_behavior.webp" alt="Multi-pose pedestrian trajectories and pose-dependent inertial behavior" loading="lazy" decoding="async">
            <figcaption>Representative visualization: user pose changes and trajectory behavior.</figcaption>
          </figure>
        </div>
      </div>
    </article>

    <article class="problem-tree-row">
      <div class="problem-tree-index"><span>02</span></div>
      <div class="problem-tree-card">
        <div class="problem-tree-top">
          <div class="problem-tree-copy">
            <div class="problem-tree-kicker"><span class="problem-tree-symbol">📡</span> Challenge pathway</div>
            <h3>Radio-map scarcity, update reliability, and crowdsensed fingerprint quality</h3>
            <div class="problem-tree-tags"><span>radio maps</span><span>crowdsensing</span><span>reliability</span><span>write-back</span></div>
            <div class="problem-tree-flow">
              <div class="flow-box flow-problem">
                <h4>Problem</h4>
                <p>Initial site surveys are expensive, crowd data are noisy, and unfiltered write-back can degrade the radio map instead of improving it.</p>
              </div>
              <div class="flow-arrow">→</div>
              <div class="flow-box flow-response">
                <h4>Research response</h4>
                <p>Accumulate ordinary user data over time, infer trajectories and anchors, and admit new fingerprints only after spatial, feature, denoising, confidence, and structure checks.</p>
              </div>
            </div>
            <div class="problem-tree-papers">
              <h4>Representative works</h4>
              <ul>
                <li><a href="publications/towards-ubiquitous-ips-crowdsourced-data-accumulation.html">Towards Ubiquitous IPS: Leveraging Crowdsourced Data Accumulation Over Time to Alleviate Reliance on External Sources in Initial Fingerprinting Map Generation</a> <span>(2024)</span></li>
                <li><a href="publications/reliability-governed-3d-radio-mapping-lifecycle-review.html">Reliability-Governed Scaling of Mobile Crowdsensing-Based 3D Radio Mapping for Ubiquitous Indoor Positioning</a> <span>(2026)</span></li>
                <li><a href="publications/leveraging-human-mobility-pervasive-smartphone-crowdsourcing.html">Leveraging Human Mobility for Pervasive Smartphone Crowdsourcing in Indoor Positioning</a> <span>(2023)</span></li>
              </ul>
            </div>
          </div>
          <figure class="problem-tree-figure">
            <img src="assets/home/problem-tree-v25/radio_map_reliability.webp" alt="Reliability-governed radio map write-back flow" loading="lazy" decoding="async">
            <figcaption>Representative visualization: reliability-governed radio-map write-back.</figcaption>
          </figure>
        </div>
      </div>
    </article>

    <article class="problem-tree-row">
      <div class="problem-tree-index"><span>03</span></div>
      <div class="problem-tree-card">
        <div class="problem-tree-top">
          <div class="problem-tree-copy">
            <div class="problem-tree-kicker"><span class="problem-tree-symbol">🏢</span> Challenge pathway</div>
            <h3>3D indoor positioning and multi-floor detection</h3>
            <div class="problem-tree-tags"><span>3D assembly</span><span>multi-floor</span><span>vertical transitions</span><span>building-scale maps</span></div>
            <div class="problem-tree-flow">
              <div class="flow-box flow-problem">
                <h4>Problem</h4>
                <p>Deployment-ready IPS must connect floor-local tracks across stairs, elevators, and gates while preserving building geometry and floor identity.</p>
              </div>
              <div class="flow-arrow">→</div>
              <div class="flow-box flow-response">
                <h4>Research response</h4>
                <p>Build floor-local map skeletons, assemble them into building-local 3D structures, and refine them with anchors and structural constraints for reliable multi-floor positioning.</p>
              </div>
            </div>
            <div class="problem-tree-papers">
              <h4>Representative works</h4>
              <ul>
                <li><a href="publications/reliability-governed-3d-radio-mapping-lifecycle-review.html">Reliability-Governed Scaling of Mobile Crowdsensing-Based 3D Radio Mapping for Ubiquitous Indoor Positioning</a> <span>(2026)</span></li>
                <li><a href="publications/towards-ubiquitous-ips-crowdsourced-data-accumulation.html">Towards Ubiquitous IPS: Leveraging Crowdsourced Data Accumulation Over Time to Alleviate Reliance on External Sources in Initial Fingerprinting Map Generation</a> <span>(2024)</span></li>
                <li><a href="publications/leveraging-human-mobility-pervasive-smartphone-crowdsourcing.html">Leveraging Human Mobility for Pervasive Smartphone Crowdsourcing in Indoor Positioning</a> <span>(2023)</span></li>
              </ul>
            </div>
          </div>
          <figure class="problem-tree-figure">
            <img src="assets/home/problem-tree-v25/three_d_multifloor.webp" alt="Three-stage 3D indoor positioning and multi-floor map assembly" loading="lazy" decoding="async">
            <figcaption>Representative visualization: floor-local skeletons, 3D assembly, and global refinement.</figcaption>
          </figure>
        </div>
      </div>
    </article>

    <article class="problem-tree-row">
      <div class="problem-tree-index"><span>04</span></div>
      <div class="problem-tree-card">
        <div class="problem-tree-top">
          <div class="problem-tree-copy">
            <div class="problem-tree-kicker"><span class="problem-tree-symbol">🔄</span> Challenge pathway</div>
            <h3>Seamless indoor-outdoor continuity and multisensor context</h3>
            <div class="problem-tree-tags"><span>IOD</span><span>GNSS/PDR fusion</span><span>context descriptor</span><span>session logs</span></div>
            <div class="problem-tree-flow">
              <div class="flow-box flow-problem">
                <h4>Problem</h4>
                <p>Real-world navigation crosses indoor tracks, outdoor legs, gates, vertical transitions, and sensor dropouts, so a single sensor or fixed mode is not enough.</p>
              </div>
              <div class="flow-arrow">→</div>
              <div class="flow-box flow-response">
                <h4>Research response</h4>
                <p>Fuse Wi-Fi, IMU, magnetometer, barometer, GNSS, and app events into a context descriptor and session stream that preserves continuity across spaces and transitions.</p>
              </div>
            </div>
            <div class="problem-tree-papers">
              <h4>Representative works</h4>
              <ul>
                <li><a href="publications/suns-seamless-ubiquitous-navigation-indoor-outdoor-awareness.html">SUNS: Seamless Ubiquitous Navigation System Based on GNSS, Wi-Fi, and MEMS Sensors</a> <span>(2022)</span></li>
                <li><a href="publications/gnss-positioning-aided-with-pdr-in-urban-areas.html">GNSS Positioning Aided with Pedestrian Dead Reckoning in Urban Areas</a> <span>(2026)</span></li>
                <li><a href="publications/tightly-coupled-bluetooth-enhanced-gnss-pdr-urban.html">Tightly Coupled Bluetooth Enhanced GNSS/PDR System for Pedestrian Navigation in Dense Urban Environments</a> <span>(2024)</span></li>
                <li><a href="publications/ac-hmm-azimuth-constrained-map-matching-urban-canyons.html">AC-HMM: Azimuth-Constrained Hidden Markov Model-Based Map Matching for Robust Pedestrian Positioning in Urban Canyons</a> <span>(2026)</span></li>
              </ul>
            </div>
          </div>
          <figure class="problem-tree-figure">
            <img src="assets/home/problem-tree-v25/context_descriptor.webp" alt="Context descriptor for seamless indoor-outdoor and vertical transitions" loading="lazy" decoding="async">
            <figcaption>Representative visualization: motion state, pose, turn-stop, vertical transition, and integrity context.</figcaption>
          </figure>
        </div>
      </div>
    </article>

    <article class="problem-tree-row">
      <div class="problem-tree-index"><span>05</span></div>
      <div class="problem-tree-card">
        <div class="problem-tree-top">
          <div class="problem-tree-copy">
            <div class="problem-tree-kicker"><span class="problem-tree-symbol">👥</span> Challenge pathway</div>
            <h3>Scalable, user-centered, and crowd-powered deployment</h3>
            <div class="problem-tree-tags"><span>privacy</span><span>battery</span><span>user burden</span><span>scaling IPS</span></div>
            <div class="problem-tree-flow">
              <div class="flow-box flow-problem">
                <h4>Problem</h4>
                <p>Large-scale IPS must operate under user-governed permissions, energy limits, asynchronous sensing, cross-building variation, and low participation tolerance.</p>
              </div>
              <div class="flow-arrow">→</div>
              <div class="flow-box flow-response">
                <h4>Research response</h4>
                <p>Design low-burden, consumer-centric, self-healing, and deployment-aware IPS pipelines that remain usable with ordinary devices and real human behavior.</p>
              </div>
            </div>
            <div class="problem-tree-papers">
              <h4>Representative works</h4>
              <ul>
                <li><a href="publications/towards-scalable-ips-user-centric-crowd-powered-framework.html">Towards Scalable IPS: User-Centric Challenges, Methods, and Recommendations for User-Friendly Crowd-Powered Schemes</a> <span>(2026)</span></li>
                <li><a href="publications/modular-prompting-ai-guided-user-engagement-crowd-powered-ips.html">A Modular Prompting Framework for AI-Guided Unobtrusive User Engagement in Crowd-Powered Indoor Positioning with Semantic Knowledge Graphs and GPT-4-Based LLMs</a> <span>(2025)</span></li>
                <li><a href="publications/everywhere-framework-ubiquitous-indoor-localization.html">Everywhere: A Framework for Ubiquitous Indoor Localization</a> <span>(2022)</span></li>
                <li><a href="publications/power-of-many-multi-user-collaborative-indoor-localization.html">The Power of Many: Multi-User Collaborative Indoor Localization</a> <span>(2023)</span></li>
              </ul>
            </div>
          </div>
          <div class="problem-tree-figure-stack">
            <figure class="problem-tree-figure small-stack">
              <img src="assets/home/problem-tree-v25/deployment_realities.webp" alt="Crowd-powered deployment realities for indoor positioning" loading="lazy" decoding="async">
              <figcaption>Representative visualization: energy, privacy, user burden, and sampling realities.</figcaption>
            </figure>
            <figure class="problem-tree-figure small-stack secondary">
              <img src="assets/home/problem-tree-v25/scaling_principles.webp" alt="Principles for scaling indoor positioning systems" loading="lazy" decoding="async">
              <figcaption>Representative visualization: no dependencies, self-healing, consumer-centric, generic, and global applicability.</figcaption>
            </figure>
          </div>
        </div>
      </div>
    </article>
  </div>
</section>
<!-- === Homepage problem tree v25 END === -->
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

css = re.sub(r'/\* === Homepage problem tree v25 START === \*/.*?/\* === Homepage problem tree v25 END === \*/', '', css, flags=re.S)
css = re.sub(r'/\* === Homepage key thematic extension v24 START === \*/.*?/\* === Homepage key thematic extension v24 END === \*/', '', css, flags=re.S)

css_block = '''
/* === Homepage problem tree v25 START === */
.home-problem-tree {
  width: min(1220px, calc(100% - 32px));
  margin: 56px auto 36px;
}
.problem-tree-heading {
  max-width: 930px;
  margin: 0 auto 26px;
  text-align: center;
}
.problem-tree-heading h2 {
  margin: 0.2rem 0 0.6rem;
  font-size: clamp(1.75rem, 2.7vw, 2.7rem);
  letter-spacing: -0.04em;
}
.problem-tree-heading p:not(.eyebrow) {
  color: #5f7287;
  font-size: 0.98rem;
  line-height: 1.68;
}
.problem-tree-list {
  display: grid;
  gap: 22px;
}
.problem-tree-row {
  display: grid;
  grid-template-columns: 76px minmax(0, 1fr);
  gap: 16px;
  align-items: stretch;
}
.problem-tree-index {
  position: relative;
  display: flex;
  justify-content: center;
}
.problem-tree-index::after {
  content: '';
  position: absolute;
  top: 72px;
  bottom: -22px;
  width: 2px;
  background: linear-gradient(180deg, rgba(84, 194, 204, 0.35), rgba(131, 104, 243, 0.22));
}
.problem-tree-row:last-child .problem-tree-index::after {
  display: none;
}
.problem-tree-index span {
  width: 52px;
  height: 52px;
  border-radius: 18px;
  display: grid;
  place-items: center;
  font-weight: 800;
  color: #0b5175;
  background: linear-gradient(135deg, rgba(104, 207, 216, 0.18), rgba(152, 109, 255, 0.14));
  border: 1px solid rgba(111, 163, 202, 0.34);
  box-shadow: 0 14px 28px rgba(29, 64, 95, 0.08);
}
.problem-tree-card {
  border-radius: 28px;
  padding: 22px;
  background: linear-gradient(180deg, rgba(255,255,255,0.94), rgba(249,252,255,0.96));
  border: 1px solid rgba(135, 164, 191, 0.26);
  box-shadow: 0 22px 50px rgba(17, 45, 74, 0.08);
  overflow: hidden;
}
.problem-tree-top {
  display: grid;
  grid-template-columns: minmax(0, 1.3fr) minmax(340px, 0.95fr);
  gap: 22px;
  align-items: start;
}
.problem-tree-copy h3 {
  margin: 0.25rem 0 0.65rem;
  color: #083d63;
  font-size: clamp(1.2rem, 1.8vw, 1.65rem);
  line-height: 1.22;
  letter-spacing: -0.028em;
}
.problem-tree-kicker {
  display: inline-flex;
  align-items: center;
  gap: 8px;
  padding: 0.42rem 0.78rem;
  border-radius: 999px;
  background: rgba(119, 210, 218, 0.12);
  color: #0a627f;
  font-size: 0.84rem;
  font-weight: 700;
  letter-spacing: 0.01em;
}
.problem-tree-symbol { font-size: 1rem; }
.problem-tree-tags {
  display: flex;
  flex-wrap: wrap;
  gap: 8px;
  margin: 0 0 14px;
}
.problem-tree-tags span {
  padding: 0.38rem 0.7rem;
  border-radius: 999px;
  background: rgba(232, 239, 245, 0.92);
  border: 1px solid rgba(147, 171, 192, 0.22);
  color: #51667a;
  font-size: 0.78rem;
  font-weight: 600;
}
.problem-tree-flow {
  display: grid;
  grid-template-columns: minmax(0, 1fr) 40px minmax(0, 1fr);
  gap: 10px;
  align-items: stretch;
  margin-bottom: 16px;
}
.flow-box {
  border-radius: 20px;
  padding: 15px 16px;
  border: 1px solid rgba(132, 160, 184, 0.22);
  min-height: 100%;
}
.flow-problem { background: linear-gradient(180deg, rgba(235, 245, 251, 0.88), rgba(247, 250, 253, 0.95)); }
.flow-response { background: linear-gradient(180deg, rgba(242, 239, 255, 0.86), rgba(250, 248, 255, 0.95)); }
.flow-box h4, .problem-tree-papers h4 {
  margin: 0 0 6px;
  color: #0b4f74;
  font-size: 0.89rem;
  line-height: 1.25;
}
.flow-box p {
  margin: 0;
  color: #5d7084;
  font-size: 0.9rem;
  line-height: 1.62;
}
.flow-arrow {
  display: grid;
  place-items: center;
  font-size: 1.35rem;
  color: #5d7fa0;
  font-weight: 800;
}
.problem-tree-papers {
  border-top: 1px dashed rgba(136, 163, 186, 0.42);
  padding-top: 12px;
}
.problem-tree-papers ul {
  margin: 0;
  padding-left: 1.05rem;
  display: grid;
  gap: 0.32rem;
}
.problem-tree-papers li {
  color: #1a3852;
  font-size: 0.84rem;
  line-height: 1.48;
}
.problem-tree-papers a, .problem-tree-papers a:visited {
  color: #035083;
  font-weight: 400 !important;
  text-decoration: none;
}
.problem-tree-papers a:hover { color: #006c96; text-decoration: underline; }
.problem-tree-papers span { color: #7a8a9d; }
.problem-tree-figure, .problem-tree-figure.small-stack {
  margin: 0;
  border-radius: 24px;
  overflow: hidden;
  border: 1px solid rgba(134, 163, 188, 0.24);
  background: #f4f8fb;
  box-shadow: inset 0 1px 0 rgba(255,255,255,0.82);
}
.problem-tree-figure img, .problem-tree-figure.small-stack img {
  display: block;
  width: 100%;
  height: auto;
}
.problem-tree-figure figcaption, .problem-tree-figure.small-stack figcaption {
  padding: 10px 14px 12px;
  color: #697d91;
  font-size: 0.76rem;
  line-height: 1.45;
  background: linear-gradient(180deg, rgba(251,253,255,0.86), rgba(245,249,252,0.96));
}
.problem-tree-figure-stack { display: grid; gap: 14px; }
.problem-tree-figure-stack .secondary figcaption {
  background: linear-gradient(180deg, rgba(252,250,255,0.92), rgba(247,245,255,0.96));
}
@media (max-width: 1080px) {
  .problem-tree-top { grid-template-columns: 1fr; }
  .problem-tree-figure, .problem-tree-figure.small-stack { max-width: 860px; }
}
@media (max-width: 820px) {
  .problem-tree-row { grid-template-columns: 1fr; }
  .problem-tree-index { justify-content: flex-start; }
  .problem-tree-index::after { display: none; }
  .problem-tree-card { padding: 18px; }
  .problem-tree-flow { grid-template-columns: 1fr; }
  .flow-arrow { transform: rotate(90deg); min-height: 24px; }
}
/* === Homepage problem tree v25 END === */
'''

CSS.write_text(css.rstrip() + '\n\n' + css_block.strip() + '\n', encoding='utf-8')
print('Done: replaced the old homepage thematic block with a problem-tree style section on the homepage.')
