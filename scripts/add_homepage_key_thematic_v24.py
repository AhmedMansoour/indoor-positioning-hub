from pathlib import Path
import re
import html

ROOT = Path('.')
INDEX = ROOT / 'index.html'
THEMES = ROOT / 'research-themes.html'
CSS = ROOT / 'assets' / 'css' / 'style.css'

if not INDEX.exists():
    raise SystemExit('index.html not found. Run this script from the repository root.')
if not THEMES.exists():
    raise SystemExit('research-themes.html not found. Run this script from the repository root.')
if not CSS.exists():
    raise SystemExit('assets/css/style.css not found. Run this script from the repository root.')

index_html = INDEX.read_text(encoding='utf-8', errors='ignore')
theme_html = THEMES.read_text(encoding='utf-8', errors='ignore')

# Remove any previous v24 block, so the script is safe to rerun.
index_html = re.sub(
    r'\n\s*<!-- === Homepage key thematic extension v24 START === -->.*?<!-- === Homepage key thematic extension v24 END === -->\s*\n',
    '\n',
    index_html,
    flags=re.S,
)

# Helper to extract image path from research-themes.html using the image alt or nearby card title.
def find_src_by_alt_or_title(keys):
    for key in keys:
        # direct alt search
        pat = r'<img\b[^>]*src=["\']([^"\']+)["\'][^>]*alt=["\'][^"\']*' + re.escape(key) + r'[^"\']*["\'][^>]*>'
        m = re.search(pat, theme_html, flags=re.I | re.S)
        if m:
            return html.unescape(m.group(1))
        # reverse order inside img
        pat = r'<img\b[^>]*alt=["\'][^"\']*' + re.escape(key) + r'[^"\']*["\'][^>]*src=["\']([^"\']+)["\'][^>]*>'
        m = re.search(pat, theme_html, flags=re.I | re.S)
        if m:
            return html.unescape(m.group(1))
        # title-near-card search
        card_pat = r'(<article\b[^>]*>.*?' + re.escape(key) + r'.*?</article>)'
        m = re.search(card_pat, theme_html, flags=re.I | re.S)
        if m:
            img = re.search(r'<img\b[^>]*src=["\']([^"\']+)["\']', m.group(1), flags=re.I | re.S)
            if img:
                return html.unescape(img.group(1))
    return None

# Fallback: collect any available visual atlas images in order.
all_imgs = re.findall(r'<img\b[^>]*src=["\']([^"\']+)["\'][^>]*alt=["\']([^"\']+)["\']', theme_html, flags=re.I | re.S)

def fallback_src(pos=0):
    if all_imgs:
        return html.unescape(all_imgs[min(pos, len(all_imgs)-1)][0])
    return 'assets/home/indoor-positioning-layered-building-alt.webp'

# Publication links already existing in the repository.
P = 'publications/'
papers = {
    'everywhere': (P + 'everywhere-framework-ubiquitous-indoor-localization.html', 'Everywhere: A Framework for Ubiquitous Indoor Localization', '2022'),
    'suns': (P + 'suns-seamless-ubiquitous-navigation-indoor-outdoor-awareness.html', 'SUNS: Seamless Ubiquitous Navigation System Based on GNSS, Wi-Fi, and MEMS Sensors', '2022'),
    'scalable': (P + 'towards-scalable-ips-user-centric-crowd-powered-framework.html', 'Towards Scalable IPS: User-Centric Challenges, Methods, and Recommendations for User-Friendly Crowd-Powered Schemes', '2026'),
    'modular': (P + 'modular-prompting-ai-guided-user-engagement-crowd-powered-ips.html', 'A Modular Prompting Framework for AI-Guided Unobtrusive User Engagement in Crowd-Powered Indoor Positioning with Semantic Knowledge Graphs and GPT-4-Based LLMs', '2025'),
    'radio_review': (P + 'reliability-governed-3d-radio-mapping-lifecycle-review.html', 'Reliability-Governed Scaling of Mobile Crowdsensing-Based 3D Radio Mapping for Ubiquitous Indoor Positioning', '2026'),
    'ubiquitous': (P + 'towards-ubiquitous-ips-crowdsourced-data-accumulation.html', 'Towards Ubiquitous IPS: Leveraging Crowdsourced Data Accumulation Over Time to Alleviate Reliance on External Sources in Initial Fingerprinting Map Generation', '2024'),
    'hybrid_pdr': (P + 'hybrid-neural-network-pdr-multi-layer-heading-correction.html', 'Hybrid Neural Network-Based PDR with Multi-Layer Heading Correction Across Smartphone Carrying Modes', '2026'),
    'heading_sr': (P + 'enhancing-real-time-heading-estimation-deep-learning-smartphone-sensors.html', 'Enhancing Real-Time Heading Estimation for Pedestrian Navigation Using Deep Learning and Smartphone Sensors', '2025'),
    'drift_tim': (P + 'drift-resistant-heading-estimation-wifi-magnetic-stability.html', 'Drift-Resistant Heading Estimation for Smartphone-Based Indoor Positioning via Adaptive Calibration Using Wi-Fi Fingerprinting and Magnetic Stability', '2026'),
    'drift_proc': (P + 'drift-control-pdr-long-period-navigation-smartphone-poses.html', 'Drift Control of Pedestrian Dead Reckoning for Long-Period Navigation Under Multiple Smartphone Poses', '2021'),
    'gnss_pdr': (P + 'gnss-positioning-aided-with-pdr-in-urban-areas.html', 'GNSS Positioning Aided with Pedestrian Dead Reckoning in Urban Areas', '2026'),
    'ble_gnss': (P + 'tightly-coupled-bluetooth-enhanced-gnss-pdr-urban.html', 'Tightly Coupled Bluetooth Enhanced GNSS/PDR System for Pedestrian Navigation in Dense Urban Environments', '2024'),
    'ac_hmm': (P + 'ac-hmm-azimuth-constrained-map-matching-urban-canyons.html', 'AC-HMM: Azimuth-Constrained Hidden Markov Model-Based Map Matching for Robust Pedestrian Positioning in Urban Canyons', '2026'),
    'mobility': (P + 'leveraging-human-mobility-pervasive-smartphone-crowdsourcing.html', 'Leveraging Human Mobility for Pervasive Smartphone Crowdsourcing in Indoor Positioning', '2023'),
    'many': (P + 'power-of-many-multi-user-collaborative-indoor-localization.html', 'The Power of Many: Multi-User Collaborative Indoor Localization', '2023'),
}

