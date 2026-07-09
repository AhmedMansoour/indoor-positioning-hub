from pathlib import Path
import shutil
import re

ROOT = Path(".")
SRC = Path(__file__).resolve().parent.parent / "bundle_visuals_v51"
VIS_DIR = ROOT / "assets" / "visual-gallery-v51"

INDEX = ROOT / "index.html"
RESOURCES = ROOT / "resources.html"
CSS = ROOT / "assets" / "css" / "style.css"
LLMS = ROOT / "llms.txt"

REQUIRED = [
    "future-spatial-intelligence.webp",
    "indoor-navigation-2d-mall.webp",
    "indoor-navigation-3d-multilevel.webp",
    "everywhere-autonomous-radio-map-animated.webp",
    "iod-3d-positioning-demo-animated.webp",
    "everywhere-autonomous-radio-map-static.webp",
    "iod-3d-positioning-demo-static.webp",
]

for name in REQUIRED:
    if not (SRC / name).exists():
        raise SystemExit(f"Missing bundled visual asset: {name}")

VIS_DIR.mkdir(parents=True, exist_ok=True)
for name in REQUIRED:
    shutil.copy2(SRC / name, VIS_DIR / name)

def read(path):
    return path.read_text(encoding="utf-8", errors="ignore")

def write(path, text):
    path.write_text(text, encoding="utf-8")

def remove_block(text, start, end):
    return re.sub(rf"\n?\s*{re.escape(start)}.*?{re.escape(end)}\s*\n?", "\n", text, flags=re.S)

def insert_before(text, marker, block):
    idx = text.find(marker)
    if idx != -1:
        return text[:idx] + block + "\n" + text[idx:]
    return text + "\n" + block

def insert_after(text, marker, block):
    idx = text.find(marker)
    if idx != -1:
        end = idx + len(marker)
        return text[:end] + "\n" + block + text[end:]
    return text + "\n" + block

home_start_v50 = "<!-- === Visual research gallery v50 START === -->"
home_end_v50 = "<!-- === Visual research gallery v50 END === -->"
home_start_v51 = "<!-- === Visual research gallery v51 START === -->"
home_end_v51 = "<!-- === Visual research gallery v51 END === -->"

home_block = '''
<!-- === Visual research gallery v51 START === -->
<section class="visual-gallery-v51" id="visual-research-gallery" aria-label="Visual research gallery">
  <div class="vg51-head">
    <p class="vg51-eyebrow">Visual research gallery</p>
    <h2>From signals and motion to indoor spatial intelligence</h2>
    <p>These visuals provide a fast reading path through the hub. The layout preserves the natural figure proportions: 1024 × 559 for the three scene figures, 1280 × 540 for the autonomous radio-map workflow, and 800 × 349 for the indoor-outdoor and 3D-positioning workflow.</p>
  </div>

  <div class="vg51-grid">
    <article class="vg51-card vg51-scene vg51-wide">
      <figure><img src="assets/visual-gallery-v51/future-spatial-intelligence.webp" alt="Future city-scale positioning and spatial intelligence vision with navigation overlays" loading="lazy" decoding="async"></figure>
      <div>
        <span>Vision layer</span>
        <h3>Future spatial intelligence</h3>
        <p>A high-level view of positioning as part of connected urban, indoor, and multi-level navigation services.</p>
      </div>
    </article>

    <article class="vg51-card vg51-scene">
      <figure><img src="assets/visual-gallery-v51/indoor-navigation-2d-mall.webp" alt="Two-dimensional indoor navigation and wayfinding in a shopping mall" loading="lazy" decoding="async"></figure>
      <div>
        <span>User-facing navigation</span>
        <h3>2D indoor navigation</h3>
        <p>Shows maps, routes, landmarks, shops, and wayfinding inside a building.</p>
      </div>
    </article>

    <article class="vg51-card vg51-scene">
      <figure><img src="assets/visual-gallery-v51/indoor-navigation-3d-multilevel.webp" alt="Three-dimensional multi-floor indoor positioning with escalators and vertical context" loading="lazy" decoding="async"></figure>
      <div>
        <span>3D spatial context</span>
        <h3>Multi-floor positioning</h3>
        <p>Connects floor recognition, vertical movement, escalators, stairs, and multi-level indoor geometry.</p>
      </div>
    </article>

    <article class="vg51-card vg51-panorama">
      <figure><img src="assets/visual-gallery-v51/everywhere-autonomous-radio-map-animated.webp" alt="Animated workflow for autonomous radio and magnetic map generation from crowdsourced data" loading="lazy" decoding="async"></figure>
      <div>
        <span>Radio-map scaling</span>
        <h3>Autonomous map generation</h3>
        <p>Links mobile crowdsensing, database generation, radio and magnetic maps, and online positioning.</p>
      </div>
    </article>

    <article class="vg51-card vg51-panorama">
      <figure><img src="assets/visual-gallery-v51/iod-3d-positioning-demo-animated.webp" alt="Animated indoor outdoor detection and 3D positioning with floor detection demonstration" loading="lazy" decoding="async"></figure>
      <div>
        <span>Transition awareness</span>
        <h3>IOD and 3D positioning</h3>
        <p>Shows indoor-outdoor detection, transition states, 3D trajectory estimation, and floor-level positioning.</p>
      </div>
    </article>
  </div>
</section>
<!-- === Visual research gallery v51 END === -->
'''

