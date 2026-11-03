/*
 * Gradient blobs inside the top-page service cards.
 * Hovering a card wakes three soft blobs in the brand pink, purple and cyan; they drift and lean toward the pointer.
 * On touch screens a card lights up while it sits in the middle of the screen.
 * Written for Ill inc. after the React Bits Pro "Features 6" block description; no code from it is used.
 * Styles are injected here so style.css (served immutable) does not change.
 */
(() => {
  const cards = document.querySelectorAll('[data-feature-blobs] .service-card');
  if (!cards.length) return;
  const reduce = window.matchMedia('(prefers-reduced-motion: reduce)').matches;
  const canHover = window.matchMedia('(hover: hover) and (pointer: fine)').matches;

  const style = document.createElement('style');
  style.textContent = `
    .service-card.has-blobs { isolation: isolate; }
    .service-card.has-blobs::before { display: none; }
    .service-card.has-blobs > :not(.blob-layer) { position: relative; z-index: 1; }
    .blob-layer { position: absolute; inset: 0; z-index: 0; pointer-events: none; opacity: 0;
      transition: opacity .6s ease; border-radius: inherit; overflow: hidden; }
    .service-card.blobs-on .blob-layer { opacity: 1; }
    .blob { position: absolute; width: 22rem; height: 22rem; left: 0; top: 0; border-radius: 50%;
      filter: blur(48px); will-change: transform; }
    .blob.b1 { background: var(--color-pink); opacity: .30; }
    .blob.b2 { background: var(--color-purple); opacity: .30; width: 26rem; height: 26rem; }
    .blob.b3 { background: var(--color-cyan); opacity: .32; width: 20rem; height: 20rem; }
    body.theme-light .blob.b1, body.theme-light .blob.b2 { opacity: .22; }
    body.theme-light .blob.b3 { opacity: .26; }
  `;
  document.head.appendChild(style);

  const state = [];
  cards.forEach((card, i) => {
    card.classList.add('has-blobs');
    const layer = document.createElement('div');
    layer.className = 'blob-layer';
    layer.setAttribute('aria-hidden', 'true');
    const blobs = ['b1', 'b2', 'b3'].map(c => {
      const b = document.createElement('span');
      b.className = 'blob ' + c;
      layer.appendChild(b);
      return b;
    });
    card.prepend(layer);
    // Pointer target in card-relative 0..1; rests at the upper right until touched.
    const s = { card, blobs, on: false, tx: 0.7, ty: 0.3, x: 0.7, y: 0.3, seed: i * 2.1 };
    state.push(s);

    if (canHover) {
      card.addEventListener('pointerenter', () => { s.on = true; card.classList.add('blobs-on'); wake(); });
      card.addEventListener('pointerleave', () => { s.on = false; card.classList.remove('blobs-on'); });
      card.addEventListener('pointermove', e => {
        const r = card.getBoundingClientRect();
        s.tx = (e.clientX - r.left) / r.width;
        s.ty = (e.clientY - r.top) / r.height;
      });
    }
  });

  if (!canHover) {
    // Touch: light the card that crosses the middle band of the screen.
    const io = new IntersectionObserver(entries => {
      entries.forEach(e => {
        const s = state.find(v => v.card === e.target);
        s.on = e.isIntersecting;
        s.card.classList.toggle('blobs-on', s.on);
      });
      wake();
    }, { rootMargin: '-35% 0px -35% 0px' });
    state.forEach(s => io.observe(s.card));
  }

  let raf = 0;
  const place = (s, now) => {
    const w = s.card.clientWidth, h = s.card.clientHeight;
    const t = reduce ? 0 : now / 1000;
    s.x += (s.tx - s.x) * 0.08;
    s.y += (s.ty - s.y) * 0.08;
    // Each blob orbits its own anchor; the anchors lean toward the pointer by different amounts.
    const anchors = [
      [0.15 + (s.x - 0.15) * 0.55, 0.20 + (s.y - 0.20) * 0.55],
      [0.85 + (s.x - 0.85) * 0.35, 0.80 + (s.y - 0.80) * 0.35],
      [s.x, s.y]
    ];
    s.blobs.forEach((b, k) => {
      const a = anchors[k];
      const ox = Math.sin(t * (0.5 + k * 0.17) + s.seed + k) * 0.10;
      const oy = Math.cos(t * (0.42 + k * 0.13) + s.seed * 1.3 + k) * 0.08;
      const bw = b.offsetWidth, bh = b.offsetHeight;
      b.style.transform = `translate(${(a[0] + ox) * w - bw / 2}px, ${(a[1] + oy) * h - bh / 2}px)`;
    });
  };
  const loop = now => {
    raf = 0;
    const active = state.filter(s => s.on);
    active.forEach(s => place(s, now));
    if (active.length && !reduce) raf = requestAnimationFrame(loop);
  };
  const wake = () => { if (!raf) raf = requestAnimationFrame(loop); };
  state.forEach(s => place(s, performance.now()));
})();
