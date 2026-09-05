import os
import re

site_dir = '/Users/user/.gemini/antigravity/scratch/ill-homepage'
css_path = os.path.join(site_dir, 'style.css')

with open(css_path, 'r', encoding='utf-8') as f:
    css = f.read()

# 1. Add global media resets near top (after *, *::before, *::after)
global_reset_target = "*, *::before, *::after {\n  box-sizing: border-box;\n  margin: 0;\n  padding: 0;\n}"
global_reset_replacement = """*, *::before, *::after {
  box-sizing: border-box;
  margin: 0;
  padding: 0;
}

img, svg, video, canvas, iframe {
  max-width: 100%;
  height: auto;
  vertical-align: middle;
}

h1, h2, h3, h4, h5, h6, p, a, span, li, td, th {
  overflow-wrap: break-word;
  word-break: break-word;
}

pre, code {
  max-width: 100%;
  overflow-x: auto;
  white-space: pre-wrap;
  word-break: break-all;
}"""

if global_reset_target in css:
    css = css.replace(global_reset_target, global_reset_replacement)
    print("Injected global responsive reset rules successfully.")

# 2. Append comprehensive responsive design system to end of file if not present
responsive_block = """

/* --- COMPREHENSIVE RESPONSIVE DESIGN SYSTEM OVERRIDES --- */

/* Tablet & Mobile Layout Enhancements (<= 768px) */
@media (max-width: 768px) {
  .container {
    padding: 0 1.6rem;
  }

  .section {
    padding: 4rem 0;
  }

  .section-header {
    margin-bottom: 4rem;
  }

  .section-title {
    font-size: clamp(2.4rem, 6vw, 3.6rem);
  }

  .hero-title {
    font-size: clamp(2.8rem, 7vw, 4.8rem);
    line-height: 1.25;
  }

  .article-layout {
    grid-template-columns: 1fr;
    gap: 3.2rem;
  }

  .article-main-visual {
    height: auto;
    aspect-ratio: 16/9;
  }

  .article-title {
    font-size: clamp(2.2rem, 5.5vw, 3.2rem);
    line-height: 1.35;
  }

  .article-body h2 {
    font-size: clamp(1.9rem, 4.5vw, 2.4rem);
    margin: 3.6rem 0 1.8rem 0;
  }

  .article-body h3 {
    font-size: clamp(1.6rem, 3.8vw, 2rem);
    margin: 2.8rem 0 1.4rem 0;
  }

  .toc-box {
    padding: 2rem 1.6rem;
    margin-bottom: 3.2rem;
  }

  .toc-title {
    font-size: 1.6rem;
  }

  .inline-cta {
    padding: 2.8rem 1.8rem;
    margin-top: 4rem;
  }

  .inline-cta-title {
    font-size: clamp(1.8rem, 4.5vw, 2.2rem);
  }

  .inline-cta-desc {
    font-size: 1.4rem;
    margin-bottom: 2.4rem;
  }

  .table-wrapper,
  .article-table-wrapper {
    margin: 2rem 0;
    max-width: 100%;
    overflow-x: auto;
    -webkit-overflow-scrolling: touch;
  }

  .article-table {
    min-width: 540px;
    font-size: 1.4rem;
  }

  .article-table th, 
  .article-table td {
    padding: 1.2rem 1.4rem;
  }
}

/* Small Smartphone Screen Enhancements (<= 480px) */
@media (max-width: 480px) {
  html {
    font-size: 58%; /* 1rem = 5.8px for responsive font scaling on 320px-375px screens */
  }

  .container {
    padding: 0 1.2rem;
  }

  .btn {
    padding: 1.4rem 2rem;
    font-size: 1.4rem;
    width: 100%;
    text-align: center;
  }

  .btn-group,
  .hero-buttons,
  .inline-cta-buttons {
    flex-direction: column;
    width: 100%;
    gap: 1.2rem;
  }

  .card-grid,
  .column-grid,
  .blog-grid {
    grid-template-columns: 1fr;
    gap: 1.8rem;
  }

  .toc-list li {
    font-size: 1.4rem;
  }

  .sidebar-box {
    padding: 1.8rem 1.4rem;
  }
}
"""

if "COMPREHENSIVE RESPONSIVE DESIGN SYSTEM OVERRIDES" not in css:
    css += responsive_block
    print("Appended responsive overrides to style.css successfully.")

with open(css_path, 'w', encoding='utf-8') as f:
    f.write(css)

print("Updated style.css with responsive design enhancements!")
