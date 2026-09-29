import re

file_path = "column/web-system-security.html"
with open(file_path, "r", encoding="utf-8") as f:
    content = f.read()

new_body_content = """          <div class="toc-box">
            <div class="toc-title">目次</div>
            <ul class="toc-list">
              <li><a href="#sec-1">1. 【経営リスク】なぜWebシステムにセキュリティ対策が必須なのか？</a></li>
              <li><a href="#sec-2">2. 【3大脆弱性】知っておくべき代表的な攻撃手法（SQLi・XSS・CSRF）</a></li>
              <li><a href="#sec-3">3. 【実践ガイド】Webシステムセキュリティ基本チェックリスト5選</a></li>
              <li><a href="#sec-pricing-table">4. 【費用相場】セキュリティ対策込みのシステム開発費用と工期比較</a></li>
              <li><a href="#sec-4">5. 【Ill Inc.の強み】セキュアバイデザインによる安心の設計・開発標準</a></li>
              <li><a href="#section-faq">6. よくある質問（FAQ）</a></li>
            </ul>
          </div>

          <p>
            インターネット上で一般公開される<strong>「Webシステム」や「Webアプリケーション」</strong>。24時間365日どこからでもアクセスできる利便性の裏には、悪意ある第三者（ハッカー）からのサイバー攻撃リスクが常に潜んでいます。
          </p>
          <div style="background: rgba(14, 165, 233, 0.08); border-left: 4px solid #0EA5E9; padding: 18px 20px; border-radius: 6px; margin: 24px 0;">
            <strong style="color: #0EA5E9; display: block; margin-bottom: 8px;">💡 Webシステムセキュリティの最重要ポイント</strong>
            <ul style="margin: 0; padding-left: 20px; font-size: 1.5rem; line-height: 1.75;">
              <li><strong>「うちは中小企業・新規事業だから狙われない」は通用しない</strong>（全自動探索ボットが無差別に攻撃）</li>
              <li><strong>後付けのセキュリティ改修は初期設計の3倍以上の追加コストが発生</strong>する</li>
              <li><strong>設計初期から安全性を組み込む「セキュアバイデザイン」</strong>が最も低コストで確実</li>
            </ul>
          </div>
          <p>
            セキュリティ脆弱性を放置したままWebシステムを公開すると、顧客情報の流出、サイトの改ざん、システムの不正利用に繋がり、多額の損害賠償やブランドイメージの致命的な失墜を招きます。本コラムでは、企業が最低限押さえるべきWebセキュリティの基本と防御策を分かりやすく解説します。
          </p>

          <h2 id="sec-1">1. 【経営リスク】なぜWebシステムにセキュリティ対策が必須なのか？</h2>
          <p>
            Webシステムにはデータベースが組み込まれており、顧客の個人情報、決済履歴、ログインパスワードなどが格納されています。これらはダークウェブ等での取引対象となるため、サイバー犯罪者の標的になります。
          </p>
          <p>
            近年では、脆弱性のあるWebサイトを24時間自動で探索するボットプログラムが巡回しているため、企業の知名度や事業規模に関係なく、インターネット上に公開されているすべてのシステムが無差別に攻撃の対象になります。
          </p>
          
          <div style="display: grid; grid-template-columns: repeat(auto-fit, minmax(240px, 1fr)); gap: 16px; margin: 28px 0;">
            <div style="background: rgba(239, 68, 68, 0.06); border: 1px solid rgba(239, 68, 68, 0.25); border-radius: 8px; padding: 18px;">
              <div style="font-size: 1.8rem; margin-bottom: 6px;">🚨 個人情報の漏洩・賠償</div>
              <p style="margin: 0; font-size: 1.4rem; line-height: 1.6; color: var(--text-muted);">
                顧客名簿やクレジットカード情報の流出。1件あたり数万円の補償金や、個人情報保護法違反による最大1億円の罰金リスク。
              </p>
            </div>
            <div style="background: rgba(245, 158, 11, 0.06); border: 1px solid rgba(245, 158, 11, 0.25); border-radius: 8px; padding: 18px;">
              <div style="font-size: 1.8rem; margin-bottom: 6px;">🛑 サイト改ざん・踏み台化</div>
              <p style="margin: 0; font-size: 1.4rem; line-height: 1.6; color: var(--text-muted);">
                自社サイトが偽画面へ改ざんされ、取引先やユーザーへマルウェアをばら撒く「加害者」になってしまう二次被害。
              </p>
            </div>
            <div style="background: rgba(99, 102, 241, 0.06); border: 1px solid rgba(99, 102, 241, 0.25); border-radius: 8px; padding: 18px;">
              <div style="font-size: 1.8rem; margin-bottom: 6px;">📉 業務停止と信用の失墜</div>
              <p style="margin: 0; font-size: 1.4rem; line-height: 1.6; color: var(--text-muted);">
                サービス緊急停止に伴う売上機会の損失、大手企業との取引停止、メディア報道による企業価値の致命的ダウン。
              </p>
            </div>
          </div>

          <h2 id="sec-2">2. 【3大脆弱性】知っておくべき代表的な攻撃手法（SQLi・XSS・CSRF）</h2>
          <p>
            Webアプリケーション層において、攻撃者に悪用されやすい代表的な脆弱性と攻撃手法は以下の通りです。
          </p>

          <div class="article-table-wrapper">
            <table class="article-table">
              <thead>
                <tr>
                  <th style="width: 25%;">脆弱性・攻撃名</th>
                  <th style="width: 35%;">攻撃の仕組み</th>
                  <th style="width: 40%;">主な被害と具体的な防御策</th>
                </tr>
              </thead>
              <tbody>
                <tr>
                  <td><strong>SQLインジェクション (SQLi)</strong></td>
                  <td>入力フォームやURLパラメータに不正なSQL文を注入し、データベースを違法に操作する</td>
                  <td><strong>【被害】</strong> DB全データの漏洩・消去<br><strong>【対策】</strong> <code>プレースホルダ（Prepared Statements）</code> やモダンORM（Prisma等）の徹底使用</td>
                </tr>
                <tr>
                  <td><strong>クロスサイトスクリプティング (XSS)</strong></td>
                  <td>脆弱性のあるサイトに悪意あるJavaScriptコードを埋め込み、閲覧者のブラウザ上で実行させる</td>
                  <td><strong>【被害】</strong> セッションCookieの盗取、なりすまし操作<br><strong>【対策】</strong> 出力時のHTMLサニタイズ、Reactの自動エスケープ、<code>CSP</code> 設定</td>
                </tr>
                <tr>
                  <td><strong>クロスサイトリクエストフォージェリ (CSRF)</strong></td>
                  <td>ログイン中のユーザーのブラウザを利用し、本人が意図しない重要処理（送金・パスワード変更等）を強制実行させる</td>
                  <td><strong>【被害】</strong> 不正送金、不正書き込み、購入被害<br><strong>【対策】</strong> ワンタイムCSRFトークンの検証、Cookieの <code>SameSite=Lax</code> 設定</td>
                </tr>
                <tr>
                  <td><strong>認証・認可不備 (Broken Auth)</strong></td>
                  <td>パスワードの推測やブルートフォース攻撃、URL直接アクセスによる他者データの閲覧</td>
                  <td><strong>【被害】</strong> アカウント乗っ取り、権限昇格<br><strong>【対策】</strong> 強力なパスワードポリシー、レートリミット制限、多要素認証（MFA）</td>
                </tr>
              </tbody>
            </table>
          </div>

          <h3>1. SQLインジェクション：データベースの不正操作</h3>
          <p>
            データベースに対して送信する命令文（SQL）を、ユーザーの入力値によって改ざんされてしまう脆弱性です。古いシステムや手作業でSQLを組み立てている場合に多発します。
          </p>
          <p>
            <strong>【対策】</strong>: SQLを発行する際に入力値をリテラルとして安全に分離処理する「プレースホルダ」の使用をコーディング規約で義務化し、PrismaやTypeORMなどの検証済みライブラリを使用します。
          </p>

          <h3>2. クロスサイトスクリプティング（XSS）：悪意あるスクリプトの実行</h3>
          <p>
            HTMLを出力する部分で、ユーザーが入力したスクリプト（HTMLタグやJavaScript）をそのまま出力してしまうことで発生します。
          </p>
          <p>
            <strong>【対策】</strong>: 出力するすべてのテキストに対して <code>&lt;</code> や <code>&gt;</code> などの特殊文字を無害化する「サニタイジング（エスケープ処理）」を行います。ReactやNext.jsなどのモダンフレームワークは標準で自動エスケープ機構を備えています。
          </p>

          <h3>3. クロスサイトリクエストフォージェリ（CSRF）：なりすましリクエスト</h3>
          <p>
            ユーザーがログイン済みの状態で悪意あるWebページを閲覧した際、そのブラウザから正規のWebシステムへ勝手に送金やパスワード変更のリクエストを送信させてしまう攻撃です。
          </p>
          <p>
            <strong>【対策】</strong>: フォーム送信ごとにランダムな一回限りの検証コード（CSRFトークン）を発行・照合する仕組みを導入し、Cookieに <code>SameSite=Lax/Strict</code> 属性を付与します。
          </p>

          <h2 id="sec-3">3. 【実践ガイド】Webシステムセキュリティ基本チェックリスト5選</h2>
          <p>
            開発時および本番運用時に必ず確認すべき、最も基本的かつ効果的なチェックリストです。
          </p>

          <div class="checklist-box" style="background: rgba(16, 185, 129, 0.06); border-left: 4px solid #10B981; padding: 24px; border-radius: 8px; margin: 32px 0;">
            <strong class="checklist-title" style="color: #10B981; font-size: 1.8rem; display: block; margin-bottom: 16px;">🛡️ Webシステムセキュリティ基本チェックリスト</strong>
            <ul style="margin: 0; padding-left: 24px; line-height: 1.85;">
              <li><strong>通信の完全暗号化（常時HTTPS / TLS 1.3）</strong>: SSL/TLS証明書を導入し、データ送受信の盗聴・改ざんを100%遮断しているか。</li>
              <li><strong>安全なセッション管理</strong>: セッションCookieに <code>HttpOnly</code>（JavaScriptからのアクセス禁止）および <code>Secure</code>（HTTPS通信限定）属性を付与しているか。</li>
              <li><strong>パスワードのソルト付き強固ハッシュ化保存</strong>: データベースに平文パスワードを保存せず、<code>BCrypt</code> や <code>Argon2</code> などの暗号学的ハッシュ関数を使用しているか。</li>
              <li><strong>WAF（Web Application Firewall）とレート制限</strong>: アプリケーション手前にAWS WAFやCloudflare等を配置し、悪意あるアクセスやDDoS攻撃を自動遮断しているか。</li>
              <li><strong>脆弱性スキャンの自動化</strong>: GitHub DependabotやCI/CDパイプラインを構築し、利用しているオープンソースライブラリの既知の脆弱性を常時監視しているか。</li>
            </ul>
          </div>

          <h2 id="sec-pricing-table">4. 【費用相場】セキュリティ対策込みのシステム開発費用と工期比較</h2>
          <p>
            システム開発の見積もりにおいて、セキュリティ対策が「別料金のオプション」として数百万円上乗せされるケースがあります。以下は、一般的な大手SIerと、<strong>Ill（イル）株式会社</strong> の標準セキュリティ込み開発費用の比較です。
          </p>

          <div class="article-table-wrapper">
            <table class="article-table">
              <thead>
                <tr>
                  <th>開発規模・用途</th>
                  <th>含まれるセキュリティ対策</th>
                  <th>一般的な受託相場</th>
                  <th>Ill（イル）株式会社</th>
                  <th>想定工期</th>
                </tr>
              </thead>
              <tbody>
                <tr>
                  <td><strong>新規事業・MVP（PoC版）</strong></td>
                  <td>常時HTTPS、SQLi/XSS防御、セッション保護、環境変数分離</td>
                  <td>300万〜500万円</td>
                  <td><strong>120万〜200万円</strong></td>
                  <td>約3〜4週間</td>
                </tr>
                <tr>
                  <td><strong>標準Webシステム（会員・業務）</strong></td>
                  <td>上記 + 権限管理（RBAC）、CSRF防御、パスワードBCrypt、WAF設定</td>
                  <td>600万〜1,200万円</td>
                  <td><strong>250万〜450万円</strong></td>
                  <td>約1.5〜2.5ヶ月</td>
                </tr>
                <tr>
                  <td><strong>高機密・基幹データベース連携</strong></td>
                  <td>上記 + VPC閉域網、DB暗号化、IP制限、自動スキャンCI/CD統合</td>
                  <td>1,500万〜3,000万円</td>
                  <td><strong>550万〜900万円</strong></td>
                  <td>約3〜4ヶ月</td>
                </tr>
              </tbody>
            </table>
          </div>

          <h2 id="sec-4">5. 【Ill Inc.の強み】セキュアバイデザインによる安心の設計・開発標準</h2>
          <p>
            私たち <strong>Ill（イル）株式会社 (Ill inc.)</strong> では、セキュリティを開発完了後の追加オプションではなく、<strong>「設計の最初のフェーズから標準装備する（セキュアバイデザイン）」</strong>アプローチを徹底しています。
          </p>
          <div style="display: grid; grid-template-columns: repeat(auto-fit, minmax(280px, 1fr)); gap: 16px; margin: 28px 0;">
            <div style="background: var(--bg-subtle); border-radius: 8px; padding: 20px; border-left: 4px solid var(--color-cyan);">
              <h4 style="margin: 0 0 8px 0; font-size: 1.6rem; color: var(--text-main);">☁️ クラウド閉域網・VPC分離設計</h4>
              <p style="margin: 0; font-size: 1.4rem; color: var(--text-muted); line-height: 1.6;">
                AWS/GCP上でデータベースをプライベートサブネットに隔離し、外部インターネットからの直接アクセスを物理的に遮断します。
              </p>
            </div>
            <div style="background: var(--bg-subtle); border-radius: 8px; padding: 20px; border-left: 4px solid var(--color-purple);">
              <h4 style="margin: 0 0 8px 0; font-size: 1.6rem; color: var(--text-main);">🔑 最小権限（Least Privilege）の徹底</h4>
              <p style="margin: 0; font-size: 1.4rem; color: var(--text-muted); line-height: 1.6;">
                IAMロールやAPIキーの権限を必要最小限に制限し、万が一のキー漏洩時にも被害範囲を極小化します。
              </p>
            </div>
            <div style="background: var(--bg-subtle); border-radius: 8px; padding: 20px; border-left: 4px solid var(--color-pink);">
              <h4 style="margin: 0 0 8px 0; font-size: 1.6rem; color: var(--text-main);">🤖 自動静的コード解析とCI/CDテスト</h4>
              <p style="margin: 0; font-size: 1.4rem; color: var(--text-muted); line-height: 1.6;">
                コード push 時に自動でセキュリティ診断テストを実行し、脆弱性のあるコードが本番環境へデプロイされるのを未然に防止します。
              </p>
            </div>
            <div style="background: var(--bg-subtle); border-radius: 8px; padding: 20px; border-left: 4px solid #10B981;">
              <h4 style="margin: 0 0 8px 0; font-size: 1.6rem; color: var(--text-main);">📋 納品時セキュリティ診断チェックシート</h4>
              <p style="margin: 0; font-size: 1.4rem; color: var(--text-muted); line-height: 1.6;">
                IPA（情報処理推進機構）の安全なウェブサイトの作り方ガイドラインに準拠したチェックシートを納品時に無償提供いたします。
              </p>
            </div>
          </div>

          <h2 id="section-faq">6. よくある質問（FAQ）</h2>
          <div class="faq-container">
            <div class="faq-item">
              <h3>Q. セキュリティ対策を強化すると、開発費用や月額サーバー代は大幅に高くなりますか？</h3>
              <p>A. いいえ、大幅に高くなることはありません。モダンなフレームワーク（Next.js/TypeScript/PostgreSQL）やクラウド標準機能（AWS WAF/Cloudflare/Let's Encrypt等）を適切に設計段階から活用するため、追加の専用高額アプライアンスを導入することなく、最小限の固定費で高いセキュリティ水準を実現できます。</p>
            </div>
            <div class="faq-item">
              <h3>Q. 開発完了後に第三者機関による脆弱性診断（ペネトレーションテスト）を受けることは可能ですか？</h3>
              <p>A. はい、完全に可能です。他社のセキュリティ診断会社による診断実施時にも、検出事項への対応や診断環境のセットアップなどを全面的にサポートいたします。</p>
            </div>
            <div class="faq-item">
              <h3>Q. 個人情報保護法や各種業界ガイドラインに準拠した仕様策定も相談できますか？</h3>
              <p>A. はい。ユーザーデータの保存期間設定、退会時のデータ完全消去、アクセスログの取得・保管など、法令要件に適合したシステム仕様の設計から伴走いたします。</p>
            </div>
          </div>
"""

