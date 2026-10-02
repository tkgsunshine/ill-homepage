# Lighthouse詳細（モバイル・3回の中央値）

## https://re-en.jp/

- 3回のLCP(ms): 2446, 2447, 15053
- 性能 88 / FCP 1.0 s / LCP 2.4 s / CLS 0.041 / TBT 390 ms

### lcp-breakdown-insight
```
{"type": "list", "items": [{"type": "table", "headings": [{"key": "label", "valueType": "text", "label": "Subpart"}, {"key": "duration", "valueType": "ms", "label": "Duration"}], "items": [{"subpart": "timeToFirstByte", "label": "Time to first byte", "duration": 82.4}, {"subpart": "resourceLoadDelay", "label": "Resource load delay", "duration": 17.21}, {"subpart": "resourceLoadDuration", "label": "Resource load duration", "duration": 57.191}, {"subpart": "elementRenderDelay", "label": "Element render delay", "duration": 129.909}]}, {"type": "node", "lhId": "page-0-SECTION", "path": "1,HTML,1,BODY,6,MAIN,1,SECTION", "selector": "body > main > section#hero", "boundingRect": {"top": 0, "bottom": 1084, "left": 0, "right": 412, "width": 412, "height": 1084}, "snippet": "<section id=\"hero\" class=\"hero hero--preregister\">", "nodeLabel": "2026年冬リリース予定\n創設メンバー（先着1,000名）\n優先インビテーション\n限定ウェイトリスト\n完全審査制\nハイクラス\n同じ立場だから、\n響きあう上質な…"}]}
```

### lcp-discovery-insight
```
{"type": "list", "items": [{"type": "checklist", "items": {"priorityHinted": {"label": "fetchpriority=high applied", "value": true}, "requestDiscoverable": {"label": "Request is discoverable in initial document", "value": true}, "eagerlyLoaded": {"label": "lazy load not applied", "value": true}}}, {"type": "node", "lhId": "page-0-SECTION", "path": "1,HTML,1,BODY,6,MAIN,1,SECTION", "selector": "body > main > section#hero", "boundingRect": {"top": 0, "bottom": 1084, "left": 0, "right": 412, "width": 412, "height": 1084}, "snippet": "<section id=\"hero\" class=\"hero hero--preregister\">", "nodeLabel": "2026年冬リリース予定\n創設メンバー（先着1,000名）\n優先インビテーション\n限定ウェイトリスト\n完全審査制\nハイクラス\n同じ立場だから、\n響きあう上質な…"}]}
```

### render-blocking-insight
```
{"type": "table", "headings": [{"key": "url", "valueType": "url", "label": "URL"}, {"key": "totalBytes", "valueType": "bytes", "label": "Transfer Size"}, {"key": "wastedMs", "valueType": "timespanMs", "label": "Duration"}], "items": [{"url": "https://re-en.jp/index.css?v=1.80", "totalBytes": 16422, "wastedMs": 173}]}
```

### network-dependency-tree-insight
```
{"type": "list", "items": [{"type": "list-section", "value": {"type": "network-tree", "chains": {"2E212ACA4936FF48257A52904A982D80": {"url": "https://re-en.jp/", "navStartToEndTime": 105, "transferSize": 11892, "isLongest": true, "children": {"2919.4": {"url": "https://re-en.jp/index.css?v=1.80", "navStartToEndTime": 160, "transferSize": 16422, "isLongest": true, "children": {}}}}}, "longestChain": {"duration": 160}}}, {"type": "list-section", "title": "Preconnected origins", "description": "[preconnect](https://developer.chrome.com/docs/lighthouse/performance/uses-rel-preconnect/) hints help the browser establish a connection earlier in the page load, saving time when the first request for that origin is made. The following are the origins that the page preconnected to.", "value": {"type": "table", "headings": [{"key": "origin", "valueType": "text", "subItemsHeading": {"key": "warning"}, "label": "Origin"}, {"key": "source", "valueType": "node", "label": "Source"}], "items": [{"origin": "https://fonts.googleapis.com/", "source": {"type": "node", "lhId": "page-47-LINK", "path": "1,HTML,0,HEAD,27,LINK", "selector": "head > link", "boundingRect": {"top": 0, "bottom": 0, "left": 0, "right": 0, "width": 0, "height": 0}, "snippet": "<link rel=\"preconnect\" href=\"https://fonts.googleapis.com\">", "nodeLabel": "head > link"}, "subItems": {"type": "subitems", "items": []}}, {"origin": "https://fonts.gstatic.com/", "source": {"type": "node", "lhId": "page-48-LINK", "path": "1,HTML,0…
```

