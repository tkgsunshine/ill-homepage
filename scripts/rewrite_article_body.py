"""既存のコラム記事の本文を、書き直した内容に差し替える。

使い方:
  python3 scripts/rewrite_article_body.py scripts/rewrite_data/batch1.py [--check]

データファイル（Python）は、ARTICLES というリストを持つ。1件の形:
  {
    "filename": "018-simple-rfp-writing-for-non-it-buyers.html",
    "answer": "結論（2〜3文。価格は 10万〜100万円・数日〜数週間 / 100万〜300万円・約1〜2ヶ月 / 個別見積もり の範囲で書く）",
    "keywords": "検索キーワード,…（自然な語句。本文には、そのまま並べない）",   # 省略可
    "description": "メタ説明",                                                   # 省略可
    "sections": [{"h2": "見出し（番号は自動で付く）", "html": "<p>…</p>"}, …],
    "pricing": {"h2": "…", "intro": "<p>…</p>", "rows": [("名前", "機能", "他社の目安"), ×3], "note_html": "…"} または None,
    "faqs": [("質問ですか？", "答え"), …3件],
  }

差し替えるのは <main class="article-body"> の中身と、FAQ の構造化データ、keywords、dateModified だけ。
記事の題名・公開日・バナーなどは変えない。--check を付けると、書き込まずに検査だけする。
"""
import datetime
import html as htmllib
import importlib.util
import json
import os
import re
import sys

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, os.path.join(ROOT, "scripts"))
from add_answer_box import build_answer_box  # noqa: E402

ILL = {
    1: ("10万〜100万円", "数日〜数週間"),
    2: ("100万〜300万円（目安）", "約1〜2ヶ月"),
    3: ("個別見積もり", "要件により異なる"),
}


def table_html(rows):
    head = ("<th>開発の規模</th>\n        <th>主な内容</th>\n        <th>他社の目安</th>\n"
            "        <th>Ill（イル）株式会社</th>\n        <th>想定期間</th>")
    body = ""
    for i, (name, feat, other) in enumerate(rows, start=1):
        price, term = ILL[i]
        body += (f"      <tr>\n        <td><strong>{name}</strong></td>\n        <td>{feat}</td>\n"
                 f"        <td>{other}</td>\n        <td><strong>{price}</strong></td>\n        <td>{term}</td>\n      </tr>\n")
    return ('<div class="article-table-wrapper">\n  <table class="article-table">\n    <thead>\n      <tr>\n        '
            + head + "\n      </tr>\n    </thead>\n    <tbody>\n" + body + "    </tbody>\n  </table>\n</div>")


def build_main(a, old_main):
    toc, parts = [], []
    for i, s in enumerate(a["sections"], start=1):
        toc.append(f'              <li><a href="#sec-{i}">{i}. {s["h2"]}</a></li>')
        parts.append(f'\n          <h2 id="sec-{i}">{i}. {s["h2"]}</h2>\n          {s["html"]}\n')
    p = a.get("pricing")
    if p:
        toc.append(f'              <li><a href="#sec-pricing-table">{p["h2"]}</a></li>')
        parts.append(f'\n          <h2 id="sec-pricing-table">{p["h2"]}</h2>\n          {p["intro"]}\n          '
                     f'{table_html(p["rows"])}\n          {p.get("note_html", "")}\n')
    toc.append('              <li><a href="#section-faq">よくある質問</a></li>')
    faq = '\n          <h2 id="section-faq">よくある質問</h2>\n          <div class="faq-container">\n'
    for q, ans in a["faqs"]:
        faq += (f'            <div class="faq-item">\n              <h3>{q}</h3>\n              <p>{ans}</p>\n            </div>\n')
    faq += "          </div>\n"
    cta_i = old_main.find("<!-- Eye-catching Bottom CTA Banner -->")
    cta = "          " + old_main[cta_i:] if cta_i >= 0 else ""
    toc_box = ('\n          <div class="toc-box">\n            <div class="toc-title">目次</div>\n            <ul class="toc-list">\n'
               + "\n".join(toc) + "\n            </ul>\n          </div>\n")
    return build_answer_box(a["answer"], a["description"]) + toc_box + "".join(parts) + faq + "\n" + cta


