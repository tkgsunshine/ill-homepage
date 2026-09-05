import os
import re

site_dir = '/Users/user/.gemini/antigravity/scratch/ill-homepage'
css_path = os.path.join(site_dir, 'style.css')

with open(css_path, 'r', encoding='utf-8') as f:
    css_content = f.read()

print(f'Length of style.css: {len(css_content)} bytes')

# Extract media queries
media_queries = re.findall(r'@media[^{]+\{', css_content)
print('\nMedia queries found in style.css:')
for mq in media_queries:
    print('  - ', mq.strip())

# Check responsive safeguards in CSS:
checks = {
    'img responsive max-width': r'img\s*\{[^}]*max-width:\s*100%',
    'svg responsive max-width': r'svg\s*\{[^}]*max-width:\s*100%',
    'table responsive wrapper/overflow': r'table\s*\{[^}]*overflow|overflow-x',
    'pre/code responsive overflow': r'pre\s*\{[^}]*overflow|word-break|white-space',
    'viewport meta tag in html': None
}

print('\nAutomated responsive CSS rule checks:')
for check_name, pattern in checks.items():
    if pattern:
        match = re.search(pattern, css_content, re.IGNORECASE)
        print(f"  [{'OK' if match else 'MISSING'}] {check_name}")

# Check HTML files for viewport meta tag and element overflow risks
import glob
html_files = glob.glob(os.path.join(site_dir, '**/*.html'), recursive=True)
html_files = [f for f in html_files if 'node_modules' not in f and '.git' not in f]

missing_viewport = []
table_without_wrapper = []

for filepath in html_files:
    rel_path = os.path.relpath(filepath, site_dir)
    with open(filepath, 'r', encoding='utf-8', errors='ignore') as f:
        content = f.read()

    # Check viewport meta tag
    if not re.search(r'<meta\s+name=["\']viewport["\']\s+content=["\'][^"\']*width=device-width', content, re.IGNORECASE):
        missing_viewport.append(rel_path)

    # Check tables for responsive wrappers or overflow container
    tables = re.findall(r'<table.*?>.*?</table>', content, re.DOTALL)
    for table in tables:
        # Check if table is wrapped in a container with overflow or table-wrapper class
        if '<div class="table-wrapper"' not in content and '<div class="table-container"' not in content and 'overflow-x' not in css_content:
            table_without_wrapper.append(rel_path)
            break

print(f"\nHTML files missing viewport meta tag: {len(missing_viewport)}")
if missing_viewport:
    for f in missing_viewport[:5]:
        print('  - ', f)

print(f"HTML files with tables that might need responsive wrappers: {len(table_without_wrapper)}")
