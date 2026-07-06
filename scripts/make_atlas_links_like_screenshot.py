#!/usr/bin/env python3
"""Place simple paper-title bullet lists directly under each visual atlas figure.

This replaces the previous boxed "Related papers" design with the layout Ahmed requested:
plain blue paper-title bullet links under each figure, similar to the screenshot.

Run from the repository root:
    python scripts/make_atlas_links_like_screenshot.py
"""
from __future__ import annotations
from pathlib import Path
import html
import re

ROOT = Path.cwd()

# Titles must match the h3 titles in the visual atlas cards.
ATLAS_PAPERS: dict[str, list[tuple[str, str, str]]] = {
    "Smart building positioning system": [
        ("Everywhere: A Framework for Ubiquitous Indoor Localization", "publications/everywhere-framework-ubiquitous-indoor-localization.html", "2022"),
        ("SUNS: Seamless Ubiquitous Navigation System Based on GNSS, Wi-Fi, and MEMS Sensors", "publications/suns-seamless-ubiquitous-navigation-indoor-outdoor-awareness.html", "2022"),
        ("Towards Scalable IPS: User-Centric Challenges, Methods, and Recommendations for User-Friendly Crowd-Powered Schemes", "publications/towards-scalable-ips-user-centric-crowd-powered-framework.html", "2026"),
    ],
    "Context descriptor c(t)": [
        ("A Modular Prompting Framework for AI-Guided Unobtrusive User Engagement in Crowd-Powered Indoor Positioning with Semantic Knowledge Graphs and GPT-4-Based LLMs", "publications/modular-prompting-ai-guided-user-engagement-crowd-powered-ips.html", "2025"),
        ("SUNS: Seamless Ubiquitous Navigation System Based on GNSS, Wi-Fi, and MEMS Sensors", "publications/suns-seamless-ubiquitous-navigation-indoor-outdoor-awareness.html", "2022"),
        ("Everywhere: A Framework for Ubiquitous Indoor Localization", "publications/everywhere-framework-ubiquitous-indoor-localization.html", "2022"),
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
    ],
    "Crowd-powered IPS deployment realities": [
        ("Towards Scalable IPS: User-Centric Challenges, Methods, and Recommendations for User-Friendly Crowd-Powered Schemes", "publications/towards-scalable-ips-user-centric-crowd-powered-framework.html", "2026"),
        ("A Modular Prompting Framework for AI-Guided Unobtrusive User Engagement in Crowd-Powered Indoor Positioning with Semantic Knowledge Graphs and GPT-4-Based LLMs", "publications/modular-prompting-ai-guided-user-engagement-crowd-powered-ips.html", "2025"),
        ("Reliability-Governed Scaling of Mobile Crowdsensing-Based 3D Radio Mapping for Ubiquitous Indoor Positioning", "publications/reliability-governed-3d-radio-mapping-lifecycle-review.html", "2026"),
    ],
    "Multisensor session log stream": [
        ("SUNS: Seamless Ubiquitous Navigation System Based on GNSS, Wi-Fi, and MEMS Sensors", "publications/suns-seamless-ubiquitous-navigation-indoor-outdoor-awareness.html", "2022"),
        ("GNSS Positioning Aided with Pedestrian Dead Reckoning in Urban Areas", "publications/gnss-positioning-aided-with-pdr-in-urban-areas.html", "2026"),
        ("Tightly Coupled Bluetooth Enhanced GNSS/PDR System for Pedestrian Navigation in Dense Urban Environments", "publications/tightly-coupled-bluetooth-enhanced-gnss-pdr-urban.html", "2024"),
        ("AC-HMM: Azimuth-Constrained Hidden Markov Model-Based Map Matching for Robust Pedestrian Positioning in Urban Canyons", "publications/ac-hmm-azimuth-constrained-map-matching-urban-canyons.html", "2026"),
    ],
    "Skeleton, assembly, and refinement": [
        ("Towards Ubiquitous IPS: Leveraging Crowdsourced Data Accumulation Over Time to Alleviate Reliance on External Sources in Initial Fingerprinting Map Generation", "publications/towards-ubiquitous-ips-crowdsourced-data-accumulation.html", "2024"),
        ("Leveraging Human Mobility for Pervasive Smartphone Crowdsourcing in Indoor Positioning", "publications/leveraging-human-mobility-pervasive-smartphone-crowdsourcing.html", "2023"),
        ("The Power of Many: Multi-User Collaborative Indoor Localization", "publications/power-of-many-multi-user-collaborative-indoor-localization.html", "2023"),
        ("Reliability-Governed Scaling of Mobile Crowdsensing-Based 3D Radio Mapping for Ubiquitous Indoor Positioning", "publications/reliability-governed-3d-radio-mapping-lifecycle-review.html", "2026"),
    ],
    "Principles for scaling IPS": [
        ("Towards Scalable IPS: User-Centric Challenges, Methods, and Recommendations for User-Friendly Crowd-Powered Schemes", "publications/towards-scalable-ips-user-centric-crowd-powered-framework.html", "2026"),
        ("Everywhere: A Framework for Ubiquitous Indoor Localization", "publications/everywhere-framework-ubiquitous-indoor-localization.html", "2022"),
        ("Reliability-Governed Scaling of Mobile Crowdsensing-Based 3D Radio Mapping for Ubiquitous Indoor Positioning", "publications/reliability-governed-3d-radio-mapping-lifecycle-review.html", "2026"),
    ],
}