cards = [
    {
        'title': 'Context descriptor c(t)',
        'keys': ['Context descriptor', 'c(t)'],
        'desc': 'Motion state, carrying mode, turns, stops, vertical transitions, indoor-outdoor gates, and data-quality events are organized as a context layer for adaptive indoor positioning.',
        'links': ['modular', 'suns', 'everywhere'],
    },
    {
        'title': 'Phone pose and trajectory behavior',
        'keys': ['Phone pose', 'trajectory behavior'],
        'desc': 'The same pedestrian route can generate different trajectories when the phone is handheld, swinging, in pocket, used for calling, or mixed across modes.',
        'links': ['hybrid_pdr', 'heading_sr', 'drift_tim', 'drift_proc'],
    },
    {
        'title': 'Reliability-governed radio-map write-back',
        'keys': ['Reliability-governed', 'radio-map write-back'],
        'desc': 'Candidate fingerprints should pass spatial, feature, denoising, confidence, and structural checks before being used to update a radio map.',
        'links': ['radio_review', 'ubiquitous'],
    },
    {
        'title': 'Crowd-powered IPS deployment realities',
        'keys': ['Crowd-powered IPS deployment realities', 'deployment realities'],
        'desc': 'Scalable IPS must handle battery limits, privacy permissions, missing scans, carrying-mode changes, cross-building differences, and real user behavior.',
        'links': ['scalable', 'modular', 'radio_review'],
    },
    {
        'title': 'Multisensor session log stream',
        'keys': ['Multisensor session log stream', 'session log'],
        'desc': 'A mobile session y(t) can aggregate Wi-Fi, IMU, barometer, magnetometer, GNSS, and app events into a time-ordered spatial sensing stream.',
        'links': ['suns', 'gnss_pdr', 'ble_gnss', 'ac_hmm'],
    },
    {
        'title': '3D indoor positioning and multi-floor detection',
        'keys': ['Skeleton, assembly, and refinement', 'Skeleton'],
        'desc': 'Floor-local route skeletons, vertical transitions, gate constraints, and access-point anchors support 3D indoor positioning, building-level assembly, and multi-floor detection.',
        'links': ['ubiquitous', 'mobility', 'many', 'radio_review'],
    },
    {
        'title': 'Principles for scaling IPS',
        'keys': ['Principles for scaling IPS', 'scaling IPS'],
        'desc': 'The long-term goal is a generic, self-healing, user-centered IPS that learns from ordinary user data while reducing skilled survey effort and device-specific calibration.',
        'links': ['scalable', 'everywhere', 'radio_review'],
    },
]


def link_list(keys):
    out = ['<ul class="home-key-paper-list">']
    for k in keys:
        href, title, year = papers[k]
        out.append(f'  <li><a href="{href}">{html.escape(title)}</a> <span>({year})</span></li>')
    out.append('</ul>')
    return '\n'.join(out)

