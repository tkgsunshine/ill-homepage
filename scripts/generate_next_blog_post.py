import os
import re
import json
import datetime
import subprocess

SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
WORKSPACE_DIR = os.path.dirname(SCRIPT_DIR)
COLUMN_DIR = os.path.join(WORKSPACE_DIR, "column")
CALENDAR_PATH = os.path.join(SCRIPT_DIR, "editorial_calendar.json")
TEMPLATE_PATH = os.path.join(COLUMN_DIR, "history-and-difference-of-generative-ai.html")

def main():
    print("Executing generate_next_blog_post.py...")
    
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
    
    # Generate body HTML
    body_html = ""
    # Add body sections
    for sec in target_post["body_sections"]:
        body_html += f"\n          <h2>{sec['h2']}</h2>\n          {sec['text']}\n"
        
    # Add FAQ section
    if "questions" in target_post and target_post["questions"]:
        body_html += '\n          <h2 id="section-faq">よくある質問</h2>\n          <div class="faq-container">\n'
        for qa in target_post["questions"]:
            body_html += f'            <div class="faq-item">\n              <h3>{qa["q"]}</h3>\n              <p>{qa["a"]}</p>\n            </div>\n'
        body_html += '          </div>\n'
        
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
    
    # 2. Update meta tags
    new_html = re.sub(r'<meta name="description" content="[^"]*">', f'<meta name="description" content="{target_post["description"]}">', new_html)
    new_html = re.sub(r'<meta name="keywords" content="[^"]*">', f'<meta name="keywords" content="{target_post["keywords"]}">', new_html)
    
    # 3. Update breadcrumbs
    new_html = re.sub(r'(?s)(<div class="breadcrumbs">.*?<span class="breadcrumb-item">).*?(</span>\s*</div>)', rf'\g<1>{target_post["title_line2"]}\g<2>', new_html)
    
    # 4. Update Header banner
    new_html = re.sub(r'<span class="article-category">[^<]+</span>', f'<span class="article-category">{target_post["category_name"]}</span>', new_html)
    new_html = re.sub(r'<h1 class="article-title">[^<]+</h1>', f'<h1 class="article-title">{target_post["headline"]}</h1>', new_html)
    
    # 5. Update Date in Header
    new_html = re.sub(r'<time datetime="[^"]*">[^<]+</time>', f'<time datetime="{iso_date}">{period_date}</time>', new_html)
    new_html = re.sub(r'<span>公開日:\s*\d{4}\.\d{2}\.\d{2}</span>', f'<span>公開日: {period_date}</span>', new_html)
    new_html = re.sub(r'"headline":\s*"[^"]+"', f'"headline": "{target_post["headline"]}"', new_html)
    new_html = re.sub(r'"description":\s*"[^"]+"', f'"description": "{target_post["description"]}"', new_html)
    new_html = re.sub(r'"datePublished":\s*"\d{4}-\d{2}-\d{2}"', f'"datePublished": "{iso_date}"', new_html)
    new_html = re.sub(r'"dateModified":\s*"\d{4}-\d{2}-\d{2}"', f'"dateModified": "{iso_date}"', new_html)
    
    # 6. Update SVG main visual
    new_html = re.sub(r'(?s)<div class="article-main-visual">.*?</div>', f'<div class="article-main-visual">\n        {banner_svg}\n      </div>', new_html)
    
    # 7. Replace Main body content
    new_html = re.sub(r'(?s)<main class="article-body">.*?</main>', f'<main class="article-body">{body_html}\n        </main>', new_html)
    
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
