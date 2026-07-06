from pathlib import Path
import re

ROOT = Path(__file__).resolve().parents[1]

ATLAS_LINKS = {
    "Smart building positioning system": [
        ("Everywhere: A Framework for Ubiquitous Indoor Localization", "publications/everywhere-framework-ubiquitous-indoor-localization.html", "2022"),
        ("Towards Scalable IPS: User-Centric Challenges, Methods, and Recommendations for User-Friendly Crowd-Powered Schemes", "publications/towards-scalable-ips-user-centric-crowd-powered-framework.html", "2026"),
        ("SUNS: Seamless Ubiquitous Navigation System Based on GNSS, Wi-Fi, and MEMS Sensors", "publications/suns-seamless-ubiquitous-navigation-indoor-outdoor-awareness.html", "2022"),
    ],
    "Context descriptor c(t)": [
        ("SUNS: Seamless Ubiquitous Navigation System Based on GNSS, Wi-Fi, and MEMS Sensors", "publications/suns-seamless-ubiquitous-navigation-indoor-outdoor-awareness.html", "2022"),
        ("Everywhere: A Framework for Ubiquitous Indoor Localization", "publications/everywhere-framework-ubiquitous-indoor-localization.html", "2022"),
        ("A Modular Prompting Framework for AI-Guided Unobtrusive User Engagement in Crowd-Powered Indoor Positioning with Semantic Knowledge Graphs and GPT-4-Based LLMs", "publications/modular-prompting-ai-guided-user-engagement-crowd-powered-ips.html", "2025"),
    ],
    "Phone pose and trajectory behavior": [
        ("Hybrid Neural Network-Based PDR with Multi-Layer Heading Correction Across Smartphone Carrying Modes", "publications/hybrid-neural-network-pdr-multi-layer-heading-correction.html", "2026"),
        ("Enhancing Real-Time Heading Estimation for Pedestrian Navigation Using Deep Learning and Smartphone Sensors", "publications/enhancing-real-time-heading-estimation-deep-learning-smartphone-sensors.html", "2025"),
        ("Drift-Resistant Heading Estimation for Smartphone-Based Indoor Positioning via Adaptive Calibration Using Wi-Fi Fingerprinting and Magnetic Stability", "publications/drift-resistant-heading-estimation-wifi-magnetic-stability.html", "2026"),
        ("Drift-Control PDR for Long-Period Navigation Under Multiple Smartphone Poses", "publications/drift-control-pdr-long-period-navigation-smartphone-poses.html", "2021"),
    ],
    "Reliability-governed radio-map write-back": [
        ("Reliability-Governed Scaling of Mobile Crowdsensing-Based 3D Radio Mapping for Ubiquitous Indoor Positioning", "publications/reliability-governed-3d-radio-mapping-lifecycle-review.html", "2026"),
        ("Towards Ubiquitous IPS: Leveraging Crowdsourced Data Accumulation Over Time to Alleviate Reliance on External Sources in Initial Fingerprinting Map Generation", "publications/towards-ubiquitous-ips-crowdsourced-data-accumulation.html", "2024"),
        ("Everywhere: A Framework for Ubiquitous Indoor Localization", "publications/everywhere-framework-ubiquitous-indoor-localization.html", "2022"),
    ],
    "Crowd-powered IPS deployment realities": [
        ("Towards Scalable IPS: User-Centric Challenges, Methods, and Recommendations for User-Friendly Crowd-Powered Schemes", "publications/towards-scalable-ips-user-centric-crowd-powered-framework.html", "2026"),
        ("A Modular Prompting Framework for AI-Guided Unobtrusive User Engagement in Crowd-Powered Indoor Positioning with Semantic Knowledge Graphs and GPT-4-Based LLMs", "publications/modular-prompting-ai-guided-user-engagement-crowd-powered-ips.html", "2025"),
        ("Reliability-Governed Scaling of Mobile Crowdsensing-Based 3D Radio Mapping for Ubiquitous Indoor Positioning", "publications/reliability-governed-3d-radio-mapping-lifecycle-review.html", "2026"),
        ("Towards Ubiquitous IPS: Leveraging Crowdsourced Data Accumulation Over Time to Alleviate Reliance on External Sources in Initial Fingerprinting Map Generation", "publications/towards-ubiquitous-ips-crowdsourced-data-accumulation.html", "2024"),
    ],
    "Multisensor session log stream": [
        ("SUNS: Seamless Ubiquitous Navigation System Based on GNSS, Wi-Fi, and MEMS Sensors", "publications/suns-seamless-ubiquitous-navigation-indoor-outdoor-awareness.html", "2022"),
        ("GNSS Positioning Aided with Pedestrian Dead Reckoning in Urban Areas", "publications/gnss-positioning-aided-with-pdr-in-urban-areas.html", "2026"),
        ("Tightly Coupled Bluetooth Enhanced GNSS/PDR System for Pedestrian Navigation in Dense Urban Environments", "publications/tightly-coupled-bluetooth-enhanced-gnss-pdr-urban.html", "2024"),
        ("Everywhere: A Framework for Ubiquitous Indoor Localization", "publications/everywhere-framework-ubiquitous-indoor-localization.html", "2022"),
    ],
    "Skeleton, assembly, and refinement": [
        ("Towards Ubiquitous IPS: Leveraging Crowdsourced Data Accumulation Over Time to Alleviate Reliance on External Sources in Initial Fingerprinting Map Generation", "publications/towards-ubiquitous-ips-crowdsourced-data-accumulation.html", "2024"),
        ("Reliability-Governed Scaling of Mobile Crowdsensing-Based 3D Radio Mapping for Ubiquitous Indoor Positioning", "publications/reliability-governed-3d-radio-mapping-lifecycle-review.html", "2026"),
        ("Leveraging Human Mobility for Pervasive Smartphone Crowdsourcing in Indoor Positioning", "publications/leveraging-human-mobility-pervasive-smartphone-crowdsourcing.html", "2023"),
        ("The Power of Many: Multi-User Collaborative Indoor Localization", "publications/power-of-many-multi-user-collaborative-indoor-localization.html", "2023"),
    ],
    "Principles for scaling IPS": [
        ("Towards Scalable IPS: User-Centric Challenges, Methods, and Recommendations for User-Friendly Crowd-Powered Schemes", "publications/towards-scalable-ips-user-centric-crowd-powered-framework.html", "2026"),
        ("Everywhere: A Framework for Ubiquitous Indoor Localization", "publications/everywhere-framework-ubiquitous-indoor-localization.html", "2022"),
        ("Reliability-Governed Scaling of Mobile Crowdsensing-Based 3D Radio Mapping for Ubiquitous Indoor Positioning", "publications/reliability-governed-3d-radio-mapping-lifecycle-review.html", "2026"),
        ("A Modular Prompting Framework for AI-Guided Unobtrusive User Engagement in Crowd-Powered Indoor Positioning with Semantic Knowledge Graphs and GPT-4-Based LLMs", "publications/modular-prompting-ai-guided-user-engagement-crowd-powered-ips.html", "2025"),
    ],
}

