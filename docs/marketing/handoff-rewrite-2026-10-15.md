# 引き継ぎメモ: コラム書き直し（2026-10-15 時点）

新しい会話（セッション）で、コラム書き直しを続けるためのメモ。会話の記憶は引き継がれないので、まずこのファイルと、下の「先に読むもの」を読む。

## 先に読むもの
- `CLAUDE.md` / `.agents/AGENTS.md`（特に項目5〜17）/ `REGULATIONS.md`（第9条）
- `docs/marketing/content-audit-2026-10-15.md`（重複調査の方法と結果）
- `scripts/rewrite_article_body.py`（本文の差し替えと検査。使い方は冒頭の説明）
- `scripts/rewrite_data/batch1.py` 〜 `batch3.py`（書き直しの書き方の見本）

## 何のための作業か（ユーザーが承認済み）
- 記事に残っている「検索キーワードを並べた不自然な見出し・文」を直す。
- 別テーマの費用表・よくある質問（特に「マッチングプラットフォーム・C2Cサービスの開発費用と相場比較」）を、記事ごとの内容に差し替える。
- 読者は 50/50（起業家・新規事業担当 と 中小企業の担当者）。専門用語は初出で説明する。
- Ill側の価格は、MVP 10万〜100万円（数日〜数週間）／標準 100万〜300万円（目安・約1〜2ヶ月）／大規模 個別見積もり、のみ。契約条件（着手金・保証期間・単価）は書かない。事実を作らない（体験談・実績の捏造をしない）。

## 進み具合
- 書き直し済み: 011〜013, 015, 017, 018（#46）／009, 010, 014, 016, 019, 020（#47）／021〜025（#48。マージ済みか要確認）
- **008（不動産向けCRM）は、ユーザーの指示で残す**（削除・リダイレクトしない）。不自然な文だけ直す。テーマ（不動産）は変えない。
- 残り（要書き直し）の見つけ方:
  - `grep -lE 'ターゲットキーワード|取り組む企業が急増' column/*.html`（確実な不具合。8本前後）
  - `grep -l 'マッチングプラットフォーム・C2Cサービスの開発費用と相場比較' column/*.html`（別テーマの費用表）
  - `grep -lE '<h2 id="sec-[0-9]">[0-9]\. 【' column/*.html`（見出しの【キーワード】。約56本。ただし 095 以降の手書き記事の【予算別の目安】のような、見出しのラベルは不自然ではないので、内容を見て判断する）
- 次の山: 009〜025 の外の、`custom-crm-development-cost` / `how-to-reduce-system-development-cost` / `mvp-development-startup-speed` / `rag-chatbot-internal-document-cost` / `react-native-app-development-cost` / `system-development-estimation-details` / `system-development-requirements-definition-support`、そして 035〜087 の自動生成記事。
- その後: 題名と別の本文（AIエージェントの文章）が入っている10本の差し替え: enterprise-genai-security, genai-market-trends-2026, genai-vendor-selection-tips, genai-roi-cost-design, offshore-agile-development, mvp-validation-strategy, micro-frontends-architecture, ai-agent-implementation, agile-requirements-definition, llm-providers-comparison（`ai-agent-business-automation` は、そのままでよい）。
- さらに: 本文の50〜90%が他記事と同じ27本（`content-audit-2026-10-15.md` の表）。

## 進め方（1回 5〜6本）
1. `scripts/rewrite_data/batchN.py` を作る（見本は batch3）。`pricing: None` にして表を省いてもよい。
2. `python3 scripts/rewrite_article_body.py scripts/rewrite_data/batchN.py --check` で検査 → 通ったら `--check` なしで書き込む。
3. 1ページをブラウザで見て確認（Playwright / Chromium は `/opt/pw-browsers/chromium`、`--no-sandbox`）。
4. 作業ブランチで commit → PR（日本語の本文）。mainへ直接pushしない。`.github/workflows/` は変更しない。
5. ホーム（https://claude.ai/artifact/9eu8jRktA8nGCC8HKN7L8A）の DB に、tasks（PRのマージ依頼）と feed（報告）を1件ずつ書く。
