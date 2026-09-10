import os
import re
import glob

SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
WORKSPACE_DIR = os.path.dirname(SCRIPT_DIR)
COLUMN_DIR = os.path.join(WORKSPACE_DIR, "column")

TOPIC_THEMES = {
    "ai": {
        "keywords": ["ai", "生成ai", "chatgpt", "claude", "gemini", "rag", "llm", "プロンプト"],
        "accent": "#00F0FF",
        "orb1": "#00F0FF",
        "orb2": "#A855F7",
        "takeaways": ("社内データ連携（RAG）", "API連携・自動化", "導入ROIの最大化")
    },
    "data_scraping": {
        "keywords": ["スクレイピング", "データ", "filemaker", "access", "excel", "エクセル", "データベース", "db"],
        "accent": "#22D3EE",
        "orb1": "#06B6D4",
        "orb2": "#3B82F6",
        "takeaways": ("手作業の完全撤廃", "クラウドWebDB化", "保守コスト大幅削減")
    },
    "mvp_startup": {
        "keywords": ["mvp", "新規事業", "新規サービス", "スタートアップ", "アジャイル", "マッチング", "c2c", "saas"],
        "accent": "#38BDF8",
        "orb1": "#0EA5E9",
        "orb2": "#6366F1",
        "takeaways": ("最短1ヶ月の市場検証", "コア機能への集中", "低リスク・低コスト開発")
    },
    "offshore": {
        "keywords": ["オフショア", "ベトナム", "ラボ型", "準委任", "請負", "契約"],
        "accent": "#34D399",
        "orb1": "#10B981",
        "orb2": "#0EA5E9",
        "takeaways": ("専任エンジニア確保", "国内人件費の半額水準", "バイリンガルPM直結")
    },
    "default": {
        "keywords": [],
        "accent": "#38BDF8",
        "orb1": "#0EA5E9",
        "orb2": "#818CF8",
        "takeaways": ("見積もりの適正化", "不要機能の排除", "契約トラブル防止")
    }
}

