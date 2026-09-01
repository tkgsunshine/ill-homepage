import os
import re
import json

SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
WORKSPACE_DIR = os.path.dirname(SCRIPT_DIR)
COLUMN_DIR = os.path.join(WORKSPACE_DIR, "column")

# Chronological order of all 53 articles
ALL_ARTICLES_CHRONO = [
    "inhouse-vs-outsourcing.html",
    "requirements-definition-tips.html",
    "development-schedule-shortening.html",
    "nocode-vs-scratch.html",
    "contract-types-comparison.html",
    "rfp-development-request.html",
    "agile-minimalist-dev.html",
    "ai-app-integration.html",
    "saas-product-launch.html",
    "development-cost-market.html",
    "offshore-hybrid-development.html",
    "new-service-success.html",
    "new-service-development.html",
    "minimal-development.html",
    "offshore-labo-contract-tips.html",
    "global-offshore-quality-control.html",
    "llm-fine-tuning-vs-rag.html",
    "ai-agent-business-automation.html",
    "llm-providers-comparison.html",
    "genai-vendor-selection-tips.html",
    "genai-market-trends-2026.html",
    "genai-roi-cost-design.html",
    "enterprise-genai-security.html",
    "micro-frontends-architecture.html",
    "agile-requirements-definition.html",
    "mvp-validation-strategy.html",
    "offshore-agile-development.html",
    "ai-agent-implementation.html",
    "history-and-difference-of-generative-ai.html",
    "future-of-work-with-generative-ai.html",
    "generative-ai-security-risks.html",
    "generative-ai-prompt-tips.html",
    "how-to-use-generative-ai-in-business.html",
    "which-generative-ai-to-use.html",
    "beginner-guide-to-ai-image-generation.html",
    "chatgpt-free-vs-plus.html",
    "smartphone-generative-ai-apps.html",
    "how-to-ask-chatgpt-better-questions.html",
    "what-generative-ai-can-and-cannot-do.html",
    # 14 Recent articles with unique staggered dates
    "physical-ai-robotics-automation.html",           # 2026-07-18
    "api-integration-development.html",               # 2026-07-19
    "sovereign-ai-japanese-llm.html",                 # 2026-07-20
    "basic-vs-detailed-design.html",                  # 2026-07-21
    "generative-ai-roi-assessment.html",              # 2026-07-22
    "legacy-system-modernization.html",               # 2026-07-23
    "autonomous-ai-agents-digital-workers.html",       # 2026-07-24
    "web-system-security.html",                       # 2026-07-25
    "system-development-testing.html",                # 2026-07-26
    "system-development-cost-breakdown.html",          # 2026-07-27
    "openai-api-pricing-comparison.html",              # 2026-07-28
    "how-to-choose-system-development-vendor.html",   # 2026-07-29
    "rag-enterprise-search-development.html",         # 2026-07-30
    "ai-chatbot-system-development.html",             # 2026-07-31
    "system-development-estimation-details.html",     # 2026-08-20
    "custom-crm-development-cost.html",               # 2026-08-20
    "mvp-development-startup-speed.html"              # 2026-08-21
]

# Explicit dates mapping for the 14 recent articles
RECENT_DATES = {
    "physical-ai-robotics-automation.html": ("2026.07.18", "2026-07-18"),
    "api-integration-development.html": ("2026.07.19", "2026-07-19"),
    "sovereign-ai-japanese-llm.html": ("2026.07.20", "2026-07-20"),
    "basic-vs-detailed-design.html": ("2026.07.21", "2026-07-21"),
    "generative-ai-roi-assessment.html": ("2026.07.22", "2026-07-22"),
    "legacy-system-modernization.html": ("2026.07.23", "2026-07-23"),
    "autonomous-ai-agents-digital-workers.html": ("2026.07.24", "2026-07-24"),
    "web-system-security.html": ("2026.07.25", "2026-07-25"),
    "system-development-testing.html": ("2026.07.26", "2026-07-26"),
    "system-development-cost-breakdown.html": ("2026.07.27", "2026-07-27"),
    "openai-api-pricing-comparison.html": ("2026.07.28", "2026-07-28"),
    "how-to-choose-system-development-vendor.html": ("2026.07.29", "2026-07-29"),
    "rag-enterprise-search-development.html": ("2026.07.30", "2026-07-30"),
    "ai-chatbot-system-development.html": ("2026.07.31", "2026-07-31"),
    "system-development-estimation-details.html": ("2026.08.20", "2026-08-20"),
    "custom-crm-development-cost.html": ("2026.08.20", "2026-08-20"),
    "mvp-development-startup-speed.html": ("2026.08.21", "2026-08-21")
}

