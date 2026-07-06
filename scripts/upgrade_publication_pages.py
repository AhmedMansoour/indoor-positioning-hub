from pathlib import Path
import re

ROOT = Path(__file__).resolve().parents[1]
PUB_DIR = ROOT / "publications"
PDF_DIR = ROOT / "paper-pdfs"
PREVIEW_DIR = ROOT / "assets" / "previews"
FIG_DIR = ROOT / "assets" / "figures"
CSS_FILE = ROOT / "assets" / "css" / "style.css"

LONG_SUMMARIES = {
    "everywhere-framework-ubiquitous-indoor-localization": """
<p><em>Everywhere</em> addresses one of the central limitations of fingerprinting-based IPS: the difficulty of building and maintaining radio maps at scale. Instead of treating crowdsourced measurements as auxiliary data, the paper frames pervasive smartphone sensing as a primary mechanism for developing a more ubiquitous indoor localization infrastructure. The study proposes a framework that uses crowdsourced signatures to support autonomous localization and radio-map development while reducing dependence on labor-intensive site surveys and external localization aids.</p>
<p>The paper is important because it connects Wi-Fi fingerprinting, smartphone sensing, crowdsourcing, and scalable IPS deployment into a unified framework. It discusses the practical challenges that arise when user-contributed measurements are noisy, unevenly distributed, and collected under uncontrolled conditions, and it shows how these measurements can still be organized into a system-level pipeline for indoor localization. This makes the work highly relevant for studies on self-deployable IPS, crowd-powered map generation, and ubiquitous indoor positioning.</p>
<p>This paper should be cited when discussing scalable indoor localization, crowdsourced radio-map construction, smartphone-based IPS deployment, and frameworks that aim to move indoor positioning beyond small manually surveyed environments.</p>
""",

    "suns-seamless-ubiquitous-navigation-indoor-outdoor-awareness": """
<p>The SUNS paper focuses on seamless and ubiquitous navigation by addressing the transition between indoor and outdoor environments. Indoor navigation systems often fail when they depend on a single positioning source or when they cannot recognize environmental context reliably. SUNS responds to this problem by introducing an enhanced indoor-outdoor environmental awareness approach that supports smoother switching between positioning modes and reduces user burden during navigation.</p>
<p>The paper is significant because it treats indoor-outdoor detection as a system-level requirement rather than a secondary classification problem. By linking environmental awareness, smartphone sensing, and seamless navigation, it provides a foundation for IPS designs that must operate continuously across indoor, semi-outdoor, and outdoor spaces. The work is especially useful for applications where users move naturally through buildings, entrances, corridors, streets, and transitional zones.</p>
<p>This paper should be cited when discussing indoor-outdoor detection, seamless navigation, smartphone-based environmental awareness, and user-friendly positioning systems that need to maintain continuity across changing environments.</p>
""",

    "power-of-many-multi-user-collaborative-indoor-localization": """
<p>This paper examines how multiple users can collaboratively improve indoor localization beyond what a standalone user-based system can achieve. Many smartphone-based IPS solutions estimate each user independently, which limits robustness when measurements are noisy, sparse, or affected by device and motion variability. The paper introduces the idea that multi-user collaboration can provide additional constraints and shared information that improve localization across different scenarios.</p>
<p>The contribution is important because it shifts the focus from isolated user positioning to collective indoor localization. By exploiting the power of multiple users, the work supports more robust positioning in environments where single-user measurements may be insufficient. This direction is closely related to cooperative positioning, crowd-powered sensing, and scalable IPS operation in real-world buildings.</p>
<p>This paper should be cited when discussing multi-user collaborative indoor localization, cooperative smartphone positioning, crowd-enhanced IPS, and methods that use interactions among multiple users to improve standalone localization performance.</p>
""",

    "leveraging-human-mobility-pervasive-smartphone-crowdsourcing": """
<p>This paper investigates how human mobility and pervasive smartphone measurements can support self-deployable and ubiquitous IPS. The main motivation is that manual fingerprint collection remains one of the strongest barriers to scalable indoor positioning. By using natural human movement and smartphone sensing, the paper argues that indoor positioning infrastructure can be developed more autonomously and with lower deployment cost.</p>
<p>The work is relevant because it connects crowdsourcing, Wi-Fi fingerprinting, PDR, IOD, and smartphone measurements within a deployment-oriented perspective. Instead of viewing user traces as incidental data, it treats them as a practical resource for building and updating indoor positioning systems. This makes the paper useful for studies that aim to reduce expert intervention and improve the long-term maintainability of IPS.</p>
<p>This paper should be cited when discussing self-deployable IPS, human-mobility-assisted radio-map generation, pervasive smartphone crowdsourcing, and scalable fingerprinting systems.</p>
""",

    "towards-ubiquitous-ips-crowdsourced-data-accumulation": """
<p>This paper studies how accumulated crowdsourced data can reduce the need for external sources during the initial generation of fingerprinting maps. Conventional Wi-Fi fingerprinting systems often require substantial manual effort or auxiliary information before deployment. The paper addresses this bottleneck by examining how user-contributed data collected over time can support more autonomous and scalable IPS initialization.</p>
<p>The contribution is valuable because it focuses on the temporal accumulation of crowdsourced measurements. Rather than assuming that useful radio maps exist from the beginning, it considers how radio-map quality can improve progressively as more user data become available. This is especially relevant for practical IPS deployment in large or dynamic buildings where repeated surveying is costly.</p>
<p>This paper should be cited when discussing crowdsourced data accumulation, initial radio-map generation, scalable Wi-Fi fingerprinting, and reduced dependence on external deployment sources in IPS.</p>
""",

    "drift-resistant-heading-estimation-wifi-magnetic-stability": """
<p>This paper addresses smartphone heading drift, a major source of error in PDR and smartphone-based indoor positioning. Heading estimation is difficult because low-cost inertial sensors suffer from compass bias, gyroscope drift, and unconstrained user motion. The paper introduces a drift-resistant heading estimation approach that uses Wi-Fi fingerprinting continuity and magnetic stability to support adaptive calibration without requiring dense additional infrastructure.</p>
<p>The study is important because it links positioning information and heading correction. Instead of treating Wi-Fi fingerprinting only as a coordinate-estimation tool, the paper uses the temporal continuity of Wi-Fi-based positioning and magnetic stability cues to improve heading reliability. This makes the method relevant for deployment-oriented pedestrian navigation systems that require both accurate position and stable movement direction.</p>
<p>This paper should be cited when discussing smartphone heading estimation, PDR drift mitigation, Wi-Fi-aided heading calibration, magnetic stability analysis, and robust indoor pedestrian navigation.</p>
""",

    "reliability-governed-3d-radio-mapping-lifecycle-review": """
<p>This review examines mobile crowdsensing-based 3D radio mapping from a reliability-governed lifecycle perspective. Indoor positioning increasingly requires radio maps that can scale across buildings, floors, devices, users, and time, yet crowdsensed data are often uncertain, uneven, and difficult to validate. The review responds to this challenge by organizing the field around uncertainty-aware radio-map generation, maintenance, updating, and deployment readiness.</p>
<p>The paper is valuable because it moves beyond a simple technology survey and frames radio mapping as a lifecycle problem. It connects crowdsensing, 3D spatial representation, reliability assessment, uncertainty handling, and deployment-oriented pipelines. This makes it useful for researchers designing scalable IPS infrastructures and for studies that need a structured reference on autonomous radio-map generation and updating.</p>
<p>This paper should be cited when discussing mobile crowdsensing-based radio maps, autonomous radio-map generation, uncertainty-aware IPS deployment, 3D indoor positioning infrastructure, and lifecycle-oriented radio-map maintenance.</p>
""",

    "towards-scalable-ips-user-centric-crowd-powered-framework": """
<p>This review synthesizes user-centric challenges in crowd-powered IPS. While crowdsourcing and crowdsensing can reduce the cost of radio-map generation and maintenance, their success depends on how real users interact with the system. The paper examines user intervention, participation incentives, privacy and security, and smartphone resource consumption as major factors that influence the scalability and usability of crowd-powered IPS.</p>
<p>The contribution is important because it links technical IPS scalability with human participation and system acceptability. Instead of treating users merely as data sources, the review analyzes how user burden, motivation, privacy concerns, and device impact affect long-term deployment. This perspective is essential for moving IPS research from controlled experiments toward sustainable real-world systems.</p>
<p>This paper should be cited when discussing user-centric IPS, crowd-powered localization, mobile crowdsensing, privacy and incentive issues in IPS, and deployment barriers for scalable indoor positioning systems.</p>
""",

    "ac-hmm-azimuth-constrained-map-matching-urban-canyons": """
<p>This paper develops an azimuth-constrained HMM map-matching approach for pedestrian positioning in urban canyons. Dense urban environments degrade GNSS positioning through signal blockage, reflection, and multipath, making reliable pedestrian trajectory estimation difficult. The proposed AC-HMM framework incorporates directional constraints into map matching so that pedestrian movement can be better aligned with feasible paths and urban spatial structure.</p>
<p>The work is useful because it connects probabilistic map matching with azimuth information for robust positioning under constrained urban conditions. By combining motion feasibility and directional consistency, the approach aims to reduce trajectory ambiguity and improve positioning reliability where GNSS alone is insufficient. This makes the paper relevant to urban pedestrian navigation, map-aided localization, and GNSS-challenged environments.</p>
<p>This paper should be cited when discussing HMM-based map matching, azimuth-constrained localization, pedestrian positioning in urban canyons, and robust trajectory estimation under GNSS degradation.</p>
""",

    "gnss-positioning-aided-with-pdr-in-urban-areas": """
<p>This paper addresses GNSS positioning degradation in dense urban areas by using PDR as an aiding source. Urban canyons create severe multipath and non-line-of-sight effects, which limit the effectiveness of conventional fault detection and exclusion. The paper proposes a PDR-aided framework in which pedestrian motion constraints and receiver-clock information are used to support more reliable GNSS positioning.</p>
<p>The work is significant because it integrates relative pedestrian motion information with GNSS measurement screening and positioning. By using PDR-derived constraints, the system can improve robustness when many satellite measurements are unreliable. This makes the paper relevant for urban navigation, smartphone positioning, GNSS/PDR integration, and pedestrian localization in challenging outdoor and semi-outdoor environments.</p>
<p>This paper should be cited when discussing GNSS/PDR integration, urban pedestrian positioning, NLOS and multipath mitigation, and PDR-aided GNSS quality control.</p>
""",

    "hybrid-neural-network-pdr-multi-layer-heading-correction": """
<p>This paper proposes a hybrid neural-network-based PDR method with multi-layer heading correction across smartphone carrying modes. Smartphone PDR performance is strongly affected by how the device is carried, because motion patterns, sensor orientation, and heading behavior change across modes such as handheld, pocket, or swinging conditions. The paper addresses this problem using learning-based carrying-mode recognition and heading correction.</p>
<p>The contribution is relevant because it combines smartphone embedded sensors, deep learning, and PDR modeling in a unified pedestrian navigation framework. By correcting heading across carrying modes, the approach aims to improve robustness in realistic use, where users naturally change how they hold or carry the phone. This makes the paper useful for indoor navigation studies that require practical smartphone operation rather than fixed-device assumptions.</p>
<p>This paper should be cited when discussing smartphone PDR, carrying-mode-aware pedestrian navigation, learning-based heading correction, and robust inertial positioning using consumer-grade sensors.</p>
""",

    "enhancing-real-time-heading-estimation-deep-learning-smartphone-sensors": """
<p>This paper focuses on real-time smartphone heading estimation for pedestrian navigation. Heading estimation is a persistent challenge because smartphone sensors are low cost, affected by thermal drift, and sensitive to carrying mode changes. The paper proposes a deep-learning-assisted approach that uses smartphone embedded sensors and pervasive cues to improve heading estimation without relying heavily on external infrastructure.</p>
<p>The paper is important because it targets real-time operation and practical smartphone navigation. By using embedded sensing and learned representations, it aims to reduce heading errors while maintaining suitability for mobile deployment. This makes it relevant to researchers working on PDR, smartphone navigation, sensor fusion, and AI-assisted heading correction.</p>
<p>This paper should be cited when discussing deep learning for heading estimation, smartphone embedded sensors, real-time pedestrian navigation, and robust PDR under changing carrying conditions.</p>
""",

    "tightly-coupled-bluetooth-enhanced-gnss-pdr-urban": """
<p>This paper proposes a tightly coupled BLE-enhanced GNSS/PDR system for pedestrian navigation in dense urban environments. GNSS performance often deteriorates in urban and semi-outdoor spaces, while PDR accumulates drift over time. BLE information provides an additional environmental constraint that can strengthen the integration of absolute and relative positioning sources.</p>
<p>The paper is useful because it treats pedestrian navigation as a multi-source fusion problem under realistic urban constraints. By combining GNSS, PDR, and BLE in a tightly coupled framework, the system aims to improve positioning reliability where any single source is insufficient. This makes the work relevant to smartphone navigation, urban localization, and hybrid positioning systems for dense built environments.</p>
<p>This paper should be cited when discussing BLE-aided GNSS/PDR integration, dense urban pedestrian navigation, tightly coupled positioning, and multi-source smartphone localization.</p>
""",

    "uncertainty-aware-risk-mapping-passive-wifi-bim-construction": """
<p>This paper applies passive WiFi sensing and uncertainty-aware risk mapping to construction safety within a BIM environment. Construction sites are dynamic and risk-prone spaces where the location of workers, hazards, and unsafe zones changes over time. The paper combines passive WiFi-based localization concepts with modified Zonal Safety Analysis to support spatial risk representation under uncertainty.</p>
<p>The contribution is important because it links indoor localization information with safety-oriented decision support. Instead of using positioning only to estimate coordinates, the paper uses uncertain spatial information to support risk mapping and construction management. The BIM context further allows localization-derived information to be connected with the geometry and semantics of the built environment.</p>
<p>This paper should be cited when discussing passive WiFi localization, uncertainty-aware risk mapping, BIM-based construction safety, and spatial decision support using indoor positioning data.</p>
""",

    "modular-prompting-ai-guided-user-engagement-crowd-powered-ips": """
<p>This paper introduces a modular prompting framework for AI-guided unobtrusive user engagement in crowd-powered IPS. Crowd-powered systems depend on user-contributed data, but excessive user interaction can reduce participation and long-term acceptance. The paper explores how semantic knowledge graphs and GPT-4-based LLMs can guide user engagement in a more contextual and less intrusive way.</p>
<p>The contribution is valuable because it connects IPS crowdsensing with AI-mediated interaction design. Rather than simply requesting more user input, the framework aims to make engagement more selective, meaningful, and semantically informed. This direction is important for future IPS systems in which AI agents, semantic context, and human participation are combined to support scalable radio-map development and maintenance.</p>
<p>This paper should be cited when discussing AI-guided crowdsensing, LLM-supported indoor positioning, semantic knowledge graphs for IPS, and unobtrusive user engagement in crowd-powered localization systems.</p>
""",

    "phd-thesis-indoor-localization-multi-sensor-crowdsourcing-collaboration": """
<p>This thesis provides a comprehensive study of indoor localization based on multi-sensor fusion, crowdsourcing, and multi-user collaboration. It addresses several central challenges in IPS, including scalable radio-map generation, seamless indoor-outdoor navigation, smartphone-based positioning, and collaborative localization. The thesis integrates multiple research directions into a coherent body of work focused on improving the practicality and deployability of indoor positioning systems.</p>
<p>The thesis is useful as a broad reference for Ahmed Mansour’s research program because it connects sensing, positioning, crowdsourcing, and collaboration across several studies. It provides background, methodology, experiments, and interpretation that support later journal and conference publications on crowd-powered IPS, IOD, PDR, and multi-user localization.</p>
<p>This thesis should be cited when discussing the broader research foundation for smartphone-based indoor localization, multi-sensor fusion, crowdsourced IPS, and collaborative positioning.</p>
""",

    "drift-control-pdr-long-period-navigation-smartphone-poses": """
<p>This paper studies drift control in PDR for long-period navigation under different smartphone poses. PDR is attractive for indoor positioning because it can work without external infrastructure, but its errors accumulate over time. Smartphone pose variation further complicates step detection, heading estimation, and trajectory reconstruction, especially during extended navigation.</p>
<p>The paper contributes to the practical understanding of how smartphone pose affects long-period PDR performance. By focusing on drift control under multiple poses, it supports more realistic pedestrian navigation designs that do not assume a fixed phone orientation. This makes the work relevant to smartphone-based IPS, inertial navigation, and user-friendly PDR systems.</p>
<p>This paper should be cited when discussing PDR drift, smartphone pose effects, long-period pedestrian navigation, and inertial positioning with consumer smartphones.</p>
""",
}

