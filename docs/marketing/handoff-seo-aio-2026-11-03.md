# 引き継ぎ指示書: コラムのSEO・AI検索（AIO）見直し（2026-11-03 時点）

新しい会話（プロジェクトのセッション）で、この作業を続けるための指示書。会話の記憶は引き継がれないので、まずこのファイルと「先に読むもの」を読むこと。担当は、マーケAI社員（`@marketing-employee`）。

## 0. 先に読むもの
- 各リポジトリの `CLAUDE.md`（と、そこから参照される `AGENTS.md` / `.agents/AGENTS.md` / `REGULATIONS.md`）。ルールは、リポジトリごとに違う。
- Ill: `docs/marketing/content-audit-2026-10-15.md`（重複調査）、`docs/marketing/handoff-rewrite-2026-10-15.md`（書き直しの進め方）、`docs/marketing/weekly/`（週次GSC）
- Re.en: `docs/marketing/seo-review-2026-10-23.md`、`docs/marketing/weekly/`
- 月と蓮: `docs/marketing/seo-review-2026-10-26.md`、`docs/marketing/aio-2026-10-28.md`、`docs/design/tool-pages-2026-10-29.md`、`docs/marketing/weekly/`

## 1. 3つのサイト（混同しない）
| サイト | リポジトリ | 中身 | 読者 |
|---|---|---|---|
| Ill（イル）株式会社 | `tkgsunshine/ill-homepage` | B2B開発会社の公式HP。コラム約166本（`column/*.html`） | 新規事業の個人・中小企業 |
| Re.en（リエン） | `tkgsunshine/re.en-invitation-lp` | 既婚者向けの完全審査制コミュニティの招待制LP。コラム約115本（`column-detail-*.html`） | 30〜50代の既婚男女 |
| 月と蓮 | `tkgsunshine/tsuki-to-ren` | 四柱推命・MBTIの恋愛相性占いアプリ。コラム約110本（`src/data/columnsData.ts`） | 10代後半〜20代 |

※「月と蓮」を、Re.en と取り違えない（この会話で一度取り違えた）。依頼の「月と蓮」は `tsuki-to-ren`。

## 2. 共通の約束
- 作業ブランチで変更し、PRで反映する。**mainへ直接pushしない。** マージは、ユーザーが「マージ」と言ってから。
- **`.github/workflows/` は変更しない**（公開用の本番の仕組み）。
- 各PRの後に、ホーム（https://claude.ai/artifact/9eu8jRktA8nGCC8HKN7L8A）の DB に、`tasks`（PRのマージ依頼。マージ後に `done`）と `feed`（報告）を1件ずつ書く。形式は各 `CLAUDE.md`。
- 事実は確認してから報告する。PRの状態は、報告の前に GitHub で確認する（この会話で、マージ済みのPRを「未マージ」と誤って書いた）。
- 体験談・口コミ・実在の人物の話・根拠のない統計・「専門家監修」を書かない。占いは断定しない。
- 検索データは少ない（Ill: 3か月で約4,000表示・87クリック。Re.en・月と蓮: 28日で約200表示・約10クリック）。結果が出るまで1〜2週間かかる。小さな数字の変動で、方針を変えない。

## 3. サイト別の状況と、次にやること

### 3-1. Ill（`ill-homepage`）
**済み:** コラムの書き直し 第1〜5弾（#46〜#51。011〜025、008・custom-crm・legacy・sovereign-ai など）、費用削減・MVP・RAG・React Native・見積書・要件定義の6本（#50）。
**残り（見つけ方）:**
- 別テーマの費用表が残る記事: `grep -l 'マッチングプラットフォーム・C2Cサービスの開発費用と相場比較' column/*.html`（現在: `036-2026-smb-agile-mvp-cost-optimization.html`）
- 見出しの【キーワード】: `grep -lE '<h2 id="sec-[0-9]">[0-9]\. 【' column/*.html`（現在59本）。095 以降の手書き記事の【予算別の目安】のようなラベルは不自然でないので、内容を見て判断する
- 題名と別の本文（AIエージェントの文章）が入っている10本: `enterprise-genai-security` / `genai-market-trends-2026` / `genai-vendor-selection-tips` / `genai-roi-cost-design` / `offshore-agile-development` / `mvp-validation-strategy` / `micro-frontends-architecture` / `ai-agent-implementation` / `agile-requirements-definition` / `llm-providers-comparison`（`ai-agent-business-automation` は、そのままでよい）。これらは、題名のテーマに合う本文に書き直す
- 本文の50〜90%が他記事と同じ27本（`content-audit-2026-10-15.md` の表）
- 008（不動産向けCRM）は、ユーザーの指示で残す（削除しない）。不動産は新規企画しない
**やり方:** `scripts/rewrite_article_body.py` と `scripts/rewrite_data/batchN.py`（見本は batch4・batch5）。`--check` で検査してから書き込む。1回5〜6本。
**検索データからの提案（返事待ち）:** 「仕様策定」（3か月で216表示・2クリック・平均8.5位）。表示されているのは `column/requirements-definition-tips.html` の1本。題名と説明文を調整し、具体例（仕様書の項目のひな形、決めない項目の例）を足し、関連記事（要件定義の支援・RFPの書き方）からリンクを整理する。ユーザーの了承が要る。
**注意:** 毎日の自動生成（`daily_column.yml`）が main を進める。PRを出す前に `git fetch origin main` して、衝突があれば取り込む。

