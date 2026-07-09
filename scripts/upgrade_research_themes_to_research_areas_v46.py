from pathlib import Path
import re

ROOT = Path(".")
PAGE = ROOT / "research-themes.html"
CSS = ROOT / "assets" / "css" / "style.css"
LLMS = ROOT / "llms.txt"

if not PAGE.exists():
    raise SystemExit("research-themes.html not found. Run from repository root.")
if not CSS.exists():
    raise SystemExit("assets/css/style.css not found. Run from repository root.")

html = PAGE.read_text(encoding="utf-8", errors="ignore")
css = CSS.read_text(encoding="utf-8", errors="ignore")

header = ""
footer = ""
header_match = re.search(r"<body[^>]*>\s*(<header.*?</header>)", html, flags=re.S | re.I)
if header_match:
    header = header_match.group(1)

footer_match = re.search(r"(<footer.*?</footer>)", html, flags=re.S | re.I)
if footer_match:
    footer = footer_match.group(1)

if not header:
    header = """<header class="site-header">
  <a class="brand" href="index.html">Indoor Positioning Hub</a>
  <nav class="site-nav" aria-label="Main navigation">
    <a href="index.html">Home</a>
    <a href="publications.html">Publications</a>
    <a href="research-themes.html" class="active">Research Themes</a>
    <a href="resources.html">Datasets &amp; Code</a>
    <a href="citation-resources.html">Citation Resources</a>
    <a href="about.html">About</a>
  </nav>
</header>"""

if not footer:
    footer = """<footer class="site-footer"><div class="container"><p>© <span id="year"></span> Ahmed Mansour. Indoor Positioning Research, Engineering, and Deployment Hub.</p></div></footer>"""

header = re.sub(r'(<a href="research-themes\.html")([^>]*)>', r'\1 class="active">', header, flags=re.I)
header = re.sub(r'(<a href="index\.html")\s+class="active"([^>]*)>', r'\1\2>', header, flags=re.I)

head = """<head>
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width, initial-scale=1">
  <!-- === Research areas SEO metadata v46 START === -->
  <title>Research Areas | Indoor Positioning Hub | Ahmed Mansour</title>
  <meta name="description" content="Research-area landing page for Ahmed Mansour's Indoor Positioning Hub, connecting inertial positioning, Wi-Fi fingerprinting, seamless indoor-outdoor fusion, 3D radio-map generation, vertical positioning, and deployment-ready indoor spatial intelligence.">
  <meta name="author" content="Ahmed Mansour">
  <meta name="keywords" content="indoor positioning, indoor localization, indoor navigation, PDR, Wi-Fi fingerprinting, mobile crowdsensing, radio map generation, 3D radio map, seamless indoor-outdoor positioning, GNSS/PDR integration, floor recognition, vertical positioning, spatial intelligence, Ahmed Mansour">
  <link rel="canonical" href="https://ahmedmansoour.github.io/indoor-positioning-hub/research-themes.html">
  <meta property="og:title" content="Research Areas | Indoor Positioning Hub | Ahmed Mansour">
  <meta property="og:description" content="A structured map of Ahmed Mansour's research program across inertial positioning, Wi-Fi fingerprinting, seamless fusion, and 3D radio-map generation.">
  <meta property="og:type" content="website">
  <meta property="og:url" content="https://ahmedmansoour.github.io/indoor-positioning-hub/research-themes.html">
  <meta property="og:image" content="https://ahmedmansoour.github.io/indoor-positioning-hub/assets/home/research-area4-v42/skeleton-assembly-refinement.webp">
  <meta name="twitter:card" content="summary_large_image">
  <meta name="twitter:title" content="Research Areas | Indoor Positioning Hub | Ahmed Mansour">
  <meta name="twitter:description" content="A structured research-area map for indoor positioning, PDR, Wi-Fi fingerprinting, seamless positioning, and 3D radio mapping.">
  <meta name="twitter:image" content="https://ahmedmansoour.github.io/indoor-positioning-hub/assets/home/research-area4-v42/skeleton-assembly-refinement.webp">
  <script type="application/ld+json">{
    "@context": "https://schema.org",
    "@type": "CollectionPage",
    "name": "Research Areas | Indoor Positioning Hub | Ahmed Mansour",
    "url": "https://ahmedmansoour.github.io/indoor-positioning-hub/research-themes.html",
    "description": "Research-area landing page connecting Ahmed Mansour's indoor positioning publications across inertial positioning, Wi-Fi fingerprinting, seamless indoor-outdoor positioning, and 3D radio-map generation.",
    "isPartOf": {
      "@type": "WebSite",
      "name": "Indoor Positioning Hub",
      "url": "https://ahmedmansoour.github.io/indoor-positioning-hub/"
    },
    "about": [
      "Indoor positioning",
      "Pedestrian dead reckoning",
      "Wi-Fi fingerprinting",
      "Mobile crowdsensing",
      "Seamless indoor-outdoor positioning",
      "3D radio-map generation",
      "Floor recognition",
      "Vertical positioning"
    ],
    "mainEntity": {
      "@type": "ItemList",
      "itemListElement": [
        {"@type": "ListItem", "position": 1, "name": "Enhancing Inertial Positioning Performance"},
        {"@type": "ListItem", "position": 2, "name": "Scaling Wi-Fi Fingerprinting and Autonomous Radio-Map Generation"},
        {"@type": "ListItem", "position": 3, "name": "Seamless Indoor-Outdoor Positioning and Multi-Source Fusion"},
        {"@type": "ListItem", "position": 4, "name": "3D Radio-Map Generation from Mobile Crowdsensing"}
      ]
    }
  }</script>
  <!-- === Research areas SEO metadata v46 END === -->
  <link rel="stylesheet" href="assets/css/style.css">
</head>"""