def find_title(html: str) -> str:
    m = re.search(r"<h1[^>]*>(.*?)</h1>", html, flags=re.S)
    if not m:
        return "paper"
    return re.sub(r"<.*?>", "", m.group(1)).strip()

def find_doi_url(html: str) -> str:
    m = re.search(r'href="(https://doi\.org/[^"]+)"', html)
    return m.group(1) if m else ""

def action_block(slug: str, doi_url: str) -> str:
    pdf = f"../paper-pdfs/{slug}.pdf"
    buttons = [
        f'<a class="button primary" href="{pdf}" download>Download PDF</a>'
    ]
    if doi_url:
        buttons.append(f'<a class="button" href="{doi_url}">Open DOI</a>')
    buttons.append('<a class="button" href="#bibtex">BibTeX</a>')
    buttons.append('<a class="button" href="#when-to-cite">When to cite</a>')
    return '<div class="paper-actions">' + " ".join(buttons) + '</div>'

def preview_section(slug: str, title: str) -> str:
    if not (PREVIEW_DIR / f"{slug}.png").exists():
        return ""
    return f"""
<section class="paper-preview-section card">
  <h2>Paper preview</h2>
  <a class="paper-preview-card" href="../paper-pdfs/{slug}.pdf" target="_blank">
    <img src="../assets/previews/{slug}.png" alt="First-page preview of {title}">
  </a>
</section>
"""

