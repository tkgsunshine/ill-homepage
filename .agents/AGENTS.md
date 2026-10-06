# Workspace Rules

## Core Business Positioning & USP (Unique Selling Proposition)

1. **Target Projects**:
   - Focus on attracting **greenfield/new development projects (新規開発プロジェクト)**. This applies to both **Web applications** and **mobile apps (iOS/Android)**.

2. **Core Strength / Competitive Advantage**:
   - Our main competitive advantage is that we can build these new projects **cheaper than any competitor (どこよりも安く作れる)**.
   - Emphasize how we achieve this cost-efficiency (e.g., via minimal MVP scoping, cross-platform frameworks like React Native/Flutter, and our efficient hybrid offshore team structure).

3. **Industries / projects NOT to target**:
   - We do **not** want to take on **real estate (不動産) industry projects**.
   - Do not plan new columns, case studies, or keyword targets aimed at real estate (e.g. `不動産 CRM`, `eラーニングシステム 不動産`).
   - Do not use real estate as the example industry in new articles; use neutral or other industries instead.


## Positioning & Target (updated 2026-10-01)

4. **Goal**: Acquire leads for **new development** (new Web apps / iOS / Android).
5. **Target customers**: (a) individual entrepreneurs, (b) new-business owners inside existing companies. They want a **low-price MVP / new IT business launch**.
6. **How we want to be seen**: an **AI-native development company** — we build heavily with AI and have real AI know-how. Do not claim anything we cannot back with facts.
7. **Facts we can state** (do not invent beyond these):
   - Development tool: **Claude Code** (AI-driven development)
   - Delivery structure: **Vietnam offshore** development team (hybrid: Japan-side requirements/quality control + offshore implementation)
   - **MVP price range: 100,000 – 1,000,000 JPY (10万〜100万円)**
   - **MVP delivery: from a few days to a few weeks**
   - Beyond-MVP / full-scale development: quote per project (state "要件により個別見積もり" or a clearly-labelled rough guide; never present guesses as fixed prices)
8. **Content direction**: existing columns stay as they are. **New columns focus on MVP, new business launch, and AI-driven development.** Avoid generic "SMB DX / legacy migration" topics unless they connect to new development.
9. **Author byline**: keep **「Ill inc. 編集部」** (no personal names).
10. **No official SNS/company accounts exist** — do not add `sameAs` or invent profile URLs.
11. **Do not publish contract terms in columns**: no payment terms (e.g. 着手金/分割比率), no free-warranty / 瑕疵担保 periods, no fixed unit prices (人月単価). These are decided per client. Allowed: "月額数万円からの継続保守プランあり（条件は個別案内）" and the MVP price/time range above.
12. **Price consistency**: Ill-side prices in columns follow this ladder — MVP 10万〜100万円（数日〜数週間）／標準 100万〜300万円（目安・約1〜2ヶ月）／大規模 個別見積もり. Do not invent other Ill-side numbers.

## Answer-first (AIO / AI summaries) — added 2026-10-02

13. Every column starts with an **answer box** (結論/要点) above the table of contents. Add a hand-written `answer` (2-3 sentences, facts and price ladder from items 7 and 12 only) to new calendar entries; otherwise the generator falls back to the meta description. `scripts/add_answer_box.py` backfills pages that lack the box and is idempotent.

## Plain-language writing (Non-IT readers) — added 2026-10-06

14. **Columns and case studies must be understandable by non-IT readers.** Target readers are individual entrepreneurs and new-business owners, not engineers.
    - Explain every technical term the first time it appears (short parenthetical, or a「用語かんたん解説」box at the end of the page). Prefer everyday Japanese over loanwords and abbreviations (e.g. PR → 「変更の確認依頼」, ワークフロー → 「自動で動く仕組み」).
    - Short sentences (aim for ≤ 60 characters), one idea per sentence. Use a concrete example or analogy for each key idea.
    - Lead with "what it means for the business" (time saved, cost, risk) before how it works.
    - Table headers and headings must also be plain language.
    - All fact/price rules (items 7, 11, 12) still apply. Plain language must not add claims we cannot back.
