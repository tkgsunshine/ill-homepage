/*
 * Photon knot for the philosophy section: a translucent ribbon of light tied into a slowly turning trefoil knot.
 * The ribbon draws itself in when it scrolls into view, leans toward the pointer, and can be dragged to spin.
 * Written for Ill inc. after React Bits Pro "Photon Knot"; no code from that component is used. Plain WebGL, no libraries.
 */
(() => {
  const host = document.querySelector('[data-photon-knot]');
  if (!host) return;
  const canvas = document.createElement('canvas');
  canvas.setAttribute('aria-hidden', 'true');
  Object.assign(canvas.style, { position: 'absolute', inset: '0', width: '100%', height: '100%', display: 'block', touchAction: 'pan-y' });
  const gl = canvas.getContext('webgl', { premultipliedAlpha: true, alpha: true, antialias: true });
  if (!gl) return;
  host.appendChild(canvas);
  host.querySelector('.photon-knot-fallback')?.remove();

  const reduce = window.matchMedia('(prefers-reduced-motion: reduce)').matches;
  const SEGMENTS = 900;
  const TWISTS = 4;        // half-turns of twist along the ribbon
  const WIDTH = 0.34;      // ribbon width relative to the knot
  const TILT = 32 * Math.PI / 180;

  // Trefoil centre line, normalised to roughly unit radius.
  const curve = t => [
    (Math.sin(t) + 2 * Math.sin(2 * t)) / 3,
    (Math.cos(t) - 2 * Math.cos(2 * t)) / 3,
    -Math.sin(3 * t) / 3
  ];
  const sub = (a, b) => [a[0] - b[0], a[1] - b[1], a[2] - b[2]];
  const cross = (a, b) => [a[1] * b[2] - a[2] * b[1], a[2] * b[0] - a[0] * b[2], a[0] * b[1] - a[1] * b[0]];
  const dot = (a, b) => a[0] * b[0] + a[1] * b[1] + a[2] * b[2];
  const norm = a => { const l = Math.hypot(a[0], a[1], a[2]) || 1; return [a[0] / l, a[1] / l, a[2] / l]; };

  // Parallel-transport frames so the ribbon does not twist on its own, then close the seam evenly.
  const pts = [], tans = [];
  for (let i = 0; i <= SEGMENTS; i++) {
    const t = (i / SEGMENTS) * Math.PI * 2;
    pts.push(curve(t));
    tans.push(norm(sub(curve(t + 1e-3), curve(t - 1e-3))));
  }
  const normals = [norm(cross(tans[0], [0, 0, 1]))];
  for (let i = 1; i <= SEGMENTS; i++) {
    const n = normals[i - 1];
    const tt = tans[i];
    normals.push(norm(sub(n, tt.map(v => v * dot(n, tt)))));
  }
  const b0 = cross(tans[0], normals[0]);
  const seam = Math.atan2(dot(normals[SEGMENTS], b0), dot(normals[SEGMENTS], normals[0]));

  const data = [];
  for (let i = 0; i <= SEGMENTS; i++) {
    const s = i / SEGMENTS;
    const tt = tans[i], n = normals[i], b = cross(tt, n);
    const a = -seam * s + TWISTS * Math.PI * s * 0.5;
    const ca = Math.cos(a), sa = Math.sin(a);
    const w = [n[0] * ca + b[0] * sa, n[1] * ca + b[1] * sa, n[2] * ca + b[2] * sa];   // across the ribbon
    const face = cross(tt, w);                                                          // ribbon surface normal
    for (const side of [-1, 1]) {
      const h = (WIDTH / 2) * side;
      data.push(pts[i][0] + w[0] * h, pts[i][1] + w[1] * h, pts[i][2] + w[2] * h, s, side, face[0], face[1], face[2]);
    }
  }
  const buf = gl.createBuffer();
  gl.bindBuffer(gl.ARRAY_BUFFER, buf);
  gl.bufferData(gl.ARRAY_BUFFER, new Float32Array(data), gl.STATIC_DRAW);

  const vs = `
    attribute vec3 aPos; attribute float aS; attribute float aSide; attribute vec3 aNormal;
    uniform mat3 uRot; uniform float uAspect; uniform float uScale; uniform vec2 uOffset;
    varying float vS; varying float vSide; varying float vFacing; varying float vDepth;
    void main() {
      vec3 p = uRot * aPos;
      vec3 n = normalize(uRot * aNormal);
      float persp = 1.0 / (1.0 - p.z * 0.35);
      vS = aS; vSide = aSide; vFacing = abs(n.z); vDepth = p.z;
      gl_Position = vec4(p.x * uScale * persp / uAspect + uOffset.x, p.y * uScale * persp + uOffset.y, 0.0, 1.0);
    }`;
  const fs = `
    precision mediump float;
    uniform vec3 uC1; uniform vec3 uC2; uniform vec3 uC3;
    uniform float uTime; uniform float uDraw; uniform vec2 uLight; uniform float uDark;
    varying float vS; varying float vSide; varying float vFacing; varying float vDepth;
    void main() {
      if (vS > uDraw) discard;
      float k = 0.5 + 0.5 * sin(6.2831 * (vS * 2.0 - uTime * 0.08));
      vec3 col = k < 0.5 ? mix(uC1, uC2, k * 2.0) : mix(uC2, uC3, k * 2.0 - 1.0);
      float edge = smoothstep(0.72, 1.0, abs(vSide));
      float fold = pow(1.0 - vFacing, 3.0);
      float sheen = pow(max(0.0, 1.0 - length(vec2(vSide * 0.4, vFacing) - uLight)), 4.0);
      float near = mix(0.45, 1.0, smoothstep(-0.6, 0.6, vDepth));
      float a = (0.16 + edge * 0.55 + fold * 0.5 + sheen * 0.35) * near;
      vec3 lit = col + vec3(1.0) * (edge * 0.35 + sheen * 0.45) * uDark;
      a = clamp(a, 0.0, 0.95);
      gl_FragColor = vec4(lit * a, a);
    }`;
  const compile = (type, src) => { const s = gl.createShader(type); gl.shaderSource(s, src); gl.compileShader(s); return s; };
  const prog = gl.createProgram();
  gl.attachShader(prog, compile(gl.VERTEX_SHADER, vs));
  gl.attachShader(prog, compile(gl.FRAGMENT_SHADER, fs));
  gl.linkProgram(prog);
  if (!gl.getProgramParameter(prog, gl.LINK_STATUS)) { canvas.remove(); return; }
  gl.useProgram(prog);
  const stride = 8 * 4;
  [['aPos', 3, 0], ['aS', 1, 3], ['aSide', 1, 4], ['aNormal', 3, 5]].forEach(([name, size, off]) => {
    const loc = gl.getAttribLocation(prog, name);
    gl.enableVertexAttribArray(loc);
    gl.vertexAttribPointer(loc, size, gl.FLOAT, false, stride, off * 4);
  });
  const u = name => gl.getUniformLocation(prog, name);
  const U = { offset: u('uOffset'), rot: u('uRot'), aspect: u('uAspect'), scale: u('uScale'), c1: u('uC1'), c2: u('uC2'), c3: u('uC3'),
    time: u('uTime'), draw: u('uDraw'), light: u('uLight'), dark: u('uDark') };
  gl.enable(gl.BLEND);
  gl.blendFunc(gl.ONE, gl.ONE_MINUS_SRC_ALPHA);
  gl.disable(gl.DEPTH_TEST);

  const toRgb = css => {
    const c = document.createElement('canvas').getContext('2d');
    c.fillStyle = css; c.fillRect(0, 0, 1, 1);
    const d = c.getImageData(0, 0, 1, 1).data;
    return [d[0] / 255, d[1] / 255, d[2] / 255];
  };
  const colours = () => {
    const root = getComputedStyle(document.body);
    gl.uniform3fv(U.c1, toRgb(root.getPropertyValue('--color-pink').trim() || '#ff2e9b'));
    gl.uniform3fv(U.c2, toRgb(root.getPropertyValue('--color-purple').trim() || '#8a14ff'));
    gl.uniform3fv(U.c3, toRgb(root.getPropertyValue('--color-cyan').trim() || '#00c8ff'));
    gl.uniform1f(U.dark, document.body.classList.contains('theme-light') ? 0.0 : 1.0);
  };
  colours();
  new MutationObserver(() => { colours(); if (!raf) draw(performance.now()); }).observe(document.body, { attributes: true, attributeFilter: ['class'] });

  const resize = () => {
    const dpr = Math.min(window.devicePixelRatio || 1, 2);
    const w = host.clientWidth, h = host.clientHeight;
    canvas.width = Math.max(1, Math.round(w * dpr));
    canvas.height = Math.max(1, Math.round(h * dpr));
    gl.viewport(0, 0, canvas.width, canvas.height);
    gl.uniform1f(U.aspect, w / Math.max(1, h));
    // The top-left of this card sits under the philosophy card, so the knot is set toward the open lower right.
    gl.uniform1f(U.scale, 0.5);
    gl.uniform2fv(U.offset, [0.14, -0.16]);
    if (!raf) draw(performance.now());
  };

  // Rotation: slow turn around Y, backward tilt, lean toward the pointer, plus drag spin with momentum.
  let angle = 0, spin = 0, leanX = 0, leanY = 0, targetX = 0, targetY = 0, drawn = reduce ? 1 : 0;
  let raf = 0, last = 0, time = 0, visible = false, dragging = false, lastX = 0;
  const light = [0.5, 0.6];
  const mat = (ax, ay) => {
    const cx = Math.cos(ax), sx = Math.sin(ax), cy = Math.cos(ay), sy = Math.sin(ay);
    return new Float32Array([cy, sx * sy, -cx * sy, 0, cx, sx, sy, -sx * cy, cx * cy]);
  };

  function draw(now) {
    const dt = Math.min(0.05, Math.max(0, (now - last) / 1000));
    last = now;
    if (!reduce) {
      time += dt;
      drawn = Math.min(1, drawn + dt / 1.6);
      if (!dragging) { spin *= Math.pow(0.15, dt); angle += (0.5 * 0.6 + spin) * dt; }
      leanX += (targetX - leanX) * Math.min(1, dt * 4);
      leanY += (targetY - leanY) * Math.min(1, dt * 4);
    }
    gl.uniformMatrix3fv(U.rot, false, mat(TILT + leanY * 0.25, angle + leanX * 0.25));
    gl.uniform1f(U.time, time);
    gl.uniform1f(U.draw, drawn < 1 ? 1 - Math.pow(1 - drawn, 3) : 1.01);
    gl.uniform2fv(U.light, light);
    gl.clearColor(0, 0, 0, 0);
    gl.clear(gl.COLOR_BUFFER_BIT);
    gl.drawArrays(gl.TRIANGLE_STRIP, 0, (SEGMENTS + 1) * 2);
  }
  const loop = now => { raf = 0; draw(now); if (visible && !reduce) raf = requestAnimationFrame(loop); };
  const start = () => { if (!raf && visible && !reduce) { last = performance.now(); raf = requestAnimationFrame(loop); } };

  host.addEventListener('pointermove', e => {
    const r = host.getBoundingClientRect();
    const x = (e.clientX - r.left) / r.width - 0.5, y = (e.clientY - r.top) / r.height - 0.5;
    targetX = x * 2; targetY = y * 2;
    light[0] = 0.5 + x; light[1] = 0.6 - y;
    if (dragging) { spin = (e.clientX - lastX) * 0.6; angle += (e.clientX - lastX) * 0.01; lastX = e.clientX; }
  });
  host.addEventListener('pointerdown', e => { dragging = true; lastX = e.clientX; host.setPointerCapture?.(e.pointerId); });
  const release = () => { dragging = false; spin = Math.max(-6, Math.min(6, spin)); };
  host.addEventListener('pointerup', release);
  host.addEventListener('pointercancel', release);
  host.addEventListener('pointerleave', () => { targetX = 0; targetY = 0; });

  new ResizeObserver(resize).observe(host);
  new IntersectionObserver(([entry]) => { visible = entry.isIntersecting; start(); }).observe(host);
  resize();
})();
