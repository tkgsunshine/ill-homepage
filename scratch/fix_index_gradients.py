import os
import re

site_dir = '/Users/user/.gemini/antigravity/scratch/ill-homepage'

for filename in ['index.html', 'column/index.html']:
    filepath = os.path.join(site_dir, filename)
    if not os.path.exists(filepath):
        continue
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()

    # Find all inline SVGs in the page and assign unique gradient IDs for bg-grad and text-grad if duplicate
    card_counter = [0]
    
    def fix_svg_gradients(match):
        svg_code = match.group(0)
        card_counter[0] += 1
        cid = card_counter[0]
        
        # Replace generic linearGradient id="bg-grad" / url(#bg-grad)
        svg_code = re.sub(r'id=["\']bg-grad["\']', f'id="bg-grad-idx-{cid}"', svg_code)
        svg_code = re.sub(r'url\(#bg-grad\)', f'url(#bg-grad-idx-{cid})', svg_code)
        
        # Replace generic linearGradient id="text-grad" / url(#text-grad)
        svg_code = re.sub(r'id=["\']text-grad["\']', f'id="text-grad-idx-{cid}"', svg_code)
        svg_code = re.sub(r'url\(#text-grad\)', f'url(#text-grad-idx-{cid})', svg_code)
        
        return svg_code

    new_content = re.sub(r'<svg.*?</svg>', fix_svg_gradients, content, flags=re.DOTALL)
    
    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(new_content)

print("Fixed inline SVG gradient IDs in index.html and column/index.html!")
