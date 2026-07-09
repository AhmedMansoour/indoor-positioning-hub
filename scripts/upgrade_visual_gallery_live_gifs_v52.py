from pathlib import Path
import shutil
import re

ROOT = Path('.')
SRC = Path(__file__).resolve().parent.parent / 'bundle_visuals_v52'
VIS_DIR = ROOT / 'assets' / 'visual-gallery-v52'
INDEX = ROOT / 'index.html'
RESOURCES = ROOT / 'resources.html'
CSS = ROOT / 'assets' / 'css' / 'style.css'
LLMS = ROOT / 'llms.txt'

PUB_PAGES = {
    'everywhere-framework-ubiquitous-indoor-localization.html': {
        'heading': 'Visual workflow: autonomous radio-map generation',
        'image': 'autonomous-map-generation-live.gif',
        'alt': 'Animated workflow for autonomous radio-map generation from crowdsourced mobile data',
        'text': 'This live GIF preserves the original workflow animation: ordinary users contribute pervasive signatures, the system generates radio and magnetic maps, and online positioning queries the learned reference.',
        'anchor': 'area-radio-map',
        'media_class': 'paper-visual-panorama-v52',
        'section_id': 'autonomous-map-generation-visual'
    },
    'suns-seamless-ubiquitous-navigation-indoor-outdoor-awareness.html': {
        'heading': 'Visual context: indoor-outdoor awareness and 3D positioning',
        'image': 'iod-seamless-live.gif',
        'alt': 'Animated indoor-outdoor detection and 3D positioning with floor detection',
        'text': 'This live GIF shows the transition-aware positioning problem directly: indoor-outdoor state recognition, floor-level positioning, and seamless trajectory continuity across environmental boundaries.',
        'anchor': 'area-seamless',
        'media_class': 'paper-visual-panorama-v52',
        'section_id': 'iod-3d-positioning-visual'
    },
    'reliability-governed-3d-radio-mapping-lifecycle-review.html': {
        'heading': 'Visual context: multi-floor indoor spatial structure',
        'image': 'indoor-navigation-3d-multilevel.webp',
        'alt': 'Multi-floor indoor navigation scene with vertical movement and indoor positioning cues',
        'text': 'This figure emphasizes the multi-level building context behind 3D radio-map generation, floor recognition, and vertical positioning.',
        'anchor': 'area-3d',
        'media_class': 'paper-visual-scene-v52',
        'section_id': 'multilevel-indoor-context-visual'
    }
}

REQ = [
    'future-spatial-intelligence.webp',
    'indoor-navigation-3d-multilevel.webp',
    'autonomous-map-generation-live.gif',
    'iod-seamless-live.gif',
]

for name in REQ:
    if not (SRC / name).exists():
        raise SystemExit(f'Missing bundled visual asset: {name}')

VIS_DIR.mkdir(parents=True, exist_ok=True)
for name in REQ:
    shutil.copy2(SRC / name, VIS_DIR / name)

def read(path):
    return path.read_text(encoding='utf-8', errors='ignore')

def write(path, text):
    path.write_text(text, encoding='utf-8')

def remove_between(text, start, end):
    return re.sub(rf'\n?\s*{re.escape(start)}.*?{re.escape(end)}\s*\n?', '\n', text, flags=re.S)

def insert_before(text, marker, block):
    idx = text.find(marker)
    return text[:idx] + block + '\n' + text[idx:] if idx != -1 else text + '\n' + block

def insert_after(text, marker, block):
    idx = text.find(marker)
    if idx == -1:
        return text + '\n' + block
    end = idx + len(marker)
    return text[:end] + '\n' + block + text[end:]

home_markers = [
    ('<!-- === Visual research gallery v50 START === -->', '<!-- === Visual research gallery v50 END === -->'),
    ('<!-- === Visual research gallery v51 START === -->', '<!-- === Visual research gallery v51 END === -->'),
    ('<!-- === Visual research gallery v52 START === -->', '<!-- === Visual research gallery v52 END === -->'),
]

