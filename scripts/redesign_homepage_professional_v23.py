from pathlib import Path
import re

ROOT = Path('.')
INDEX_PATH = ROOT / 'index.html'
CSS_PATH = ROOT / 'assets' / 'css' / 'style.css'

INDEX_HTML = r'''<!doctype html>
<html lang="en">
<head>
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width, initial-scale=1">
  <title>Indoor Positioning Hub | Ahmed Mansour</title>
  <meta name="description" content="Indoor Positioning Hub by Ahmed Mansour, Ph.D., with publications, PDFs, citation resources, datasets, code links, visual research atlas, and definitions of indoor positioning, indoor localization, and indoor navigation.">
  <link rel="stylesheet" href="assets/css/style.css">
</head>
<body class="home-v23-page">
  <header class="site-header v23-site-header">
    <a class="site-brand" href="index.html" aria-label="Indoor Positioning Hub home">
      <span class="brand-mark">IP</span>
      <span class="brand-text">Indoor Positioning Hub</span>
    </a>
    <nav class="site-nav" aria-label="Main navigation">
      <a href="index.html" class="active">Home</a>
      <a href="publications.html">Publications</a>
      <a href="research-themes.html">Research Themes</a>
      <a href="resources.html">Datasets &amp; Code</a>
      <a href="citation-resources.html">Citation Resources</a>
      <a href="about.html">About</a>
    </nav>
  </header>

  <main class="v23-home" id="home">
    <section class="v23-hero" aria-label="Ahmed Mansour academic homepage">
      <div class="v23-hero-bg" aria-hidden="true"></div>
      <div class="v23-hero-grid">
        <div class="v23-hero-copy">
          <p class="v23-eyebrow">Indoor Positioning Hub</p>
          <h1>Ahmed Mansour, Ph.D.</h1>
          <p class="v23-titleline">Indoor positioning, localization, navigation, and spatial intelligence for smart built environments.</p>
          <p class="v23-lead">This website brings together my academic profile, publication portfolio, downloadable papers, citation resources, datasets, code links, and visual research maps. The research connects smartphone sensing, Wi-Fi fingerprinting, pedestrian dead reckoning, mobile crowdsensing, autonomous radio mapping, indoor-outdoor awareness, and deployment-ready indoor spatial intelligence.</p>
          <div class="v23-actions" aria-label="Homepage shortcuts">
            <a class="v23-btn v23-btn-main" href="publications.html">Explore publications</a>
            <a class="v23-btn" href="#research-atlas">Research atlas</a>
            <a class="v23-btn" href="assets/cv/ahmed-mansour-public-cv.pdf">Download CV</a>
            <a class="v23-btn" href="citation-resources.html">Citation resources</a>
          </div>
          <div class="v23-tag-row" aria-label="Research keywords">
            <span>Wi-Fi fingerprinting</span><span>PDR</span><span>GNSS/PDR integration</span><span>Mobile crowdsensing</span><span>Radio maps</span><span>Indoor-outdoor awareness</span>
          </div>
        </div>

        <aside class="v23-profile" aria-label="Ahmed Mansour profile card">
          <div class="v23-photo-frame">
            <img src="assets/img/profile/ahmed-mansour-photo.webp" alt="Ahmed Mansour academic profile photo" loading="eager" decoding="async">
          </div>
          <div class="v23-profile-body">
            <h2>Indoor positioning researcher</h2>
            <p>Researcher in geomatics, indoor localization, smartphone sensing, crowdsensing-based IPS, PDR, radio-map maintenance, and smart built-environment positioning.</p>
            <div class="v23-mini-stats"><span><strong>17+</strong> outputs</span><span><strong>IPS</strong> methods and deployment</span></div>
          </div>
        </aside>
      </div>
    </section>

    <section class="v23-logos" aria-label="Academic affiliations">
      <article><img src="assets/home/polyu-logo.webp" alt="The Hong Kong Polytechnic University logo" loading="lazy" decoding="async"><div><strong>The Hong Kong Polytechnic University</strong><span>Ph.D. research training and postdoctoral work in geomatics, sensor fusion, indoor positioning, and smart built environments.</span></div></article>
      <article><img src="assets/home/cairo-university-logo.webp" alt="Cairo University logo" loading="lazy" decoding="async"><div><strong>Cairo University</strong><span>Civil engineering, public works, geomatics, surveying, and foundational engineering background.</span></div></article>
    </section>

    <section class="v23-section v23-definitions" id="definitions" aria-label="Definitions of indoor positioning localization and navigation">
      <div class="v23-section-head">
        <p class="v23-eyebrow">Field guide</p><h2>What are indoor positioning, indoor localization, and indoor navigation?</h2>
        <p>These terms are related, but each describes a different layer of the indoor spatial-information pipeline. The distinction helps readers move from measurements to estimated locations, routes, services, and operational decisions inside buildings where satellite positioning is weak or unavailable.</p>
      </div>
      <div class="v23-def-grid">
        <article><img src="assets/home/positioning-icon.webp" alt="Indoor positioning icon" loading="lazy" decoding="async"><h3>Indoor positioning</h3><p>Indoor positioning estimates the position of a person, smartphone, robot, asset, or sensor inside a building using radio signals, inertial sensors, maps, vision, magnetic fields, barometers, or fused measurements.</p></article>
        <article><img src="assets/home/building-pin-icon.webp" alt="Indoor localization icon" loading="lazy" decoding="async"><h3>Indoor localization</h3><p>Indoor localization determines where the user or object is within an indoor reference frame, such as a coordinate, floor, room, corridor, zone, landmark, or building-level map representation.</p></article>
        <article><img src="assets/home/campus-pin-icon.webp" alt="Indoor navigation icon" loading="lazy" decoding="async"><h3>Indoor navigation</h3><p>Indoor navigation uses position, heading, motion state, route information, and spatial context to guide movement, support wayfinding, enable location-aware services, and connect positioning outputs to decisions.</p></article>
      </div>
    </section>

    <section class="v23-section v23-bridge" aria-label="Research profile overview"><div class="v23-bridge-card"><div><p class="v23-eyebrow">Academic profile</p><h2>From positioning measurements to indoor spatial intelligence</h2><p>The hub is organized to help readers move from a research question to the relevant paper, method, dataset, figure, or citation entry. The work connects smartphone sensing, radio signals, human mobility, map information, and deployment constraints into practical positioning systems for buildings, campuses, cities, and smart built environments.</p></div><div class="v23-focus-list"><span>Seamless indoor-outdoor positioning</span><span>User-friendly crowd-powered IPS</span><span>Autonomous 3D radio-map scaling</span><span>Robust PDR and heading correction</span><span>GNSS/PDR integration in urban areas</span><span>Deployment-aware spatial intelligence</span></div></div></section>

    <section class="v23-section v23-atlas" id="research-atlas" aria-label="Research themes and visual research atlas">
      <div class="v23-section-head v23-centered"><p class="v23-eyebrow">Research Themes and Visual Research Atlas</p><h2>A thematic map of Ahmed Mansour's work across indoor positioning research, engineering, and deployment.</h2><p>The atlas links core papers, system concepts, and visual explanations across sensing, inference, mapping, crowdsensing, pedestrian navigation, and deployment readiness.</p></div>
      <div class="v23-atlas-grid">
        <article class="v23-atlas-card v23-atlas-wide"><img src="assets/home/indoor-navigation-office.webp" alt="Indoor navigation and positioning in a smart building" loading="lazy" decoding="async"><div><h3>Smart indoor positioning in real buildings</h3><p>Indoor positioning systems must work in complex spaces with changing signals, moving users, multiple floors, and limited user attention. This direction connects research outputs to operational indoor services.</p><a href="publications.html">Open publication portfolio</a></div></article>
        <article class="v23-atlas-card"><img src="assets/home/layered-building-positioning.webp" alt="Layered indoor positioning and localization concept" loading="lazy" decoding="async"><div><h3>Signals, sensors, maps, and context</h3><p>Research themes include Wi-Fi fingerprinting, PDR, sensor fusion, indoor-outdoor detection, radio-map maintenance, and context-aware positioning pipelines.</p><a href="research-themes.html">Explore research themes</a></div></article>
        <article class="v23-atlas-card v23-list-card"><h3>Core directions</h3><ul><li>Indoor positioning and localization</li><li>Wi-Fi fingerprinting and autonomous radio maps</li><li>Pedestrian dead reckoning and heading control</li><li>Mobile crowdsensing and user-centered IPS</li><li>Indoor-outdoor awareness and seamless positioning</li><li>Spatial intelligence for smart built environments</li></ul></article>
      </div>
    </section>

    <section class="v23-section v23-access" aria-label="Publication and citation access"><div class="v23-section-head"><p class="v23-eyebrow">Publication access</p><h2>Find papers, PDFs, citation records, and visual explanations</h2><p>Each publication page is designed for fast reading and reuse, with first-page previews, PDF access where available, DOI metadata, BibTeX, when-to-cite guidance, long research-story summaries, and selected visual explanations.</p></div><div class="v23-access-grid"><a href="publications.html"><strong>Publication portfolio</strong><span>Visual paper cards with first-page previews, DOI links, venues, and topic cues.</span></a><a href="citation-resources.html"><strong>Citation resources</strong><span>BibTeX entries, citation-ready paper titles, and paper-use guidance.</span></a><a href="resources.html"><strong>Datasets and code</strong><span>Shared resources, reproducibility links, and supporting research materials.</span></a><a href="about.html"><strong>About Ahmed Mansour</strong><span>Academic background, research focus, and contact links.</span></a></div></section>
  </main>
  <footer class="site-footer"><p>&copy; Ahmed Mansour. Indoor Positioning Research, Engineering, and Deployment Hub.</p></footer>
</body>
</html>
'''

