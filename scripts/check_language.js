/* Check built script loading and JavaScript syntax; Playwright tests real interactions. */
const fs = require('node:fs');
const path = require('node:path');
const vm = require('node:vm');
const assert = require('node:assert/strict');
const input = process.argv[2];
const script = input ? path.join(path.dirname(input), 'assets/js/language.js') : 'assets/js/language.js';
new vm.Script(fs.readFileSync(script, 'utf8'));
if (input) {
  const html = fs.readFileSync(input, 'utf8');
  assert.match(html, /<script src="[^"]*\/assets\/js\/language\.js\?v=2"><\/script>/);
  assert.match(html, /<button[^>]*id="lang-btn"[^>]*type="button"/);
  assert.doesNotMatch(html, /onclick="toggleLang\(\)"|href="javascript:void\(0\)"/);
}
console.log('PASS: external language script and native button wiring; use browser tests for interaction validation.');
