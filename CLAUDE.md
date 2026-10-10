# Ill inc. コーポレートサイト（ill-homepage）

このプロジェクトは Antigravity(AG) から Claude Code(CC) へ引き継ぎ済み。今後の開発・運用はCCで行う。

## 必読ルール（AG時代から継続）
@.agents/AGENTS.md
@REGULATIONS.md

## Claude Code での運用
- 作業ブランチで変更し、PRで反映する（mainへ直接pushしない）。
- マーケ業務（コラム補充・週次GSCレビュー・記事リライト）は `@marketing-employee`（`.claude/agents/marketing-employee.md`）。詳細は `docs/AI_EMPLOYEE_SETUP.md`。
- **`.github/workflows/` の公開用workflow（`daily_column.yml` 等）は本番の仕組みなので、依頼なく変更しない。**
- 事実は検証してから報告する。推測で原因を断定しない。
- 依頼のないファイル削除・無関係な改変をしない。破壊的操作（`git reset --hard` 等）は確認してから。


## 担当の線引き（マーケAI社員 / PJ別の開発・運用セッション）
- **マーケAI社員（`@marketing-employee`）**: コラム、記事キュー、SEO（タイトル・説明文・構造化データ・サイトマップ・Search Console分析）を担当する。
- **PJ別の開発・運用セッション**: 機能、画面、運用を担当する。
- **`.github/workflows/` の公開用workflow**: どちらも、ユーザーの依頼がない限り変更しない。
- どちらも、PRで変更する（mainへ直接pushしない）。
- 開発アイデア: ユーザーが新機能・改善のアイデアを話したら、`.claude/agents/dev-employee.md` の「ホーム」の節に従い、ホームのダッシュボード（https://claude.ai/artifact/9eu8jRktA8nGCC8HKN7L8A）の `ideas` に保存する（実装は依頼があるまでしない）。

## 作業の報告（AI社員ホームの「最近の報告」）
- 作業を終えたとき（PRの作成・マージ、調査の完了、不具合の修正など）に、チャットへの報告と同じ要点を、ホームのダッシュボード（https://claude.ai/artifact/9eu8jRktA8nGCC8HKN7L8A）のDBのコレクション `feed` に1件書く（ArtifactData の `set`）。ホームの「最近の報告」に、全AI社員の報告が新しい順で並び、ユーザーがチャットを見に行かなくても把握できる。
- ID: `YYYYMMDD-HHMMSS-<area>`（JST）。項目: `at`（`YYYY-MM-DD HH:MM`、JST）、`area`（`marketing` / `dev` / `x` / `other`）、`who`（例: 「月と蓮 開発」「Ill HP 開発」）、`text`（1〜2文。専門用語を避け、何が変わったか・何を確認すべきかを書く）、`link`（任意。PRなどの `https://` のURL）。
- 小さな途中作業は書かない。個人情報・秘密情報（トークン、メールアドレス等）は書かない。ホームのDBに書けない環境のときは、書けなかったことをチャットで伝える。
