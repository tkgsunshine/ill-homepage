"""Weekly Search Console report: click sources, top-10 queries, rewrite candidates (avg position 10-45) and low-CTR pages.

Reads credentials from gsc-credentials.json (written from the GSC_CREDENTIALS secret).
Writes docs/marketing/weekly/YYYY-MM-DD.md for the marketing-employee agent to act on.
"""
import datetime
import os
import sys

from google.oauth2 import service_account
from googleapiclient.discovery import build

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
SITE_URL = os.environ.get("GSC_SITE_URL", "")
POS_MIN, POS_MAX = 10, 45
MIN_IMPRESSIONS = 5

creds = service_account.Credentials.from_service_account_file(
    os.path.join(ROOT, "gsc-credentials.json"),
    scopes=["https://www.googleapis.com/auth/webmasters.readonly"],
)
service = build("searchconsole", "v1", credentials=creds)

if not SITE_URL:
    # Do not guess: this service account can see several sites, and a report for the wrong site is worse than none.
    sites = [s["siteUrl"] for s in service.sites().list().execute().get("siteEntry", [])]
    sys.exit("GSC_SITE_URL is not set. Set the repository variable GSC_SITE_URL to one of: " + ", ".join(sites))

today = datetime.date.today()
# GSC data lags ~2 days
end = today - datetime.timedelta(days=2)
start = end - datetime.timedelta(days=27)


def query(dimensions, limit=1000):
    body = {"startDate": str(start), "endDate": str(end), "dimensions": dimensions, "rowLimit": limit}
    return service.searchanalytics().query(siteUrl=SITE_URL, body=body).execute().get("rows", [])


qp = query(["query", "page"])
candidates = sorted(
    (r for r in qp if POS_MIN <= r["position"] <= POS_MAX and r["impressions"] >= MIN_IMPRESSIONS),
    key=lambda r: -r["impressions"],
)[:30]
pages = query(["page"])
low_ctr = sorted(
    (r for r in pages if r["impressions"] >= 30 and r["ctr"] < 0.02),
    key=lambda r: -r["impressions"],
)[:15]
# Where the clicks actually come from, and which queries already sit on page one.
# (Added 2026-11-24: the tables below only show positions 10-45, which hid both.)
click_pages = sorted((r for r in pages if r["clicks"] > 0), key=lambda r: (-r["clicks"], -r["impressions"]))[:15]
click_queries = sorted((r for r in qp if r["clicks"] > 0), key=lambda r: (-r["clicks"], -r["impressions"]))[:20]
top10 = sorted(
    (r for r in qp if r["position"] < POS_MIN and r["impressions"] >= MIN_IMPRESSIONS),
    key=lambda r: -r["impressions"],
)[:30]
BUCKETS = [("1〜3位", 0, 3.5), ("4〜10位", 3.5, 10.5), ("11〜20位", 10.5, 20.5), ("21〜50位", 20.5, 50.5), ("51位以下", 50.5, 10**6)]
bucket_rows = []
for label, lo, hi in BUCKETS:
    rs = [r for r in pages if lo <= r["position"] < hi]
    bucket_rows.append((label, len(rs), sum(r["impressions"] for r in rs), sum(r["clicks"] for r in rs)))
total_clicks = sum(r["clicks"] for r in pages)
total_imp = sum(r["impressions"] for r in pages)

lines = [
    f"# GSC週次レポート {today}",
    f"対象: {SITE_URL} / {start} ~ {end}",
    f"合計クリック: {total_clicks} / 表示回数: {total_imp}",
    "",
    "## 掲載順位ごとの内訳（ページ単位）",
    "| 平均順位 | ページ数 | 表示 | クリック |",
    "|---|---|---|---|",
    *[f"| {label} | {n} | {imp} | {clk} |" for label, n, imp, clk in bucket_rows],
    "",
    "## クリックのあったページ（クリックの多い順）",
    "| ページ | クリック | 表示 | CTR | 順位 |",
    "|---|---|---|---|---|",
    *[
        f"| {r['keys'][0]} | {r['clicks']} | {r['impressions']} | {r['ctr'] * 100:.1f}% | {r['position']:.1f} |"
        for r in click_pages
    ],
    "",
    "## クリックのあった検索語（検索語が非公開の分は含まれない）",
    "| クエリ | ページ | クリック | 表示 | 順位 |",
    "|---|---|---|---|---|",
    *[
        f"| {r['keys'][0]} | {r['keys'][1]} | {r['clicks']} | {r['impressions']} | {r['position']:.1f} |"
        for r in click_queries
    ],
    "",
    f"## 1ページ目の検索語（平均順位 {POS_MIN}位未満・表示{MIN_IMPRESSIONS}回以上）",
    "| クエリ | ページ | 順位 | 表示 | クリック |",
    "|---|---|---|---|---|",
    *[
        f"| {r['keys'][0]} | {r['keys'][1]} | {r['position']:.1f} | {r['impressions']} | {r['clicks']} |"
        for r in top10
    ],
    "",
    f"## リライト候補KW（平均順位 {POS_MIN}〜{POS_MAX}位・表示{MIN_IMPRESSIONS}回以上）",
    "| クエリ | ページ | 順位 | 表示 | クリック |",
    "|---|---|---|---|---|",
]
for r in candidates:
    q, p = r["keys"]
    lines.append(f"| {q} | {p} | {r['position']:.1f} | {r['impressions']} | {r['clicks']} |")
lines += ["", "## 低CTRページ（表示30回以上・CTR2%未満）", "| ページ | 表示 | CTR | 順位 |", "|---|---|---|---|"]
for r in low_ctr:
    lines.append(f"| {r['keys'][0]} | {r['impressions']} | {r['ctr'] * 100:.1f}% | {r['position']:.1f} |")

out_dir = os.path.join(ROOT, "docs", "marketing", "weekly")
os.makedirs(out_dir, exist_ok=True)
out = os.path.join(out_dir, f"{today}.md")
with open(out, "w", encoding="utf-8") as f:
    f.write("\n".join(lines) + "\n")
print(f"Wrote {out}")
