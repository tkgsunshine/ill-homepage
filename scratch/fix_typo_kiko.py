import os
import glob

site_dir = '/Users/user/.gemini/antigravity/scratch/ill-homepage'

target_files = [
    os.path.join(site_dir, 'scripts/editorial_calendar.json'),
    os.path.join(site_dir, 'column/020-c2c-sharing-matching-platform-development.html'),
    os.path.join(site_dir, 'column/035-c2c-sharing-matching-platform-development.html')
]

fixed_count = 0

for filepath in target_files:
    if os.path.exists(filepath):
        with open(filepath, 'r', encoding='utf-8') as f:
            content = f.read()

        if '自動化できます起？' in content:
            new_content = content.replace('自動化できます起？', '自動化できますか？')
            with open(filepath, 'w', encoding='utf-8') as f:
                f.write(new_content)
            fixed_count += 1
            print(f"Fixed typo in: {os.path.relpath(filepath, site_dir)}")

print(f"Total files fixed: {fixed_count}")