card_html = []
for i, c in enumerate(cards):
    src = find_src_by_alt_or_title(c['keys']) or fallback_src(i)
    card_html.append(f'''
      <article class="home-key-card">
        <img src="{src}" alt="{html.escape(c['title'])}" loading="lazy" decoding="async">
        <div class="home-key-card-body">
          <h3>{html.escape(c['title'])}</h3>
          <p>{html.escape(c['desc'])}</p>
          {link_list(c['links'])}
        </div>
      </article>''')

section = f'''
<!-- === Homepage key thematic extension v24 START === -->
<section class="home-key-thematic-extension" id="key-thematic-map">
  <div class="home-section-heading">
    <p class="eyebrow">Extended thematic map</p>
    <h2>Key thematic pathways across the hub</h2>
    <p>These visual pathways connect the main research themes to specific papers. The list is intentionally compact so readers can move quickly from a concept to the relevant publication.</p>
  </div>
  <div class="home-key-grid">
{''.join(card_html)}
  </div>
</section>
<!-- === Homepage key thematic extension v24 END === -->
'''

# Insert before Publication access when possible, otherwise before footer.
inserted = False
for marker in ['<p class="eyebrow">Publication access</p>', '<h2>Find papers, PDFs, citation records, and visual explanations</h2>', '<footer']:
    pos = index_html.find(marker)
    if pos != -1:
        index_html = index_html[:pos] + section + '\n' + index_html[pos:]
        inserted = True
        break

if not inserted:
    index_html = index_html.rstrip() + '\n' + section + '\n'

INDEX.write_text(index_html, encoding='utf-8')

css = CSS.read_text(encoding='utf-8', errors='ignore')
css = re.sub(
    r'/\* === Homepage key thematic extension v24 START === \*/.*?/\* === Homepage key thematic extension v24 END === \*/',
    '',
    css,
    flags=re.S,
)

css_block = r'''
/* === Homepage key thematic extension v24 START === */
.home-key-thematic-extension {
  width: min(1180px, calc(100% - 32px));
  margin: 48px auto 34px;
}

.home-key-thematic-extension .home-section-heading {
  max-width: 880px;
  margin: 0 auto 22px;
  text-align: center;
}

.home-key-thematic-extension .home-section-heading h2 {
  margin: 0.15rem 0 0.55rem;
  font-size: clamp(1.65rem, 2.4vw, 2.45rem);
  letter-spacing: -0.035em;
}

.home-key-thematic-extension .home-section-heading p:not(.eyebrow) {
  color: #607084;
  font-size: 0.98rem;
  line-height: 1.65;
}

.home-key-grid {
  display: grid;
  grid-template-columns: repeat(2, minmax(0, 1fr));
  gap: 18px;
}

.home-key-card {
  overflow: hidden;
  border-radius: 22px;
  background: rgba(255, 255, 255, 0.86);
  border: 1px solid rgba(142, 171, 198, 0.28);
  box-shadow: 0 16px 42px rgba(21, 55, 90, 0.08);
}

.home-key-card img {
  display: block;
  width: 100%;
  height: 215px;
  object-fit: cover;
  object-position: center;
  background: #eef5f8;
  border-bottom: 1px solid rgba(142, 171, 198, 0.22);
}

.home-key-card-body {
  padding: 16px 20px 18px;
}

.home-key-card-body h3 {
  margin: 0 0 8px;
  color: #083e63;
  font-size: 1.04rem;
  line-height: 1.28;
  letter-spacing: -0.012em;
}

.home-key-card-body p {
  margin: 0 0 12px;
  color: #5d6f83;
  font-size: 0.9rem;
  line-height: 1.55;
}

.home-key-paper-list {
  margin: 0;
  padding-left: 1.05rem;
  display: grid;
  gap: 0.28rem;
}

.home-key-paper-list li {
  margin: 0;
  color: #1d3851;
  font-size: 0.86rem;
  line-height: 1.45;
}

.home-key-paper-list a,
.home-key-paper-list a:visited {
  color: #035083;
  font-weight: 400 !important;
  text-decoration: none;
}

.home-key-paper-list a:hover {
  color: #00739f;
  text-decoration: underline;
}

.home-key-paper-list span {
  color: #718196;
  font-weight: 400;
}

@media (max-width: 900px) {
  .home-key-grid {
    grid-template-columns: 1fr;
  }

  .home-key-card img {
    height: auto;
    max-height: 260px;
  }
}
/* === Homepage key thematic extension v24 END === */
'''

css = css.rstrip() + '\n\n' + css_block.strip() + '\n'
CSS.write_text(css, encoding='utf-8')

print('Done: added compact key thematic pathways to the homepage under the existing thematic section.')
