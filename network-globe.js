/*
 * Network globe for the top-page hero: a dotted globe turned toward Japan and Vietnam.
 * Tokyo and Hanoi are linked by an arc, and a "deploy pulse" spreads out from Tokyo across the network every few seconds.
 * Written for Ill inc. after the React Bits Pro "Hero 26" block description; no code from it is used. Canvas 2D, no libraries.
 */
(() => {
  const host = document.querySelector('[data-network-globe]');
  if (!host || host.offsetParent === null) return;   // the hero visual is hidden on phones
  const canvas = document.createElement('canvas');
  canvas.setAttribute('aria-hidden', 'true');
  Object.assign(canvas.style, { position: 'absolute', inset: '0', width: '100%', height: '100%', display: 'block' });
  const ctx = canvas.getContext('2d');
  if (!ctx) return;
  host.appendChild(canvas);
  host.querySelector('.network-globe-fallback')?.remove();

  const reduce = window.matchMedia('(prefers-reduced-motion: reduce)').matches;
  const RAD = Math.PI / 180;
  const POINTS = 1100;
  const PULSE_EVERY = 3.2;   // seconds between deploy pulses
  const PULSE_TIME = 2.6;    // seconds for a pulse to cross half the globe
  const CENTER_LON = 122;    // keeps Japan and Vietnam facing the viewer
  const CENTER_LAT = 18;

  const unit = (lat, lon) => [Math.cos(lat * RAD) * Math.sin(lon * RAD), Math.sin(lat * RAD), Math.cos(lat * RAD) * Math.cos(lon * RAD)];
  const dot = (a, b) => a[0] * b[0] + a[1] * b[1] + a[2] * b[2];

  // Evenly spread points (Fibonacci sphere).
  const pts = [];
  const golden = Math.PI * (3 - Math.sqrt(5));
  for (let i = 0; i < POINTS; i++) {
    const y = 1 - (i / (POINTS - 1)) * 2;
    const r = Math.sqrt(1 - y * y);
    pts.push([Math.cos(golden * i) * r, y, Math.sin(golden * i) * r]);
  }
  const tokyo = unit(35.68, 139.69);
  const hanoi = unit(21.03, 105.85);

  // A sparse network: hub points joined to their nearest neighbours.
  const hubs = pts.filter((_, i) => i % 9 === 0);
  const edges = [];
  hubs.forEach((a, i) => {
    hubs.map((b, j) => [j, dot(a, b)]).filter(([j]) => j > i).sort((x, y) => y[1] - x[1]).slice(0, 2)
      .forEach(([j, d]) => { if (d > 0.93) edges.push([a, hubs[j]]); });
  });

  let W = 0, H = 0, R = 0, dpr = 1, raf = 0, visible = false, start = performance.now();
  let leanX = 0, leanY = 0, targetX = 0, targetY = 0;

  const resize = () => {
    dpr = Math.min(window.devicePixelRatio || 1, 2);
    W = host.clientWidth; H = host.clientHeight;
    canvas.width = Math.round(W * dpr); canvas.height = Math.round(H * dpr);
    R = Math.min(W, H) * 0.4;
    if (!raf) draw(performance.now());
  };

  const palette = () => {
    const cs = getComputedStyle(document.body);
    const light = document.body.classList.contains('theme-light');
    return {
      dot: light ? '30,41,82' : '210,220,255',
      pink: cs.getPropertyValue('--color-pink').trim() || '#ff2e9b',
      purple: cs.getPropertyValue('--color-purple').trim() || '#8a14ff',
      cyan: cs.getPropertyValue('--color-cyan').trim() || '#00c8ff',
      text: cs.getPropertyValue('--text-main').trim() || '#111',
      muted: cs.getPropertyValue('--text-muted').trim() || '#666'
    };
  };
  let pal = palette();
  new MutationObserver(() => { pal = palette(); if (!raf) draw(performance.now()); }).observe(document.body, { attributes: true, attributeFilter: ['class'] });

  function draw(now) {
    const t = (now - start) / 1000;
    leanX += (targetX - leanX) * 0.06;
    leanY += (targetY - leanY) * 0.06;
    const lon = (CENTER_LON + (reduce ? 0 : Math.sin(t * 0.12) * 14) + leanX * 10) * RAD;
    const lat = (CENTER_LAT + leanY * 8) * RAD;
    const cl = Math.cos(lon), sl = Math.sin(lon), ca = Math.cos(lat), sa = Math.sin(lat);
    const cx = W / 2, cy = H / 2;
    // Rotate so (CENTER_LAT, CENTER_LON) faces the viewer, then project.
    const proj = p => {
      const x1 = p[0] * cl - p[2] * sl, z1 = p[0] * sl + p[2] * cl;
      const y2 = p[1] * ca - z1 * sa, z2 = p[1] * sa + z1 * ca;
      return [cx + x1 * R, cy - y2 * R, z2];
    };

    ctx.setTransform(dpr, 0, 0, dpr, 0, 0);
    ctx.clearRect(0, 0, W, H);

    // Soft rim.
    const rim = ctx.createRadialGradient(cx, cy, R * 0.7, cx, cy, R * 1.12);
    rim.addColorStop(0, 'rgba(0,0,0,0)');
    rim.addColorStop(0.85, `rgba(${pal.dot},0.06)`);
    rim.addColorStop(1, 'rgba(0,0,0,0)');
    ctx.fillStyle = rim;
    ctx.beginPath(); ctx.arc(cx, cy, R * 1.12, 0, Math.PI * 2); ctx.fill();

    // Deploy pulse: angular radius grows from Tokyo; points near the front of the wave light up.
    const phase = reduce ? 0.45 : (t % PULSE_EVERY) / PULSE_TIME;
    const wave = phase * Math.PI;           // 0 .. pi (half the globe)
    const waveOn = phase <= 1;

    ctx.lineWidth = 1;
    for (const [a, b] of edges) {
      const pa = proj(a), pb = proj(b);
      if (pa[2] < 0 || pb[2] < 0) continue;
      const da = Math.acos(Math.max(-1, Math.min(1, dot(a, tokyo))));
      const lit = waveOn ? Math.max(0, 1 - Math.abs(da - wave) / 0.25) : 0;
      ctx.strokeStyle = lit > 0 ? `rgba(${pal.dot},${0.12 + lit * 0.5})` : `rgba(${pal.dot},${0.08 * pa[2] + 0.04})`;
      ctx.beginPath(); ctx.moveTo(pa[0], pa[1]); ctx.lineTo(pb[0], pb[1]); ctx.stroke();
    }

    for (const p of pts) {
      const q = proj(p);
      if (q[2] < -0.15) continue;
      const depth = (q[2] + 0.15) / 1.15;
      const d = Math.acos(Math.max(-1, Math.min(1, dot(p, tokyo))));
      const lit = waveOn ? Math.max(0, 1 - Math.abs(d - wave) / 0.14) : 0;
      if (lit > 0.05) {
        ctx.fillStyle = d < 0.8 ? pal.pink : d < 1.8 ? pal.purple : pal.cyan;
        ctx.globalAlpha = lit * depth;
        ctx.beginPath(); ctx.arc(q[0], q[1], 1.2 + lit * 1.6, 0, Math.PI * 2); ctx.fill();
        ctx.globalAlpha = 1;
      } else {
        ctx.fillStyle = `rgba(${pal.dot},${0.1 + depth * 0.35})`;
        ctx.fillRect(q[0] - 0.8, q[1] - 0.8, 1.6, 1.6);
      }
    }

    // Tokyo - Hanoi arc, lifted off the surface, with a packet travelling along it.
    const T = proj(tokyo), N = proj(hanoi);
    const mid = [(tokyo[0] + hanoi[0]) / 2, (tokyo[1] + hanoi[1]) / 2, (tokyo[2] + hanoi[2]) / 2];
    const ml = Math.hypot(mid[0], mid[1], mid[2]);
    const M = proj(mid.map(v => (v / ml) * 1.18));
    const grad = ctx.createLinearGradient(T[0], T[1], N[0], N[1]);
    grad.addColorStop(0, pal.pink); grad.addColorStop(0.5, pal.purple); grad.addColorStop(1, pal.cyan);
    ctx.strokeStyle = grad; ctx.lineWidth = 2;
    ctx.beginPath(); ctx.moveTo(T[0], T[1]); ctx.quadraticCurveTo(M[0], M[1], N[0], N[1]); ctx.stroke();
    if (!reduce) {
      const k = (t % 1.8) / 1.8;
      const px = (1 - k) * (1 - k) * T[0] + 2 * (1 - k) * k * M[0] + k * k * N[0];
      const py = (1 - k) * (1 - k) * T[1] + 2 * (1 - k) * k * M[1] + k * k * N[1];
      ctx.fillStyle = pal.purple;
      ctx.beginPath(); ctx.arc(px, py, 3, 0, Math.PI * 2); ctx.fill();
    }

    // City markers: Tokyo pulses when a deploy goes out.
    const ring = reduce ? 0 : Math.max(0, 1 - (t % PULSE_EVERY) / 1.2);
    for (const [P, name, colour, pulse] of [[T, 'Tokyo', pal.pink, ring], [N, 'Hanoi', pal.cyan, 0]]) {
      if (pulse > 0) {
        ctx.strokeStyle = colour; ctx.globalAlpha = pulse; ctx.lineWidth = 1.5;
        ctx.beginPath(); ctx.arc(P[0], P[1], 6 + (1 - pulse) * 22, 0, Math.PI * 2); ctx.stroke();
        ctx.globalAlpha = 1;
      }
      ctx.fillStyle = colour;
      ctx.beginPath(); ctx.arc(P[0], P[1], 5, 0, Math.PI * 2); ctx.fill();
      ctx.font = '600 13px Outfit, "Noto Sans JP", sans-serif';
      ctx.fillStyle = pal.text;
      ctx.fillText(name, P[0] + 10, P[1] - 8);
    }
  }

  const loop = now => { raf = 0; draw(now); if (visible && !reduce) raf = requestAnimationFrame(loop); };
  host.addEventListener('pointermove', e => {
    const r = host.getBoundingClientRect();
    targetX = ((e.clientX - r.left) / r.width - 0.5) * 2;
    targetY = ((e.clientY - r.top) / r.height - 0.5) * 2;
  });
  host.addEventListener('pointerleave', () => { targetX = 0; targetY = 0; });
  new ResizeObserver(resize).observe(host);
  new IntersectionObserver(([e]) => { visible = e.isIntersecting; if (visible && !raf && !reduce) raf = requestAnimationFrame(loop); }).observe(host);
  resize();
})();
