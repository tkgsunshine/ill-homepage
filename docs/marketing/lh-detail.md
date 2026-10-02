# Lighthouse詳細（モバイル・3回の中央値）

## https://www.ill-inc.net/

- 3回のLCP(ms): 11258, 13081, 13190
- 性能 55 / FCP 11.9 s / LCP 13.1 s / CLS 0 / TBT 0 ms

### metrics(observed vs simulated)
```
{"firstContentfulPaint": 11949, "largestContentfulPaint": 13081, "interactive": 13195, "speedIndex": 11949, "totalBlockingTime": 0, "observedFirstContentfulPaint": 1331, "observedFirstContentfulPaintTs": 72405132, "observedFirstContentfulPaintAllFrames": 1331, "observedFirstContentfulPaintAllFramesTs": 72405132, "observedLargestContentfulPaint": 2363, "observedLargestContentfulPaintTs": 73436896, "observedLargestContentfulPaintAllFrames": 2363, "observedLargestContentfulPaintAllFramesTs": 73436896, "observedSpeedIndex": 1783}
```

### lcp-breakdown-insight
```
{"type": "list", "items": [{"type": "table", "headings": [{"key": "label", "valueType": "text", "label": "Subpart"}, {"key": "duration", "valueType": "ms", "label": "Duration"}], "items": [{"subpart": "timeToFirstByte", "label": "Time to first byte", "duration": 62.267}, {"subpart": "elementRenderDelay", "label": "Element render delay", "duration": 2300.685}]}, {"type": "node", "lhId": "page-0-H2", "path": "1,HTML,1,BODY,7,SECTION,0,DIV,1,DIV,1,H2", "selector": "section#concept > div.container > div.concept-right > h2#philosophy-title", "boundingRect": {"top": 691, "bottom": 780, "left": 11, "right": 401, "width": 390, "height": 89}, "snippet": "<h2 class=\"concept-quote\" id=\"philosophy-title\">", "nodeLabel": "ミニマル設計と生成AI活用で、\n素早くカタチにする。"}]}
```

### render-blocking-insight
```
{"type": "table", "headings": [{"key": "url", "valueType": "url", "label": "URL"}, {"key": "totalBytes", "valueType": "bytes", "label": "Transfer Size"}, {"key": "wastedMs", "valueType": "timespanMs", "label": "Duration"}], "items": [{"url": "https://www.ill-inc.net/style.css?v=61", "totalBytes": 18226}]}
```

### network-dependency-tree-insight
```
{"type": "list", "items": [{"type": "list-section", "value": {"type": "network-tree", "chains": {"CEDD2180D636E0388855B82195B6F3F3": {"url": "https://www.ill-inc.net/", "navStartToEndTime": 177, "transferSize": 21763, "isLongest": true, "children": {"2677.3": {"url": "https://www.ill-inc.net/style.css?v=61", "navStartToEndTime": 194, "transferSize": 18226, "isLongest": true, "children": {}}}}}, "longestChain": {"duration": 194}}}, {"type": "list-section", "title": "Preconnected origins", "description": "[preconnect](https://developer.chrome.com/docs/lighthouse/performance/uses-rel-preconnect/) hints help the browser establish a connection earlier in the page load, saving time when the first request for that origin is made. The following are the origins that the page preconnected to.", "value": {"type": "table", "headings": [{"key": "origin", "valueType": "text", "subItemsHeading": {"key": "warning"}, "label": "Origin"}, {"key": "source", "valueType": "node", "label": "Source"}], "items": [{"origin": "https://fonts.googleapis.com/", "source": {"type": "node", "lhId": "page-8-LINK", "path": "1,HTML,0,HEAD,32,LINK", "selector": "head > link", "boundingRect": {"top": 0, "bottom": 0, "left": 0, "right": 0, "width": 0, "height": 0}, "snippet": "<link rel=\"preconnect\" href=\"https://fonts.googleapis.com\">", "nodeLabel": "head > link"}, "subItems": {"type": "subitems", "items": []}}, {"origin": "https://fonts.gstatic.com/", "source": {"type": "node", "lhId": "page-9-LINK", "path":…
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
{"type": "opportunity", "headings": [{"key": "url", "valueType": "url", "label": "URL"}, {"key": "totalBytes", "valueType": "bytes", "label": "Transfer Size"}, {"key": "wastedBytes", "valueType": "bytes", "label": "Est Savings"}], "items": [{"url": "https://fonts.googleapis.com/css2?family=Noto+Sans+JP:wght@400;500;700&family=Outfit:wght@400;500;600;700;800&display=swap", "wastedBytes": 91316, "wastedPercent": 100, "totalBytes": 91316}, {"url": "https://www.ill-inc.net/style.css?v=61", "wastedBytes": 11335, "wastedPercent": 62.78611386448827, "totalBytes": 18053}], "overallSavingsMs": 460, "overallSavingsBytes": 102651, "sortedBy": ["wastedBytes"], "debugData": {"type": "debugdata", "metricSavings": {"FCP": 460, "LCP": 460}}}
```

### unused-javascript
```
{"type": "opportunity", "headings": [], "items": [], "overallSavingsMs": 0, "overallSavingsBytes": 0, "sortedBy": ["wastedBytes"], "debugData": {"type": "debugdata", "metricSavings": {"FCP": 0, "LCP": 0}}}
```

### 転送サイズ上位
```
   549056 95ms https://www.ill-inc.net/security-action.png
    91762 77ms https://fonts.googleapis.com/css2?family=Noto+Sans+JP:wght@400;500;700&family=Outfit:wght@400;500;600;700;800&
    78905 96ms https://fonts.gstatic.com/s/notosansjp/v57/-F62fjtqLzI2JPCgQBnw7HFowwII2lcnk-AFfrgQrvWXpdFg3KXxAMsKMbdN.119.wo
    75913 95ms https://fonts.gstatic.com/s/notosansjp/v57/-F62fjtqLzI2JPCgQBnw7HFowwII2lcnk-AFfrgQrvWXpdFg3KXxAMsKMbdN.13.wof
    32257 34ms https://fonts.gstatic.com/s/outfit/v15/QGYvz_MVcBeNP4NJtEtqUYLknw.woff2
    24677 36ms https://fonts.gstatic.com/s/notosansjp/v57/-F62fjtqLzI2JPCgQBnw7HFYwQgP-FVthw.woff2
    23889 105ms https://fonts.gstatic.com/s/notosansjp/v57/-F62fjtqLzI2JPCgQBnw7HFowwII2lcnk-AFfrgQrvWXpdFg3KXxAMsKMbdN.106.wo
    22911 93ms https://fonts.gstatic.com/s/notosansjp/v57/-F62fjtqLzI2JPCgQBnw7HFowwII2lcnk-AFfrgQrvWXpdFg3KXxAMsKMbdN.72.wof
    22909 63ms https://fonts.gstatic.com/s/notosansjp/v57/-F62fjtqLzI2JPCgQBnw7HFowwII2lcnk-AFfrgQrvWXpdFg3KXxAMsKMbdN.100.wo
    22332 99ms https://fonts.gstatic.com/s/notosansjp/v57/-F62fjtqLzI2JPCgQBnw7HFowwII2lcnk-AFfrgQrvWXpdFg3KXxAMsKMbdN.79.wof
```

