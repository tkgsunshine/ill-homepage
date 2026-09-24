import os
import re
import glob

SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
WORKSPACE_DIR = os.path.dirname(SCRIPT_DIR)
COLUMN_DIR = os.path.join(WORKSPACE_DIR, "column")

TOPIC_THEMES = {
    "ai": {
        "accent": "#00F0FF",
        "orb1": "#00F0FF",
        "orb2": "#A855F7",
        "takeaways": ("社内データ連携（RAG）", "API連携・自動化", "導入ROIの最大化")
    },
    "data_scraping": {
        "accent": "#22D3EE",
        "orb1": "#06B6D4",
        "orb2": "#3B82F6",
        "takeaways": ("手作業の完全撤廃", "クラウドWebDB化", "保守コスト大幅削減")
    },
    "cloud_infra": {
        "accent": "#38BDF8",
        "orb1": "#0EA5E9",
        "orb2": "#6366F1",
        "takeaways": ("アイドル時コスト削減", "フルマネージド保守", "オートスケール対応")
    },
    "mvp_startup": {
        "accent": "#38BDF8",
        "orb1": "#0EA5E9",
        "orb2": "#818CF8",
        "takeaways": ("最短1ヶ月の市場検証", "コア機能への集中", "低リスク・低コスト開発")
    },
    "offshore": {
        "accent": "#34D399",
        "orb1": "#10B981",
        "orb2": "#0EA5E9",
        "takeaways": ("専任エンジニア確保", "国内人件費の半額水準", "バイリンガルPM直結")
    },
    "management": {
        "accent": "#F59E0B",
        "orb1": "#EAB308",
        "orb2": "#6366F1",
        "takeaways": ("見積もりの適正化", "不要機能の排除", "契約トラブル防止")
    },
    "default": {
        "accent": "#38BDF8",
        "orb1": "#0EA5E9",
        "orb2": "#818CF8",
        "takeaways": ("見積もりの適正化", "不要機能の排除", "契約トラブル防止")
    }
}

