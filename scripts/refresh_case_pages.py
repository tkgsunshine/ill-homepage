#!/usr/bin/env python3
"""Refresh the cases (実績) pages. Safe to run again (idempotent).

- cases/index.html: plain-language card text (困りごと / やったこと), featured first card,
  page-switch area, cases.css / cases.js.
- cases/*.html (each case): cases.css, facts row class, shared CTA,
  and a "ほかの事例" block built from the list page (between related-cases markers).

When you add a case: add its card to cases/index.html (and a CARD_TEXT entry here), then run
    python3 scripts/refresh_case_pages.py
"""
import html
import re
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
CASES = ROOT / "cases"
CSS_TAG = '<link rel="stylesheet" href="cases.css?v=2">'

# Card text for the list page: (困りごと, やったこと). Plain language, no numbers (numbers go in CARD_RESULT).
CARD_TEXT = {
    "claude-code-x-auto-posting": ("SNSの毎日の発信が、手作業では続かない。", "AIが翌日分の投稿案を作り、人が承認したものだけを自動で投稿する仕組み。"),
    "ai-employee-development": ("ホームページの細かな修正や更新に、人の手が足りない。", "ルールを渡したAIが修正案を作り、人が確認して反映する進め方。"),
    "ai-employee-marketing": ("コラムの企画・公開・見直しを続ける人手がない。", "AIが記事の公開と検索データの分析を回し、人は判断だけをする分担。"),
    "ai-daily-report-automation": ("自動で動く仕組みが増え、毎日何が起きたか追いきれない。", "毎晩AIが日報をまとめ、人の判断が必要なことだけを知らせる仕組み。"),
    "ai-dashboard-site-health": ("運用の状況やサイトの速さが、数字で見えていない。", "日報を一覧できる画面と、表示速度を自動で測るレポート。"),
    "meshi-drive-lp": ("飲食店に、デリバリーを始める利点がうまく伝わっていない。", "税率の差をひと目で伝える構成と、30秒で終わる相談フォームを備えた宣伝用ページ。"),
    "security-recruitment": ("古い仕組みの求人サイトが重く、サーバー代も高い。", "サイトを作り直し、安く安全に動くクラウドの構成へ引っ越し。"),
    "matching-platform": ("安心して使える出会いのサービスを、新しく立ち上げたい。", "相性の計算、AIによる自己紹介文づくり、不適切な発言の検知を備えたアプリ。"),
    "enterprise-rag": ("社内の資料が散らばり、必要な情報がすぐ見つからない。", "見てよい人だけが、社内の資料をAIに質問して探せる仕組み。"),
    "recruitment-portal": ("求人票づくりと、応募者との条件合わせに手間がかかる。", "履歴書からスキルを読み取り、AIが求人票づくりを手伝う求人サイト。"),
    "interview-feedback": ("面談の振り返りが、担当者の感覚頼りになっている。", "面談の動画をAIが文字にして分析し、振り返りのレポートを自動で作る仕組み。"),
    "staffing-crm": ("案件・スタッフ・シフト・請求の情報が、バラバラに管理されている。", "まとめて管理でき、契約内容の確認も自動で行う社内システム。"),
    "disabled-community": ("障がいのある方が、安心して使える交流の場が少ない。", "読み上げや見やすさに配慮し、本人確認も備えた交流アプリ。"),
    "ma-contracts": ("M&Aの契約書づくりに時間がかかり、確認漏れも心配。", "AIが契約書の下書きを作り、金額の食い違いや注意すべき条文を自動で確かめる仕組み。"),
    "filemaker-optimization": ("社内のデータベース（FileMaker）の検索や帳票の印刷が遅い。", "遅い原因を突き止めて処理を見直し、クラウドへ移して速くした。"),
    "gcp-migration": ("古い自社サーバーの保守に、手間と費用がかかる。", "システムをクラウド（Google Cloud）へ引っ越し、保守の手間を減らした。"),
    "cloud-security": ("クラウドの安全対策が、どこまでできているか分からない。", "不正アクセス対策など17項目を点検し、まとめて強化した。"),
    "restaurant-recruitment": ("店舗ごとの求人と応募者の管理が、手作業でバラバラ。", "求人づくり・応募者の管理・面接日程の調整をひとつにまとめた採用の仕組み。"),
    "foreign-matching": ("日本に住む外国の方が、言葉の壁で交流しにくい。", "在留カードで本人確認をし、AI翻訳つきでチャットできる交流アプリ。"),
    "car-rental": ("海外のレンタカー予約と、日本側の支払い・車両の情報がつながっていない。", "多言語で予約でき、空き状況と支払いが自動でそろう予約サイト。"),
    "sns-app": ("自分たちのSNSを、新しいサービスとして立ち上げたい。", "多くの利用者に耐える、つぶやき・共有機能つきのSNSアプリ。"),
    "real-estate-elearning": ("全国の加盟店で、営業研修の質がそろわない。", "動画研修と学習の記録、練習動画への指導ができる研修システム。"),
    "telemedicine": ("通院の手間を減らし、オンラインで診察を受けられるようにしたい。", "ビデオ診察・予約・事前の問診・支払いまでできるスマホアプリ。"),
    "pharmacy-inventory": ("薬の在庫の過不足や、期限切れによるムダが出ている。", "バーコードで入出庫を記録し、期限や在庫の注意を知らせる在庫管理の仕組み。"),
}

