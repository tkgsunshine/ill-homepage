/*
 * Ghostly orb behind the top-page hero, wrapped in drifting smoke, lit in the brand cyan, purple and pink.
 * Wide screens: the orb sits where the hero illustration was (that illustration is hidden while the orb runs).
 * Narrow screens: a softer orb in the upper right, behind the text.
 * The pointer swings the lighting. Resolution drops automatically on slow devices.
 * Written for Ill inc. after the React Bits Pro "Specter Orb" description; no code from it is used. Plain WebGL.
 */
(() => {
  const hero = document.querySelector('[data-specter-orb]');
  if (!hero) return;
  const canvas = document.createElement('canvas');
  canvas.setAttribute('aria-hidden', 'true');
  Object.assign(canvas.style, {
    position: 'absolute', inset: '0', width: '100%', height: '100%', maxWidth: 'none',
    zIndex: '-1', pointerEvents: 'none', display: 'block'
  });
  const gl = canvas.getContext('webgl', { premultipliedAlpha: true, alpha: true, antialias: false });
  if (!gl) return;

  const vs = 'attribute vec2 p; void main(){ gl_Position = vec4(p, 0.0, 1.0); }';
  const fs = `
    precision highp float;
    uniform vec2 uRes; uniform vec2 uCenter; uniform float uSize; uniform float uTime; uniform vec2 uPointer;
    uniform vec3 uKey; uniform vec3 uFill; uniform vec3 uAmb; uniform vec3 uSpecA; uniform vec3 uSpecB;
    uniform float uOpacity; uniform float uLight;
    const float R = 0.36;      // core radius
    const float TURB = 0.2;    // how far the smoke pushes the surface out
    float h(vec3 p){ p = fract(p * 0.3183099 + 0.1); p *= 17.0; return fract(p.x * p.y * p.z * (p.x + p.y + p.z)); }
    float n(vec3 x){ vec3 i = floor(x), f = fract(x); f = f*f*(3.0-2.0*f);
      return mix(mix(mix(h(i), h(i+vec3(1,0,0)), f.x), mix(h(i+vec3(0,1,0)), h(i+vec3(1,1,0)), f.x), f.y),
                 mix(mix(h(i+vec3(0,0,1)), h(i+vec3(1,0,1)), f.x), mix(h(i+vec3(0,1,1)), h(i+vec3(1,1,1)), f.x), f.y), f.z); }
    float fbm(vec3 p){ float a = 0.5, s = 0.0; for (int i = 0; i < 3; i++){ s += a * n(p); p *= 2.0; a *= 0.5; } return s / 0.875; }
    vec3 flow(){ return vec3(0.0, uTime * 0.3, uTime * 0.15); }
    float sdf(vec3 p){ return length(p) - R - TURB * fbm(p * 1.8 + flow()); }
    vec3 normal(vec3 p){ vec2 e = vec2(0.012, 0.0);
      return normalize(vec3(sdf(p+e.xyy)-sdf(p-e.xyy), sdf(p+e.yxy)-sdf(p-e.yxy), sdf(p+e.yyx)-sdf(p-e.yyx))); }
    void main(){
      vec2 uv = (gl_FragCoord.xy - uCenter) / uSize;
      float r = length(uv);
      // Halo and smoke around the silhouette, from the ray's closest approach to the centre.
      float wisp = fbm(vec3(uv * 2.6, 0.0) + flow() * 1.3);
      float edge = max(0.0, r - R - TURB * 0.45);
      float halo = exp(-edge * 7.0) * (0.45 + 0.75 * wisp) * smoothstep(1.2, 0.3, r);
      vec3 haloCol = mix(uFill, uKey, smoothstep(-0.6, 0.6, uv.x - uv.y)) ;
      vec4 col = vec4(haloCol * halo * 0.55, halo * 0.55);
      if (r < R + TURB + 0.02) {
        // Orthographic march through the displaced sphere.
        vec3 ro = vec3(uv, 1.0), rd = vec3(0.0, 0.0, -1.0);
        float t = 0.0; bool hit = false;
        for (int i = 0; i < 64; i++){
          float d = sdf(ro + rd * t);
          if (d < 0.004){ hit = true; break; }
          t += d * 0.55;
          if (t > 2.0) break;
        }
        if (hit){
          vec3 p = ro + rd * t, nn = normal(p), v = -rd;
          // Two opposing lights; the pointer swings them.
          vec3 l1 = normalize(vec3(-0.7 + uPointer.x * uLight * 2.0, 0.6 + uPointer.y * uLight * 2.0, 0.6));
          vec3 l2 = normalize(vec3(-l1.x, -l1.y, 0.4));
          float rim = pow(1.0 - max(dot(nn, v), 0.0), 3.0);
          vec3 c = uAmb * (0.18 + 0.12 * nn.y);
          c += uKey * max(dot(nn, l1), 0.0) * 0.55 + uFill * max(dot(nn, l2), 0.0) * 0.5;
          c += (uKey * max(dot(nn, l1), 0.0) + uFill * max(dot(nn, l2), 0.0)) * rim * 1.4;
          c += uSpecA * pow(max(dot(reflect(-l1, nn), v), 0.0), 12.0);
          c += uSpecB * pow(max(dot(reflect(-l2, nn), v), 0.0), 12.0) * 0.8;
          c = pow(c, vec3(1.0 / 1.25));
          // Ghostly: the body stays a little see-through, densest at the rim.
          float a = 0.5 + 0.5 * rim;
          col = vec4(c * a, a) + col * (1.0 - a);
        }
      }
      gl_FragColor = col * uOpacity;
    }`;
  const sh = (type, src) => { const s = gl.createShader(type); gl.shaderSource(s, src); gl.compileShader(s); return s; };
  const prog = gl.createProgram();
  gl.attachShader(prog, sh(gl.VERTEX_SHADER, vs));
  gl.attachShader(prog, sh(gl.FRAGMENT_SHADER, fs));
  gl.linkProgram(prog);
  if (!gl.getProgramParameter(prog, gl.LINK_STATUS)) return;
  gl.useProgram(prog);
  gl.bindBuffer(gl.ARRAY_BUFFER, gl.createBuffer());
  gl.bufferData(gl.ARRAY_BUFFER, new Float32Array([-1, -1, 3, -1, -1, 3]), gl.STATIC_DRAW);
  const loc = gl.getAttribLocation(prog, 'p');
  gl.enableVertexAttribArray(loc);
  gl.vertexAttribPointer(loc, 2, gl.FLOAT, false, 0, 0);
  const U = {};
  ['uRes', 'uCenter', 'uSize', 'uTime', 'uPointer', 'uKey', 'uFill', 'uAmb', 'uSpecA', 'uSpecB', 'uOpacity', 'uLight']
    .forEach(k => { U[k] = gl.getUniformLocation(prog, k); });

  // The old illustration keeps its place in the layout (the orb is centred on it) but is hidden.
  const visual = hero.querySelector('.hero-visual');
  const hideVisual = document.createElement('style');
  hideVisual.textContent = '[data-specter-orb] .hero-visual > * { visibility: hidden; }';
  document.head.appendChild(hideVisual);
  if (getComputedStyle(hero).position === 'static') hero.style.position = 'relative';
  hero.style.isolation = 'isolate';
  hero.prepend(canvas);

  const reduce = window.matchMedia('(prefers-reduced-motion: reduce)').matches;
  const rgb = css => {
    const c = document.createElement('canvas').getContext('2d');
    c.fillStyle = css; c.fillRect(0, 0, 1, 1);
    const d = c.getImageData(0, 0, 1, 1).data;
    return [d[0] / 255, d[1] / 255, d[2] / 255];
  };
  const mixc = (a, b, t) => a.map((v, i) => v + (b[i] - v) * t);
  let narrow = false;
  const colours = () => {
    const cs = getComputedStyle(document.body);
    const cyan = rgb(cs.getPropertyValue('--color-cyan').trim() || '#00c8ff');
    const purple = rgb(cs.getPropertyValue('--color-purple').trim() || '#8a14ff');
    const pink = rgb(cs.getPropertyValue('--color-pink').trim() || '#ff2e9b');
    const light = document.body.classList.contains('theme-light');
    gl.uniform3fv(U.uKey, cyan);
    gl.uniform3fv(U.uFill, purple);
    gl.uniform3fv(U.uAmb, mixc(cyan, purple, 0.5));
    gl.uniform3fv(U.uSpecA, mixc(cyan, [1, 1, 1], 0.5));
    gl.uniform3fv(U.uSpecB, pink);
    // Behind the text on narrow screens, so keep it soft there; a touch softer on the light theme.
    gl.uniform1f(U.uOpacity, (narrow ? 0.5 : 1) * (light ? 0.9 : 1));
  };

  let scale = 1;   // render resolution as a fraction of the capped device pixels
  const DPR = Math.min(window.devicePixelRatio || 1, 1.5);
  const layout = () => {
    const px = DPR * scale;
    canvas.width = Math.max(1, Math.round(hero.clientWidth * px));
    canvas.height = Math.max(1, Math.round(hero.clientHeight * px));
    gl.viewport(0, 0, canvas.width, canvas.height);
    gl.uniform2f(U.uRes, canvas.width, canvas.height);
    const hb = hero.getBoundingClientRect();
    const vb = visual && visual.getBoundingClientRect();
    narrow = !vb || vb.width === 0;
    let cx, cy, size;
    if (!narrow) {
      cx = vb.left - hb.left + vb.width / 2;
      cy = vb.top - hb.top + vb.height / 2;
      size = Math.min(vb.width, vb.height) * 0.62;
    } else {
      cx = hb.width * 0.86;
      cy = hb.height * 0.27;
      size = hb.width * 0.4;
    }
    gl.uniform2f(U.uCenter, cx * px, canvas.height - cy * px);
    gl.uniform1f(U.uSize, size * px);
    colours();
  };

  let raf = 0, visible = true, t0 = performance.now(), frames = 0, slow = 0, lastFrame = 0;
  const pointer = [0, 0], target = [0, 0];
  gl.uniform1f(U.uLight, 0.35);
  const draw = now => {
    pointer[0] += (target[0] - pointer[0]) * 0.05;
    pointer[1] += (target[1] - pointer[1]) * 0.05;
    gl.uniform1f(U.uTime, reduce ? 4 : (now - t0) / 1000);
    gl.uniform2fv(U.uPointer, pointer);
    gl.drawArrays(gl.TRIANGLES, 0, 3);
  };
  const loop = now => {
    raf = 0;
    // Adaptive quality: after a few slow frames in a row, render fewer pixels.
    if (lastFrame) {
      const dt = now - lastFrame;
      slow = dt > 24 ? slow + 1 : Math.max(0, slow - 1);
      if (slow > 20 && scale > 0.45) { scale *= 0.8; slow = 0; layout(); }
    }
    lastFrame = now;
    frames++;
    draw(now);
    if (visible && !reduce) raf = requestAnimationFrame(loop);
  };
  new MutationObserver(() => { colours(); if (!raf) draw(performance.now()); })
    .observe(document.body, { attributes: true, attributeFilter: ['class'] });
  window.addEventListener('pointermove', e => {
    const r = hero.getBoundingClientRect();
    if (e.clientY > r.bottom) return;
    target[0] = ((e.clientX - r.left) / r.width) * 2 - 1;
    target[1] = 1 - ((e.clientY - r.top) / r.height) * 2;
  }, { passive: true });
  new ResizeObserver(() => { layout(); if (!raf) draw(performance.now()); }).observe(hero);
  new IntersectionObserver(([e]) => {
    visible = e.isIntersecting;
    lastFrame = 0;
    if (visible && !raf && !reduce) raf = requestAnimationFrame(loop);
  }).observe(hero);
  layout();
  draw(performance.now());
})();
