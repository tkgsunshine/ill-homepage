import os
import glob
import re

site_dir = '/Users/user/.gemini/antigravity/scratch/ill-homepage'

# 1. Update style.css with prominent checklist styling
css_path = os.path.join(site_dir, 'style.css')
with open(css_path, 'r', encoding='utf-8') as f:
    css = f.read()

checklist_css_override = """

/* --- CHECKLIST BOX FONT SIZE & STYLING OVERRIDES --- */
.article-body div[style*="background"],
.article-body .checklist-box {
  padding: 2.4rem !important;
  border-radius: 1.2rem !important;
  margin: 3.2rem 0 !important;
}

.article-body div[style*="background"] strong[style*="color"],
.article-body div[style*="background"] strong,
.checklist-title {
  font-size: clamp(1.7rem, 3.8vw, 1.9rem) !important;
  font-weight: 800 !important;
  margin-bottom: 1.4rem !important;
  display: block !important;
}

.article-body div[style*="background"] ul,
.article-body .checklist-box ul {
  font-size: clamp(1.45rem, 3.2vw, 1.6rem) !important;
  line-height: 1.8 !important;
  padding-left: 2.4rem !important;
}

.article-body div[style*="background"] li,
.article-body .checklist-box li {
  font-size: clamp(1.45rem, 3.2vw, 1.6rem) !important;
  margin-bottom: 1rem !important;
  line-height: 1.75 !important;
}
"""

if "CHECKLIST BOX FONT SIZE & STYLING OVERRIDES" not in css:
    css += checklist_css_override
    with open(css_path, 'w', encoding='utf-8') as f:
        f.write(css)
    print("Updated style.css with checklist font size overrides!")

# 2. Batch replace 'font-size: 0.95rem' across all files
target_files = glob.glob(os.path.join(site_dir, '**/*.html'), recursive=True) + glob.glob(os.path.join(site_dir, 'scripts/*.*'), recursive=True)

replaced_files = 0

for filepath in target_files:
    if 'node_modules' in filepath or '.git' in filepath:
        continue
    with open(filepath, 'r', encoding='utf-8', errors='ignore') as f:
        content = f.read()

    if 'font-size: 0.95rem' in content or 'font-size:0.95rem' in content:
        new_content = content.replace('font-size: 0.95rem', 'font-size: 1.5rem').replace('font-size:0.95rem', 'font-size: 1.5rem')
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(new_content)
        replaced_files += 1

print(f"Replaced 0.95rem inline font size in {replaced_files} files!")
