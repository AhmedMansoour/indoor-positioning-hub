from pathlib import Path
import re

ROOT = Path(".")
INDEX = ROOT / "index.html"
LLMS = ROOT / "llms.txt"

if not INDEX.exists():
    raise SystemExit("index.html not found. Run this from the repository root.")

html = INDEX.read_text(encoding="utf-8", errors="ignore")

replacements = {
    "Indoor Positioning Hub by Ahmed Mansour, Ph.D., with publications, PDFs, citation resources, datasets, code links, visual research atlas, and definitions of indoor positioning, indoor localization, and indoor navigation.":
    "Indoor Positioning Hub by Ahmed Mansour, Ph.D., bringing together publications, PDFs, citation resources, research areas, visual explanations, and reusable materials on indoor positioning, indoor localization, indoor navigation, Wi-Fi fingerprinting, PDR, mobile crowdsensing, and seamless spatial intelligence.",

    "Indoor positioning, localization, navigation, and spatial intelligence for smart built environments.":
    "Indoor positioning, localization, navigation, and spatial intelligence for complex indoor and urban spaces.",

    "This website brings together my academic profile, publication portfolio, downloadable papers, citation resources, datasets, code links, and visual research maps. The research connects smartphone sensing, Wi-Fi fingerprinting, pedestrian dead reckoning, mobile crowdsensing, autonomous radio mapping, indoor-outdoor awareness, and deployment-ready indoor spatial intelligence.":
    "This site brings together my publications, downloadable papers, citation resources, visual explanations, and reusable research materials. The work addresses a central problem in indoor positioning: how to keep location, motion, floor, and context reliable when signals are unstable, users move naturally, and environments change over time.",

    "Researcher in geomatics, indoor localization, smartphone sensing, crowdsensing-based IPS, PDR, radio-map maintenance, and smart built-environment positioning.":
    "Researcher in geomatics, indoor localization, smartphone sensing, PDR, Wi-Fi fingerprinting, mobile crowdsensing, radio-map generation, and seamless indoor-outdoor positioning.",

    "Ph.D. research training and postdoctoral work in geomatics, sensor fusion, indoor positioning, and smart built environments.":
    "Ph.D. research training and postdoctoral work in geomatics, sensor fusion, indoor positioning, and smartphone-based navigation.",

    "Civil engineering, public works, geomatics, surveying, and foundational engineering background.":
    "Civil engineering, public works, geomatics, surveying, and engineering foundations for spatial measurement.",

    "Field guide":
    "Foundational concepts",

    "What are indoor positioning, indoor localization, and indoor navigation?":
    "Indoor positioning, indoor localization, and indoor navigation",

    "These terms are related, but each describes a different layer of the indoor spatial-information pipeline. The distinction helps readers move from measurements to estimated locations, routes, services, and operational decisions inside buildings where satellite positioning is weak or unavailable.":
    "These terms are often used together, but they do not describe the same task. Indoor positioning estimates where a person, phone, robot, or asset is. Indoor localization relates that estimate to a meaningful indoor reference, such as a floor, room, corridor, or zone. Indoor navigation uses this information to guide movement and support location-aware services where GNSS is weak, unreliable, or unavailable.",

    "Indoor positioning estimates the position of a person, smartphone, robot, asset, or sensor inside a building using radio signals, inertial sensors, maps, vision, magnetic fields, barometers, or fused measurements.":
    "Indoor positioning estimates the location of a person, smartphone, robot, asset, or sensor using measurements such as Wi-Fi, BLE, inertial sensors, magnetic fields, barometers, maps, vision, or fused observations.",

    "Indoor localization determines where the user or object is within an indoor reference frame, such as a coordinate, floor, room, corridor, zone, landmark, or building-level map representation.":
    "Indoor localization interprets the estimated position inside an indoor reference frame. The output may be a coordinate, floor, room, corridor, zone, landmark, or map-based location that is meaningful to the user or service.",

    "Indoor navigation uses position, heading, motion state, route information, and spatial context to guide movement, support wayfinding, enable location-aware services, and connect positioning outputs to decisions.":
    "Indoor navigation turns positioning and localization outputs into guidance. It combines position, heading, motion state, route information, map constraints, and spatial context to support wayfinding and service decisions.",

    "Academic profile":
    "Research focus",

    "The hub is organized to help readers move from a research question to the relevant paper, method, dataset, figure, or citation entry. The work connects smartphone sensing, radio signals, human mobility, map information, and deployment constraints into practical positioning systems for buildings, campuses, cities, and smart built environments.":
    "My research asks how indoor positioning can remain usable outside controlled experiments. The work connects smartphone sensing, radio signals, human mobility, map information, and deployment constraints so that positioning systems can support buildings, campuses, transport spaces, and dense urban areas.",

    "Research Themes and Visual Research Atlas":
    "Research map and visual overview",

    "A thematic map of Ahmed Mansour's work across indoor positioning research, engineering, and deployment.":
    "A concise map of the research program across sensing, radio mapping, fusion, 3D context, and deployment.",

    "The atlas links core papers, system concepts, and visual explanations across sensing, inference, mapping, crowdsensing, pedestrian navigation, and deployment readiness.":
    "The map links papers and concepts across smartphone sensing, Wi-Fi fingerprinting, radio-map generation, pedestrian navigation, indoor-outdoor continuity, and multi-floor spatial context.",

    "Smart indoor positioning in real buildings":
    "Indoor positioning in real operating spaces",

    "Indoor positioning systems must work in complex spaces with changing signals, moving users, multiple floors, and limited user attention. This direction connects research outputs to operational indoor services.":
    "Indoor positioning must work where people actually move: through corridors, entrances, elevators, lobbies, floors, and crowded service areas. This direction connects positioning algorithms to practical indoor services.",

    "Signals, sensors, maps, and context":
    "Signals, sensors, maps, and spatial context",

    "Research themes include Wi-Fi fingerprinting, PDR, sensor fusion, indoor-outdoor detection, radio-map maintenance, and context-aware positioning pipelines.":
    "The research combines Wi-Fi fingerprints, inertial sensing, GNSS/PDR integration, barometer readings, maps, floor information, and reliability checks to keep positioning outputs meaningful.",

    "Explore research themes":
    "Open research areas",

    "Core directions":
    "Main research directions",

    "Spatial intelligence for smart built environments":
    "Indoor spatial intelligence and deployment",

    "Find papers, PDFs, citation records, and visual explanations":
    "Find papers, PDFs, metadata, and citation guidance",

    "Each publication page is designed for fast reading and reuse, with first-page previews, PDF access where available, DOI metadata, BibTeX, when-to-cite guidance, long research-story summaries, and selected visual explanations.":
    "Each publication page gives a structured entry point to the work: paper title, venue, DOI, PDF access where permitted, citation metadata, short research context, and links back to the relevant research area.",

    "Shared resources, reproducibility links, and supporting research materials.":
    "PDFs, metadata files, reproducibility notes, and responsible sharing information.",

    "Academic background, research focus, and contact links.":
    "Academic profile, research identity, identifiers, CV, and contact links.",

    "Home · Key thematic pathways across the hub":
    "Research program",

    "Research areas across the hub":
    "Research areas across the Indoor Positioning Hub",

    "Indoor positioning is not a single sensing problem. It is a set of connected challenges: preserving motion continuity, controlling drift, handling user behavior, maintaining spatial references, and linking relative motion to absolute indoor location.":
    "Indoor positioning is a connected research problem. It requires motion continuity, drift control, robust radio references, floor awareness, reliable transitions between outdoor and indoor spaces, and careful interpretation of what a location estimate means in a real building.",

    "Infrastructure-free positioning":
    "Infrastructure-free motion sensing",

    "Smartphone inertial sensing is the most available motion source in pedestrian navigation. It requires no installed anchors, no prior radio visibility, and no dedicated infrastructure. Its value is strongest when other positioning cues become weak or unavailable: it can carry motion through GNSS outages, sparse Wi-Fi RSS or BLE coverage, temporary map-matching ambiguity, and interruptions in LiDAR or image-based localization.":
    "Smartphone inertial sensing is the most widely available source of pedestrian motion. It works without installed anchors, prior radio coverage, or a prepared indoor map, which makes it valuable when GNSS is blocked, Wi-Fi or BLE coverage is sparse, and visual or LiDAR-based cues are unavailable.",

    "In this role, inertial positioning is not only a standalone method. It is the relative-motion backbone that keeps the trajectory alive between absolute updates from external or environmental cues.":
    "Its strongest role is not as an isolated positioning method, but as the motion backbone of a hybrid system. PDR carries the trajectory between more reliable updates from GNSS, Wi-Fi, BLE, maps, vision, or other environmental cues.",

    "Accurate position and heading initialization are required when PDR is expected to provide absolute positioning, because an initial offset shifts the whole trajectory.":
    "Initialization matters: an incorrect starting position or heading shifts the entire trajectory.",

    "The phone frame must be related to the pedestrian body frame; otherwise, a correct sensor measurement can point in the wrong walking direction.":
    "The phone frame must be related to the pedestrian body frame, especially when users hold, swing, call, or pocket the device.",

    "Heading drift is the dominant long-term error source, as small gyroscope biases gradually integrate into large orientation errors.":
    "Small gyroscope biases accumulate over time and can turn a locally smooth path into a globally wrong trajectory.",

    "Magnetometer heading can provide absolute direction, but it is easily disturbed by steel structures, elevators, electronics, reinforced concrete, and local magnetic anomalies.":
    "Magnetometer updates can help, but indoor magnetic fields are often distorted by steel, elevators, electronics, reinforced concrete, and local anomalies.",

    "Carrying modes such as holding, calling, swinging, and in-pocket use change the sensor pattern and weaken fixed assumptions about step events, stride length, and walking direction.":
    "Carrying modes change the motion signal, so fixed assumptions about steps, stride length, and walking direction are rarely sufficient.",

    "Standalone inertial propagation needs periodic correction from GNSS, Wi-Fi, BLE, map constraints, vision, or other trusted observations to prevent long-term divergence.":
    "Long-term use requires correction from trusted observations such as GNSS, Wi-Fi, BLE, maps, vision, or landmarks.",

    "Wi-Fi fingerprinting provides the absolute indoor reference that inertial positioning cannot maintain by itself. A fingerprint links a wireless observation to a physical indoor location, making it useful for correcting PDR drift, recognizing floors, initializing trajectories, and supporting building-scale indoor services where GNSS is unavailable.":
    "Wi-Fi fingerprinting gives indoor positioning a practical reference frame. A fingerprint links a wireless observation to a physical location, which helps correct PDR drift, initialize trajectories, recognize floors, and support building-scale services where GNSS cannot be trusted.",

    "The central challenge is no longer only how to match an RSS vector to a point. The harder deployment question is how to generate, update, and trust radio maps when the data arrive from ordinary mobile sessions rather than controlled survey campaigns.":
    "The key deployment challenge is not only matching an RSS vector to a point. It is building and maintaining radio maps when the measurements come from ordinary mobile sessions, with irregular motion, changing devices, and imperfect spatial labels.",

    "Manual radio-map surveying is costly because each building, floor, corridor, and reference point requires repeated measurement when the site or wireless infrastructure changes.":
    "Manual surveys do not scale well because each building, floor, corridor, and reference point may require repeated measurements after layout or access-point changes.",

    "Crowdsourced measurements are irregular because real users move freely, stop, turn, change floors, carry phones differently, and do not follow predefined survey paths.":
    "Mobile sessions are irregular: users stop, turn, change floors, hold phones differently, and rarely follow predefined survey paths.",

    "RSS observations are unstable across devices, time, human blockage, furniture layout, access-point configuration, and routine environmental dynamics.":
    "RSS values vary across devices, time, body blockage, furniture layout, access-point settings, and routine indoor activity.",

    "Multifloor positioning requires vertical interpretation from barometer, motion state, building topology, and wireless evidence rather than horizontal fingerprint matching alone.":
    "Multi-floor positioning needs vertical evidence from barometers, motion events, building topology, and wireless patterns, not only horizontal fingerprint matching.",

    "Session logs must align Wi-Fi scans, IMU samples, magnetometer readings, barometer pressure, GNSS fixes, and app events into one coherent spatial record.":
    "Useful sessions must align Wi-Fi scans, IMU samples, magnetometer readings, barometer pressure, GNSS fixes, and app events into one spatial record.",

    "Radio-map updating must be reliability-governed, because blindly writing noisy or wrongly localized fingerprints can degrade the map instead of improving it.":
    "Map updates need reliability control, because noisy or wrongly localized fingerprints can damage the reference map instead of improving it.",

    "Indoor positioning should not break at the building entrance. Real users move through streets, entrances, semi-open spaces, corridors, elevators, staircases, lobbies, and indoor rooms, while the available positioning sources change continuously.":
    "Positioning should not fail at the building entrance. Real users move across streets, entrances, canopies, lobbies, corridors, elevators, staircases, and rooms while the useful sensing sources change continuously.",

    "GNSS provides an outdoor absolute reference, but it degrades near dense buildings and often fails indoors. Inertial positioning preserves motion continuity during signal outages, while Wi-Fi, BLE, barometer readings, map constraints, and indoor–outdoor awareness provide correction and context. This research area connects the relative-motion layer from inertial positioning with the absolute indoor reference from radio mapping to maintain a continuous trajectory across outdoor, transition, and indoor spaces.":
    "GNSS provides outdoor reference information, but it degrades near buildings and usually fails indoors. Inertial positioning preserves motion during outages, while Wi-Fi, BLE, barometer readings, map constraints, and indoor-outdoor awareness provide correction and context. The goal is a continuous trajectory across outdoor, transition, and indoor spaces.",

    "GNSS degradation near buildings can introduce large position errors before the user reaches an indoor entrance.":
    "GNSS can become unreliable before the user actually enters the building.",

    "Indoor–outdoor transition is gradual, because covered entrances, semi-open spaces, lobbies, and corridors create mixed signal conditions.":
    "The transition is gradual: covered entrances, semi-open spaces, lobbies, and corridors often produce mixed signal conditions.",

    "Sensor availability changes along the trajectory, since GNSS, Wi-Fi, BLE, IMU, barometer, and map constraints become useful at different moments.":
    "GNSS, Wi-Fi, BLE, IMU, barometer, and map constraints become useful at different parts of the route.",

    "Fusion must judge source reliability, because a strong measurement is not always a trustworthy positioning cue.":
    "Fusion must judge reliability, because a strong signal is not always a trustworthy positioning cue.",

    "Vertical movement requires explicit handling when users pass through stairs, elevators, ramps, and multi-level indoor spaces.":
    "Stairs, elevators, ramps, and multi-level spaces require explicit vertical-motion handling.",

    "Seamless navigation requires transition awareness and source switching logic, not only point-by-point localization accuracy.":
    "Seamless navigation depends on transition awareness and source-switching logic, not only point-by-point accuracy.",

    "Indoor positioning becomes operational only when the system understands the building as a multi-level spatial structure. A correct horizontal estimate is not enough in a multi-floor environment, because the same x–y location may correspond to different rooms, corridors, activities, or services on different floors.":
    "Indoor positioning becomes useful at scale only when it understands the building as a multi-level spatial structure. A correct horizontal coordinate is not enough, because the same plan location may correspond to different rooms, corridors, services, and activities on different floors.",

    "This research area addresses 3D radio-map generation from mobile crowdsensing. The aim is to convert ordinary walking sessions into floor-local map skeletons, assemble them into a building-level 3D representation, and refine the structure using reliable anchors such as gates, payment terminals, Wi-Fi access points, vertical transitions, and spatial constraints. The result is not only a set of fingerprints, but a 3D indoor spatial reference that supports floor recognition, vertical positioning, and deployment-ready localization.":
    "This area examines how ordinary mobile sessions can be converted into floor-local map skeletons, assembled into a building-level 3D representation, and refined using stable anchors, vertical transitions, and spatial constraints. The outcome is not only a set of fingerprints, but a floor-aware indoor reference for localization and navigation.",

    "Floor-local traces must be reconstructed from noisy mobile sessions before they can be used as reliable spatial skeletons.":
    "Noisy mobile traces must be reconstructed before they can serve as reliable floor-local skeletons.",

    "Vertical positioning requires more than height-change detection; it must connect barometer trends, motion events, stairs, elevators, ramps, and building topology.":
    "Vertical positioning must connect barometer trends, motion events, stairs, elevators, ramps, and building topology.",

    "Floor recognition is difficult when Wi-Fi and BLE signals leak across floors, especially near atriums, stairwells, open shafts, and dense access-point layouts.":
    "Wi-Fi and BLE signals often leak across floors, especially near atriums, stairwells, open shafts, and dense access-point layouts.",

    "Building-level 3D assembly must align separate floor skeletons into one consistent spatial structure instead of treating each floor as an isolated map.":
    "Building-level assembly must align floor skeletons into one consistent spatial structure.",

    "Anchor objects and stable signal landmarks are needed to reduce accumulated distortion and connect the generated structure to real building coordinates.":
    "Stable anchors and signal landmarks help reduce distortion and connect the generated structure to real building coordinates.",

    "Global refinement must correct local errors while preserving floor connectivity, vertical transitions, and the physical constraints of the indoor environment.":
    "Global refinement must correct local errors while preserving floor connectivity, vertical transitions, and physical constraints.",

    "This visual index keeps the gallery concise: the 2D navigation illustration is removed, the 3D indoor figure is enlarged, and the autonomous radio-map and indoor-outdoor demonstrations are shown as live GIFs.":
    "These visuals offer a quick conceptual entry into the research program: future spatial intelligence, multi-floor indoor positioning, autonomous radio-map generation, and seamless indoor-outdoor positioning.",

    "A high-level view of positioning as part of connected urban, indoor, and multi-level navigation services.":
    "A future-facing view of positioning as a layer that connects outdoor movement, indoor navigation, multi-level spaces, and location-aware services.",

    "An enlarged figure that highlights floor recognition, vertical movement, and multi-level indoor geometry.":
    "A multi-level indoor scene that emphasizes floor recognition, vertical movement, escalators, and floor-aware navigation.",

    "The original live GIF now runs directly on the site, preserving the workflow animation.":
    "A live workflow showing how crowdsensed signatures can support autonomous map generation and online positioning.",

    "The original live GIF shows indoor-outdoor awareness, floor detection, and transition-aware positioning.":
    "A live demonstration of indoor-outdoor awareness, floor detection, and continuous positioning across changing spaces."
}

count = 0
for old_text, new_text in replacements.items():
    if old_text in html:
        html = html.replace(old_text, new_text)
        count += 1

html = html.replace("Research Themes</a>", "Research Areas</a>")
html = html.replace("Datasets &amp; Code</a>", "Resources</a>")
html = html.replace("smart built environments", "complex indoor and urban spaces")
html = html.replace("smart built-environment positioning", "indoor spatial positioning")
html = html.replace("Indoor–outdoor transition", "Indoor-outdoor transition")

INDEX.write_text(html, encoding="utf-8")

if LLMS.exists():
    llms = LLMS.read_text(encoding="utf-8", errors="ignore")
    add = """
## Homepage copy refinement

- Homepage: https://ahmedmansoour.github.io/indoor-positioning-hub/index.html
- Update: homepage copy refined to remove process-oriented update wording, reduce repetitive mechanical phrasing, and present the research program in clearer academic website language.
"""
    if "## Homepage copy refinement" not in llms:
        marker = "## Visual research gallery"
        llms = llms.replace(marker, add + "\\n" + marker) if marker in llms else llms.rstrip() + "\\n" + add + "\\n"
        LLMS.write_text(llms, encoding="utf-8")

print(f"Done: refined homepage text. Replacements applied: {count}.")
