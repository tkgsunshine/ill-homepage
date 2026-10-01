# マーケAI社員 初期設定ガイド

## 現状（すでに自動化済み）
- 1日2回のコラム自動生成・公開（GitHub Actions → Vercel）
- sitemap / JSON-LD / OGP の自動同期

## AI社員が担う領域（未自動化の部分）
| 領域 | 内容 | 頻度 |
|---|---|---|
| 分析 | GSCデータからリライト/新規KW抽出 | 週1 |
| 企画 | `editorial_calendar.json` の補充（残10本維持） | 週1 |
| 改善 | 低CTR記事のtitle/description・FAQ改善 | 週1 |
| 配信 | X/LinkedIn/メルマガ原稿 | 公開ごと/月1 |

AI社員の定義: `.claude/agents/marketing-employee.md`（Claude Codeで `@marketing-employee` と呼び出し）

## 推奨の初期設定（優先順）
1. **計測基盤**: Google Search Console と GA4 を接続し、問い合わせ完了を CV イベントに設定
2. **GitHub Secrets**: `GSC_CREDENTIALS`（サービスアカウントJSON）を登録 → `fetch_gsc_data.py` を週次Action化
3. **週次レビューの定期実行**: 毎週月曜に AI社員が分析→カレンダー補充→PR作成（人間は承認のみ）
4. **記事品質ゲート**: コラム公開前に typo / canonical / 文字数チェックを CI で必須化
5. **リード獲得**: 問い合わせフォームのUTM保存、CTA A/Bテスト、ホワイトペーパー（見積り比較表など）でメール取得
6. **配信チャネル**: X と LinkedIn を公開コラムから半自動投稿（最初は下書き生成→人間承認）

## 人間が承認すべきもの
価格・事例の記載、CTA/サイト構造の大幅変更、外部への自動投稿の有効化。

## 週次GSCレポート（導入済み）
`.github/workflows/weekly_gsc_report.yml` が毎週月曜9:07 JSTに `docs/marketing/weekly/YYYY-MM-DD.md` を生成します（リライト候補KW・低CTRページ）。AI社員はこの最新レポートを読んで施策を提案します。

### 有効化手順（人間の作業）
1. Google Cloud でサービスアカウントを作成し、Search Console API を有効化、JSONキーを発行
2. Search Console の「設定 > ユーザーと権限」にそのサービスアカウントのメールを「制限付き」で追加
3. GitHub リポジトリ Settings > Secrets に `GSC_CREDENTIALS`（JSON全文）を登録
4. （任意）Variables に `GSC_SITE_URL`（例 `sc-domain:ill-inc.net`）。未設定なら最初のプロパティを使用
5. Actions タブから "Weekly GSC Report" を手動実行して動作確認
