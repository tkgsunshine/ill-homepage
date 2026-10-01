"""HTTP response + PageSpeed audit for the three sites. Writes docs/marketing/site-health.md.

Run on a GitHub Actions runner (it has outbound access). Uses curl for status / redirects / TTFB / headers
and the PageSpeed Insights API for mobile Core Web Vitals.
"""
import json
import os
import re
import subprocess
import time
import urllib.parse
import urllib.request

SITES = {
    "ill-inc.net": {
        "base": "https://www.ill-inc.net",
        "urls": [
            "http://ill-inc.net/", "https://ill-inc.net/", "http://www.ill-inc.net/", "https://www.ill-inc.net/",
            "https://www.ill-inc.net/column/", "https://www.ill-inc.net/column/requirements-definition-tips",
            "https://www.ill-inc.net/column/requirements-definition-tips.html", "https://www.ill-inc.net/cases/",
            "https://www.ill-inc.net/column/026-non-it-smb-system-development-no-engineer",
            "https://www.ill-inc.net/robots.txt", "https://www.ill-inc.net/sitemap.xml",
            "https://www.ill-inc.net/this-page-does-not-exist-xyz", "https://www.ill-inc.net/ill-homepage.zip",
        ],
        "psi": ["https://www.ill-inc.net/", "https://www.ill-inc.net/column/requirements-definition-tips"],
    },
    "re-en.jp": {
        "base": "https://re-en.jp",
        "urls": [
            "http://re-en.jp/", "https://re-en.jp/", "https://www.re-en.jp/", "https://re-en.jp/column",
            "https://re-en.jp/column-detail-111", "https://re-en.jp/column-detail-80.html", "https://re-en.jp/pricing",
            "https://re-en.jp/robots.txt", "https://re-en.jp/sitemap.xml",
            "https://re-en.jp/this-page-does-not-exist-xyz", "https://re-en.jp/registrations.csv",
        ],
        "psi": ["https://re-en.jp/", "https://re-en.jp/column-detail-111"],
    },
    "tsuki-to-ren.com": {
        "base": "https://www.tsuki-to-ren.com",
        "urls": [
            "http://tsuki-to-ren.com/", "https://tsuki-to-ren.com/", "https://www.tsuki-to-ren.com/",
            "https://www.tsuki-to-ren.com/column/", "https://www.tsuki-to-ren.com/column/kaigou-shichutsuimei-guide",
            "https://www.tsuki-to-ren.com/column/infp-entj-polar-attraction-chemistry",
            "https://www.tsuki-to-ren.com/compatibility", "https://www.tsuki-to-ren.com/robots.txt",
            "https://www.tsuki-to-ren.com/sitemap.xml", "https://www.tsuki-to-ren.com/this-page-does-not-exist-xyz",
        ],
        "psi": ["https://www.tsuki-to-ren.com/", "https://www.tsuki-to-ren.com/column/kaigou-shichutsuimei-guide"],
    },
}


def probe(url):
    fmt = "%{http_code}|%{num_redirects}|%{url_effective}|%{time_starttransfer}|%{time_total}|%{size_download}"
    out = subprocess.run(["curl", "-sL", "-o", "/dev/null", "-m", "30", "-H", "Accept-Encoding: gzip, br", "-A", "Mozilla/5.0 (compatible; SiteHealth)", "-w", fmt, url], capture_output=True, text=True).stdout
    first = subprocess.run(["curl", "-sI", "-m", "30", "-H", "Accept-Encoding: gzip, br", "-A", "Mozilla/5.0 (compatible; SiteHealth)", url], capture_output=True, text=True).stdout
    h = {}
    for ln in first.splitlines():
        if ":" in ln:
            k, v = ln.split(":", 1)
            h[k.strip().lower()] = v.strip()
    code, nred, eff, ttfb, tot, size = (out.split("|") + [""] * 6)[:6]
    return {"code": code, "redirects": nred, "final": eff, "ttfb": ttfb, "total": tot, "size": size,
            "first_status": first.splitlines()[0] if first else "", "loc": h.get("location", ""),
            "enc": h.get("content-encoding", "-"), "cache": h.get("cache-control", "-"), "vc": h.get("x-vercel-cache", "-"),
            "ctype": h.get("content-type", "-")}


def psi(url):
    import subprocess, tempfile
    out = tempfile.mktemp(suffix=".json")
    try:
        subprocess.run(["npx", "--yes", "lighthouse", url, "--quiet", "--output=json", "--output-path=" + out,
                        "--only-categories=performance,seo", "--form-factor=mobile",
                        "--chrome-flags=--headless=new --no-sandbox"], check=True, timeout=240,
                       stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
        lh = json.load(open(out))
    except Exception as e:
        return {"error": str(e)[:100]}
    a = lh["audits"]
    g = lambda k: a.get(k, {}).get("displayValue", "-")
    return {"perf": round(lh["categories"]["performance"]["score"] * 100), "seo": round(lh["categories"]["seo"]["score"] * 100),
            "LCP": g("largest-contentful-paint"), "CLS": g("cumulative-layout-shift"), "TBT": g("total-blocking-time"),
            "FCP": g("first-contentful-paint"), "TTFB": g("server-response-time"), "weight": g("total-byte-weight"),
            "failed": [k for k, v in a.items() if v.get("score") == 0 and v.get("scoreDisplayMode") in ("binary", "numeric")][:8]}


lines = ["# サイト応答・速度の診断", ""]
for name, cfg in SITES.items():
    lines += [f"## {name}", "", "| URL | 初回 | 最終 | 転送数 | TTFB(s) | 合計(s) | 圧縮 | cache-control | Vercel cache |", "|---|---|---|---|---|---|---|---|---|"]
    for u in cfg["urls"]:
        p = probe(u)
        lines.append(f"| {u} | {p['first_status']} {('→ ' + p['loc']) if p['loc'] else ''} | {p['code']} {p['final'] if p['final'] != u else ''} | {p['redirects']} | {p['ttfb']} | {p['total']} | {p['enc']} | {p['cache'][:40]} | {p['vc']} |")
    lines += ["", "### PageSpeed Insights（モバイル）", ""]
    for u in cfg["psi"]:
        r = psi(u)
        lines.append(f"- {u}: " + (json.dumps(r, ensure_ascii=False) if "error" in r else f"性能{r['perf']} / SEO{r['seo']} | LCP {r['LCP']} | CLS {r['CLS']} | TBT {r['TBT']} | FCP {r['FCP']} | サーバー応答 {r['TTFB']} | 転送量 {r['weight']} | 要改善: {', '.join(r['failed'])}"))
    lines.append("")
os.makedirs("docs/marketing", exist_ok=True)
open("docs/marketing/site-health.md", "w", encoding="utf-8").write("\n".join(lines) + "\n")
print("\n".join(lines))
