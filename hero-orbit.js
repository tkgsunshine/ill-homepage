// Hero first-view orbit: the six service nodes slowly circle the centre
// on a perfect circle (the dashed ring), one turn per ~60s, clockwise,
// evenly spaced. Labels stay upright.
(function () {
  var root = document.querySelector('.hero-orbit');
  if (!root) return;

  var nodes = Array.prototype.slice.call(root.querySelectorAll('.hero-orbit-node'));
  if (!nodes.length) return;

  var reduce = window.matchMedia && window.matchMedia('(prefers-reduced-motion: reduce)').matches;

  var RADIUS = 0.44;            // orbit radius, as a share of the box width (= the dashed .r2 ring)
  var TURN_SECONDS = 60;        // one full revolution
  var step = (Math.PI * 2) / nodes.length;

  var size = 0;
  var elapsed = 0;
  function measure() { size = root.clientWidth; }

  function place(t) {
    var half = size / 2;
    var spin = reduce ? 0 : (t / TURN_SECONDS) * Math.PI * 2;
    for (var i = 0; i < nodes.length; i++) {
      var r = RADIUS * size;
      var a = -Math.PI / 2 + i * step + spin;
      var x = half + Math.cos(a) * r;
      var y = half + Math.sin(a) * r;
      nodes[i].style.transform = 'translate3d(' + x.toFixed(2) + 'px,' + y.toFixed(2) + 'px,0)';
    }
  }

  // JS takes over from the static fallback positions written in the HTML.
  measure();
  nodes.forEach(function (n) { n.style.left = '0'; n.style.top = '0'; });
  place(0);

  if (!reduce) root.classList.add('is-animated');

  window.addEventListener('resize', function () { measure(); place(elapsed); });

  if (reduce) return;

  var last = null;
  var visible = true;
  var rafId = null;

  function frame(now) {
    if (last !== null) elapsed += Math.min((now - last) / 1000, 0.1);
    last = now;
    place(elapsed);
    rafId = visible ? requestAnimationFrame(frame) : null;
  }

  function start() {
    if (rafId === null) { last = null; rafId = requestAnimationFrame(frame); }
  }

  if ('IntersectionObserver' in window) {
    new IntersectionObserver(function (entries) {
      visible = entries[0].isIntersecting;
      if (visible) start();
    }).observe(root);
  }

  start();
})();