resources_start_v50 = "<!-- === Resources visual materials v50 START === -->"
resources_end_v50 = "<!-- === Resources visual materials v50 END === -->"
resources_start_v51 = "<!-- === Resources visual materials v51 START === -->"
resources_end_v51 = "<!-- === Resources visual materials v51 END === -->"

resources_block = '''
<!-- === Resources visual materials v51 START === -->
<section class="res47-section res51-visuals" id="visual-materials">
  <div class="res47-section-head">
    <p class="res47-eyebrow">Visual research materials</p>
    <h2>Figures and animations used across the hub</h2>
    <p>The scene figures are shown in their natural 1024 × 559 ratio, while the workflow animations use wide panels so their labels and diagrams remain readable without cropping.</p>
  </div>
  <div class="res51-visual-grid">
    <a class="res51-scene" href="index.html#visual-research-gallery"><img src="assets/visual-gallery-v51/future-spatial-intelligence.webp" alt="Future spatial intelligence visual"><strong>Future spatial intelligence</strong><span>Homepage vision and positioning services.</span></a>
    <a class="res51-panorama" href="research-themes.html#area-radio-map"><img src="assets/visual-gallery-v51/everywhere-autonomous-radio-map-animated.webp" alt="Autonomous radio-map generation workflow animation"><strong>Autonomous map generation</strong><span>Area 2, mobile crowdsensing and Wi-Fi fingerprinting.</span></a>
    <a class="res51-panorama" href="research-themes.html#area-seamless"><img src="assets/visual-gallery-v51/iod-3d-positioning-demo-animated.webp" alt="Indoor-outdoor detection and 3D positioning animation"><strong>IOD and 3D positioning</strong><span>Area 3 and Area 4, transition and floor awareness.</span></a>
  </div>
</section>
<!-- === Resources visual materials v51 END === -->
'''

pub_start_v50 = "<!-- === Publication visual context v50 START === -->"
pub_end_v50 = "<!-- === Publication visual context v50 END === -->"
pub_start_v51 = "<!-- === Publication visual context v51 START === -->"
pub_end_v51 = "<!-- === Publication visual context v51 END === -->"

