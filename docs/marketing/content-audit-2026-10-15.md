# コラム内容の重複・薄さの調査（2026-10-15）

対象: ill-inc.net のコラム 124本（`column/*.html` の本文）。

## 調べ方
各記事の本文を、段落・箇条書き・表のセル単位に分け、ほかの5本以上の記事にも、まったく同じ文章で出てくる部分の割合（共通率）を数えた。サイドバー・相談ボタンなど記事ごとに変わらない定型部分も本文欄に含まれるため、実際の重なりは、この数字よりやや小さい。

## 結果
- 平均の本文量: 約2342字／平均の共通率: 41%
- 共通率が9割以上: 11本／5〜9割: 27本／5割未満: 86本

## 最優先: 本文がほぼ同じ記事（共通率9割以上）
同じ「AIエージェント」の本文が、題名だけ違う別テーマの記事に入っている。題名と本文の内容も一致していない。

| 共通率 | 本文量 | ファイル | 題名 |
|---|---|---|---|
| 98% | 2810 | `enterprise-genai-security.html` | 企業向け生成AI導入におけるセキュリティ対策とデータガバナンス構築の極意 |
| 97% | 2812 | `genai-market-trends-2026.html` | 【2026年予測】生成AIの市場動向とビジネス適用の最新トレンド |
| 97% | 2813 | `genai-vendor-selection-tips.html` | 生成AI受託開発会社選びで失敗しないための選定基準と「技術力の強み」の見極め方 |
| 97% | 2813 | `genai-roi-cost-design.html` | 生成AI導入の投資対効果（ROI）を最大化するコスト設計とPoC（概念実証）の正しい進め方 |
| 97% | 2814 | `offshore-agile-development.html` | オフショア開発におけるアジャイル運用の実践法 |
| 97% | 2817 | `mvp-validation-strategy.html` | 新規事業立ち上げにおけるMVP検証手法 |
| 97% | 2817 | `micro-frontends-architecture.html` | マイクロフロントエンド設計入門 |
| 97% | 2821 | `ai-agent-implementation.html` | 業務に自律型AIエージェントを組み込む手法 |
| 97% | 2821 | `agile-requirements-definition.html` | アジャイル要件定義の失敗を避ける手法 |
| 97% | 2837 | `llm-providers-comparison.html` | 【2026年最新】主要LLMベンダー徹底比較 |
| 96% | 2847 | `ai-agent-business-automation.html` | AIエージェントを活用した業務自動化の最前線 — 導入ステップと開発事例 |

