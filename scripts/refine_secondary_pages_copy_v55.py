from pathlib import Path
import re

ROOT = Path('.')
PAGES = {
    'about': ROOT / 'about.html',
    'citation': ROOT / 'citation-resources.html',
    'cv': ROOT / 'cv.html',
    'publications': ROOT / 'publications.html',
    'research': ROOT / 'research-themes.html',
    'resources': ROOT / 'resources.html',
}
LLMS = ROOT / 'llms.txt'

missing = [str(path) for path in PAGES.values() if not path.exists()]
if missing:
    raise SystemExit('Missing required page(s): ' + ', '.join(missing) + '. Run from the repository root.')


def apply_replacements(text, replacements, page_name):
    applied = 0
    missing_items = []
    for old, new in replacements.items():
        if old in text:
            text = text.replace(old, new)
            applied += 1
        elif new not in text:
            missing_items.append(old[:110])
    print(f'[{page_name}] replacements applied: {applied}')
    for item in missing_items:
        print(f'[{page_name}] warning, source text not found: {item}')
    return text


def standardize_navigation(text):
    text = text.replace('>Research Themes</a>', '>Research Areas</a>')
    text = text.replace('>Datasets &amp; Code</a>', '>Resources</a>')
    return text


# ABOUT PAGE
path = PAGES['about']
text = path.read_text(encoding='utf-8', errors='ignore')
about_replacements = {
    'Academic profile of Ahmed Mansour, indoor positioning and navigation researcher working on smartphone sensing, Wi-Fi fingerprinting, PDR, mobile crowdsensing, GNSS/PDR integration, 3D radio-map generation, and deployment-ready indoor spatial intelligence.':
    'Academic profile of Ahmed Mansour, a geomatics and indoor-positioning researcher working on smartphone sensing, Wi-Fi fingerprinting, pedestrian dead reckoning, mobile crowdsensing, seamless positioning, and 3D radio-map generation.',
    'About the researcher': 'Academic profile',
    'Indoor positioning, smartphone sensing, Wi-Fi fingerprinting, PDR, mobile crowdsensing, and deployment-ready indoor spatial intelligence.':
    'Researching how smartphones, radio signals, motion sensors, maps, and crowdsensed data can support reliable indoor and seamless pedestrian positioning.',
    "Ahmed Mansour is a civil engineering and geomatics researcher whose work focuses on reliable indoor positioning and navigation in complex indoor and urban environments. His research connects inertial positioning, Wi-Fi fingerprinting, autonomous radio-map generation, mobile crowdsensing, GNSS/PDR integration, indoor-outdoor transition awareness, and multi-floor spatial context.":
    "Ahmed Mansour is a civil engineering and geomatics researcher specializing in indoor positioning and pedestrian navigation. His work examines how inertial sensors, Wi-Fi fingerprints, GNSS, BLE, maps, mobile crowdsensing, and multi-user information can be combined to improve positioning continuity, reduce deployment effort, and support floor-aware services in real environments.",
    'Research identity': 'Research perspective',
    'From positioning signals to indoor spatial intelligence': 'Reliable positioning in real indoor and urban environments',
    "The hub presents Ahmed Mansour's research as a connected pipeline: inertial sensing preserves relative motion, Wi-Fi fingerprinting and radio maps provide indoor reference information, multi-source fusion supports continuity across outdoor and indoor spaces, and 3D spatial context connects positioning outputs to floor-aware and building-level services.":
    "The research is driven by a practical question: how can a positioning system remain useful when signals fluctuate, users carry phones differently, buildings span multiple floors, and no single sensing source is continuously reliable? The work addresses this question through motion estimation, radio-based references, crowdsensed mapping, multi-source fusion, and spatial context.",
    'Heading drift, carrying modes, smartphone sensing, and correction sources.':
    'Long-duration PDR, heading stability, carrying-mode changes, and trusted correction sources.',
    'Mobile crowdsensing, autonomous map generation, and reliability-governed updating.':
    'Wi-Fi fingerprints, natural mobile sessions, autonomous map generation, and controlled map updates.',
    'GNSS, PDR, Wi-Fi, BLE, barometer, maps, and transition awareness.':
    'Continuous positioning across outdoor, transition, and indoor spaces using complementary sensing sources.',
    'Floor recognition, vertical positioning, 3D radio maps, and multi-level indoor structure.':
    'Floor recognition, vertical motion, building-level map assembly, and multi-level spatial context.',
    'Research work at The Hong Kong Polytechnic University on indoor positioning, radio mapping, and smartphone-based navigation.':
    'Postdoctoral and research work at The Hong Kong Polytechnic University on smartphone navigation, radio mapping, and scalable indoor positioning.',
    'Research outputs': 'Explore the work',
    'Publication and resource entry points': 'Publications, research areas, and reusable materials',
    'Use these pages to move from the author profile to papers, citation records, machine-readable metadata, PDFs, and reproducibility notes.':
    'The following pages provide direct access to the publication portfolio, research themes, citation records, downloadable papers, structured metadata, and supporting materials.',
    'Visual paper cards, DOI links, PDFs, BibTeX, summaries, and research-area connections.':
    'Peer-reviewed papers, conference work, thesis research, DOI links, PDFs, and concise paper context.',
    'Four-area map connecting methods, sensing sources, deployment problems, and linked papers.':
    'A structured view of the research program across inertial positioning, radio mapping, seamless fusion, and 3D context.',
    'PDF index, metadata files, code and dataset status, responsible sharing notes, and reproducibility material.':
    'Downloadable papers, metadata files, visual materials, reproducibility notes, and resource-availability information.',
    'Author identifiers, paper finder, DOI links, AI-search prompts, and citation guidance.':
    'Author identifiers, DOI records, BibTeX, paper selection guidance, and literature-discovery queries.',
    'AI-readable guide to the website, publication pages, research areas, and visual assets.':
    'A machine-readable overview of the site, research areas, publication pages, and supporting files.',
    'Crawlable site map for search engines and indexing tools.':
    'A structured index of the public pages and publication records available on the site.',
    'Contact and collaboration': 'Research and collaboration',
    'Research collaboration and citation inquiries': 'Research, collaboration, and publication inquiries',
    'For questions about indoor positioning, Wi-Fi fingerprinting, pedestrian dead reckoning, mobile crowdsensing, 3D radio-map generation, or citation use of the published papers, use the contact link or start from the publication and citation-resource pages.':
    'For research discussions, collaboration opportunities, technical questions, or publication and citation inquiries, contact Ahmed Mansour directly or begin with the publication and citation-resource pages.'
}
text = apply_replacements(text, about_replacements, 'about')
text = standardize_navigation(text)
path.write_text(text, encoding='utf-8')