pub_block_template = '''
<!-- === Publication visual context v51 START === -->
<section class="paper-visual-context-v51" id="{section_id}">
  <h2>{heading}</h2>
  <div class="paper-visual-context-grid-v51 {media_class}">
    <figure>
      <img src="../assets/visual-gallery-v51/{image}" alt="{alt}" loading="lazy" decoding="async">
    </figure>
    <div>
      <p>{text}</p>
      <a href="../research-themes.html#{area_anchor}">Open the related research area</a>
    </div>
  </div>
</section>
<!-- === Publication visual context v51 END === -->
'''

def add_pub_visual(page_name, section_id, heading, image, alt, text, area_anchor, media_class):
    path = ROOT / "publications" / page_name
    if not path.exists():
        print(f"Skipped missing publication page: {page_name}")
        return
    html = read(path)
    html = remove_block(html, pub_start_v50, pub_end_v50)
    html = remove_block(html, pub_start_v51, pub_end_v51)
    block = pub_block_template.format(section_id=section_id, heading=heading, image=image, alt=alt, text=text, area_anchor=area_anchor, media_class=media_class)
    marker = "<!-- === Publication research-area index v45 START === -->"
    if marker in html:
        html = insert_before(html, marker, block)
    elif "</main>" in html:
        html = insert_before(html, "</main>", block)
    else:
        html += "\n" + block
    write(path, html)
    print(f"Updated {page_name}")

if INDEX.exists():
    html = read(INDEX)
    html = remove_block(html, home_start_v50, home_end_v50)
    html = remove_block(html, home_start_v51, home_end_v51)
    marker = "<!-- === Homepage research area 4 3d radio map v42 END === -->"
    if marker in html:
        html = insert_after(html, marker, home_block)
    elif '<section class="v23-section v23-access"' in html:
        html = insert_before(html, '<section class="v23-section v23-access"', home_block)
    else:
        html += "\n" + home_block
    write(INDEX, html)
    print("Updated index.html with improved visual gallery.")

if RESOURCES.exists():
    html = read(RESOURCES)
    html = remove_block(html, resources_start_v50, resources_end_v50)
    html = remove_block(html, resources_start_v51, resources_end_v51)
    repro_marker = '<section class="res47-section">\n    <div class="res47-section-head"><p class="res47-eyebrow">Reproducibility by research area</p>'
    if repro_marker in html:
        html = insert_before(html, repro_marker, resources_block)
    elif "</main>" in html:
        html = insert_before(html, "</main>", resources_block)
    else:
        html += "\n" + resources_block
    write(RESOURCES, html)
    print("Updated resources.html with improved visual materials section.")

add_pub_visual(
    "everywhere-framework-ubiquitous-indoor-localization.html",
    "autonomous-map-generation-visual",
    "Visual workflow: autonomous radio-map generation",
    "everywhere-autonomous-radio-map-animated.webp",
    "Animated autonomous database generation workflow for self-deployable indoor positioning",
    "This animated workflow summarizes the paper's deployment logic: ordinary users contribute pervasive signatures, the system generates and stores radio or magnetic maps, and online users query the generated reference for positioning.",
    "area-radio-map",
    "paper-visual-panorama-v51",
)

add_pub_visual(
    "suns-seamless-ubiquitous-navigation-indoor-outdoor-awareness.html",
    "iod-3d-positioning-visual",
    "Visual context: indoor-outdoor awareness and 3D positioning",
    "iod-3d-positioning-demo-animated.webp",
    "Animated indoor-outdoor detection and 3D positioning with floor detection",
    "This animated visual illustrates the transition-aware positioning problem: the system must recognize indoor, outdoor, and semi-transition states while maintaining a usable position estimate across floors and spaces.",
    "area-seamless",
    "paper-visual-panorama-v51",
)

add_pub_visual(
    "reliability-governed-3d-radio-mapping-lifecycle-review.html",
    "multilevel-indoor-context-visual",
    "Visual context: multi-floor indoor spatial structure",
    "indoor-navigation-3d-multilevel.webp",
    "Multi-floor indoor navigation scene with vertical movement and indoor positioning cues",
    "This visual supports the review's 3D radio-map perspective by showing why floor recognition, vertical movement, and multi-level indoor spatial context are necessary for deployment-ready indoor positioning.",
    "area-3d",
    "paper-visual-scene-v51",
)

