import os

site_dir = '/Users/user/.gemini/antigravity/scratch/ill-homepage'

# Update scripts/generate_next_blog_post.py
gen_script = os.path.join(site_dir, 'scripts/generate_next_blog_post.py')

with open(gen_script, 'r', encoding='utf-8') as f:
    code = f.read()

sanitizer_code = """    # Foolproof Sanitizer & Quality Assurance Step
    new_html = new_html.replace("株式会社イル", "Ill（イル）株式会社")
    new_html = new_html.replace("font-size: 0.95rem", "font-size: 1.5rem")
    new_html = new_html.replace("font-size:0.95rem", "font-size: 1.5rem")
    new_html = new_html.replace("起？", "か？")

    # Save the new article"""

if "# Save the new article" in code and "Foolproof Sanitizer" not in code:
    code = code.replace("# Save the new article", sanitizer_code)
    with open(gen_script, 'w', encoding='utf-8') as f:
        f.write(code)
    print("Injected Foolproof Sanitizer into generate_next_blog_post.py!")

# Also check scripts/apply_seo_optimizations.py
seo_script = os.path.join(site_dir, 'scripts/apply_seo_optimizations.py')
if os.path.exists(seo_script):
    with open(seo_script, 'r', encoding='utf-8') as f:
        seo_code = f.read()
    if "株式会社イル" in seo_code:
        seo_code = seo_code.replace("株式会社イル", "Ill（イル）株式会社")
        with open(seo_script, 'w', encoding='utf-8') as f:
            f.write(seo_code)
        print("Replaced company name in apply_seo_optimizations.py!")

print("Quality assurance safeguards added to auto-generator pipeline!")
