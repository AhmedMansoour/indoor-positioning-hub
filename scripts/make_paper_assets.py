from pathlib import Path
import shutil
import fitz

ROOT = Path(__file__).resolve().parents[1]

SOURCE_PDFS = ROOT / "pdfs"
PUBLIC_PDFS = ROOT / "paper-pdfs"
PREVIEWS = ROOT / "assets" / "previews"
FIGURES = ROOT / "assets" / "figures"

PUBLIC_PDFS.mkdir(parents=True, exist_ok=True)
PREVIEWS.mkdir(parents=True, exist_ok=True)
FIGURES.mkdir(parents=True, exist_ok=True)

PDF_MAP = {
    "ac-hmm-azimuth-constrained-map-matching-urban-canyons":
        "AC-HMM  azimuth-constrained hidden Markov model-based map matching for robust pedestrian positioning in urban canyons.pdf",

    "drift-resistant-heading-estimation-wifi-magnetic-stability":
        "Drift-Resistant_Heading_Estimation_for_Smartphone-Based_Indoor_Positioning_via_Adaptive_Calibration_Using_Wi-Fi_Fingerprinting_and_Magnetic_Stability.pdf",

    "gnss-positioning-aided-with-pdr-in-urban-areas":
        "GNSS_Positioning_Aided_with_Pedestrian_Dead_Reckoning_PDR_in_Urban_Areas.pdf",

    "hybrid-neural-network-pdr-multi-layer-heading-correction":
        "sensors-26-02421-v2.pdf",

    "reliability-governed-3d-radio-mapping-lifecycle-review":
        "1-s2.0-S1566253526003386-main.pdf",

    "towards-scalable-ips-user-centric-crowd-powered-framework":
        "1-s2.0-S1566253525007754-main.pdf",

    "uncertainty-aware-risk-mapping-passive-wifi-bim-construction":
        "1-s2.0-S0926580526000208-main.pdf",

    "modular-prompting-ai-guided-user-engagement-crowd-powered-ips":
        "short24.pdf",

    "enhancing-real-time-heading-estimation-deep-learning-smartphone-sensors":
        "s41598-025-13390-9.pdf",

    "tightly-coupled-bluetooth-enhanced-gnss-pdr-urban":
        "Tightly_Coupled_Bluetooth_Enhanced_GNSS_PDR_System_for_Pedestrian_Navigation_in_Dense_Urban_Environments.pdf",

    "towards-ubiquitous-ips-crowdsourced-data-accumulation":
        "Towards_Ubiquitous_IPS_Leveraging_Crowdsourced_Data_Accumulation_Over_Time_to_Alleviate_Reliance_on_External_Sources_in_Initial_Fingerprinting_Map_Generation.pdf",

    "everywhere-framework-ubiquitous-indoor-localization":
        "Everywhere_A_Framework_for_Ubiquitous_Indoor_Localization.pdf",

    "phd-thesis-indoor-localization-multi-sensor-crowdsourcing-collaboration":
        "6889.pdf",

    "leveraging-human-mobility-pervasive-smartphone-crowdsourcing":
        "isprs-archives-XLVIII-1-W2-2023-1119-2023.pdf",

    "power-of-many-multi-user-collaborative-indoor-localization":
        "ION GNSS+2023 revised.pdf",

    "suns-seamless-ubiquitous-navigation-indoor-outdoor-awareness":
        "remotesensing-14-05263-v2.pdf",

    "drift-control-pdr-long-period-navigation-smartphone-poses":
        "engproc-10-00021.pdf",
}

def render_first_page(pdf_path: Path, out_png: Path):
    doc = fitz.open(pdf_path)
    page = doc.load_page(0)
    pix = page.get_pixmap(matrix=fitz.Matrix(2.0, 2.0), alpha=False)
    pix.save(out_png)
    doc.close()

def extract_candidate_figures(pdf_path: Path, out_dir: Path):
    out_dir.mkdir(parents=True, exist_ok=True)
    doc = fitz.open(pdf_path)

    candidates = []

    for page_index in range(min(10, doc.page_count)):
        page = doc.load_page(page_index)
        for img_index, img in enumerate(page.get_images(full=True), start=1):
            xref = img[0]
            pix = fitz.Pixmap(doc, xref)

            if pix.width < 350 or pix.height < 250:
                pix = None
                continue

            area = pix.width * pix.height
            candidates.append((area, page_index, img_index, xref))
            pix = None

    candidates = sorted(candidates, reverse=True)[:5]

    for rank, (_, page_index, img_index, xref) in enumerate(candidates, start=1):
        pix = fitz.Pixmap(doc, xref)
        if pix.n - pix.alpha > 3:
            pix = fitz.Pixmap(fitz.csRGB, pix)
        out_file = out_dir / f"candidate_{rank:02d}_page_{page_index+1}.png"
        pix.save(out_file)
        pix = None

    doc.close()
    return len(candidates)

def main():
    built = []
    missing = []

    for slug, raw_name in PDF_MAP.items():
        raw_pdf = SOURCE_PDFS / raw_name
        public_pdf = PUBLIC_PDFS / f"{slug}.pdf"
        preview_png = PREVIEWS / f"{slug}.png"
        fig_dir = FIGURES / slug

        if not raw_pdf.exists():
            missing.append((slug, raw_name))
            continue

        shutil.copy2(raw_pdf, public_pdf)
        render_first_page(public_pdf, preview_png)
        nfig = extract_candidate_figures(public_pdf, fig_dir)
        built.append((slug, nfig))

    print("\nBuilt assets:")
    for slug, nfig in built:
        print(f"  {slug}: preview created, {nfig} candidate figures extracted")

    if missing:
        print("\nMissing PDFs:")
        for slug, raw_name in missing:
            print(f"  {slug}: {raw_name}")

if __name__ == "__main__":
    main()