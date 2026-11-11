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
    btns.forEach(function(b){ b.classList.toggle('active', b.dataset.lang === l); b.setAttribute('aria-pressed',String(b.dataset.lang===l)); });
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
    if (href && href !== '/' && href !== '/src/site/' && path.indexOf(href) === 0) a.style.color = 'var(--amber)';
    else if ((href === '/' || href === '/src/site/') && (path === href || path === href + 'index.html')) a.style.color = 'var(--amber)';
  });
})();

/* ============================================================
   Reading tools v1: progress bar, section jump menu,
   previous/next chapter links, homepage search + continue.
   Runs on every page; each feature no-ops when its page
   does not need it.
   ============================================================ */
(function () {
  'use strict';

  function onReady(fn) {
    if (document.readyState === 'loading') document.addEventListener('DOMContentLoaded', fn);
    else fn();
  }
  function esc(s) {
    return String(s).replace(/[&<>"']/g, function (c) {
      return { '&': '&amp;', '<': '&lt;', '>': '&gt;', '"': '&quot;', "'": '&#39;' }[c];
    });
  }

  var CH = null, CHpending = [];
  function withCatalogue(cb) {
    if (CH) { cb(CH); return; }
    CHpending.push(cb);if(CHpending.length>1)return;
    try {
      var x = new XMLHttpRequest();
      x.open('GET', '/assets/data/chapters.json', true);
      x.onreadystatechange = function () {
        if (x.readyState !== 4) return;
        try { CH = x.status === 200 ? JSON.parse(x.responseText) : []; }
        catch (e) { CH = []; }
        var callbacks=CHpending;CHpending=[];callbacks.forEach(function(fn){fn(CH)});
      };
      x.send();
    } catch (e) { var callbacks=CHpending;CHpending=[];callbacks.forEach(function(fn){fn([])}); }
  }

  function currentChapter() {
    var m = location.pathname.match(/^\/src\/site\/class-(\d+)\/(.+)\/ch-(\d+)\/?$/);
    return m ? { c: m[1], g: m[2], n: parseInt(m[3], 10) } : null;
  }
  function isHome() {
    return /^\/src\/site\/?(index\.html)?$/.test(location.pathname);
  }
  function subjLabel(s) { return s.replace(/-/g, ' '); }

  /* ---------- 1. reading progress bar (every page) ---------- */
  function progressBar() {
    var bar = document.createElement('div');
    bar.className = 'm-progress';
    bar.setAttribute('aria-hidden', 'true');
    document.body.appendChild(bar);
    var ticking = false;
    function update() {
      ticking = false;
      var h = document.documentElement;
      var max = h.scrollHeight - h.clientHeight;
      bar.style.transform = 'scaleX(' + (max > 0 ? Math.min(1, h.scrollTop / max) : 0) + ')';
    }
    window.addEventListener('scroll', function () {
      if (!ticking) { ticking = true; requestAnimationFrame(update); }
    }, { passive: true });
    window.addEventListener('resize', update);
    update();
  }

  /* ---------- 2. section jump menu (chapter pages) ---------- */
  function jumpMenu() {
    function collectTargets() {
      var out = [], i, j, hs = null;
      var blocks = document.querySelectorAll('.lang-block');
      for (i = 0; i < blocks.length; i++) {
        if (blocks[i].hasAttribute('hidden')) continue;
        hs = blocks[i].querySelectorAll('.note-sec h3');
        if (hs.length) break;
        hs = null;
      }
      if (!hs) hs = document.querySelectorAll('.note-sec h3');
      for (j = 0; j < hs.length; j++) {
        if (!hs[j].id) hs[j].id = 'm-sec-' + (hs[j].closest('.lang-block')?hs[j].closest('.lang-block').dataset.lang:'all') + '-' + j;
        out.push({ id: hs[j].id, label: hs[j].textContent.trim() });
      }
      var extra = [['walkthrough', 'Walkthrough'], ['short-notes', 'Short notes'], ['practice', 'Practice']];
      for (i = 0; i < extra.length; i++) {
        if (document.getElementById(extra[i][0])) out.push({ id: extra[i][0], label: extra[i][1] });
      }
      return out;
    }
    if (!collectTargets().length) return;

    var btn = document.createElement('button');
    btn.type = 'button';
    btn.className = 'm-jump-btn';
    btn.textContent = 'Sections';
    btn.setAttribute('aria-haspopup', 'true');
    document.body.appendChild(btn);
    document.body.classList.add('m-has-jump');

    var veil = null, panel = null;
    function close() {
      if (veil) veil.remove();
      if (panel) panel.remove();
      veil = panel = null;
      document.removeEventListener('keydown', onKey);btn.setAttribute('aria-expanded','false');btn.focus();
    }
    function onKey(e) { if(e.key==='Escape'){close();return}if(e.key==='Tab'&&panel){var f=panel.querySelectorAll('button,a[href]');if(e.shiftKey&&document.activeElement===f[0]){e.preventDefault();f[f.length-1].focus()}else if(!e.shiftKey&&document.activeElement===f[f.length-1]){e.preventDefault();f[0].focus()}} }
    function open() {
      var items = collectTargets();
      veil = document.createElement('div');
      veil.className = 'm-jump-veil';
      veil.addEventListener('click', close);
      panel = document.createElement('div');
      panel.className = 'm-jump-panel';
      panel.setAttribute('role', 'dialog');
      panel.setAttribute('aria-label', 'Page sections');panel.setAttribute('aria-modal','true');
      var html = '<div class="m-jump-head">Is page mein<button type="button" class="m-jump-close" aria-label="Close">&#10005;</button></div><div class="m-jump-list">';
      for (var i = 0; i < items.length; i++) {
        html += '<a class="m-jump-item" href="#' + esc(items[i].id) + '" data-t="' + esc(items[i].id) + '">' + esc(items[i].label) + '</a>';
      }
      panel.innerHTML = html + '</div>';
      document.body.appendChild(veil);
      document.body.appendChild(panel);
      panel.querySelector('.m-jump-close').addEventListener('click', close);
      panel.addEventListener('click', function (e) {
        var a = e.target.closest ? e.target.closest('.m-jump-item') : null;
        if (!a) return;
        e.preventDefault();
        var el = document.getElementById(a.getAttribute('data-t'));
        close();
        if (el) el.scrollIntoView();
      });
      document.addEventListener('keydown', onKey);btn.setAttribute('aria-expanded','true');panel.querySelector('button').focus();
    }
    btn.addEventListener('click', open);

    /* keep the pill out of the way while reading: hide on scroll down,
       show again on scroll up or when scrolling stops */
    var lastY = window.scrollY || 0;
    window.addEventListener('scroll', function () {
      var y = window.scrollY || 0;
      if (y > lastY + 4 && y > 120 && !panel) btn.classList.add('m-jump-hidden');
      else if (y < lastY - 4 || y <= 120) btn.classList.remove('m-jump-hidden');
      lastY = y;
    }, { passive: true });
  }

  /* ---------- 3. previous / next chapter ---------- */
  function prevNext() {
    var cur = currentChapter();
    if (!cur) return;
    withCatalogue(function (all) {
      var prev = null, next = null, i;
      for (i = 0; i < all.length; i++) {
        var e = all[i];
        if (e.c !== cur.c || e.g !== cur.g) continue;
        if (e.n < cur.n && (!prev || e.n > prev.n)) prev = e;
        if (e.n > cur.n && (!next || e.n < next.n)) next = e;
      }
      if (!prev && !next) return;
      var nav = document.createElement('nav');
      nav.className = 'm-pnx wrap';
      nav.setAttribute('aria-label', 'Chapter navigation');
      var html = '';
      if (prev) {
        html += '<a class="m-pnx-link" href="' + esc(prev.u) + '"><span class="m-pnx-k">&larr; Pichla chapter</span><span class="m-pnx-t">Ch ' + prev.n + ' - ' + esc(prev.t) + '</span></a>';
      } else {
        html += '<a class="m-pnx-link" href="/src/site/class-' + esc(cur.c) + '/' + esc(cur.g.split('/')[0]) + '/"><span class="m-pnx-k">&larr; Subject index</span><span class="m-pnx-t">' + esc(subjLabel(cur.g.split('/')[0])) + '</span></a>';
      }
      if (next) {
        html += '<a class="m-pnx-link m-pnx-next" href="' + esc(next.u) + '"><span class="m-pnx-k">Agla chapter &rarr;</span><span class="m-pnx-t">Ch ' + next.n + ' - ' + esc(next.t) + '</span></a>';
      } else {
        html += '<a class="m-pnx-link m-pnx-next" href="/src/site/class-' + esc(cur.c) + '/' + esc(cur.g.split('/')[0]) + '/"><span class="m-pnx-k">Subject index &rarr;</span><span class="m-pnx-t">' + esc(subjLabel(cur.g.split('/')[0])) + '</span></a>';
      }
      nav.innerHTML = html;
      var foot = document.querySelector('footer.foot');
      if (foot && foot.parentNode) foot.parentNode.insertBefore(nav, foot);
      else document.body.appendChild(nav);
    });
  }

  /* ---------- 4. homepage: chapter search + continue reading ---------- */
  function norm(s) { return String(s).toLowerCase().replace(/[^a-z0-9\u0900-\u097F]+/g, ' '); }
  function homeTools() {
    if (!isHome()) return;
    var hero = document.querySelector('.hero-inner');
    if (!hero) return;

    var cont = null;
    try {
      var last = JSON.parse(localStorage.getItem('maida-last-ch') || 'null');
      if (last && last.u && last.t && /^\/src\/site\//.test(last.u)) {
        cont = document.createElement('a');
        cont.className = 'm-cont';
        cont.href = last.u;
        cont.innerHTML = '<span class="m-cont-k">Aage padho &rarr;</span> ' + esc(last.t);
      }
    } catch (e) {}

    var box = document.createElement('div');
    box.className = 'm-find';
    box.innerHTML = '<input id="m-find-q" type="search" autocomplete="off" placeholder="Chapter khojo - jaise waves, motion, ya class 9 maths" aria-label="Chapter khojo">' +
      '<div class="m-find-res" id="m-find-res" hidden></div>';
    var anchor = hero.querySelector('h1') || hero.querySelector('.hero-sub') || hero.querySelector('.hero-stats');
    if (anchor && anchor.parentNode === hero) hero.insertBefore(box, anchor.nextSibling);
    else hero.appendChild(box);
    if (cont) hero.insertBefore(cont, box);

    var q = box.querySelector('#m-find-q'), res = box.querySelector('#m-find-res');
    withCatalogue(function (all) {
      q.addEventListener('input', function () {
        var v = norm(q.value).trim();
        if (v.length < 2) { res.hidden = true; res.innerHTML = ''; return; }
        var toks = v.split(/\s+/), hits = [], i, j;
        for (i = 0; i < all.length; i++) {
          var e = all[i];
          var hay = norm(e.t) + ' ' + norm(subjLabel(e.g)) + ' class ' + e.c + ' ch ' + e.n;
          var ok = true;
          for (j = 0; j < toks.length; j++) if (hay.indexOf(toks[j]) < 0) { ok = false; break; }
          if (ok) hits.push(e);
          if (hits.length >= 8) break;
        }
        if (!hits.length) {
          res.innerHTML = '<div class="m-find-none">Kuch nahi mila - spelling ya class number badal kar dekho.</div>';
          res.hidden = false;
          return;
        }
        var h = '';
        for (i = 0; i < hits.length; i++) {
          h += '<a class="m-find-item" href="' + esc(hits[i].u) + '">' +
            '<span class="m-find-badge">' + esc(hits[i].c) + '</span>' +
            '<span class="m-find-sub">' + esc(subjLabel(hits[i].g)) + ' &middot; Ch ' + hits[i].n + '</span>' +
            '<span class="m-find-title">' + esc(hits[i].t) + '</span></a>';
        }
        res.innerHTML = h;
        res.hidden = false;
      });
    });
  }

  /* ---------- 5. remember last chapter ---------- */
  function recordVisit() {
    var cur = currentChapter();
    if (!cur) return;
    try {
      var h1 = document.querySelector('.ch-hero h1') || document.querySelector('h1');
      var t = h1 ? h1.textContent.trim().slice(0, 80) : '';
      localStorage.setItem('maida-last-ch', JSON.stringify({ u: location.pathname, t: t }));
    } catch (e) {}
  }

  /* ---------- 0. stylesheet freshness: self-heal a stale cached style.css ---------- */
  function ensureCss() {
    var found = false, i, j;
    for (i = 0; i < document.styleSheets.length; i++) {
      var sh = document.styleSheets[i];
      if (!sh.href || sh.href.indexOf('/assets/css/style.css') < 0) continue;
      try {
        var rs = sh.cssRules;
        for (j = 0; j < rs.length; j++) {
          if (rs[j].selectorText === '.m-jump-btn') { found = true; break; }
        }
      } catch (e) { found = true; }
      if (found) break;
    }
    if (!found) {
      var l = document.createElement('link');
      l.rel = 'stylesheet';
      l.href = '/assets/css/style.css?v=rt1';
      document.head.appendChild(l);
      return 'reloaded-css';
    }
    return 'css-ok';
  }

  onReady(function () {
    try { progressBar(); } catch (e) {}
    try { jumpMenu(); } catch (e) {}
    try { prevNext(); } catch (e) {}
    try { homeTools(); } catch (e) {}
    try { recordVisit(); } catch (e) {}
    if (document.readyState === 'complete') { try { ensureCss(); } catch (e) {} }
    else window.addEventListener('load', function () { try { ensureCss(); } catch (e) {} });
  });
})();