CSS_BLOCK = r'''

/* Atlas paper-link blocks, added by scripts/add_atlas_paper_links.py */
.atlas-related-papers {
  margin-top: 0.95rem;
  padding: 0.95rem 1.05rem;
  border: 1px solid rgba(14, 116, 144, 0.16);
  border-left: 4px solid rgba(14, 116, 144, 0.72);
  border-radius: 14px;
  background: linear-gradient(180deg, rgba(240, 249, 255, 0.72), rgba(255, 255, 255, 0.94));
  box-shadow: 0 8px 22px rgba(15, 23, 42, 0.035);
}
.atlas-related-papers .related-label {
  display: inline-flex;
  align-items: center;
  gap: 0.35rem;
  margin-bottom: 0.25rem;
  font-size: 0.78rem;
  font-weight: 800;
  letter-spacing: 0.075em;
  text-transform: uppercase;
  color: #0f766e;
}
.atlas-related-papers ul {
  margin: 0.35rem 0 0 1.1rem;
  padding: 0;
}
.atlas-related-papers li {
  margin: 0.42rem 0;
  line-height: 1.52;
  color: #0f172a;
}
.atlas-related-papers a {
  color: #075985;
  font-weight: 650;
  text-decoration: none;
}
.atlas-related-papers a:hover,
.atlas-related-papers a:focus {
  text-decoration: underline;
  text-underline-offset: 3px;
}
.atlas-related-papers .paper-year {
  color: #64748b;
  white-space: nowrap;
}
@media (max-width: 760px) {
  .atlas-related-papers {
    padding: 0.85rem 0.9rem;
  }
  .atlas-related-papers li {
    margin: 0.55rem 0;
  }
}
'''

START = "<!-- atlas-related-papers-start -->"
END = "<!-- atlas-related-papers-end -->"

def make_block(items):
    lines = [START, '<div class="atlas-related-papers" aria-label="Related papers for this visual">', '  <div class="related-label">Related papers</div>', '  <ul>']
    for title, href, year in items:
        safe_title = title.replace('&', '&amp;')
        lines.append(f'    <li><a href="{href}">{safe_title}</a> <span class="paper-year">({year})</span></li>')
    lines += ['  </ul>', '</div>', END]
    return "\n".join(lines)

def remove_existing_blocks(html):
    return re.sub(r"\n?\s*" + re.escape(START) + r".*?" + re.escape(END) + r"\s*\n?", "\n", html, flags=re.S)

def add_links_to_html(path: Path):
    if not path.exists():
        return False, f"missing {path}"
    html = path.read_text(encoding="utf-8", errors="ignore")
    original = html
    html = remove_existing_blocks(html)
    inserted = 0
    for heading, links in ATLAS_LINKS.items():
        # Insert after the first paragraph that follows the h3 heading.
        # This keeps the link list visually under the figure caption/explanation.
        pattern = re.compile(rf"(<h3>\s*{re.escape(heading)}\s*</h3>\s*<p>.*?</p>)", flags=re.S)
        block = "\n" + make_block(links) + "\n"
        html, n = pattern.subn(lambda m, block=block: m.group(1) + block, html, count=1)
        inserted += n
    if html != original:
        path.write_text(html, encoding="utf-8")
    return True, f"{path}: inserted {inserted} related-paper blocks"

def ensure_css():
    css_path = ROOT / "assets" / "css" / "style.css"
    if not css_path.exists():
        return "missing assets/css/style.css"
    css = css_path.read_text(encoding="utf-8", errors="ignore")
    css = re.sub(r"\n?/\* Atlas paper-link blocks, added by scripts/add_atlas_paper_links\.py \*/.*", "", css, flags=re.S)
    css_path.write_text(css.rstrip() + CSS_BLOCK + "\n", encoding="utf-8")
    return "updated assets/css/style.css"

def main():
    targets = [ROOT / "index.html"]
    # Also update research-themes.html if it still contains the visual atlas.
    if (ROOT / "research-themes.html").exists():
        targets.append(ROOT / "research-themes.html")
    for target in targets:
        ok, msg = add_links_to_html(target)
        print(msg)
    print(ensure_css())
    print("Done. Check with: findstr /N /C:\"Related papers\" index.html")

if __name__ == "__main__":
    main()
