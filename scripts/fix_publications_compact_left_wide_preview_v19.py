from pathlib import Path
import re

root = Path('.')
css_path = root / 'assets' / 'css' / 'style.css'
html_path = root / 'publications.html'

if not css_path.exists():
    raise FileNotFoundError('assets/css/style.css not found. Run from the repository root.')
if not html_path.exists():
    raise FileNotFoundError('publications.html not found. Run from the repository root.')

css = css_path.read_text(encoding='utf-8', errors='ignore')
html = html_path.read_text(encoding='utf-8', errors='ignore')

css = re.sub(
    r"/\* === Publications compact-left wider-preview layout v19 START === \*/.*?/\* === Publications compact-left wider-preview layout v19 END === \*/",
    "",
    css,
    flags=re.S,
)

html = re.sub(r'(\bdecoding="async")\s+Visual summary for[^>]*', r'\1', html)
html = re.sub(r'\s+Visual summary for [^>]+(?=></div>)', '', html)

css_block = r"""
/* === Publications compact-left wider-preview layout v19 START === */
.publication-card,
.pub-visual-card {
  display: grid !important;
  grid-template-columns: minmax(0, 0.54fr) minmax(430px, 0.46fr) !important;
  gap: clamp(1.15rem, 2vw, 2rem) !important;
  align-items: start !important;
  padding: clamp(1.2rem, 2vw, 1.9rem) !important;
}

.pub-content,
.pub-card-main,
.publication-info,
.pub-visual-main {
  min-width: 0 !important;
  max-width: 100% !important;
}

.publication-card h2,
.pub-visual-card h2,
.pub-title {
  font-size: clamp(1.15rem, 1.65vw, 1.58rem) !important;
  line-height: 1.22 !important;
  letter-spacing: -0.025em !important;
  margin-top: 0.45rem !important;
  margin-bottom: 0.65rem !important;
}

.pub-meta-line,
.pub-year-type,
.pub-authors,
.publication-authors {
  font-size: clamp(0.9rem, 1vw, 1.02rem) !important;
  line-height: 1.45 !important;
  margin-bottom: 0.55rem !important;
}

.pub-badges,
.pub-meta-badges,
.publication-badges {
  gap: 0.45rem !important;
  margin: 0.65rem 0 !important;
}

.pub-badge,
.pub-pill,
.publication-badge,
.pub-metric-badge,
.pub-doi-badge {
  font-size: clamp(0.72rem, 0.85vw, 0.86rem) !important;
  padding: 0.34rem 0.58rem !important;
  line-height: 1.15 !important;
  border-radius: 999px !important;
}

.pub-insight-box,
.pub-reading-lens,
.pub-summary-box {
  padding: clamp(0.75rem, 1.2vw, 1.05rem) !important;
  margin: 0.8rem 0 !important;
  border-radius: 18px !important;
}

.pub-insight-box p,
.pub-reading-lens p,
.pub-summary-box p,
.pub-insight-text {
  font-size: clamp(0.86rem, 0.95vw, 0.98rem) !important;
  line-height: 1.5 !important;
  margin: 0 !important;
}

.pub-symbols,
.pub-symbol-grid {
  grid-template-columns: repeat(2, minmax(34px, 42px)) !important;
  gap: 0.4rem !important;
}

.pub-symbol,
.pub-symbols span {
  width: 38px !important;
  height: 38px !important;
  font-size: 1rem !important;
}

.pub-tags,
.publication-tags {
  gap: 0.4rem !important;
  margin-top: 0.75rem !important;
}

.pub-tags span,
.publication-tags span,
.keyword-chip {
  font-size: 0.72rem !important;
  line-height: 1.1 !important;
  padding: 0.28rem 0.5rem !important;
}

.pub-links,
.publication-links {
  gap: 0.55rem !important;
  margin-top: 0.85rem !important;
}

.pub-links a,
.publication-links a,
.pub-action-button {
  font-size: 0.82rem !important;
  padding: 0.55rem 0.8rem !important;
  border-radius: 14px !important;
}

.pub-visual,
.pub-card-visual,
.publication-visual,
.pub-preview-column {
  align-self: start !important;
  justify-self: stretch !important;
  width: 100% !important;
  min-width: 0 !important;
  max-width: none !important;
  display: flex !important;
  justify-content: center !important;
}

.pub-visual-frame,
.pub-preview-true-40-frame,
.pub-a4-wide-frame,
.pub-final-a4-thumb-frame,
.pub-compact-a4-frame,
.pub-a4-page-frame,
.pub-final-a4-frame,
.pub-a4-wide-preview-frame {
  width: min(100%, 620px) !important;
  max-width: 620px !important;
  min-width: min(100%, 430px) !important;
  aspect-ratio: 210 / 297 !important;
  height: auto !important;
  min-height: 0 !important;
  padding: clamp(10px, 1vw, 16px) !important;
  border-radius: 30px !important;
  overflow: hidden !important;
  background: linear-gradient(180deg, #f7fbff 0%, #eef5fb 100%) !important;
  border: 1px solid rgba(118, 155, 190, 0.24) !important;
  box-shadow: 0 18px 40px rgba(20, 48, 82, 0.12) !important;
}

.pub-visual-frame img,
.pub-preview-true-40-frame img,
.pub-a4-wide-frame img,
.pub-final-a4-thumb-frame img,
.pub-compact-a4-frame img,
.pub-a4-page-frame img,
.pub-final-a4-frame img,
.pub-a4-wide-preview-frame img {
  display: block !important;
  width: 100% !important;
  height: 100% !important;
  max-width: none !important;
  max-height: none !important;
  object-fit: contain !important;
  object-position: top center !important;
  border-radius: 20px !important;
  background: #ffffff !important;
}

@media (max-width: 1300px) {
  .publication-card,
  .pub-visual-card {
    grid-template-columns: minmax(0, 0.58fr) minmax(380px, 0.42fr) !important;
  }
  .pub-visual-frame,
  .pub-preview-true-40-frame,
  .pub-a4-wide-frame,
  .pub-final-a4-thumb-frame,
  .pub-compact-a4-frame,
  .pub-a4-page-frame,
  .pub-final-a4-frame,
  .pub-a4-wide-preview-frame {
    width: min(100%, 520px) !important;
    max-width: 520px !important;
    min-width: min(100%, 360px) !important;
  }
}

@media (max-width: 980px) {
  .publication-card,
  .pub-visual-card {
    grid-template-columns: 1fr !important;
  }
  .pub-visual,
  .pub-card-visual,
  .publication-visual,
  .pub-preview-column {
    justify-content: center !important;
  }
  .pub-visual-frame,
  .pub-preview-true-40-frame,
  .pub-a4-wide-frame,
  .pub-final-a4-thumb-frame,
  .pub-compact-a4-frame,
  .pub-a4-page-frame,
  .pub-final-a4-frame,
  .pub-a4-wide-preview-frame {
    width: min(100%, 420px) !important;
    max-width: 420px !important;
    min-width: 0 !important;
  }
}
/* === Publications compact-left wider-preview layout v19 END === */
"""

css = css.rstrip() + "\n\n" + css_block.strip() + "\n"
css_path.write_text(css, encoding='utf-8')
html_path.write_text(html, encoding='utf-8')

print('Done: compacted left publication text and enlarged the right A4-ratio first-page preview area (v19).')