/* Content-preserving discovery and click-to-load video controls. */
(function(){
 'use strict';document.documentElement.classList.add('m-enhanced');
 document.querySelectorAll('.m-video').forEach(function(box){
  var button=box.querySelector('.m-video-load'),tpl=box.querySelector('template');
  if(!button||!tpl)return;
  button.addEventListener('click',function(){
   var frame=tpl.content.querySelector('iframe').cloneNode(true);
   frame.loading='eager';box.replaceChildren(frame);frame.focus();
  },{once:true});
 });
 var cards=document.querySelector('.cards');
 var isIndex=/^\/src\/site\/class-\d+\/.+\/$/.test(location.pathname)&&!location.pathname.includes('/ch-')&&!location.pathname.includes('/walkthrough/');
 if(isIndex&&cards){
  var entries=Array.prototype.slice.call(cards.children).filter(function(x){return x.classList.contains('card')});
  if(entries.length>3){
   cards.classList.add('m-index-list');
   entries.forEach(function(card){
    var topics=card.querySelector('.card-topics'),meta=card.querySelector('.card-meta');
    if(!topics&&!meta)return;
    var detail=document.createElement('details');detail.className='m-index-details';
    var summary=document.createElement('summary');summary.textContent='Topics aur details';detail.append(summary);
    if(topics)detail.append(topics);if(meta)detail.append(meta);card.append(detail);
   });
   var tools=document.createElement('div');tools.className='m-index-tools';
   tools.innerHTML='<label for="m-index-q">Is list mein khojo</label><input id="m-index-q" type="search" placeholder="Chapter ka naam ya topic" autocomplete="off"><p class="m-index-status" role="status" aria-live="polite"></p>';
   cards.before(tools);var input=tools.querySelector('input'),status=tools.querySelector('[role="status"]');
   var empty=document.createElement('p');empty.className='m-index-empty';empty.textContent='Koi matching chapter nahi. Doosra naam ya topic try karo.';empty.hidden=true;cards.after(empty);
   function filter(){var terms=input.value.toLowerCase().trim().split(/\s+/).filter(Boolean),n=0;
    entries.forEach(function(e){var text=e.textContent.toLowerCase();var show=terms.every(function(t){return text.includes(t)});e.hidden=!show;if(show)n++});
    status.textContent=n+' / '+entries.length+' entries dikh rahe hain. Coverage har chapter par dekhein.';empty.hidden=n!==0;
   }
   input.addEventListener('input',filter);filter();
  }
 }
 var dest=document.querySelector('#notes')||document.querySelector('.hero')||document.querySelector('.ch-hero');
 if(dest){if(!dest.id)dest.id='main-content';var skip=document.createElement('a');skip.className='m-skip';skip.href='#'+dest.id;skip.textContent='Main content par jao';document.body.prepend(skip);dest.setAttribute('tabindex','-1')}
})();