## 次に見直す: 共通率5〜9割の記事
| 共通率 | 本文量 | ファイル | 題名 |
|---|---|---|---|
| 70% | 2032 | `015-smb-system-development-cost-standard.html` | システム開発の適正価格とは？見積もり上乗せを防ぐチェックリスト |
| 69% | 2058 | `021-custom-workflow-management-tool-cost.html` | 業務管理システムの独自開発費用｜過剰機能を削って低コストで構築 |
| 69% | 2068 | `012-hiring-vs-outsourcing-cost-comparison.html` | エンジニア採用と開発外注のコスト比較｜固定費リスクで見る判断基準 |
| 68% | 2072 | `016-nocode-limitations-real-development-cost.html` | ノーコードの限界とスクラッチ開発の損益分岐点｜費用が高騰する前に |
| 68% | 2072 | `014-non-it-smb-genai-business-efficiency.html` | 中小企業の生成AI活用｜API連携で定型業務を自動化する方法と費用 |
| 68% | 2073 | `011-non-it-smb-system-development-no-engineer.html` | エンジニアがいない中小企業のシステム開発外注｜騙されないための防衛策 |
| 68% | 2075 | `025-web-scraping-automation-marketing-leads.html` | Webスクレイピング自動収集システムの開発費用｜営業リスト作成を自動化 |
| 68% | 2078 | `022-pwa-web-app-vs-native-cost-comparison.html` | PWAとネイティブアプリの開発費用比較｜ストア申請不要でコスト削減 |
| 68% | 2080 | `019-smb-ec-site-development-shopify-cost.html` | ECサイト構築はShopifyが安い？初期費用・維持費を自社開発と比較 |
| 68% | 2083 | `018-simple-rfp-writing-for-non-it-buyers.html` | RFP（提案依頼書）の書き方｜IT知識ゼロでも開発会社に伝わる作り方 |
| 68% | 2085 | `017-non-it-contract-types-risk-management.html` | 請負契約と準委任契約の違い｜システム開発のリスクを避ける発注の基本 |
| 68% | 2088 | `system-development-estimation-details.html` | システム開発の見積書にある「項目」の正しい見方と、発注側が損をしないためのチェックポイント |
| 68% | 2088 | `013-excel-to-web-system-dx-cost.html` | ExcelからWebシステムへ移行する費用と効果｜業務の限界を解消するDX |
| 68% | 2096 | `024-filemaker-access-legacy-modernization.html` | FileMaker・AccessからWebシステムへの移行費用と手順｜脱レガシー |
| 67% | 2102 | `010-matching-platform-mvp-cost.html` | マッチングプラットフォームのMVP開発は最小限の機能に絞れば低コストで検証できる。 |
| 67% | 2124 | `020-c2c-sharing-matching-platform-development.html` | C2Cマッチングサイト・シェアリングサービスの開発費用と安く作る方法 |
| 66% | 2134 | `system-development-requirements-definition-support.html` | 外注先との要件定義をブレずに進めればシステム開発の後戻りは完全に防止できる。 |
| 66% | 2146 | `how-to-reduce-system-development-cost.html` | 発注側のちょっとした工夫と交渉術だけでシステム開発の初期費用は賢く削減できる。 |
| 66% | 2155 | `mvp-development-startup-speed.html` | 【スピード重視】新規事業立ち上げにおける最小限のシステム開発（MVP）手法と費用を抑える3つの鉄則 |
| 66% | 2161 | `rag-chatbot-internal-document-cost.html` | 社内データ専用のセキュアなRAGチャットボットは安全かつ低コストで構築できる。 |
| 65% | 2182 | `react-native-app-development-cost.html` | React NativeによるマルチOS同時構築はアプリの開発・保守コストを大幅に圧縮できる。 |
| 60% | 1401 | `067-api-first-microservices-cost-advantage.html` | APIファースト設計がもたらすシステム拡張性と開発コスト削減メリット。 |
| 57% | 1332 | `069-b2b-customer-portal-development.html` | 取引先専用のB2B受発注・顧客ポータルサイト構築の費用相場とメリット。 |
| 57% | 1337 | `070-agile-sprint-cost-control-method.html` | アジャイル開発で予算オーバーを防ぎ、納期通りに納品するスプリント管理術。 |
| 56% | 1494 | `065-cloud-cost-reduction-serverless.html` | AWS・GCPの月額インフラ費用を最大70%削減するサーバーレス移行設計。 |
| 54% | 1415 | `063-modern-web-nextjs-fast-development.html` | Next.jsとTypeScriptによる高速Webシステム開発が保守費用を劇的に下げる理由。 |
| 54% | 1607 | `061-ai-agent-custom-workflow-automation.html` | 自律型AIエージェントによるバックオフィス業務の全自動化と導入費用相場。 |

## 対応方針
1. 本文がほぼ同じ記事は、題名のテーマに合う本文に書き直す（固有の内容を本文の7割以上にする）。書き直せないものは、近いテーマの記事へ統合して301リダイレクトする（REGULATIONS 第10条）。
2. 共通率5〜9割の記事は、固有の内容を足す。費用の表は、記事のテーマに合った内容にする。
3. 新しい記事は、共通の導入文を入れず、固有の内容を本文の7割以上にする（REGULATIONS 第9条を改訂済み）。