### cls-culprits-insight
```
{"type": "list", "items": [{"type": "table", "headings": [{"key": "node", "valueType": "node", "subItemsHeading": {"key": "extra"}, "label": "Element"}, {"key": "score", "valueType": "numeric", "subItemsHeading": {"key": "cause", "valueType": "text"}, "granularity": 0.001, "label": "Layout shift score"}], "items": [{"node": {"type": "text", "value": "Total"}, "score": 0.040686071111780645}, {"node": {"type": "node", "lhId": "page-6-DIV", "path": "1,HTML,1,BODY,6,MAIN,1,SECTION,0,DIV,0,DIV,6,DIV,0,DIV", "selector": "div.container > div.hero__content > div.privilege__wrapper > div.privilege-card", "boundingRect": {"top": 421, "bottom": 878, "left": 40, "right": 372, "width": 332, "height": 458}, "snippet": "<div class=\"privilege-card reveal reveal--visible\" style=\"padding: 36px 32px;\">", "nodeLabel": "先着1,000名様限定\n有料サブスクリプション\n【2ヶ月間】完全無料提供\n\n厳正な審査を通過した創設メンバーは、本リリース後2ヶ月間、マッチング、メッセージ送…"}, "score": 0.03609460281529231}, {"node": {"type": "node", "lhId": "page-1-H1", "path": "1,HTML,1,BODY,6,MAIN,1,SECTION,0,DIV,0,DIV,2,H1", "selector": "section#hero > div.container > div.hero__content > h1.hero__headline", "boundingRect": {"top": 218, "bottom": 270, "left": 102, "right": 310, "width": 207, "height": 52}, "snippet": "<h1 class=\"hero__headline\">", "nodeLabel": "同じ立場だから、\n響きあう上質な関係。"}, "score": 0.003995202116771865, "subItems": {"type": "subitems", "items": [{"extra": {"type": "url", "value": "https://fonts.gstatic.com/s/notoserifjp/v34/xn7mYHs72GKoTvER4Gn3b5eMbNmuY2Q3X88.woff…
```

### image-delivery-insight
```
{"type": "table", "headings": [{"key": "url", "valueType": "url", "label": "URL", "subItemsHeading": {"key": "reason", "valueType": "text"}}, {"key": "totalBytes", "valueType": "bytes", "label": "Resource Size"}, {"key": "wastedBytes", "valueType": "bytes", "label": "Est Savings", "subItemsHeading": {"key": "wastedBytes", "valueType": "bytes"}}], "items": [], "debugData": {"type": "debugdata", "wastedBytes": 0}}
```

### font-display-insight
```
{"type": "table", "headings": [{"key": "url", "valueType": "url", "label": "URL"}, {"key": "wastedMs", "valueType": "ms", "label": "Est Savings"}], "items": []}
```

### unused-css-rules
```
{"type": "opportunity", "headings": [{"key": "url", "valueType": "url", "label": "URL"}, {"key": "totalBytes", "valueType": "bytes", "label": "Transfer Size"}, {"key": "wastedBytes", "valueType": "bytes", "label": "Est Savings"}], "items": [{"url": "https://fonts.googleapis.com/css2?family=Noto+Sans+JP:wght@400;700&family=Noto+Serif+JP:wght@500;700&family=Oswald:wght@500;700&display=swap", "wastedBytes": 121765, "wastedPercent": 100, "totalBytes": 121765}], "overallSavingsMs": 560, "overallSavingsBytes": 121765, "sortedBy": ["wastedBytes"], "debugData": {"type": "debugdata", "metricSavings": {"FCP": 0, "LCP": 560}}}
```

