/*
 * Flowing mesh gradient behind the top-page hero, in the brand pink, purple and cyan.
 * Soft colour fields drift and fold into each other; the pointer gently pulls the nearest field.
 * Written for Ill inc. after the React Bits Pro "Hero 22" block description; no code from it is used. Plain WebGL.
 */
(() => {
  const hero = document.querySelector('[data-mesh-gradient]');
  if (!hero) return;
  const canvas = document.createElement('canvas');
  canvas.setAttribute('aria-hidden', 'true');
  Object.assign(canvas.style, {
    position: 'absolute', inset: '0', width: '100%', height: '100%', maxWidth: 'none',
    zIndex: '-1', pointerEvents: 'none', display: 'block'
  });
  const gl = canvas.getContext('webgl', { premultipliedAlpha: false, alpha: true, antialias: false });
  if (!gl) return;
  if (getComputedStyle(hero).position === 'static') hero.style.position = 'relative';
  hero.style.isolation = 'isolate';
  hero.style.overflow = 'hidden';
  hero.prepend(canvas);

  const reduce = window.matchMedia('(prefers-reduced-motion: reduce)').matches;
  const vs = 'attribute vec2 p; void main(){ gl_Position = vec4(p, 0.0, 1.0); }';
  const fs = `
    precision mediump float;
    uniform vec2 uRes; uniform float uTime; uniform vec2 uPointer;
    uniform vec3 uBg; uniform vec3 uC1; uniform vec3 uC2; uniform vec3 uC3; uniform float uStrength;
    // Smooth value noise for the folding flow.
    float h(vec2 p){ return fract(sin(dot(p, vec2(127.1, 311.7))) * 43758.5453); }
    float n(vec2 p){ vec2 i = floor(p), f = fract(p); f = f*f*(3.0-2.0*f);
      return mix(mix(h(i), h(i+vec2(1,0)), f.x), mix(h(i+vec2(0,1)), h(i+vec2(1,1)), f.x), f.y); }
    void main(){
      vec2 uv = gl_FragCoord.xy / uRes;
      vec2 q = uv * vec2(uRes.x / uRes.y, 1.0);
      float t = uTime * 0.06;
      // Warp the space so the fields fold like silk.
      vec2 w = q + 0.35 * vec2(n(q * 1.6 + t), n(q * 1.6 - t + 4.0));
      vec2 a = vec2(0.25 + 0.15 * sin(t * 1.3), 0.75 + 0.12 * cos(t * 1.1));
      vec2 b = vec2(0.95 + 0.20 * cos(t * 0.9), 0.30 + 0.15 * sin(t * 1.4));
      vec2 c = vec2(1.45 + 0.15 * sin(t * 1.2 + 2.0), 0.80 + 0.12 * sin(t * 0.8));
      vec2 m = uPointer * vec2(uRes.x / uRes.y, 1.0);
      b = mix(b, m, 0.18);
      float fa = exp(-3.2 * dot(w - a, w - a));
      float fb = exp(-3.0 * dot(w - b, w - b));
      float fc = exp(-3.2 * dot(w - c, w - c));
      vec3 col = uBg;
      col = mix(col, uC1, fa * uStrength);
      col = mix(col, uC2, fb * uStrength);
      col = mix(col, uC3, fc * uStrength);
      col += (h(gl_FragCoord.xy + uTime) - 0.5) * 0.015;   // fine grain against banding
      // Fade out at the bottom so the next section joins cleanly whatever its background.
      gl_FragColor = vec4(col, smoothstep(0.0, 0.35, uv.y));
    }`;
  const sh = (type, src) => { const s = gl.createShader(type); gl.shaderSource(s, src); gl.compileShader(s); return s; };
  const prog = gl.createProgram();
  gl.attachShader(prog, sh(gl.VERTEX_SHADER, vs));
  gl.attachShader(prog, sh(gl.FRAGMENT_SHADER, fs));
  gl.linkProgram(prog);
  if (!gl.getProgramParameter(prog, gl.LINK_STATUS)) { canvas.remove(); return; }
  gl.useProgram(prog);
  gl.bindBuffer(gl.ARRAY_BUFFER, gl.createBuffer());
  gl.bufferData(gl.ARRAY_BUFFER, new Float32Array([-1, -1, 3, -1, -1, 3]), gl.STATIC_DRAW);
  const loc = gl.getAttribLocation(prog, 'p');
  gl.enableVertexAttribArray(loc);
  gl.vertexAttribPointer(loc, 2, gl.FLOAT, false, 0, 0);
  const U = {};
  ['uRes', 'uTime', 'uPointer', 'uBg', 'uC1', 'uC2', 'uC3', 'uStrength'].forEach(k => { U[k] = gl.getUniformLocation(prog, k); });

  const rgb = css => {
    const c = document.createElement('canvas').getContext('2d');
    c.fillStyle = css; c.fillRect(0, 0, 1, 1);
    const d = c.getImageData(0, 0, 1, 1).data;
    return [d[0] / 255, d[1] / 255, d[2] / 255];
  };
  const colours = () => {
    const cs = getComputedStyle(document.body);
    const light = document.body.classList.contains('theme-light');
    gl.uniform3fv(U.uBg, rgb(cs.getPropertyValue('--bg-dark').trim() || (light ? '#f1f3f9' : '#05070f')));
    gl.uniform3fv(U.uC1, rgb(cs.getPropertyValue('--color-pink').trim() || '#ff2e9b'));
    gl.uniform3fv(U.uC2, rgb(cs.getPropertyValue('--color-purple').trim() || '#8a14ff'));
    gl.uniform3fv(U.uC3, rgb(cs.getPropertyValue('--color-cyan').trim() || '#00c8ff'));
    // Pastel on the light theme so the heading stays readable; deeper glow on dark.
    gl.uniform1f(U.uStrength, light ? 0.32 : 0.45);
  };

  let raf = 0, visible = true, t0 = performance.now();
  const pointer = [0.6, 0.5], target = [0.6, 0.5];
  const draw = now => {
    pointer[0] += (target[0] - pointer[0]) * 0.04;
    pointer[1] += (target[1] - pointer[1]) * 0.04;
    gl.uniform1f(U.uTime, reduce ? 8 : (now - t0) / 1000);
    gl.uniform2fv(U.uPointer, pointer);
    gl.drawArrays(gl.TRIANGLES, 0, 3);
  };
  const loop = now => { raf = 0; draw(now); if (visible && !reduce) raf = requestAnimationFrame(loop); };
  const resize = () => {
    const dpr = Math.min(window.devicePixelRatio || 1, 1.5);   // a soft gradient needs few pixels
    canvas.width = Math.max(1, Math.round(hero.clientWidth * dpr));
    canvas.height = Math.max(1, Math.round(hero.clientHeight * dpr));
    gl.viewport(0, 0, canvas.width, canvas.height);
    gl.uniform2f(U.uRes, canvas.width, canvas.height);
    if (!raf) draw(performance.now());
  };
  colours();
  new MutationObserver(() => { colours(); if (!raf) draw(performance.now()); }).observe(document.body, { attributes: true, attributeFilter: ['class'] });
  hero.addEventListener('pointermove', e => {
    const r = hero.getBoundingClientRect();
    target[0] = (e.clientX - r.left) / r.width;
    target[1] = 1 - (e.clientY - r.top) / r.height;
  });
  new ResizeObserver(resize).observe(hero);
  new IntersectionObserver(([e]) => { visible = e.isIntersecting; if (visible && !raf && !reduce) raf = requestAnimationFrame(loop); }).observe(hero);
  resize();
})();
