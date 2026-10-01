# サイト応答・速度の診断

## ill-inc.net

| URL | 初回 | 最終 | 転送数 | TTFB(s) | 合計(s) | 圧縮 | cache-control | Vercel cache |
|---|---|---|---|---|---|---|---|---|
| http://ill-inc.net/ | HTTP/1.0 308 Permanent Redirect → https://ill-inc.net/ | 200 https://www.ill-inc.net/ | 2 | 1.098572 | 1.098794 | - | - | - |
| https://ill-inc.net/ | HTTP/2 308  → https://www.ill-inc.net/ | 200 https://www.ill-inc.net/ | 1 | 0.639747 | 0.639866 | - | public, max-age=0, must-revalidate | - |
| http://www.ill-inc.net/ | HTTP/1.0 308 Permanent Redirect → https://www.ill-inc.net/ | 200 https://www.ill-inc.net/ | 1 | 0.286367 | 0.286570 | - | - | - |
| https://www.ill-inc.net/ | HTTP/2 200   | 200  | 0 | 0.186550 | 0.186612 | br | public, max-age=0, must-revalidate | HIT |
| https://www.ill-inc.net/column/ | HTTP/2 200   | 200  | 0 | 0.195095 | 0.217827 | br | public, max-age=0, must-revalidate | HIT |
| https://www.ill-inc.net/column/requirements-definition-tips | HTTP/2 200   | 200  | 0 | 0.247691 | 0.247757 | br | public, max-age=0, must-revalidate | HIT |
| https://www.ill-inc.net/column/requirements-definition-tips.html | HTTP/2 308  → /column/requirements-definition-tips | 200 https://www.ill-inc.net/column/requirements-definition-tips | 1 | 0.122348 | 0.122568 | - | public, max-age=0, must-revalidate | - |
| https://www.ill-inc.net/cases/ | HTTP/2 200   | 200  | 0 | 0.247400 | 0.247465 | br | public, max-age=0, must-revalidate | HIT |
| https://www.ill-inc.net/column/026-non-it-smb-system-development-no-engineer | HTTP/2 308  → /column/011-non-it-smb-system-development-no-engineer | 200 https://www.ill-inc.net/column/011-non-it-smb-system-development-no-engineer | 1 | 0.222964 | 0.223067 | - | public, max-age=0, must-revalidate | - |
| https://www.ill-inc.net/robots.txt | HTTP/2 200   | 200  | 0 | 0.200948 | 0.201003 | - | public, max-age=0, must-revalidate | HIT |
| https://www.ill-inc.net/sitemap.xml | HTTP/2 200   | 200  | 0 | 0.203999 | 0.204063 | br | public, max-age=0, must-revalidate | HIT |
| https://www.ill-inc.net/this-page-does-not-exist-xyz | HTTP/2 404   | 404  | 0 | 0.090702 | 0.090766 | - | public, max-age=0, must-revalidate | - |
| https://www.ill-inc.net/ill-homepage.zip | HTTP/2 404   | 404  | 0 | 0.091839 | 0.091881 | - | public, max-age=0, must-revalidate | - |

### PageSpeed Insights（モバイル）

- https://www.ill-inc.net/: 性能72 / SEO100 | LCP 6.8 s | CLS 0.009 | TBT 220 ms | FCP 1.6 s | サーバー応答 Root document took 20 ms | 転送量 Total size was 1,589 KiB | 要改善: network-dependency-tree-insight
- https://www.ill-inc.net/column/requirements-definition-tips: 性能97 / SEO100 | LCP 1.0 s | CLS 0.004 | TBT 200 ms | FCP 1.0 s | サーバー応答 Root document took 20 ms | 転送量 Total size was 1,018 KiB | 要改善: network-dependency-tree-insight

## re-en.jp

| URL | 初回 | 最終 | 転送数 | TTFB(s) | 合計(s) | 圧縮 | cache-control | Vercel cache |
|---|---|---|---|---|---|---|---|---|
| http://re-en.jp/ | HTTP/1.0 308 Permanent Redirect → https://re-en.jp/ | 200 https://re-en.jp/ | 1 | 0.585016 | 0.585153 | - | - | - |
| https://re-en.jp/ | HTTP/2 200   | 200  | 0 | 0.271696 | 0.271759 | br | public, max-age=0, must-revalidate | HIT |
| https://www.re-en.jp/ | HTTP/2 308  → https://re-en.jp/ | 200 https://re-en.jp/ | 1 | 0.382293 | 0.382399 | - | public, max-age=0, must-revalidate | - |
| https://re-en.jp/column | HTTP/2 200   | 200  | 0 | 0.221542 | 0.221607 | br | public, max-age=0, must-revalidate | HIT |
| https://re-en.jp/column-detail-111 | HTTP/2 200   | 200  | 0 | 0.260793 | 0.260856 | br | public, max-age=0, must-revalidate | HIT |
| https://re-en.jp/column-detail-80.html | HTTP/2 308  → /column-detail-80 | 200 https://re-en.jp/column-detail-70 | 2 | 0.293979 | 0.294129 | - | public, max-age=0, must-revalidate | - |
| https://re-en.jp/pricing | HTTP/2 200   | 200  | 0 | 0.222523 | 0.222590 | br | public, max-age=0, must-revalidate | HIT |
| https://re-en.jp/robots.txt | HTTP/2 200   | 200  | 0 | 0.304849 | 0.304913 | - | public, max-age=0, must-revalidate | HIT |
| https://re-en.jp/sitemap.xml | HTTP/2 200   | 200  | 0 | 0.254921 | 0.255013 | br | public, max-age=0, must-revalidate | HIT |
| https://re-en.jp/this-page-does-not-exist-xyz | HTTP/2 404   | 404  | 0 | 0.243269 | 0.243355 | br | public, max-age=0, must-revalidate | HIT |
| https://re-en.jp/registrations.csv | HTTP/2 404   | 404  | 0 | 0.145836 | 0.145887 | br | public, max-age=0, must-revalidate | HIT |

