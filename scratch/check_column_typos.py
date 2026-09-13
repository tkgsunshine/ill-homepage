import os
import glob
import re

site_dir = '/Users/user/.gemini/antigravity/scratch/ill-homepage'
column_dir = os.path.join(site_dir, 'column')
html_files = glob.glob(os.path.join(column_dir, '*.html'))

print(f"Scanning {len(html_files)} column files for typos and content anomalies...")

anomalies = []

for filepath in html_files:
    rel_path = os.path.relpath(filepath, site_dir)
    with open(filepath, 'r', encoding='utf-8', errors='ignore') as f:
        content = f.read()

    # 1. Search for strange ending characters like 'ます[漢字]？' or 'です[漢字]？'
    matches = re.findall(r'(?:ます|です|可能|でき)([一-龠ぁ-んァ-ヶa-zA-Z0-9])？', content)
    for m in matches:
        if m not in ['か', 'の', 'ん', 'ね', 'よ']:
            # Find surrounding context
            idx = content.find(m + '？')
            snippet = content[max(0, idx-30):min(len(content), idx+30)].replace('\n', ' ')
            anomalies.append(f"[{rel_path}] Strange ending character '{m}？' in: ...{snippet}...")

    # 2. Search for repeated punctuation or typos
    typos = re.findall(r'(?:？？|！！|ですです|ますます|かか？|か？か|{{|}})', content)
    for t in set(typos):
        if t in ['{{', '}}']:
            anomalies.append(f"[{rel_path}] Template placeholder tag: {t}")
        elif t in ['ですです', 'ますます', 'かか？', 'か？か']:
            anomalies.append(f"[{rel_path}] Repeated word/punctuation typo: {t}")

    # 3. Search for placeholder texts
    placeholders = ['undefined', 'null', '[object Object]', 'TODO', 'FIXME', 'ダミー', 'テスト本文']
    for p in placeholders:
        if p in content:
            anomalies.append(f"[{rel_path}] Found placeholder text: {p}")

print(f"\n--- TYPO & ANOMALY SCAN SUMMARY ---")
print(f"Total Anomalies Found: {len(anomalies)}")

if anomalies:
    print("\nANOMALIES:")
    for a in anomalies:
        print("  - ", a)
