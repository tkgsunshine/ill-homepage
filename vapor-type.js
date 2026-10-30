/*
 * Vapor heading for the top-page hero.
 * The heading condenses out of drifting vapour when the page opens, then sits still as normal text.
 * Moving the pointer over it blows letters into vapour; they settle back on their own.
 * Written for Ill inc. after React Bits Pro "Vapor Type"; no code from that component is used.
 * The real <h1> text stays in the page (for search engines, screen readers and copy) and is only made transparent.
 */
(() => {
  const title = document.querySelector('.hero-title');
  if (!title || !window.HTMLCanvasElement) return;
  if (window.matchMedia('(prefers-reduced-motion: reduce)').matches) return;

  const STEP = 2;            // sampling grid in CSS px
  const VAPOR = '#b19eef';   // colour particles fade toward
  const CONDENSE = 1.8;      // seconds for a particle to condense
  const STAGGER = 0.9;       // seconds between the left and right edge starting
  const RADIUS = 0.8;        // pointer reach, in font-size multiples
  const RECOVERY = 1.2;      // seconds before blown letters drift back

  const canvas = document.createElement('canvas');
  canvas.setAttribute('aria-hidden', 'true');
  Object.assign(canvas.style, { position: 'absolute', left: '0', top: '0', pointerEvents: 'none' });
  const ctx = canvas.getContext('2d');
  const page = document.createElement('canvas');
  const pctx = page.getContext('2d', { willReadFrequently: true });

  let dpr = 1, pad = 0, fontPx = 64, W = 0, H = 0;
  let parts = [];
  let raf = 0, started = 0, last = 0, settled = false;
  const pointer = { x: 0, y: 0, over: false, at: 0 };

  const hideDomText = () => {
    title.style.color = 'transparent';
    title.querySelectorAll('.glow-word').forEach(el => { el.style.background = 'none'; });
  };
  const showDomText = () => {
    title.style.color = '';
    title.querySelectorAll('.glow-word').forEach(el => { el.style.background = ''; });
    canvas.remove();
  };

  // Draws the heading, character by character, at the exact places the browser laid it out.
  const paintText = () => {
    const box = title.getBoundingClientRect();
    const cs = getComputedStyle(title);
    fontPx = parseFloat(cs.fontSize);
    pad = Math.round(fontPx * 1.2);
    dpr = Math.min(window.devicePixelRatio || 1, 2);
    W = Math.ceil(box.width + pad * 2);
    H = Math.ceil(box.height + pad * 2);
    for (const c of [canvas, page]) { c.width = W * dpr; c.height = H * dpr; }
    Object.assign(canvas.style, { width: W + 'px', height: H + 'px', left: -pad + 'px', top: -pad + 'px' });
    pctx.setTransform(dpr, 0, 0, dpr, 0, 0);
    pctx.clearRect(0, 0, W, H);

    const root = getComputedStyle(document.body);
    const walker = document.createTreeWalker(title, NodeFilter.SHOW_TEXT);
    const range = document.createRange();
    for (let node = walker.nextNode(); node; node = walker.nextNode()) {
      const el = node.parentElement;
      if (el.closest('.typing-cursor')) continue;
      const ecs = getComputedStyle(el);
      pctx.font = `${ecs.fontWeight} ${ecs.fontSize} ${ecs.fontFamily}`;
      const m = pctx.measureText('本');
      const ascent = m.fontBoundingBoxAscent ?? fontPx * 0.88;
      let fill = getComputedStyle(title).getPropertyValue('--text-main') ? root.getPropertyValue('--text-main').trim() : '#111';
      if (el.closest('.glow-word')) {
        const g = el.closest('.glow-word').getBoundingClientRect();
        const x0 = g.left - box.left + pad, y0 = g.top - box.top + pad;
        const grad = pctx.createLinearGradient(x0, y0, x0 + g.width, y0 + g.height);
        grad.addColorStop(0, root.getPropertyValue('--color-pink').trim());
        grad.addColorStop(0.5, root.getPropertyValue('--color-purple').trim());
        grad.addColorStop(1, root.getPropertyValue('--color-cyan').trim());
        fill = grad;
      }
      pctx.fillStyle = fill;
      const text = node.textContent;
      for (let i = 0; i < text.length; i++) {
        if (!text[i].trim()) continue;
        range.setStart(node, i);
        range.setEnd(node, i + 1);
        const r = range.getBoundingClientRect();
        if (!r.width) continue;
        pctx.fillText(text[i], r.left - box.left + pad, r.top - box.top + pad + ascent);
      }
    }
  };

  // Turns the painted heading into particles, one per filled cell of the grid.
  const sample = () => {
    const data = pctx.getImageData(0, 0, page.width, page.height).data;
    const next = [];
    for (let y = 0; y < H; y += STEP) {
      for (let x = 0; x < W; x += STEP) {
        const i = (Math.floor(y * dpr) * page.width + Math.floor(x * dpr)) * 4;
        if (data[i + 3] < 110) continue;
        next.push({
          tx: x, ty: y, r: data[i], g: data[i + 1], b: data[i + 2],
          x: 0, y: 0, vx: 0, vy: 0, t: 0, blown: 0,
          delay: ((x - pad) / Math.max(1, W - pad * 2)) * STAGGER + Math.random() * 0.25,
          sx: x + (Math.random() - 0.5) * fontPx * 1.4,
          sy: y + fontPx * (0.4 + Math.random() * 0.9),
          seed: Math.random() * 1000
        });
      }
    }
    parts = next;
  };

  const vr = 0xb1, vg = 0x9e, vb = 0xef;
  const ease = t => 1 - Math.pow(1 - t, 3);

  const frame = now => {
    raf = 0;
    const dt = Math.min(0.05, (now - last) / 1000 || 0);
    last = now;
    const time = (now - started) / 1000;
    ctx.setTransform(dpr, 0, 0, dpr, 0, 0);
    ctx.clearRect(0, 0, W, H);

    const reach = fontPx * RADIUS;
    // Once the entrance is over, draw the crisp heading and only cut out the letters' blown cells.
    const formed = time > CONDENSE + STAGGER + 0.3;
    if (formed) {
      ctx.setTransform(1, 0, 0, 1, 0, 0);
      ctx.drawImage(page, 0, 0);
      ctx.setTransform(dpr, 0, 0, dpr, 0, 0);
      for (const p of parts) if (p.blown) ctx.clearRect(p.tx, p.ty, STEP, STEP);
    }
    const calm = now - pointer.at > RECOVERY * 1000;
    let moving = false;

    for (const p of parts) {
      let alpha, mix;
      const t = Math.min(1, Math.max(0, (time - p.delay) / CONDENSE));
      if (t < 1) {
        // Condensing: drift in from below with a curl that dies away.
        const e = ease(t);
        const curl = (1 - e) * fontPx * 0.25;
        p.x = p.sx + (p.tx - p.sx) * e + Math.sin(p.seed + time * 3) * curl;
        p.y = p.sy + (p.ty - p.sy) * e + Math.cos(p.seed * 1.3 + time * 2.4) * curl * 0.6;
        alpha = Math.min(1, t * 1.6);
        mix = e;
        moving = true;
      } else {
        if (p.t < 1) { p.x = p.tx; p.y = p.ty; p.t = 1; }
        if (pointer.over) {
          const dx = p.x - pointer.x, dy = p.y - pointer.y;
          const d = Math.hypot(dx, dy);
          if (d < reach) {
            const f = (1 - d / reach) * 900;
            p.vx += (dx / (d || 1)) * f * dt + (Math.random() - 0.5) * 60 * dt;
            p.vy += (dy / (d || 1)) * f * dt - 380 * dt;
            p.blown = 1;
          }
        }
        if (p.blown) {
          // Vapour rises and curls, then is pulled home once the pointer has been still for a moment.
          if (!calm) {
            p.vx += Math.sin(p.seed + now / 400) * 40 * dt;
            p.vy -= 30 * dt;
          } else {
            p.vx += (p.tx - p.x) * 40 * dt;
            p.vy += (p.ty - p.y) * 40 * dt;
          }
          p.vx *= Math.pow(calm ? 0.002 : 0.08, dt);
          p.vy *= Math.pow(calm ? 0.002 : 0.08, dt);
          p.x += p.vx * dt;
          p.y += p.vy * dt;
          const off = Math.hypot(p.x - p.tx, p.y - p.ty);
          if (calm && off < 0.6 && Math.abs(p.vx) + Math.abs(p.vy) < 6) { p.x = p.tx; p.y = p.ty; p.vx = p.vy = 0; p.blown = 0; }
          else moving = true;
          mix = Math.max(0, 1 - off / (fontPx * 0.6));
          alpha = Math.max(0.15, mix);
        } else {
          alpha = 1; mix = 1;
        }
      }
      if (formed && !p.blown) continue;
      const r = Math.round(vr + (p.r - vr) * mix), g = Math.round(vg + (p.g - vg) * mix), b = Math.round(vb + (p.b - vb) * mix);
      ctx.fillStyle = `rgba(${r},${g},${b},${alpha})`;
      const s = mix > 0.98 ? STEP + 0.3 : 1.2 + mix;
      ctx.fillRect(p.x, p.y, s, s);
    }

    if (!moving && !pointer.over) {
      // At rest, show the crisp painted heading instead of the particle grid.
      ctx.clearRect(0, 0, W, H);
      ctx.setTransform(1, 0, 0, 1, 0, 0);
      ctx.drawImage(page, 0, 0);
      settled = true;
      return;
    }
    settled = false;
    raf = requestAnimationFrame(frame);
  };

  const wake = () => { if (!raf) { last = performance.now(); raf = requestAnimationFrame(frame); } };

  const build = () => {
    paintText();
    sample();
    if (!parts.length) { showDomText(); return false; }
    return true;
  };

  const start = () => {
    if (getComputedStyle(title).position === 'static') title.style.position = 'relative';
    title.appendChild(canvas);
    hideDomText();
    if (!build()) return;
    started = performance.now();
    wake();

    title.addEventListener('pointermove', e => {
      const b = canvas.getBoundingClientRect();
      pointer.x = e.clientX - b.left;
      pointer.y = e.clientY - b.top;
      pointer.over = true;
      pointer.at = performance.now();
      wake();
    });
    title.addEventListener('pointerleave', () => { pointer.over = false; pointer.at = performance.now(); wake(); });

    // Rebuild on resize and on the light/dark switch, without replaying the entrance.
    let timer = 0;
    let lastSize = `${title.offsetWidth}x${title.offsetHeight}`;
    const onResize = () => {
      const size = `${title.offsetWidth}x${title.offsetHeight}`;
      if (size !== lastSize) { lastSize = size; rebuild(); }
    };
    const rebuild = () => {
      clearTimeout(timer);
      timer = setTimeout(() => {
        if (!build()) return;
        for (const p of parts) { p.t = 1; p.x = p.tx; p.y = p.ty; }
        started = performance.now() - (CONDENSE + STAGGER + 1) * 1000;
        wake();
      }, 120);
    };
    new ResizeObserver(onResize).observe(title);
    new MutationObserver(rebuild).observe(document.body, { attributes: true, attributeFilter: ['class'] });
    // The web font may arrive after the first paint; repaint with it.
    if (document.fonts) document.fonts.addEventListener('loadingdone', rebuild);
  };

  const ready = document.fonts && document.fonts.ready ? document.fonts.ready : Promise.resolve();
  ready.then(() => requestAnimationFrame(start)).catch(showDomText);
})();