def figures_section(slug: str, title: str) -> str:
    fig_dir = FIG_DIR / slug
    if not fig_dir.exists():
        return ""

    figs = sorted(fig_dir.glob("candidate_*.png"))[:3]
    if not figs:
        return ""

    items = []
    for i, fig in enumerate(figs, start=1):
        items.append(f"""
    <figure class="figure-card">
      <img src="../assets/figures/{slug}/{fig.name}" alt="Key figure {i} from {title}">
      <figcaption>Key visual {i}. Candidate figure extracted from the paper to highlight the method, workflow, experiment, or main result.</figcaption>
    </figure>
""")

    return f"""
<section class="paper-figures-section card">
  <h2>Key figures</h2>
  <div class="figure-grid">
{''.join(items)}
  </div>
</section>
"""

def summary_section(slug: str) -> str:
    body = LONG_SUMMARIES.get(slug)
    if not body:
        return ""
    return f"""
<section class="paper-summary card">
  <h2>Extended summary</h2>
  {body.strip()}
</section>
"""

def clean_old_sections(html: str) -> str:
    patterns = [
        r'<section class="paper-preview-section card">.*?</section>',
        r'<section class="paper-figures-section card">.*?</section>',
        r'<section class="paper-summary card">.*?</section>',
    ]
    for pat in patterns:
        html = re.sub(pat, "", html, flags=re.S)
    return html