### unused-javascript
```
{"type": "opportunity", "headings": [], "items": [], "overallSavingsMs": 0, "overallSavingsBytes": 0, "sortedBy": ["wastedBytes"], "debugData": {"type": "debugdata", "metricSavings": {"FCP": 0, "LCP": 0}}}
```

### 転送サイズ上位
```
   122211 117ms https://fonts.googleapis.com/css2?family=Noto+Sans+JP:wght@400;700&family=Noto+Serif+JP:wght@500;700&family=Os
   109990 141ms https://fonts.gstatic.com/s/notoserifjp/v34/xn7mYHs72GKoTvER4Gn3b5eMXNukZEY1FdvPydaYCaeub8TUnmzwwRURhX8K-w.119
    78905 125ms https://fonts.gstatic.com/s/notosansjp/v57/-F62fjtqLzI2JPCgQBnw7HFowwII2lcnk-AFfrgQrvWXpdFg3KXxAMsKMbdN.119.wo
    71088 105ms https://fonts.gstatic.com/s/notosansjp/v57/-F62fjtqLzI2JPCgQBnw7HFowwII2lcnk-AFfrgQrvWXpdFg3KXxAMsKMbdN.16.wof
    39725 54ms https://re-en.jp/images/hero_lifestyle.webp
    33420 51ms https://fonts.gstatic.com/s/notoserifjp/v34/xn7mYHs72GKoTvER4Gn3b5eMbNmuY2Q3X88.woff2
    33138 54ms https://re-en.jp/images/hero_lifestyle_mobile.webp
    31684 111ms https://fonts.gstatic.com/s/notoserifjp/v34/xn7mYHs72GKoTvER4Gn3b5eMXNukZEY1FdvPydaYCaeub8TUnmzwwRURhX8K-w.106
    31309 74ms https://fonts.gstatic.com/s/notoserifjp/v34/xn7mYHs72GKoTvER4Gn3b5eMXNukZEY1FdvPydaYCaeub8TUnmzwwRURhX8K-w.100
    30925 100ms https://fonts.gstatic.com/s/notoserifjp/v34/xn7mYHs72GKoTvER4Gn3b5eMXNukZEY1FdvPydaYCaeub8TUnmzwwRURhX8K-w.99.
```

## https://www.tsuki-to-ren.com/

- 3回のLCP(ms): 1715, 4654, 5041
- 性能 74 / FCP 4.0 s / LCP 4.7 s / CLS 0.013 / TBT 30 ms

### lcp-breakdown-insight
```
{"type": "list", "items": [{"type": "table", "headings": [{"key": "label", "valueType": "text", "label": "Subpart"}, {"key": "duration", "valueType": "ms", "label": "Duration"}], "items": [{"subpart": "timeToFirstByte", "label": "Time to first byte", "duration": 84.464}, {"subpart": "elementRenderDelay", "label": "Element render delay", "duration": 166.594}]}, {"type": "node", "lhId": "page-2-P", "path": "0,HEADER,2,P", "selector": "div > header > p", "boundingRect": {"top": 0, "bottom": 0, "left": 0, "right": 0, "width": 0, "height": 0}, "snippet": "<p style=\"font-size: 0.9rem; color: rgb(203, 213, 225); line-height: 1.6; max-width: 580px;\">", "nodeLabel": "\n        東洋最高峰の四柱推命・九星気学と西洋の16タイプ（MBTI）心理統計学を融合した完全無料の本格恋愛占い『月と蓮』。片思い・復縁・好きな人との…"}]}
```

### render-blocking-insight
```
{"type": "table", "headings": [{"key": "url", "valueType": "url", "label": "URL"}, {"key": "totalBytes", "valueType": "bytes", "label": "Transfer Size"}, {"key": "wastedMs", "valueType": "timespanMs", "label": "Duration"}], "items": [{"url": "https://www.tsuki-to-ren.com/assets/index-DBWJIcbu.css", "totalBytes": 5246}]}
```

