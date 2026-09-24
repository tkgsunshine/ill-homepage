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
            # Check the timestamp of the last ADDED article file in column/ (ignoring index.html or maintenance commits)
            res = subprocess.run(
                ["git", "log", "-1", "--diff-filter=A", "--format=%ct", "--", "column/*.html"],
                capture_output=True,
                text=True,
                check=True
            )
            stdout_str = res.stdout.strip()
            if stdout_str:
                last_article_added_ts = int(stdout_str)
                elapsed_seconds = time.time() - last_article_added_ts
                # Guard window: 2.5 hours (9000 seconds)
                if elapsed_seconds < 9000:
                    elapsed_min = int(elapsed_seconds / 60)
                    print(f"Notice: A new article was added {elapsed_min} minutes ago. Skipping duplicate generation for this retry window.")
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
        
    # Generate dates using Tokyo / JST timezone (UTC+9) so GitHub Actions UTC environment generates the correct Japanese business date
    jst = datetime.timezone(datetime.timedelta(hours=9))
    now_jst = datetime.datetime.now(jst)
    period_date = now_jst.strftime('%Y.%m.%d')
    iso_date = now_jst.strftime('%Y-%m-%d')
    
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

    bottom_cta_html = """
          <!-- Eye-catching Bottom CTA Banner -->
          <div class="article-bottom-cta">
            <div class="cta-badge">
              <span class="badge-dot"></span>無料相談・相見積もり歓迎
            </div>
            <h3 class="cta-title">システム開発・AI導入の無料相談・概算見積もり</h3>
            <p class="cta-desc">
              不要な機能を削ぎ落とす「ミニマル設計」で、高品質な開発を適正価格で実現します。
            </p>
            <div class="cta-check-pills">
              <span class="cta-check-pill">
                <svg class="check-icon" width="16" height="16" viewBox="0 0 20 20" fill="currentColor">
                  <path fill-rule="evenodd" d="M10 18a8 8 0 100-16 8 8 0 000 16zm3.707-9.293a1 1 0 00-1.414-1.414L9 10.586 7.707 9.293a1 1 0 00-1.414 1.414l2 2a1 1 0 001.414 0l4-4z" clip-rule="evenodd"/>
                </svg>
                他社見積もりの妥当性診断
              </span>
              <span class="cta-check-pill">
                <svg class="check-icon" width="16" height="16" viewBox="0 0 20 20" fill="currentColor">
                  <path fill-rule="evenodd" d="M10 18a8 8 0 100-16 8 8 0 000 16zm3.707-9.293a1 1 0 00-1.414-1.414L9 10.586 7.707 9.293a1 1 0 00-1.414 1.414l2 2a1 1 0 001.414 0l4-4z" clip-rule="evenodd"/>
                </svg>
                最短即日の概算提示
              </span>
              <span class="cta-check-pill">
                <svg class="check-icon" width="16" height="16" viewBox="0 0 20 20" fill="currentColor">
                  <path fill-rule="evenodd" d="M10 18a8 8 0 100-16 8 8 0 000 16zm3.707-9.293a1 1 0 00-1.414-1.414L9 10.586 7.707 9.293a1 1 0 00-1.414 1.414l2 2a1 1 0 001.414 0l4-4z" clip-rule="evenodd"/>
                </svg>
                仕様変更に強いアジャイル
              </span>
            </div>
            <div class="cta-buttons">
              <a href="../index.html#contact" class="btn btn-primary btn-cta-primary">
                無料相談・見積もりを依頼する <span class="arrow">→</span>
              </a>
            </div>
            <p class="cta-microcopy">
              <span>🔒</span> オンライン相談対応・無理な営業は一切いたしません
            </p>
          </div>
"""
    toc_box_html = '\n          <div class="toc-box">\n            <div class="toc-title">目次</div>\n            <ul class="toc-list">\n' + '\n'.join(toc_items) + '\n            </ul>\n          </div>\n'
    body_html = toc_box_html + sections_html + bottom_cta_html
        
    # Generate custom SVG banner (Super-Clean Minimal 2-Line Style)
    from apply_new_thumbnail_design import generate_svg
    banner_svg = generate_svg(target_post['filename'], target_post['headline'], target_post.get('category_name', 'システム開発'))

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
    if len(clean_text) < 1400:
        raise ValueError(f"CRITICAL ERROR: Article body text length ({len(clean_text)} chars) is below required 1400 chars threshold!")

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