# Headline result shown on the card. Only numbers the user confirmed as real (2026-11-02).
# pharmacy-inventory: the 4,200万円 figure is NOT real and was removed; do not reintroduce it.
CARD_RESULT = {
    "meshi-drive-lp": "企画から公開まで2日で納品",
    "security-recruitment": "サーバー代が月100万円超から40万円台に（約60%削減）",
    "matching-platform": "初回登録を最後まで終える人が55%から92%に",
    "enterprise-rag": "社内の情報探しが1人1日45分から5分に",
    "recruitment-portal": "求職者の登録完了率が35%から88%に",
    "interview-feedback": "面談後の記録づくりが1回20分から3分に",
    "staffing-crm": "月末の請求・契約更新が5営業日から半日に",
    "disabled-community": "公開から半年で200以上の福祉施設が登録",
    "ma-contracts": "資料を見せるまでの期間が平均10日から最短即日に",
    "filemaker-optimization": "検索・集計が15秒以上から0.2秒に",
    "gcp-migration": "サーバーの月額費用を65%削減",
    "cloud-security": "金融機関の第三者による安全監査を指摘ゼロで通過",
    "restaurant-recruitment": "当日の欠員を埋められた割合が89%",
    "foreign-matching": "ビザ申請書類の作成が1件12時間から40分に",
    "car-rental": "予約の手入力作業が月120時間からゼロに",
    "sns-app": "公開3ヶ月で有料会員が2万人を突破",
    "real-estate-elearning": "研修の受講完了率が62%から96%に",
    "telemedicine": "オンライン診療が月1,200件を突破",
    "pharmacy-inventory": "発注・在庫管理の事務が1店舗1日1.5時間減",
}

TAB_LABELS = {
    "all": "すべて",
    "gen-ai": "AI活用・自動化",
    "system-app": "業務システム・Web",
    "matching-app": "新規サービス・アプリ",
    "cloud-security": "インフラ・セキュリティ",
}

SHARED_CTA = """<div class="glass-panel cases-cta" style="margin-top: 6rem;">
        <h3 class="cases-cta-title">
          AI駆動開発・MVP開発のご相談・無料お見積もり
        </h3>
        <p class="cases-cta-desc">
          新規Webアプリ・iOS/Androidアプリを、Claude Codeを活用したAI駆動開発とベトナムのオフショアチームで開発します。<br>
          <span class="gradient-text" style="font-weight: 700;">MVPは10万〜100万円、数日〜数週間から。要件により個別にお見積もりします。</span>
        </p>
        <div class="cases-cta-buttons">
          <a href="../#contact" class="btn btn-primary">無料で相談する</a>
          <a href="../#services" class="btn btn-secondary">サービス内容を見る</a>
        </div>
      </div>"""

CARD_RE = re.compile(
    r'(<article class="column-card[^"]*" data-category="(?P<cat>[^"]+)">)(?P<body>.*?)</article>', re.S
)


def add_body_class(s):
    return re.sub(r'<body class="theme-light">', '<body class="theme-light cases-page">', s, count=1)


def add_css(s):
    if "cases.css?v=" in s:
        return re.sub(r'cases\.css\?v=\d+', CSS_TAG.split('href="')[1].split('"')[0], s)
    return re.sub(r'(<link rel="stylesheet" href="\.\./style\.css\?v=\d+">)', r'\1\n  ' + CSS_TAG, s, count=1)


def read_cards(index_html):
    cards = []
    for m in CARD_RE.finditer(index_html):
        body = m.group("body")
        slug = re.search(r'href="/cases/([^"]+)"', body).group(1)
        cards.append({
            "slug": slug,
            "cat": m.group("cat"),
            "badge": re.search(r'column-card-badge">([^<]*)<', body).group(1),
            "title": re.search(r'column-card-title">([^<]*)<', body).group(1),
            "img": re.search(r'<img src="\.\./([^"]+)"', body).group(1),
        })
    return cards


