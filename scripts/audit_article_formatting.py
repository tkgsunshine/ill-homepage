import glob
import re
import os

files = sorted(glob.glob('column/*.html'))
print(f'Inspecting {len(files)-1} column articles...')

issues = {}
for f in files:
    if 'index.html' in f:
        continue
    with open(f, 'r', encoding='utf-8') as fp:
        c = fp.read()
    
    file_issues = []
    
    # 1. Check duplicate or broken TOC
    if '<ul class="toc-list">\n            </ul>' in c or '<ul class="toc-list"></ul>' in c or '<!-- Table of Contents -->\n          \n            <ul' in c:
        file_issues.append('Empty/broken TOC tag')
    
    toc_boxes = re.findall(r'<div class="toc-box">', c)
    if len(toc_boxes) > 1:
        file_issues.append(f'Multiple TOC boxes ({len(toc_boxes)})')
    
    # 2. Check raw markdown backticks
    if re.search(r'`[^`]+`', c):
        file_issues.append('Raw markdown backticks')
        
    # 3. Check if body length is short (< 4500 chars)
    body_match = re.search(r'<main class="article-body">(.*?)</main>', c, re.DOTALL)
    if body_match:
        body_len = len(body_match.group(1).strip())
        if body_len < 4500:
            file_issues.append(f'Short article body ({body_len} chars)')
            
    # 4. Check if missing FAQ section
    if 'class="faq-container"' not in c and 'id="section-faq"' not in c and 'id="faq"' not in c:
        file_issues.append('Missing FAQ section')
    
    if file_issues:
        issues[f] = file_issues

print(f'Total articles with potential formatting/quality issues: {len(issues)}')
for f, iss in issues.items():
    print(f'{f}: {", ".join(iss)}')
