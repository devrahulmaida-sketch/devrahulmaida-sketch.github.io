/* ============ MAIDA — main.js (v3) ============ */
(function(){
  if (window.Plyr) {
    document.querySelectorAll('video.plyr').forEach(function(v){
      new Plyr(v, {controls:['play-large','play','progress','current-time','duration','mute','volume','settings','fullscreen'], ratio:'16:9', resetOnEnd:true, hideControls:true});
    });
  }
  // language switcher
  var btns = document.querySelectorAll('.lang-btn');
  function setLang(l){
    if (!document.querySelector('.lang-block[data-lang="'+l+'"]')) l = 'hinglish';
    document.querySelectorAll('.lang-block').forEach(function(b){ b.hidden = (b.dataset.lang !== l); });
    btns.forEach(function(b){ b.classList.toggle('active', b.dataset.lang === l); });
    document.querySelectorAll('.lang-title,.lang-sub').forEach(function(el){
      var v = el.getAttribute('data-'+l); if (v) el.textContent = v;
    });
    try { localStorage.setItem('maida-lang', l); } catch(e){}
    try { history.replaceState(null,'',location.pathname+'?lang='+l+location.hash); } catch(e){}
  }
  if (btns.length) {
    btns.forEach(function(b){ b.addEventListener('click', function(){ setLang(b.dataset.lang); }); });
    var p = new URLSearchParams(location.search).get('lang') || (function(){try{return localStorage.getItem('maida-lang')}catch(e){return null}})() || 'hinglish';
    setLang(p);
  }
  // navbar active
  var path = location.pathname;
  document.querySelectorAll('.nav nav a').forEach(function(a){
    var href = a.getAttribute('href').split('#')[0];
    if (href && href !== '/' && path.indexOf(href) === 0) a.style.color = 'var(--amber)';
    else if (href === '/' && (path === '/' || path === '/index.html')) a.style.color = 'var(--amber)';
  });
})();