# CITATION RESOURCES PAGE
path = PAGES['citation']
text = path.read_text(encoding='utf-8', errors='ignore')
citation_replacements = {
    'Citation Resources and AI Search Guide | Indoor Positioning Hub | Ahmed Mansour':
    'Citation and Discovery Guide | Indoor Positioning Hub | Ahmed Mansour',
    "Citation toolkit for Ahmed Mansour's indoor positioning publications, including author identifiers, DOI links, BibTeX, metadata files, research-area guidance, paper-use notes, and AI-search prompts.":
    "Citation and discovery guide for Ahmed Mansour's indoor-positioning publications, including author identifiers, DOI links, BibTeX, structured metadata, research-area guidance, and literature-search queries.",
    'Citation Resources and AI Search Guide': 'Citation and discovery',
    "Find, cite, and connect Ahmed Mansour's indoor positioning publications": 'Find the right paper and cite it accurately',
    'This page helps readers identify which paper fits a specific indoor positioning question, copy citation resources, verify author identifiers, and test discovery through Google, Google Scholar, Semantic Scholar-style systems, OpenAlex, Elicit, SciSpace, Perplexity, and AI-assisted web search.':
    'Use this page to identify the paper that best matches a research question, verify the author record, open the published source, and retrieve citation-ready metadata. It also provides practical search queries for locating the work through scholarly databases and AI-assisted literature tools.',
    'Citation identity': 'Research scope',
    'Core research identity': 'Research scope at a glance',
    "Ahmed Mansour's work focuses on indoor positioning, smartphone positioning, pedestrian positioning, Wi-Fi fingerprinting, mobile crowdsensing, autonomous radio-map generation, seamless indoor-outdoor positioning, PDR, GNSS/PDR integration, cooperative positioning, and deployment-ready indoor spatial intelligence.":
    "Ahmed Mansour's publications address indoor positioning and pedestrian navigation from sensing, mapping, fusion, and deployment perspectives. The main themes include smartphone PDR, Wi-Fi fingerprinting, mobile crowdsensing, autonomous radio-map generation, seamless indoor-outdoor positioning, GNSS/PDR integration, cooperative localization, and floor-aware spatial context.",
    'When to cite which work': 'Selecting a relevant paper',
    'Research-area citation guide': 'Choose publications by research question',
    'Use the four research areas to choose the most relevant paper for a specific argument, literature review, method comparison, or background section.':
    'The four research areas below provide a direct route from a topic or manuscript claim to the most relevant publications.',
    'Cite these papers for smartphone PDR, heading drift control, carrying-mode robustness, inertial sensing, and GNSS/PDR-aided pedestrian navigation.':
    'Use these publications for smartphone PDR, heading estimation, carrying-mode changes, inertial drift control, and pedestrian navigation supported by GNSS or other corrections.',
    'Cite these papers for Wi-Fi fingerprinting, mobile crowdsensing, radio-map generation, autonomous map updating, and reliability-governed IPS scaling.':
    'Use these publications for Wi-Fi fingerprinting, mobile crowdsensing, initial radio-map generation, long-term map maintenance, and scalable indoor-positioning deployment.',
    'Cite these papers for GNSS, Wi-Fi, MEMS, BLE, PDR, indoor-outdoor awareness, source switching, and transition-aware navigation.':
    'Use these publications for indoor-outdoor detection, GNSS/PDR integration, BLE-enhanced positioning, source switching, and continuity across transition spaces.',
    'Cite these papers for 3D radio maps, multi-floor positioning, floor recognition, vertical positioning, building-level assembly, and spatial context.':
    'Use these publications for multi-floor positioning, 3D radio maps, floor recognition, vertical movement, building-level assembly, and spatial constraints.',
    'Paper finder': 'Publication records',
    'Publication pages, DOI links, and PDFs': 'Publication records, DOI links, and accessible PDFs',
    'The publication page is the best citation entry point because it links title, year, venue, DOI, PDF, summary, and research-area connection.':
    "Each publication page brings together the title, authors, year, venue, DOI, available PDF, citation metadata, and a concise explanation of the paper's role in the wider research program.",
    'AI-search prompts': 'Literature-search queries',
    'Discovery test queries': 'Useful queries for literature discovery',
    'Use these prompts to test whether the hub and individual publication pages are discoverable by conventional search engines and AI-assisted search tools.':
    'These queries can be copied into scholarly search engines or AI-assisted literature tools to locate the most relevant publications by topic.',
    'Machine-readable citation resources': 'Structured citation resources',
    'Metadata files for citation and indexing': 'Citation files and structured metadata',
    'These files support citation managers, search engines, AI systems, and reproducibility workflows.':
    'These files support citation managers, automated indexing, publication discovery, and reproducible reference management.',
    'BibTeX entries for manuscript and citation-manager workflows.':
    'BibTeX records for manuscripts, reference managers, and collaborative writing workflows.',
    'Structured publication metadata used by the hub.':
    'Structured records containing publication titles, links, years, venues, and related metadata.',
    'AI-readable guide to the site, research areas, and publication pages.':
    'A concise machine-readable guide to the site, research areas, and publication pages.',
    'Crawlable URL map for search engines and indexing tools.':
    'A structured URL index for search engines and scholarly discovery services.',
    'PDFs, metadata, reproducibility notes, code and dataset status.':
    'PDFs, visual materials, metadata, reproducibility notes, and resource-availability information.',
    'Author identity, academic profile, affiliations, and profile links.':
    'Academic profile, research background, identifiers, CV, and professional links.',
    'Citation note': 'Good citation practice',
    'Use DOI and official publication metadata when available': 'Prefer the published version of record',
    'For formal manuscripts, cite the published version of record whenever a DOI is available. Use this hub as a discovery, reading, PDF-access, and citation-guidance layer. For papers with publisher restrictions, use DOI links rather than redistributing restricted PDFs.':
    'For formal manuscripts, cite the published version of record whenever a DOI is available. The hub is intended to support discovery, reading, and citation preparation; publisher-restricted papers should be accessed through their DOI or authorized source.'
}
text = apply_replacements(text, citation_replacements, 'citation')
text = standardize_navigation(text)
path.write_text(text, encoding='utf-8')


