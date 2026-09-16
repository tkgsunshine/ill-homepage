import os
import re

COLUMN_DIR = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), "column")

BOTTOM_CTA_HTML = """          <!-- Eye-catching Bottom CTA Banner -->
          <div class="article-bottom-cta">
            <div class="cta-badge">
              <span class="badge-dot"></span>無料相談・相見積もり歓迎
            </div>
            <h3 class="cta-title">システム開発・AI導入の無料相談・概算見積もり</h3>
            <p class="cta-desc">
              不要な機能を削ぎ落とす「ミニマル設計」で、高品質な開発を適正価格で実現します。
            </p>
            <div class="cta-check-pills">
              <span class="cta-check-pill">
                <svg class="check-icon" width="16" height="16" viewBox="0 0 20 20" fill="currentColor">
                  <path fill-rule="evenodd" d="M10 18a8 8 0 100-16 8 8 0 000 16zm3.707-9.293a1 1 0 00-1.414-1.414L9 10.586 7.707 9.293a1 1 0 00-1.414 1.414l2 2a1 1 0 001.414 0l4-4z" clip-rule="evenodd"/>
                </svg>
                他社見積もりの妥当性診断
              </span>
              <span class="cta-check-pill">
                <svg class="check-icon" width="16" height="16" viewBox="0 0 20 20" fill="currentColor">
                  <path fill-rule="evenodd" d="M10 18a8 8 0 100-16 8 8 0 000 16zm3.707-9.293a1 1 0 00-1.414-1.414L9 10.586 7.707 9.293a1 1 0 00-1.414 1.414l2 2a1 1 0 001.414 0l4-4z" clip-rule="evenodd"/>
                </svg>
                最短即日の概算提示
              </span>
              <span class="cta-check-pill">
                <svg class="check-icon" width="16" height="16" viewBox="0 0 20 20" fill="currentColor">
                  <path fill-rule="evenodd" d="M10 18a8 8 0 100-16 8 8 0 000 16zm3.707-9.293a1 1 0 00-1.414-1.414L9 10.586 7.707 9.293a1 1 0 00-1.414 1.414l2 2a1 1 0 001.414 0l4-4z" clip-rule="evenodd"/>
                </svg>
                仕様変更に強いアジャイル
              </span>
            </div>
            <div class="cta-buttons">
              <a href="../index.html#contact" class="btn btn-primary btn-cta-primary">
                無料相談・見積もりを依頼する <span class="arrow">→</span>
              </a>
              <a href="../cases/index.html" class="btn btn-secondary btn-cta-secondary">
                開発実績を見る →
              </a>
            </div>
            <p class="cta-microcopy">
              <span>🔒</span> オンライン相談対応・無理な営業は一切いたしません
            </p>
          </div>
"""

SIDEBAR_CTA_HTML = """          <div class="sidebar-box glass-card sidebar-cta">
            <div class="sidebar-cta-badge">
              <span class="badge-dot"></span>無料相談・相見積もり歓迎
            </div>
            <h3 class="sidebar-cta-title">
              システム開発・AI導入の<br>
              <span class="cta-highlight">無料相談・概算見積もり</span>
            </h3>
            <ul class="sidebar-cta-points">
              <li class="sidebar-cta-point">
                <svg class="check-icon" width="16" height="16" viewBox="0 0 20 20" fill="currentColor">
                  <path fill-rule="evenodd" d="M10 18a8 8 0 100-16 8 8 0 000 16zm3.707-9.293a1 1 0 00-1.414-1.414L9 10.586 7.707 9.293a1 1 0 00-1.414 1.414l2 2a1 1 0 001.414 0l4-4z" clip-rule="evenodd"/>
                </svg>
                <span>開発費を最大50%以上削減</span>
              </li>
              <li class="sidebar-cta-point">
                <svg class="check-icon" width="16" height="16" viewBox="0 0 20 20" fill="currentColor">
                  <path fill-rule="evenodd" d="M10 18a8 8 0 100-16 8 8 0 000 16zm3.707-9.293a1 1 0 00-1.414-1.414L9 10.586 7.707 9.293a1 1 0 00-1.414 1.414l2 2a1 1 0 001.414 0l4-4z" clip-rule="evenodd"/>
                </svg>
                <span>他社見積もりの妥当性診断</span>
              </li>
              <li class="sidebar-cta-point">
                <svg class="check-icon" width="16" height="16" viewBox="0 0 20 20" fill="currentColor">
                  <path fill-rule="evenodd" d="M10 18a8 8 0 100-16 8 8 0 000 16zm3.707-9.293a1 1 0 00-1.414-1.414L9 10.586 7.707 9.293a1 1 0 00-1.414 1.414l2 2a1 1 0 001.414 0l4-4z" clip-rule="evenodd"/>
                </svg>
                <span>最短即日の概算見積もり提示</span>
              </li>
            </ul>
            <a href="../index.html#contact" class="btn sidebar-cta-btn">
              無料相談・見積もりを依頼する <span class="arrow">→</span>
            </a>
            <span class="sidebar-cta-note">🔒 オンライン相談対応・無理な営業なし</span>
          </div>
"""

def update_file(filepath):
    with open(filepath, "r", encoding="utf-8") as f:
        content = f.read()

    # 1. Clean up any existing bottom CTA blocks
    content = re.sub(r'<!--\s*(?:Conversion\s+CTA|Eye-catching\s+Bottom\s+CTA)[^>]*-->\s*', '', content)
    content = re.sub(r'<div class="(?:inline-cta|inline-cta-box|article-bottom-cta)[^"]*">.*?</div>\s*(?=(?:</main>|</div>\s*</article>))', '', content, flags=re.DOTALL)
    content = re.sub(r'<div class="inline-cta-box glass-card"[^>]*>.*?</div>\s*</div>', '</div>', content, flags=re.DOTALL)

    # 2. Insert the new bottom CTA right before </main> or </div>\s*</article>
    if "</main>" in content:
        content = re.sub(r'(?s)(.*?)\s*</main>', rf'\g<1>\n\n{BOTTOM_CTA_HTML}        </main>', content, count=1)
    elif "</div>\s*</article>" in content:
        content = re.sub(r'(?s)(.*?)\s*</div>\s*</article>', rf'\g<1>\n\n{BOTTOM_CTA_HTML}        </div>\n      </article>', content, count=1)

    # 3. Clean up and replace sidebar CTA
    if re.search(r'<div class="sidebar-box[^\"]*sidebar-cta[^>]*>.*?</div>', content, flags=re.DOTALL):
        content = re.sub(
            r'<div class="sidebar-box[^\"]*sidebar-cta[^>]*>.*?</div>',
            SIDEBAR_CTA_HTML.strip(),
            content,
            flags=re.DOTALL
        )
    else:
        if "</aside>" in content:
            content = re.sub(r'(?s)(.*?)\s*</aside>', rf'\g<1>\n{SIDEBAR_CTA_HTML}        </aside>', content, count=1)

    with open(filepath, "w", encoding="utf-8") as f:
        f.write(content)

def main():
    files = [f for f in os.listdir(COLUMN_DIR) if f.endswith(".html") and f != "index.html"]
    print(f"Updating CTAs in {len(files)} column files...")
    for fn in sorted(files):
        fp = os.path.join(COLUMN_DIR, fn)
        update_file(fp)
    print("All column files updated successfully.")

if __name__ == "__main__":
    main()