home_block = '''
<!-- === Visual research gallery v52 START === -->
<section class="visual-gallery-v52" id="visual-research-gallery" aria-label="Visual research gallery">
  <div class="vg52-head">
    <p class="vg52-eyebrow">Visual research gallery</p>
    <h2>From signals and motion to indoor spatial intelligence</h2>
    <p>This visual index keeps the gallery concise: the 2D navigation illustration is removed, the 3D indoor figure is enlarged, and the autonomous radio-map and indoor-outdoor demonstrations are shown as live GIFs.</p>
  </div>
  <div class="vg52-grid">
    <article class="vg52-card vg52-scene vg52-wide">
      <figure><img src="assets/visual-gallery-v52/future-spatial-intelligence.webp" alt="Future city-scale positioning and spatial intelligence vision with navigation overlays" loading="lazy" decoding="async"></figure>
      <div>
        <span>Vision layer</span>
        <h3>Future spatial intelligence</h3>
        <p>A high-level view of positioning as part of connected urban, indoor, and multi-level navigation services.</p>
      </div>
    </article>
    <article class="vg52-card vg52-scene vg52-wide vg52-emphasis">
      <figure><img src="assets/visual-gallery-v52/indoor-navigation-3d-multilevel.webp" alt="Three-dimensional multi-floor indoor positioning with escalators and vertical context" loading="lazy" decoding="async"></figure>
      <div>
        <span>3D spatial context</span>
        <h3>Multi-floor positioning</h3>
        <p>An enlarged figure that highlights floor recognition, vertical movement, and multi-level indoor geometry.</p>
      </div>
    </article>
    <article class="vg52-card vg52-panorama">
      <figure><img src="assets/visual-gallery-v52/autonomous-map-generation-live.gif" alt="Animated workflow for autonomous radio-map generation from crowdsourced mobile data" loading="lazy"></figure>
      <div>
        <span>Radio-map scaling</span>
        <h3>Autonomous map generation</h3>
        <p>The original live GIF now runs directly on the site, preserving the workflow animation.</p>
      </div>
    </article>
    <article class="vg52-card vg52-panorama">
      <figure><img src="assets/visual-gallery-v52/iod-seamless-live.gif" alt="Animated indoor-outdoor detection and 3D positioning with floor detection" loading="lazy"></figure>
      <div>
        <span>Transition awareness</span>
        <h3>IOD and seamless positioning</h3>
        <p>The original live GIF shows indoor-outdoor awareness, floor detection, and transition-aware positioning.</p>
      </div>
    </article>
  </div>
</section>
<!-- === Visual research gallery v52 END === -->
'''

if INDEX.exists():
    html = read(INDEX)
    for s, e in home_markers:
        html = remove_between(html, s, e)
    marker = '<!-- === Homepage research area 4 3d radio map v42 END === -->'
    if marker in html:
        html = insert_after(html, marker, home_block)
    elif '<section class="v23-section v23-access"' in html:
        html = insert_before(html, '<section class="v23-section v23-access"', home_block)
    else:
        html += '\n' + home_block
    write(INDEX, html)

resource_markers = [
    ('<!-- === Resources visual materials v50 START === -->', '<!-- === Resources visual materials v50 END === -->'),
    ('<!-- === Resources visual materials v51 START === -->', '<!-- === Resources visual materials v51 END === -->'),
    ('<!-- === Resources visual materials v52 START === -->', '<!-- === Resources visual materials v52 END === -->'),
]

resources_block = '''
<!-- === Resources visual materials v52 START === -->
<section class="res47-section res52-visuals" id="visual-materials">
  <div class="res47-section-head">
    <p class="res47-eyebrow">Visual research materials</p>
    <h2>Figures and live GIFs used across the hub</h2>
    <p>The resources page now reflects the streamlined visual set: a future-facing scene, an enlarged 3D indoor scene, and two live GIF demonstrations for autonomous radio-map generation and indoor-outdoor seamless positioning.</p>
  </div>
  <div class="res52-visual-grid">
    <a class="res52-scene" href="index.html#visual-research-gallery"><img src="assets/visual-gallery-v52/future-spatial-intelligence.webp" alt="Future spatial intelligence visual"><strong>Future spatial intelligence</strong><span>Homepage vision for connected positioning services.</span></a>
    <a class="res52-scene res52-emphasis" href="research-themes.html#area-3d"><img src="assets/visual-gallery-v52/indoor-navigation-3d-multilevel.webp" alt="Three-dimensional indoor navigation visual"><strong>Multi-floor indoor positioning</strong><span>Area 4, 3D indoor spatial context and floor-aware positioning.</span></a>
    <a class="res52-panorama" href="research-themes.html#area-radio-map"><img src="assets/visual-gallery-v52/autonomous-map-generation-live.gif" alt="Autonomous radio-map generation live GIF"><strong>Autonomous map generation</strong><span>Area 2, mobile crowdsensing and Wi-Fi fingerprinting.</span></a>
    <a class="res52-panorama" href="research-themes.html#area-seamless"><img src="assets/visual-gallery-v52/iod-seamless-live.gif" alt="Indoor-outdoor positioning live GIF"><strong>IOD and seamless positioning</strong><span>Area 3, transition awareness and continuity.</span></a>
  </div>
</section>
<!-- === Resources visual materials v52 END === -->
'''