### network-dependency-tree-insight
```
{"type": "list", "items": [{"type": "list-section", "value": {"type": "network-tree", "chains": {"F7B5FD2D131FD11B8AFFC09DFC811A20": {"url": "https://www.tsuki-to-ren.com/", "navStartToEndTime": 105, "transferSize": 5543, "isLongest": true, "children": {"3301.543": {"url": "https://www.tsuki-to-ren.com/__/auth/iframe.js", "navStartToEndTime": 1694, "transferSize": 94814, "isLongest": true, "children": {"3301.545": {"url": "https://www.googleapis.com/identitytoolkit/v3/relyingparty/getProjectConfig?key=AIzaSyC8KuxFTkHR_3nLX7h8b-L_G40n59ymyY8&cb=1790924258295", "navStartToEndTime": 1889, "transferSize": 410, "isLongest": true, "children": {}}}}, "3301.7": {"url": "https://www.tsuki-to-ren.com/assets/index-CKAVm4PL.js", "navStartToEndTime": 275, "transferSize": 194733, "children": {}}, "3301.25": {"url": "https://www.tsuki-to-ren.com/site.webmanifest", "navStartToEndTime": 252, "transferSize": 743, "children": {}}, "3301.12": {"url": "https://www.tsuki-to-ren.com/assets/index-DBWJIcbu.css", "navStartToEndTime": 191, "transferSize": 5246, "children": {}}}}}, "longestChain": {"duration": 1889}}}, {"type": "list-section", "title": "Preconnected origins", "description": "[preconnect](https://developer.chrome.com/docs/lighthouse/performance/uses-rel-preconnect/) hints help the browser establish a connection earlier in the page load, saving time when the first request for that origin is made. The following are the origins that the page preconnected to.", "value": {"type": "table", "he…
```

### cls-culprits-insight
```
{"type": "list", "items": [{"type": "table", "headings": [{"key": "node", "valueType": "node", "subItemsHeading": {"key": "extra"}, "label": "Element"}, {"key": "score", "valueType": "numeric", "subItemsHeading": {"key": "cause", "valueType": "text"}, "granularity": 0.001, "label": "Layout shift score"}], "items": [{"node": {"type": "text", "value": "Total"}, "score": 0.01284693545049388}, {"node": {"type": "node", "lhId": "page-3-DIV", "path": "1,HTML,1,BODY,0,DIV,0,DIV,1,MAIN,0,DIV,0,HEADER,3,DIV", "selector": "main.main-content > div.home-input-flow > header.app-header > div", "boundingRect": {"top": 176, "bottom": 282, "left": 28, "right": 384, "width": 356, "height": 105}, "snippet": "<div style=\"margin: 1rem auto 0px; padding: 1.1rem;\">", "nodeLabel": "東洋の命式と西洋の心理統計が導く\n全273,088,320通り（約2.7億通り）の運命マトリクス\n二人の魂の相性・運気のバイオリズム・LINE攻略法を徹底鑑定…"}, "score": 0.01284693545049388, "subItems": {"type": "subitems", "items": [{"extra": {"type": "url", "value": "https://fonts.gstatic.com/s/shipporimincho/v17/VdGDAZweH5EbgHY6YExcZfDoj0B4Z9Cm4ZEI5-7s2xZbIDLfwlghWkaUqSYfzWdYeCMQ.118.woff2"}, "cause": "Web font"}, {"extra": {"type": "url", "value": "https://fonts.gstatic.com/s/shipporimincho/v17/VdGDAZweH5EbgHY6YExcZfDoj0B4L9am4ZEI5-7s2xZbIDLfwlghWkaUqSYfzWdYeCMQ.118.woff2"}, "cause": "Web font"}, {"extra": {"type": "url", "value": "https://fonts.gstatic.com/s/shipporimincho/v17/VdGDAZweH5EbgHY6YExcZfDoj0B4Z9Cm4ZEI5-7s2xZbIDLfwlghWkaUqSYfzWdYeCMQ.119.woff2"}, "cause": "Web font"}, {"extra":…
```

