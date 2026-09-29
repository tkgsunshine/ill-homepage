import glob
import re

files = sorted(glob.glob('column/*.html'))
print(f'Checking {len(files)-1} column articles for duplicate TOCs...')

cleaned = 0
for f in files:
    if 'index.html' in f:
        continue
    with open(f, 'r', encoding='utf-8') as fp:
        c = fp.read()
    
    orig = c
    
    # Check if there is a rogue partial TOC before the intro paragraph
    # Pattern: <main class="article-body">\s*(?:<!-- Table of Contents -->\s*)?<ul class="toc-list">.*?</ul>\s*</div>
    c = re.sub(
        r'(<main class="article-body">\s*)(?:<!-- Table of Contents -->\s*)?<ul class="toc-list">.*?</ul>\s*</div>\s*',
        r'\1',
        c,
        flags=re.DOTALL
    )
    
    # Also clean if it's wrapped in a half div
    c = re.sub(
        r'(<main class="article-body">\s*)<!-- Table of Contents -->\s*',
        r'\1',
        c
    )
    
    if c != orig:
        cleaned += 1
        with open(f, 'w', encoding='utf-8') as fp:
            fp.write(c)

print(f'Cleaned duplicate/broken TOCs in {cleaned} files.')