if RESOURCES.exists():
    html = read(RESOURCES)
    for s, e in resource_markers:
        html = remove_between(html, s, e)
    repro_marker = '<section class="res47-section">\n    <div class="res47-section-head"><p class="res47-eyebrow">Reproducibility by research area</p>'
    if repro_marker in html:
        html = insert_before(html, repro_marker, resources_block)
    elif '</main>' in html:
        html = insert_before(html, '</main>', resources_block)
    else:
        html += '\n' + resources_block
    write(RESOURCES, html)

old_markers = [
    ('<!-- === Publication visual context v50 START === -->', '<!-- === Publication visual context v50 END === -->'),
    ('<!-- === Publication visual context v51 START === -->', '<!-- === Publication visual context v51 END === -->'),
    ('<!-- === Publication visual context v52 START === -->', '<!-- === Publication visual context v52 END === -->'),
]

pub_template = '''
<!-- === Publication visual context v52 START === -->
<section class="paper-visual-context-v52" id="{section_id}">
  <h2>{heading}</h2>
  <div class="paper-visual-context-grid-v52 {media_class}">
    <figure>
      <img src="../assets/visual-gallery-v52/{image}" alt="{alt}" loading="lazy">
    </figure>
    <div>
      <p>{text}</p>
      <a href="../research-themes.html#{anchor}">Open the related research area</a>
    </div>
  </div>
</section>
<!-- === Publication visual context v52 END === -->
'''

for page_name, meta in PUB_PAGES.items():
    path = ROOT / 'publications' / page_name
    if not path.exists():
        continue
    html = read(path)
    for s, e in old_markers:
        html = remove_between(html, s, e)
    block = pub_template.format(**meta)
    marker = '<!-- === Publication research-area index v45 START === -->'
    if marker in html:
        html = insert_before(html, marker, block)
    elif '</main>' in html:
        html = insert_before(html, '</main>', block)
    else:
        html += '\n' + block
    write(path, html)