### image-delivery-insight
```
{"type": "table", "headings": [{"key": "url", "valueType": "url", "label": "URL", "subItemsHeading": {"key": "reason", "valueType": "text"}}, {"key": "totalBytes", "valueType": "bytes", "label": "Resource Size"}, {"key": "wastedBytes", "valueType": "bytes", "label": "Est Savings", "subItemsHeading": {"key": "wastedBytes", "valueType": "bytes"}}], "items": [{"url": "https://www.tsuki-to-ren.com/assets/tsuki.webp", "totalBytes": 60854, "wastedBytes": 54787, "subItems": {"type": "subitems", "items": [{"reason": "Increasing the image compression factor could improve this image's download size.", "wastedBytes": 25187}, {"reason": "This image file is larger than it needs to be (400x535) for its displayed dimensions (165x221). Use responsive images to reduce the image download size.", "wastedBytes": 50503}]}}, {"url": "https://www.tsuki-to-ren.com/assets/ren.webp", "totalBytes": 46740, "wastedBytes": 40449, "subItems": {"type": "subitems", "items": [{"reason": "Increasing the image compression factor could improve this image's download size.", "wastedBytes": 11073}, {"reason": "This image file is larger than it needs to be (400x535) for its displayed dimensions (168x225). Use responsive images to reduce the image download size.", "wastedBytes": 38496}]}}], "debugData": {"type": "debugdata", "wastedBytes": 95236}}
```

### font-display-insight
```
{"type": "table", "headings": [{"key": "url", "valueType": "url", "label": "URL"}, {"key": "wastedMs", "valueType": "ms", "label": "Est Savings"}], "items": []}
```

### unused-css-rules
```
{"type": "opportunity", "headings": [{"key": "url", "valueType": "url", "label": "URL"}, {"key": "totalBytes", "valueType": "bytes", "label": "Transfer Size"}, {"key": "wastedBytes", "valueType": "bytes", "label": "Est Savings"}], "items": [{"url": "https://fonts.googleapis.com/css2?family=Noto+Serif+JP:wght@400;700&family=Shippori+Mincho:wght@500;700&family=Inter:wght@400;600&display=swap", "wastedBytes": 121904, "wastedPercent": 100, "totalBytes": 121904}], "overallSavingsMs": 690, "overallSavingsBytes": 121904, "sortedBy": ["wastedBytes"], "debugData": {"type": "debugdata", "metricSavings": {"FCP": 520, "LCP": 690}}}
```

### unused-javascript
```
{"type": "opportunity", "headings": [{"key": "url", "valueType": "url", "subItemsHeading": {"key": "source", "valueType": "code"}, "label": "URL"}, {"key": "totalBytes", "valueType": "bytes", "subItemsHeading": {"key": "sourceBytes"}, "label": "Transfer Size"}, {"key": "wastedBytes", "valueType": "bytes", "subItemsHeading": {"key": "sourceWastedBytes"}, "label": "Est Savings"}], "items": [{"url": "https://www.tsuki-to-ren.com/assets/vendor-firebase-BFt_6Eht.js", "totalBytes": 106190, "wastedBytes": 88042, "wastedPercent": 82.90964674296222}, {"url": "https://accounts.google.com/gsi/client", "totalBytes": 101436, "wastedBytes": 84768, "wastedPercent": 83.56767726730484}, {"url": "https://www.tsuki-to-ren.com/assets/index-CKAVm4PL.js", "totalBytes": 130499, "wastedBytes": 73265, "wastedPercent": 56.142579247172385}, {"url": "https://www.tsuki-to-ren.com/assets/vendor-core-ISfjsLyJ.js", "totalBytes": 105953, "wastedBytes": 72445, "wastedPercent": 68.37434796678453}, {"url": "https://www.tsuki-to-ren.com/__/auth/iframe.js", "totalBytes": 94689, "wastedBytes": 58179, "wastedPercent": 61.44265068343565}], "overallSavingsMs": 1210, "overallSavingsBytes": 376699, "sortedBy": ["wastedBytes"], "debugData": {"type": "debugdata", "metricSavings": {"FCP": 1170, "LCP": 1210}}}
```

