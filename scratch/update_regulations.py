import os

site_dir = '/Users/user/.gemini/antigravity/scratch/ill-homepage'
reg_path = os.path.join(site_dir, 'REGULATIONS.md')

with open(reg_path, 'r', encoding='utf-8') as f:
    content = f.read()

new_section = """
---

## 8. 見出しデザイン＆ビジュアル階層構造レギュレーション
* **H2大見出し（章タイトル）のデザイン規定**:
  * 左側に5pxの太めグラデーションアクセントバー（`border-left: 5px solid var(--color-cyan)`）を配置。
  * 背景にネオングラデーションの半透明背景（`background: linear-gradient(90deg, ...)`）と右角丸（`border-radius: 0 1.2rem 1.2rem 0`）、および立体的シャドウ（`box-shadow`）を適用。
  * 単なる下線のみのフラットデザインを排除し、一目で章の切り替わりがわかるハイテック・プレミアムな背景ブロックデザインで統一する。
* **H3中見出し（小見出し）のデザイン規定**:
  * 左側に4pxのパープルアクセントバー（`border-left: 4px solid var(--color-purple)`）を配置。
  * 背景にすっきりとしたアッシュトーンの角丸タグ風背景（`background: var(--bg-subtle)` / `padding: 1rem 1.6rem`）を敷き、本文テキストとの境界を明確に区別する。
* **FAQ（よくある質問）見出し＆文末表記規律**:
  * FAQの質問タイトルは「〜は自動化できますか？」「〜は可能ですか？」の形式で文末の疑問詞（「か？」）の誤字脱字・タイポ（「起？」など）を100%防止・検知する自動テストを義務付ける。
"""

if "## 8. 見出しデザイン＆ビジュアル階層構造レギュレーション" not in content:
    content += new_section
    with open(reg_path, 'w', encoding='utf-8') as f:
        f.write(content)
    print("Updated REGULATIONS.md with Section 8 successfully!")

# Also update the artifact REGULATIONS file in brain directory if present
brain_reg = '/Users/user/.gemini/antigravity/brain/e2d060df-f6ea-4e3d-8e62-9acdb00bd704/column_generation_regulations.md'
if os.path.exists(brain_reg):
    with open(brain_reg, 'r', encoding='utf-8') as f:
        brain_content = f.read()
    if "見出しデザイン" not in brain_content:
        brain_content += new_section
        with open(brain_reg, 'w', encoding='utf-8') as f:
            f.write(brain_content)
        print("Updated artifact column_generation_regulations.md successfully!")
