from pathlib import Path
import json
import re

ROOT = Path(__file__).resolve().parents[1]
SUMMARY_FILE = ROOT / "data" / "long_summaries.json"
PUB_DIR = ROOT / "publications"
CSS_FILE = ROOT / "assets" / "css" / "style.css"

summaries = json.loads(SUMMARY_FILE.read_text(encoding="utf-8"))

CSS = r"""

/* Long research story summaries */
.paper-story-section {
  margin-top: 2rem;
}
.story-flow {
  display: flex;
  flex-wrap: wrap;
  gap: 0.55rem;
  align-items: center;
  margin: 0.75rem 0 1.25rem 0;
  padding: 0.85rem 1rem;
  border: 1px solid #d9e1ea;
  border-radius: 16px;
  background: linear-gradient(180deg, #ffffff, #f7fbff);
}
.story-flow span {
  display: inline-flex;
  align-items: center;
  font-size: 0.95rem;
  line-height: 1.35;
}
.story-flow .node {
  padding: 0.35rem 0.65rem;
  border-radius: 999px;
  background: #eef5ff;
  color: #173b63;
  font-weight: 650;
}
.story-flow .arrow {
  color: #6b7a8a;
  font-weight: 700;
}
.story-legend {
  display: grid;
  grid-template-columns: repeat(auto-fit, minmax(180px, 1fr));
  gap: 0.75rem;
  margin: 1rem 0 1.25rem 0;
}
.story-legend div {
  padding: 0.75rem;
  border-radius: 14px;
  background: #f8fafc;
  border: 1px solid #e5edf5;
}
.story-legend strong {
  display: block;
  margin-bottom: 0.25rem;
  color: #173b63;
}
.paper-story-section p {
  margin-bottom: 1rem;
  line-height: 1.75;
}
"""

def make_story(slug, record):
    flow = record.get("flow", [])
    nodes = []
    for i, item in enumerate(flow):
        if i:
            nodes.append('<span class="arrow">→</span>')
        nodes.append(f'<span class="node">{item}</span>')
    flow_html = '<div class="story-flow">' + "\n    ".join(nodes) + '</div>'
    legend = """
  <div class="story-legend">
    <div><strong>Problem</strong>The paper starts from a practical barrier that limits reliable positioning or deployment.</div>
    <div><strong>Mechanism</strong>The method or framework converts signals, sensors, users, or maps into useful positioning knowledge.</div>
    <div><strong>Value</strong>The contribution helps readers understand where the work fits and when it should be cited.</div>
  </div>
"""
    return f"""<section class="paper-story-section card">
  <h2>Research story and quick reading guide</h2>
  {flow_html}
  {legend}
  {record["html"].strip()}
</section>"""

def remove_old_summary_sections(html):
    # Remove our earlier story section if present.
    html = re.sub(r'\n?<section class="paper-story-section card">.*?</section>\n?', '\n', html, flags=re.S)
    # Remove old paper-summary section if present.
    html = re.sub(r'\n?<section class="paper-summary card">.*?</section>\n?', '\n', html, flags=re.S)
    # Remove old generic summary card only, keep When to cite, Keywords, BibTeX.
    html = re.sub(r'\n?<section class="card">\s*<h2>(?:Summary|Extended summary)</h2>.*?</section>\n?', '\n', html, flags=re.S)
    return html

def insert_after_preview_or_actions(html, story):
    # Prefer insertion immediately after the paper preview section.
    m = re.search(r'(<section class="paper-preview-section card">.*?</section>)', html, flags=re.S)
    if m:
        return html[:m.end()] + "\n" + story + html[m.end():]
    # Fallback: insert after paper-actions.
    m = re.search(r'(<div class="paper-actions">.*?</div>)', html, flags=re.S)
    if m:
        return html[:m.end()] + "\n" + story + html[m.end():]
    # Final fallback: before When to cite.
    m = re.search(r'(<section class="card" id="when-to-cite">)', html)
    if m:
        return html[:m.start()] + story + "\n" + html[m.start():]
    return html + "\n" + story

def ensure_css():
    css = CSS_FILE.read_text(encoding="utf-8", errors="ignore")
    if "/* Long research story summaries */" not in css:
        CSS_FILE.write_text(css + CSS, encoding="utf-8")

def main():
    changed = []
    missing = []
    for slug, record in summaries.items():
        page = PUB_DIR / f"{slug}.html"
        if not page.exists():
            missing.append(slug)
            continue
        html = page.read_text(encoding="utf-8", errors="ignore")
        new_html = remove_old_summary_sections(html)
        story = make_story(slug, record)
        new_html = insert_after_preview_or_actions(new_html, story)
        if new_html != html:
            page.write_text(new_html, encoding="utf-8")
            changed.append(slug)
    ensure_css()
    print("Updated long summaries:", len(changed))
    for slug in changed:
        print(" -", slug)
    if missing:
        print("Missing pages:", len(missing))
        for slug in missing:
            print(" -", slug)

if __name__ == "__main__":
    main()
