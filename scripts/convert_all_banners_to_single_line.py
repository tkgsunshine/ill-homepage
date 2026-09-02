import os
import re

SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
WORKSPACE_DIR = os.path.dirname(SCRIPT_DIR)
COLUMN_DIR = os.path.join(WORKSPACE_DIR, "column")

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

def split_text(text):
    if len(text) <= 18:
        return [text]
    
    best_idx = len(text) // 2
    best_score = -9999
    particles = ["で", "と", "に", "を", "は", "が", "の", "や", "・", "も", "から", "にて"]
    
    for i in range(5, len(text) - 5):
        diff = abs(i - (len(text) - i))
        score = -diff * 1.5
        
        # Check particle splitting
        if text[i-1] in particles:
            score += 15
        if i >= 2 and text[i-2:i] in ["による", "した", "での", "への"]:
            score += 18
            
        if score > best_score:
            best_score = score
            best_idx = i
            
    return [text[:best_idx], text[best_idx:]]

def main():
    print("Starting conversion of all column banners with unique SVG IDs (supporting 2-line split)...")
    if not os.path.exists(COLUMN_DIR):
        print(f"Column directory not found: {COLUMN_DIR}")
        return

    updated_count = 0
    for filename in os.listdir(COLUMN_DIR):
        if not filename.endswith(".html") or filename == "index.html":
            continue

        filepath = os.path.join(COLUMN_DIR, filename)
        with open(filepath, "r", encoding="utf-8") as f:
            content = f.read()

        summary_text = SUMMARY_MAPPING.get(filename)
        if not summary_text:
            print(f"Warning: No mapped summary for {filename}, skipping.")
            continue

        # Extract Category
        cat_match = re.search(r'<span class="article-category">([^<]+)</span>', content)
        category = cat_match.group(1) if cat_match else "SYSTEM DEVELOPMENT"

        # Extract H1 title
        h1_match = re.search(r'<h1 class="article-title">(.*?)</h1>', content)
        h1_title = h1_match.group(1) if h1_match else summary_text

        # Extract English Title
        eng_match = re.search(r'y="270"[^>]*>([^<]+)</text>', content)
        if not eng_match:
            eng_match = re.search(r'y="180"[^>]*>([^<]+)</text>', content)
        if not eng_match:
            eng_match = re.search(r'Outfit[^>]*>([^<]+)</text>', content)
        eng_title = eng_match.group(1).strip() if eng_match else "TECHNOLOGY INSIGHTS"

        # Suffix
        clean_name = filename.replace(".html", "").replace("-", "_")

        # Split text into 1 or 2 lines
        lines = split_text(summary_text)
        font_size = 38
        if len(lines) == 1:
            if len(lines[0]) > 25:
                font_size = 32
            text_element = f'<text x="500" y="240" text-anchor="middle" fill="url(#text-grad-{clean_name})" font-size="{font_size}" font-family="\'Noto Sans JP\', sans-serif" font-weight="900" letter-spacing="0.05em">{lines[0]}</text>'
        else:
            max_len = max(len(lines[0]), len(lines[1]))
            if max_len > 22:
                font_size = 32
            text_element = f'''<text x="500" y="210" text-anchor="middle" fill="url(#text-grad-{clean_name})" font-size="{font_size}" font-family="\'Noto Sans JP\', sans-serif" font-weight="900" letter-spacing="0.05em">{lines[0]}</text>
          <text x="500" y="270" text-anchor="middle" fill="url(#text-grad-{clean_name})" font-size="{font_size}" font-family="\'Noto Sans JP\', sans-serif" font-weight="900" letter-spacing="0.05em">{lines[1]}</text>'''

        # Make friendly single-line or double-line light-slate SVG with unique gradient IDs
        new_svg = f"""<svg viewBox="0 0 1000 428" fill="none" xmlns="http://www.w3.org/2000/svg" role="img" aria-label="「{h1_title}」のビジュアルバナー">
          <defs>
            <linearGradient id="bg-grad-{clean_name}" x1="0" y1="0" x2="1000" y2="428" gradientUnits="userSpaceOnUse">
              <stop stop-color="#F1F5F9" />
              <stop offset="0.5" stop-color="#E2E8F0" />
              <stop offset="1" stop-color="#CBD5E1" />
            </linearGradient>
            <linearGradient id="text-grad-{clean_name}" x1="0" y1="0" x2="800" y2="0" gradientUnits="userSpaceOnUse">
              <stop stop-color="#0EA5E9" />
              <stop offset="1" stop-color="#10B981" />
            </linearGradient>
          </defs>
          <rect width="1000" height="428" fill="url(#bg-grad-{clean_name})"/>
          
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
          <text x="500" y="270" text-anchor="middle" fill="#0EA5E9" font-size="90" font-family="'Outfit', sans-serif" font-weight="900" opacity="0.05" letter-spacing="0.1em">{eng_title}</text>
          
          <!-- Corner Lines -->
          <line x1="50" y1="50" x2="150" y2="50" stroke="#0EA5E9" stroke-width="2" opacity="0.6"/>
          <line x1="50" y1="50" x2="50" y2="150" stroke="#0EA5E9" stroke-width="2" opacity="0.6"/>
          
          <line x1="950" y1="378" x2="850" y2="378" stroke="#10B981" stroke-width="2" opacity="0.6"/>
          <line x1="950" y1="378" x2="950" y2="278" stroke="#10B981" stroke-width="2" opacity="0.6"/>

          <!-- Centered Main message (1 or 2 lines) -->
          {text_element}
          
          <path d="M0 428 L1000 428" stroke="var(--glass-border)" stroke-width="1"/>
        </svg>"""

        # Replace main visual block
        new_content, count = re.subn(r'(?s)<div class="article-main-visual">.*?</div>', f'<div class="article-main-visual">\n        {new_svg}\n      </div>', content)
        if count > 0:
            with open(filepath, "w", encoding="utf-8") as f:
                f.write(new_content)
            print(f"  - Converted banner in {filename}")
            updated_count += 1

    print(f"\nCompleted! Rebuilt all {updated_count} banners with unique SVG gradient IDs.")

if __name__ == "__main__":
    main()
