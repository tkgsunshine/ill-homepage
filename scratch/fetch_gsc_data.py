import json
import datetime
from google.oauth2 import service_account
from googleapiclient.discovery import build

creds = service_account.Credentials.from_service_account_file(
    "gsc-credentials.json",
    scopes=["https://www.googleapis.com/auth/webmasters.readonly"]
)
service = build("searchconsole", "v1", credentials=creds)

sites = service.sites().list().execute()
site_urls = [s["siteUrl"] for s in sites.get("siteEntry", [])]
print(f"Registered Sites in GSC: {site_urls}")

for site_url in site_urls:
    print(f"\n==========================================")
    print(f"📊 Site Performance: {site_url}")
    print(f"==========================================")
    today = datetime.date.today()
    start_date = (today - datetime.timedelta(days=28)).strftime("%Y-%m-%d")
    end_date = today.strftime("%Y-%m-%d")
    
    # 1. Total overview by date
    try:
        daily_req = {
            "startDate": start_date,
            "endDate": end_date,
            "dimensions": ["date"]
        }
        daily_resp = service.searchanalytics().query(siteUrl=site_url, body=daily_req).execute()
        daily_rows = daily_resp.get("rows", [])
        total_clicks = sum(r["clicks"] for r in daily_rows)
        total_impressions = sum(r["impressions"] for r in daily_rows)
        avg_ctr = (total_clicks / total_impressions * 100) if total_impressions > 0 else 0
        avg_pos = (sum(r.get("position", 0) * r["impressions"] for r in daily_rows) / total_impressions) if total_impressions > 0 else 0
        
        print(f"📅 Period: {start_date} ~ {end_date} (Last 28 Days)")
        print(f"🖱️ Total Clicks: {total_clicks}")
        print(f"👁️ Total Impressions (表示回数): {total_impressions}")
        print(f"📈 Average CTR (クリック率): {avg_ctr:.2f}%")
        print(f"🎯 Average Position (平均掲載順位): {avg_pos:.1f}")
        
        print("\n📈 Recent Daily Trend (Last 14 Days):")
        for r in daily_rows[-14:]:
            dt = r["keys"][0]
            c = r["clicks"]
            imp = r["impressions"]
            pos = r.get("position", 0)
            print(f"  [{dt}] Clicks: {c:2d} | Impressions: {imp:4d} | Avg Pos: {pos:5.1f}")
    except Exception as e:
        print(f"Error fetching daily metrics: {e}")

    # 2. Top Queries
    try:
        query_req = {
            "startDate": start_date,
            "endDate": end_date,
            "dimensions": ["query"],
            "rowLimit": 25
        }
        query_resp = service.searchanalytics().query(siteUrl=site_url, body=query_req).execute()
        query_rows = query_resp.get("rows", [])
        print(f"\n🔍 Top Search Queries ({len(query_rows)} found):")
        for r in query_rows:
            q = r["keys"][0]
            c = r["clicks"]
            imp = r["impressions"]
            ctr = r["ctr"] * 100
            pos = r["position"]
            print(f"  • \"{q}\" -> Clicks: {c}, Imp: {imp}, CTR: {ctr:.1f}%, Pos: {pos:.1f}")
    except Exception as e:
        print(f"Error fetching queries: {e}")

    # 3. Top Pages
    try:
        page_req = {
            "startDate": start_date,
            "endDate": end_date,
            "dimensions": ["page"],
            "rowLimit": 20
        }
        page_resp = service.searchanalytics().query(siteUrl=site_url, body=page_req).execute()
        page_rows = page_resp.get("rows", [])
        print(f"\n📄 Top Performing Pages ({len(page_rows)} found):")
        for r in page_rows:
            p = r["keys"][0]
            c = r["clicks"]
            imp = r["impressions"]
            pos = r["position"]
            print(f"  • {p} -> Clicks: {c}, Imp: {imp}, Pos: {pos:.1f}")
    except Exception as e:
        print(f"Error fetching pages: {e}")

    # 4. Sitemaps info
    try:
        sitemaps_resp = service.sitemaps().list(siteUrl=site_url).execute()
        sitemaps = sitemaps_resp.get("sitemap", [])
        print(f"\n🗺️ Submitted Sitemaps ({len(sitemaps)} found):")
        for sm in sitemaps:
            path = sm.get("path")
            last_sub = sm.get("lastSubmitted")
            last_dl = sm.get("lastDownloaded")
            has_err = sm.get("hasErrors", False)
            warns = sm.get("warnings", 0)
            errs = sm.get("errors", 0)
            print(f"  • Path: {path} | Submitted: {last_sub} | Downloaded: {last_dl} | Errors: {errs} | Warnings: {warns}")
            for content in sm.get("contents", []):
                ctype = content.get("type")
                submitted_cnt = content.get("submitted")
                indexed_cnt = content.get("indexed")
                print(f"    - Type: {ctype} | Submitted: {submitted_cnt} | Indexed: {indexed_cnt}")
    except Exception as e:
        print(f"Error fetching sitemaps: {e}")
