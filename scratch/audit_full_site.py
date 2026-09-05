import os
import glob
import re
import xml.etree.ElementTree as ET

site_dir = '/Users/user/.gemini/antigravity/scratch/ill-homepage'
html_files = glob.glob(os.path.join(site_dir, '**/*.html'), recursive=True)
html_files = [f for f in html_files if 'node_modules' not in f and '.git' not in f]

errors = []
warnings = []

print(f'Checking {len(html_files)} HTML files...')

for filepath in html_files:
    rel_path = os.path.relpath(filepath, site_dir)
    with open(filepath, 'r', encoding='utf-8', errors='ignore') as f:
        content = f.read()

    # 1. Check title tag
    if not re.search(r'<title>(.*?)</title>', content, re.IGNORECASE | re.DOTALL):
        errors.append(f'[{rel_path}] Missing <title> tag')

    # 2. Check meta description
    if not re.search(r'<meta\s+name=["\']description["\']', content, re.IGNORECASE):
        warnings.append(f'[{rel_path}] Missing meta description')

    # 3. Check canonical URL
    if not re.search(r'<link\s+rel=["\']canonical["\']', content, re.IGNORECASE):
        warnings.append(f'[{rel_path}] Missing canonical URL')

    # 4. Check for broken unreplaced template placeholders
    if '{{' in content or '}}' in content:
        errors.append(f'[{rel_path}] Contains unreplaced template placeholder')

    if 'src="undefined"' in content or 'href="undefined"' in content:
        errors.append(f'[{rel_path}] Contains undefined href/src attribute')

    # 5. Check SVG linearGradient IDs uniqueness within file
    svg_grad_ids = re.findall(r'<linearGradient\s+id=["\']([^"\']+)["\']', content)
    if len(svg_grad_ids) != len(set(svg_grad_ids)):
        errors.append(f'[{rel_path}] Duplicate linearGradient IDs within file: {svg_grad_ids}')

    # 6. Check internal href links target files exist
    hrefs = re.findall(r'href=["\']([^"\']+)["\']', content)
    for href in hrefs:
        if href.startswith('http://') or href.startswith('https://') or href.startswith('#') or href.startswith('mailto:') or href.startswith('tel:'):
            continue
        clean_href = href.split('?')[0].split('#')[0]
        if not clean_href:
            continue
        
        # Resolve target path
        if clean_href.startswith('/'):
            target_path = os.path.normpath(os.path.join(site_dir, clean_href.lstrip('/')))
        else:
            file_dir = os.path.dirname(filepath)
            target_path = os.path.normpath(os.path.join(file_dir, clean_href))
        
        if not os.path.exists(target_path):
            if not (os.path.isdir(target_path) and os.path.exists(os.path.join(target_path, 'index.html'))):
                errors.append(f'[{rel_path}] Broken internal link: href="{href}" (Target non-existent: {os.path.relpath(target_path, site_dir)})')

    # 7. For column articles, verify H2 heading formatting and TOC anchor IDs
    if rel_path.startswith('column/') and rel_path != 'column/index.html':
        toc_anchors = re.findall(r'href=["\'](#sec-[^"\']+)["\']', content)
        for anchor in set(toc_anchors):
            anchor_id = anchor[1:]
            if f'id="{anchor_id}"' not in content and f"id='{anchor_id}'" not in content:
                errors.append(f'[{rel_path}] TOC link {anchor} has no matching id="{anchor_id}"')

        if '<script type="application/ld+json">' not in content:
            warnings.append(f'[{rel_path}] Missing JSON-LD script tag')

# 8. Audit sitemap.xml
sitemap_path = os.path.join(site_dir, 'sitemap.xml')
if os.path.exists(sitemap_path):
    with open(sitemap_path, 'r', encoding='utf-8') as f:
        sitemap_content = f.read()
    urls_in_sitemap = re.findall(r'<loc>(.*?)</loc>', sitemap_content)
    print(f'Checking {len(urls_in_sitemap)} URLs in sitemap.xml...')
    for u in urls_in_sitemap:
        if u.startswith('https://ill-inc.net/'):
            path_part = u.replace('https://ill-inc.net/', '')
            if not path_part or path_part == '/':
                local_file = os.path.join(site_dir, 'index.html')
            else:
                local_file = os.path.normpath(os.path.join(site_dir, path_part))
            if not os.path.exists(local_file):
                if not (os.path.isdir(local_file) and os.path.exists(os.path.join(local_file, 'index.html'))):
                    errors.append(f'[sitemap.xml] URL points to non-existent file: {u}')

print(f'\n--- AUDIT SUMMARY ---')
print(f'Total Errors: {len(errors)}')
print(f'Total Warnings: {len(warnings)}')

if errors:
    print('\nERRORS FOUND:')
    for err in errors:
        print('  - ', err)

if warnings:
    print('\nWARNINGS FOUND:')
    for warn in warnings:
        print('  - ', warn)
