import os
import re
import glob

SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
WORKSPACE_DIR = os.path.dirname(SCRIPT_DIR)
COLUMN_DIR = os.path.join(WORKSPACE_DIR, "column")

TOPIC_THEMES = {
    "ai": {
        "keywords": ["ai", "生成ai", "chatgpt", "claude", "gemini", "rag", "llm", "プロンプト"],
        "tag_en": "GENAI & AUTOMATION",
        "accent": "#00F0FF",
        "orb1": "#00F0FF",
        "orb2": "#A855F7",
        "takeaways": ("社内データ連携（RAG）", "API連携・自動化", "導入ROIの最大化")
    },
    "data_scraping": {
        "keywords": ["スクレイピング", "データ", "filemaker", "access", "excel", "エクセル", "データベース", "db"],
        "tag_en": "DATA & MODERNIZATION",
        "accent": "#22D3EE",
        "orb1": "#06B6D4",
        "orb2": "#3B82F6",
        "takeaways": ("手作業の完全撤廃", "クラウドWebDB化", "保守コスト大幅削減")
    },
    "mvp_startup": {
        "keywords": ["mvp", "新規事業", "新規サービス", "スタートアップ", "アジャイル", "マッチング", "c2c", "saas"],
        "tag_en": "AGILE & MVP LAUNCH",
        "accent": "#38BDF8",
        "orb1": "#0EA5E9",
        "orb2": "#6366F1",
        "takeaways": ("最短1ヶ月の市場検証", "コア機能への集中", "低リスク・低コスト開発")
    },
    "offshore": {
        "keywords": ["オフショア", "ベトナム", "ラボ型", "準委任", "請負", "契約"],
        "tag_en": "GLOBAL TECH TEAM",
        "accent": "#34D399",
        "orb1": "#10B981",
        "orb2": "#0EA5E9",
        "takeaways": ("専任エンジニア確保", "国内人件費の半額水準", "バイリンガルPM直結")
    },
    "default": {
        "keywords": [],
        "tag_en": "SMB DEFENSE STRATEGY",
        "accent": "#38BDF8",
        "orb1": "#0EA5E9",
        "orb2": "#818CF8",
        "takeaways": ("見積もりの適正化", "不要機能の排除", "契約トラブル防止")
    }
}

def get_theme(filename, title, category):
    text = (filename + " " + title + " " + category).lower()
    for key in ["ai", "data_scraping", "mvp_startup", "offshore"]:
        theme = TOPIC_THEMES[key]
        if any(kw in text for kw in theme["keywords"]):
            return theme
    return TOPIC_THEMES["default"]

def split_catchphrase(text):
    clean = " ".join(re.sub(r"<[^>]+>", "", text).split())
    if not clean:
        return ["システム開発の要点と", "失敗を防ぐ実践アプローチ"]
    if len(clean) <= 19:
        return [clean]
    
    best_idx = len(clean) // 2
    best_score = -9999
    particles = ["で", "と", "に", "を", "は", "が", "の", "や", "・", "も", "から", "にて", "し"]
    for i in range(5, len(clean) - 5):
        diff = abs(i - (len(clean) - i))
        score = -diff * 1.5
        if clean[i-1] in particles:
            score += 15
        if i >= 2 and clean[i-2:i] in ["による", "した", "での", "への", "から"]:
            score += 18
        if score > best_score:
            best_score = score
            best_idx = i
    return [clean[:best_idx], clean[best_idx:]]

