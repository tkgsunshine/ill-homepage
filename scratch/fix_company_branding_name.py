import os
import glob
import re

site_dir = '/Users/user/.gemini/antigravity/scratch/ill-homepage'

all_files = glob.glob(os.path.join(site_dir, '**/*.html'), recursive=True) + \
            glob.glob(os.path.join(site_dir, 'scripts/**/*.*'), recursive=True) + \
            glob.glob(os.path.join(site_dir, 'REGULATIONS.md'))

forbidden_pattern = re.compile(r'株式会社イル')

modified_files = []

for filepath in all_files:
    if 'node_modules' in filepath or '.git' in filepath:
        continue
    # Skip regulations.md rule quote lines where "株式会社イルの使用は絶対禁止" is mentioned
    with open(filepath, 'r', encoding='utf-8', errors='ignore') as f:
        content = f.read()

    if '株式会社イル' in content:
        # If REGULATIONS.md, don't replace the prohibition note
        if os.path.basename(filepath) == 'REGULATIONS.md':
            new_content = content.replace('「株式会社イル」の使用は絶対禁止', '[[PROHIBITED_QUOTE_TOKEN]]')
            new_content = new_content.replace('株式会社イル', 'Ill（イル）株式会社')
            new_content = new_content.replace('[[PROHIBITED_QUOTE_TOKEN]]', '「株式会社イル」の使用は絶対禁止')
        else:
            new_content = content.replace('株式会社イル', 'Ill（イル）株式会社')

        if new_content != content:
            with open(filepath, 'w', encoding='utf-8') as f:
                f.write(new_content)
            modified_files.append(os.path.relpath(filepath, site_dir))

print(f"Fixed company branding in {len(modified_files)} files!")
for mf in modified_files[:10]:
    print("  - ", mf)