# RESEARCH AREAS PAGE
path = PAGES['research']
text = path.read_text(encoding='utf-8', errors='ignore')
research_replacements = {
    "Research-area landing page for Ahmed Mansour's Indoor Positioning Hub, connecting inertial positioning, Wi-Fi fingerprinting, seamless indoor-outdoor fusion, 3D radio-map generation, vertical positioning, and deployment-ready indoor spatial intelligence.":
    "Research program for Ahmed Mansour's Indoor Positioning Hub, connecting inertial positioning, Wi-Fi fingerprinting, mobile crowdsensing, seamless indoor-outdoor positioning, 3D radio-map generation, floor recognition, and vertical positioning.",
    'Research Areas and Publication Map': 'Research program',
    'Research areas across the Indoor Positioning Hub': 'Four connected research areas in indoor positioning',
    "This page connects the publication portfolio to four research areas that structure Ahmed Mansour's work: inertial positioning, Wi-Fi fingerprinting and radio-map scaling, seamless indoor-outdoor fusion, and 3D indoor spatial context. The goal is to help readers move from a broad positioning question to the most relevant papers, methods, figures, and citation records.":
    "The research program is organized around four connected problems: maintaining pedestrian motion with inertial sensing, creating dependable indoor references from Wi-Fi and crowdsensed data, preserving continuity across outdoor and indoor spaces, and representing multi-floor environments in 3D. Each area links the underlying research questions to representative publications.",
    'Smartphone inertial sensing keeps the trajectory alive when external positioning cues are weak or unavailable.':
    'Smartphone inertial sensing preserves short-term motion when external references are unavailable, but drift and heading errors must be controlled.',
    'Wi-Fi fingerprints and radio maps provide indoor absolute references for correction, initialization, and map-based services.':
    'Wi-Fi fingerprints provide indoor reference information, while scalable deployment depends on how radio maps are created, checked, and updated.',
    'GNSS, PDR, Wi-Fi, BLE, barometer, maps, and transition awareness are fused to prevent positioning breaks.':
    'Complementary sources are combined so that positioning remains continuous as users move through outdoor, transition, and indoor spaces.',
    'Floor recognition, vertical motion, and building-level map assembly connect positioning to multi-level indoor structure.':
    'Floor recognition, vertical motion, and building-level assembly place the position estimate within a meaningful multi-level structure.',
    'Smartphone inertial sensing is the relative-motion layer of pedestrian navigation. It supports positioning when GNSS, Wi-Fi, BLE, vision, or map-based cues are weak, intermittent, or unavailable. The central challenge is to control drift, heading error, pose changes, and walking-direction uncertainty without requiring dedicated infrastructure.':
    'Smartphone inertial sensing provides continuous motion information without installed infrastructure. The research focuses on keeping that motion estimate useful despite gyroscope drift, magnetic disturbance, changing phone poses, uncertain walking direction, and interruptions between trusted position updates.',
    'Wi-Fi fingerprinting provides an indoor absolute reference, but scalable deployment requires moving beyond manual radio-map surveys. This area studies how ordinary mobile sessions, multisensor logs, RSS observations, and reliability checks can support autonomous map generation, map updating, and long-term maintenance.':
    'Wi-Fi fingerprinting can anchor a user to an indoor location, but conventional surveying is expensive to repeat across buildings and floors. The work examines how natural mobile sessions, multisensor logs, crowdsensed fingerprints, and reliability checks can support map creation and long-term maintenance with less dedicated surveying.',
    'Positioning should remain continuous as users move through streets, entrances, semi-open spaces, corridors, elevators, lobbies, and rooms. This area connects GNSS, PDR, Wi-Fi, BLE, barometer, map constraints, and indoor–outdoor awareness so that the trajectory does not break when sensing conditions change.':
    'A pedestrian trajectory should remain meaningful as the user moves from open sky to urban canyons, entrances, lobbies, corridors, elevators, and rooms. This work combines GNSS, PDR, Wi-Fi, BLE, barometer readings, maps, and environmental awareness so that the system can adapt as signal conditions change.',
    'Multi-floor indoor positioning requires more than a two-dimensional coordinate. This area studies 3D radio-map generation from mobile crowdsensing, including floor-local skeleton construction, building-level assembly, global refinement, vertical positioning, floor recognition, and multi-level indoor spatial context.':
    'A two-dimensional coordinate is insufficient when the same plan location may occur on several floors. This area addresses floor-local trace reconstruction, vertical-motion interpretation, floor recognition, building-level assembly, and global refinement for 3D radio maps generated from mobile crowdsensing.',
    'Key problems': 'Research challenges',
    'Linked publications': 'Representative publications',
    'Supporting directions': 'Cross-cutting directions',
    'Related themes connected to the four-area map': 'Applications and cross-cutting research directions',
    'Some publications extend the positioning pipeline toward cooperative localization, construction safety, BIM-based risk mapping, AI-guided engagement, and deployment-ready services. These directions remain connected to the four-area structure but serve specific application or system-design needs.':
    'Several publications extend these core areas into cooperative positioning, construction safety, BIM-based risk mapping, AI-guided user engagement, and location-aware services. These studies show how the underlying positioning methods support broader operational and decision-making needs.'
}
text = apply_replacements(text, research_replacements, 'research')
text = standardize_navigation(text)
path.write_text(text, encoding='utf-8')


