import glob
import re

files = sorted(glob.glob('column/*.html'))
print(f'Processing {len(files)-1} column articles...')

cleaned_toc = 0
fixed_markdown = 0

for f in files:
    if 'index.html' in f:
        continue
    with open(f, 'r', encoding='utf-8') as fp:
        c = fp.read()
    
    orig = c
    
    # 1. Remove empty/broken TOC block at top of body
    c = re.sub(r'<!-- Table of Contents -->\s*<ul class="toc-list">\s*</ul>\s*</div>\s*', '', c)
    
    # 2. Fix raw markdown bold **text** -> <strong>text</strong>
    c = re.sub(r'\*\*(.*?)\*\*', r'<strong>\1</strong>', c)
    
    # 3. Fix raw markdown inline code `code` -> <code>code</code>
    c = re.sub(r'`([^`]+)`', r'<code>\1</code>', c)
    
    if c != orig:
        if '<!-- Table of Contents -->' in orig and '<!-- Table of Contents -->' not in c:
            cleaned_toc += 1
        fixed_markdown += 1
        with open(f, 'w', encoding='utf-8') as fp:
            fp.write(c)

print(f'Cleaned broken TOC in {cleaned_toc} files, updated markdown in {fixed_markdown} files.')
