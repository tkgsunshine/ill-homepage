"""One-off Search Console diagnosis: daily impressions trend + URL Inspection of sample URLs.

Reads gsc-credentials.json (written from the GSC_CREDENTIALS secret) and GSC_SITE_URL.
Writes docs/marketing/diagnosis.md.
"""
import datetime
import os
import sys

from google.oauth2 import service_account
from googleapiclient.discovery import build

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
SITE = os.environ.get("GSC_SITE_URL", "")
if not SITE:
    sys.exit("GSC_SITE_URL is not set")
BASE = os.environ.get("INSPECT_BASE", "https://www.ill-inc.net")
URLS = [x for x in os.environ.get("INSPECT_URLS", "").split() if x]

creds = service_account.Credentials.from_service_account_file(
    os.path.join(ROOT, "gsc-credentials.json"),
    scopes=["https://www.googleapis.com/auth/webmasters.readonly"],
)
svc = build("searchconsole", "v1", credentials=creds)
today = datetime.date.today()
lines = [f"# GSC診断 {today}", f"対象: {SITE}", ""]

# 1) daily impressions / clicks, last ~90 days, summed per week
start = today - datetime.timedelta(days=90)
rows = svc.searchanalytics().query(siteUrl=SITE, body={"startDate": str(start), "endDate": str(today), "dimensions": ["date"], "rowLimit": 1000}).execute().get("rows", [])
lines += ["## 週ごとの表示回数・クリック（直近約90日）", "| 週の開始日 | 表示回数 | クリック | 日数 |", "|---|---|---|---|"]
weeks = {}
for r in rows:
    d = datetime.date.fromisoformat(r["keys"][0])
    w = d - datetime.timedelta(days=d.weekday())
    a = weeks.setdefault(w, [0, 0, 0])
    a[0] += r["impressions"]; a[1] += r["clicks"]; a[2] += 1
for w in sorted(weeks):
    lines.append(f"| {w} | {weeks[w][0]} | {weeks[w][1]} | {weeks[w][2]} |")

# 2) number of distinct pages with impressions, early vs recent
def pages(s, e):
    return svc.searchanalytics().query(siteUrl=SITE, body={"startDate": str(s), "endDate": str(e), "dimensions": ["page"], "rowLimit": 1000}).execute().get("rows", [])
for label, s, e in (("9/1〜9/14", datetime.date(2026, 9, 1), datetime.date(2026, 9, 14)), ("直近14日", today - datetime.timedelta(days=16), today - datetime.timedelta(days=2))):
    p = pages(s, e)
    lines += ["", f"## 表示回数のあったページ数（{label}）: {len(p)}"]
    for r in sorted(p, key=lambda r: -r["impressions"])[:8]:
        lines.append(f"- {r['keys'][0]} 表示{r['impressions']} 順位{r['position']:.1f}")

# 3) URL Inspection
lines += ["", "## URL検査（Googleの認識）", "| URL | 判定 | カバレッジ | 最終クロール | Googleが選んだcanonical | ユーザー指定canonical |", "|---|---|---|---|---|---|"]
for u in URLS:
    try:
        res = svc.urlInspection().index().inspect(body={"inspectionUrl": u, "siteUrl": SITE}).execute()["inspectionResult"]["indexStatusResult"]
        lines.append(f"| {u} | {res.get('verdict')} | {res.get('coverageState')} | {res.get('lastCrawlTime','-')} | {res.get('googleCanonical','-')} | {res.get('userCanonical','-')} |")
    except Exception as e:
        lines.append(f"| {u} | ERROR | {str(e)[:80]} | | | |")

out = os.path.join(ROOT, "docs", "marketing")
os.makedirs(out, exist_ok=True)
open(os.path.join(out, "diagnosis.md"), "w", encoding="utf-8").write("\n".join(lines) + "\n")
print("\n".join(lines))
