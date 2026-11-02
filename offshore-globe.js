/*
 * Dotted globe for the top-page offshore section, turned toward Japan and Vietnam (replaces the flat map while it runs).
 * Dots sit only on land, so the continents read; Japan and Vietnam are coloured and linked by an arc,
 * and a pulse spreads out from Tokyo every few seconds.
 * Land mask: Natural Earth 1:50m land (public domain) via world-atlas (ISC), sampled once onto the dot grid below.
 * The JAPAN / VIETNAM tags from the HTML stay on top. Canvas 2D, no libraries.
 */
(() => {
  const host = document.querySelector('[data-network-globe]');
  if (!host) return;
  const canvas = document.createElement('canvas');
  canvas.setAttribute('aria-hidden', 'true');
  Object.assign(canvas.style, { position: 'absolute', inset: '0', width: '100%', height: '100%', display: 'block' });
  const ctx = canvas.getContext('2d');
  if (!ctx) return;
  canvas.style.maxWidth = 'none';
  host.prepend(canvas);
  // Hide the flat map; the tags stay.
  const hideMap = document.createElement('style');
  hideMap.textContent = '[data-network-globe] > svg { display: none; }';
  document.head.appendChild(hideMap);

  const reduce = window.matchMedia('(prefers-reduced-motion: reduce)').matches;
  const RAD = Math.PI / 180;
  const PULSE_EVERY = 3.2;   // seconds between deploy pulses
  const PULSE_TIME = 2.6;    // seconds for a pulse to cross half the globe
  const CENTER_LON = 122;    // keeps Japan and Vietnam facing the viewer
  const CENTER_LAT = 18;

  const unit = (lat, lon) => [Math.cos(lat * RAD) * Math.sin(lon * RAD), Math.sin(lat * RAD), Math.cos(lat * RAD) * Math.cos(lon * RAD)];
  const dot = (a, b) => a[0] * b[0] + a[1] * b[1] + a[2] * b[2];

  // Dots on a Fibonacci sphere; LAND marks which of them fall on land (one bit per dot).
  const POINTS = 12000;
  const LAND = 'AAAAAAAAAQEhMCQEgIQAElASAmpCKgyAGQkwABQG4MQMmIk7I3Dm///UmVkzm2dP/+q01p7W0lpbWktLa2mtLa21pbS0luy5/z+3p/7+1N6+23N/e2rv362pvT81p+b21N6/G1Nzf0pOzskpuTOnp+bstJyYc1Nyd05PzJlpuTvnJ+TsvJyYczNyZs5OyNk5OSPn5+TsvJ2es/Nydt7Oydk5Oyvn5+XsnJ2Vs3NyVk7Oy9k5OS9n5+2snJyVk/N2Vs7Oy1k5OS9n5+SsnJyVs3NyVs6Oi1k5OStmx+SsnJ0VM3NyXkyOiFk5OSsmxuWMmBwVs/JyRkyMihk5OSsnZ+WMnBiVM3JyTkbOyhk5OSInZMWMjBiVE3JyTkbMyhkZMSInZOWMnJiVkzJiTE7IiFkZMSMm5MS8iJARszJiXk7IiFkZMSsmZcSsmJAVkzJCVkzIiFkZISsmZeSsmJQXkzJCVkzKSlk5KSsnZYSsnJSVkzJSUk7KSFk5KSsnZaSknJSUs3JSUk7KSEk5KSklZaSgnJSUkmJSUkrKSkE5KSlFZaSknJSUgnJSUg7KSkE5KCklRaSkFJSUgnJQUgqKSkkpKCklZaCklJSVkhJQUsrKQkkJKCklZaCklASVshJQUkLCQFkJCAslZaCkhISFshJQUkLCUEkJCAolJaCkhISjshIUFEpCQFkJCAslJaCohISAshIQFEpCQFgJCA0lISAoFISAshIQEspCQEgpCAllJSAkFIWAkBIQGopCQEgoCAEFJSA0FIWAgFIQEgJCQEgoCkEBJSA0hISAkFAQgkJKQEgoCkEhJSAEhYSAkFQUAkpKUAgKCEEhKSgEhZSA0BQQgkJaQCgKCUEhKSAEhYSAUBQQgkJSQAgqKUEhKCAEhaSAEBSQgkpQAAgKQQEhKAAVlaQAEFSAikJQAAgKQQEgKAAVhaAAEBSAikBQACoqQQEgKAAVhaAAFFSAikBQASoKQAWgqAAVgaAAFBSAikBQASoKRAEoqBAVgaAAFBSAglBRASoKQAGoKAAVoaBCFBSAAlFQICpCQIUoKBEFo6BCFISAAlFRAApGQIUoKAEFo6AEFISAAlFwAgpGQQEoCAEVoqAEFIyAAlAQAipEQQkoGAEFoqAEVISKAlARAgpERQkoCAEFoKAEFICCAlAwAgpARQkoCAUFoCAEFICCAlAQAgpAQQkoAAUFoCAEFICCAlEAAgpAQYkoEAUFoiAEFICCAlEACgpAQQgoEAWFogBEFICCAlEgCgpEQYgoAAWFokBEHogCUlEgCgpEAYgoEAWFokBEFIgCEFEgCgpFgYgoEAWEokBEFIgCEFEgIgpFgYgoEAWgokBEFIgCEVEgKghFgYgoEBWiokBEFIgCEVEgKgRFgYgoEBUCokBUFIoCAVEgKgRFgYgoEBUCokBECIgCAVEgKgREgYg4EAUCokBUCIgCAVEgKgREgYgYEAUCokBUCIgCATEgCgREgYgQEAUCokBUCIgCATEgCgREgYgQEAUCIkAUCIgCATEACgREgYgQAAUCIgAECIACACEACgRAAAgQAAECIAAECIAAACAAAoRAAAAQAAEAIAAECIEAACAAAgRAAAgQAAEAIAAEAIAAAAAAAgBAAAAAAgEAAAAAAIAAAAAAAgBAAAAAAgEAQAAAAIEAAAAAAgAAAAAAAAEAAAAAAIEgAAAAAoBAAAAAAAEAAAAAAIEAAAAAAgAAAAAAAAEAAAAEAAAAAAAAAgAAAAAAAAEAAAAAAAAAAAAAAgAAAAAAAAEAAAAAAAAAAAAAAgAAAAAAAAAAAACEAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAACAgAESkgIAQkBICUkJKCkhJOSkhJcWkpLSUlpbD0lpa2ktLeXk9L+/n5/38vp/f8/P6ft/P6/l7P//v//8DAAAA';
  const bits = atob(LAND);
  const pts = [];
  const golden = Math.PI * (3 - Math.sqrt(5));
  const inBox = (lat, lon, b) => lat >= b[0] && lat <= b[1] && lon >= b[2] && lon <= b[3];
  const JAPAN = [30, 46, 128, 146.5], VIETNAM = [8, 23.5, 102, 110];
  for (let i = 0; i < POINTS; i++) {
    if (!(bits.charCodeAt(i >> 3) & (1 << (i & 7)))) continue;
    const y = 1 - (i / (POINTS - 1)) * 2;
    const r = Math.sqrt(1 - y * y);
    const p = [Math.cos(golden * i) * r, y, Math.sin(golden * i) * r];
    const lat = Math.asin(y) / RAD, lon = Math.atan2(p[0], p[2]) / RAD;
    p.tag = inBox(lat, lon, JAPAN) ? 'jp' : inBox(lat, lon, VIETNAM) ? 'vn' : '';
    pts.push(p);
  }
  const tokyo = unit(35.68, 139.69);
  const hanoi = unit(21.03, 105.85);

  let W = 0, H = 0, R = 0, dpr = 1, raf = 0, visible = false, start = performance.now();
  let leanX = 0, leanY = 0, targetX = 0, targetY = 0;

  const resize = () => {
    dpr = Math.min(window.devicePixelRatio || 1, 2);
    W = host.clientWidth; H = host.clientHeight;
    canvas.width = Math.round(W * dpr); canvas.height = Math.round(H * dpr);
    R = Math.min(W, H) * 0.46;
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
    // Ocean: a faint disc with an outline so the globe reads as a sphere.
    ctx.fillStyle = `rgba(${pal.dot},0.035)`;
    ctx.beginPath(); ctx.arc(cx, cy, R, 0, Math.PI * 2); ctx.fill();
    ctx.strokeStyle = `rgba(${pal.dot},0.12)`; ctx.lineWidth = 1;
    ctx.stroke();

    for (const p of pts) {
      const q = proj(p);
      if (q[2] < 0.02) continue;
      const depth = 0.35 + 0.65 * q[2];
      const d = Math.acos(Math.max(-1, Math.min(1, dot(p, tokyo))));
      const lit = waveOn ? Math.max(0, 1 - Math.abs(d - wave) / 0.14) : 0;
      if (p.tag) {
        ctx.fillStyle = p.tag === 'jp' ? pal.cyan : pal.pink;
        ctx.globalAlpha = 0.95;
        ctx.beginPath(); ctx.arc(q[0], q[1], 1.6, 0, Math.PI * 2); ctx.fill();
      } else if (lit > 0.05) {
        ctx.fillStyle = pal.purple;
        ctx.globalAlpha = (0.35 + lit * 0.5) * depth;
        ctx.beginPath(); ctx.arc(q[0], q[1], 1.1 + lit * 0.8, 0, Math.PI * 2); ctx.fill();
      } else {
        ctx.fillStyle = `rgb(${pal.dot})`;
        ctx.globalAlpha = 0.18 + depth * 0.32;
        ctx.fillRect(q[0] - 0.9, q[1] - 0.9, 1.8, 1.8);
      }
    }
    ctx.globalAlpha = 1;

    // Tokyo - Hanoi arc, lifted off the surface, with a packet travelling along it.
    const T = proj(tokyo), N = proj(hanoi);
    const mid = [(tokyo[0] + hanoi[0]) / 2, (tokyo[1] + hanoi[1]) / 2, (tokyo[2] + hanoi[2]) / 2];
    const ml = Math.hypot(mid[0], mid[1], mid[2]);
    const M = proj(mid.map(v => (v / ml) * 1.18));
    const grad = ctx.createLinearGradient(T[0], T[1], N[0], N[1]);
    grad.addColorStop(0, pal.cyan); grad.addColorStop(0.5, pal.purple); grad.addColorStop(1, pal.pink);
    ctx.strokeStyle = grad; ctx.lineWidth = 2;
    ctx.beginPath(); ctx.moveTo(T[0], T[1]); ctx.quadraticCurveTo(M[0], M[1], N[0], N[1]); ctx.stroke();
    if (!reduce) {
      const k = (t % 1.8) / 1.8;
      const px = (1 - k) * (1 - k) * T[0] + 2 * (1 - k) * k * M[0] + k * k * N[0];
      const py = (1 - k) * (1 - k) * T[1] + 2 * (1 - k) * k * M[1] + k * k * N[1];
      ctx.fillStyle = pal.purple;
      ctx.beginPath(); ctx.arc(px, py, 3, 0, Math.PI * 2); ctx.fill();
    }

    // Markers in the tag colours (Japan cyan, Vietnam pink); Japan pulses when the wave goes out.
    const ring = reduce ? 0 : Math.max(0, 1 - (t % PULSE_EVERY) / 1.2);
    for (const [P, colour, pulse] of [[T, pal.cyan, ring], [N, pal.pink, 0]]) {
      if (pulse > 0) {
        ctx.strokeStyle = colour; ctx.globalAlpha = pulse; ctx.lineWidth = 1.5;
        ctx.beginPath(); ctx.arc(P[0], P[1], 6 + (1 - pulse) * 22, 0, Math.PI * 2); ctx.stroke();
        ctx.globalAlpha = 1;
      }
      ctx.fillStyle = colour;
      ctx.beginPath(); ctx.arc(P[0], P[1], 5, 0, Math.PI * 2); ctx.fill();
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