def faq_jsonld(faqs):
    ent = [{"@type": "Question", "name": q,
            "acceptedAnswer": {"@type": "Answer", "text": re.sub(r"<[^>]+>", "", ans)}} for q, ans in faqs]
    data = {"@context": "https://schema.org", "@type": "FAQPage", "mainEntity": ent}
    return json.dumps(data, ensure_ascii=False, indent=2)


def text_len(h):
    return len(re.sub(r"\s+", "", htmllib.unescape(re.sub(r"<[^>]+>", "", h))))


def apply(a, write):
    path = os.path.join(ROOT, "column", a["filename"])
    s = open(path, encoding="utf-8").read()
    m = re.search(r'(<main class="article-body">)(.*?)(</main>)', s, re.S)
    if not m:
        raise SystemExit(f"{a['filename']}: main が見つかりません")
    desc = a.get("description")
    if not desc:
        d = re.search(r'<meta name="description" content="([^"]*)">', s)
        desc = htmllib.unescape(d.group(1)) if d else ""
    a = dict(a, description=desc)
    main = build_main(a, m.group(2))
    # 検査
    body_text = text_len(main)
    errs = []
    if body_text < 1800:
        errs.append(f"本文が短い（{body_text}字）")
    if "株式会社イル" in main:
        errs.append("禁止の社名表記")
    if re.search(r"【[^】]+】", re.sub(r"<[^>]+>", "", main)) and not a.get("allow_brackets"):
        errs.append("見出しなどに【】がある")
    if re.search(r"ターゲットキーワード|取り組む企業が急増", main):
        errs.append("キーワードを並べた文が残っている")
    for q, _ in a["faqs"]:
        if not q.endswith("か？"):
            errs.append(f"FAQの質問の語尾: {q[:20]}")
    if len(a["faqs"]) != 3:
        errs.append("FAQは3問")
    if errs:
        raise SystemExit(f"{a['filename']}: " + " / ".join(errs))
    new = s[:m.start()] + m.group(1) + main + "\n        " + m.group(3) + s[m.end():]
    # FAQ構造化データ
    fm = re.search(r'(<script type="application/ld\+json">\s*)(\{[^<]*?"@type":\s*"FAQPage".*?\})(\s*</script>)', new, re.S)
    if not fm:
        raise SystemExit(f"{a['filename']}: FAQPage の構造化データが見つかりません")
    new = new[:fm.start(2)] + faq_jsonld(a["faqs"]) + new[fm.end(2):]
    if a.get("keywords"):
        new = re.sub(r'<meta name="keywords" content="[^"]*">', f'<meta name="keywords" content="{a["keywords"]}">', new)
    today = datetime.datetime.now(datetime.timezone(datetime.timedelta(hours=9))).strftime("%Y-%m-%d")
    new = re.sub(r'"dateModified":\s*"\d{4}-\d{2}-\d{2}"', f'"dateModified": "{today}"', new)
    new = re.sub(r"([一-龠])？", lambda x: "か？" if x.group(1) not in ["何", "誰"] else x.group(0), new)
    if write:
        open(path, "w", encoding="utf-8").write(new)
    return body_text


def main():
    if len(sys.argv) < 2:
        raise SystemExit(__doc__)
    spec = importlib.util.spec_from_file_location("data", sys.argv[1])
    mod = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(mod)
    write = "--check" not in sys.argv
    for a in mod.ARTICLES:
        n = apply(a, write)
        print(("書き換え" if write else "検査OK"), a["filename"], n, "字")


if __name__ == "__main__":
    main()