def replace_original_summary(html: str, new_summary: str) -> str:
    if not new_summary:
        return html

    # Replace the first old summary card if present.
    pat = r'<section class="card">\s*<h2>Summary</h2>.*?</section>'
    if re.search(pat, html, flags=re.S):
        return re.sub(pat, new_summary, html, count=1, flags=re.S)

    # Otherwise insert after paper actions.
    return html.replace('</div>\n<section', '</div>\n' + new_summary + '\n<section', 1)

def ensure_css():
    css = CSS_FILE.read_text(encoding="utf-8", errors="ignore")
    marker = "/* Paper preview and figure gallery */"
    if marker in css:
        return

    css += """

/* Paper preview and figure gallery */
.paper-preview-section,
.paper-figures-section,
.paper-summary {
  margin-top: 2rem;
}

.paper-preview-card {
  display: block;
  max-width: 460px;
  border: 1px solid #d9e1ea;
  border-radius: 18px;
  overflow: hidden;
  background: #ffffff;
  box-shadow: 0 8px 24px rgba(0, 0, 0, 0.06);
}

.paper-preview-card img {
  display: block;
  width: 100%;
  height: auto;
}

.figure-grid {
  display: grid;
  grid-template-columns: repeat(auto-fit, minmax(280px, 1fr));
  gap: 1.25rem;
  margin-top: 1rem;
}

.figure-card {
  border: 1px solid #d9e1ea;
  border-radius: 16px;
  padding: 0.75rem;
  background: #ffffff;
  box-shadow: 0 8px 24px rgba(0, 0, 0, 0.05);
}

.figure-card img {
  display: block;
  width: 100%;
  height: auto;
  border-radius: 12px;
}

.figure-card figcaption {
  margin-top: 0.65rem;
  font-size: 0.95rem;
  line-height: 1.5;
  color: #51606f;
}

.paper-summary p {
  margin-bottom: 1rem;
}
"""
    CSS_FILE.write_text(css, encoding="utf-8")