body = r"""<body class="research-areas-v46-page">
""" + header + r"""

<main class="research-areas-v46">
  <section class="ra46-hero">
    <p class="ra46-eyebrow">Research Areas and Publication Map</p>
    <h1>Research areas across the Indoor Positioning Hub</h1>
    <p class="ra46-lead">This page connects the publication portfolio to four research areas that structure Ahmed Mansour's work: inertial positioning, Wi-Fi fingerprinting and radio-map scaling, seamless indoor-outdoor fusion, and 3D indoor spatial context. The goal is to help readers move from a broad positioning question to the most relevant papers, methods, figures, and citation records.</p>
    <div class="ra46-quicklinks" aria-label="Research-area quick links">
      <a href="#area-inertial">Inertial positioning</a>
      <a href="#area-radio-map">Wi-Fi and radio maps</a>
      <a href="#area-seamless">Seamless fusion</a>
      <a href="#area-3d">3D spatial context</a>
      <a href="publications.html">Publication portfolio</a>
    </div>
  </section>

  <section class="ra46-flow" aria-label="Research program flow">
    <article><span>01</span><strong>Relative motion</strong><p>Smartphone inertial sensing keeps the trajectory alive when external positioning cues are weak or unavailable.</p></article>
    <article><span>02</span><strong>Indoor reference</strong><p>Wi-Fi fingerprints and radio maps provide indoor absolute references for correction, initialization, and map-based services.</p></article>
    <article><span>03</span><strong>Continuity</strong><p>GNSS, PDR, Wi-Fi, BLE, barometer, maps, and transition awareness are fused to prevent positioning breaks.</p></article>
    <article><span>04</span><strong>3D context</strong><p>Floor recognition, vertical motion, and building-level map assembly connect positioning to multi-level indoor structure.</p></article>
  </section>

  <section class="ra46-area" id="area-inertial">
    <div class="ra46-area-head">
      <p class="ra46-eyebrow">Research Area 1</p>
      <h2>Enhancing Inertial Positioning Performance</h2>
      <p>Smartphone inertial sensing is the relative-motion layer of pedestrian navigation. It supports positioning when GNSS, Wi-Fi, BLE, vision, or map-based cues are weak, intermittent, or unavailable. The central challenge is to control drift, heading error, pose changes, and walking-direction uncertainty without requiring dedicated infrastructure.</p>
    </div>
    <div class="ra46-area-grid">
      <figure><img src="assets/home/research-area1-v38/inertial-multipose-route-rotated.webp" alt="Inertial positioning and smartphone pedestrian dead reckoning across carrying poses" loading="lazy" decoding="async"></figure>
      <div class="ra46-card"><h3>Key problems</h3><ul><li>Heading initialization and long-term gyroscope drift.</li><li>Phone-to-body frame alignment under changing carrying modes.</li><li>Magnetic disturbance in steel-rich, electronic, and reinforced indoor spaces.</li><li>Periodic correction from GNSS, Wi-Fi, BLE, maps, or trusted observations.</li></ul></div>
    </div>
    <div class="ra46-papers"><h3>Linked publications</h3><ul>
      <li><a href="publications/drift-control-pdr-long-period-navigation-smartphone-poses.html">Drift Control of Pedestrian Dead Reckoning for Long Period Navigation under Different Smartphone Poses</a> <span>2021</span></li>
      <li><a href="publications/enhancing-real-time-heading-estimation-deep-learning-smartphone-sensors.html">Enhancing Real-Time Heading Estimation for Pedestrian Navigation via Deep Learning and Smartphone Embedded Sensors</a> <span>2025</span></li>
      <li><a href="publications/hybrid-neural-network-pdr-multi-layer-heading-correction.html">Hybrid Neural Network-Based PDR with Multi-Layer Heading Correction Across Smartphone Carrying Modes</a> <span>2026</span></li>
      <li><a href="publications/gnss-positioning-aided-with-pdr-in-urban-areas.html">GNSS Positioning Aided with Pedestrian Dead Reckoning in Urban Areas</a> <span>2026</span></li>
      <li><a href="publications/tightly-coupled-bluetooth-enhanced-gnss-pdr-urban.html">Tightly Coupled Bluetooth Enhanced GNSS/PDR System for Pedestrian Navigation in Dense Urban Environments</a> <span>2024</span></li>
      <li><a href="publications/ac-hmm-azimuth-constrained-map-matching-urban-canyons.html">AC-HMM: Azimuth-Constrained Hidden Markov Model-Based Map Matching for Robust Pedestrian Positioning in Urban Canyons</a> <span>2026</span></li>
    </ul></div>
  </section>

  <section class="ra46-area" id="area-radio-map">
    <div class="ra46-area-head">
      <p class="ra46-eyebrow">Research Area 2</p>
      <h2>Scaling Wi-Fi Fingerprinting and Autonomous Radio-Map Generation</h2>
      <p>Wi-Fi fingerprinting provides an indoor absolute reference, but scalable deployment requires moving beyond manual radio-map surveys. This area studies how ordinary mobile sessions, multisensor logs, RSS observations, and reliability checks can support autonomous map generation, map updating, and long-term maintenance.</p>
    </div>
    <div class="ra46-area-grid">
      <figure><img src="assets/home/research-area2-v40/multisensor-session-log-stream.webp" alt="Mobile crowdsensing session logs for Wi-Fi fingerprinting and autonomous radio-map generation" loading="lazy" decoding="async"></figure>
      <div class="ra46-card"><h3>Key problems</h3><ul><li>Irregular mobile measurements from natural user movement.</li><li>RSS instability across devices, time, human blockage, and access-point changes.</li><li>Alignment of Wi-Fi scans, IMU, magnetometer, barometer, GNSS, and app events.</li><li>Reliability-governed map updating to avoid writing noisy fingerprints into the map.</li></ul></div>
    </div>
    <div class="ra46-papers"><h3>Linked publications</h3><ul>
      <li><a href="publications/reliability-governed-3d-radio-mapping-lifecycle-review.html">Reliability-Governed Scaling of Mobile Crowdsensing-Based 3D Radio Mapping for Ubiquitous Indoor Positioning</a> <span>2026</span></li>
      <li><a href="publications/towards-ubiquitous-ips-crowdsourced-data-accumulation.html">Towards Ubiquitous IPS: Leveraging Crowdsourced Data Accumulation Over Time to Alleviate Reliance on External Sources in Initial Fingerprinting Map Generation</a> <span>2024</span></li>
      <li><a href="publications/leveraging-human-mobility-pervasive-smartphone-crowdsourcing.html">Leveraging Human Mobility and Pervasive Smartphone Measurements-Based Crowdsourcing for Developing Self-Deployable and Ubiquitous Indoor Positioning Systems</a> <span>2023</span></li>
      <li><a href="publications/everywhere-framework-ubiquitous-indoor-localization.html">Everywhere: A Framework for Ubiquitous Indoor Localization</a> <span>2022</span></li>
      <li><a href="publications/modular-prompting-ai-guided-user-engagement-crowd-powered-ips.html">A Modular Prompting Framework for AI-Guided Unobtrusive User Engagement in Crowd-Powered Indoor Positioning</a> <span>2025</span></li>
    </ul></div>
  </section>

  <section class="ra46-area" id="area-seamless">
    <div class="ra46-area-head">
      <p class="ra46-eyebrow">Research Area 3</p>
      <h2>Seamless Indoor–Outdoor Positioning and Multi-Source Fusion</h2>
      <p>Positioning should remain continuous as users move through streets, entrances, semi-open spaces, corridors, elevators, lobbies, and rooms. This area connects GNSS, PDR, Wi-Fi, BLE, barometer, map constraints, and indoor–outdoor awareness so that the trajectory does not break when sensing conditions change.</p>
    </div>
    <div class="ra46-area-grid">
      <figure><img src="assets/home/research-area3-v41/seamless-indoor-outdoor-transition.webp" alt="Seamless outdoor transition and indoor positioning with multi-source fusion" loading="lazy" decoding="async"></figure>
      <div class="ra46-card"><h3>Key problems</h3><ul><li>GNSS degradation near buildings before the user enters indoor space.</li><li>Mixed signal conditions in entrances, canopies, lobbies, and transition zones.</li><li>Source-reliability switching when GNSS, Wi-Fi, BLE, IMU, barometer, and maps vary over time.</li><li>Joint handling of position estimation, floor movement, and transition awareness.</li></ul></div>
    </div>
    <div class="ra46-papers"><h3>Linked publications</h3><ul>
      <li><a href="publications/suns-seamless-ubiquitous-navigation-indoor-outdoor-awareness.html">SUNS: Seamless Ubiquitous Navigation System Based on GNSS, Wi-Fi, and MEMS Sensors</a> <span>2022</span></li>
      <li><a href="publications/gnss-positioning-aided-with-pdr-in-urban-areas.html">GNSS Positioning Aided with Pedestrian Dead Reckoning in Urban Areas</a> <span>2026</span></li>
      <li><a href="publications/tightly-coupled-bluetooth-enhanced-gnss-pdr-urban.html">Tightly Coupled Bluetooth Enhanced GNSS/PDR System for Pedestrian Navigation in Dense Urban Environments</a> <span>2024</span></li>
      <li><a href="publications/ac-hmm-azimuth-constrained-map-matching-urban-canyons.html">AC-HMM: Azimuth-Constrained Hidden Markov Model-Based Map Matching for Robust Pedestrian Positioning in Urban Canyons</a> <span>2026</span></li>
    </ul></div>
  </section>

  <section class="ra46-area" id="area-3d">
    <div class="ra46-area-head">
      <p class="ra46-eyebrow">Research Area 4</p>
      <h2>3D Radio-Map Generation from Mobile Crowdsensing</h2>
      <p>Multi-floor indoor positioning requires more than a two-dimensional coordinate. This area studies 3D radio-map generation from mobile crowdsensing, including floor-local skeleton construction, building-level assembly, global refinement, vertical positioning, floor recognition, and multi-level indoor spatial context.</p>
    </div>
    <div class="ra46-area-grid">
      <figure><img src="assets/home/research-area4-v42/skeleton-assembly-refinement.webp" alt="3D radio-map generation from floor-local skeleton assembly and global refinement" loading="lazy" decoding="async"></figure>
      <div class="ra46-card"><h3>Key problems</h3><ul><li>Reconstruction of floor-local traces from noisy mobile sessions.</li><li>Vertical interpretation from barometer trends, stairs, elevators, ramps, and topology.</li><li>Signal leakage across floors in atriums, stairwells, open shafts, and dense AP deployments.</li><li>Building-level assembly and global refinement that preserve physical floor connectivity.</li></ul></div>
    </div>
    <div class="ra46-papers"><h3>Linked publications</h3><ul>
      <li><a href="publications/reliability-governed-3d-radio-mapping-lifecycle-review.html">Reliability-Governed Scaling of Mobile Crowdsensing-Based 3D Radio Mapping for Ubiquitous Indoor Positioning</a> <span>2026</span></li>
      <li><a href="publications/towards-ubiquitous-ips-crowdsourced-data-accumulation.html">Towards Ubiquitous IPS: Leveraging Crowdsourced Data Accumulation Over Time to Alleviate Reliance on External Sources in Initial Fingerprinting Map Generation</a> <span>2024</span></li>
      <li><a href="publications/leveraging-human-mobility-pervasive-smartphone-crowdsourcing.html">Leveraging Human Mobility and Pervasive Smartphone Measurements-Based Crowdsourcing for Developing Self-Deployable and Ubiquitous Indoor Positioning Systems</a> <span>2023</span></li>
      <li><a href="publications/phd-thesis-indoor-localization-multi-sensor-crowdsourcing-collaboration.html">Indoor Localization Based on Multi-Sensor Fusion, Crowdsourcing, and Multi-User Collaboration</a> <span>PhD thesis</span></li>
    </ul></div>
  </section>

  <section class="ra46-supporting" aria-label="Supporting themes">
    <div class="ra46-area-head">
      <p class="ra46-eyebrow">Supporting directions</p>
      <h2>Related themes connected to the four-area map</h2>
      <p>Some publications extend the positioning pipeline toward cooperative localization, construction safety, BIM-based risk mapping, AI-guided engagement, and deployment-ready services. These directions remain connected to the four-area structure but serve specific application or system-design needs.</p>
    </div>
    <div class="ra46-support-grid">
      <a href="publications/power-of-many-multi-user-collaborative-indoor-localization.html"><strong>Cooperative positioning</strong><span>Multi-user collaboration for improving standalone user-based indoor localization.</span></a>
      <a href="publications/uncertainty-aware-risk-mapping-passive-wifi-bim-construction.html"><strong>Deployment and spatial safety</strong><span>Passive Wi-Fi localization, BIM, uncertainty-aware risk mapping, and construction safety.</span></a>
      <a href="publications/towards-scalable-ips-user-centric-crowd-powered-framework.html"><strong>User-friendly crowd-powered IPS</strong><span>User intervention, participation, privacy, security, device burden, and deployment readiness.</span></a>
      <a href="citation-resources.html"><strong>Citation resources</strong><span>BibTeX, publication metadata, DOI links, AI-search prompts, and paper-use guidance.</span></a>
    </div>
  </section>
</main>
""" + footer + r"""
<script src="assets/js/site.js"></script>
</body>
</html>
"""