### 3-2. Re.en（`re.en-invitation-lp`）
**済み（PR #42 マージ済み）:** 定型文46本を書き直し、手書き68本＋公開待ち6本を2,800字以上に増強、重複30本を統合（301リダイレクトは `vercel.json`）、題名の「(Vol.N)」を除去、OGP・JSON-LD・関連記事を整理（`scripts/normalize_column_head.py`）、記事ごとの固有アイキャッチを生成（`scripts/generate_column_banners.py`）。記事生成のひな形は `templates/column-template.html`（旧 `column-detail-52.html`）。
**次にやること:**
- マージ後の確認: 統合した旧URL（例 `/column-detail-2` → `/column-detail-54`）の転送、次回の自動公開で記事が増え、画像が記事ごとに変わること
- 画像: AGで写真を生成して追加する計画（指示書: 下の「付録」）。写真が届いたら、カレンダーの `source_photo` に割り当て、`python3 scripts/generate_column_banners.py --force`
- 1〜2週間後に、週次レポートで表示・クリックの変化を確認
- 公開待ちが10本を切ったら補充（手書きで `"authored": true` を付ける。付けないと定型文に上書きされる）
**ルール:** 家族を欺く方法・「バレない」系の助言は書かない。根拠のない監修表記をしない。

### 3-3. 月と蓮（`tsuki-to-ren`）
**済み（#180・#227・#230 マージ済み）:** コラム約112本を平均約790字→約1,830字に増強（`scripts/apply_column_rewrite.py`）、関連記事を同カテゴリ・近いキーワードから選び通常のリンクにした、/column の静的HTMLに全記事リンクを入れた、記事冒頭に「この記事の結論」と更新日（`scripts/apply_column_answers.py`）、AIチャット（ChatGPT・Perplexity・Gemini・Copilot・Claude）からの流入を管理画面で別集計、ツール型ページの設計書。
**サムネイル:** #181（別セッション）で、AGの画像30枚に切り替え済み。ただし112本に30枚なので、1枚を最大7本で使い回す（規定の「記事ごとに固有」は満たせない）。`scripts/generate-column.js` の Guard 3 は、URLにタグを足すだけで画像自体は同じ。AGに追加を依頼するか、規定を現実に合わせるかを、ユーザーと決める。
**ツール型ページ（日柱の調べ方・計算）:** 開発PJへ引き継ぎ済み。画面ができたら、マーケ側が題名・説明文・結論文・FAQ・内部リンクの文面をPRで入れる（設計書の第9章）。
**次にやること:**
- 数週間、管理画面でAI由来の流入を見る。ゼロのままなら、記事の手直しより名前の認知（X・外部サイトでの言及）に力を入れる
- 唯一クリックが出ている記事（`kaigou-shichutsuimei-guide`、魁罡）は、題名・メタ説明を変えない
- 自動公開で増えた記事には、個別の結論文が無い（メタ説明で代用される）。気になるなら `scripts/apply_column_answers.py` の手順で足す
- 公開待ち（`scripts/column-pool.json`）の補充は、本文1,800字以上・H3 3個以上で書く
**ルール:** `AGENTS.md` §2（四柱推命・MBTIの専門用語を平易にする）。鑑定ロジック（`src/utils/fortuneEngine.ts`）は変更しない。作業完了前に `npm run build`。

## 4. 作業のコツ（この会話で分かったこと）
- 並列のサブエージェントを多く起動すると、利用制限で中断する。5〜7件までにし、中断したら制限の解除後に `SendMessage` で再開する（途中の成果は残る）。
- 書き直した本文は、エージェントにJSONで書かせ、**検査つきの反映スクリプト**で入れる（各リポジトリの `scripts/apply_*.py`）。禁止語・文字数・リンク先の実在を機械的に確認できる。
- この環境の `git clone --depth 1` では、リモートの追跡情報が古くなり、終了時のフックが「未pushのコミットがある」と警告することがある。`git fetch origin +refs/heads/<ブランチ>:refs/remotes/origin/<ブランチ>` で解消する（実際には、push済みのことが多い）。
- 自動公開が main を進めるので、PRの直前に main を取り込む。衝突したら、記事ページは自分の側を採用し、反映スクリプトを再実行する。
- 画像生成の素材は、サイトの既存の写真だけ（文字は重ねる）。AIによる新しい写真は、AGの担当。

## 5. 付録: AGへの指示書
- Re.en用・月と蓮用の指示書は、この会話の一時フォルダにあった（会話の終了で消える）。必要なら、本ファイルの「3-2」「3-3」の画像の項目をもとに、書き直す（仕様の要点: 横長 1536×1024 か 1600×900 のWebP・文字を入れない・左と下に余白・既存の写真の雰囲気にそろえる・PRで渡す・既存画像は変更しない）。
