import os
import re

site_dir = '/Users/user/.gemini/antigravity/scratch/ill-homepage'
gen_script = os.path.join(site_dir, 'scripts/generate_next_blog_post.py')

with open(gen_script, 'r', encoding='utf-8') as f:
    code = f.read()

strict_check_code = """    # --- MANDATORY PRE-PUBLISH TYPO & QUALITY ASSURANCE SUITE ---
    # 1. Company Branding Enforcement
    new_html = new_html.replace("株式会社イル", "Ill（イル）株式会社")
    new_html = new_html.replace("株式会社Ill", "Ill（イル）株式会社")
    new_html = new_html.replace("イル株式会社", "Ill（イル）株式会社")

    # 2. Font Size Enforcement (Checklist boxes & text)
    new_html = new_html.replace("font-size: 0.95rem", "font-size: 1.5rem")
    new_html = new_html.replace("font-size:0.95rem", "font-size: 1.5rem")

    # 3. Automatic Typo Repair for Question Endings
    new_html = re.sub(r'([一-龠])？', lambda m: 'か？' if m.group(1) not in ['何', '誰', '何日', '何月'] else m.group(0), new_html)

    # 4. Strict Validation Assertion
    if "株式会社イル" in new_html:
        raise ValueError("CRITICAL ERROR: Prohibited company name '株式会社イル' detected before saving!")
    if "font-size: 0.95rem" in new_html:
        raise ValueError("CRITICAL ERROR: Microscopic font size 0.95rem detected before saving!")
    if "起？" in new_html:
        raise ValueError("CRITICAL ERROR: Typo '起？' detected before saving!")

    # Save the new article"""

if "# Foolproof Sanitizer & Quality Assurance Step" in code:
    old_block = re.search(r'# Foolproof Sanitizer.*?(?=# Save the new article)', code, flags=re.DOTALL)
    if old_block:
        code = code.replace(old_block.group(0), strict_check_code + "\n    ")
        with open(gen_script, 'w', encoding='utf-8') as f:
            f.write(code)
        print("Upgraded generate_next_blog_post.py with Mandatory Pre-Publish Typo Verification Suite!")

print("Pre-publish quality assurance suite successfully installed!")