# Complete curated mappings for all column articles
BANNER_DATA = {
    # Newly caught-up articles 061 - 065
    "061-ai-agent-custom-workflow-automation.html": {
        "lines": ("自律型AIエージェントによる", "バックオフィス業務の全自動化と費用"),
        "theme": "ai",
        "takeaways": ("複数ツール連携の自律実行", "人的ミスの完全排除", "月数百時間の作業時間削減")
    },
    "062-local-llm-on-premise-security-cost.html": {
        "lines": ("機密データを外部に出さない", "ローカルLLM（社内専用AI）構築"),
        "theme": "ai",
        "takeaways": ("社内閉域網で完全オンプレ", "トークン課金なしで固定費化", "情報漏洩リスクゼロのAI活用")
    },
    "063-modern-web-nextjs-fast-development.html": {
        "lines": ("Next.js×TypeScriptによる", "高速Webシステム開発で保守費削減"),
        "theme": "cloud_infra",
        "takeaways": ("SSR/SSGで超高速表示", "型安全性でバグ発生を抑止", "将来の機能拡張コスト半減")
    },
    "064-multi-tenant-saas-architecture-mvp.html": {
        "lines": ("B2B SaaS立ち上げにおける", "マルチテナント設計とMVP開発費用"),
        "theme": "mvp_startup",
        "takeaways": ("データ完全分離とセキュリティ", "スキーマ共有でインフラ節約", "最短1ヶ月のMVPリリース")
    },
    "065-cloud-cost-reduction-serverless.html": {
        "lines": ("AWS・GCPの月額インフラ費用を", "最大70%削減するサーバーレス移行"),
        "theme": "cloud_infra",
        "takeaways": ("アイドル時コスト完全ゼロ化", "フルマネージドで保守費半減", "オートスケールで負荷耐性向上")
    },

    # 008 - 060 articles
    "008-real-estate-crm-custom-development.html": {
        "lines": ("独自CRM開発で", "不動産業務の成約率を高める"),
        "theme": "mvp_startup",
        "takeaways": ("物件・顧客データ一元化", "追客業務の自動化", "市販パッケージ比50%節約")
    },
    "009-logistics-matching-system-cost.html": {
        "lines": ("配送マッチングシステムを", "低コスト・短納期で構築する"),
        "theme": "mvp_startup",
        "takeaways": ("配車計画の自動最適化", "ドライバーアプリ連携", "MVPで最短2ヶ月ローンチ")
    },
    "010-matching-platform-mvp-cost.html": {
        "lines": ("マッチングプラットフォームの", "MVP開発費を賢く抑える"),
        "theme": "mvp_startup",
        "takeaways": ("ユーザー決済機能の統合", "必要最小限の機能検証", "段階的な追加開発アプローチ")
    },
    "011-non-it-smb-system-development-no-engineer.html": {
        "lines": ("エンジニア不在の中小企業でも", "開発外注で成功する実践手法"),
        "theme": "management",
        "takeaways": ("丸投げを防ぐ要件整理", "専任PMによる伴走体制", "追加費用の発生を徹底予防")
    },
    "012-hiring-vs-outsourcing-cost-comparison.html": {
        "lines": ("エンジニア採用リスクを回避し", "開発外注でコストを抑える"),
        "theme": "management",
        "takeaways": ("採用固定費の完全削減", "必要な時だけの柔軟発注", "即戦力チームの即時稼働")
    },
    "013-excel-to-web-system-dx-cost.html": {
        "lines": ("エクセルの業務限界を", "独自Webシステム化で解消する"),
        "theme": "data_scraping",
        "takeaways": ("データ破損・先祖返り防止", "同時編集と権限管理", "手入力工数を月間80時間削減")
    },
    "014-non-it-smb-genai-business-efficiency.html": {
        "lines": ("生成AI API連携で", "日常の定型業務を全自動化する"),
        "theme": "ai",
        "takeaways": ("書類作成・メール返信の自動化", "自社データ活用チャット", "月額数千円からの低コスト導入")
    },
    "015-smb-system-development-cost-standard.html": {
        "lines": ("システム開発の費用相場と", "見積もり上乗せを防ぐ防衛策"),
        "theme": "management",
        "takeaways": ("人月単価の適正相場", "不要な機能スコープの削減", "相見積もり精査のチェック軸")
    },
    "016-nocode-limitations-real-development-cost.html": {
        "lines": ("ノーコードの限界を見極め", "スクラッチ開発で最適化する"),
        "theme": "mvp_startup",
        "takeaways": ("月額課金肥大化の回避", "自由なDB設計と外部連携", "長期保守コストの最適化")
    },
    "017-non-it-contract-types-risk-management.html": {
        "lines": ("請負と準委任のリスクを回避し", "適正コストで発注する"),
        "theme": "offshore",
        "takeaways": ("契約形態ごとの責任範囲", "仕様変更への柔軟対応", "契約トラブルの未然防止")
    },
    "018-simple-rfp-writing-for-non-it-buyers.html": {
        "lines": ("IT知識ゼロから", "開発会社を動かすRFPを作成する"),
        "theme": "management",
        "takeaways": ("目的と課題の明確化", "必須機能と希望機能の分離", "見積もりブレの徹底防止")
    },
    "019-smb-ec-site-development-shopify-cost.html": {
        "lines": ("Shopify連携で", "初期費用と維持費を格安に抑える"),
        "theme": "mvp_startup",
        "takeaways": ("独自アプリ追加で差別化", "カート放棄率の改善", "決済手数料と保守費の節約")
    },
    "020-c2c-sharing-matching-platform-development.html": {
        "lines": ("C2Cシェアリング基盤を", "安価・セキュアに構築する"),
        "theme": "mvp_startup",
        "takeaways": ("エスクロー決済の実装", "本人確認（eKYC）連携", "スケーラブルな基盤設計")
    },
    "021-custom-workflow-management-tool-cost.html": {
        "lines": ("自社専用業務管理システムを", "ミニマル開発で低コスト化する"),
        "theme": "data_scraping",
        "takeaways": ("自社フローに完全準拠", "不要な機能を削ぎ落とす", "Excel脱却でミス撲滅")
    },
    "022-pwa-web-app-vs-native-cost-comparison.html": {
        "lines": ("PWA活用でスマホアプリの", "開発・保守費用を大幅削減する"),
        "theme": "cloud_infra",
        "takeaways": ("ストア審査・手数料ゼロ", "Webとアプリの単一開発", "プッシュ通知とオフライン対応")
    },
    "023-line-api-chatbot-customer-support-cost.html": {
        "lines": ("LINE×ChatGPT API連携で", "カスタマーサポートを自動化する"),
        "theme": "ai",
        "takeaways": ("24時間365日の自動応答", "有人チャットへの即時切替", "問い合わせ対応工数を70%削減")
    },
    "024-filemaker-access-legacy-modernization.html": {
        "lines": ("老朽化したFileMaker・Accessを", "Webシステムへ刷新する"),
        "theme": "data_scraping",
        "takeaways": ("ブラウザからどこでも操作", "データ移行と整合性担保", "ライセンス費用の完全削減")
    },
    "025-web-scraping-automation-marketing-leads.html": {
        "lines": ("Webスクレイピングで", "営業リスト作成と分析を自動化する"),
        "theme": "data_scraping",
        "takeaways": ("ターゲット企業情報の自動収集", "法的リスクの事前回避", "日次更新で鮮度をキープ")
    },
    "026-non-it-smb-system-development-no-engineer.html": {
        "lines": ("エンジニアなしの中小企業でも", "失敗しない開発体制を整える"),
        "theme": "management",
        "takeaways": ("丸投げを防ぐ要件整理", "専任PMによる伴走体制", "追加費用の発生を徹底予防")
    },
    "027-hiring-vs-outsourcing-cost-comparison.html": {
        "lines": ("固定費リスクを避け", "開発外注で圧倒的低コストを実現"),
        "theme": "management",
        "takeaways": ("採用固定費の完全削減", "必要な時だけの柔軟発注", "即戦力チームの即時稼働")
    },
    "028-excel-to-web-system-dx-cost.html": {
        "lines": ("エクセルの業務限界を", "Webシステム化でスマートに解消"),
        "theme": "data_scraping",
        "takeaways": ("データ破損・先祖返り防止", "同時編集と権限管理", "手入力工数を月間80時間削減")
    },
    "029-non-it-smb-genai-business-efficiency.html": {
        "lines": ("中小企業が生成AIを活用して", "業務を圧倒的に効率化する"),
        "theme": "ai",
        "takeaways": ("書類作成・メール返信の自動化", "自社データ活用チャット", "月額数千円からの低コスト導入")
    },
    "030-smb-system-development-cost-standard.html": {
        "lines": ("システム開発の費用相場と", "適正価格を見極めるチェック法"),
        "theme": "management",
        "takeaways": ("人月単価の適正相場", "不要な機能スコープの削減", "相見積もり精査のチェック軸")
    },
    "031-nocode-limitations-real-development-cost.html": {
        "lines": ("ノーコード開発の限界と", "スクラッチ開発の損益分岐点"),
        "theme": "mvp_startup",
        "takeaways": ("月額課金肥大化の回避", "自由なDB設計と外部連携", "長期保守コストの最適化")
    },
    "032-non-it-contract-types-risk-management.html": {
        "lines": ("請負契約と準委任契約の違いと", "失敗しない発注先の選び方"),
        "theme": "offshore",
        "takeaways": ("契約形態ごとの責任範囲", "仕様変更への柔軟対応", "契約トラブルの未然防止")
    },
    "033-simple-rfp-writing-for-non-it-buyers.html": {
        "lines": ("初心者でも書ける！", "システム開発RFP作成ガイド"),
        "theme": "management",
        "takeaways": ("目的と課題の明確化", "必須機能と希望機能の分離", "見積もりブレの徹底防止")
    },
    "034-smb-ec-site-development-shopify-cost.html": {
        "lines": ("Shopifyを活用した", "格安ECサイト構築のポイント"),
        "theme": "mvp_startup",
        "takeaways": ("独自アプリ追加で差別化", "カート放棄率の改善", "決済手数料と保守費の節約")
    },
    "035-2026-genai-b2b-dx-automation.html": {
        "lines": ("法人向け生成AI×自社業務自動化", "ROI実証と導入ロードマップ"),
        "theme": "ai",
        "takeaways": ("実務フローへのAPI組み込み", "データセキュリティ対策", "投資回収期間の最短化")
    },
    "035-c2c-sharing-matching-platform-development.html": {
        "lines": ("パッケージとAPIを駆使した", "マッチングプラットフォーム開発"),
        "theme": "mvp_startup",
        "takeaways": ("エスクロー決済の実装", "本人確認（eKYC）連携", "スケーラブルな基盤設計")
    },
    "036-2026-smb-agile-mvp-cost-optimization.html": {
        "lines": ("中小企業向けアジャイル・MVP開発", "費用削減とスピード納品の極意"),
        "theme": "mvp_startup",
        "takeaways": ("2週間スプリントでの検証", "無駄な仕様の徹底排除", "初期投資を1/3に圧縮")
    },
    "036-custom-workflow-management-tool-cost.html": {
        "lines": ("自社専用業務管理システムを", "低コストでスクラッチ開発する"),
        "theme": "data_scraping",
        "takeaways": ("自社フローに完全準拠", "不要な機能を削ぎ落とす", "Excel脱却でミス撲滅")
    },
    "037-pwa-web-app-vs-native-cost-comparison.html": {
        "lines": ("PWA（Webアプリ）構築で", "アプリ開発・運用費を劇的削減"),
        "theme": "cloud_infra",
        "takeaways": ("ストア審査・手数料ゼロ", "Webとアプリの単一開発", "プッシュ通知とオフライン対応")
    },
    "038-line-api-chatbot-customer-support-cost.html": {
        "lines": ("LINE公式×ChatGPT API連携", "構築費用と自動顧客対応の実践"),
        "theme": "ai",
        "takeaways": ("24時間365日の自動応答", "有人チャットへの即時切替", "問い合わせ対応工数を70%削減")
    },
    "039-filemaker-access-legacy-modernization.html": {
        "lines": ("FileMaker・Accessの", "Webシステム移行費用とメリット"),
        "theme": "data_scraping",
        "takeaways": ("ブラウザからどこでも操作", "データ移行と整合性担保", "ライセンス費用の完全削減")
    },
    "040-web-scraping-automation-marketing-leads.html": {
        "lines": ("Webデータ自動収集・スクレイピング", "開発費用とマーケティング活用術"),
        "theme": "data_scraping",
        "takeaways": ("ターゲット企業情報の自動収集", "法的リスクの事前回避", "日次更新で鮮度をキープ")
    },
    "041-non-it-smb-system-development-no-engineer.html": {
        "lines": ("システム外注で失敗しない！", "非IT企業のための防衛策ガイド"),
        "theme": "management",
        "takeaways": ("丸投げを防ぐ要件整理", "専任PMによる伴走体制", "追加費用の発生を徹底予防")
    },
    "042-hiring-vs-outsourcing-cost-comparison.html": {
        "lines": ("採用固定費リスクを回避し", "開発外注でコストを抑える"),
        "theme": "management",
        "takeaways": ("採用固定費の完全削減", "必要な時だけの柔軟発注", "即戦力チームの即時稼働")
    },
    "043-excel-to-web-system-dx-cost.html": {
        "lines": ("エクセル業務の限界を", "安価な独自Webシステムで解消"),
        "theme": "data_scraping",
        "takeaways": ("データ破損・先祖返り防止", "同時編集と権限管理", "手入力工数を月間80時間削減")
    },
    "044-non-it-smb-genai-business-efficiency.html": {
        "lines": ("API連携で日常の定型業務を", "生成AIでスマートに自動化する"),
        "theme": "ai",
        "takeaways": ("書類作成・メール返信の自動化", "自社データ活用チャット", "月額数千円からの低コスト導入")
    },
    "045-smb-system-development-cost-standard.html": {
        "lines": ("適正価格を見極め", "見積もりの過剰上乗せを防ぐ"),
        "theme": "management",
        "takeaways": ("人月単価の適正相場", "不要な機能スコープの削減", "相見積もり精査のチェック軸")
    },
    "046-nocode-limitations-real-development-cost.html": {
        "lines": ("ノーコードの罠を見極め", "スクラッチ開発で堅牢に構築"),
        "theme": "mvp_startup",
        "takeaways": ("月額課金肥大化の回避", "自由なDB設計と外部連携", "長期保守コストの最適化")
    },
    "047-non-it-contract-types-risk-management.html": {
        "lines": ("請負と準委任を正しく使い分け", "開発トラブルを未然に防ぐ"),
        "theme": "offshore",
        "takeaways": ("契約形態ごとの責任範囲", "仕様変更への柔軟対応", "契約トラブルの未然防止")
    },
    "048-simple-rfp-writing-for-non-it-buyers.html": {
        "lines": ("IT知識ゼロから書ける！", "RFP作成手順と必須項目"),
        "theme": "management",
        "takeaways": ("目的と課題の明確化", "必須機能と希望機能の分離", "見積もりブレの徹底防止")
    },
    "049-smb-ec-site-development-shopify-cost.html": {
        "lines": ("Shopifyを活用し", "ECサイト開発費用を劇的に抑える"),
        "theme": "mvp_startup",
        "takeaways": ("独自アプリ追加で差別化", "カート放棄率の改善", "決済手数料と保守費の節約")
    },
    "050-c2c-sharing-matching-platform-development.html": {
        "lines": ("パッケージとAPIを駆使した", "マッチングプラットフォーム開発"),
        "theme": "mvp_startup",
        "takeaways": ("エスクロー決済の実装", "本人確認（eKYC）連携", "スケーラブルな基盤設計")
    },
    "051-custom-workflow-management-tool-cost.html": {
        "lines": ("自社専用業務管理システムを", "低コスト・短納期で開発する"),
        "theme": "data_scraping",
        "takeaways": ("自社フローに完全準拠", "不要な機能を削ぎ落とす", "Excel脱却でミス撲滅")
    },
    "052-pwa-web-app-vs-native-cost-comparison.html": {
        "lines": ("PWA（Webアプリ）構築で", "アプリ開発・保守費を削減する"),
        "theme": "cloud_infra",
        "takeaways": ("ストア審査・手数料ゼロ", "Webとアプリの単一開発", "プッシュ通知とオフライン対応")
    },
    "053-line-api-chatbot-customer-support-cost.html": {
        "lines": ("LINE公式×ChatGPT API連携", "構築費用と自動顧客対応の実装"),
        "theme": "ai",
        "takeaways": ("24時間365日の自動応答", "有人チャットへの即時切替", "問い合わせ対応工数を70%削減")
    },
    "054-filemaker-access-legacy-modernization.html": {
        "lines": ("FileMaker・Accessの", "Webシステム移行費用とメリット"),
        "theme": "data_scraping",
        "takeaways": ("ブラウザからどこでも操作", "データ移行と整合性担保", "ライセンス費用の完全削減")
    },
    "055-web-scraping-automation-marketing-leads.html": {
        "lines": ("Webデータ自動収集・スクレイピング", "開発費用とリード獲得活用術"),
        "theme": "data_scraping",
        "takeaways": ("ターゲット企業情報の自動収集", "法的リスクの事前回避", "日次更新で鮮度をキープ")
    },
    "056-non-it-smb-system-development-no-engineer.html": {
        "lines": ("システム外注で失敗しない！", "非IT企業のための防衛策ガイド"),
        "theme": "management",
        "takeaways": ("丸投げを防ぐ要件整理", "専任PMによる伴走体制", "追加費用の発生を徹底予防")
    },
    "057-hiring-vs-outsourcing-cost-comparison.html": {
        "lines": ("採用固定費リスクを回避し", "開発外注でコストを抑える"),
        "theme": "management",
        "takeaways": ("採用固定費の完全削減", "必要な時だけの柔軟発注", "即戦力チームの即時稼働")
    },
    "058-excel-to-web-system-dx-cost.html": {
        "lines": ("エクセル業務の限界を", "安価な独自Webシステムで解消"),
        "theme": "data_scraping",
        "takeaways": ("データ破損・先祖返り防止", "同時編集と権限管理", "手入力工数を月間80時間削減")
    },
    "059-non-it-smb-genai-business-efficiency.html": {
        "lines": ("API連携で日常の定型業務を", "生成AIでスマートに自動化する"),
        "theme": "ai",
        "takeaways": ("書類作成・メール返信の自動化", "自社データ活用チャット", "月額数千円からの低コスト導入")
    },
    "060-smb-system-development-cost-standard.html": {
        "lines": ("適正価格を見極め", "見積もりの過剰上乗せを防ぐ"),
        "theme": "management",
        "takeaways": ("人月単価の適正相場", "不要な機能スコープの削減", "相見積もり精査のチェック軸")
    },

    # General / Named articles
    "agile-minimalist-dev.html": {
        "lines": ("アジャイル・ミニマル開発で", "システム開発費用を賢く抑える"),
        "theme": "mvp_startup",
        "takeaways": ("スプリント単位の柔軟開発", "最小機能での早期ローンチ", "手戻りリスクの最小化")
    },
    "agile-requirements-definition.html": {
        "lines": ("アジャイル開発における", "要件定義の進め方と変更管理"),
        "theme": "management",
        "takeaways": ("ユーザーストーリーの整理", "優先順位の動的コントロール", "ドキュメント工数の削減")
    },
    "ai-agent-business-automation.html": {
        "lines": ("AIエージェントによる", "業務プロセスの自律自動化"),
        "theme": "ai",
        "takeaways": ("複数APIの自律オーケストレーション", "例外処理と人間の承認フロー", "業務効率の飛躍的向上")
    },
    "ai-agent-implementation.html": {
        "lines": ("実務で動くAIエージェントの", "実装手順とアーキテクチャ設計"),
        "theme": "ai",
        "takeaways": ("ツール利用（Function Calling）", "メモリとステート管理", "セキュアな実行環境の構築")
    },
    "ai-app-integration.html": {
        "lines": ("自社システムに生成AIを", "API連携して業務を自動化する"),
        "theme": "ai",
        "takeaways": ("REST APIによる既存DB連携", "リアルタイムデータ処理", "低レイテンシ・安定運用の設計")
    },
    "ai-chatbot-system-development.html": {
        "lines": ("自社専用AIチャットボット開発の", "進め方・費用相場と導入手順"),
        "theme": "ai",
        "takeaways": ("社内FAQ・顧客対応の自動化", "ChatGPT API連携設計", "初期費用と月額運用の最適化")
    },
    "api-integration-development.html": {
        "lines": ("API連携システム開発の基本と", "仕組み・メリット・主要ユースケース"),
        "theme": "cloud_infra",
        "takeaways": ("システム間のデータ自動同期", "SaaS連携による業務効率化", "セキュアな認証・通信設計")
    },
    "autonomous-ai-agents-digital-workers.html": {
        "lines": ("対話型AIから自律実行型へ", "2026年AIエージェントが変える仕事"),
        "theme": "ai",
        "takeaways": ("複数タスクの自律推論・実行", "デジタルワーカーの導入設計", "業務自動化のROI最大化")
    },
    "basic-vs-detailed-design.html": {
        "lines": ("システム開発の成否を分ける", "「基本設計」と「詳細設計」の違い"),
        "theme": "management",
        "takeaways": ("作成ドキュメントの明確化", "発注者と開発側の認識ズレ防止", "手戻りをゼロにする仕様策定")
    },
    "beginner-guide-to-ai-image-generation.html": {
        "lines": ("初心者向けAI画像生成ツールの", "始め方と簡単プロンプトのコツ"),
        "theme": "ai",
        "takeaways": ("商用利用と著作権の注意点", "おすすめ無料ツール比較", "イメージ通りの生成テクニック")
    },
    "chatgpt-free-vs-plus.html": {
        "lines": ("ChatGPT無料版と有料版の違い", "課金すべき基準と費用対効果"),
        "theme": "ai",
        "takeaways": ("GPT-4o/最新モデルの利用可否", "レスポンス速度と機能比較", "ビジネス活用の損益分岐点")
    },
    "contract-types-comparison.html": {
        "lines": ("請負・準委任・派遣を正しく選び分け", "開発コストを最適化する"),
        "theme": "offshore",
        "takeaways": ("契約形態ごとの責任範囲", "アジャイル開発に適した契約", "偽装請負リスクの完全回避")
    },
    "custom-crm-development-cost.html": {
        "lines": ("高額パッケージから脱却する", "自社専用顧客管理（CRM）開発"),
        "theme": "mvp_startup",
        "takeaways": ("月額ライセンス費用の削減", "自社業務に100%フィット", "必要な機能だけに絞ったミニマル開発")
    },
    "development-cost-market.html": {
        "lines": ("システム開発費用の相場を把握し", "不要なコストを賢く削る"),
        "theme": "management",
        "takeaways": ("機能規模ごとの費用相場", "見積もり項目の適正チェック", "予算内で最大成果を出す方法")
    },
    "development-schedule-shortening.html": {
        "lines": ("システム・アプリ開発の", "納期を大幅に短縮する実践手法"),
        "theme": "mvp_startup",
        "takeaways": ("要件のスコープカット", "並行開発とCI/CDの活用", "最短2週間でのスピード納品")
    },
    "enterprise-genai-security.html": {
        "lines": ("企業向け生成AI導入における", "セキュリティ対策とデータガバナンス"),
        "theme": "ai",
        "takeaways": ("プロンプト入力の学習除外設定", "機密情報マスキングと権限管理", "社内AI利用規程の策定支援")
    },
    "future-of-work-with-generative-ai.html": {
        "lines": ("生成AI時代に求められるスキルと", "人とAIが共存するこれからの働き方"),
        "theme": "ai",
        "takeaways": ("定型作業のAIシフト", "人間にしかできないコア価値", "組織のAIリテラシー向上")
    },
    "genai-market-trends-2026.html": {
        "lines": ("2026年生成AI市場の最新動向と", "企業DXにおけるビジネス適用予測"),
        "theme": "ai",
        "takeaways": ("マルチモーダル・自律エージェント", "オンプレミスLLMの台頭", "実用化フェーズの投資戦略")
    },
    "genai-roi-cost-design.html": {
        "lines": ("生成AI導入のROIを最大化する", "コスト設計とPoCの正しい進め方"),
        "theme": "ai",
        "takeaways": ("PoC失敗を防ぐKPI設定", "トークン費用と運用コスト試算", "段階的リリースによるリスク低減")
    },
    "genai-vendor-selection-tips.html": {
        "lines": ("生成AI受託開発会社選びで", "失敗しない選定基準と技術力の見極め"),
        "theme": "ai",
        "takeaways": ("RAG・ファインチューニング実績", "プロンプト設計力とAPI知識", "適正見積もりと開発体制")
    },
    "generative-ai-prompt-tips.html": {
        "lines": ("思い通りの回答を引き出す！", "生成AIプロンプト作成の基本とコツ"),
        "theme": "ai",
        "takeaways": ("明確な役割定義と前提条件", "Few-shotプロンプティング技法", "出力フォーマットの指定法")
    },
    "generative-ai-roi-assessment.html": {
        "lines": ("生成AI導入で本当に効果を出す", "3つの見極め方と投資対効果の測定"),
        "theme": "ai",
        "takeaways": ("削減時間と人件費の可視化", "定量・定性効果の評価軸", "過度な期待を排した現実的導入")
    },
    "generative-ai-security-risks.html": {
        "lines": ("企業の機密データを守る！", "生成AI利用時のセキュリティとリスク"),
        "theme": "ai",
        "takeaways": ("情報漏洩・権利侵害の防止策", "オプトアウト申請の手順", "シャドーAI対策と利用ログ管理")
    },
    "global-offshore-quality-control.html": {
        "lines": ("オフショア開発で手戻りを防ぐ", "品質管理（QA）プロセスと連携の極意"),
        "theme": "offshore",
        "takeaways": ("バイリンガルPMによる仕様徹底", "自動テスト・コードレビュー標準化", "文化ギャップを埋めるコミュニケーション")
    },
    "gpt-6-astra-computer-use-agentic-ai.html": {
        "lines": ("OpenAI GPT-6 Astraの衝撃と", "PC自律操作AIの実務活用法"),
        "theme": "ai",
        "takeaways": ("Computer-Useによる画面自律操作", "複雑な事務作業の完全自動化", "企業DXを変革する次世代基盤")
    },
    "history-and-difference-of-generative-ai.html": {
        "lines": ("生成AIの歴史的変遷と", "従来の識別系AIとの決定的な違い"),
        "theme": "ai",
        "takeaways": ("トランスフォーマーとLLMの進化", "確率モデルと創造性の関係", "ビジネスへの影響と今後の展望")
    },
    "how-to-ask-chatgpt-better-questions.html": {
        "lines": ("ChatGPTの回答精度を高める！", "上手な質問のしかたと実践フレーズ"),
        "theme": "ai",
        "takeaways": ("曖昧さをなくすコンテキスト付与", "段階的思考（CoT）の促し方", "即座に使えるテンプレート集")
    },
    "how-to-choose-system-development-vendor.html": {
        "lines": ("システム開発会社選びで失敗しない", "7つの選定基準と発注のポイント"),
        "theme": "management",
        "takeaways": ("見積もりの透明性と内訳精査", "提案力・コミュニケーション力", "納品後の保守体制と瑕疵担保")
    },
    "how-to-reduce-system-development-cost.html": {
        "lines": ("発注側の工夫と交渉術で", "システム開発の初期費用を賢く削減"),
        "theme": "management",
        "takeaways": ("要件の優先順位付けとミニマル化", "既存SaaS・OSSの積極活用", "適正な発注タイミングと契約選定")
    },
    "how-to-use-generative-ai-in-business.html": {
        "lines": ("仕事で今すぐ使える！", "生成AIの業務活用アイデアと5つの具体例"),
        "theme": "ai",
        "takeaways": ("文章作成・要約・校正の自動化", "データ分析とレポート自動生成", "顧客対応ボット・社内ナレッジ検索")
    },
    "inhouse-vs-outsourcing.html": {
        "lines": ("システム開発の内製化と外注", "最適なバランスとロードマップ"),
        "theme": "management",
        "takeaways": ("コア領域と非コア領域の切り分け", "エンジニア採用・育成コスト比較", "ハイブリッド体制によるリスク分散")
    },
    "legacy-system-modernization.html": {
        "lines": ("塩漬けレガシーシステム刷新", "DXを成功させるマイグレーション手順"),
        "theme": "data_scraping",
        "takeaways": ("ブラックボックス化の解消", "段階的移行（ストラングラー）", "保守コスト大幅削減とセキュリティ強化")
    },
    "llm-fine-tuning-vs-rag.html": {
        "lines": ("社内データのAI活用における", "RAGとファインチューニングの比較選定"),
        "theme": "ai",
        "takeaways": ("更新頻度と学習コストの比較", "ハルシネーション抑制の仕組み", "自社ユースケースに応じた最適選択")
    },
    "llm-providers-comparison.html": {
        "lines": ("OpenAI・Anthropic・Google", "主要LLMベンダーの性能・料金徹底比較"),
        "theme": "ai",
        "takeaways": ("GPT-4o vs Claude 3.5 vs Gemini", "コンテキスト窓とAPIコスト比較", "用途別（コード・推論・翻訳）最適モデル")
    },
    "micro-frontends-architecture.html": {
        "lines": ("大規模Webアプリを分割開発する", "マイクロフロントエンド設計入門"),
        "theme": "cloud_infra",
        "takeaways": ("チームごとの独立デプロイ", "技術スタックの柔軟な混在", "モノリス脱却による開発速度向上")
    },
    "minimal-development.html": {
        "lines": ("ミニマル開発で新規事業を加速", "コスト削減と高速リリースを両立"),
        "theme": "mvp_startup",
        "takeaways": ("コア価値に絞った機能設計", "余分な初期投資の完全排除", "最短サイクルでのユーザー検証")
    },
    "mvp-development-startup-speed.html": {
        "lines": ("新規事業立ち上げにおける", "MVP開発手法と費用を抑える3つの鉄則"),
        "theme": "mvp_startup",
        "takeaways": ("必要最小限の機能要件定義", "ノーコードとコードのハイブリッド", "市場投入までの期間を最短化")
    },
    "mvp-validation-strategy.html": {
        "lines": ("新規事業の仮説検証を成功させる", "MVP開発とユーザーフィードバック収集"),
        "theme": "mvp_startup",
        "takeaways": ("定性・定量データの計測設計", "ピボット判断の迅速化", "無駄な開発費を抑える検証プロセス")
    },
    "new-service-development.html": {
        "lines": ("新規サービス開発の外注で失敗しない", "提案力・技術力・コストの比較ポイント"),
        "theme": "mvp_startup",
        "takeaways": ("要件の解像度を高める提案力", "アジャイル対応の柔軟性", "初期費用と運用費用の透明性")
    },
    "new-service-success.html": {
        "lines": ("新規サービス開発を成功させる！", "失敗を防ぐ5つの実践ガイド"),
        "theme": "mvp_startup",
        "takeaways": ("ユーザー課題の徹底検証", "スコープの肥大化防止", "リリース後の高速改善サイクル")
    },
    "nocode-vs-scratch.html": {
        "lines": ("ノーコードの限界とスクラッチの境界線", "新規事業の失敗しない技術選定基準"),
        "theme": "mvp_startup",
        "takeaways": ("拡張性・セキュリティの制約", "月額ランニングコストの比較", "将来の移行を見据えたアーキテクチャ")
    },
    "offshore-agile-development.html": {
        "lines": ("オフショア開発×アジャイル運用", "リモート体制で成果を出す実践法"),
        "theme": "offshore",
        "takeaways": ("スプリント運用とタスク可視化", "時差と英語・日本語の壁を克服", "継続的インテグレーション（CI/CD）")
    },
    "offshore-hybrid-development.html": {
        "lines": ("日本×ベトナムのハイブリッド体制", "高品質・低コスト開発の新常識"),
        "theme": "offshore",
        "takeaways": ("国内人件費の半額水準で専任確保", "日本語PMによる完全サポート", "仕様理解と品質の確実な担保")
    },
    "offshore-labo-contract-tips.html": {
        "lines": ("オフショア開発ラボ型（準委任）契約で", "自社専用開発チームを構築・拡大"),
        "theme": "offshore",
        "takeaways": ("柔軟な仕様変更と優先度調整", "ノウハウの社内蓄積と体制固定", "契約リスクの回避と適正単価")
    },
    "openai-api-pricing-comparison.html": {
        "lines": ("OpenAI API料金体系と計算方法", "コストを劇的に下げるシステム設計"),
        "theme": "ai",
        "takeaways": ("トークン消費の最適化テクニック", "プロンプトキャッシュとバッチAPI活用", "モデル使い分けによる費用半減")
    },
    "physical-ai-robotics-automation.html": {
        "lines": ("画面を飛び出すフィジカルAIと", "ものづくり・物流の自動化革命"),
        "theme": "ai",
        "takeaways": ("ロボティクス×AIの最新トレンド", "人手不足を解決する現場自動化", "エッジAIとセンシング技術")
    },
    "rag-chatbot-internal-document-cost.html": {
        "lines": ("社内データ専用のセキュアな", "RAGチャットボットを安全・低コスト構築"),
        "theme": "ai",
        "takeaways": ("自社独自マニュアル・規程の即時検索", "Azure OpenAI等の閉域環境", "情報漏洩ゼロの権限分離設計")
    },
    "rag-enterprise-search-development.html": {
        "lines": ("社内データを安全に活用する", "RAG（検索拡張生成）の仕組みと開発相場"),
        "theme": "ai",
        "takeaways": ("ベクトル検索とLLMの融合", "チャンキングと検索精度の最適化", "PoCから本番運用へのロードマップ")
    },
    "react-native-app-development-cost.html": {
        "lines": ("React NativeによるマルチOS開発で", "スマホアプリ開発・保守費を大幅圧縮"),
        "theme": "cloud_infra",
        "takeaways": ("iOS/Android単一コードベース", "ネイティブ同等の快適な操作性", "ストア審査・アップデート工数の削減")
    },
    "requirements-definition-tips.html": {
        "lines": ("システム開発の要件定義で失敗しない！", "非エンジニア向け仕様策定ガイド"),
        "theme": "management",
        "takeaways": ("ビジネス要件をシステム要件へ翻訳", "5W1Hで曖昧さを排除", "スコープ定義で予算オーバー防止")
    },
    "rfp-development-request.html": {
        "lines": ("開発会社を本気にさせる！", "失敗しないRFP（提案依頼書）の書き方"),
        "theme": "management",
        "takeaways": ("発注背景と目的の明確化", "必須要件と希望要件の切り分け", "見積もり精度を高める前提条件の提示")
    },
    "saas-product-launch.html": {
        "lines": ("SaaS立ち上げで失敗しない", "MVPからスケールまでの外注ステップ"),
        "theme": "mvp_startup",
        "takeaways": ("マルチテナントと課金設計", "スピード最優先のMVPリリース", "拡張性を担保したクラウド設計")
    },
    "smartphone-generative-ai-apps.html": {
        "lines": ("スマホで使えるおすすめ生成AI！", "移動中に業務効率化するアプリ活用術"),
        "theme": "ai",
        "takeaways": ("音声入力による議事録作成", "カメラ画像からのテキスト抽出", "外出先でのアイデア出し・要約")
    },
    "sovereign-ai-japanese-llm.html": {
        "lines": ("データ主権を守るソブリンAIと", "日本企業のためのセキュアなAI選び"),
        "theme": "ai",
        "takeaways": ("国内データセンターでの運用", "海外クラウド依存リスクの回避", "日本語特化LLMの性能と活用例")
    },
    "system-development-cost-breakdown.html": {
        "lines": ("システム開発費用の相場と内訳", "見積書で損をしないためのチェックリスト"),
        "theme": "management",
        "takeaways": ("人月単価と工程別コストの内訳", "過剰なバッファを見抜く方法", "適正価格での契約交渉テクニック")
    },
    "system-development-estimation-details.html": {
        "lines": ("システム開発見積書の「項目」の正しい見方", "発注側が損をしないチェックポイント"),
        "theme": "management",
        "takeaways": ("ディレクション費・PM費の妥当性", "仕様変更・追加開発の条件確認", "保守運用費の適正相場")
    },
    "system-development-requirements-definition-support.html": {
        "lines": ("外注先との要件定義をブレずに進め", "システム開発の手戻りを完全防止"),
        "theme": "management",
        "takeaways": ("画面モックアップによる事前合意", "例外処理・権限設計の網羅", "開発フェーズでの追加費用ゼロ化")
    },
    "system-development-testing.html": {
        "lines": ("システム開発テスト工程の重要性と", "不具合・バグを防ぐ品質管理プロセス"),
        "theme": "management",
        "takeaways": ("単体・結合・受入テストの違い", "テストシナリオの網羅性確保", "本番リリース時の障害リスク回避")
    },
    "web-system-security.html": {
        "lines": ("Webシステムのセキュリティ対策入門", "企業が最初に行うべき脆弱性対策"),
        "theme": "management",
        "takeaways": ("SQLインジェクション・XSS防御", "SSL暗号化とWAFの導入", "定期的な脆弱性診断とアクセス監視")
    },
    "what-generative-ai-can-and-cannot-do.html": {
        "lines": ("図解：生成AIのできること・できないこと", "得意分野と苦手な作業をスッキリ理解"),
        "theme": "ai",
        "takeaways": ("文章作成・コード生成の圧倒的速さ", "最新情報・論理計算の注意点", "人間による確認（ファクトチェック）の必要性")
    },
    "which-generative-ai-to-use.html": {
        "lines": ("ChatGPT・Gemini・Claude", "初心者向け！主要生成AIの違いと選び方"),
        "theme": "ai",
        "takeaways": ("文章力・コーディング力の比較", "無料プランと有料プランの機能差", "自社の利用目的に合った最適ツール")
    }
}

