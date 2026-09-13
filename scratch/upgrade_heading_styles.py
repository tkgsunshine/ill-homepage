import os

site_dir = '/Users/user/.gemini/antigravity/scratch/ill-homepage'
css_path = os.path.join(site_dir, 'style.css')

with open(css_path, 'r', encoding='utf-8') as f:
    css = f.read()

# Replace H2 and H3 rules in .article-body
old_h2_h3 = """.article-body h2 {
  font-size: 2.4rem;
  font-weight: 800;
  margin: 4.8rem 0 2.4rem 0;
  padding-bottom: 1.2rem;
  border-bottom: 1px solid var(--glass-border);
  position: relative;
}

.article-body h2::after {
  content: '';
  position: absolute;
  bottom: -1px;
  left: 0;
  width: 80px;
  height: 2px;
  background: var(--gradient-primary);
}

.article-body h3 {
  font-size: 2rem;
  font-weight: 700;
  margin: 3.6rem 0 1.6rem 0;
  display: flex;
  align-items: center;
  gap: 1rem;
}

.article-body h3::before {
  content: '';
  display: inline-block;
  width: 4px;
  height: 1.8rem;
  background: var(--color-cyan);
  border-radius: 2px;
}"""

new_h2_h3 = """/* Article Headings (Enhanced High-Impact Design) */
.article-body h2 {
  font-size: clamp(2rem, 4.5vw, 2.4rem);
  font-weight: 800;
  line-height: 1.4;
  margin: 4.8rem 0 2.4rem 0;
  padding: 1.4rem 2rem;
  background: linear-gradient(90deg, hsla(186, 100%, 50%, 0.1) 0%, hsla(271, 100%, 54%, 0.05) 60%, transparent 100%);
  border-left: 5px solid var(--color-cyan);
  border-bottom: 1px solid var(--glass-border);
  border-radius: 0 1.2rem 1.2rem 0;
  color: var(--text-main);
  position: relative;
  box-shadow: 0 4px 20px rgba(0, 0, 0, 0.04);
}

body.theme-light .article-body h2 {
  background: linear-gradient(90deg, hsla(190, 100%, 42%, 0.12) 0%, hsla(271, 90%, 50%, 0.06) 65%, rgba(255, 255, 255, 0.8) 100%);
  border-left: 5px solid var(--color-cyan);
  border-bottom: 1px solid var(--glass-border);
  color: hsl(var(--hue-base), 40%, 10%);
  box-shadow: 0 4px 16px rgba(15, 23, 42, 0.05);
}

.article-body h3 {
  font-size: clamp(1.7rem, 3.8vw, 1.9rem);
  font-weight: 700;
  line-height: 1.45;
  margin: 3.6rem 0 1.6rem 0;
  padding: 1rem 1.6rem;
  background: var(--bg-subtle);
  border-left: 4px solid var(--color-purple);
  border-radius: 0 0.8rem 0.8rem 0;
  color: var(--text-main);
  display: flex;
  align-items: center;
  gap: 1rem;
}

body.theme-light .article-body h3 {
  background: rgba(0, 0, 0, 0.03);
  border-left: 4px solid var(--color-purple);
  color: hsl(var(--hue-base), 40%, 12%);
}"""

if old_h2_h3 in css:
    css = css.replace(old_h2_h3, new_h2_h3)
    print("Replaced article H2/H3 CSS with high-impact design rules!")
else:
    print("WARNING: Could not find exact old H2/H3 block. Checking fallback...")

with open(css_path, 'w', encoding='utf-8') as f:
    f.write(css)

print("Updated style.css with enhanced heading design!")