PAGE.write_text("<!doctype html>\n<html lang=\"en\">\n" + head + "\n" + body, encoding="utf-8")

css = re.sub(r"/\* === Research areas page v46 START === \*/.*?/\* === Research areas page v46 END === \*/", "", css, flags=re.S)
css_block = r"""
/* === Research areas page v46 START === */
.research-areas-v46{width:min(1180px,calc(100% - 56px));margin:0 auto 48px}
.ra46-hero{margin:36px 0 22px;padding:32px;border-radius:32px;background:radial-gradient(circle at 80% 12%,rgba(79,196,211,.16),transparent 35%),linear-gradient(180deg,rgba(255,255,255,.98),rgba(246,251,255,.98));border:1px solid rgba(130,165,194,.25);box-shadow:0 22px 50px rgba(20,45,74,.08)}
.ra46-eyebrow{margin:0 0 .55rem;color:#0b6380;text-transform:uppercase;letter-spacing:.12em;font-size:.75rem;font-weight:800}
.ra46-hero h1{margin:0 0 .85rem;color:#073d63;font-size:clamp(2rem,4vw,3.6rem);line-height:1.02;letter-spacing:-.055em}
.ra46-lead{max-width:950px;margin:0;color:#405b71;font-size:1.04rem;line-height:1.68}
.ra46-quicklinks{display:flex;flex-wrap:wrap;gap:.6rem;margin-top:1.3rem}
.ra46-quicklinks a{display:inline-flex;padding:.62rem .85rem;border-radius:999px;background:rgba(83,197,213,.10);border:1px solid rgba(79,159,187,.24);color:#084f72;font-weight:700;text-decoration:none;font-size:.85rem}
.ra46-flow{display:grid;grid-template-columns:repeat(4,1fr);gap:14px;margin:0 0 24px}
.ra46-flow article{padding:17px;border-radius:22px;background:linear-gradient(180deg,rgba(255,255,255,.96),rgba(248,252,255,.98));border:1px solid rgba(127,160,186,.20)}
.ra46-flow span{display:inline-flex;margin-bottom:.55rem;width:34px;height:34px;align-items:center;justify-content:center;border-radius:50%;color:#084f72;background:rgba(83,197,213,.13);font-weight:800;font-size:.78rem}
.ra46-flow strong{display:block;color:#073d63;margin-bottom:.35rem}
.ra46-flow p{margin:0;color:#5e7286;line-height:1.5;font-size:.88rem}
.ra46-area,.ra46-supporting{margin:24px 0;padding:22px;border-radius:30px;background:linear-gradient(180deg,rgba(255,255,255,.98),rgba(248,252,255,.98));border:1px solid rgba(130,165,194,.23);box-shadow:0 16px 38px rgba(20,45,74,.065)}
.ra46-area-head h2{margin:0 0 .65rem;color:#073d63;font-size:clamp(1.45rem,2.5vw,2.2rem);line-height:1.1;letter-spacing:-.04em}
.ra46-area-head p:not(.ra46-eyebrow){margin:0;max-width:980px;color:#405b71;font-size:.98rem;line-height:1.65}
.ra46-area-grid{display:grid;grid-template-columns:minmax(420px,1.05fr) minmax(0,.95fr);gap:18px;align-items:stretch;margin-top:18px}
.ra46-area-grid figure{margin:0;border-radius:24px;overflow:hidden;background:#fff;border:1px solid rgba(126,159,186,.22);box-shadow:0 14px 30px rgba(19,45,74,.075)}
.ra46-area-grid img{display:block;width:100%;height:100%;object-fit:cover}
.ra46-card{padding:17px;border-radius:22px;background:linear-gradient(180deg,rgba(245,242,255,.92),rgba(251,249,255,.98));border:1px solid rgba(148,132,200,.18)}
.ra46-card h3,.ra46-papers h3{margin:0 0 .6rem;color:#0b5074;font-size:.98rem}
.ra46-card ul,.ra46-papers ul{margin:0;padding-left:1.08rem}
.ra46-card li{margin:0 0 .52rem;color:#405b71;line-height:1.48;font-size:.91rem}
.ra46-papers{margin-top:18px;padding:16px 17px;border-radius:22px;background:linear-gradient(180deg,rgba(239,247,251,.96),rgba(249,252,255,.98));border:1px solid rgba(79,159,187,.17)}
.ra46-papers ul{columns:2;column-gap:2.2rem}
.ra46-papers li{break-inside:avoid;margin:0 0 .45rem;color:#607488;line-height:1.42;font-size:.86rem}
.ra46-papers a{color:#035083;text-decoration:none}
.ra46-papers a:hover{text-decoration:underline}
.ra46-papers span{color:#7f90a2}
.ra46-support-grid{display:grid;grid-template-columns:repeat(4,1fr);gap:14px;margin-top:18px}
.ra46-support-grid a{padding:16px;border-radius:20px;text-decoration:none;background:linear-gradient(180deg,rgba(255,255,255,.90),rgba(247,250,253,.96));border:1px solid rgba(127,160,186,.18)}
.ra46-support-grid strong{display:block;color:#073d63;margin-bottom:.35rem}
.ra46-support-grid span{display:block;color:#607488;font-size:.86rem;line-height:1.45}
@media(max-width:980px){.research-areas-v46{width:min(100%,calc(100% - 22px))}.ra46-flow,.ra46-support-grid{grid-template-columns:1fr 1fr}.ra46-area-grid{grid-template-columns:1fr}.ra46-papers ul{columns:1}}
@media(max-width:640px){.research-areas-v46{width:min(100%,calc(100% - 18px))}.ra46-hero,.ra46-area,.ra46-supporting{padding:17px;border-radius:24px}.ra46-flow,.ra46-support-grid{grid-template-columns:1fr}}
/* === Research areas page v46 END === */
"""
CSS.write_text(css.rstrip() + "\n\n" + css_block.strip() + "\n", encoding="utf-8")

if LLMS.exists():
    llms = LLMS.read_text(encoding="utf-8", errors="ignore")
    marker = "## Research areas on the homepage"
    add = """\n## Research-area landing page\n\n- Research Areas landing page: https://ahmedmansoour.github.io/indoor-positioning-hub/research-themes.html\n- Purpose: a dedicated machine-readable and reader-facing map that aligns the research-themes page with the homepage areas: inertial positioning, Wi-Fi fingerprinting and radio-map scaling, seamless indoor-outdoor fusion, and 3D radio-map generation from mobile crowdsensing.\n"""
    if "## Research-area landing page" not in llms:
        if marker in llms:
            llms = llms.replace(marker, add + "\n" + marker)
        else:
            llms = llms.rstrip() + "\n" + add + "\n"
        LLMS.write_text(llms, encoding="utf-8")

print("Done: upgraded research-themes.html into a Research Areas landing page aligned with homepage Areas 1-4.")