### 転送サイズ上位
```
   194733 134ms https://www.tsuki-to-ren.com/assets/index-CKAVm4PL.js
   122350 129ms https://fonts.googleapis.com/css2?family=Noto+Serif+JP:wght@400;700&family=Shippori+Mincho:wght@500;700&family
   106306 125ms https://www.tsuki-to-ren.com/assets/vendor-firebase-BFt_6Eht.js
   106067 105ms https://www.tsuki-to-ren.com/assets/vendor-core-ISfjsLyJ.js
   102211 221ms https://accounts.google.com/gsi/client
    94814 67ms https://www.tsuki-to-ren.com/__/auth/iframe.js
    78156 29ms https://www.tsuki-to-ren.com/assets/bg-stars.webp
    61033 67ms https://www.tsuki-to-ren.com/assets/tsuki.webp
    50155 29ms https://www.tsuki-to-ren.com/icon-192.png
    48464 87ms https://fonts.gstatic.com/s/inter/v20/UcC73FwrK3iLTeHuS_nVMrMxCp50SjIa1ZL7W0Q5nw.woff2
```

## https://www.ill-inc.net/

- 3回のLCP(ms): 11389, 13232, 13268
- 性能 55 / FCP 12.0 s / LCP 13.2 s / CLS 0 / TBT 0 ms

### lcp-breakdown-insight
```
{"type": "list", "items": [{"type": "table", "headings": [{"key": "label", "valueType": "text", "label": "Subpart"}, {"key": "duration", "valueType": "ms", "label": "Duration"}], "items": [{"subpart": "timeToFirstByte", "label": "Time to first byte", "duration": 87.125}, {"subpart": "elementRenderDelay", "label": "Element render delay", "duration": 2226.359}]}, {"type": "node", "lhId": "page-0-H2", "path": "1,HTML,1,BODY,7,SECTION,0,DIV,1,DIV,1,H2", "selector": "section#concept > div.container > div.concept-right > h2#philosophy-title", "boundingRect": {"top": 691, "bottom": 780, "left": 11, "right": 401, "width": 390, "height": 89}, "snippet": "<h2 class=\"concept-quote\" id=\"philosophy-title\">", "nodeLabel": "ミニマル設計と生成AI活用で、\n素早くカタチにする。"}]}
```

### render-blocking-insight
```
{"type": "table", "headings": [{"key": "url", "valueType": "url", "label": "URL"}, {"key": "totalBytes", "valueType": "bytes", "label": "Transfer Size"}, {"key": "wastedMs", "valueType": "timespanMs", "label": "Duration"}], "items": [{"url": "https://www.ill-inc.net/style.css?v=61", "totalBytes": 18204}]}
```

### network-dependency-tree-insight
```
{"type": "list", "items": [{"type": "list-section", "value": {"type": "network-tree", "chains": {"2E32D03F70DAABFF8ED1AE8092C96917": {"url": "https://www.ill-inc.net/", "navStartToEndTime": 113, "transferSize": 21763, "isLongest": true, "children": {"4056.3": {"url": "https://www.ill-inc.net/style.css?v=61", "navStartToEndTime": 145, "transferSize": 18204, "isLongest": true, "children": {}}}}}, "longestChain": {"duration": 145}}}, {"type": "list-section", "title": "Preconnected origins", "description": "[preconnect](https://developer.chrome.com/docs/lighthouse/performance/uses-rel-preconnect/) hints help the browser establish a connection earlier in the page load, saving time when the first request for that origin is made. The following are the origins that the page preconnected to.", "value": {"type": "table", "headings": [{"key": "origin", "valueType": "text", "subItemsHeading": {"key": "warning"}, "label": "Origin"}, {"key": "source", "valueType": "node", "label": "Source"}], "items": [{"origin": "https://fonts.googleapis.com/", "source": {"type": "node", "lhId": "page-8-LINK", "path": "1,HTML,0,HEAD,32,LINK", "selector": "head > link", "boundingRect": {"top": 0, "bottom": 0, "left": 0, "right": 0, "width": 0, "height": 0}, "snippet": "<link rel=\"preconnect\" href=\"https://fonts.googleapis.com\">", "nodeLabel": "head > link"}, "subItems": {"type": "subitems", "items": []}}, {"origin": "https://fonts.gstatic.com/", "source": {"type": "node", "lhId": "page-9-LINK", "path":…
```