if CSS.exists():
    css = read(CSS)
    css = re.sub(r'/\* === Visual research gallery v50 START === \*/.*?/\* === Visual research gallery v50 END === \*/', '', css, flags=re.S)
    css = re.sub(r'/\* === Visual research gallery v51 START === \*/.*?/\* === Visual research gallery v51 END === \*/', '', css, flags=re.S)
    css = re.sub(r'/\* === Visual research gallery v52 START === \*/.*?/\* === Visual research gallery v52 END === \*/', '', css, flags=re.S)
    css_block = '''
/* === Visual research gallery v52 START === */
.visual-gallery-v52{width:min(1180px,calc(100% - 56px));margin:28px auto 44px;padding:24px;border-radius:30px;background:linear-gradient(180deg,rgba(255,255,255,.98),rgba(248,252,255,.98));border:1px solid rgba(130,165,194,.23);box-shadow:0 16px 38px rgba(20,45,74,.065)}
.vg52-head{max-width:980px;margin-bottom:18px}
.vg52-eyebrow{margin:0 0 .55rem;color:#0b6380;text-transform:uppercase;letter-spacing:.12em;font-size:.75rem;font-weight:800}
.vg52-head h2{margin:0 0 .65rem;color:#073d63;font-size:clamp(1.55rem,2.8vw,2.35rem);line-height:1.08;letter-spacing:-.045em}
.vg52-head p{margin:0;color:#405b71;font-size:.98rem;line-height:1.62}
.vg52-grid{display:grid;grid-template-columns:repeat(4,1fr);gap:14px}
.vg52-card{overflow:hidden;border-radius:22px;background:#fff;border:1px solid rgba(127,160,186,.20);box-shadow:0 10px 24px rgba(20,45,74,.055)}
.vg52-card.vg52-wide,.vg52-card.vg52-panorama{grid-column:span 2}
.vg52-card figure{margin:0;background:#eef6fb;overflow:hidden;display:flex;align-items:center;justify-content:center}
.vg52-scene figure{aspect-ratio:1024/559}
.vg52-panorama figure{aspect-ratio:1280/540}
.vg52-card img{width:100%;height:100%;display:block}
.vg52-scene img{object-fit:cover}
.vg52-panorama img{object-fit:contain;background:#fff}
.vg52-emphasis figure{background:linear-gradient(180deg,#f4f9fd,#eef6fb)}
.vg52-card div{padding:14px 15px}
.vg52-card span{display:inline-flex;margin-bottom:.38rem;padding:.28rem .52rem;border-radius:999px;background:rgba(83,197,213,.11);color:#0b6380;font-size:.72rem;font-weight:800}
.vg52-card h3{margin:0 0 .35rem;color:#073d63;font-size:1rem;line-height:1.2}
.vg52-card p{margin:0;color:#607488;font-size:.86rem;line-height:1.45}
.res52-visual-grid{display:grid;grid-template-columns:1fr 1fr;gap:14px;margin-top:18px;align-items:stretch}
.res52-visual-grid a{display:block;overflow:hidden;border-radius:22px;background:#fff;text-decoration:none;border:1px solid rgba(127,160,186,.20);box-shadow:0 10px 24px rgba(20,45,74,.045)}
.res52-visual-grid img{display:block;width:100%}
.res52-scene img{aspect-ratio:1024/559;object-fit:cover;background:#eef6fb}
.res52-panorama img{aspect-ratio:1280/540;object-fit:contain;background:#fff}
.res52-visual-grid strong{display:block;padding:13px 14px 4px;color:#073d63}
.res52-visual-grid span{display:block;padding:0 14px 14px;color:#607488;font-size:.85rem;line-height:1.42}
.paper-visual-context-v52{margin:1.4rem 0;padding:1rem;border-radius:22px;background:linear-gradient(180deg,rgba(255,255,255,.98),rgba(248,252,255,.98));border:1px solid rgba(130,165,194,.22);box-shadow:0 12px 28px rgba(20,45,74,.055)}
.paper-visual-context-v52 h2{margin:0 0 .8rem;color:#073d63;font-size:1.18rem;letter-spacing:-.02em}
.paper-visual-context-grid-v52{display:grid;grid-template-columns:minmax(300px,1.05fr) .95fr;gap:14px;align-items:center}
.paper-visual-panorama-v52{grid-template-columns:minmax(420px,1.25fr) .75fr}
.paper-visual-context-grid-v52 figure{margin:0;border-radius:18px;overflow:hidden;border:1px solid rgba(127,160,186,.18);background:#fff;display:flex;align-items:center;justify-content:center}
.paper-visual-context-grid-v52 img{display:block;width:100%;height:auto}
.paper-visual-panorama-v52 figure{aspect-ratio:1280/540}
.paper-visual-panorama-v52 img{height:100%;object-fit:contain}
.paper-visual-scene-v52 figure{aspect-ratio:1024/559}
.paper-visual-scene-v52 img{height:100%;object-fit:cover}
.paper-visual-context-grid-v52 p{margin:0 0 .75rem;color:#405b71;line-height:1.58}
.paper-visual-context-grid-v52 a{color:#084f72;font-weight:700;text-decoration:none}
.paper-visual-context-grid-v52 a:hover{text-decoration:underline}
@media(max-width:980px){.visual-gallery-v52{width:min(100%,calc(100% - 22px));padding:18px}.vg52-grid{grid-template-columns:1fr 1fr}.vg52-card.vg52-wide,.vg52-card.vg52-panorama{grid-column:span 2}.res52-visual-grid{grid-template-columns:1fr}.paper-visual-context-grid-v52,.paper-visual-panorama-v52{grid-template-columns:1fr}}
@media(max-width:640px){.visual-gallery-v52{width:min(100%,calc(100% - 18px));border-radius:24px;padding:16px}.vg52-grid{grid-template-columns:1fr}.vg52-card.vg52-wide,.vg52-card.vg52-panorama{grid-column:span 1}}
/* === Visual research gallery v52 END === */
'''
    write(CSS, css.rstrip() + '\n\n' + css_block.strip() + '\n')

if LLMS.exists():
    llms = read(LLMS)
    llms = re.sub(r'\n## Visual research gallery\n\n- Visual Research Gallery:.*?(?=\n## |\Z)', '\n', llms, flags=re.S)
    add = '''
## Visual research gallery

- Visual Research Gallery: https://ahmedmansoour.github.io/indoor-positioning-hub/index.html#visual-research-gallery
- Purpose: a compact visual index centered on future spatial intelligence, enlarged 3D indoor positioning, autonomous radio-map generation, and indoor-outdoor seamless positioning.
- Live GIF assets: assets/visual-gallery-v52/autonomous-map-generation-live.gif and assets/visual-gallery-v52/iod-seamless-live.gif
- Static scene assets: assets/visual-gallery-v52/future-spatial-intelligence.webp and assets/visual-gallery-v52/indoor-navigation-3d-multilevel.webp
'''
    marker = '## Resources and reproducibility page'
    if marker in llms:
        llms = llms.replace(marker, add + '\n' + marker)
    else:
        llms = llms.rstrip() + '\n' + add + '\n'
    write(LLMS, llms)

print('Applied v52 patch logic successfully.')