### PageSpeed Insights（モバイル）

- https://re-en.jp/: 性能55 / SEO100 | LCP 14.5 s | CLS 0.001 | TBT 0 ms | FCP 14.2 s | サーバー応答 Root document took 20 ms | 転送量 Total size was 1,744 KiB | 要改善: first-contentful-paint, largest-contentful-paint, forced-reflow-insight, network-dependency-tree-insight
- https://re-en.jp/column-detail-111: 性能76 / SEO100 | LCP 4.3 s | CLS 0.126 | TBT 260 ms | FCP 1.0 s | サーバー応答 Root document took 20 ms | 転送量 Total size was 1,453 KiB | 要改善: cls-culprits-insight, forced-reflow-insight, lcp-discovery-insight, network-dependency-tree-insight

## tsuki-to-ren.com

| URL | 初回 | 最終 | 転送数 | TTFB(s) | 合計(s) | 圧縮 | cache-control | Vercel cache |
|---|---|---|---|---|---|---|---|---|
| http://tsuki-to-ren.com/ | HTTP/1.0 308 Permanent Redirect → https://tsuki-to-ren.com/ | 200 https://www.tsuki-to-ren.com/ | 2 | 1.809558 | 1.809894 | - | - | - |
| https://tsuki-to-ren.com/ | HTTP/2 308  → https://www.tsuki-to-ren.com/ | 200 https://www.tsuki-to-ren.com/ | 1 | 0.268430 | 0.268766 | - | public, max-age=0, must-revalidate | - |
| https://www.tsuki-to-ren.com/ | HTTP/2 200   | 200  | 0 | 0.230906 | 0.230968 | br | public, max-age=0, must-revalidate | HIT |
| https://www.tsuki-to-ren.com/column/ | HTTP/2 200   | 200  | 0 | 0.187711 | 0.187768 | br | public, max-age=0, must-revalidate | HIT |
| https://www.tsuki-to-ren.com/column/kaigou-shichutsuimei-guide | HTTP/2 200   | 200  | 0 | 0.251292 | 0.251354 | br | public, max-age=0, must-revalidate | HIT |
| https://www.tsuki-to-ren.com/column/infp-entj-polar-attraction-chemistry | HTTP/2 308  → /column/infp-entj-contrast-relationship | 200 https://www.tsuki-to-ren.com/column/infp-entj-contrast-relationship | 1 | 0.219663 | 0.219764 | - | public, max-age=0, must-revalidate | - |
| https://www.tsuki-to-ren.com/compatibility | HTTP/2 200   | 200  | 0 | 0.333544 | 0.333606 | br | public, max-age=0, must-revalidate | HIT |
| https://www.tsuki-to-ren.com/robots.txt | HTTP/2 200   | 200  | 0 | 0.233720 | 0.233775 | - | public, max-age=0, must-revalidate | HIT |
| https://www.tsuki-to-ren.com/sitemap.xml | HTTP/2 200   | 200  | 0 | 0.186782 | 0.186841 | br | public, max-age=0, must-revalidate | HIT |
| https://www.tsuki-to-ren.com/this-page-does-not-exist-xyz | HTTP/2 404   | 404  | 0 | 0.243623 | 0.243684 | br | public, max-age=0, must-revalidate | HIT |

### PageSpeed Insights（モバイル）

- https://www.tsuki-to-ren.com/: 性能56 / SEO100 | LCP 12.3 s | CLS 0 | TBT 10 ms | FCP 11.0 s | サーバー応答 Root document took 30 ms | 転送量 Total size was 1,507 KiB | 要改善: first-contentful-paint, largest-contentful-paint, network-dependency-tree-insight
- https://www.tsuki-to-ren.com/column/kaigou-shichutsuimei-guide: 性能74 / SEO100 | LCP 10.6 s | CLS 0.002 | TBT 30 ms | FCP 1.6 s | サーバー応答 Root document took 30 ms | 転送量 Total size was 1,616 KiB | 要改善: largest-contentful-paint, forced-reflow-insight, lcp-discovery-insight, network-dependency-tree-insight