if CSS.exists():
    css = read(CSS)
    css = re.sub(r"/\* === Visual research gallery v50 START === \*/.*?/\* === Visual research gallery v50 END === \*/", "", css, flags=re.S)
    css = re.sub(r"/\* === Visual research gallery v51 START === \*/.*?/\* === Visual research gallery v51 END === \*/", "", css, flags=re.S)
    css_block = '''
/* === Visual research gallery v51 START === */
.visual-gallery-v51{width:min(1180px,calc(100% - 56px));margin:28px auto 44px;padding:24px;border-radius:30px;background:linear-gradient(180deg,rgba(255,255,255,.98),rgba(248,252,255,.98));border:1px solid rgba(130,165,194,.23);box-shadow:0 16px 38px rgba(20,45,74,.065)}
.vg51-head{max-width:980px;margin-bottom:18px}
.vg51-eyebrow{margin:0 0 .55rem;color:#0b6380;text-transform:uppercase;letter-spacing:.12em;font-size:.75rem;font-weight:800}
.vg51-head h2{margin:0 0 .65rem;color:#073d63;font-size:clamp(1.55rem,2.8vw,2.35rem);line-height:1.08;letter-spacing:-.045em}
.vg51-head p{margin:0;color:#405b71;font-size:.98rem;line-height:1.62}
.vg51-grid{display:grid;grid-template-columns:repeat(4,1fr);gap:14px}
.vg51-card{overflow:hidden;border-radius:22px;background:#fff;border:1px solid rgba(127,160,186,.20);box-shadow:0 10px 24px rgba(20,45,74,.055)}
.vg51-card.vg51-wide{grid-column:span 2}
.vg51-card.vg51-panorama{grid-column:span 2}
.vg51-card figure{margin:0;background:#eef6fb;overflow:hidden;display:flex;align-items:center;justify-content:center}
.vg51-scene figure{aspect-ratio:1024/559}
.vg51-panorama figure{aspect-ratio:1280/540}
.vg51-card img{width:100%;height:100%;display:block;object-fit:contain}
.vg51-scene img{object-fit:cover}
.vg51-panorama img{object-fit:contain;background:#fff}
.vg51-card div{padding:14px 15px}
.vg51-card span{display:inline-flex;margin-bottom:.38rem;padding:.28rem .52rem;border-radius:999px;background:rgba(83,197,213,.11);color:#0b6380;font-size:.72rem;font-weight:800}
.vg51-card h3{margin:0 0 .35rem;color:#073d63;font-size:1rem;line-height:1.2}
.vg51-card p{margin:0;color:#607488;font-size:.86rem;line-height:1.45}
.res51-visual-grid{display:grid;grid-template-columns:1fr 1.35fr 1.2fr;gap:14px;margin-top:18px;align-items:stretch}
.res51-visual-grid a{display:block;overflow:hidden;border-radius:22px;background:#fff;text-decoration:none;border:1px solid rgba(127,160,186,.20);box-shadow:0 10px 24px rgba(20,45,74,.045)}
.res51-visual-grid img{display:block;width:100%;background:#eef6fb}
.res51-scene img{aspect-ratio:1024/559;object-fit:cover}
.res51-panorama img{aspect-ratio:1280/540;object-fit:contain;background:#fff}
.res51-visual-grid strong{display:block;padding:13px 14px 4px;color:#073d63}
.res51-visual-grid span{display:block;padding:0 14px 14px;color:#607488;font-size:.85rem;line-height:1.42}
.paper-visual-context-v51{margin:1.4rem 0;padding:1rem;border-radius:22px;background:linear-gradient(180deg,rgba(255,255,255,.98),rgba(248,252,255,.98));border:1px solid rgba(130,165,194,.22);box-shadow:0 12px 28px rgba(20,45,74,.055)}
.paper-visual-context-v51 h2{margin:0 0 .8rem;color:#073d63;font-size:1.18rem;letter-spacing:-.02em}
.paper-visual-context-grid-v51{display:grid;grid-template-columns:minmax(300px,1.05fr) .95fr;gap:14px;align-items:center}
.paper-visual-panorama-v51{grid-template-columns:minmax(420px,1.25fr) .75fr}
.paper-visual-context-grid-v51 figure{margin:0;border-radius:18px;overflow:hidden;border:1px solid rgba(127,160,186,.18);background:#fff;display:flex;align-items:center;justify-content:center}
.paper-visual-context-grid-v51 img{display:block;width:100%;height:auto;object-fit:contain}
.paper-visual-panorama-v51 figure{aspect-ratio:1280/540}
.paper-visual-panorama-v51 img{height:100%;object-fit:contain}
.paper-visual-scene-v51 figure{aspect-ratio:1024/559}
.paper-visual-scene-v51 img{height:100%;object-fit:cover}
.paper-visual-context-grid-v51 p{margin:0 0 .75rem;color:#405b71;line-height:1.58}
.paper-visual-context-grid-v51 a{color:#084f72;font-weight:700;text-decoration:none}
.paper-visual-context-grid-v51 a:hover{text-decoration:underline}
@media(max-width:980px){.visual-gallery-v51{width:min(100%,calc(100% - 22px));padding:18px}.vg51-grid{grid-template-columns:1fr 1fr}.vg51-card.vg51-wide,.vg51-card.vg51-panorama{grid-column:span 2}.res51-visual-grid{grid-template-columns:1fr}.paper-visual-context-grid-v51,.paper-visual-panorama-v51{grid-template-columns:1fr}}
@media(max-width:640px){.visual-gallery-v51{width:min(100%,calc(100% - 18px));border-radius:24px;padding:16px}.vg51-grid{grid-template-columns:1fr}.vg51-card.vg51-wide,.vg51-card.vg51-panorama{grid-column:span 1}}
/* === Visual research gallery v51 END === */
'''
    write(CSS, css.rstrip() + "\n\n" + css_block.strip() + "\n")
    print("Updated CSS with v51 natural-ratio visual styles.")