def refresh_index():
    p = CASES / "index.html"
    s = p.read_text(encoding="utf-8")
    s = add_body_class(s)
    s = add_css(s)

    def card(m):
        head, body = m.group(1), m.group("body")
        slug = re.search(r'href="/cases/([^"]+)"', body).group(1)
        q, a = CARD_TEXT[slug]
        text = (f'<span class="case-q"><b>困りごと<span class="sep">：</span></b>{q}</span> '
                f'<span class="case-a"><b>やったこと<span class="sep">：</span></b>{a}</span>')
        if slug in CARD_RESULT:
            text += f' <span class="case-r"><b>結果<span class="sep">：</span></b>{CARD_RESULT[slug]}</span>'
        body = re.sub(r'<p class="column-card-excerpt">.*?</p>', f'<p class="column-card-excerpt">{text}</p>', body, flags=re.S)
        return head + body + "</article>"

    s = CARD_RE.sub(card, s)
    # featured = first card
    s = s.replace('column-card glass-card reveal is-featured"', 'column-card glass-card reveal"')
    s = s.replace('<article class="column-card glass-card reveal"', '<article class="column-card glass-card reveal is-featured"', 1)
    for key, label in TAB_LABELS.items():
        s = re.sub(rf'(<button class="category-tab[^"]*" data-filter="{key}">)[^<]*(</button>)', rf'\g<1>{label}\g<2>', s)
    if 'id="column-pagination"' not in s:
        s = s.replace('      <!-- CTA Cards Area -->',
                      '      <nav class="pagination-container" id="column-pagination" aria-label="事例一覧のページ送り"></nav>\n\n      <!-- CTA Cards Area -->', 1)
    if 'cases.js?v=' not in s:
        s = s.replace('<script defer src="../script.js', '<script defer src="cases.js?v=1"></script>\n  <script defer src="../script.js', 1)
    p.write_text(s, encoding="utf-8")
    return read_cards(s)


def related_block(cards, me):
    mine = next(c for c in cards if c["slug"] == me)
    same = [c for c in cards if c["slug"] != me and c["cat"] == mine["cat"]]
    rest = [c for c in cards if c["slug"] != me and c["cat"] != mine["cat"]]
    pick = (same + rest)[:3]
    items = "\n".join(
        f'''          <li><a href="/cases/{c["slug"]}">
            <img src="../{c["img"]}" alt="" loading="lazy" decoding="async" width="800" height="450">
            <span class="case-related-body"><span class="case-related-label">{c["badge"]}</span><span class="case-related-name">{c["title"]}</span></span>
          </a></li>''' for c in pick)
    return f'''<!-- related-cases:start -->
      <section class="case-related" aria-labelledby="case-related-title">
        <div class="case-related-head">
          <h2 class="case-related-title" id="case-related-title">ほかの事例</h2>
          <a class="case-related-all" href="./">事例をすべて見る →</a>
        </div>
        <ul class="case-related-list">
{items}
        </ul>
      </section>
      <!-- related-cases:end -->'''


INFO_BOX_RE = re.compile(
    r'<div style="background: rgba\(255, 255, 255, 0\.03\); border: 1px solid rgba\(255, 255, 255, 0\.08\); '
    r'border-radius: 1\.2rem; padding: 2\.2rem; margin-bottom: 3\.5rem;">(\s*)'
    r'<div style="display: grid; grid-template-columns: repeat\(auto-fit, minmax\(200px, 1fr\)\); gap: 1\.8rem;">'
)
CTA_RE = re.compile(r'<div class="glass-panel cases-cta"[^>]*>.*?<div class="cases-cta-buttons">.*?</div>\s*</div>', re.S)


def refresh_case(path, cards):
    s = path.read_text(encoding="utf-8")
    s = add_body_class(s)
    s = add_css(s)
    s = INFO_BOX_RE.sub(r'<div class="case-facts">\1<div class="case-facts-grid">', s)
    s = re.sub(r'<!-- related-cases:start -->.*?<!-- related-cases:end -->\s*', '', s, flags=re.S)
    s = CTA_RE.sub(lambda m: related_block(cards, path.stem) + "\n\n      " + SHARED_CTA, s, count=1)
    path.write_text(s, encoding="utf-8")


def main():
    cards = refresh_index()
    missing = [c["slug"] for c in cards if c["slug"] not in CARD_TEXT]
    if missing:
        raise SystemExit(f"CARD_TEXT is missing: {missing}")
    for c in cards:
        refresh_case(CASES / f'{c["slug"]}.html', cards)
    print(f"refreshed index + {len(cards)} case pages")


if __name__ == "__main__":
    main()
