"""Run Lighthouse 3x per URL (mobile) and write the median run's LCP details to docs/marketing/lh-detail.md."""
import json
import os
import subprocess
import tempfile

URLS = os.environ.get("LH_URLS", "").split()


def run(url):
    out = tempfile.mktemp(suffix=".json")
    subprocess.run(["npx", "--yes", "lighthouse", url, "--quiet", "--output=json", "--output-path=" + out,
                    "--only-categories=performance", "--form-factor=mobile",
                    "--chrome-flags=--headless=new --no-sandbox"], check=True, timeout=240,
                   stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
    return json.load(open(out))


def short(x, n=700):
    s = json.dumps(x, ensure_ascii=False)
    return s if len(s) <= n else s[:n] + "…"


lines = ["# Lighthouse詳細（モバイル・3回の中央値）", ""]
for url in URLS:
    runs = []
    for _ in range(3):
        try:
            runs.append(run(url))
        except Exception as e:
            lines.append(f"- {url}: 失敗 {str(e)[:80]}")
    if not runs:
        continue
    runs.sort(key=lambda r: r["audits"]["largest-contentful-paint"]["numericValue"])
    lh = runs[len(runs) // 2]
    a = lh["audits"]
    lines += [f"## {url}", "",
              "- 3回のLCP(ms): " + ", ".join(str(round(r["audits"]["largest-contentful-paint"]["numericValue"])) for r in runs),
              f"- 性能 {round(lh['categories']['performance']['score'] * 100)} / FCP {a['first-contentful-paint']['displayValue']} / LCP {a['largest-contentful-paint']['displayValue']} / CLS {a['cumulative-layout-shift']['displayValue']} / TBT {a['total-blocking-time']['displayValue']}", ""]
    m = a.get("metrics", {}).get("details", {}).get("items", [{}])[0]
    lines += ["### metrics(observed vs simulated)", "```", short({k: v for k, v in m.items() if "FirstContentful" in k or "LargestContentful" in k or k in ("firstContentfulPaint", "largestContentfulPaint", "interactive", "speedIndex", "observedSpeedIndex", "totalBlockingTime")}, 900), "```", ""]
    for k in ("lcp-breakdown-insight", "lcp-discovery-insight", "render-blocking-insight", "network-dependency-tree-insight", "cls-culprits-insight", "image-delivery-insight", "font-display-insight", "unused-css-rules", "unused-javascript"):
        if k in a and a[k].get("details"):
            lines += [f"### {k}", "```", short(a[k]["details"], 1500), "```", ""]
    reqs = a.get("network-requests", {}).get("details", {}).get("items", [])
    reqs = sorted(reqs, key=lambda r: -(r.get("transferSize") or 0))[:10]
    lines += ["### 転送サイズ上位", "```"] + [f"{r.get('transferSize', 0):>9} {round((r.get('networkEndTime', 0) - r.get('networkRequestTime', 0)))}ms {r.get('url', '')[:110]}" for r in reqs] + ["```", ""]
os.makedirs("docs/marketing", exist_ok=True)
open("docs/marketing/lh-detail.md", "w", encoding="utf-8").write("\n".join(lines) + "\n")