# RESOURCES PAGE
path = PAGES['resources']
text = path.read_text(encoding='utf-8', errors='ignore')
resources_replacements = {
    'Resources, PDFs, Metadata, and Reproducibility | Indoor Positioning Hub | Ahmed Mansour':
    'Research Resources | Indoor Positioning Hub | Ahmed Mansour',
    "Resources page for Ahmed Mansour's Indoor Positioning Hub, including publication PDFs, BibTeX, JSON metadata, reproducibility notes, code and dataset status, responsible sharing policy, sitemap, and llms.txt.":
    "Research resources for Ahmed Mansour's Indoor Positioning Hub, including publication PDFs, BibTeX, structured metadata, visual materials, reproducibility notes, resource availability, sitemap, and llms.txt.",
    'Resources, PDFs, Metadata, and Reproducibility': 'Research resources',
    'Research resources for indoor positioning, radio mapping, and spatial intelligence':
    'Papers, metadata, visuals, and reproducibility materials',
    'This page collects reusable materials connected to the Indoor Positioning Hub: publication PDFs, citation files, machine-readable metadata, reproducibility notes, code and dataset status, and responsible sharing rules. It gives readers, collaborators, reviewers, students, and AI-assisted search systems a clear entry point to the technical resources behind the publication portfolio.':
    'Use this page to access publication PDFs, citation files, structured metadata, visual explanations, reproducibility notes, and information about code and dataset availability. The materials are organized to support reading, citation, teaching, collaboration, and future reuse.',
    'Paper summaries, DOI links, PDFs, BibTeX, and research-area connections.':
    'Paper records with DOI links, accessible PDFs, citation files, and links to the relevant research areas.',
    'Citation-ready records for the publication portfolio.':
    'BibTeX records for manuscripts, reference managers, and collaborative writing.',
    'Machine-readable publication data for indexing and reuse.':
    'Structured publication records for indexing, search, and programmatic reuse.',
    'Crawlable URL map for pages, PDFs, and metadata resources.':
    'A structured index of public pages, publication records, and supporting resources.',
    'AI-readable guide to the hub, research areas, and publication pages.':
    'A concise machine-readable guide to the site, research areas, and publication pages.',
    'Academic profile, identifiers, and publication record.':
    'Academic background, research profile, identifiers, and publication record.',
    'Downloadable resources': 'Publication access',
    'Publication PDFs and paper-level records': 'Publication PDFs and source records',
    'Each publication page is the preferred entry point because it connects the PDF, DOI, BibTeX, summary, visual preview, and research-area context. Direct PDF links are listed here for fast access when redistribution is allowed.':
    'The publication pages provide the most complete record of each work, including the DOI, available PDF, citation metadata, visual preview, and research context. Direct PDF links are also listed below where redistribution is permitted.',
    'Visual research materials': 'Visual explanations',
    'Figures and live GIFs used across the hub': 'Figures and animations that explain the research',
    'The resources page now reflects the streamlined visual set: a future-facing scene, an enlarged 3D indoor scene, and two live GIF demonstrations for autonomous radio-map generation and indoor-outdoor seamless positioning.':
    'Selected figures and animations provide visual introductions to multi-floor positioning, autonomous radio-map generation, indoor-outdoor awareness, and the longer-term vision of indoor spatial intelligence.',
    'Reproducibility by research area': 'Methods and reproducibility',
    'How the resources map to the research program': 'Resources organized by research area',
    'The hub is organized around four research areas. These notes explain which types of implementation details and reproducibility material are most relevant to each area.':
    'The four research areas below indicate the types of technical material associated with each part of the research program.',
    'Smartphone inertial processing, heading estimation, carrying-mode descriptions, PDR correction logic, and implementation notes.':
    'Sensor-processing details, heading estimation, carrying-mode handling, PDR correction strategies, and implementation notes.',
    'Fingerprinting metadata, crowdsensing session descriptions, radio-map generation diagrams, and reliability-governed updating concepts.':
    'Fingerprinting metadata, mobile-session descriptions, radio-map generation workflows, uncertainty checks, and map-maintenance concepts.',
    'GNSS/PDR integration, transition figures, BLE-enhanced positioning records, and source-switching explanations.':
    'GNSS/PDR integration, indoor-outdoor detection, BLE-enhanced positioning, transition figures, and source-selection logic.',
    'Floor-local skeletons, building-level assembly, vertical positioning, floor recognition, and 3D indoor spatial-reference material.':
    'Floor-local skeletons, vertical-motion interpretation, floor recognition, building-level assembly, and 3D spatial references.',
    'Code and dataset status': 'Resource availability',
    'Availability and sharing notes': 'What is available, under preparation, or shared selectively',
    'The status is stated directly so readers know what is available now, what is planned, and what may require permission or request-based access.':
    'Availability depends on publication rights, privacy, collaborator agreements, and the maturity of the supporting material. The categories below distinguish resources that can be accessed now from material under preparation or shared selectively.',
    'Available now': 'Available on this site',
    'Publication pages with DOI links, PDFs when allowed, and citation material.':
    'Publication pages with DOI links, accessible PDFs, and citation records.',
    'Machine-readable publication metadata in JSON.':
    'Structured publication metadata in JSON format.',
    'BibTeX file for citation workflows.':
    'A consolidated BibTeX file for reference-management workflows.',
    'Figures and visual research-area explanations embedded in the website.':
    'Figures and animations that explain the main research areas and selected papers.',
    'Planned resources': 'Under preparation',
    'Wi-Fi fingerprinting reliability benchmarks.':
    'Benchmark material for Wi-Fi fingerprinting reliability and integrity assessment.',
    'Autonomous 3D radio-map generation scripts.':
    'Implementation material for autonomous 3D radio-map generation.',
    'PDR and heading-estimation implementation notes.':
    'Technical notes for PDR, carrying-mode recognition, and heading correction.',
    'IOD and seamless-positioning supplementary tables and search strings.':
    'Supplementary tables and search records for indoor-outdoor detection and seamless positioning reviews.',
    'Request-based or restricted': 'Shared selectively or restricted',
    'Indoor trajectories that contain privacy-sensitive location traces.':
    'Indoor trajectories containing privacy-sensitive movement or location information.',
    'Raw mobile crowdsensing sessions with user or device identifiers.':
    'Raw mobile crowdsensing sessions that may contain user, device, or site identifiers.',
    'Publisher-restricted PDFs, where DOI links are used instead of direct redistribution.':
    'Publisher-restricted articles, which are linked through the DOI rather than redistributed.',
    'Project-specific datasets controlled by collaborators, institutions, or venue policies.':
    'Project-specific data governed by collaborator agreements, institutional requirements, or publication policies.',
    'Responsible sharing policy': 'Responsible access',
    'Open where possible, careful where necessary': 'Open access where possible, controlled sharing where necessary',
    'Indoor positioning resources can include sensitive location traces, Wi-Fi scans, device identifiers, building layouts, and movement patterns. The hub separates public academic material from restricted or request-based data. Open-access papers, accepted manuscripts, BibTeX, metadata, and explanatory figures are shared directly when permitted. Restricted publisher files, privacy-sensitive datasets, and collaboration-controlled materials are linked or described without exposing data that should not be redistributed.':
    'Indoor-positioning data can reveal movement patterns, device information, wireless infrastructure, and details of internal spaces. Public papers, citation records, metadata, and explanatory figures are shared directly when permitted. Privacy-sensitive data, restricted publisher files, and collaboration-controlled material are described or linked without exposing information that should not be redistributed.',
    'Machine-readable resources': 'Structured site resources',
    'Files for search engines, AI systems, and citation workflows':
    'Files for indexing, citation, and machine-assisted discovery',
    'These files help machines discover the site structure, publication records, and research-area relationships.':
    'These files describe the site structure, publication records, and relationships among the research areas in formats suitable for indexing and automated discovery.',
    'AI-readable guide to the hub and research areas.':
    'A concise machine-readable guide to the site and its research areas.',
    'Crawlable index of website URLs.': 'A structured index of public website URLs.',
    'Search-engine access and sitemap pointer.': 'Crawling guidance and the location of the site map.',
    'Structured publication metadata.': 'Structured records for the publication portfolio.',
    'BibTeX entries for citation workflows.': 'BibTeX records for reference managers and manuscript preparation.',
    'Author identifiers and paper-use guidance.':
    'Author identifiers, publication records, and guidance for selecting the relevant paper.'
}
text = apply_replacements(text, resources_replacements, 'resources')
text = standardize_navigation(text)
path.write_text(text, encoding='utf-8')