def generate_svg(filename, title, category, existing_jp_lines=None):
    clean_id = re.sub(r"[^a-zA-Z0-9_]", "_", filename.replace(".html", ""))
    theme = get_theme(filename, title, category)
    
    accent = theme["accent"]
    orb1 = theme["orb1"]
    orb2 = theme["orb2"]
    tag_en = theme["tag_en"]
    t1, t2, t3 = theme["takeaways"]
    
    if existing_jp_lines and len(existing_jp_lines) > 0:
        raw_text = "".join(existing_jp_lines)
    else:
        raw_text = title.split("|")[0].split("—")[0].strip()
        if "【2026年最新】" in raw_text:
            raw_text = raw_text.replace("【2026年最新】", "")
        if len(raw_text) > 30:
            raw_text = raw_text[:28] + "..."
            
    lines = split_catchphrase(raw_text)
    
    if len(lines) == 1:
        text_svg = f"""<text x="110" y="238" fill="#FFFFFF" font-size="34" font-family="'Noto Sans JP', sans-serif" font-weight="900" letter-spacing="0.03em">
    {lines[0]}
  </text>"""
    else:
        l1, l2 = lines[0], lines[1]
        text_svg = f"""<text x="110" y="215" fill="#FFFFFF" font-size="32" font-family="'Noto Sans JP', sans-serif" font-weight="900" letter-spacing="0.02em">
    {l1}
  </text>
  <text x="110" y="260" fill="#FFFFFF" font-size="32" font-family="'Noto Sans JP', sans-serif" font-weight="900" letter-spacing="0.02em">
    <tspan fill="{accent}">{l2}</tspan>
  </text>"""

    svg = f"""<svg viewBox="0 0 1000 428" fill="none" xmlns="http://www.w3.org/2000/svg" role="img" aria-label="「{title}」のビジュアルバナー">
  <defs>
    <linearGradient id="bg_{clean_id}" x1="0" y1="0" x2="1000" y2="428" gradientUnits="userSpaceOnUse">
      <stop stop-color="#131D33"/>
      <stop offset="0.5" stop-color="#1E293B"/>
      <stop offset="1" stop-color="#172338"/>
    </linearGradient>
    <linearGradient id="border_{clean_id}" x1="0" y1="0" x2="1" y2="1">
      <stop stop-color="{accent}" stop-opacity="0.6"/>
      <stop offset="1" stop-color="{orb2}" stop-opacity="0.3"/>
    </linearGradient>
    <filter id="blur_{clean_id}" x="0" y="0" width="1000" height="428" filterUnits="userSpaceOnUse">
      <feGaussianBlur stdDeviation="70"/>
    </filter>
  </defs>

  <rect width="1000" height="428" fill="url(#bg_{clean_id})"/>

  <circle cx="850" cy="80" r="230" fill="{orb1}" opacity="0.3" filter="url(#blur_{clean_id})"/>
  <circle cx="150" cy="350" r="200" fill="{orb2}" opacity="0.25" filter="url(#blur_{clean_id})"/>

  <g opacity="0.18" stroke="{accent}" stroke-width="1">
    <line x1="80" y1="0" x2="80" y2="428"/>
    <line x1="200" y1="0" x2="200" y2="428"/>
    <line x1="320" y1="0" x2="320" y2="428"/>
    <line x1="440" y1="0" x2="440" y2="428"/>
    <line x1="560" y1="0" x2="560" y2="428"/>
    <line x1="680" y1="0" x2="680" y2="428"/>
    <line x1="800" y1="0" x2="800" y2="428"/>
    <line x1="920" y1="0" x2="920" y2="428"/>
    <line x1="0" y1="80" x2="1000" y2="80"/>
    <line x1="0" y1="180" x2="1000" y2="180"/>
    <line x1="0" y1="280" x2="1000" y2="280"/>
    <line x1="0" y1="380" x2="1000" y2="380"/>
  </g>

  <circle cx="200" cy="80" r="4" fill="{accent}" opacity="0.9"/>
  <circle cx="680" cy="180" r="4" fill="{accent}" opacity="0.9"/>
  <circle cx="800" cy="280" r="4" fill="{orb2}" opacity="0.9"/>

  <text x="500" y="155" text-anchor="middle" fill="{accent}" font-size="68" font-family="'Outfit', sans-serif" font-weight="900" opacity="0.08" letter-spacing="0.2em">{tag_en}</text>

  <!-- High-transparency Lightweight Frosted Glass Card -->
  <rect x="70" y="100" width="860" height="245" rx="18" fill="rgba(255, 255, 255, 0.08)" stroke="url(#border_{clean_id})" stroke-width="1.8"/>
  <path d="M70 118 C70 108 78 100 88 100 L912 100 C922 100 930 108 930 118" stroke="rgba(255, 255, 255, 0.4)" stroke-width="1.2" fill="none"/>

  <!-- Category Tag -->
  <g transform="translate(110, 135)">
    <rect width="195" height="28" rx="14" fill="rgba(255, 255, 255, 0.12)" stroke="{accent}" stroke-width="1.2"/>
    <text x="97" y="19" text-anchor="middle" fill="{accent}" font-size="13" font-family="'Outfit', sans-serif" font-weight="800" letter-spacing="0.06em">{tag_en}</text>
  </g>

  {text_svg}

  <!-- 3 Key Takeaways -->
  <g transform="translate(110, 292)">
    <text x="0" y="15" fill="#F1F5F9" font-size="15" font-family="'Noto Sans JP', sans-serif" font-weight="600">
      <tspan fill="{accent}">✔</tspan> {t1}　<tspan fill="{accent}">✔</tspan> {t2}　<tspan fill="{accent}">✔</tspan> {t3}
    </text>
  </g>

  <text x="890" y="322" text-anchor="end" fill="#CBD5E1" font-size="13" font-family="'Outfit', sans-serif" font-weight="700" letter-spacing="0.1em">ILL INC. TECH INSIGHTS</text>

  <rect x="0" y="0" width="1000" height="428" stroke="rgba(255, 255, 255, 0.15)" stroke-width="1.2" fill="none"/>
</svg>"""
    return svg

