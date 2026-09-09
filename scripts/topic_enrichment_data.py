# Shared Topic Enrichment Data for Automated Columns
TOPIC_CONFIGS = {
    'crm': {
        'keywords': ['crm', '顧客管理'],
        'h2_title': '独自CRM・顧客管理システム開発の費用相場と大手SIer比較',
        'table_html': '''<div class="article-table-wrapper">
  <table class="article-table">
    <thead>
      <tr>
        <th>開発規模・用途</th>
        <th>主な機能要件</th>
        <th>一般的な受託相場</th>
        <th>Ill（イル）株式会社</th>
        <th>想定工期</th>
      </tr>
    </thead>
    <tbody>
      <tr>
        <td><strong>スモールCRM（10名規模）</strong></td>
        <td>顧客一覧、商談ステータス管理、検索、CSV入出力</td>
        <td>300万〜500万円</td>
        <td><strong>100万〜180万円</strong></td>
        <td>約1ヶ月</td>
      </tr>
      <tr>
        <td><strong>標準CRM（30〜50名規模）</strong></td>
        <td>権限管理、LINE・メール自動連携、帳票・見積書PDF出力</td>
        <td>600万〜1,200万円</td>
        <td><strong>200万〜350万円</strong></td>
        <td>約2ヶ月</td>
      </tr>
      <tr>
        <td><strong>高機能CRM（100名以上）</strong></td>
        <td>AI自動マッチング、反響自動集計、外部基幹・会計API連携</td>
        <td>1,500万〜3,000万円</td>
        <td><strong>450万〜800万円</strong></td>
        <td>約3〜4ヶ月</td>
      </tr>
    </tbody>
  </table>
</div>''',
        'explanation_html': '''<h3>独自CRM開発で圧倒的な低コスト・高ROIを実現できる3つの理由</h3>
<p>大手SIerや一般的なシステム開発会社に見積もりを依頼すると、顧客管理システムの開発は平気で1,000万円を超えるケースが後を絶ちません。これに対し、<strong>Ill（イル）株式会社</strong> では以下の技術的アプローチにより、半額以下の適正価格で高品質なスクラッチ開発を実現しています。</p>
<ul>
  <li><strong>中間マージン・多重下請けの完全排除</strong>: 大手SIerのように元請け営業や中間ディレクターを挟まず、弊社の専任リードエンジニアが直接要件定義から実装までをワンストップで担当します。</li>
  <li><strong>生成AIによるコーディング・テスト工数の極小化</strong>: 最新のAIコーディング環境（Claude Code / GitHub Copilot）および独自CI/CDテスト自動化基盤を活用し、従来エンジニアが手作業で書いていた定型コードを自動生成して人件費を圧縮します。</li>
  <li><strong>パッケージ月額ライセンス費の完全撤廃</strong>: SalesforceやHubSpotなどのSaaSはユーザー数（アカウント数）に応じた従量課金が発生し、社員が増えるほど年間数百万円の固定費が垂れ流しになります。独自開発CRMならユーザー数無制限で自社サーバー（AWS/GCP）にて固定数千円〜数万円で運用可能です。</li>
</ul>''',
        'extra_faqs': [
            ('Q. Salesforceや既存ツールからのデータ移行は可能ですか？',
             'A. はい、完全に可能です。既存システムからエクスポートしたCSVやデータベースを抽出し、データクレンジングを行った上で新CRMへスムーズにデータ移行を実施いたします。'),
            ('Q. 開発後に自社の業務フローが変わった場合、機能の追加・変更はできますか？',
             'A. もちろん可能です。拡張性の高いオープンソース技術（React / TypeScript / Node.js / PostgreSQL等）で設計しているため、ベンダーロックインがなく、将来の要件追加や画面改修も柔軟に行えます。')
        ]
    },
    'logistics': {
        'keywords': ['logistics', '物流', '配車'],
        'h2_title': '物流・配車マッチングシステムの開発費用相場と機能別内訳',
        'table_html': '''<div class="article-table-wrapper">
  <table class="article-table">
    <thead>
      <tr>
        <th>システム規模</th>
        <th>実装機能</th>
        <th>一般的な受託相場</th>
        <th>Ill（イル）株式会社</th>
        <th>開発期間</th>
      </tr>
    </thead>
    <tbody>
      <tr>
        <td><strong>MVP（基本検証版）</strong></td>
        <td>荷主・ドライバー登録、案件一覧、手動マッチング、簡易チャット</td>
        <td>400万〜700万円</td>
        <td><strong>150万〜250万円</strong></td>
        <td>1〜1.5ヶ月</td>
      </tr>
      <tr>
        <td><strong>標準配車システム</strong></td>
        <td>GPS位置トラッキング、最適ルート計算API、運行状況ステータス</td>
        <td>900万〜1,800万円</td>
        <td><strong>300万〜500万円</strong></td>
        <td>2〜3ヶ月</td>
      </tr>
      <tr>
        <td><strong>大規模求荷求車基盤</strong></td>
        <td>自動エスクロー決済、請求書・日報自動発行、ドライバー相互評価</td>
        <td>2,000万〜4,000万円</td>
        <td><strong>600万〜1,000万円</strong></td>
        <td>3〜4ヶ月</td>
      </tr>
    </tbody>
  </table>
</div>''',
        'explanation_html': '''<h3>物流現場特有の要件を低コストで開発するポイント</h3>
<p>物流業界の2024年問題やドライバー不足に対応するため、運行効率を最大化する独自システムの導入が急務となっています。しかし、汎用パッケージでは荷物の規格や現場の細かな受け渡しフローに対応できず、かといって従来型開発では工数が肥大化します。</p>
<p>Ill（イル）株式会社では、Google Maps APIやMapbox等のモダンな地図・ルーティングAPIを効率的に組み合わせ、現場のスマートフォンから直感的に操作できるレスポンシブなWeb/PWAとして構築することで、アプリストア審査の手間と端末ごとの開発費を最小化します。</p>''',
        'extra_faqs': [
            ('Q. ドライバーが高齢でITに不慣れでも使えますか？',
             'A. 直感的に操作できるよう、LINE連携やタップのみで完了する大きなボタン配置など、UI/UXを極限までシンプルに設計します。'),
            ('Q. インフラの維持費（サーバー代など）は月額いくらくらいかかりますか？',
             'A. クラウドの従量課金サーバー（AWS/Cloud Run等）を活用するため、利用ユーザー数や案件数に応じたミニマル設計で、月額数千円〜2万円程度から運用可能です。')
        ]
    },
    'matching': {
        'keywords': ['matching', 'c2c', 'シェアリング', 'プラットフォーム'],
        'h2_title': 'マッチングプラットフォーム・C2Cサービスの開発費用と相場比較',
        'table_html': '''<div class="article-table-wrapper">
  <table class="article-table">
    <thead>
      <tr>
        <th>開発フェーズ</th>
        <th>主要な提供機能</th>
        <th>他社・SIer相場</th>
        <th>Ill（イル）株式会社</th>
        <th>想定期間</th>
      </tr>
    </thead>
    <tbody>
      <tr>
        <td><strong>プロトタイプ（PoC）</strong></td>
        <td>ユーザー/事業者登録、条件検索、プロフィール、マッチング機能</td>
        <td>350万〜600万円</td>
        <td><strong>120万〜200万円</strong></td>
        <td>3〜4週間</td>
      </tr>
      <tr>
        <td><strong>本番商用版（MVP）</strong></td>
        <td>Stripe決済（手数料自動徴収）、リアルタイムチャット、通知</td>
        <td>700万〜1,500万円</td>
        <td><strong>250万〜450万円</strong></td>
        <td>1.5〜2.5ヶ月</td>
      </tr>
      <tr>
        <td><strong>拡張スケール版</strong></td>
        <td>本人確認（eKYC）、AIレコメンド、不正検知、多言語対応</td>
        <td>1,800万〜3,500万円</td>
        <td><strong>550万〜900万円</strong></td>
        <td>3〜4ヶ月</td>
      </tr>
    </tbody>
  </table>
</div>''',
        'explanation_html': '''<h3>マッチングビジネス立ち上げで失敗しない「MVPアプローチ」</h3>
<p>マッチングプラットフォームビジネスで最も避けるべきは、最初から数千万円を投じてフルスペックのシステムを開発し、ユーザーが集まらずに資金ショートすることです。成功する起業家や新規事業担当者は、必ず「コア機能のみを最小コスト（MVP）で作り、ユーザーの反応を見ながら改善する」手法を取ります。</p>
<p>Ill（イル）株式会社では、認証（Supabase/Firebase）や決済（Stripe Connect）など検証済みの実績基盤を活用し、ゼロから無駄な車輪の再発明を行わないことで、最短1ヶ月・業界最安値水準での市場投入を可能にしています。</p>''',
        'extra_faqs': [
            ('Q. 決済機能（クレジットカード決済や売上分配）は簡単に組み込めますか？',
             'A. はい。世界標準の決済プラットフォームであるStripe Connectを標準採用しており、プラットフォーム手数料の自動徴収やユーザーへの自動送金を安全に実装できます。'),
            ('Q. iOS/Androidのアプリストアへの申請も依頼できますか？',
             'A. はい、ストア申請の代行サポートはもちろん、初期は審査不要で即日リリース可能なPWA（Webアプリ）として立ち上げ、利用者が増えた段階でネイティブアプリ化するコスト削減戦略もご提案可能です。')
        ]
    },
    'hiring_outsourcing': {
        'keywords': ['hiring', '採用', '外注', 'no-engineer', 'エンジニア不在'],
        'h2_title': 'エンジニア正社員採用 vs 開発外注（受託・準委任）の費用対効果比較',
        'table_html': '''<div class="article-table-wrapper">
  <table class="article-table">
    <thead>
      <tr>
        <th>項目</th>
        <th>正社員エンジニア採用</th>
        <th>大手SIer外注</th>
        <th>Ill（イル）株式会社</th>
      </tr>
    </thead>
    <tbody>
      <tr>
        <td><strong>初期費用（導入時）</strong></td>
        <td>採用手数料 150万〜250万円（年収の35%）</td>
        <td>初期着手金 100万〜300万円</td>
        <td><strong>0円（開発実費のみ）</strong></td>
      </tr>
      <tr>
        <td><strong>月額コスト（ランニング）</strong></td>
        <td>給与＋社保・福利厚生 60万〜90万円/月</td>
        <td>人月単価 140万〜220万円/人月</td>
        <td><strong>人月単価 60万〜85万円/人月</strong></td>
      </tr>
      <tr>
        <td><strong>リソースの柔軟性</strong></td>
        <td>解雇規制のため減員・解任が極めて困難</td>
        <td>契約期間拘束・変更不可</td>
        <td><strong>必要な開発期間のみ1ヶ月単位で稼働</strong></td>
      </tr>
      <tr>
        <td><strong>離職・退職リスク</strong></td>
        <td>退職によるブラックボックス化リスク大</td>
        <td>担当変更による引き継ぎ遅延あり</td>
        <td><strong>組織としてコード品質と保守を継続保証</strong></td>
      </tr>
    </tbody>
  </table>
</div>''',
        'explanation_html': '''<h3>非IT企業がシステム内製化に失敗する構造的罠</h3>
<p>近年「DXの内製化」が叫ばれていますが、ITを本業としない企業が優秀なエンジニアを採用・定着させる難易度は年々上がっています。高い採用費を払って採用しても、技術評価ができる上司がおらず、2年も経たずに退職してコードが放置されるケースが後を絶ちません。</p>
<p>Ill（イル）株式会社では、「社外の専任CTO・開発チーム」として伴走し、要件定義からアーキテクチャ選定、本番保守までを一括サポート。お客様の社内にエンジニアがいなくても、技術面で一切騙されない透明な開発体制を提供します。</p>''',
        'extra_faqs': [
            ('Q. 社内にITの専門用語がわかる人が誰もいませんが大丈夫ですか？',
             'A. 完全に大丈夫です。専門用語を使わず、「誰が、どの画面で、何をしたいのか」という業務目線で丁寧にヒアリングを行い、実際のモックアップ画面をお見せしながら進めます。'),
            ('Q. 開発したシステムの著作権やソースコードの権利はどうなりますか？',
             'A. 納品完了後、開発したソースコードおよび著作権はお客様側に完全に帰属します。将来的に自社で保守を引き継ぐことも可能です。')
        ]
    },
    'excel_db': {
        'keywords': ['excel', 'workflow', 'filemaker', '業務管理', 'dx-cost'],
        'h2_title': 'Excel・Accessから独自Webシステムへの移行費用相場',
        'table_html': '''<div class="article-table-wrapper">
  <table class="article-table">
    <thead>
      <tr>
        <th>移行対象・規模</th>
        <th>主な機能</th>
        <th>一般的なSIer相場</th>
        <th>Ill（イル）株式会社</th>
        <th>移行工期</th>
      </tr>
    </thead>
    <tbody>
      <tr>
        <td><strong>簡易台帳・マスタ管理</strong></td>
        <td>複数人同時編集、入力制御、履歴管理、CSVインポート</td>
        <td>250万〜450万円</td>
        <td><strong>80万〜150万円</strong></td>
        <td>約3〜4週間</td>
      </tr>
      <tr>
        <td><strong>業務ワークフロー・申請</strong></td>
        <td>申請・承認ルート、権限管理、ステータス自動通知</td>
        <td>500万〜900万円</td>
        <td><strong>180万〜300万円</strong></td>
        <td>約1.5〜2ヶ月</td>
      </tr>
      <tr>
        <td><strong>基幹連動型データベース</strong></td>
        <td>在庫・受発注・請求データ自動連携、帳票PDF自動生成</td>
        <td>1,000万〜2,200万円</td>
        <td><strong>350万〜600万円</strong></td>
        <td>約2.5〜3.5ヶ月</td>
      </tr>
    </tbody>
  </table>
</div>''',
        'explanation_html': '''<h3>なぜExcelやFileMakerの属人化業務はWebシステム化すべきなのか</h3>
<p>「ファイルが重くて開かない」「複数人で同時編集すると先祖返りする」「担当者が退職したらVBAマクロがブラックボックス化した」――こうした現場課題は、データを中央集権型のクラウドWebシステムに移行することで一掃されます。</p>
<p>Ill（イル）株式会社では、既存のExcelやAccessのシート構造をそのまま活かしながら、最新のWebフレームワーク（Next.js / TypeScript）と堅牢なリレーショナルデータベース（PostgreSQL）へ移行。現場スタッフが迷わず使える直感的なUIで、初日から業務効率を大幅に引き上げます。</p>''',
        'extra_faqs': [
            ('Q. 今使っている巨大なExcelマクロ（VBA）のデータもそのまま移せますか？',
             'A. はい。既存の計算ロジックやマクロの処理内容を解析し、サーバー側で安全かつ高速に自動実行するWebロジックへ再構築いたします。'),
            ('Q. 社員ごとに見せたくない情報（給与や売上など）のアクセス制限はできますか？',
             'A. ロール別の詳細な権限管理（管理者・一般社員・閲覧のみなど）を標準実装できますので、セキュリティ面も安心です。')
        ]
    },
    'genai_automation': {
        'keywords': ['genai', 'rag', 'chatgpt', '生成ai', '業務効率化'],
        'h2_title': '社内向け生成AI・RAGシステムの導入費用相場と開発期間',
        'table_html': '''<div class="article-table-wrapper">
  <table class="article-table">
    <thead>
      <tr>
        <th>導入構成・システム種別</th>
        <th>提供機能・連携先</th>
        <th>市場の受託相場</th>
        <th>Ill（イル）株式会社</th>
        <th>導入期間</th>
      </tr>
    </thead>
    <tbody>
      <tr>
        <td><strong>社内FAQボット</strong></td>
        <td>社内マニュアルPDF投入、Slack/Teams通知連携</td>
        <td>200万〜400万円</td>
        <td><strong>80万〜150万円</strong></td>
        <td>約2〜3週間</td>
      </tr>
      <tr>
        <td><strong>セキュアRAG検索基盤</strong></td>
        <td>契約書・社内規定全文検索、出典元の明示、権限管理</td>
        <td>500万〜1,000万円</td>
        <td><strong>180万〜320万円</strong></td>
        <td>約1〜1.5ヶ月</td>
      </tr>
      <tr>
        <td><strong>AI業務自動化エージェント</strong></td>
        <td>メール下書き自動作成、見積データ抽出、外部API連携実行</td>
        <td>800万〜1,600万円</td>
        <td><strong>280万〜500万円</strong></td>
        <td>約2〜3ヶ月</td>
      </tr>
    </tbody>
  </table>
</div>''',
        'explanation_html': '''<h3>社内データをAIに学習させない「完全セキュアなRAG設計」</h3>
<p>ChatGPTなどの汎用AIをそのまま業務に使うと「機密情報がAIの学習データに使われて漏洩するのではないか」というセキュリティ上の懸念が生じます。これに対し、<strong>Ill（イル）株式会社</strong> ではOpenAIやAnthropicのエンタープライズAPI（ゼロデータリテンション・学習利用ゼロ保証）を採用し、社内データは自社のプライベートなベクターデータベース（pgvector / Pinecone）内でのみ完結するRAGアーキテクチャを構築します。</p>
<p>高額な専用AIパッケージに頼ることなく、必要最小限のセキュアなパイプラインを構築することで、月額のAPI実費（数千円〜数万円程度）のみで高度な業務自動化を実現します。</p>''',
        'extra_faqs': [
            ('Q. 自社の機密情報や個人情報がAIの学習に使われる心配はありませんか？',
             'A. 一切ありません。商用APIの規約上、入力データがモデルの再学習に利用されることはなく、通信・保管時ともに最高水準で暗号化されます。'),
            ('Q. PDFやWord、Excelなど様々な形式のドキュメントを読み込ませることは可能ですか？',
             'A. はい、可能です。ドキュメントの自動テキスト抽出・チャンク分割・埋め込み（Embedding）パイプラインを構築し、形式を問わず検索可能にします。')
        ]
    },
    'cost_standards': {
        'keywords': ['cost-standard', 'estimation', '適正価格', '見積もり', '削減'],
        'h2_title': 'システム開発の工程別費用内訳と大手SIerとのコスト削減比較',
        'table_html': '''<div class="article-table-wrapper">
  <table class="article-table">
    <thead>
      <tr>
        <th>開発工程</th>
        <th>一般的な費用比率</th>
        <th>大手SIer見積もり例</th>
        <th>Ill（イル）株式会社</th>
        <th>コスト削減の理由</th>
      </tr>
    </thead>
    <tbody>
      <tr>
        <td><strong>要件定義・基本設計</strong></td>
        <td>15〜20%</td>
        <td>150万〜300万円</td>
        <td><strong>40万〜80万円</strong></td>
        <td>動くプロトタイプで合意形成を高速化</td>
      </tr>
      <tr>
        <td><strong>UI/UX設計・デザイン</strong></td>
        <td>15〜20%</td>
        <td>150万〜250万円</td>
        <td><strong>30万〜60万円</strong></td>
        <td>洗練されたコンポーネント資産の再利用</td>
      </tr>
      <tr>
        <td><strong>プログラミング・実装</strong></td>
        <td>40〜50%</td>
        <td>400万〜800万円</td>
        <td><strong>120万〜250万円</strong></td>
        <td>生成AI活用によるコード作成の自動化</td>
      </tr>
      <tr>
        <td><strong>テスト・検証・納品</strong></td>
        <td>15〜20%</td>
        <td>150万〜250万円</td>
        <td><strong>30万〜60万円</strong></td>
        <td>CI/CDによる結合テスト自動化</td>
      </tr>
    </tbody>
  </table>
</div>''',
        'explanation_html': '''<h3>過剰な見積もり上乗せを見抜く3つのポイント</h3>
<p>開発会社から提示された見積書に「システム開発一式：800万円」といった大雑把な項目しか書かれていない場合、高確率で不要な安全マージン（バッファ）が上乗せされています。適正な見積もりを見極めるには、以下の3点を確認してください。</p>
<ol>
  <li><strong>人月単価と想定工数が分離して記載されているか</strong>: 単価が100万円なのか60万円なのか、作業期間は何人月なのかを確認する。</li>
  <li><strong>機能ごとの個別見積もりが記載されているか</strong>: 「この機能を削るといくら安くなるか」が判断できる透明性があるか。</li>
  <li><strong>納品後の月額保守費用が開発費の10〜15%以下に収まっているか</strong>: 高額な縛り契約がないかを事前にチェックする。</li>
</ol>''',
        'extra_faqs': [
            ('Q. 他社の見積書を見せて、妥当かどうか診断してもらうことはできますか？',
             'A. はい、無料で見積書診断を承っております。過剰な要件や削れるポイントをエンジニア目線で率直にアドバイスいたします。'),
            ('Q. 開発途中で追加費用が請求されることはありませんか？',
             'A. 請負契約の場合、事前に合意した要件の範囲内で追加費用が発生することは一切ありません。仕様変更が必要な場合も、必ず事前に工数と金額をご提示して合意をいただきます。')
        ]
    },
    'nocode_scratch': {
        'keywords': ['nocode', 'ノーコード'],
        'h2_title': 'ノーコード開発 vs スクラッチ開発の3年間損益分岐点比較',
        'table_html': '''<div class="article-table-wrapper">
  <table class="article-table">
    <thead>
      <tr>
        <th>比較項目</th>
        <th>ノーコード開発（Bubble/Adalo等）</th>
        <th>Ill（イル）スクラッチ開発</th>
      </tr>
    </thead>
    <tbody>
      <tr>
        <td><strong>初期開発費用</strong></td>
        <td>50万〜150万円（初期は安価）</td>
        <td><strong>150万〜350万円</strong>（必要十分なミニマル設計）</td>
      </tr>
      <tr>
        <td><strong>月額プラットフォーム利用料</strong></td>
        <td>5万〜30万円/月（プランやDB量で急騰）</td>
        <td><strong>0円〜1万円/月</strong>（クラウドサーバー実費のみ）</td>
      </tr>
      <tr>
        <td><strong>3年間の総保有コスト（TCO）</strong></td>
        <td><strong>230万〜1,200万円</strong>（運用費で逆転）</td>
        <td><strong>180万〜380万円</strong>（長期的に圧倒的に安価）</td>
      </tr>
      <tr>
        <td><strong>機能の拡張性・独自ロジック</strong></td>
        <td>ツールの制約・仕様制限により限界あり</td>
        <td><strong>完全スクラッチのため制限一切なし</strong></td>
      </tr>
      <tr>
        <td><strong>表示速度・SEO</strong></td>
        <td>JavaScriptが肥大化し表示が遅い傾向</td>
        <td><strong>SSR/SSGにより超高速表示・SEO最高評価</strong></td>
      </tr>
    </tbody>
  </table>
</div>''',
        'explanation_html': '''<h3>「最初はノーコードで、後から作り直す」は二重コストの典型</h3>
<p>ノーコードツールは初期のプロトタイプ作成には適していますが、事業が成長して会員数やトランザクションが増えると、プラットフォーム利用料の急激な値上げや表示速度の低下、複雑な業務ロジックに対応できない「ノーコードの壁」に直面します。結局ゼロからスクラッチで作り直すことになり、最初の費用と時間が完全に無駄になるケースが多発しています。</p>
<p>Ill（イル）株式会社では、生成AIを駆使した超高速コーディングにより、ノーコード並みの低価格・短納期で最初から堅牢なフルスクラッチシステムを構築します。</p>''',
        'extra_faqs': [
            ('Q. ノーコードで作ってしまった既存システムをスクラッチに移植できますか？',
             'A. はい、数多くの移行実績があります。既存のデータベースと画面構成を引き継ぎ、高速で拡張性の高いモダンシステムへスムーズにリプレイスいたします。'),
            ('Q. スクラッチ開発だと運用後の修正にエンジニアが必要になりませんか？',
             'A. よく更新する設定やテキストは直感的な管理画面からノンプログラミングで編集できるように設計しますので、日常業務でエンジニアの手を煩わせることはありません。')
        ]
    },
    'contracts_risk': {
        'keywords': ['contract', '請負', '準委任', '契約'],
        'h2_title': '「請負契約」と「準委任契約」の法的一覧比較と使い分け基準',
        'table_html': '''<div class="article-table-wrapper">
  <table class="article-table">
    <thead>
      <tr>
        <th>項目</th>
        <th>請負契約</th>
        <th>準委任契約（アジャイル・ラボ型）</th>
      </tr>
    </thead>
    <tbody>
      <tr>
        <td><strong>契約の目的</strong></td>
        <td>「成果物の完成・納品」を約束</td>
        <td>「善管注意義務に基づく専門的役務提供」</td>
      </tr>
      <tr>
        <td><strong>契約不適合責任（旧瑕疵担保）</strong></td>
        <td>あり（期間内の不具合は無償修正義務）</td>
        <td>原則なし（故意・重大な過失を除く）</td>
      </tr>
      <tr>
        <td><strong>仕様変更への柔軟性</strong></td>
        <td>低い（契約変更・再見積もりが必要）</td>
        <td><strong>極めて高い（優先順位を随時変更可能）</strong></td>
      </tr>
      <tr>
        <td><strong>コストの確定性</strong></td>
        <td>固定金額（バッファが乗りやすい）</td>
        <td>月額固定・実働精算（無駄な安全マージン排除）</td>
      </tr>
      <tr>
        <td><strong>最適なプロジェクト</strong></td>
        <td>要件が100%確定した基幹システム構築</td>
        <td>新規事業、MVP検証、アジャイル改善開発</td>
      </tr>
    </tbody>
  </table>
</div>''',
        'explanation_html': '''<h3>トラブルを100%防止する契約書のチェックポイント</h3>
<p>システム開発における訴訟や納品トラブルの多くは、「完成の定義」が曖昧なまま請負契約を結んでしまったこと、または準委任契約で開発側の進捗管理が不透明だったことに起因します。発注者側として損をしないためには、以下の条項を必ず契約書に盛り込んでください。</p>
<ul>
  <li><strong>検収期間と検収基準の明確化</strong>: 納品後何日以内に検収を行い、どのようなテストをパスすれば合格となるかを具体的に定義する。</li>
  <li><strong>著作権の帰属</strong>: 成果物の著作権（著作権法第27条および第28条の権利を含む）が発注者に譲渡されることを明記する。</li>
  <li><strong>再委託の可否と責任範囲</strong>: 勝手に無断で外部へ多重下請けされないよう、再委託条項を管理する。</li>
</ul>''',
        'extra_faqs': [
            ('Q. Ill（イル）株式会社ではどちらの契約形態に対応していますか？',
             'A. お客様のプロジェクトの性質に合わせて両方に対応しております。仕様が固まっている場合は「請負契約」、事業検証しながら柔軟に進めたい場合は「準委任契約（月額スプリント型）」をお選びいただけます。'),
            ('Q. 途中で開発会社を変えたくなった場合、成果物は引き継げますか？',
             'A. 弊社ではすべてのリポジトリ（GitHub）をお客様へ共有し、透明なコミット履歴とドキュメントを残しますので、いつでも他社へ引き継ぐことが可能です。')
        ]
    },
    'rfp_requirements': {
        'keywords': ['rfp', 'requirements', '要件定義', '提案依頼書'],
        'h2_title': '開発会社から最安・最高提案を引き出すRFP構成テンプレート',
        'table_html': '''<div class="article-table-wrapper">
  <table class="article-table">
    <thead>
      <tr>
        <th>構成セクション</th>
        <th>記載すべき必須事項</th>
        <th>発注者が得られるメリット</th>
      </tr>
    </thead>
    <tbody>
      <tr>
        <td><strong>1. プロジェクト背景・目的</strong></td>
        <td>解決したい経営課題、ターゲット層、狙うKPI</td>
        <td>開発会社がビジネスゴールを理解し的確な提案が可能</td>
      </tr>
      <tr>
        <td><strong>2. 業務フローと利用シーン</strong></td>
        <td>現行フローの課題、システム利用者の役割・導線</td>
        <td>不要な機能の作り込みを防ぎ、工数を最小化</td>
      </tr>
      <tr>
        <td><strong>3. 必須要件（Must）と希望（Want）</strong></td>
        <td>初回リリースで絶対に外せない機能の峻別</td>
        <td>見積もりのブレを防ぎ、価格比較が極めて容易になる</td>
      </tr>
      <tr>
        <td><strong>4. 予算感と希望納期</strong></td>
        <td>想定予算レンジ（例: 200万〜300万）、リリース希望月</td>
        <td>予算に応じた最適なアーキテクチャ提案を引き出せる</td>
      </tr>
    </tbody>
  </table>
</div>''',
        'explanation_html': '''<h3>RFP（提案依頼書）はA4用紙2〜3枚で十分</h3>
<p>「RFPを書くには専門的なIT知識が必要なのではないか」と身構える発注者が多いですが、数十ページの専門文書を作る必要は一切ありません。重要なのは「何を解決したいのか（Why）」と「絶対に欲しいコア機能（What）」が明確になっていることです。</p>
<p>Ill（イル）株式会社では、箇条書きのメモやオンラインでの30分のヒアリングからでも、要件を瞬時に整理してプロトタイプ画面を提示する「要件定義代行サポート」を無料で実施しています。</p>''',
        'extra_faqs': [
            ('Q. 構想段階で具体的な仕様が決まっていなくても相談できますか？',
             'A. 大歓迎です。「こういうビジネスをやりたい」「業務を効率化したい」というアイデアレベルから、最適な技術選定とミニマルな要件定義をリードいたします。'),
            ('Q. 複数社での相見積もり（コンペ）を行っても問題ありませんか？',
             'A. 全く問題ありません。他社様の提案書や見積もりと比較していただき、弊社の価格競争力と技術的合理性を実感してください。')
        ]
    },
    'shopify_ec': {
        'keywords': ['shopify', 'ec'],
        'h2_title': 'Shopify連携 vs フルスクラッチECの構築費用・維持費比較',
        'table_html': '''<div class="article-table-wrapper">
  <table class="article-table">
    <thead>
      <tr>
        <th>比較項目</th>
        <th>フルスクラッチEC</th>
        <th>Shopify＋独自API連携（Ill）</th>
      </tr>
    </thead>
    <tbody>
      <tr>
        <td><strong>初期構築費用</strong></td>
        <td>800万〜2,500万円</td>
        <td><strong>150万〜350万円</strong></td>
      </tr>
      <tr>
        <td><strong>構築期間</strong></td>
        <td>5〜8ヶ月</td>
        <td><strong>1.5〜2.5ヶ月</strong></td>
      </tr>
      <tr>
        <td><strong>セキュリティ・PCI DSS</strong></td>
        <td>自社で巨額のセキュリティ投資が必要</td>
        <td><strong>世界最高水準（Level 1 PCI DSS）準拠</strong></td>
      </tr>
      <tr>
        <td><strong>月額運用・保守コスト</strong></td>
        <td>15万〜40万円/月</td>
        <td><strong>3万〜8万円/月</strong></td>
      </tr>
    </tbody>
  </table>
</div>''',
        'explanation_html': '''<h3>ECは「決済・基盤はShopify」＋「独自機能はAPI連携」が現代の正解</h3>
<p>ECサイトをゼロからスクラッチで作る時代は終わりました。カートや決済、セキュリティといったインフラは世界標準のShopifyを活用し、独自の業務要件（自社基幹システムとの在庫連携、定期購入の独自ロジック、会員ランク機能など）のみをカスタム開発（Headless / Storefront API）で繋ぎ込むのが、最も低コストで売上を伸ばせるアプローチです。</p>''',
        'extra_faqs': [
            ('Q. 既存のECサイト（ECCubeやBASEなど）からの商品データ移行は可能ですか？',
             'A. はい。既存の商品マスタ、顧客データ、過去の注文履歴をすべて安全にShopifyおよび新システムへ移行できます。'),
            ('Q. BtoB向けのクローズドEC（卸売り・掛け払い対応）も構築できますか？',
             'A. はい、会員承認制ECや顧客ごとの掛け率・価格設定、請求書払い決済の連携など、B2B特有の機能も柔軟に構築可能です。')
        ]
    },
    'pwa_mobile': {
        'keywords': ['pwa', 'native', 'react-native', 'スマホアプリ'],
        'h2_title': 'PWA（Webアプリ） vs React Native vs ネイティブアプリ開発比較',
        'table_html': '''<div class="article-table-wrapper">
  <table class="article-table">
    <thead>
      <tr>
        <th>開発方式</th>
        <th>初期開発費用</th>
        <th>ストア審査・手数料</th>
        <th>更新・リリースの手軽さ</th>
      </tr>
    </thead>
    <tbody>
      <tr>
        <td><strong>PWA（Webアプリ）</strong></td>
        <td><strong>150万〜280万円</strong></td>
        <td><strong>審査なし（手数料0%）</strong></td>
        <td><strong>即日デプロイ・即時反映</strong></td>
      </tr>
      <tr>
        <td><strong>React Native（クロス開発）</strong></td>
        <td><strong>350万〜650万円</strong></td>
        <td>審査あり（15〜30%）</td>
        <td>コード共通化で1回の修正で両OS反映</td>
      </tr>
      <tr>
        <td><strong>ネイティブ（Swift/Kotlin個別）</strong></td>
        <td>800万〜1,800万円</td>
        <td>審査あり（15〜30%）</td>
        <td>iOSとAndroidで別々の開発・修正が必要</td>
      </tr>
    </tbody>
  </table>
</div>''',
        'explanation_html': '''<h3>アプリストアの手数料30%と審査リジェクトを回避するPWA戦略</h3>
<p>スマートフォンアプリをストア（App Store / Google Play）で公開すると、厳しいガイドライン審査に数週間待たされ、決済売上の15〜30%がApple/Googleに徴収されます。さらに、iOS用とAndroid用で別々のエンジニアが必要になり、開発費と維持費が2倍に跳ね上がります。</p>
<p>Ill（イル）株式会社では、ストアを通さずにホーム画面に追加でき、プッシュ通知やカメラ・位置情報も利用可能なPWA（Progressive Web Apps）技術を推奨。開発費を劇的に削減しながら、ネイティブアプリと遜色ない快適な操作性を実現します。</p>''',
        'extra_faqs': [
            ('Q. PWAでもスマートフォンのプッシュ通知を送ることはできますか？',
             'A. はい、現在のiOS（Safari）およびAndroid（Chrome）はPWAでのWebプッシュ通知に完全対応しています。'),
            ('Q. 将来的にApp Storeでもアプリとして配信したくなった場合はどうすればいいですか？',
             'A. PWAのWebコード資産をベースにCapacitorやReact Nativeでラップすることで、少額の追加費用でストア申請アプリへ変換可能です。')
        ]
    },
    'line_chatbot': {
        'keywords': ['line', 'chatbot'],
        'h2_title': 'LINEチャットボット導入形態別の費用相場とランニングコスト',
        'table_html': '''<div class="article-table-wrapper">
  <table class="article-table">
    <thead>
      <tr>
        <th>構築方式</th>
        <th>初期開発費用</th>
        <th>月額ランニング費用</th>
        <th>独自システム連携・拡張性</th>
      </tr>
    </thead>
    <tbody>
      <tr>
        <td><strong>既製チャットボットSaaS</strong></td>
        <td>10万〜30万円</td>
        <td>5万〜15万円/月（従量課金大）</td>
        <td>△ 既定の機能しか使えない</td>
      </tr>
      <tr>
        <td><strong>大手SIer受託開発</strong></td>
        <td>400万〜800万円</td>
        <td>10万〜20万円/月</td>
        <td>○ 可能だが仕様変更に高額請求</td>
      </tr>
      <tr>
        <td><strong>Ill（イル）独自API連携</strong></td>
        <td><strong>120万〜220万円</strong></td>
        <td><strong>1万〜3万円/月（API実費のみ）</strong></td>
        <td><strong>◎ 自社DB・予約システムと完全連動</strong></td>
      </tr>
    </tbody>
  </table>
</div>''',
        'explanation_html': '''<h3>高額な月額課金ツールを使わずにLINE自動化を実現する裏技</h3>
<p>市販のLINE拡張ツールやチャットボットSaaSは、初期費用が安く見えても、友だち数や配信メッセージ数が増えるにつれて月額費用が数万円〜十数万円に膨らみます。さらに、自社の顧客データベースや予約管理システムと連動させようとすると、機能制限に阻まれます。</p>
<p>Ill（イル）株式会社では、LINE公式のMessaging APIとOpenAI（ChatGPT）APIを直接接続するサーバーレス構成を構築。無駄なSaaS利用料をゼロにし、APIの利用実費のみで動く完全自動応答環境を提供します。</p>''',
        'extra_faqs': [
            ('Q. 既存の予約システムや顧客名簿とLINEを繋ぎ込むことはできますか？',
             'A. はい。Webhook経由で自社データベースをリアルタイムに検索し、空き枠の照会から予約確定までをチャット上で完結させることが可能です。'),
            ('Q. チャットボットで対応できない複雑な問い合わせは人間に引き継げますか？',
             'A. もちろん可能です。AIが未対応と判断した場合や、ユーザーが「オペレーター呼び出し」を選択した場合に、通知を飛ばして人間が有人チャットに切り替える仕組みを構築できます。')
        ]
    },
    'web_scraping': {
        'keywords': ['scraping', 'スクレイピング', '自動収集'],
        'h2_title': 'Webデータスクレイピング・自動クローリングシステムの開発費用',
        'table_html': '''<div class="article-table-wrapper">
  <table class="article-table">
    <thead>
      <tr>
        <th>システム構成</th>
        <th>対応サイト・規模</th>
        <th>一般的な受託相場</th>
        <th>Ill（イル）株式会社</th>
        <th>納期</th>
      </tr>
    </thead>
    <tbody>
      <tr>
        <td><strong>単一ポータル定期巡回</strong></td>
        <td>1〜2サイト、CSV/スプレッドシート自動出力</td>
        <td>150万〜300万円</td>
        <td><strong>60万〜120万円</strong></td>
        <td>約1〜2週間</td>
      </tr>
      <tr>
        <td><strong>複数サイト差分検知</strong></td>
        <td>3〜5サイト、重複排除、画像保存、Slack通知</td>
        <td>350万〜600万円</td>
        <td><strong>150万〜250万円</strong></td>
        <td>約3〜4週間</td>
      </tr>
      <tr>
        <td><strong>大規模クローリング基盤</strong></td>
        <td>10サイト以上、IP分散・ブロック回避、DB自動蓄積API</td>
        <td>700万〜1,200万円</td>
        <td><strong>280万〜450万円</strong></td>
        <td>約1.5〜2ヶ月</td>
      </tr>
    </tbody>
  </table>
</div>''',
        'explanation_html': '''<h3>法的リスク・アクセス遮断を回避するプロのスクレイピング技術</h3>
<p>営業リストの自動収集や価格調査などでスクレイピングを内製しようとすると、対象サイトの仕様変更でエラーが頻発したり、過度なアクセスでIPブロックされたり、著作権法や利用規約上のトラブルに巻き込まれるリスクがあります。</p>
<p>Ill（イル）株式会社では、法的ガイドラインに完全準拠し、適切なインターバル制御（アクセス負荷軽減）とヘッドレスブラウザ（Playwright / Puppeteer）による高度な動的描画対応を完備した安全な収集基盤を構築します。</p>''',
        'extra_faqs': [
            ('Q. スクレイピングは法律的に問題ありませんか？',
             'A. 日本の著作権法第30条の4（情報解析のための利用）に基づき、サーバーに過剰な負荷をかけず適切にデータを収集・分析することは適法と認められています。法的に問題のない設計を徹底いたします。'),
            ('Q. 収集先のサイトデザインが変わったら動かなくなりませんか？',
             'A. 仕様変更を検知するアラート機能と、耐性の高いセレクタ設計を実装します。定期的なセレクタ更新の保守サポートも安価に承っております。')
        ]
    },
    'default': {
        'keywords': [],
        'h2_title': 'システム開発の費用相場とIll（イル）株式会社のコスト最適化設計',
        'table_html': '''<div class="article-table-wrapper">
  <table class="article-table">
    <thead>
      <tr>
        <th>開発規模</th>
        <th>開発内容</th>
        <th>大手SIer相場</th>
        <th>Ill（イル）株式会社</th>
        <th>想定工期</th>
      </tr>
    </thead>
    <tbody>
      <tr>
        <td><strong>スモールMVP</strong></td>
        <td>コア機能のみ（主要3画面）、プロトタイプ検証</td>
        <td>300万〜500万円</td>
        <td><strong>100万〜180万円</strong></td>
        <td>約3〜4週間</td>
      </tr>
      <tr>
        <td><strong>標準ビジネス版</strong></td>
        <td>認証、権限管理、決済連携、管理画面ダッシュボード</td>
        <td>600万〜1,200万円</td>
        <td><strong>200万〜380万円</strong></td>
        <td>約1.5〜2.5ヶ月</td>
      </tr>
      <tr>
        <td><strong>エンタープライズ</strong></td>
        <td>大規模トラフィック対応、基幹連動、高度セキュリティ</td>
        <td>1,500万〜3,000万円</td>
        <td><strong>450万〜850万円</strong></td>
        <td>約3〜4ヶ月</td>
      </tr>
    </tbody>
  </table>
</div>''',
        'explanation_html': '''<h3>無駄なコストを削ぎ落とし、事業成果にコミットする「ミニマル開発」</h3>
<p>従来のシステム開発では、「使うかどうかわからない機能」の見積もりが積み重なり、数百万円単位の無駄金が発生していました。<strong>Ill（イル）株式会社</strong> では、お客様のビジネスゴールから逆算し、本当に必要なコア機能だけに絞ったミニマル設計を徹底します。</p>
<p>さらに最新の生成AIを活用してコード作成・単体テストを徹底自動化することで、開発工数を半減させ、業界最安値水準のスクラッチ開発を提供しています。</p>''',
        'extra_faqs': [
            ('Q. 開発費用の支払いタイミングはどのようになっていますか？',
             'A. 原則として着手金（50%）と納品完了検収後（50%）の2分割ですが、ご予算やご都合に応じた柔軟な分割払いや月額スプリント契約もご相談可能です。'),
            ('Q. 納品後のサポートや保守体制はどうなっていますか？',
             'A. 納品後の無償瑕疵担保期間を設けているほか、月額数万円からの柔軟な継続保守プランをご用意しております。')
        ]
    }
}

def get_best_config(filename, content):
    fname_lower = filename.lower()
    content_lower = content.lower()
    for key, cfg in TOPIC_CONFIGS.items():
        if key == 'default':
            continue
        for kw in cfg['keywords']:
            if kw in fname_lower or kw in content_lower:
                return cfg
    return TOPIC_CONFIGS['default']