# PUBLICATIONS PAGE
path = PAGES['publications']
text = path.read_text(encoding='utf-8', errors='ignore')
publications_replacements = {
    "Visual, citation-ready publication list for Ahmed Mansour's work on indoor positioning, Wi-Fi fingerprinting, crowdsensing, radio maps, PDR, IOD, GNSS/PDR integration, and spatial intelligence.":
    "Publication portfolio for Ahmed Mansour's work on indoor positioning, Wi-Fi fingerprinting, pedestrian dead reckoning, mobile crowdsensing, radio-map generation, seamless positioning, cooperative localization, and indoor spatial intelligence.",
    "This page brings together Ahmed Mansour's peer-reviewed publications, thesis work, and conference outputs in indoor positioning and indoor spatial intelligence. The papers are organized around Wi-Fi fingerprinting, smartphone PDR, mobile crowdsensing, autonomous 3D radio mapping, indoor--outdoor awareness, GNSS/PDR integration, cooperative localization, and deployment-aware positioning for smart buildings, construction sites, and urban environments.":
    "This portfolio brings together journal articles, conference papers, workshop contributions, and doctoral research on indoor positioning and pedestrian navigation. The publications span smartphone PDR, Wi-Fi fingerprinting, mobile crowdsensing, radio-map generation, indoor-outdoor continuity, GNSS/PDR integration, cooperative localization, construction safety, and floor-aware spatial context.",
    "Each card works as a quick reading guide. The first-page preview identifies the paper at a glance, the highlighted author name shows Ahmed Mansour's role, the venue, ranking, and DOI badges support citation, and the symbol and keyword cues summarize the problem setting, sensing data, method family, and deployment context.":
    "Each card provides a concise view of the paper's research problem, sensing sources, method, application setting, publication venue, DOI, and available PDF. Open the dedicated publication page for a fuller explanation and links to the related research area."
}
text = apply_replacements(text, publications_replacements, 'publications')