if LLMS.exists():
    llms = read(LLMS)
    llms = re.sub(r"\n## Visual research gallery\n\n- Visual Research Gallery:.*?(?=\n## |\Z)", "\n", llms, flags=re.S)
    add = '''
## Visual research gallery

- Visual Research Gallery: https://ahmedmansoour.github.io/indoor-positioning-hub/index.html#visual-research-gallery
- Purpose: a natural-ratio visual index for future spatial intelligence, 2D indoor navigation, multi-floor indoor positioning, autonomous radio-map generation, and indoor-outdoor transition-aware 3D positioning.
- Figure dimensions used in layout: 1024 × 559 for the three scene figures, 1280 × 540 for the autonomous radio-map workflow, and 800 × 349 for the indoor-outdoor and 3D-positioning workflow.
- Related assets: assets/visual-gallery-v51/future-spatial-intelligence.webp, assets/visual-gallery-v51/indoor-navigation-2d-mall.webp, assets/visual-gallery-v51/indoor-navigation-3d-multilevel.webp, assets/visual-gallery-v51/everywhere-autonomous-radio-map-animated.webp, assets/visual-gallery-v51/iod-3d-positioning-demo-animated.webp
'''
    marker = "## Resources and reproducibility page"
    if marker in llms:
        llms = llms.replace(marker, add + "\n" + marker)
    else:
        llms = llms.rstrip() + "\n" + add + "\n"
    write(LLMS, llms)
    print("Updated llms.txt.")

print("Done: v51 improved visual layout, natural ratios, and animated workflow WebP assets.")
