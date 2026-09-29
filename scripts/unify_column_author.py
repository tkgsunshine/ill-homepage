import glob
import re

files = sorted(glob.glob('column/*.html'))
updated = 0

author_widget_new = """          <div class="sidebar-box glass-card author-profile">
            <div class="author-avatar">Ill</div>
            <h3 class="author-name">Ill inc. 編集部</h3>
            <p class="author-role">Technology Research Division</p>
            <p class="author-bio">
              最先端のAIトレンド（GenAI / Agentic AI）のビジネス応用、LLMセキュリティ、RAGアーキテクチャ設計などの知見を発信。新規事業における迅速な技術検証とPoC設計を担当。
            </p>
          </div>"""

schema_author_new = """    "author": {
      "@type": "Organization",
      "name": "Ill（イル）株式会社"
    },"""

for f in files:
    if 'index.html' in f:
        continue
    with open(f, 'r', encoding='utf-8') as fp:
        c = fp.read()
    
    orig = c
    # 1. Meta tag
    c = re.sub(r'<meta name="author" content="[^"]*">', '<meta name="author" content="Ill inc. 編集部">', c)
    
    # 2. Header author text
    c = re.sub(r'<span>著者:\s*[^<]+</span>', '<span>著者: Ill inc. 編集部</span>', c)
    
    # 3. JSON-LD author schema
    c = re.sub(r'(?s)"author":\s*\{.*?"name":\s*"山下 高志".*?\},', schema_author_new, c)
    c = re.sub(r'(?s)"author":\s*\{[^}]*"@type":\s*"Person"[^}]*\},', schema_author_new, c)
    
    # 4. Sidebar author widget
    # Target existing author widget with "山下 高志"
    c = re.sub(
        r'(?s)<div class="sidebar-box glass-card author-profile">\s*<div class="author-avatar">.*?</div>\s*<h3 class="author-name">山下 高志</h3>.*?</div>',
        author_widget_new,
        c
    )
    
    if c != orig:
        updated += 1
        with open(f, 'w', encoding='utf-8') as fp:
            fp.write(c)

print(f'Updated {updated} column files successfully.')
