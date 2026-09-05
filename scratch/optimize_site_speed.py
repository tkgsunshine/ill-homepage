import os
import glob
import re
import json

site_dir = '/Users/user/.gemini/antigravity/scratch/ill-homepage'

# 1. Update vercel.json with performance & caching headers
vercel_json_path = os.path.join(site_dir, 'vercel.json')
with open(vercel_json_path, 'r', encoding='utf-8') as f:
    vercel_data = json.load(f)

vercel_data['headers'] = [
    {
        "source": "/(.*).(css|js|svg|png|jpg|jpeg|gif|webp|woff2|ico)",
        "headers": [
            {
                "key": "Cache-Control",
                "value": "public, max-age=31536000, immutable"
            }
        ]
    },
    {
        "source": "/(.*)",
        "headers": [
            {
                "key": "X-Content-Type-Options",
                "value": "nosniff"
            },
            {
                "key": "X-Frame-Options",
                "value": "SAMEORIGIN"
            },
            {
                "key": "X-XSS-Protection",
                "value": "1; mode=block"
            }
        ]
    }
]

with open(vercel_json_path, 'w', encoding='utf-8') as f:
    json.dump(vercel_data, f, indent=2, ensure_ascii=False)
print("Updated vercel.json with HTTP Cache-Control & Security headers.")

# 2. Update HTML files for non-blocking Google Fonts and image decoding="async"
html_files = glob.glob(os.path.join(site_dir, '**/*.html'), recursive=True)
html_files = [f for f in html_files if 'node_modules' not in f and '.git' not in f]

updated_font_count = 0
updated_img_count = 0

old_font_link = '<link href="https://fonts.googleapis.com/css2?family=Noto+Sans+JP:wght@400;500;700&family=Outfit:wght@400;500;600;700;800&display=swap" rel="stylesheet">'
new_font_link = '<link rel="preload" as="style" href="https://fonts.googleapis.com/css2?family=Noto+Sans+JP:wght@400;500;700&family=Outfit:wght@400;500;600;700;800&display=swap" onload="this.onload=null;this.rel=\'stylesheet\'">\n  <noscript><link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=Noto+Sans+JP:wght@400;500;700&family=Outfit:wght@400;500;600;700;800&display=swap"></noscript>'

for filepath in html_files:
    with open(filepath, 'r', encoding='utf-8', errors='ignore') as f:
        content = f.read()

    new_content = content

    # Optimize Google Fonts link to non-blocking async
    if old_font_link in new_content:
        new_content = new_content.replace(old_font_link, new_font_link)
        updated_font_count += 1

    # Add decoding="async" to <img> tags if missing
    def optimize_img(match):
        img_tag = match.group(0)
        if 'decoding=' not in img_tag:
            img_tag = img_tag.replace('<img ', '<img decoding="async" ')
        return img_tag

    new_content = re.sub(r'<img\s+[^>]+>', optimize_img, new_content)

    if new_content != content:
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(new_content)
        updated_img_count += 1

print(f"Optimized font loading in {updated_font_count} HTML files.")
print(f"Optimized image decoding in {updated_img_count} HTML files.")
