# サイト応答・速度の診断

## ill-inc.net

| URL | 初回 | 最終 | 転送数 | TTFB(s) | 合計(s) | 圧縮 | cache-control | Vercel cache |
|---|---|---|---|---|---|---|---|---|
| http://ill-inc.net/ | HTTP/1.0 308 Permanent Redirect → https://ill-inc.net/ | 200 https://www.ill-inc.net/ | 2 | 1.335019 | 1.335321 | - | - | - |
| https://ill-inc.net/ | HTTP/2 308  → https://www.ill-inc.net/ | 200 https://www.ill-inc.net/ | 1 | 0.357279 | 0.357372 | - | public, max-age=0, must-revalidate | - |
| http://www.ill-inc.net/ | HTTP/1.0 308 Permanent Redirect → https://www.ill-inc.net/ | 200 https://www.ill-inc.net/ | 1 | 0.215446 | 0.215552 | - | - | - |
| https://www.ill-inc.net/ | HTTP/2 200   | 200  | 0 | 0.087922 | 0.087996 | br | public, max-age=0, must-revalidate | HIT |
| https://www.ill-inc.net/column/ | HTTP/2 200   | 200  | 0 | 0.201390 | 0.202709 | br | public, max-age=0, must-revalidate | HIT |
| https://www.ill-inc.net/column/requirements-definition-tips | HTTP/2 200   | 200  | 0 | 0.221917 | 0.221978 | br | public, max-age=0, must-revalidate | HIT |
| https://www.ill-inc.net/column/requirements-definition-tips.html | HTTP/2 308  → /column/requirements-definition-tips | 200 https://www.ill-inc.net/column/requirements-definition-tips | 1 | 0.121851 | 0.121963 | - | public, max-age=0, must-revalidate | - |
| https://www.ill-inc.net/cases/ | HTTP/2 200   | 200  | 0 | 0.214135 | 0.214194 | br | public, max-age=0, must-revalidate | HIT |
| https://www.ill-inc.net/column/026-non-it-smb-system-development-no-engineer | HTTP/2 308  → /column/011-non-it-smb-system-development-no-engineer | 200 https://www.ill-inc.net/column/011-non-it-smb-system-development-no-engineer | 1 | 0.254855 | 0.254948 | - | public, max-age=0, must-revalidate | - |
| https://www.ill-inc.net/robots.txt | HTTP/2 200   | 200  | 0 | 0.170970 | 0.171027 | - | public, max-age=0, must-revalidate | HIT |
| https://www.ill-inc.net/sitemap.xml | HTTP/2 200   | 200  | 0 | 0.178597 | 0.178652 | br | public, max-age=0, must-revalidate | HIT |
| https://www.ill-inc.net/this-page-does-not-exist-xyz | HTTP/2 404   | 404  | 0 | 0.076153 | 0.076216 | - | public, max-age=0, must-revalidate | - |
| https://www.ill-inc.net/ill-homepage.zip | HTTP/2 404   | 404  | 0 | 0.137134 | 0.137197 | - | public, max-age=0, must-revalidate | - |

### PageSpeed Insights（モバイル）

- https://www.ill-inc.net/: {"error": "HTTP Error 429: Too Many Requests"}
- https://www.ill-inc.net/column/requirements-definition-tips: {"error": "HTTP Error 429: Too Many Requests"}

## re-en.jp

