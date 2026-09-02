import os
import re

SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
WORKSPACE_DIR = os.path.dirname(SCRIPT_DIR)
COLUMN_DIR = os.path.join(WORKSPACE_DIR, "column")

SUMMARY_MAPPING = {
    "008-real-estate-crm-custom-development.html": "不動産業向け独自CRM開発のメリット",
    "009-logistics-matching-system-cost.html": "物流・配送マッチングシステムの構築費用",
    "010-matching-platform-mvp-cost.html": "マッチングプラットフォームのMVP低コスト開発",
    "011-non-it-smb-system-development-no-engineer.html": "エンジニア不在の中小企業向け外注防衛策",
    "012-hiring-vs-outsourcing-cost-comparison.html": "社内エンジニア採用リスクと外注費用比較",
    "013-excel-to-web-system-dx-cost.html": "エクセル業務限界を解消するWebシステム化",
    "014-non-it-smb-genai-business-efficiency.html": "IT担当者不要の生成AI API業務自動化",
    "015-smb-system-development-cost-standard.html": "システム開発の見積もり上乗せ防止策",
    "016-nocode-limitations-real-development-cost.html": "ノーコードの限界とスクラッチ開発の損益分岐点",
    "017-non-it-contract-types-risk-management.html": "発注者が知るべき請負と準委任のリスク回避",
    "018-simple-rfp-writing-for-non-it-buyers.html": "IT知識ゼロから書けるRFP作成ノウハウ",
    "019-smb-ec-site-development-shopify-cost.html": "Shopifyを活用した低コストEC構築",
    "020-c2c-sharing-matching-platform-development.html": "C2Cシェアリングプラットフォーム開発費用",
    "021-custom-workflow-management-tool-cost.html": "自社専用業務管理ツールのミニマル開発",
    "022-pwa-web-app-vs-native-cost-comparison.html": "PWA（Webアプリ）活用によるアプリ開発費削減",
    "023-line-api-chatbot-customer-support-cost.html": "LINE×ChatGPT APIによる顧客対応自動化",
    "024-filemaker-access-legacy-modernization.html": "FileMaker・AccessのWebシステム移行",
    "025-web-scraping-automation-marketing-leads.html": "Webスクレイピングによる営業リスト自動化",
    "026-non-it-smb-system-development-no-engineer.html": "エンジニアなしの中小企業向けシステム開発体制",
    "027-hiring-vs-outsourcing-cost-comparison.html": "エンジニア採用リスクと開発外注のコストメリット",
    "rag-chatbot-internal-document-cost.html": "社内データ専用セキュアRAG構築費用",
    "react-native-app-development-cost.html": "React Nativeによるアプリ開発費削減",
    "system-development-requirements-definition-support.html": "要件定義の後戻りを防ぐ開発進め方",
    "how-to-reduce-system-development-cost.html": "発注側の交渉術による開発初期費用削減",
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