CSS_BLOCK = r'''
/* === Homepage professional integrated redesign v23 START === */
.home-v23-page{--v23-ink:#0b2438;--v23-blue:#064d6a;--v23-teal:#087f89;--v23-soft:#eff8fb;--v23-muted:#526b7e;--v23-border:rgba(68,126,157,.18);--v23-shadow:0 20px 58px rgba(8,31,54,.10);background:radial-gradient(circle at 12% 5%,rgba(31,163,181,.14),transparent 28%),radial-gradient(circle at 86% 3%,rgba(73,108,190,.10),transparent 30%),linear-gradient(180deg,#f7fbfd 0%,#fff 48%,#f4fafc 100%)!important;color:var(--v23-ink)}
.home-v23-page .v23-site-header{position:sticky;top:0;z-index:1000;display:flex;justify-content:space-between;align-items:center;gap:1.1rem;padding:.85rem clamp(1rem,3.5vw,3rem);background:rgba(255,255,255,.9);backdrop-filter:blur(18px);border-bottom:1px solid var(--v23-border);box-shadow:0 10px 30px rgba(8,31,54,.05)}
.home-v23-page .site-brand{display:flex;align-items:center;gap:.62rem;color:var(--v23-ink);text-decoration:none;font-weight:900;letter-spacing:-.02em}.home-v23-page .brand-mark{width:38px;height:38px;border-radius:14px;display:grid;place-items:center;color:#fff;background:linear-gradient(135deg,#064d6a,#0b9aa3);box-shadow:0 12px 24px rgba(7,88,116,.18)}.home-v23-page .brand-text{font-size:1.06rem}.home-v23-page .site-nav{display:flex;flex-wrap:wrap;justify-content:flex-end;gap:.22rem}.home-v23-page .site-nav a{padding:.52rem .72rem;border-radius:999px;text-decoration:none;color:#0b4f70;font-weight:780;font-size:.92rem}.home-v23-page .site-nav a:hover,.home-v23-page .site-nav a.active{background:rgba(11,154,163,.11);color:#043c54}
.home-v23-page .v23-home{overflow:hidden}.home-v23-page .v23-hero{position:relative;max-width:1360px;margin:0 auto;padding:clamp(1.9rem,4vw,4.2rem) clamp(1rem,4vw,3.2rem) 1.3rem}.home-v23-page .v23-hero-bg{position:absolute;inset:1.1rem clamp(.6rem,2vw,1.4rem) 0;border-radius:42px;background:linear-gradient(104deg,rgba(255,255,255,.97) 0%,rgba(255,255,255,.91) 58%,rgba(229,246,250,.84) 100%),url('../home/subtle-circuit-background.webp') center/cover no-repeat;border:1px solid var(--v23-border);box-shadow:var(--v23-shadow);z-index:-1}.home-v23-page .v23-hero-grid{display:grid;grid-template-columns:minmax(0,1.18fr) minmax(300px,.52fr);gap:clamp(1.3rem,3vw,3rem);align-items:center}.home-v23-page .v23-eyebrow{margin:0 0 .65rem;color:var(--v23-teal);text-transform:uppercase;letter-spacing:.14em;font-size:.76rem;font-weight:900}.home-v23-page .v23-hero-copy h1{margin:0;font-size:clamp(2.75rem,5.6vw,5.1rem);line-height:.96;letter-spacing:-.055em;color:var(--v23-ink)}.home-v23-page .v23-titleline{margin:.85rem 0 0;font-size:clamp(1.12rem,1.85vw,1.58rem);line-height:1.36;color:#123f5d;font-weight:820;max-width:880px}.home-v23-page .v23-lead{margin:1rem 0 0;max-width:900px;line-height:1.72;color:var(--v23-muted);font-size:1.02rem}
.home-v23-page .v23-actions{display:flex;flex-wrap:wrap;gap:.66rem;margin-top:1.25rem}.home-v23-page .v23-btn{display:inline-flex;align-items:center;justify-content:center;min-height:42px;padding:.64rem .96rem;border-radius:999px;border:1px solid var(--v23-border);background:rgba(255,255,255,.86);color:#074d6b;font-weight:850;text-decoration:none;box-shadow:0 10px 22px rgba(8,31,54,.06)}.home-v23-page .v23-btn-main{background:linear-gradient(135deg,#075a7a,#0b9aa3);color:white;border-color:transparent}.home-v23-page .v23-tag-row,.home-v23-page .v23-focus-list{display:flex;flex-wrap:wrap;gap:.46rem;margin-top:1rem}.home-v23-page .v23-tag-row span,.home-v23-page .v23-focus-list span{padding:.4rem .63rem;border-radius:999px;background:rgba(255,255,255,.76);border:1px solid var(--v23-border);color:#174761;font-size:.88rem;font-weight:760}
.home-v23-page .v23-profile{border-radius:32px;padding:1.05rem;background:linear-gradient(180deg,rgba(255,255,255,.95),rgba(238,248,252,.94));border:1px solid var(--v23-border);box-shadow:0 22px 60px rgba(8,31,54,.12)}.home-v23-page .v23-photo-frame{width:min(100%,245px);aspect-ratio:1/1;margin:0 auto;border-radius:30px;overflow:hidden;background:#fff;border:8px solid rgba(255,255,255,.85);box-shadow:0 16px 34px rgba(9,42,69,.13)}.home-v23-page .v23-photo-frame img{width:100%;height:100%;object-fit:cover;display:block}.home-v23-page .v23-profile-body{text-align:center;padding:.72rem .25rem 0}.home-v23-page .v23-profile-body h2{margin:.1rem 0 .38rem;font-size:1.2rem;color:var(--v23-ink)}.home-v23-page .v23-profile-body p{margin:0 auto;color:var(--v23-muted);line-height:1.58;font-size:.95rem}.home-v23-page .v23-mini-stats{display:grid;grid-template-columns:1fr 1fr;gap:.6rem;margin-top:.85rem}.home-v23-page .v23-mini-stats span{border-radius:18px;background:#fff;border:1px solid var(--v23-border);padding:.65rem .55rem;color:#174761;font-size:.86rem}.home-v23-page .v23-mini-stats strong{display:block;color:#075a7a;font-size:1.05rem}
.home-v23-page .v23-logos{max-width:1280px;margin:1.1rem auto 0;padding:0 clamp(1rem,4vw,3.2rem);display:grid;grid-template-columns:repeat(2,minmax(0,1fr));gap:.85rem}.home-v23-page .v23-logos article{display:grid;grid-template-columns:84px minmax(0,1fr);gap:.85rem;align-items:center;padding:.95rem 1rem;border-radius:24px;background:rgba(255,255,255,.84);border:1px solid var(--v23-border);box-shadow:0 12px 30px rgba(8,31,54,.06)}.home-v23-page .v23-logos img{max-width:84px;max-height:58px;object-fit:contain}.home-v23-page .v23-logos strong{display:block;color:var(--v23-ink);margin-bottom:.18rem}.home-v23-page .v23-logos span{display:block;color:var(--v23-muted);line-height:1.45;font-size:.9rem}
.home-v23-page .v23-section{max-width:1280px;margin:clamp(1.2rem,3vw,2.3rem) auto 0;padding:0 clamp(1rem,4vw,3.2rem)}.home-v23-page .v23-section-head{max-width:920px;margin-bottom:1rem}.home-v23-page .v23-section-head h2{margin:0;font-size:clamp(1.85rem,3vw,2.9rem);line-height:1.05;letter-spacing:-.04em;color:var(--v23-ink)}.home-v23-page .v23-section-head p:not(.v23-eyebrow){color:var(--v23-muted);line-height:1.68;font-size:1rem}.home-v23-page .v23-centered{text-align:center;margin-left:auto;margin-right:auto}.home-v23-page .v23-def-grid{display:grid;grid-template-columns:repeat(3,minmax(0,1fr));gap:1rem}.home-v23-page .v23-def-grid article,.home-v23-page .v23-bridge-card,.home-v23-page .v23-atlas-card,.home-v23-page .v23-access-grid a{background:rgba(255,255,255,.9);border:1px solid var(--v23-border);border-radius:28px;box-shadow:0 14px 38px rgba(8,31,54,.07)}.home-v23-page .v23-def-grid article{padding:1.05rem}.home-v23-page .v23-def-grid img{width:48px;height:48px;object-fit:contain;margin-bottom:.65rem}.home-v23-page .v23-def-grid h3{margin:.1rem 0 .45rem;color:#0b4260;font-size:1.12rem}.home-v23-page .v23-def-grid p{color:var(--v23-muted);line-height:1.62;margin:0;font-size:.96rem}
.home-v23-page .v23-bridge-card{display:grid;grid-template-columns:minmax(0,1fr) minmax(280px,.72fr);gap:1.2rem;align-items:center;padding:clamp(1.15rem,2.4vw,1.8rem);background:linear-gradient(135deg,rgba(255,255,255,.94),rgba(232,247,250,.88))}.home-v23-page .v23-bridge-card h2{margin:0;font-size:clamp(1.7rem,2.8vw,2.55rem);letter-spacing:-.04em}.home-v23-page .v23-bridge-card p{color:var(--v23-muted);line-height:1.68}.home-v23-page .v23-focus-list{margin:0;align-content:center}.home-v23-page .v23-atlas-grid{display:grid;grid-template-columns:1.2fr .8fr;gap:1rem}.home-v23-page .v23-atlas-card{overflow:hidden}.home-v23-page .v23-atlas-wide{grid-row:span 2}.home-v23-page .v23-atlas-card img{width:100%;height:230px;object-fit:cover;display:block}.home-v23-page .v23-atlas-wide img{height:360px}.home-v23-page .v23-atlas-card div,.home-v23-page .v23-list-card{padding:1.05rem 1.15rem}.home-v23-page .v23-atlas-card h3{margin:0 0 .45rem;color:#0b4260}.home-v23-page .v23-atlas-card p,.home-v23-page .v23-list-card li{color:var(--v23-muted);line-height:1.58}.home-v23-page .v23-atlas-card a{color:#086c83;font-weight:850;text-decoration:none}.home-v23-page .v23-list-card ul{margin:.6rem 0 0;padding-left:1.2rem}
.home-v23-page .v23-access-grid{display:grid;grid-template-columns:repeat(4,minmax(0,1fr));gap:.9rem}.home-v23-page .v23-access-grid a{padding:1rem;text-decoration:none;color:var(--v23-ink)}.home-v23-page .v23-access-grid strong{display:block;margin-bottom:.35rem;color:#0b4260}.home-v23-page .v23-access-grid span{display:block;color:var(--v23-muted);line-height:1.5;font-size:.93rem}.home-v23-page .site-footer{margin-top:2.5rem;padding:1.4rem;text-align:center;color:var(--v23-muted)}
@media(max-width:980px){.home-v23-page .v23-hero-grid,.home-v23-page .v23-bridge-card,.home-v23-page .v23-atlas-grid{grid-template-columns:1fr}.home-v23-page .v23-logos,.home-v23-page .v23-def-grid,.home-v23-page .v23-access-grid{grid-template-columns:1fr}.home-v23-page .v23-profile{max-width:420px;margin:0 auto}.home-v23-page .v23-site-header{align-items:flex-start;flex-direction:column}.home-v23-page .site-nav{justify-content:flex-start}}
/* === Homepage professional integrated redesign v23 END === */
'''

INDEX_PATH.write_text(INDEX_HTML, encoding='utf-8')
css = CSS_PATH.read_text(encoding='utf-8', errors='ignore') if CSS_PATH.exists() else ''
patterns = [
    r'/\* === Homepage logo/background redesign v20 START === \*/.*?/\* === Homepage logo/background redesign v20 END === \*/',
    r'/\* === Homepage profile restore and definitions v21 START === \*/.*?/\* === Homepage profile restore and definitions v21 END === \*/',
    r'/\* === Homepage professional profile redesign v22 START === \*/.*?/\* === Homepage professional profile redesign v22 END === \*/',
    r'/\* === Homepage professional integrated redesign v23 START === \*/.*?/\* === Homepage professional integrated redesign v23 END === \*/',
]
for pat in patterns:
    css = re.sub(pat, '', css, flags=re.S)
css = css.rstrip() + '\n\n' + CSS_BLOCK.strip() + '\n'
CSS_PATH.write_text(css, encoding='utf-8')
print('Done: redesigned homepage with v23 professional integrated layout.')
print('Open: index.html?v=home-v23-professional-integrated')
