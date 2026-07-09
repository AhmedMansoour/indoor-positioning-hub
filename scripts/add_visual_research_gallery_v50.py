from pathlib import Path
import shutil
import re

ROOT = Path(".")
SRC = Path(__file__).resolve().parent.parent / "bundle_visuals"
VIS_DIR = ROOT / "assets" / "visual-gallery-v50"

INDEX = ROOT / "index.html"
RESOURCES = ROOT / "resources.html"
CSS = ROOT / "assets" / "css" / "style.css"
LLMS = ROOT / "llms.txt"

REQUIRED = [
    "future-spatial-intelligence.webp",
    "indoor-navigation-2d-mall.webp",
    "indoor-navigation-3d-multilevel.webp",
    "everywhere-autonomous-radio-map.gif",
    "iod-3d-positioning-demo.gif",
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

home_block_start = "<!-- === Visual research gallery v50 START === -->"
home_block_end = "<!-- === Visual research gallery v50 END === -->"

home_block = '''
<!-- === Visual research gallery v50 START === -->
<section class="visual-gallery-v50" id="visual-research-gallery" aria-label="Visual research gallery">
  <div class="vg50-head">
    <p class="vg50-eyebrow">Visual research gallery</p>
    <h2>From signals and motion to indoor spatial intelligence</h2>
    <p>These visuals provide a fast reading path through the hub. They illustrate the long-term vision, user-facing indoor navigation, multi-floor spatial context, autonomous radio-map generation, and indoor-outdoor transition-aware positioning.</p>
  </div>

  <div class="vg50-grid">
    <article class="vg50-card vg50-wide">
      <figure><img src="assets/visual-gallery-v50/future-spatial-intelligence.webp" alt="Future city-scale positioning and spatial intelligence vision with navigation overlays" loading="lazy" decoding="async"></figure>
      <div>
        <span>Vision layer</span>
        <h3>Future spatial intelligence</h3>
        <p>A high-level view of positioning as part of connected urban, indoor, and multi-level navigation services.</p>
      </div>
    </article>

    <article class="vg50-card">
      <figure><img src="assets/visual-gallery-v50/indoor-navigation-2d-mall.webp" alt="Two-dimensional indoor navigation and wayfinding in a shopping mall" loading="lazy" decoding="async"></figure>
      <div>
        <span>User-facing navigation</span>
        <h3>Indoor navigation services</h3>
        <p>Shows how indoor positioning supports maps, routes, landmarks, shops, and wayfinding inside a building.</p>
      </div>
    </article>

    <article class="vg50-card">
      <figure><img src="assets/visual-gallery-v50/indoor-navigation-3d-multilevel.webp" alt="Three-dimensional multi-floor indoor positioning with escalators and vertical context" loading="lazy" decoding="async"></figure>
      <div>
        <span>3D spatial context</span>
        <h3>Multi-floor positioning</h3>
        <p>Connects floor recognition, vertical movement, escalators, stairs, and multi-level indoor geometry.</p>
      </div>
    </article>

    <article class="vg50-card">
      <figure><img src="assets/visual-gallery-v50/everywhere-autonomous-radio-map.gif" alt="Workflow for autonomous radio and magnetic map generation from crowdsourced data" loading="lazy" decoding="async"></figure>
      <div>
        <span>Radio-map scaling</span>
        <h3>Autonomous map generation</h3>
        <p>Links mobile crowdsensing, database generation, radio and magnetic maps, and online positioning.</p>
      </div>
    </article>

    <article class="vg50-card">
      <figure><img src="assets/visual-gallery-v50/iod-3d-positioning-demo.gif" alt="Indoor outdoor detection and 3D positioning with floor detection demonstration" loading="lazy" decoding="async"></figure>
      <div>
        <span>Transition awareness</span>
        <h3>IOD and 3D positioning</h3>
        <p>Shows indoor-outdoor detection, transition states, 3D trajectory estimation, and floor-level positioning.</p>
      </div>
    </article>
  </div>
</section>
<!-- === Visual research gallery v50 END === -->
'''

resources_block_start = "<!-- === Resources visual materials v50 START === -->"
resources_block_end = "<!-- === Resources visual materials v50 END === -->"

resources_block = '''
<!-- === Resources visual materials v50 START === -->
<section class="res47-section res50-visuals" id="visual-materials">
  <div class="res47-section-head">
    <p class="res47-eyebrow">Visual research materials</p>
    <h2>Figures and animations used across the hub</h2>
    <p>These visuals support fast understanding of the main research directions without changing the paper-centered organization of the website. They are linked to the relevant research areas and publication records.</p>
  </div>
  <div class="res50-visual-grid">
    <a href="index.html#visual-research-gallery"><img src="assets/visual-gallery-v50/future-spatial-intelligence.webp" alt="Future spatial intelligence visual"><strong>Future spatial intelligence</strong><span>Homepage vision and positioning services.</span></a>
    <a href="research-themes.html#area-radio-map"><img src="assets/visual-gallery-v50/everywhere-autonomous-radio-map.gif" alt="Autonomous radio-map generation workflow"><strong>Autonomous map generation</strong><span>Area 2, mobile crowdsensing and Wi-Fi fingerprinting.</span></a>
    <a href="research-themes.html#area-seamless"><img src="assets/visual-gallery-v50/iod-3d-positioning-demo.gif" alt="Indoor-outdoor detection and 3D positioning"><strong>IOD and 3D positioning</strong><span>Area 3 and Area 4, transition and floor awareness.</span></a>
  </div>
</section>
<!-- === Resources visual materials v50 END === -->
'''

pub_block_template = '''
<!-- === Publication visual context v50 START === -->
<section class="paper-visual-context-v50" id="{section_id}">
  <h2>{heading}</h2>
  <div class="paper-visual-context-grid-v50">
    <figure>
      <img src="../assets/visual-gallery-v50/{image}" alt="{alt}" loading="lazy" decoding="async">
    </figure>
    <div>
      <p>{text}</p>
      <a href="../research-themes.html#{area_anchor}">Open the related research area</a>
    </div>
  </div>
</section>
<!-- === Publication visual context v50 END === -->
'''

def add_pub_visual(page_name, section_id, heading, image, alt, text, area_anchor):
    path = ROOT / "publications" / page_name
    if not path.exists():
        print(f"Skipped missing publication page: {page_name}")
        return
    html = read(path)
    html = remove_block(html, "<!-- === Publication visual context v50 START === -->", "<!-- === Publication visual context v50 END === -->")
    block = pub_block_template.format(section_id=section_id, heading=heading, image=image, alt=alt, text=text, area_anchor=area_anchor)
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
    html = remove_block(html, home_block_start, home_block_end)
    marker = "<!-- === Homepage research area 4 3d radio map v42 END === -->"
    if marker in html:
        html = insert_after(html, marker, home_block)
    elif '<section class="v23-section v23-access"' in html:
        html = insert_before(html, '<section class="v23-section v23-access"', home_block)
    else:
        html += "\n" + home_block
    write(INDEX, html)
    print("Updated index.html with visual gallery.")

if RESOURCES.exists():
    html = read(RESOURCES)
    html = remove_block(html, resources_block_start, resources_block_end)
    repro_marker = '<section class="res47-section">\n    <div class="res47-section-head"><p class="res47-eyebrow">Reproducibility by research area</p>'
    if repro_marker in html:
        html = insert_before(html, repro_marker, resources_block)
    elif "</main>" in html:
        html = insert_before(html, "</main>", resources_block)
    else:
        html += "\n" + resources_block
    write(RESOURCES, html)
    print("Updated resources.html with visual materials section.")

add_pub_visual(
    "everywhere-framework-ubiquitous-indoor-localization.html",
    "autonomous-map-generation-visual",
    "Visual workflow: autonomous radio-map generation",
    "everywhere-autonomous-radio-map.gif",
    "Autonomous database generation workflow for self-deployable indoor positioning",
    "This workflow visual summarizes the paper's deployment logic: ordinary users contribute pervasive signatures, the system generates and stores radio or magnetic maps, and online users query the generated reference for positioning.",
    "area-radio-map",
)

add_pub_visual(
    "suns-seamless-ubiquitous-navigation-indoor-outdoor-awareness.html",
    "iod-3d-positioning-visual",
    "Visual context: indoor-outdoor awareness and 3D positioning",
    "iod-3d-positioning-demo.gif",
    "Indoor-outdoor detection and 3D positioning with floor detection",
    "This animation illustrates the transition-aware positioning problem: the system must recognize indoor, outdoor, and semi-transition states while maintaining a usable position estimate across floors and spaces.",
    "area-seamless",
)

add_pub_visual(
    "reliability-governed-3d-radio-mapping-lifecycle-review.html",
    "multilevel-indoor-context-visual",
    "Visual context: multi-floor indoor spatial structure",
    "indoor-navigation-3d-multilevel.webp",
    "Multi-floor indoor navigation scene with vertical movement and indoor positioning cues",
    "This visual supports the review's 3D radio-map perspective by showing why floor recognition, vertical movement, and multi-level indoor spatial context are necessary for deployment-ready indoor positioning.",
    "area-3d",
)

if CSS.exists():
    css = read(CSS)
    css = re.sub(r"/\* === Visual research gallery v50 START === \*/.*?/\* === Visual research gallery v50 END === \*/", "", css, flags=re.S)
    css_block = '''
/* === Visual research gallery v50 START === */
.visual-gallery-v50{width:min(1180px,calc(100% - 56px));margin:28px auto 44px;padding:24px;border-radius:30px;background:linear-gradient(180deg,rgba(255,255,255,.98),rgba(248,252,255,.98));border:1px solid rgba(130,165,194,.23);box-shadow:0 16px 38px rgba(20,45,74,.065)}
.vg50-head{max-width:980px;margin-bottom:18px}
.vg50-eyebrow{margin:0 0 .55rem;color:#0b6380;text-transform:uppercase;letter-spacing:.12em;font-size:.75rem;font-weight:800}
.vg50-head h2{margin:0 0 .65rem;color:#073d63;font-size:clamp(1.55rem,2.8vw,2.35rem);line-height:1.08;letter-spacing:-.045em}
.vg50-head p{margin:0;color:#405b71;font-size:.98rem;line-height:1.62}
.vg50-grid{display:grid;grid-template-columns:repeat(4,1fr);gap:14px}
.vg50-card{overflow:hidden;border-radius:22px;background:#fff;border:1px solid rgba(127,160,186,.20);box-shadow:0 10px 24px rgba(20,45,74,.055)}
.vg50-card.vg50-wide{grid-column:span 2}
.vg50-card figure{margin:0;aspect-ratio:16/9;background:#eef6fb;overflow:hidden}
.vg50-card img{width:100%;height:100%;display:block;object-fit:cover}
.vg50-card div{padding:14px 15px}
.vg50-card span{display:inline-flex;margin-bottom:.38rem;padding:.28rem .52rem;border-radius:999px;background:rgba(83,197,213,.11);color:#0b6380;font-size:.72rem;font-weight:800}
.vg50-card h3{margin:0 0 .35rem;color:#073d63;font-size:1rem;line-height:1.2}
.vg50-card p{margin:0;color:#607488;font-size:.86rem;line-height:1.45}
.res50-visual-grid{display:grid;grid-template-columns:repeat(3,1fr);gap:14px;margin-top:18px}
.res50-visual-grid a{display:block;overflow:hidden;border-radius:22px;background:#fff;text-decoration:none;border:1px solid rgba(127,160,186,.20);box-shadow:0 10px 24px rgba(20,45,74,.045)}
.res50-visual-grid img{display:block;width:100%;aspect-ratio:16/9;object-fit:cover;background:#eef6fb}
.res50-visual-grid strong{display:block;padding:13px 14px 4px;color:#073d63}
.res50-visual-grid span{display:block;padding:0 14px 14px;color:#607488;font-size:.85rem;line-height:1.42}
.paper-visual-context-v50{margin:1.4rem 0;padding:1rem;border-radius:22px;background:linear-gradient(180deg,rgba(255,255,255,.98),rgba(248,252,255,.98));border:1px solid rgba(130,165,194,.22);box-shadow:0 12px 28px rgba(20,45,74,.055)}
.paper-visual-context-v50 h2{margin:0 0 .8rem;color:#073d63;font-size:1.18rem;letter-spacing:-.02em}
.paper-visual-context-grid-v50{display:grid;grid-template-columns:minmax(260px,.95fr) 1.05fr;gap:14px;align-items:center}
.paper-visual-context-grid-v50 figure{margin:0;border-radius:18px;overflow:hidden;border:1px solid rgba(127,160,186,.18);background:#eef6fb}
.paper-visual-context-grid-v50 img{display:block;width:100%;height:auto}
.paper-visual-context-grid-v50 p{margin:0 0 .75rem;color:#405b71;line-height:1.58}
.paper-visual-context-grid-v50 a{color:#084f72;font-weight:700;text-decoration:none}
.paper-visual-context-grid-v50 a:hover{text-decoration:underline}
@media(max-width:980px){.visual-gallery-v50{width:min(100%,calc(100% - 22px));padding:18px}.vg50-grid{grid-template-columns:1fr 1fr}.vg50-card.vg50-wide{grid-column:span 2}.res50-visual-grid{grid-template-columns:1fr}.paper-visual-context-grid-v50{grid-template-columns:1fr}}
@media(max-width:640px){.visual-gallery-v50{width:min(100%,calc(100% - 18px));border-radius:24px;padding:16px}.vg50-grid{grid-template-columns:1fr}.vg50-card.vg50-wide{grid-column:span 1}}
/* === Visual research gallery v50 END === */
'''
    write(CSS, css.rstrip() + "\n\n" + css_block.strip() + "\n")
    print("Updated CSS with visual gallery styles.")

if LLMS.exists():
    llms = read(LLMS)
    add = '''
## Visual research gallery

- Visual Research Gallery: https://ahmedmansoour.github.io/indoor-positioning-hub/index.html#visual-research-gallery
- Purpose: a visual index for future spatial intelligence, 2D indoor navigation, multi-floor indoor positioning, autonomous radio-map generation, and indoor-outdoor transition-aware 3D positioning.
- Related assets: assets/visual-gallery-v50/future-spatial-intelligence.webp, assets/visual-gallery-v50/indoor-navigation-2d-mall.webp, assets/visual-gallery-v50/indoor-navigation-3d-multilevel.webp, assets/visual-gallery-v50/everywhere-autonomous-radio-map.gif, assets/visual-gallery-v50/iod-3d-positioning-demo.gif
'''
    if "## Visual research gallery" not in llms:
        marker = "## Resources and reproducibility page"
        if marker in llms:
            llms = llms.replace(marker, add + "\n" + marker)
        else:
            llms = llms.rstrip() + "\n" + add + "\n"
        write(LLMS, llms)
        print("Updated llms.txt.")

print("Done: visual gallery assets copied and page sections updated.")