note_pattern = re.compile(r'<section class="publications-note-card">.*?</section>', flags=re.S)
new_note = '''<section class="publications-note-card">
    <strong>Browse the portfolio by research problem, sensing source, method, or application.</strong>
    The collection shows how the research has developed from smartphone PDR and multi-sensor fusion toward mobile crowdsensing, autonomous radio mapping, cooperative positioning, seamless navigation, and location-aware decision support.
  </section>'''
if note_pattern.search(text):
    text = note_pattern.sub(new_note, text, count=1)
    print('[publications] publication note card refined')
elif new_note not in text:
    print('[publications] warning, publication note card not found')

lens_map = {
    'uncertainty-aware-risk-mapping-passive-wifi-bim-construction':
    'Passive Wi-Fi observations are translated into uncertainty-aware spatial risk zones within BIM, supporting non-intrusive construction safety monitoring when location estimates are imperfect.',
    'towards-scalable-ips-user-centric-crowd-powered-framework':
    "The review examines why crowd-powered indoor positioning succeeds or fails from the user's perspective. It brings together participation, incentives, privacy, security, device burden, and long-term deployment.",
    'reliability-governed-3d-radio-mapping-lifecycle-review':
    'The review treats 3D radio mapping as a lifecycle rather than a one-time survey. It connects map creation, updating, uncertainty assessment, validation, and deployment safeguards.',
    'hybrid-neural-network-pdr-multi-layer-heading-correction':
    'The method recognizes smartphone carrying modes and applies layered heading corrections so that PDR remains stable when the phone moves between calling, swinging, texting, and pocket use.',
    'gnss-positioning-aided-with-pdr-in-urban-areas':
    'PDR-derived motion constraints are used to identify and limit faulty GNSS observations in urban areas, improving pedestrian positioning under multipath and non-line-of-sight conditions.',
    'drift-resistant-heading-estimation-wifi-magnetic-stability':
    'Wi-Fi continuity and magnetic stability provide opportunistic references for adaptive heading calibration, reducing drift without depending on a single absolute heading source.',
    'ac-hmm-azimuth-constrained-map-matching-urban-canyons':
    'Directional constraints are embedded in a hidden Markov map-matching framework to keep pedestrian trajectories consistent with road geometry in urban canyons.',
    'enhancing-real-time-heading-estimation-deep-learning-smartphone-sensors':
    'Visual and inertial cues are combined to correct smartphone heading in real time, reducing the effect of gyroscope drift and compass bias during pedestrian navigation.',
    'modular-prompting-ai-guided-user-engagement-crowd-powered-ips':
    'Semantic knowledge graphs and modular prompts are used to request spatial feedback only when it is useful, making crowd-powered data collection more contextual and less intrusive.',
    'towards-ubiquitous-ips-crowdsourced-data-accumulation':
    'Accumulated crowdsourced measurements are used to infer stable access-point properties and reduce dependence on external references during initial radio-map generation.',
    'tightly-coupled-bluetooth-enhanced-gnss-pdr-urban':
    'BLE observations are tightly integrated with GNSS and PDR to maintain pedestrian navigation in dense urban and semi-outdoor areas where satellite positioning is unstable.',
    'power-of-many-multi-user-collaborative-indoor-localization':
    'Relative measurements between nearby users create temporary cooperative constraints, allowing a group to strengthen individual indoor position estimates without fixed infrastructure.',
    'leveraging-human-mobility-pervasive-smartphone-crowdsourcing':
    'Everyday human movement and smartphone sensing are turned into mapping data for a self-deployable indoor positioning system, reducing the need for dedicated survey campaigns.',
    'phd-thesis-indoor-localization-multi-sensor-crowdsourcing-collaboration':
    'The thesis develops a unified foundation for multi-sensor fusion, crowdsourced radio mapping, and multi-user collaboration in indoor localization.',
    'everywhere-framework-ubiquitous-indoor-localization':
    'Everywhere shows how selected smartphone measurements, inertial information, and GNSS-aided adjustment can build and use fingerprints with minimal dedicated surveying.',
    'suns-seamless-ubiquitous-navigation-indoor-outdoor-awareness':
    'SUNS uses indoor-outdoor awareness to select and combine positioning resources as users move across outdoor, transition, and indoor spaces.',
    'drift-control-pdr-long-period-navigation-smartphone-poses':
    'The study examines how smartphone pose changes affect long-duration PDR and develops drift-control strategies for more stable pedestrian tracking.'
}
lens_updates = 0
for article_id, new_lens in lens_map.items():
    pattern = re.compile(
        rf'(<article class="pub-visual-card" id="{re.escape(article_id)}">.*?<p class="pub-paper-lens">)(.*?)(</p>)',
        flags=re.S
    )
    if pattern.search(text):
        text = pattern.sub(lambda m: m.group(1) + new_lens + m.group(3), text, count=1)
        lens_updates += 1
    elif new_lens not in text:
        print(f'[publications] warning, lens not found for {article_id}')
