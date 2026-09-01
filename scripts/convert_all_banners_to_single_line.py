import os
import re

SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
WORKSPACE_DIR = os.path.dirname(SCRIPT_DIR)
COLUMN_DIR = os.path.join(WORKSPACE_DIR, "column")

SUMMARY_MAPPING = {
    "inhouse-vs-outsourcing.html": "開発内製化と外注の賢い役割分担",
    "requirements-definition-tips.html": "失敗しない要件定義の進め方",
    "development-schedule-shortening.html": "システム開発の納期を短縮する技術",
    "nocode-vs-scratch.html": "ノーコードの限界とスクラッチの判断基準",
    "contract-types-comparison.html": "請負・準委任・派遣の上手な選び方",
    "rfp-development-request.html": "開発会社を動かす正しいRFPの書き方",
    "agile-minimalist-dev.html": "アジャイル・ミニマル開発でコストを抑える",
    "ai-app-integration.html": "自社システムに生成AIをAPI連携する手順",
    "saas-product-launch.html": "SaaS製品立ち立ち上げ時の賢い外注ステップ",
    "development-cost-market.html": "システム開発費用の相場と賢い削り方",
    "offshore-hybrid-development.html": "ハイブリッド体制で高品質・低コスト開発",
    "new-service-success.html": "新規システム開発を成功に導くポイント",
    "new-service-development.html": "新規サービス開発を成功させる会社選び",
    "minimal-development.html": "新規事業で必要最小限の開発が重要な理由",
    "offshore-labo-contract-tips.html": "オフショア開発「ラボ型契約」の活用ノウハウ",
    "global-offshore-quality-control.html": "オフショア開発で品質を担保する管理手法",
    "llm-fine-tuning-vs-rag.html": "社内データAI活用：RAGか微調整かの判断基準",
    "ai-agent-business-automation.html": "AIエージェントによる業務自動化のロードマップ",
    "llm-providers-comparison.html": "主要LLMの特徴比較と自社に適したモデル選定",
    "genai-vendor-selection-tips.html": "生成AI開発会社を見極めるチェックリスト",
    "genai-market-trends-2026.html": "2026年最新の生成AI市場動向と活用事例",
    "genai-roi-cost-design.html": "生成AI導入時の費用対効果（ROI）最大化法",
    "enterprise-genai-security.html": "企業向け生成AI導入で必須のセキュリティ対策",
    "micro-frontends-architecture.html": "大規模Webシステムを柔軟にスケールさせる設計",
    "agile-requirements-definition.html": "アジャイル開発でブレない要件定義の進め方",
    "mvp-validation-strategy.html": "新規事業を最小コストで検証するMVP戦略",
    "offshore-agile-development.html": "オフショア開発でアジャイルを成功させる方法",
    "ai-agent-implementation.html": "AIエージェントを自社導入する具体手順",
    "history-and-difference-of-generative-ai.html": "生成AIの歴史と従来のAIとの違いを紐解く",
    "future-of-work-with-generative-ai.html": "生成AI時代に生き残る組織と働き方の未来",
    "generative-ai-security-risks.html": "生成AI利用における情報漏洩リスクと対策",
    "generative-ai-prompt-tips.html": "生成AIの回答精度を最大化するプロンプト術",
    "how-to-use-generative-ai-in-business.html": "仕事で今すぐ使える生成AIの業務活用アイデア",
    "which-generative-ai-to-use.html": "人気の生成AIツールの特徴と最適な使い分け",
    "beginner-guide-to-ai-image-generation.html": "画像生成AIの基本と業務で活かす活用法",
    "chatgpt-free-vs-plus.html": "ChatGPTの無料版とPlus（有料版）の機能比較",
    "smartphone-generative-ai-apps.html": "スマホで使える無料の生成AIアプリ活用術",
    "how-to-ask-chatgpt-better-questions.html": "ChatGPTの回答を引き出す上手な質問のしかた",
    "what-generative-ai-can-and-cannot-do.html": "生成AIの得意分野・苦手分野の完全図解",
    "physical-ai-robotics-automation.html": "ものづくりと物流を革新する『フィジカルAI』",
    "api-integration-development.html": "API連携開発で業務システムをシームレスにつなぐ",
    "sovereign-ai-japanese-llm.html": "日本企業のデータ主権を守るソブリンAI",
    "basic-vs-detailed-design.html": "システム開発における基本設計と詳細設計の違い",
    "generative-ai-roi-assessment.html": "生成AI開発の費用対効果を測定するフレームワーク",
    "legacy-system-modernization.html": "古いシステムを安全に刷新するモダナイゼーション",
    "autonomous-ai-agents-digital-workers.html": "自律型AIエージェントが拓くデジタルワークの未来",
    "web-system-security.html": "Webシステムを守るセキュリティ基本対策",
    "system-development-testing.html": "システム開発の不具合を防ぐテスト工程の進め方",
    "system-development-cost-breakdown.html": "システム開発費用の内訳とコストカットの急所",
    "openai-api-pricing-comparison.html": "OpenAI APIの料金体系とコスト最適化のルール",
    "how-to-choose-system-development-vendor.html": "信頼できるシステム開発会社の見極め方",
    "rag-enterprise-search-development.html": "社内データ検索（RAG）システム開発の費用と対策",
    "ai-chatbot-system-development.html": "自社専用AIチャットボット開発の費用とロードマップ",
    "system-development-estimation-details.html": "見積書を正しく読み解き不要な上乗せをカットする",
    "custom-crm-development-cost.html": "独自CRMへの移行で高額なライセンス費をゼロにする",
    "mvp-development-startup-speed.html": "必要十分なミニマル開発で新規事業を最速ローンチ",
    "react-native-app-development-cost.html": "React NativeによるマルチOS同時構築はアプリの開発・保守コストを大幅に圧縮できる。",
    "rag-chatbot-internal-document-cost.html": "社内データ専用のセキュアなRAGチャットボットは安全かつ低コストで構築できる。",
    "system-development-requirements-definition-support.html": "外注先との要件定義をブレずに進めればシステム開発の後戻りは完全に防止できる。",
    "how-to-reduce-system-development-cost.html": "発注側のちょっとした工夫と交渉術だけでシステム開発の初期費用は賢く削減できる。",
    "008-real-estate-crm-custom-development.html": "不動産業特有のフローに適合した独自CRM開発は成約率と業務効率を極限まで高める。",
    "009-logistics-matching-system-cost.html": "運行効率を最大化する物流・配送マッチングシステムは低コストで開発できる。",
    "010-matching-platform-mvp-cost.html": "マッチングプラットフォームのMVP開発は最小限の機能に絞れば低コストで検証できる。"
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
