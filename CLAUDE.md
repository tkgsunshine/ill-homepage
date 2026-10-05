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
