/*
 * Services as a list and a detail view, instead of a grid of identical cards.
 * Wide screens: service names in a column on the left, the chosen service's details on the right.
 * Narrow screens: the same list, with the details opening under the chosen name.
 * The service cards stay in the HTML as they are (search engines and no-JS readers see every service);
 * this script only rearranges them. Styles are injected here so style.css (served immutable) does not change.
 */
(() => {
  const grid = document.querySelector('[data-services-split]');
  if (!grid) return;
  const cards = [...grid.querySelectorAll(':scope > .service-card')];
  if (cards.length < 2) return;
  const reduce = window.matchMedia('(prefers-reduced-motion: reduce)').matches;
  const wide = window.matchMedia('(min-width: 900px)');

  const style = document.createElement('style');
  style.textContent = `
    .svc-split { position: relative; display: grid; gap: 0 5.6rem;
      grid-template-columns: minmax(24rem, 34rem) minmax(0, 1fr);
      grid-template-rows: repeat(${cards.length}, auto) 1fr; }
    .svc-split::before { content: ''; position: absolute; left: 0; top: 0; bottom: 0; width: 1px;
      background: var(--glass-border); grid-row: 1 / -1; }
    .svc-tab { grid-column: 1; display: flex; align-items: center; gap: 1.4rem; width: 100%;
      padding: 2rem 1.6rem 2rem 2.4rem; border: 0; background: none; cursor: pointer; text-align: left;
      font: inherit; font-size: 1.7rem; font-weight: 700; color: var(--text-muted); transition: color .3s ease; }
    .svc-tab:hover, .svc-tab[aria-expanded="true"] { color: var(--text-main); }
    .svc-tab:focus-visible { outline: 2px solid var(--color-cyan); outline-offset: -2px; border-radius: .6rem; }
    .svc-tab svg { width: 2.2rem; height: 2.2rem; flex: none; stroke: currentColor; stroke-width: 1.5; fill: none; opacity: .8; }
    .svc-tab[aria-expanded="true"] svg { stroke: var(--color-cyan); opacity: 1; }
    .svc-bar { position: absolute; left: -1px; top: 0; width: 3px; border-radius: 3px; background: var(--gradient-primary);
      transition: transform .45s cubic-bezier(.65,0,.35,1), height .45s cubic-bezier(.65,0,.35,1); }
    .svc-split > .service-card { grid-column: 2; grid-row: 1 / -1; align-self: start; height: auto; }
    .svc-split > .service-card:hover { transform: none; }
    .svc-split > .service-card[hidden] { display: none; }
    .svc-split > .service-card .service-title { font-size: 2.6rem; }
    /* The detail panel takes the opposite light/dark of the page, like flipping the theme switch for this card only. */
    body.theme-light .svc-split > .service-card {
      --bg-card: hsl(226, 40%, 10%); --glass-bg: hsl(226, 45%, 8%); --glass-border: hsla(0, 0%, 100%, 0.1);
      --text-main: hsl(210, 40%, 96%); --text-muted: hsl(215, 20%, 72%);
      --gradient-soft: linear-gradient(135deg, hsla(328, 100%, 59%, 0.22) 0%, hsla(271, 100%, 54%, 0.22) 50%, hsla(186, 100%, 50%, 0.22) 100%);
      box-shadow: 0 24px 60px -20px rgba(15, 23, 42, 0.45);
    }
    body:not(.theme-light) .svc-split > .service-card {
      --bg-card: hsl(226, 25%, 99%); --glass-bg: hsl(226, 30%, 98%); --glass-border: hsla(226, 20%, 10%, 0.1);
      --text-main: hsl(226, 40%, 12%); --text-muted: hsl(226, 15%, 40%);
      --color-cyan: hsl(190, 100%, 38%);
      box-shadow: 0 24px 60px -20px rgba(0, 0, 0, 0.7);
    }
    .svc-split > .service-card { background: var(--glass-bg); border-color: var(--glass-border); color: var(--text-main); }
    .svc-split > .service-card:hover { border-color: var(--glass-border); }
    @media (min-width: 900px) {
      /* Icon and title side by side at the top of the detail panel. */
      .svc-split > .service-card { display: grid; grid-template-columns: auto minmax(0, 1fr); column-gap: 2rem; align-items: center; }
      .svc-split > .service-card > :not(.service-icon-container):not(.service-title):not(.blob-layer) { grid-column: 1 / -1; }
      .svc-split > .service-card .service-icon-container { margin-bottom: 0; }
      .svc-split > .service-card .service-title { margin-bottom: 0; }
      .svc-split > .service-card .service-desc { margin-top: 2.4rem; }
    }
    @media (max-width: 899px) {
      .svc-split { display: block; padding-left: 0; }
      .svc-split::before, .svc-bar { display: none; }
      .svc-tab { padding: 1.8rem .4rem; border-bottom: 1px solid var(--glass-border); }
      .svc-tab::after { content: ''; margin-left: auto; width: .9rem; height: .9rem; border-right: 2px solid currentColor;
        border-bottom: 2px solid currentColor; transform: rotate(45deg) translateY(-25%); transition: transform .3s ease; }
      .svc-tab[aria-expanded="true"]::after { transform: rotate(-135deg) translateY(-25%); }
      .svc-split > .service-card { margin: 1.6rem 0 2.4rem; padding: 3.2rem 2.4rem; }
      .svc-split > .service-card .service-icon-container, .svc-split > .service-card .service-title { display: none; }
    }
  `;
  document.head.appendChild(style);

  grid.className = 'svc-split';
  const bar = document.createElement('span');
  bar.className = 'svc-bar';
  bar.setAttribute('aria-hidden', 'true');

  const tabs = cards.map((card, i) => {
    const id = card.id || `service-${i + 1}`;
    card.id = id;
    const tab = document.createElement('button');
    tab.type = 'button';
    tab.className = 'svc-tab';
    tab.id = `${id}-tab`;
    tab.setAttribute('aria-controls', id);
    const icon = card.querySelector('.service-icon');
    if (icon) {
      const svg = icon.cloneNode(true);
      svg.removeAttribute('class');
      svg.setAttribute('aria-hidden', 'true');
      tab.appendChild(svg);
    }
    tab.append(card.querySelector('.service-title').textContent.trim());
    card.setAttribute('role', 'region');
    card.setAttribute('aria-labelledby', tab.id);
    grid.insertBefore(tab, card);
    return tab;
  });
  grid.appendChild(bar);

  let current = -1;
  const moveBar = () => {
    const t = tabs[current];
    bar.style.height = t.offsetHeight + 'px';
    bar.style.transform = `translateY(${t.offsetTop}px)`;
  };
  const open = (i, focus) => {
    if (i === current) {
      // On narrow screens a second tap closes the open item.
      if (!wide.matches) { tabs[i].setAttribute('aria-expanded', 'false'); cards[i].hidden = true; current = -1; }
      return;
    }
    tabs.forEach((t, k) => t.setAttribute('aria-expanded', String(k === i)));
    cards.forEach((c, k) => { c.hidden = k !== i; });
    current = i;
    if (focus) tabs[i].focus();
    if (wide.matches) moveBar();
    if (!reduce) {
      const c = cards[i];
      if (wide.matches) {
        // The flipped panel spreads out from the list side, like a light being switched.
        c.animate([{ clipPath: 'circle(0% at 0% 50%)' }, { clipPath: 'circle(150% at 0% 50%)' }],
          { duration: 650, easing: 'cubic-bezier(.65,0,.35,1)' });
      } else {
        c.animate([{ opacity: 0, transform: 'translateY(12px)' }, { opacity: 1, transform: 'none' }],
          { duration: 450, easing: 'cubic-bezier(.22,1,.36,1)' });
      }
    }
  };

  tabs.forEach((t, i) => {
    t.addEventListener('click', () => open(i));
    t.addEventListener('keydown', e => {
      const step = { ArrowDown: 1, ArrowUp: -1 }[e.key];
      if (step) { e.preventDefault(); tabs[(i + step + tabs.length) % tabs.length].focus(); }
      if (e.key === 'Home') { e.preventDefault(); tabs[0].focus(); }
      if (e.key === 'End') { e.preventDefault(); tabs[tabs.length - 1].focus(); }
    });
  });
  // Wide screens always show one service; reopen the first if the last one was closed on a narrow screen.
  const onChange = () => { if (current < 0) open(0); else if (wide.matches) moveBar(); };
  wide.addEventListener('change', onChange);
  window.addEventListener('resize', () => { if (current >= 0 && wide.matches) moveBar(); });
  if (document.fonts) document.fonts.ready.then(() => { if (current >= 0 && wide.matches) moveBar(); });

  // First paint: open the first service without the entrance animation.
  tabs.forEach(t => t.setAttribute('aria-expanded', 'false'));
  cards.forEach(c => { c.hidden = true; });
  current = 0;
  tabs[0].setAttribute('aria-expanded', 'true');
  cards[0].hidden = false;
  if (wide.matches) moveBar();
})();