print(f'[publications] paper descriptions refined: {lens_updates}')
text = text.replace('indoor--outdoor', 'indoor-outdoor')
text = standardize_navigation(text)
path.write_text(text, encoding='utf-8')


# CV REDIRECT PAGE
path = PAGES['cv']
cv_html = '''<!doctype html>
<html lang="en">
<head>
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width, initial-scale=1">
  <title>Ahmed Mansour CV and Academic Profile | Indoor Positioning Hub</title>
  <meta name="description" content="Open Ahmed Mansour's academic profile or download the public CV from the Indoor Positioning Hub.">
  <meta name="robots" content="noindex,follow">
  <link rel="canonical" href="https://ahmedmansoour.github.io/indoor-positioning-hub/about.html">
  <meta http-equiv="refresh" content="0; url=about.html">
  <link rel="stylesheet" href="assets/css/style.css">
</head>
<body>
  <main class="container" style="padding:3rem 0;">
    <p class="eyebrow">Academic profile</p>
    <h1>Ahmed Mansour</h1>
    <p>The academic profile, research background, identifiers, and CV access are available on the About page.</p>
    <p>
      <a class="button primary" href="about.html">Open academic profile</a>
      <a class="button" href="assets/cv/ahmed-mansour-public-cv.pdf">Download public CV</a>
    </p>
  </main>
</body>
</html>
'''
path.write_text(cv_html, encoding='utf-8')
print('[cv] redirect copy refined and destination changed to about.html')


# LLMS NOTE
if LLMS.exists():
    llms = LLMS.read_text(encoding='utf-8', errors='ignore')
    note = '''
## Site-wide copy refinement

- Revised pages: about.html, citation-resources.html, publications.html, research-themes.html, resources.html, and cv.html.
- Update: process-oriented update language, repetitive mechanical descriptions, internal maintenance notes, and shallow page explanations were replaced with clearer academic website copy while preserving the existing layouts and URLs.
'''
    if '## Site-wide copy refinement' not in llms:
        marker = '## Homepage copy refinement'
        if marker in llms:
            llms = llms.replace(marker, note + '\n' + marker)
        else:
            llms = llms.rstrip() + '\n' + note + '\n'
        LLMS.write_text(llms, encoding='utf-8')
        print('[llms] site-wide copy refinement note added')
    else:
        print('[llms] site-wide copy refinement note already present')

print('Done: refined secondary website pages without changing their layout classes or URLs.')
