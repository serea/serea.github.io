(function () {
  'use strict';
  var root = document.documentElement;
  var language;

  function preferredLanguage() {
    var explicit = new URL(window.location.href).searchParams.get('lang');
    if (explicit === 'en' || explicit === 'zh') return explicit;
    try { return localStorage.getItem('site-lang') === 'zh' ? 'zh' : 'en'; }
    catch (error) { return 'en'; }
  }

  function applyLanguage(next, updateURL) {
    language = next;
    var isChinese = language === 'zh';
    root.classList.toggle('zh', isChinese);
    root.lang = isChinese ? 'zh-CN' : 'en';
    try { localStorage.setItem('site-lang', language); } catch (error) {}
    if (updateURL) {
      var url = new URL(window.location.href);
      url.searchParams.set('lang', language);
      try { window.history.replaceState(null, '', url); } catch (error) {}
    }
    var button = document.getElementById('lang-btn');
    if (button) {
      button.textContent = isChinese ? 'EN' : '中文';
      button.setAttribute('aria-label', isChinese ? 'Switch to English' : '切换到中文');
    }
    document.querySelectorAll('[data-en][data-zh]').forEach(function (element) {
      element.textContent = element.getAttribute(isChinese ? 'data-zh' : 'data-en');
    });
    document.querySelectorAll('.masthead a[href]').forEach(function (link) {
      var url = new URL(link.getAttribute('href'), window.location.href);
      if (url.origin === window.location.origin) {
        url.searchParams.set('lang', language);
        link.setAttribute('href', url.pathname + url.search + url.hash);
      }
    });
    window.dispatchEvent(new Event('resize'));
  }

  applyLanguage(preferredLanguage(), false);
  document.addEventListener('click', function (event) {
    if (event.target.closest && event.target.closest('#lang-btn')) {
      applyLanguage(language === 'zh' ? 'en' : 'zh', true);
    }
  });
  document.addEventListener('DOMContentLoaded', function () {
    applyLanguage(language, false);
  });
  window.addEventListener('pageshow', function () { applyLanguage(preferredLanguage(), false); });
  window.addEventListener('popstate', function () { applyLanguage(preferredLanguage(), false); });
})();