def main():
    print("Applying refined lightweight A-style thumbnail to all 96 column articles...")
    files = sorted([f for f in glob.glob(os.path.join(COLUMN_DIR, "*.html")) if "index.html" not in f])
    
    svg_map = {}
    for fpath in files:
        fname = os.path.basename(fpath)
        with open(fpath, "r", encoding="utf-8") as f:
            content = f.read()
            
        t_match = re.search(r"<h1 class=\"article-title\">(.*?)</h1>", content)
        title = t_match.group(1).strip() if t_match else fname
        cat_match = re.search(r"<span class=\"article-category\"[^>]*>(.*?)</span>", content)
        cat = cat_match.group(1).strip() if cat_match else "システム開発"
        
        mv = re.search(r"<div class=\"article-main-visual\">(.*?)</div>", content, re.DOTALL)
        existing_jp = []
        if mv:
            txts = re.findall(r"<text[^>]*>(.*?)</text>", mv.group(1), re.DOTALL)
            existing_jp = [re.sub(r"<[^>]+>", "", t).strip() for t in txts if any("\u3000" <= ch <= "\u9fff" for ch in t)]
            
        svg = generate_svg(fname, title, cat, existing_jp)
        svg_map[fname] = (svg, title, cat)
        
        new_content = re.sub(r"(?s)<div class=\"article-main-visual\">\s*<svg.*?</svg>\s*</div>", f"<div class=\"article-main-visual\">\n        {svg}\n      </div>", content)
        with open(fpath, "w", encoding="utf-8") as f:
            f.write(new_content)

    print(f"Updated article-main-visual in {len(files)} articles!")

    # Update column/index.html
    hub_path = os.path.join(COLUMN_DIR, "index.html")
    with open(hub_path, "r", encoding="utf-8") as f:
        hub = f.read()

    cards = re.findall(r"(<article class=\"column-card.*?</article>)", hub, re.DOTALL)
    print(f"Updating {len(cards)} cards in column/index.html...")
    for card in cards:
        href_match = re.search(r"href=\"/?column/([^\"]+)\"", card)
        if not href_match:
            href_match = re.search(r"href=\"([^\"]+\.html)\"", card)
        if not href_match:
            continue
        fn = href_match.group(1)
        if fn in svg_map:
            svg, title, cat = svg_map[fn]
            new_card = re.sub(r"<svg.*?</svg>", svg, card, flags=re.DOTALL)
            new_card = re.sub(r"<span class=\"column-card-badge\"[^>]*>.*?</span>", f"<span class=\"column-card-badge\">{cat}</span>", new_card)
            hub = hub.replace(card, new_card)

    with open(hub_path, "w", encoding="utf-8") as f:
        f.write(hub)
    print("Updated column/index.html successfully!")

    # Update index.html
    top_path = os.path.join(WORKSPACE_DIR, "index.html")
    with open(top_path, "r", encoding="utf-8") as f:
        top = f.read()

    top_cards = re.findall(r"(<article class=\"column-card.*?</article>)", top, re.DOTALL)
    print(f"Updating {len(top_cards)} cards in index.html...")
    for card in top_cards:
        href_match = re.search(r"href=\"column/([^\"]+)\"", card)
        if not href_match:
            continue
        fn = href_match.group(1)
        if fn in svg_map:
            svg, title, cat = svg_map[fn]
            new_card = re.sub(r"<svg.*?</svg>", svg, card, flags=re.DOTALL)
            new_card = re.sub(r"<span class=\"column-card-badge\"[^>]*>.*?</span>", f"<span class=\"column-card-badge\">{cat}</span>", new_card)
            top = top.replace(card, new_card)

    with open(top_path, "w", encoding="utf-8") as f:
        f.write(top)
    print("Updated index.html successfully!")

if __name__ == "__main__":
    main()
