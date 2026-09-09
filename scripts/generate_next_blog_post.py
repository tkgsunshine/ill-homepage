import os
import re
import json
import datetime
import subprocess
import sys
import time

SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
WORKSPACE_DIR = os.path.dirname(SCRIPT_DIR)
COLUMN_DIR = os.path.join(WORKSPACE_DIR, "column")
CALENDAR_PATH = os.path.join(SCRIPT_DIR, "editorial_calendar.json")
TEMPLATE_PATH = os.path.join(COLUMN_DIR, "history-and-difference-of-generative-ai.html")

sys.path.insert(0, SCRIPT_DIR)
from topic_enrichment_data import get_best_config

def main():
    print("Executing generate_next_blog_post.py...")
    
    force_run = "--force" in sys.argv
    if not force_run:
        try:
            res = subprocess.run(
                ["git", "log", "-1", "--format=%ct", "--", COLUMN_DIR],
                capture_output=True,
                text=True,
                check=True
            )
            last_commit_ts = int(res.stdout.strip())
            elapsed_seconds = time.time() - last_commit_ts
            # Guard window: 2.5 hours (9000 seconds)
            if elapsed_seconds < 9000:
                elapsed_min = int(elapsed_seconds / 60)
                print(f"Notice: A column commit occurred {elapsed_min} minutes ago in column/. Skipping duplicate generation for this retry window.")
                return

            # Also check if any file in COLUMN_DIR was created/modified in the last 15 minutes (uncommitted run)
            current_time = time.time()
            for fn in os.listdir(COLUMN_DIR):
                if fn.endswith(".html") and fn != "index.html":
                    fpath = os.path.join(COLUMN_DIR, fn)
                    if (current_time - os.path.getmtime(fpath)) < 900:
                        print(f"Notice: File {fn} was generated {int((current_time - os.path.getmtime(fpath))/60)} minutes ago. Skipping duplicate generation.")
                        return
        except Exception as e:
            print(f"Warning: Could not check git commit timestamp: {e}")
    
    if not os.path.exists(CALENDAR_PATH):
        print(f"Error: Editorial calendar not found at {CALENDAR_PATH}")
        return
        
    with open(CALENDAR_PATH, "r", encoding="utf-8") as f:
        calendar = json.load(f)
        
    target_post = None
    for post in calendar:
        filename = post["filename"]
        filepath = os.path.join(COLUMN_DIR, filename)
        if not os.path.exists(filepath):
            target_post = post
            break
            
    if not target_post:
        print("No new articles to generate in the editorial calendar. All posts are already created!")
        return
        
    print(f"Found next planned article: {target_post['filename']}")
    
    # Read template
    with open(TEMPLATE_PATH, "r", encoding="utf-8") as f:
        template = f.read()
        
    # Generate dates (using today's date)
    today = datetime.date.today()
    period_date = today.strftime('%Y.%m.%d')
    iso_date = today.strftime('%Y-%m-%d')
    
    # Build TOC items and body HTML
    toc_items = []
    sections_html = ""
    for idx, sec in enumerate(target_post["body_sections"], start=1):
        sec_id = f"sec-{idx}"
        toc_items.append(f'              <li><a href="#{sec_id}">{sec["h2"]}</a></li>')
        sections_html += f'\n          <h2 id="{sec_id}">{sec["h2"]}</h2>\n          {sec["text"]}\n'

    # Inject rich pricing table & SIer comparison section
    cfg = get_best_config(target_post["filename"], target_post["title"] + " " + target_post.get("description", ""))
    sec_pricing_id = "sec-pricing-table"
    toc_items.append(f'              <li><a href="#{sec_pricing_id}">{cfg["h2_title"]}</a></li>')
    sections_html += f'''
          <h2 id="{sec_pricing_id}">{cfg['h2_title']}</h2>
          <p>システム開発を検討する際、最も気になるのが「実際の費用相場」と「どこにコストがかかっているのか」という内訳です。以下の表は、一般的な受託開発会社・大手SIerと、<strong>Ill（イル）株式会社</strong> のミニマル設計による概算費用の比較です。</p>
          {cfg['table_html']}
          {cfg['explanation_html']}
'''

    # Combine questions with extra topic FAQs
    all_questions = list(target_post.get("questions", []))
    for eq_q, eq_a in cfg.get("extra_faqs", []):
        all_questions.append({"q": eq_q, "a": eq_a})

    if all_questions:
        toc_items.append('              <li><a href="#section-faq">よくある質問</a></li>')
        sections_html += '\n          <h2 id="section-faq">よくある質問</h2>\n          <div class="faq-container">\n'
        for qa in all_questions:
            sections_html += f'            <div class="faq-item">\n              <h3>{qa["q"]}</h3>\n              <p>{qa["a"]}</p>\n            </div>\n'
        sections_html += '          </div>\n'

    toc_box_html = '\n          <div class="toc-box">\n            <div class="toc-title">目次</div>\n            <ul class="toc-list">\n' + '\n'.join(toc_items) + '\n            </ul>\n          </div>\n'
    body_html = toc_box_html + sections_html
        
    # Generate custom SVG banner (Premium Light Slate Style - Single Line)
    summary_text = f"{target_post['title_line2']}がわかる" if not target_post['title_line2'].endswith("わかる") else target_post['title_line2']
    font_size = 38
    if len(summary_text) > 26:
        font_size = 32
        
    banner_svg = f"""<svg viewBox="0 0 1000 428" fill="none" xmlns="http://www.w3.org/2000/svg">
          <defs>
            <linearGradient id="bg-grad" x1="0" y1="0" x2="1000" y2="428" gradientUnits="userSpaceOnUse">
              <stop stop-color="#F1F5F9" />
              <stop offset="0.5" stop-color="#E2E8F0" />
              <stop offset="1" stop-color="#CBD5E1" />
            </linearGradient>
            <linearGradient id="text-grad" x1="0" y1="0" x2="800" y2="0" gradientUnits="userSpaceOnUse">
              <stop stop-color="#0EA5E9" />
              <stop offset="1" stop-color="#10B981" />
            </linearGradient>
          </defs>
          <rect width="1000" height="428" fill="url(#bg-grad)"/>
          
          <!-- Decorative Grid/Dots -->
          <circle cx="100" cy="80" r="1.5" fill="#0EA5E9" opacity="0.15"/>
          <circle cx="200" cy="80" r="1.5" fill="#0EA5E9" opacity="0.15"/>
          <circle cx="300" cy="80" r="1.5" fill="#0EA5E9" opacity="0.15"/>
          <circle cx="400" cy="80" r="1.5" fill="#0EA5E9" opacity="0.15"/>
          <circle cx="500" cy="80" r="1.5" fill="#0EA5E9" opacity="0.15"/>
          <circle cx="600" cy="80" r="1.5" fill="#0EA5E9" opacity="0.15"/>
          <circle cx="700" cy="80" r="1.5" fill="#0EA5E9" opacity="0.15"/>
          <circle cx="800" cy="80" r="1.5" fill="#0EA5E9" opacity="0.15"/>
          <circle cx="900" cy="80" r="1.5" fill="#0EA5E9" opacity="0.15"/>
          
          <circle cx="100" cy="180" r="1.5" fill="#0EA5E9" opacity="0.15"/>
          <circle cx="900" cy="180" r="1.5" fill="#0EA5E9" opacity="0.15"/>
          
          <circle cx="100" cy="280" r="1.5" fill="#0EA5E9" opacity="0.15"/>
          <circle cx="900" cy="280" r="1.5" fill="#0EA5E9" opacity="0.15"/>
          
          <circle cx="100" cy="380" r="1.5" fill="#0EA5E9" opacity="0.15"/>
          <circle cx="200" cy="380" r="1.5" fill="#0EA5E9" opacity="0.15"/>
          <circle cx="300" cy="380" r="1.5" fill="#0EA5E9" opacity="0.15"/>
          <circle cx="400" cy="380" r="1.5" fill="#0EA5E9" opacity="0.15"/>
          <circle cx="500" cy="380" r="1.5" fill="#0EA5E9" opacity="0.15"/>
          <circle cx="600" cy="380" r="1.5" fill="#0EA5E9" opacity="0.15"/>
          <circle cx="700" cy="380" r="1.5" fill="#0EA5E9" opacity="0.15"/>
          <circle cx="800" cy="380" r="1.5" fill="#0EA5E9" opacity="0.15"/>
          <circle cx="900" cy="380" r="1.5" fill="#0EA5E9" opacity="0.15"/>

          <!-- Large Background English text -->
          <text x="500" y="270" text-anchor="middle" fill="#0EA5E9" font-size="90" font-family="'Outfit', sans-serif" font-weight="900" opacity="0.05" letter-spacing="0.1em">{target_post['english_title']}</text>
          
          <!-- Corner Lines -->
          <line x1="50" y1="50" x2="150" y2="50" stroke="#0EA5E9" stroke-width="2" opacity="0.6"/>
          <line x1="50" y1="50" x2="50" y2="150" stroke="#0EA5E9" stroke-width="2" opacity="0.6"/>
          
          <line x1="950" y1="378" x2="850" y2="378" stroke="#10B981" stroke-width="2" opacity="0.6"/>
          <line x1="950" y1="378" x2="950" y2="278" stroke="#10B981" stroke-width="2" opacity="0.6"/>



          <!-- Single Centered Main message -->
          <text x="500" y="240" text-anchor="middle" fill="url(#text-grad)" font-size="{font_size}" font-family="'Noto Sans JP', sans-serif" font-weight="900" letter-spacing="0.05em">{summary_text}</text>
          
          <path d="M0 428 L1000 428" stroke="var(--glass-border)" stroke-width="1"/>
        </svg>"""

    # Start replacing template sections
    new_html = template
    
    # 1. Update <title>
    new_html = re.sub(r'<title>(.*?)</title>', f"<title>{target_post['title']}</title>", new_html)
    
    # 2. Update meta tags & canonical URL
    expected_url = f"https://www.ill-inc.net/column/{target_post['filename']}"
    new_html = re.sub(r'<meta name="description" content="[^"]*">', f'<meta name="description" content="{target_post["description"]}">', new_html)
    new_html = re.sub(r'<meta name="keywords" content="[^"]*">', f'<meta name="keywords" content="{target_post["keywords"]}">', new_html)
    new_html = re.sub(r'<link rel="canonical" href="[^"]*">', f'<link rel="canonical" href="{expected_url}">', new_html)

    # 2.1 Update OGP & Twitter tags
    core_title = target_post["title"].split("|")[0].split("—")[0].strip()
    og_title = f"{core_title} | Ill inc. コラム"
    new_html = re.sub(r'<meta property="og:url" content="[^"]*">', f'<meta property="og:url" content="{expected_url}">', new_html)
    new_html = re.sub(r'<meta property="og:title" content="[^"]*">', f'<meta property="og:title" content="{og_title}">', new_html)
    new_html = re.sub(r'<meta property="og:description" content="[^"]*">', f'<meta property="og:description" content="{target_post["description"]}">', new_html)
    new_html = re.sub(r'<meta name="twitter:title" content="[^"]*">', f'<meta name="twitter:title" content="{og_title}">', new_html)
    new_html = re.sub(r'<meta name="twitter:description" content="[^"]*">', f'<meta name="twitter:description" content="{target_post["description"]}">', new_html)
    
    # 3. Update breadcrumbs
    new_html = re.sub(r'(?s)(<div class="breadcrumbs">.*?<span class="breadcrumb-item">).*?(</span>\s*</div>)', rf'\g<1>{target_post["title_line2"]}\g<2>', new_html)
    
    # 4. Update Header banner
    new_html = re.sub(r'<span class="article-category">[^<]+</span>', f'<span class="article-category">{target_post["category_name"]}</span>', new_html)
    new_html = re.sub(r'<h1 class="article-title">[^<]+</h1>', f'<h1 class="article-title">{target_post["headline"]}</h1>', new_html)
    
    # 5. Update Date in Header & Schema
    new_html = re.sub(r'<time datetime="[^"]*">[^<]+</time>', f'<time datetime="{iso_date}">{period_date}</time>', new_html)
    new_html = re.sub(r'<span>公開日:\s*\d{4}\.\d{2}\.\d{2}</span>', f'<span>公開日: {period_date}</span>', new_html)
    new_html = re.sub(r'"headline":\s*"[^"]+"', f'"headline": "{target_post["headline"]}"', new_html)
    new_html = re.sub(r'"description":\s*"[^"]+"', f'"description": "{target_post["description"]}"', new_html)
    new_html = re.sub(r'"datePublished":\s*"\d{4}-\d{2}-\d{2}"', f'"datePublished": "{iso_date}"', new_html)
    new_html = re.sub(r'"dateModified":\s*"\d{4}-\d{2}-\d{2}"', f'"dateModified": "{iso_date}"', new_html)
    new_html = re.sub(r'"mainEntityOfPage":\s*\{\s*"@type":\s*"WebPage",\s*"@id":\s*"[^"]*"\s*\}', f'"mainEntityOfPage": {{\n      "@type": "WebPage",\n      "@id": "{expected_url}"\n    }}', new_html)
    
    # 6. Update SVG main visual
    new_html = re.sub(r'(?s)<div class="article-main-visual">.*?</div>', f'<div class="article-main-visual">\n        {banner_svg}\n      </div>', new_html)
    
    # 7. Replace Main body content
    new_html = re.sub(r'(?s)<main class="article-body">.*?</main>', f'<main class="article-body">{body_html}\n        </main>', new_html)
    
    # --- MANDATORY PRE-PUBLISH TYPO & QUALITY ASSURANCE SUITE ---
    # 1. Company Branding Enforcement
    new_html = new_html.replace("株式会社イル", "Ill（イル）株式会社")
    new_html = new_html.replace("株式会社Ill", "Ill（イル）株式会社")
    new_html = new_html.replace("イル株式会社", "Ill（イル）株式会社")

    # 2. Font Size Enforcement (Checklist boxes & text)
    new_html = new_html.replace("font-size: 0.95rem", "font-size: 1.5rem")
    new_html = new_html.replace("font-size:0.95rem", "font-size: 1.5rem")

    # 3. Automatic Typo Repair for Question Endings
    new_html = re.sub(r'([一-龠])？', lambda m: 'か？' if m.group(1) not in ['何', '誰', '何日', '何月'] else m.group(0), new_html)

    # 4. Strict Validation Assertions
    if "株式会社イル" in new_html:
        raise ValueError("CRITICAL ERROR: Prohibited company name '株式会社イル' detected before saving!")
    if "font-size: 0.95rem" in new_html:
        raise ValueError("CRITICAL ERROR: Microscopic font size 0.95rem detected before saving!")
    if "起？" in new_html:
        raise ValueError("CRITICAL ERROR: Typo '起？' detected before saving!")
    if f'href="{expected_url}"' not in new_html:
        raise ValueError(f"CRITICAL ERROR: Canonical URL not set to {expected_url}!")
    if f'content="{expected_url}"' not in new_html:
        raise ValueError(f"CRITICAL ERROR: og:url not set to {expected_url}!")

    clean_text = re.sub(r'\s+', '', re.sub(r'<[^>]+>', '', body_html))
    if len(clean_text) < 1800:
        raise ValueError(f"CRITICAL ERROR: Article body text length ({len(clean_text)} chars) is below required 1800 chars threshold!")

    # Save the new article
    # Save the new article
    new_filepath = os.path.join(COLUMN_DIR, target_post["filename"])
    with open(new_filepath, "w", encoding="utf-8") as f:
        f.write(new_html)
        
    print(f"Generated new article file at {new_filepath}")
    
    # Now let's trigger the rebuild scripts to sync sitemaps, sidebars, indices, and OGP/schema markup
    print("Triggering index and schema rebuild scripts...")
    
    # Run dates and sidebars rebuild script
    rebuild_script = os.path.join(SCRIPT_DIR, "rebuild_blog_index_and_dates.py")
    if os.path.exists(rebuild_script):
        subprocess.run(["python3", rebuild_script])
        
    # Run SEO optimization script to inject FAQ schema JSON-LD, Breadcrumb JSON-LD, and SVG aria-labels
    seo_script = os.path.join(SCRIPT_DIR, "apply_seo_optimizations.py")
    if os.path.exists(seo_script):
        subprocess.run(["python3", seo_script])
        
    print("New B2B column article has been fully integrated into sitemaps and indexes!")

if __name__ == "__main__":
    main()
