import glob
import re
import os
import sys

SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, SCRIPT_DIR)
from topic_enrichment_data import get_best_config

files = sorted(glob.glob('column/*.html'))
print(f'Checking {len(files)-1} column articles for missing FAQs/tables...')

enriched_count = 0

for f in files:
    if 'index.html' in f:
        continue
    with open(f, 'r', encoding='utf-8') as fp:
        c = fp.read()
    
    # Check if missing FAQ section
    if 'class="faq-container"' not in c and 'id="section-faq"' not in c and 'id="faq"' not in c:
        fname = os.path.basename(f)
        cfg = get_best_config(fname, c)
        
        # Build enrichment HTML
        h2_title = cfg['h2_title']
        table_html = cfg['table_html']
        explanation_html = cfg['explanation_html']
        faqs = cfg['extra_faqs']
        
        faq_items_html = ""
        for q, a in faqs:
            faq_items_html += f"""            <div class="faq-item">
              <h3>{q}</h3>
              <p>{a}</p>
            </div>\n"""
            
        enrichment_block = f"""
          <h2 id="sec-pricing-table">{h2_title}</h2>
          <p>システム開発を検討する際、最も気になるのが「実際の費用相場」と「どこにコストがかかっているのか」という内訳です。以下の表は、一般的な受託開発会社・大手SIerと、<strong>Ill（イル）株式会社</strong> のミニマル設計による概算費用の比較です。</p>
          {table_html}
          {explanation_html}

          <h2 id="section-faq">よくある質問（FAQ）</h2>
          <div class="faq-container">
{faq_items_html}          </div>
"""
        
        # Insert before <!-- Eye-catching Bottom CTA Banner --> or before </main>
        if '<!-- Eye-catching Bottom CTA Banner -->' in c:
            c = c.replace('<!-- Eye-catching Bottom CTA Banner -->', enrichment_block + '\n          <!-- Eye-catching Bottom CTA Banner -->')
        elif '<div class="article-bottom-cta">' in c:
            c = c.replace('<div class="article-bottom-cta">', enrichment_block + '\n          <div class="article-bottom-cta">')
        else:
            c = c.replace('</main>', enrichment_block + '\n        </main>')
            
        # Update TOC to include the new sections if not present
        if 'class="toc-list"' in c:
            toc_match = re.search(r'(?s)<ul class="toc-list">(.*?)</ul>', c)
            if toc_match:
                toc_inner = toc_match.group(1)
                if 'sec-pricing-table' not in toc_inner:
                    toc_inner = toc_inner.rstrip() + f'\n              <li><a href="#sec-pricing-table">{h2_title}</a></li>\n              <li><a href="#section-faq">よくある質問（FAQ）</a></li>\n            '
                    c = c.replace(toc_match.group(0), f'<ul class="toc-list">{toc_inner}</ul>')
                    
        enriched_count += 1
        with open(f, 'w', encoding='utf-8') as fp:
            fp.write(c)

print(f'Enriched {enriched_count} legacy column articles successfully!')
