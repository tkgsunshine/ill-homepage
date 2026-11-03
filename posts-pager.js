/*
 * Paged "latest" lists for the top-page columns and cases.
 * The three cards in the HTML stay as page 1 (search engines and no-JS readers see them as before).
 * When the section comes near, more cards are read from the list page (column/ or cases/) and split into pages
 * of three, with page buttons whose highlight slides and cards that swap with a short staggered slide.
 * Written for Ill inc. after the React Bits Pro "Blog 2" block description; no code from it is used.
 * Styles are injected here so style.css (served immutable) does not change.
 */
(() => {
  const sections = document.querySelectorAll('[data-paged-posts]');
  if (!sections.length || !window.fetch || !window.DOMParser) return;
  const reduce = window.matchMedia('(prefers-reduced-motion: reduce)').matches;
  const PER = 3;
  const MAX = 12;

  const style = document.createElement('style');
  style.textContent = `
    .pager { display: flex; align-items: center; justify-content: center; gap: .8rem; margin-top: 4rem; }
    .pager-nums { position: relative; display: flex; gap: .4rem; padding: .4rem; border-radius: 99rem;
      background: var(--glass-bg); border: 1px solid var(--glass-border); }
    .pager-pill { position: absolute; top: .4rem; bottom: .4rem; left: 0; border-radius: 99rem;
      background: var(--gradient-primary); transition: transform .45s cubic-bezier(.65,0,.35,1), width .45s cubic-bezier(.65,0,.35,1); }
    .pager button { position: relative; z-index: 1; font: inherit; font-family: var(--font-en); cursor: pointer;
      border: 0; background: none; color: var(--text-muted); }
    .pager-num { min-width: 4rem; height: 4rem; border-radius: 99rem; font-size: 1.4rem; font-weight: 700;
      transition: color .3s ease; }
    .pager-num[aria-current="true"] { color: #fff; }
    .pager-num:not([aria-current="true"]):hover { color: var(--text-main); }
    .pager-step { width: 4.4rem; height: 4.4rem; border-radius: 50%; border: 1px solid var(--glass-border) !important;
      background: var(--glass-bg) !important; display: grid; place-items: center; transition: color .3s ease, border-color .3s ease; }
    .pager-step:hover:not(:disabled) { color: var(--color-cyan); border-color: var(--color-cyan) !important; }
    .pager-step:disabled { opacity: .35; cursor: default; }
    .pager-step svg { width: 1.8rem; height: 1.8rem; stroke: currentColor; stroke-width: 2; fill: none; }
    .pager button:focus-visible { outline: 2px solid var(--color-cyan); outline-offset: 2px; }
    .paged-grid { transition: height .4s ease; }
  `;
  document.head.appendChild(style);

  const path = href => new URL(href, location.href).pathname.replace(/\.html$/, '').replace(/\/$/, '');

  // Reads cards from the list page and fixes their links and images to work from this page.
  const loadCards = async src => {
    const base = new URL(src, location.href);
    const res = await fetch(base, { credentials: 'same-origin' });
    if (!res.ok) throw new Error(res.status);
    const doc = new DOMParser().parseFromString(await res.text(), 'text/html');
    return [...doc.querySelectorAll('article.column-card')].map(card => {
      card.querySelectorAll('[href]').forEach(a => a.setAttribute('href', new URL(a.getAttribute('href'), base).pathname));
      card.querySelectorAll('img[src]').forEach(img => img.setAttribute('src', new URL(img.getAttribute('src'), base).pathname));
      card.classList.remove('reveal');
      card.removeAttribute('data-category');
      return document.importNode(card, true);
    });
  };

  const setup = async section => {
    const grid = section.querySelector('.column-grid');
    const first = [...grid.querySelectorAll(':scope > article.column-card')];
    if (!grid || !first.length) return;
    let more;
    try { more = await loadCards(section.dataset.pagedPosts); } catch (e) { return; }
    const seen = new Set(first.map(c => path(c.querySelector('a[href]').getAttribute('href'))));
    const cards = first.slice();
    for (const c of more) {
      if (cards.length >= MAX) break;
      const a = c.querySelector('a[href]');
      if (!a || seen.has(path(a.getAttribute('href')))) continue;
      seen.add(path(a.getAttribute('href')));
      cards.push(c);
    }
    const pages = Math.ceil(cards.length / PER);
    if (pages < 2) return;
    grid.classList.add('paged-grid');
    grid.setAttribute('aria-live', 'polite');

    const label = section.querySelector('.section-title')?.textContent.trim() || '一覧';
    const nav = document.createElement('nav');
    nav.className = 'pager';
    nav.setAttribute('aria-label', `${label}のページ`);
    const arrow = d => `<svg viewBox="0 0 24 24" aria-hidden="true"><polyline points="${d}"/></svg>`;
    nav.innerHTML = `
      <button type="button" class="pager-step" data-step="-1" aria-label="前のページ">${arrow('15 18 9 12 15 6')}</button>
      <div class="pager-nums"><span class="pager-pill" aria-hidden="true"></span>
        ${Array.from({ length: pages }, (_, i) => `<button type="button" class="pager-num" data-page="${i}" aria-label="${i + 1}ページ目">${i + 1}</button>`).join('')}
      </div>
      <button type="button" class="pager-step" data-step="1" aria-label="次のページ">${arrow('9 18 15 12 9 6')}</button>`;
    grid.after(nav);
    const pill = nav.querySelector('.pager-pill');
    const nums = [...nav.querySelectorAll('.pager-num')];
    const [prev, next] = nav.querySelectorAll('.pager-step');

    let current = 0, busy = false;
    const mark = () => {
      nums.forEach((b, i) => b.setAttribute('aria-current', i === current ? 'true' : 'false'));
      const b = nums[current];
      pill.style.width = b.offsetWidth + 'px';
      pill.style.transform = `translateX(${b.offsetLeft}px)`;
      prev.disabled = current === 0;
      next.disabled = current === pages - 1;
    };

    const go = async to => {
      if (busy || to === current || to < 0 || to >= pages) return;
      busy = true;
      const dir = to > current ? 1 : -1;
      current = to;
      mark();
      const out = [...grid.querySelectorAll(':scope > article.column-card')];
      const incoming = cards.slice(to * PER, to * PER + PER);
      if (reduce) {
        out.forEach(c => c.remove());
        incoming.forEach(c => grid.appendChild(c));
        busy = false;
        return;
      }
      // Old cards slide out, the grid eases to its new height, new cards slide in one after another.
      const oldH = grid.offsetHeight;
      grid.style.height = oldH + 'px';
      out.forEach((c, i) => Object.assign(c.style, {
        transition: `opacity .25s ease ${i * 40}ms, transform .25s ease ${i * 40}ms`,
        opacity: '0', transform: `translateX(${-dir * 24}px)`
      }));
      await new Promise(r => setTimeout(r, 340));
      out.forEach(c => { c.style.transition = c.style.opacity = c.style.transform = ''; c.remove(); });
      incoming.forEach(c => {
        Object.assign(c.style, { transition: 'none', opacity: '0', transform: `translateX(${dir * 32}px)` });
        grid.appendChild(c);
      });
      grid.style.height = '';
      const newH = grid.offsetHeight;
      grid.style.height = oldH + 'px';
      void grid.offsetHeight;
      grid.style.height = newH + 'px';
      incoming.forEach((c, i) => Object.assign(c.style, {
        transition: `opacity .45s ease ${i * 70}ms, transform .55s cubic-bezier(.22,1,.36,1) ${i * 70}ms`,
        opacity: '1', transform: 'none'
      }));
      await new Promise(r => setTimeout(r, 720));
      grid.style.height = '';
      incoming.forEach(c => { c.style.transition = c.style.opacity = c.style.transform = ''; });
      busy = false;
    };

    nums.forEach((b, i) => b.addEventListener('click', () => go(i)));
    prev.addEventListener('click', () => go(current - 1));
    next.addEventListener('click', () => go(current + 1));
    window.addEventListener('resize', mark);
    mark();
  };

  // Only read the list pages when the section is about to be seen.
  const io = new IntersectionObserver(entries => {
    entries.forEach(e => { if (e.isIntersecting) { io.unobserve(e.target); setup(e.target); } });
  }, { rootMargin: '600px 0px' });
  sections.forEach(s => io.observe(s));
})();
