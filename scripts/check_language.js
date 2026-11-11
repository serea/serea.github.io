/* Test the actual inline language script, including compressed build output. */
const fs = require('node:fs');
const vm = require('node:vm');
const assert = require('node:assert/strict');

const input = process.argv[2] || '_includes/head/custom.html';
const html = input === '-' ? fs.readFileSync(0, 'utf8') : fs.readFileSync(input, 'utf8');
const scripts = [...html.matchAll(/<script\b[^>]*>([\s\S]*?)<\/script>/g)];
const script = scripts.map(match => match[1]).find(text => text.includes('window.toggleLang'));
assert.ok(script, 'Language script missing');
const variants = [script, script.replace(/\s+/g, ' ')];
let cases = 0;
for (const code of variants) {
  // Also parse the one-line form to catch comments swallowing code after compression.
  new vm.Script(code);
  for (const requested of [null, 'en', 'zh']) {
    for (const saved of ['en', 'zh']) {
      for (const blocked of [false, true]) {
        const classes = new Set();
        const ready = [];
        const button = { textContent: '中文' };
        const nav = { textContent: 'Home', getAttribute: key => key === 'data-zh' ? '首页' : 'Home' };
        const document = {
          documentElement: { classList: { toggle(name, force) {
            const on = force === undefined ? !classes.has(name) : force;
            if (on) classes.add(name); else classes.delete(name);
            return on;
          } } },
          getElementById: id => id === 'lang-btn' ? button : null,
          querySelectorAll: () => [nav],
          addEventListener: (event, fn) => { if (event === 'DOMContentLoaded') ready.push(fn); }
        };
        const href = 'https://serea.github.io/' + (requested ? '?lang=' + requested : '');
        let lastURL = href;
        const window = {
          location: { href, search: new URL(href).search },
          history: { replaceState: (_, __, url) => { lastURL = String(url); } }
        };
        const localStorage = {
          getItem() { if (blocked) throw Error('Storage unavailable'); return saved; },
          setItem() { if (blocked) throw Error('Storage unavailable'); }
        };
        vm.runInNewContext(code, { document, window, localStorage, URL, URLSearchParams });
        ready.forEach(fn => fn());
        assert.equal(typeof window.toggleLang, 'function');
        const initial = requested || (blocked ? 'en' : saved);
        function verify(lang) {
          assert.equal(classes.has('zh'), lang === 'zh');
          assert.equal(document.documentElement.lang, lang === 'zh' ? 'zh-CN' : 'en');
          assert.equal(button.textContent, lang === 'zh' ? 'EN' : '中文');
          assert.equal(nav.textContent, lang === 'zh' ? '首页' : 'Home');
        }
        verify(initial);
        window.toggleLang();
        verify(initial === 'en' ? 'zh' : 'en');
        assert.equal(new URL(lastURL).searchParams.get('lang'), initial === 'en' ? 'zh' : 'en');
        window.toggleLang();
        verify(initial);
        cases++;
      }
    }
  }
}
console.log(`PASS: ${cases} language-switch cases, including compressed JavaScript, labels, URL, and blocked storage.`);
