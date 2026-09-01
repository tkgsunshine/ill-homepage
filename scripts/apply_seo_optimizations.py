import os
import re
import json

SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
WORKSPACE_DIR = os.path.dirname(SCRIPT_DIR)
COLUMN_DIR = os.path.join(WORKSPACE_DIR, "column")

def get_articles():
    return sorted([f for f in os.listdir(COLUMN_DIR) if f.endswith(".html") and f != "index.html"])

def clean_html(text):
    # Remove HTML tags and strip
    text = re.sub(r'<[^>]+>', '', text)
    # Normalize whitespaces and clean newlines
    text = " ".join(text.split())
    return text.strip()

def main():
    print("Executing apply_seo_optimizations.py...")
    
    article_titles = {} # Map filename -> clean article title (for OGP/aria-label matches)
    articles = get_articles()

    # Step 1: Process individual article files
    for filename in articles:
        filepath = os.path.join(COLUMN_DIR, filename)
        if not os.path.exists(filepath):
            print(f"Warning: File {filepath} not found.")
            continue
            
        with open(filepath, "r", encoding="utf-8") as f:
            content = f.read()
            
        # 1.1 Parse title
        title_match = re.search(r'<title>(.*?)</title>', content)
        if title_match:
            full_title = title_match.group(1)
            # Extact the core title (usually before the pipe '|' or dash '—')
            core_title = full_title.split("|")[0].split("—")[0].strip()
            article_titles[filename] = core_title
        else:
            core_title = filename.replace(".html", "").replace("-", " ").title()
            article_titles[filename] = core_title

        # 1.2 Parse breadcrumb text
        breadcrumb_text = "コラム詳細"
        bc_match = re.search(r'(?s)<div class="breadcrumbs">(.*?)</div>', content)
        if bc_match:
            bc_html = bc_match.group(1)
            items = re.findall(r'<span class="breadcrumb-item">(.*?)</span>', bc_html)
            if items:
                # The last item is the active page name
                breadcrumb_text = clean_html(items[-1])

        # 1.3 Parse FAQ Q&As
        qas = []
        faq_match = re.search(r'(?s)<h2 id="section-faq">.*?</h2>(.*?)(?=<h2|</main>)', content)
        if faq_match:
            faq_html = faq_match.group(1)
            # Find all Q&As
            # Note: handle cases where answers span multiple paragraphs or tags
            qa_raw = re.findall(r'(?s)<h3>(Q\d*\..*?)</h3>\s*<p>(.*?)</p>', faq_html)
            for q, a in qa_raw:
                q_clean = clean_html(q)
                a_clean = clean_html(a)
                qas.append((q_clean, a_clean))
                
        print(f"Parsed {filename}: Title='{core_title}', BC='{breadcrumb_text}', FAQs={len(qas)}")

        # 1.4 Generate BreadcrumbList JSON-LD
        bc_json = {
            "@context": "https://schema.org",
            "@type": "BreadcrumbList",
            "itemListElement": [
                {
                    "@type": "ListItem",
                    "position": 1,
                    "name": "Home",
                    "item": "https://www.ill-inc.net/"
                },
                {
                    "@type": "ListItem",
                    "position": 2,
                    "name": "コラム",
                    "item": "https://www.ill-inc.net/column/"
                },
                {
                    "@type": "ListItem",
                    "position": 3,
                    "name": breadcrumb_text
                }
            ]
        }
        
        # 1.5 Generate FAQPage JSON-LD if FAQs exist
        faq_json = None
        if qas:
            faq_json = {
                "@context": "https://schema.org",
                "@type": "FAQPage",
                "mainEntity": []
            }
            for q, a in qas:
                faq_json["mainEntity"].append({
                    "@type": "Question",
                    "name": q,
                    "acceptedAnswer": {
                        "@type": "Answer",
                        "text": a
                    }
                })

        # 1.6 Inject JSON-LD into <head> (right before </head>)
        # To avoid double injection, we check if they already exist
        new_schemas_html = f'\n  <!-- Breadcrumb Structured Data -->\n  <script type="application/ld+json">\n  {json.dumps(bc_json, ensure_ascii=False, indent=2)}\n  </script>\n'
        if faq_json:
            new_schemas_html += f'\n  <!-- FAQ Structured Data -->\n  <script type="application/ld+json">\n  {json.dumps(faq_json, ensure_ascii=False, indent=2)}\n  </script>\n'

        # Remove existing generated FAQ/Breadcrumb lists if any (for clean update)
        content = re.sub(r'<!-- Breadcrumb Structured Data -->\s*<script type="application/ld+json">.*?</script>\s*', '', content, flags=re.DOTALL)
        content = re.sub(r'<!-- FAQ Structured Data -->\s*<script type="application/ld+json">.*?</script>\s*', '', content, flags=re.DOTALL)

        # Inject right before </head>
        content = content.replace("</head>", f"{new_schemas_html}</head>")

        # 1.7 Inject role="img" and aria-label into article's main visual SVG
        # Target: <div class="article-main-visual">\s*<svg viewBox="0 0 1000 428" ... >
        # We replace the SVG tag inside the article visual div
        def replace_article_svg(match):
            outer_div = match.group(1)
            svg_tag = match.group(2)
            closing = match.group(3)
            # Remove any pre-existing role or aria-label to prevent duplicates
            svg_tag_clean = re.sub(r'\s+role="img"|\s+aria-label="[^"]+"', '', svg_tag)
            # Add role and aria-label
            updated_svg_tag = f'{svg_tag_clean} role="img" aria-label="「{core_title}」のビジュアルバナー"'
            return outer_div + updated_svg_tag + closing

        article_svg_pattern = r'(?s)(<div class="article-main-visual">\s*)(<svg viewBox="0 0 1000 428"[^>]*?)(>)'
        content, count = re.subn(article_svg_pattern, replace_article_svg, content)
        if count > 0:
            print(f"  - Injected role/aria-label into main SVG banner")
        else:
            print(f"  - WARNING: Main SVG banner not found/replaced in {filename}")

        with open(filepath, "w", encoding="utf-8") as f:
            f.write(content)

    # Step 2: Process column/index.html (hub page)
    hub_path = os.path.join(COLUMN_DIR, "index.html")
    if os.path.exists(hub_path):
        with open(hub_path, "r", encoding="utf-8") as f:
            hub_content = f.read()

        card_pattern = re.compile(r'(?s)<article class="column-card glass-card reveal"[^>]*>.*?</article>')
        cards = card_pattern.findall(hub_content)
        print(f"\nProcessing column/index.html: Found {len(cards)} cards")

        updated_hub_content = hub_content
        for card in cards:
            href_match = re.search(r'href="([a-zA-Z0-9_-]+\.html)"', card)
            if not href_match:
                continue
            filename = href_match.group(1)
            if filename in article_titles:
                core_title = article_titles[filename]
                
                # Check for standard badge & svg layout inside card
                card_svg_pattern = r'(?s)(<div class="column-card-image">\s*<span class="column-card-badge">[^<]+</span>\s*)(<svg viewBox="0 0 1000 428"[^>]*?)(>)'
                
                def replace_card_svg(match):
                    span_wrapper = match.group(1)
                    svg_tag = match.group(2)
                    closing = match.group(3)
                    svg_tag_clean = re.sub(r'\s+role="img"|\s+aria-label="[^"]+"', '', svg_tag)
                    updated_svg_tag = f'{svg_tag_clean} role="img" aria-label="コラム「{core_title}」のビジュアルバナー"'
                    return span_wrapper + updated_svg_tag + closing
                
                card_updated, count = re.subn(card_svg_pattern, replace_card_svg, card)
                if count > 0:
                    updated_hub_content = updated_hub_content.replace(card, card_updated)
                    print(f"  - Injected role/aria-label into card SVG for {filename}")
                else:
                    print(f"  - WARNING: Could not inject role/aria-label into card SVG for {filename}")

        with open(hub_path, "w", encoding="utf-8") as f:
            f.write(updated_hub_content)
        print("Updated column/index.html successfully!")

    # Step 3: Process index.html (homepage)
    home_path = os.path.join(WORKSPACE_DIR, "index.html")
    if os.path.exists(home_path):
        with open(home_path, "r", encoding="utf-8") as f:
            home_content = f.read()

        card_pattern = re.compile(r'(?s)<article class="column-card glass-card reveal"[^>]*>.*?</article>')
        cards = card_pattern.findall(home_content)
        print(f"\nProcessing index.html: Found {len(cards)} cards")

        updated_home_content = home_content
        for card in cards:
            href_match = re.search(r'href="column/([a-zA-Z0-9_-]+\.html)"', card)
            if not href_match:
                continue
            filename = href_match.group(1)
            if filename in article_titles:
                core_title = article_titles[filename]
                
                card_svg_pattern = r'(?s)(<div class="column-card-image">\s*<span class="column-card-badge">[^<]+</span>\s*)(<svg viewBox="0 0 1000 428"[^>]*?)(>)'
                
                def replace_card_svg(match):
                    span_wrapper = match.group(1)
                    svg_tag = match.group(2)
                    closing = match.group(3)
                    svg_tag_clean = re.sub(r'\s+role="img"|\s+aria-label="[^"]+"', '', svg_tag)
                    updated_svg_tag = f'{svg_tag_clean} role="img" aria-label="コラム「{core_title}」のビジュアルバナー"'
                    return span_wrapper + updated_svg_tag + closing
                
                card_updated, count = re.subn(card_svg_pattern, replace_card_svg, card)
                if count > 0:
                    updated_home_content = updated_home_content.replace(card, card_updated)
                    print(f"  - Injected role/aria-label into card SVG for {filename}")
                else:
                    print(f"  - WARNING: Could not inject role/aria-label into card SVG for {filename}")

        with open(home_path, "w", encoding="utf-8") as f:
            f.write(updated_home_content)
        print("Updated index.html successfully!")

    # Step 4: Update sitemap.xml
    sitemap_path = os.path.join(WORKSPACE_DIR, "sitemap.xml")
    if os.path.exists(sitemap_path):
        with open(sitemap_path, "r", encoding="utf-8") as f:
            sitemap_content = f.read()

        # Update lastmod for homepage
        # Find the url block for https://www.ill-inc.net/ and update its lastmod
        sitemap_content = re.sub(
            r'(<loc>https://www\.ill-inc\.net/</loc>\s*<lastmod>)[^<]+(</lastmod>)',
            r'\g<1>2026-06-19\g<2>',
            sitemap_content
        )
        
        # Update lastmod for column index
        sitemap_content = re.sub(
            r'(<loc>https://www\.ill-inc\.net/column/</loc>\s*<lastmod>)[^<]+(</lastmod>)',
            r'\g<1>2026-06-19\g<2>',
            sitemap_content
        )

        with open(sitemap_path, "w", encoding="utf-8") as f:
            f.write(sitemap_content)
        print("\nUpdated sitemap.xml dates for main routes successfully!")

if __name__ == "__main__":
    main()