def clean_html(text):
    text = re.sub(r'<[^>]+>', '', text)
    text = " ".join(text.split())
    return text.strip()

def main():
    print("Adjusting dates, updating indexes, sidebars, and sitemap...")

    # Dynamic discovery of new articles not in the hardcoded list
    base_articles = list(ALL_ARTICLES_CHRONO)
    new_articles = []
    for filename in os.listdir(COLUMN_DIR):
        if not filename.endswith(".html") or filename == "index.html":
            continue
        if filename in base_articles:
            continue
            
        # Parse date from the new file to sort them chronologically
        filepath = os.path.join(COLUMN_DIR, filename)
        with open(filepath, "r", encoding="utf-8") as f:
            content = f.read()
            
        date_match = re.search(r'<span>公開日:\s*(\d{4})\.(\d{2})\.(\d{2})</span>', content)
        if date_match:
            date_str = f"{date_match.group(1)}-{date_match.group(2)}-{date_match.group(3)}"
        else:
            date_str = "2026-08-22"
            
        new_articles.append((filename, date_str))
        
    # Sort new articles by date
    new_articles.sort(key=lambda x: x[1])
    
    # Append to chronological list
    for filename, _ in new_articles:
        ALL_ARTICLES_CHRONO.append(filename)
        print(f"Dynamically registered new article: {filename}")

    # Step 1: Update individual HTML files for the 14 recent articles with their new dates
    for filename, (period_date, iso_date) in RECENT_DATES.items():
        filepath = os.path.join(COLUMN_DIR, filename)
        if not os.path.exists(filepath):
            print(f"Warning: {filename} does not exist!")
            continue
            
        with open(filepath, "r", encoding="utf-8") as f:
            content = f.read()
            
        # 1.1 Replace Date text and datetime tag
        content = re.sub(
            r'<time datetime="\d{4}-\d{2}-\d{2}">\d{4}\.\d{2}\.\d{2}</time>',
            f'<time datetime="{iso_date}">{period_date}</time>',
            content
        )
        content = re.sub(
            r'<span>公開日:\s*\d{4}\.\d{2}\.\d{2}</span>',
            f'<span>公開日: {period_date}</span>',
            content
        )
        content = re.sub(
            r'<span>公開日: \d{4}\.\d{2}\.\d{2}</span>',
            f'<span>公開日: {period_date}</span>',
            content
        )

        # 1.2 Update BlogPosting structured data
        blogposting_pattern = r'(?s)<script type="application/ld\+json">\s*\{\s*"@context": "https://schema.org",\s*"@type": "BlogPosting".*?</script>'
        bp_match = re.search(blogposting_pattern, content)
        if bp_match:
            bp_text = bp_match.group(0)
            bp_text = re.sub(r'"datePublished": "\d{4}-\d{2}-\d{2}"', f'"datePublished": "{iso_date}"', bp_text)
            bp_text = re.sub(r'"dateModified": "\d{4}-\d{2}-\d{2}"', f'"dateModified": "{iso_date}"', bp_text)
            content = content.replace(bp_match.group(0), bp_text)

        with open(filepath, "w", encoding="utf-8") as f:
            f.write(content)
        print(f"Updated date in file: {filename} -> {period_date}")

    # Step 2: Cache metadata from ALL 53 articles
    articles_meta = {}
    for filename in ALL_ARTICLES_CHRONO:
        filepath = os.path.join(COLUMN_DIR, filename)
        if not os.path.exists(filepath):
            continue
            
        with open(filepath, "r", encoding="utf-8") as f:
            content = f.read()
            
        # Parse date
        date_match = re.search(r'<span>公開日:\s*(\d{4})\.(\d{2})\.(\d{2})</span>', content)
        if date_match:
            iso_date = f"{date_match.group(1)}-{date_match.group(2)}-{date_match.group(3)}"
            period_date = f"{date_match.group(1)}.{date_match.group(2)}.{date_match.group(3)}"
        else:
            bp_match = re.search(r'"datePublished": "(\d{4}-\d{2}-\d{2})"', content)
            if bp_match:
                iso_date = bp_match.group(1)
                period_date = iso_date.replace("-", ".")
            else:
                iso_date = "2026-06-05"
                period_date = "2026.06.05"

        # Cache metadata
        title_match = re.search(r'<title>(.*?)</title>', content)
        full_title = title_match.group(1) if title_match else "Ill inc. コラム"
        core_title = full_title.split("|")[0].split("—")[0].strip()
        
        desc_match = re.search(r'<meta name="description" content="([^"]*)">', content)
        excerpt = desc_match.group(1) if desc_match else ""
        
        cat_match = re.search(r'<span class="article-category">([^<]+)</span>', content)
        cat_name = cat_match.group(1) if cat_match else "生成AI・先端技術"
        cat_id = "system-app"
        if "生成AI" in cat_name or "AI" in cat_name or "LLM" in cat_name:
            cat_id = "gen-ai"
        elif "新規サービス" in cat_name:
            cat_id = "new-service"
        elif "グローバル" in cat_name:
            cat_id = "global-dev"
        elif "仕様" in cat_name:
            cat_id = "spec-design"
            
        svg_match = re.search(r'(?s)<svg viewBox="0 0 1000 428"[^>]*>.*?</svg>', content)
        clean_svg = svg_match.group(0) if svg_match else ""
        
        articles_meta[filename] = {
            "title": core_title,
            "excerpt": excerpt,
            "category_name": cat_name,
            "category_id": cat_id,
            "date": iso_date,
            "period_date": period_date,
            "svg": clean_svg
        }

    # Step 3: Synchronize Sidebars ("最近のコラム") in ALL 53 files
    latest_five = ALL_ARTICLES_CHRONO[-5:][::-1]
    
    sidebar_html_lines = []
    for filename in latest_five:
        meta = articles_meta[filename]
        sidebar_html_lines.append(f"""              <li class="related-item">
                <a href="/column/{filename}">
                  <span class="related-item-date">{meta["period_date"]}</span>
                  <span class="related-item-title">{meta["title"]}</span>
                </a>
              </li>""")
    
    sidebar_content = "\n".join(sidebar_html_lines)
    
    for filename in ALL_ARTICLES_CHRONO:
        filepath = os.path.join(COLUMN_DIR, filename)
        if not os.path.exists(filepath):
            continue
            
        with open(filepath, "r", encoding="utf-8") as f:
            content = f.read()
            
        sidebar_pattern = r'(?s)(<ul class="related-list">).*?(</ul>)'
        content = re.sub(sidebar_pattern, rf'\g<1>\n{sidebar_content}\n          \g<2>', content)
        
        with open(filepath, "w", encoding="utf-8") as f:
            f.write(content)
            
    print("Synchronized all 53 article sidebars.")

    # Step 4: Re-render card grid in column/index.html (hub page)
    all_articles_desc = ALL_ARTICLES_CHRONO[::-1]
    
    hub_cards = []
    for filename in all_articles_desc:
        meta = articles_meta[filename]
        
        card_svg = meta["svg"]
        card_svg_tag_pattern = r'(?s)(<svg viewBox="0 0 1000 428"[^>]*?)(>)'
        card_svg = re.sub(
            card_svg_tag_pattern,
            rf'\g<1> role="img" aria-label="コラム「{meta["title"]}」のビジュアルバナー"\g<2>',
            card_svg
        )
        
        card_html = f"""        <article class="column-card glass-card reveal" data-category="{meta["category_id"]}">
          <a href="/column/{filename}" style="display: block; text-decoration: none; overflow: hidden; border-radius: 1.2rem 1.2rem 0 0;">
            <div class="column-card-image">
              <span class="column-card-badge">{meta["category_name"]}</span>
              {card_svg}
            </div>
          </a>
          <div class="column-card-content">
            <div class="column-card-meta">
              <time datetime="{meta["date"]}">{meta["period_date"]}</time>
            </div>
            <a href="/column/{filename}" style="text-decoration: none;">
              <h2 class="column-card-title">{meta["title"]}</h2>
            </a>
            <p class="column-card-excerpt">{meta["excerpt"]}</p>
            <a href="/column/{filename}" class="column-card-link">記事を読む</a>
          </div>
        </article>"""
        hub_cards.append(card_html)
        
    hub_path = os.path.join(COLUMN_DIR, "index.html")
    if os.path.exists(hub_path):
        with open(hub_path, "r", encoding="utf-8") as f:
            hub_content = f.read()
            
        grid_start = '<div class="column-grid">'
        grid_end = '</div>\n  </section>'
        
        start_idx = hub_content.find(grid_start) + len(grid_start)
        end_idx = hub_content.find(grid_end, start_idx)
        
        new_grid_content = "\n" + "\n\n".join(hub_cards) + "\n      "
        hub_content = hub_content[:start_idx] + new_grid_content + hub_content[end_idx:]
        
        with open(hub_path, "w", encoding="utf-8") as f:
            f.write(hub_content)
        print("Updated column/index.html card grid.")

    # Step 5: Re-render Latest Columns in Homepage (index.html)
    newest_three = ALL_ARTICLES_CHRONO[-3:][::-1]
    
    home_cards = []
    for filename in newest_three:
        meta = articles_meta[filename]
        
        home_svg = meta["svg"].replace('href="../illust_', 'href="illust_')
        home_svg_tag_pattern = r'(?s)(<svg viewBox="0 0 1000 428"[^>]*?)(>)'
        home_svg = re.sub(
            home_svg_tag_pattern,
            rf'\g<1> role="img" aria-label="コラム「{meta["title"]}」のビジュアルバナー"\g<2>',
            home_svg
        )
        
        card_html = f"""        <article class="column-card glass-card reveal">
          <a href="column/{filename}" style="display: block; text-decoration: none; overflow: hidden; border-radius: 1.2rem 1.2rem 0 0;">
            <div class="column-card-image">
              <span class="column-card-badge">{meta["category_name"]}</span>
              {home_svg}
            </div>
          </a>
          <div class="column-card-content">
            <div class="column-card-meta">
              <time datetime="{meta["date"]}">{meta["period_date"]}</time>
            </div>
            <a href="column/{filename}" style="text-decoration: none;">
              <h2 class="column-card-title">{meta["title"]}</h2>
            </a>
            <p class="column-card-excerpt">{meta["excerpt"]}</p>
            <a href="column/{filename}" class="column-card-link">記事を読む</a>
          </div>
        </article>"""
        home_cards.append(card_html)
        
    home_path = os.path.join(WORKSPACE_DIR, "index.html")
    if os.path.exists(home_path):
        with open(home_path, "r", encoding="utf-8") as f:
            home_content = f.read()
            
        section_idx = home_content.find('id="columns"')
        if section_idx != -1:
            grid_start = '<div class="column-grid">'
            grid_end = '      </div>\n\n      <div style="text-align: center; margin-top: 4rem;">'
            
            start_idx = home_content.find(grid_start, section_idx) + len(grid_start)
            end_idx = home_content.find(grid_end, start_idx)
            
            new_grid_content = "\n" + "\n\n".join(home_cards) + "\n      "
            home_content = home_content[:start_idx] + new_grid_content + home_content[end_idx:]
            
            with open(home_path, "w", encoding="utf-8") as f:
                f.write(home_content)
            print("Updated homepage index.html columns section.")

    # Step 6: Overwrite/sync all sitemap.xml entries to match their actual dates
    sitemap_path = os.path.join(WORKSPACE_DIR, "sitemap.xml")
    if os.path.exists(sitemap_path):
        with open(sitemap_path, "r", encoding="utf-8") as f:
            lines = f.readlines()
            
        # Parse XML structure to rewrite lastmod dates of columns
        sitemap_str = "".join(lines)
        for filename, meta in articles_meta.items():
            loc_str = f"<loc>https://www.ill-inc.net/column/{filename}</loc>"
            # Search pattern for lastmod after this loc
            pattern = rf"(?s)(<loc>https://www\.ill-inc\.net/column/{filename}</loc>.*?<lastmod>)\d{{4}}-\d{{2}}-\d{{2}}(</lastmod>)"
            sitemap_str = re.sub(pattern, rf"\g<1>{meta['date']}\g<2>", sitemap_str)
            
        with open(sitemap_path, "w", encoding="utf-8") as f:
            f.write(sitemap_str)
        print("Synchronized all sitemap.xml lastmod dates.")

if __name__ == "__main__":
    main()
