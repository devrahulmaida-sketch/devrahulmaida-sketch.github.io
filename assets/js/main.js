/* ============ MAIDA — main.js ============ */
(function(){
  // Plyr video player — agar CDN load ho, use karo; warna native player rahega (controls attribute already hai)
  if (window.Plyr) {
    document.querySelectorAll('video.plyr').forEach(function(v){
      new Plyr(v, {
        controls: ['play-large','play','progress','current-time','duration','mute','volume','settings','fullscreen'],
        ratio: '16:9',
        resetOnEnd: true,
        hideControls: true
      });
    });
  }

  // Navbar active link highlight
  var path = location.pathname.split('/').pop() || 'index.html';
  document.querySelectorAll('.nav nav a').forEach(function(a){
    var href = a.getAttribute('href').split('#')[0] || 'index.html';
    if (href === path) a.style.color = 'var(--amber)';
  });

  // JEE practice answers pe click se smooth open
  document.querySelectorAll('details.jee-sol summary').forEach(function(s){
    s.addEventListener('click', function(){ /* default behavior fine */ });
  });
})();