### cls-culprits-insight
```
{"type": "list", "items": []}
```

### image-delivery-insight
```
{"type": "table", "headings": [{"key": "url", "valueType": "url", "label": "URL", "subItemsHeading": {"key": "reason", "valueType": "text"}}, {"key": "totalBytes", "valueType": "bytes", "label": "Resource Size"}, {"key": "wastedBytes", "valueType": "bytes", "label": "Est Savings", "subItemsHeading": {"key": "wastedBytes", "valueType": "bytes"}}], "items": [], "debugData": {"type": "debugdata", "wastedBytes": 0}}
```

### font-display-insight
```
{"type": "table", "headings": [{"key": "url", "valueType": "url", "label": "URL"}, {"key": "wastedMs", "valueType": "ms", "label": "Est Savings"}], "items": []}
```

### unused-css-rules
```
{"type": "opportunity", "headings": [{"key": "url", "valueType": "url", "label": "URL"}, {"key": "totalBytes", "valueType": "bytes", "label": "Transfer Size"}, {"key": "wastedBytes", "valueType": "bytes", "label": "Est Savings"}], "items": [{"url": "https://fonts.googleapis.com/css2?family=Noto+Sans+JP:wght@400;500;700&family=Outfit:wght@400;500;600;700;800&display=swap", "wastedBytes": 91316, "wastedPercent": 100, "totalBytes": 91316}, {"url": "https://www.ill-inc.net/style.css?v=61", "wastedBytes": 11335, "wastedPercent": 62.78611386448827, "totalBytes": 18053}], "overallSavingsMs": 490, "overallSavingsBytes": 102651, "sortedBy": ["wastedBytes"], "debugData": {"type": "debugdata", "metricSavings": {"FCP": 490, "LCP": 490}}}
```

### unused-javascript
```
{"type": "opportunity", "headings": [], "items": [], "overallSavingsMs": 0, "overallSavingsBytes": 0, "sortedBy": ["wastedBytes"], "debugData": {"type": "debugdata", "metricSavings": {"FCP": 0, "LCP": 0}}}
```

### 転送サイズ上位
```
   549029 127ms https://www.ill-inc.net/security-action.png
    91762 112ms https://fonts.googleapis.com/css2?family=Noto+Sans+JP:wght@400;500;700&family=Outfit:wght@400;500;600;700;800&
    78905 123ms https://fonts.gstatic.com/s/notosansjp/v57/-F62fjtqLzI2JPCgQBnw7HFowwII2lcnk-AFfrgQrvWXpdFg3KXxAMsKMbdN.119.wo
    75916 108ms https://fonts.gstatic.com/s/notosansjp/v57/-F62fjtqLzI2JPCgQBnw7HFowwII2lcnk-AFfrgQrvWXpdFg3KXxAMsKMbdN.13.wof
    32257 34ms https://fonts.gstatic.com/s/outfit/v15/QGYvz_MVcBeNP4NJtEtqUYLknw.woff2
    24677 40ms https://fonts.gstatic.com/s/notosansjp/v57/-F62fjtqLzI2JPCgQBnw7HFYwQgP-FVthw.woff2
    23889 111ms https://fonts.gstatic.com/s/notosansjp/v57/-F62fjtqLzI2JPCgQBnw7HFowwII2lcnk-AFfrgQrvWXpdFg3KXxAMsKMbdN.106.wo
    22912 95ms https://fonts.gstatic.com/s/notosansjp/v57/-F62fjtqLzI2JPCgQBnw7HFowwII2lcnk-AFfrgQrvWXpdFg3KXxAMsKMbdN.72.wof
    22909 67ms https://fonts.gstatic.com/s/notosansjp/v57/-F62fjtqLzI2JPCgQBnw7HFowwII2lcnk-AFfrgQrvWXpdFg3KXxAMsKMbdN.100.wo
    22333 107ms https://fonts.gstatic.com/s/notosansjp/v57/-F62fjtqLzI2JPCgQBnw7HFowwII2lcnk-AFfrgQrvWXpdFg3KXxAMsKMbdN.79.wof
```

