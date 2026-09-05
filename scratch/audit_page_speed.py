import os
import glob
import re

site_dir = '/Users/user/.gemini/antigravity/scratch/ill-homepage'
html_files = glob.glob(os.path.join(site_dir, '**/*.html'), recursive=True)
html_files = [f for f in html_files if 'node_modules' not in f and '.git' not in f]

print(f"Auditing {len(html_files)} HTML files for PageSpeed / Web Vitals metrics...")

lcp_missing_priority = []
images_missing_dimensions_or_lazy = []
render_blocking_scripts = []
missing_font_preconnect = []

for filepath in html_files:
    rel_path = os.path.relpath(filepath, site_dir)
    with open(filepath, 'r', encoding='utf-8', errors='ignore') as f:
        content = f.read()

    # 1. Check preconnect for Google Fonts
    if 'fonts.googleapis.com' in content or 'fonts.gstatic.com' in content:
        if '<link rel="preconnect" href="https://fonts.googleapis.com"' not in content:
            missing_font_preconnect.append(rel_path)

    # 2. Check for render-blocking <script src="..."> tags (missing async or defer)
    scripts = re.findall(r'<script\s+[^>]*src=["\']([^"\']+)["\'][^>]*>', content, re.IGNORECASE)
    for s in scripts:
        # Check full script tag
        script_tag = re.search(r'<script\s+[^>]*src=["\']' + re.escape(s) + r'["\'][^>]*>', content, re.IGNORECASE)
        if script_tag:
            tag_str = script_tag.group(0)
            if 'async' not in tag_str and 'defer' not in tag_str and 'type="module"' not in tag_str:
                render_blocking_scripts.append(f"[{rel_path}] {s}")

    # 3. Check <img> tags for loading="lazy" or fetchpriority
    imgs = re.findall(r'<img\s+[^>]+>', content, re.IGNORECASE)
    for img in imgs:
        if 'loading=' not in img:
            images_missing_dimensions_or_lazy.append(f"[{rel_path}] {img[:60]}...")

print(f"\n--- SPEED AUDIT SUMMARY ---")
print(f"Files missing font preconnect: {len(set(missing_font_preconnect))}")
print(f"Render blocking script tags: {len(render_blocking_scripts)}")
print(f"Images missing loading='lazy': {len(images_missing_dimensions_or_lazy)}")

if missing_font_preconnect:
    print("\nFiles missing preconnect (First 5):")
    for f in missing_font_preconnect[:5]:
        print("  - ", f)

if render_blocking_scripts:
    print("\nRender-blocking scripts (First 5):")
    for s in render_blocking_scripts[:5]:
        print("  - ", s)

if images_missing_dimensions_or_lazy:
    print("\nImages missing loading attribute (First 5):")
    for img in images_missing_dimensions_or_lazy[:5]:
        print("  - ", img)
