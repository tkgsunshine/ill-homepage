"""第6弾の4本の題名と説明文を、検索された言葉が先に来る形に変える（2026-11-19）。

使い方: python3 scripts/rewrite_data/batch6_titles.py [--check]

変える場所: <title>、meta description、og:/twitter: の title と description、JSON-LD の headline と description、
h1、バナーの aria-label、コラム一覧（column/index.html）のカード、記事キュー（editorial_calendar.json）。
古い題名・説明文が見つからない場所は、すでに変更済みとみなす（何度実行しても同じ結果になる）。
"""
import html
import json
import os
import re
import sys

ROOT = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
SUFFIX = " | Ill（イル）株式会社"

NEW = {
    "083-web-system-development-cost-market-price.html": (
        "業務システム・Webシステムの開発費用相場｜情報共有・予約・会員サイト別の金額と内訳",
        "業務システム・Webシステムの開発費用相場を、情報共有・予約・会員サイト・取引先ポータルなど用途別に解説。費用が決まる仕組み、既製ツールとの比べ方、開発費のほかにかかる費用、見積もりを抑える方法をまとめました。",
    ),
    "087-generative-ai-app-development-cost-guide.html": (
        "AIアプリの開発費用と相場｜生成AIを組み込む業務アプリの内訳と、毎月の利用料の考え方",
        "AIアプリの開発費用を、作るものの例と規模別の目安で解説。費用の内訳、開発費とは別にかかる毎月のAI利用料、費用を抑える進め方を、個人起業家と中小企業の両方に向けてまとめました。",
    ),
    "091-system-development-subsidy-guide-2026.html": (
        "アプリ開発・システム開発で使える補助金と助成金｜種類の違いと申請前の注意点",
        "アプリ開発やシステム開発に使える補助金・助成金の種類と違いを、初めての方向けに解説。IT導入補助金・ものづくり補助金などの向き不向き、最新情報の調べ方、交付決定の前に発注してはいけない理由をまとめました。",
    ),
    "094-system-development-copyright-source-code-ownership.html": (
        "ソースコードの譲渡と著作権の帰属｜譲渡費用の考え方と、契約で決める5つのポイント",
        "外注したシステムのソースコードは誰のものか、譲渡の費用はどう決まるのかを、発注者向けにわかりやすく解説。譲渡・利用許諾・共有の違い、契約で決める5つのポイント、納品後に譲渡を求めるときの進め方をまとめました。",
    ),
}


def main():
    write = "--check" not in sys.argv
    idx_path = os.path.join(ROOT, "column", "index.html")
    idx = open(idx_path, encoding="utf-8").read()
    cal_path = os.path.join(ROOT, "scripts", "editorial_calendar.json")
    cal = json.load(open(cal_path, encoding="utf-8"))
    for fn, (title, desc) in NEW.items():
        path = os.path.join(ROOT, "column", fn)
        s = open(path, encoding="utf-8").read()
        old_title = html.unescape(re.search(r"<title>(.*?)</title>", s).group(1)).removesuffix(SUFFIX)
        old_desc = re.search(r'<meta name="description" content="([^"]*)">', s).group(1)
        if old_title == title and old_desc == desc:
            print("変更済み", fn)
            continue
        n_t, n_d = s.count(old_title), s.count(old_desc)
        s = s.replace(old_title, title).replace(old_desc, desc)
        # 要点ボックスが説明文を使っている場合も、上の置換で揃う
        slug = fn.removesuffix(".html")
        card = re.search(r'<article class="column-card[^"]*"[^>]*>\s*<a href="/column/' + re.escape(slug) + r'".*?</article>', idx, re.S)
        if not card:
            raise SystemExit(f"{fn}: 一覧のカードが見つかりません")
        c = card.group(0)
        c_new = c.replace(old_title, title).replace(old_desc, desc)
        idx = idx[:card.start()] + c_new + idx[card.end():]
        for e in cal:
            if e["filename"] == fn:
                e["title"] = title + SUFFIX
                e["headline"] = title
                e["description"] = desc
        for need in (f"<title>{title}{SUFFIX}</title>", f'<h1 class="article-title">{title}</h1>',
                     f'"headline": "{title}"', f'<meta name="description" content="{desc}">',
                     f'<meta property="og:title" content="{title} | Ill inc. コラム">',
                     f'<meta name="twitter:description" content="{desc}">'):
            if need not in s:
                raise SystemExit(f"{fn}: 反映されていない: {need[:40]}")
        if f'column-card-title">{title}<' not in c_new:
            raise SystemExit(f"{fn}: 一覧のカードの題名が変わっていません")
        print(f"{fn}: 題名 {n_t}か所・説明文 {n_d}か所")
        if write:
            open(path, "w", encoding="utf-8").write(s)
    if write:
        open(idx_path, "w", encoding="utf-8").write(idx)
        open(cal_path, "w", encoding="utf-8").write(json.dumps(cal, ensure_ascii=False, indent=2) + "\n")


if __name__ == "__main__":
    main()