SUMMARY_MAPPING = {
    "008-real-estate-crm-custom-development.html": "独自CRM開発で不動産業務の成約率を高める",
    "009-logistics-matching-system-cost.html": "配送マッチングシステムを低コストで構築する",
    "010-matching-platform-mvp-cost.html": "マッチングプラットフォームのMVP開発費を抑える",
    "011-non-it-smb-system-development-no-engineer.html": "エンジニア不在の中小企業でも開発外注で成功する",
    "012-hiring-vs-outsourcing-cost-comparison.html": "エンジニア採用リスクを回避し開発外注で費用を落とす",
    "013-excel-to-web-system-dx-cost.html": "エクセルの業務限界を独自Webシステム化で解消する",
    "014-non-it-smb-genai-business-efficiency.html": "生成AI API連携で日常の定型業務を全自動化する",
    "015-smb-system-development-cost-standard.html": "システム開発の見積もり上乗せを未然に防ぐ",
    "016-nocode-limitations-real-development-cost.html": "ノーコードの限界を見極めスクラッチ開発で最適化する",
    "017-non-it-contract-types-risk-management.html": "請負と準委任のリスクを回避し適正コストで発注する",
    "018-simple-rfp-writing-for-non-it-buyers.html": "IT知識ゼロから開発会社を動かすRFPを作成する",
    "019-smb-ec-site-development-shopify-cost.html": "Shopify連携で初期費用と維持費を格安に抑える",
    "020-c2c-sharing-matching-platform-development.html": "C2Cシェアリングプラットフォームを安価に構築する",
    "021-custom-workflow-management-tool-cost.html": "自社専用業務管理システムをミニマル開発で低コスト化する",
    "022-pwa-web-app-vs-native-cost-comparison.html": "PWA活用でスマホアプリの開発・保守費用を大幅削減する",
    "023-line-api-chatbot-customer-support-cost.html": "LINE×ChatGPT API連携でカスタマーサポートを自動化する",
    "024-filemaker-access-legacy-modernization.html": "老朽化したFileMaker・AccessをWebシステムへ刷新する",
    "025-web-scraping-automation-marketing-leads.html": "Webスクレイピングで営業リスト作成と分析を自動化する",
    "026-non-it-smb-system-development-no-engineer.html": "エンジニアなしの中小企業でも失敗しない開発体制を整える",
    "027-hiring-vs-outsourcing-cost-comparison.html": "固定費リスクを避け開発外注で圧倒的低コストを実現する",
    "028-excel-to-web-system-dx-cost.html": "エクセルの業務限界をWebシステム化で解消する",
    "029-non-it-smb-genai-business-efficiency.html": "中小企業が生成AIを活用して業務を圧倒的に効率化する",
    "030-smb-system-development-cost-standard.html": "システム開発の費用相場と適正価格を見極める",
    "031-nocode-limitations-real-development-cost.html": "ノーコード開発の限界とスクラッチ開発の損益分岐点",
    "032-non-it-contract-types-risk-management.html": "請負契約と準委任契約の違いと失敗しない選び方",
    "033-simple-rfp-writing-for-non-it-buyers.html": "初心者でも書けるシステム開発RFP作成ガイド",
    "034-smb-ec-site-development-shopify-cost.html": "Shopifyを活用した格安ECサイト構築のポイント",
    "035-2026-genai-b2b-dx-automation.html": "法人向け生成AI×自社業務自動化のROI実証と導入法",
    "035-c2c-sharing-matching-platform-development.html": "パッケージとAPIを駆使したマッチング開発",
    "036-2026-smb-agile-mvp-cost-optimization.html": "中小企業向けアジャイル・MVP開発の費用削減法",
    "036-custom-workflow-management-tool-cost.html": "自社専用業務管理システムを低コストでスクラッチ開発",
    "037-pwa-web-app-vs-native-cost-comparison.html": "PWA（Webアプリ）構築でアプリ開発費を劇的に削減",
    "038-line-api-chatbot-customer-support-cost.html": "LINE公式×ChatGPT API連携構築費用と自動顧客対応",
    "039-filemaker-access-legacy-modernization.html": "FileMaker・AccessのWebシステム移行費用とメリット",
    "040-web-scraping-automation-marketing-leads.html": "Webデータ自動収集・スクレイピング開発費用と活用術",
    "041-non-it-smb-system-development-no-engineer.html": "システム外注で失敗しない防衛策がわかる",
    "rag-chatbot-internal-document-cost.html": "社内データ専用のセキュアなRAGチャットボットを構築する",
    "react-native-app-development-cost.html": "React NativeによるマルチOS同時構築で開発費を圧縮する",
    "system-development-requirements-definition-support.html": "要件定義をブレずに進め開発の後戻りを完全に防ぐ",
    "how-to-reduce-system-development-cost.html": "発注側の交渉術と工夫で開発初期費用を賢く削る",
    "inhouse-vs-outsourcing.html": "開発内製化と外注の最適な役割分担を定義する",
    "requirements-definition-tips.html": "失敗しない要件定義の具体的な進め方を解説する",
    "development-schedule-shortening.html": "システム開発の納期を大幅に短縮する",
    "nocode-vs-scratch.html": "ノーコードの限界とスクラッチ開発の技術選定を行う",
    "contract-types-comparison.html": "請負・準委任・派遣を正しく選び分けコストを最適化する",
    "rfp-development-request.html": "開発会社を動かす正しいRFPの書き方をマスターする",
    "agile-minimalist-dev.html": "アジャイル・ミニマル開発で開発費用を抑える",
    "ai-app-integration.html": "自社システムに生成AIをAPI連携し自動化する",
    "saas-product-launch.html": "SaaS立ち上げ時の外注ステップを最適化する",
    "development-cost-market.html": "システム開発費用の相場を把握し不要コストを削る",
    "offshore-hybrid-development.html": "ハイブリッド体制で高品質・低コスト開発を実現する",
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
    if len(clean) <= 18:
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

def generate_svg(filename, title, category):
    clean_id = re.sub(r"[^a-zA-Z0-9_]", "_", filename.replace(".html", ""))
    theme = get_theme(filename, title, category)
    
    accent = theme["accent"]
    orb1 = theme["orb1"]
    orb2 = theme["orb2"]
    t1, t2, t3 = theme["takeaways"]
    
    # Clean text from mapping or title
    if filename in SUMMARY_MAPPING:
        raw_text = SUMMARY_MAPPING[filename]
    else:
        raw_text = title.split("|")[0].split("—")[0].strip()
        raw_text = re.sub(r"【.*?】", "", raw_text).strip()
        if len(raw_text) > 30:
            raw_text = raw_text[:28] + "..."
            
    lines = split_catchphrase(raw_text)
    
    if len(lines) == 1:
        text_svg = f"""<text x="0" y="200" fill="#FFFFFF" font-size="42" font-family="'Noto Sans JP', sans-serif" font-weight="900" letter-spacing="0.02em">
      {lines[0]}
    </text>"""
    else:
        l1, l2 = lines[0], lines[1]
        text_svg = f"""<text x="0" y="165" fill="#FFFFFF" font-size="40" font-family="'Noto Sans JP', sans-serif" font-weight="900" letter-spacing="0.02em">
      {l1}
    </text>
    <text x="0" y="225" fill="#FFFFFF" font-size="40" font-family="'Noto Sans JP', sans-serif" font-weight="900" letter-spacing="0.02em">
      <tspan fill="{accent}">{l2}</tspan>
    </text>"""

    svg = f"""<svg viewBox="0 0 1000 428" fill="none" xmlns="http://www.w3.org/2000/svg" role="img" aria-label="「{title}」のビジュアルバナー">
  <defs>
    <linearGradient id="bg_{clean_id}" x1="0" y1="0" x2="1000" y2="428" gradientUnits="userSpaceOnUse">
      <stop stop-color="#111B2E"/>
      <stop offset="0.5" stop-color="#1A2740"/>
      <stop offset="1" stop-color="#141E33"/>
    </linearGradient>
    <filter id="blur_{clean_id}" x="0" y="0" width="1000" height="428" filterUnits="userSpaceOnUse">
      <feGaussianBlur stdDeviation="80"/>
    </filter>
  </defs>

  <!-- Clean Background -->
  <rect width="1000" height="428" fill="url(#bg_{clean_id})"/>

  <!-- Soft Ambient Glow Orbs -->
  <circle cx="850" cy="90" r="240" fill="{orb1}" opacity="0.25" filter="url(#blur_{clean_id})"/>
  <circle cx="150" cy="340" r="220" fill="{orb2}" opacity="0.2" filter="url(#blur_{clean_id})"/>

  <!-- Subtle Minimal Grid -->
  <g opacity="0.12" stroke="{accent}" stroke-width="1">
    <line x1="100" y1="0" x2="100" y2="428"/>
    <line x1="250" y1="0" x2="250" y2="428"/>
    <line x1="400" y1="0" x2="400" y2="428"/>
    <line x1="550" y1="0" x2="550" y2="428"/>
    <line x1="700" y1="0" x2="700" y2="428"/>
    <line x1="850" y1="0" x2="850" y2="428"/>
    <line x1="0" y1="100" x2="1000" y2="100"/>
    <line x1="0" y1="214" x2="1000" y2="214"/>
    <line x1="0" y1="328" x2="1000" y2="328"/>
  </g>

  <!-- Pure Content: Clean Typography & Key Bullets Only -->
  <g transform="translate(100, 0)">
    {text_svg}

    <!-- Key Takeaways Bullets (Enlarged 2-Line Subtitle: font-size 24px) -->
    <g transform="translate(0, 295)">
      <text x="0" y="0" fill="#E2E8F0" font-size="24" font-family="'Noto Sans JP', sans-serif" font-weight="700" letter-spacing="0.02em">
        <tspan fill="{accent}">✔</tspan> {t1}　<tspan fill="{accent}">✔</tspan> {t2}
      </text>
      <text x="0" y="42" fill="#E2E8F0" font-size="24" font-family="'Noto Sans JP', sans-serif" font-weight="700" letter-spacing="0.02em">
        <tspan fill="{accent}">✔</tspan> {t3}
      </text>
    </g>
  </g>
</svg>"""
    return svg

def main():
    print("Applying super-clean minimal thumbnail (Background + Text only) to all 96 column articles...")
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
            
        svg = generate_svg(fname, title, cat)
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