pattern = r'(?s)<main class="article-body">.*?</main>'
replacement = f'<main class="article-body">\n{new_body_content}\n\n          <!-- Eye-catching Bottom CTA Banner -->\n          <div class="article-bottom-cta">\n            <div class="cta-badge">\n              <span class="badge-dot"></span>無料相談・相見積もり歓迎\n            </div>\n            <h3 class="cta-title">システム開発・AI導入の無料相談・概算見積もり</h3>\n            <p class="cta-desc">\n              不要な機能を削ぎ落とす「ミニマル設計」で、高品質な開発を適正価格で実現します。\n            </p>\n            <div class="cta-check-pills">\n              <span class="cta-check-pill">\n                <svg class="check-icon" width="16" height="16" viewBox="0 0 20 20" fill="currentColor">\n                  <path fill-rule="evenodd" d="M10 18a8 8 0 100-16 8 8 0 000 16zm3.707-9.293a1 1 0 00-1.414-1.414L9 10.586 7.707 9.293a1 1 0 00-1.414 1.414l2 2a1 1 0 001.414 0l4-4z" clip-rule="evenodd"/>\n                </svg>\n                他社見積もりの妥当性診断\n              </span>\n              <span class="cta-check-pill">\n                <svg class="check-icon" width="16" height="16" viewBox="0 0 20 20" fill="currentColor">\n                  <path fill-rule="evenodd" d="M10 18a8 8 0 100-16 8 8 0 000 16zm3.707-9.293a1 1 0 00-1.414-1.414L9 10.586 7.707 9.293a1 1 0 00-1.414 1.414l2 2a1 1 0 001.414 0l4-4z" clip-rule="evenodd"/>\n                </svg>\n                最短即日の概算提示\n              </span>\n              <span class="cta-check-pill">\n                <svg class="check-icon" width="16" height="16" viewBox="0 0 20 20" fill="currentColor">\n                  <path fill-rule="evenodd" d="M10 18a8 8 0 100-16 8 8 0 000 16zm3.707-9.293a1 1 0 00-1.414-1.414L9 10.586 7.707 9.293a1 1 0 00-1.414 1.414l2 2a1 1 0 001.414 0l4-4z" clip-rule="evenodd"/>\n                </svg>\n                仕様変更に強いアジャイル\n              </span>\n            </div>\n            <div class="cta-buttons">\n              <a href="../index.html#contact" class="btn btn-primary btn-cta-primary">\n                無料相談・見積もりを依頼する <span class="arrow">→</span>\n              </a>\n            </div>\n            <p class="cta-microcopy">\n              <span>🔒</span> オンライン相談対応・無理な営業は一切いたしません\n            </p>\n          </div>\n        </main>'

content = re.sub(pattern, replacement, content)

with open(file_path, "w", encoding="utf-8") as f:
    f.write(content)

print("Updated column/web-system-security.html successfully!")