| URL | 初回 | 最終 | 転送数 | TTFB(s) | 合計(s) | 圧縮 | cache-control | Vercel cache |
|---|---|---|---|---|---|---|---|---|
| http://re-en.jp/ | HTTP/1.0 308 Permanent Redirect → https://re-en.jp/ | 200 https://re-en.jp/ | 1 | 2.029127 | 2.029252 | - | - | - |
| https://re-en.jp/ | HTTP/2 200   | 200  | 0 | 0.175398 | 0.175453 | br | public, max-age=0, must-revalidate | HIT |
| https://www.re-en.jp/ | HTTP/2 200   | 200  | 0 | 0.272175 | 0.272231 | br | public, max-age=0, must-revalidate | HIT |
| https://re-en.jp/column | HTTP/2 200   | 200  | 0 | 0.465786 | 0.465864 | br | public, max-age=0, must-revalidate | HIT |
| https://re-en.jp/column-detail-111 | HTTP/2 200   | 200  | 0 | 0.407016 | 0.407072 | br | public, max-age=0, must-revalidate | HIT |
| https://re-en.jp/column-detail-80.html | HTTP/2 308  → /column-detail-80 | 200 https://re-en.jp/column-detail-70 | 2 | 0.297779 | 0.297960 | - | public, max-age=0, must-revalidate | - |
| https://re-en.jp/pricing | HTTP/2 200   | 200  | 0 | 0.268936 | 0.268999 | br | public, max-age=0, must-revalidate | HIT |
| https://re-en.jp/robots.txt | HTTP/2 200   | 200  | 0 | 0.185909 | 0.185961 | - | public, max-age=0, must-revalidate | HIT |
| https://re-en.jp/sitemap.xml | HTTP/2 200   | 200  | 0 | 0.178096 | 0.178146 | br | public, max-age=0, must-revalidate | HIT |
| https://re-en.jp/this-page-does-not-exist-xyz | HTTP/2 404   | 404  | 0 | 0.338736 | 0.338790 | br | public, max-age=0, must-revalidate | HIT |
| https://re-en.jp/registrations.csv | HTTP/2 404   | 404  | 0 | 0.077593 | 0.077660 | br | public, max-age=0, must-revalidate | HIT |

### PageSpeed Insights（モバイル）

- https://re-en.jp/: {"error": "HTTP Error 429: Too Many Requests"}
- https://re-en.jp/column-detail-111: {"error": "HTTP Error 429: Too Many Requests"}

## tsuki-to-ren.com

| URL | 初回 | 最終 | 転送数 | TTFB(s) | 合計(s) | 圧縮 | cache-control | Vercel cache |
|---|---|---|---|---|---|---|---|---|
| http://tsuki-to-ren.com/ | HTTP/1.0 308 Permanent Redirect → https://tsuki-to-ren.com/ | 200 https://tsuki-to-ren.com/ | 1 | 0.729361 | 0.729686 | - | - | - |
| https://tsuki-to-ren.com/ | HTTP/2 200   | 200  | 0 | 0.219424 | 0.219483 | br | public, max-age=0, must-revalidate | HIT |
| https://www.tsuki-to-ren.com/ | HTTP/2 200   | 200  | 0 | 0.522829 | 0.522887 | br | public, max-age=0, must-revalidate | HIT |
| https://www.tsuki-to-ren.com/column/ | HTTP/2 200   | 200  | 0 | 0.256211 | 0.256264 | br | public, max-age=0, must-revalidate | HIT |
| https://www.tsuki-to-ren.com/column/kaigou-shichutsuimei-guide | HTTP/2 200   | 200  | 0 | 0.310735 | 0.310795 | br | public, max-age=0, must-revalidate | HIT |
| https://www.tsuki-to-ren.com/column/infp-entj-polar-attraction-chemistry | HTTP/2 308  → /column/infp-entj-contrast-relationship | 200 https://www.tsuki-to-ren.com/column/infp-entj-contrast-relationship | 1 | 0.204022 | 0.204123 | - | public, max-age=0, must-revalidate | - |
| https://www.tsuki-to-ren.com/compatibility | HTTP/2 200   | 200  | 0 | 0.243515 | 0.243572 | br | public, max-age=0, must-revalidate | HIT |
| https://www.tsuki-to-ren.com/robots.txt | HTTP/2 200   | 200  | 0 | 0.169381 | 0.169429 | - | public, max-age=0, must-revalidate | HIT |
| https://www.tsuki-to-ren.com/sitemap.xml | HTTP/2 200   | 200  | 0 | 0.247448 | 0.247503 | br | public, max-age=0, must-revalidate | HIT |
| https://www.tsuki-to-ren.com/this-page-does-not-exist-xyz | HTTP/2 200   | 200  | 0 | 0.241121 | 0.241175 | br | public, max-age=0, must-revalidate | HIT |

### PageSpeed Insights（モバイル）

- https://www.tsuki-to-ren.com/: {"error": "HTTP Error 429: Too Many Requests"}
- https://www.tsuki-to-ren.com/column/kaigou-shichutsuimei-guide: {"error": "HTTP Error 429: Too Many Requests"}

