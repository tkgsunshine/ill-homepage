"""Answer-first summary box at the top of each column (helps readers and AI-generated summaries).

Usage: python3 scripts/add_answer_box.py   (adds the box to column pages that lack one; idempotent)
"""
import glob
import html
import os
import re

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

ANSWERS = {
    "095-mvp-development-cost-10-to-100man-what-you-can-build.html":
        "MVP開発の目安は、10万〜100万円・数日〜数週間です。10万円台は1〜2画面の簡易な検証用、50万円前後は会員登録・ログインや簡易な管理画面まで、100万円前後は決済連携や外部サービス連携まで、が作れる範囲の目安です。金額は画面数や連携の数で変わるため、個別にお見積もりします。",
}


def build_answer_box(answer, description):
    label, text = ("この記事の結論", answer) if answer else ("この記事の要点", description)
    return (
        '\n          <div class="answer-box" style="background: var(--glass-bg); border: 1px solid var(--glass-border); '
        'border-left: 4px solid var(--color-cyan); border-radius: 1.2rem; padding: 2rem 2.4rem; margin-bottom: 3.2rem;">\n'
        f'            <p style="font-weight: 700; font-size: 1.6rem; margin: 0 0 0.8rem;">{label}</p>\n'
        f'            <p style="margin: 0; line-height: 1.9;">{html.escape(text, quote=False)}</p>\n'
        '          </div>\n'
    )


def main():
    added = 0
    for path in sorted(glob.glob(os.path.join(ROOT, "column", "*.html"))):
        name = os.path.basename(path)
        if name == "index.html":
            continue
        s = open(path, encoding="utf-8").read()
        if 'class="answer-box"' in s or '<div class="toc-box">' not in s:
            continue
        m = re.search(r'<meta name="description" content="([^"]*)">', s)
        if not m:
            continue
        box = build_answer_box(ANSWERS.get(name), html.unescape(m.group(1)))
        s = s.replace('\n          <div class="toc-box">', box + '\n          <div class="toc-box">', 1)
        open(path, "w", encoding="utf-8").write(s)
        added += 1
    print("answer box added to", added, "pages")


if __name__ == "__main__":
    main()