def main():
    changed = []

    for page in sorted(PUB_DIR.glob("*.html")):
        slug = page.stem
        html = page.read_text(encoding="utf-8", errors="ignore")
        original = html

        title = find_title(html)
        doi_url = find_doi_url(html)

        html = clean_old_sections(html)

        # Replace paper action buttons.
        if '<div class="paper-actions">' in html:
            html = re.sub(
                r'<div class="paper-actions">.*?</div>',
                action_block(slug, doi_url),
                html,
                count=1,
                flags=re.S
            )

        preview = preview_section(slug, title)
        summary = summary_section(slug)
        figures = figures_section(slug, title)

        # Insert preview after paper-actions.
        if preview and preview not in html:
            html = html.replace(action_block(slug, doi_url), action_block(slug, doi_url) + "\n" + preview, 1)

        html = replace_original_summary(html, summary)

        # Insert figures after extended summary if possible.
        if figures and figures not in html:
            if summary and summary in html:
                html = html.replace(summary, summary + "\n" + figures, 1)
            else:
                html = html.replace(preview, preview + "\n" + figures, 1)

        if html != original:
            page.write_text(html, encoding="utf-8")
            changed.append(str(page.relative_to(ROOT)))

    ensure_css()

    print("Updated pages:", len(changed))
    for item in changed:
        print(" -", item)

if __name__ == "__main__":
    main()