NEW_START = "<!-- atlas-paper-title-links-start -->"
NEW_END = "<!-- atlas-paper-title-links-end -->"
OLD_START = "<!-- atlas-related-papers-start -->"
OLD_END = "<!-- atlas-related-papers-end -->"

CSS = r'''

/* ============================================================
   Plain atlas paper-title links under each visual figure
   Added by scripts/make_atlas_links_like_screenshot.py
   ============================================================ */
.atlas-paper-title-links {
  margin: 1.05rem 0 0;
  padding: 0;
}
.atlas-paper-title-links ul {
  margin: 0.25rem 0 0 1.25rem;
  padding: 0;
}
.atlas-paper-title-links li {
  margin: 0.55rem 0;
  padding-left: 0.15rem;
  color: #0f172a;
  line-height: 1.65;
}
.atlas-paper-title-links a {
  color: #075083;
  font-weight: 650;
  text-decoration: none;
}
.atlas-paper-title-links a:hover,
.atlas-paper-title-links a:focus {
  color: #003f66;
  text-decoration: underline;
  text-underline-offset: 4px;
}
.atlas-paper-title-links .paper-year {
  color: #64748b;
  white-space: nowrap;
}
.visual-atlas-card .atlas-paper-title-links {
  font-size: clamp(1.02rem, 1.45vw, 1.28rem);
}
@media (max-width: 760px) {
  .visual-atlas-card .atlas-paper-title-links {
    font-size: 1rem;
  }
  .atlas-paper-title-links li {
    margin: 0.48rem 0;
    line-height: 1.55;
  }
}
'''


def read(path: Path) -> str:
    return path.read_text(encoding="utf-8", errors="ignore") if path.exists() else ""


def write(path: Path, text: str) -> None:
    path.write_text(text, encoding="utf-8", newline="\n")


def remove_old_blocks(text: str) -> str:
    # Remove the previous boxed Related papers blocks and the new blocks if the script is rerun.
    text = re.sub(r"\n?\s*" + re.escape(OLD_START) + r".*?" + re.escape(OLD_END) + r"\s*\n?", "\n", text, flags=re.S)
    text = re.sub(r"\n?\s*" + re.escape(NEW_START) + r".*?" + re.escape(NEW_END) + r"\s*\n?", "\n", text, flags=re.S)
    return text


def make_plain_list(items: list[tuple[str, str, str]]) -> str:
    lines = [NEW_START, '<div class="atlas-paper-title-links" aria-label="Papers linked to this visual">', '  <ul>']
    for title, href, year in items:
        lines.append(
            f'    <li><a href="{html.escape(href)}">{html.escape(title)}</a> '
            f'<span class="paper-year">({html.escape(year)})</span></li>'
        )
    lines += ['  </ul>', '</div>', NEW_END]
    return "\n".join(lines)


def insert_for_visual_cards(text: str) -> tuple[str, int]:
    text = remove_old_blocks(text)
    inserted = 0

    for title, items in ATLAS_PAPERS.items():
        # Capture a visual atlas card up to the close of the caption div.
        # The list is inserted after the caption, so it appears directly below the figure explanation,
        # as a plain bullet list under the same visual card.
        pattern = re.compile(
            r'(<article\s+class="visual-atlas-card"[^>]*>\s*'
            r'<img\b[^>]*>\s*'
            r'<div\s+class="visual-atlas-caption"[^>]*>\s*'
            r'<h3>\s*' + re.escape(title) + r'\s*</h3>\s*'
            r'<p>.*?</p>\s*'
            r'</div>)',
            flags=re.S | re.I,
        )
        block = "\n" + make_plain_list(items) + "\n"
        text, n = pattern.subn(lambda m, block=block: m.group(1).rstrip() + block, text, count=1)
        inserted += n
    return text, inserted


def update_html(path: Path) -> None:
    if not path.exists():
        print(f"[skip] missing {path}")
        return
    text = read(path)
    new_text, inserted = insert_for_visual_cards(text)
    if new_text != text:
        write(path, new_text)
    print(f"[html] {path}: inserted {inserted} plain paper-link lists")


def update_css() -> None:
    css_path = ROOT / "assets" / "css" / "style.css"
    if not css_path.exists():
        print("[skip] missing assets/css/style.css")
        return
    css = read(css_path)
    # Remove previous v3 CSS if it was appended at the end.
    css = re.sub(
        r"\n?/\* Atlas paper-link blocks, added by scripts/add_atlas_paper_links\.py \*/.*?(?=\n/\* ============================================================\n   Plain atlas paper-title links|\Z)",
        "\n",
        css,
        flags=re.S,
    )
    # Remove older runs of this exact v4 CSS.
    css = re.sub(
        r"\n?/\* ============================================================\n   Plain atlas paper-title links under each visual figure\n   Added by scripts/make_atlas_links_like_screenshot\.py\n   ============================================================ \*/.*?(?=\n/\* ============================================================|\Z)",
        "\n",
        css,
        flags=re.S,
    )
    css = css.rstrip() + CSS + "\n"
    write(css_path, css)
    print("[css] updated assets/css/style.css")


def main() -> None:
    update_html(ROOT / "index.html")
    # Update research-themes too if it still has the same atlas cards.
    update_html(ROOT / "research-themes.html")
    update_css()
    print("\nDone. Check with:")
    print('  findstr /N /C:"atlas-paper-title-links" index.html')
    print('  findstr /N /C:"atlas-related-papers" index.html')


if __name__ == "__main__":
    main()