def split_catchphrase_smart(text):
    clean = " ".join(re.sub(r"<[^>]+>", "", text).split())
    clean = re.sub(r"【.*?】", "", clean).split("|")[0].split("—")[0].strip()
    clean = clean.rstrip("。").strip()
    
    if not clean:
        return ["システム開発の要点と", "失敗を防ぐ実践アプローチ"]
    if len(clean) <= 18:
        return [clean]
    
    best_idx = len(clean) // 2
    best_score = -9999
    particles = ["で", "と", "に", "を", "は", "が", "の", "や", "・", "も", "から", "にて", "し"]
    for i in range(4, len(clean) - 4):
        diff = abs(i - (len(clean) - i))
        score = -diff * 1.5
        if clean[i-1] in particles:
            score += 15
        if i >= 2 and clean[i-2:i] in ["による", "した", "での", "への", "から", "における"]:
            score += 18
        if score > best_score:
            best_score = score
            best_idx = i
    return [clean[:best_idx], clean[best_idx:]]

def generate_svg(filename, title, category):
    clean_id = re.sub(r"[^a-zA-Z0-9_]", "_", filename.replace(".html", ""))
    
    if filename in BANNER_DATA:
        data = BANNER_DATA[filename]
        lines = data["lines"]
        theme_key = data.get("theme", "default")
        theme = TOPIC_THEMES.get(theme_key, TOPIC_THEMES["default"])
        takeaways = data.get("takeaways", theme["takeaways"])
    else:
        # Fallback without ANY truncation
        theme = TOPIC_THEMES["default"]
        text_lower = (filename + " " + title + " " + category).lower()
        for k in ["ai", "data_scraping", "cloud_infra", "mvp_startup", "offshore", "management"]:
            if k in text_lower:
                theme = TOPIC_THEMES[k]
                break
        lines = split_catchphrase_smart(title)
        takeaways = theme["takeaways"]

    accent = theme["accent"]
    orb1 = theme["orb1"]
    orb2 = theme["orb2"]
    t1, t2, t3 = takeaways

    if len(lines) == 1:
        font_size = 40 if len(lines[0]) <= 20 else 36
        text_svg = f"""<text x="0" y="200" fill="#FFFFFF" font-size="{font_size}" font-family="'Noto Sans JP', sans-serif" font-weight="900" letter-spacing="0.02em">
      {lines[0]}
    </text>"""
    else:
        l1, l2 = lines[0], lines[1]
        max_len = max(len(l1), len(l2))
        font_size = 40 if max_len <= 20 else 36
        text_svg = f"""<text x="0" y="165" fill="#FFFFFF" font-size="{font_size}" font-family="'Noto Sans JP', sans-serif" font-weight="900" letter-spacing="0.02em">
      {l1}
    </text>
    <text x="0" y="225" fill="#FFFFFF" font-size="{font_size}" font-family="'Noto Sans JP', sans-serif" font-weight="900" letter-spacing="0.02em">
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
    print("Applying super-clean minimal thumbnail with full mapping to all column articles...")
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
