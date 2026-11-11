const { test, expect } = require('@playwright/test');

test.beforeEach(async ({ page, baseURL }) => {
  await page.route('https://serea.github.io/**', route => {
    if (new URL(baseURL).hostname !== 'serea.github.io') return route.abort('blockedbyclient');
    return route.continue();
  });
});

async function language(page, value, homepage = false) {
  await expect(page.locator('html')).toHaveAttribute('lang', value === 'zh' ? 'zh-CN' : 'en');
  await expect(page.locator('#lang-btn')).toBeVisible();
  await expect(page.locator('#lang-btn')).toHaveText(value === 'zh' ? 'EN' : '中文');
  if (homepage) {
    await expect(page.locator('div.lang-' + value)).toBeVisible();
    await expect(page.locator('div.lang-' + (value === 'zh' ? 'en' : 'zh'))).toBeHidden();
  }
}

async function navigate(page, path) {
  const target = page.locator('#site-nav a[href*="' + path + '"]').first();
  if (!await target.isVisible()) await page.getByRole('button', { name: 'Navigation menu', exact: true }).click();
  await target.click();
  await expect(page).toHaveURL(new RegExp(path));
}

test('language button responds immediately, persists across tabs and refresh, and works with keyboard', async ({ page }) => {
  const errors = [];
  page.on('pageerror', error => errors.push(error.message));
  await page.goto('/');
  await language(page, 'en', true);
  await page.locator('#lang-btn').click();
  await language(page, 'zh', true);
  await page.reload();
  await language(page, 'zh', true);
  await navigate(page, '/publications/');
  await language(page, 'zh');
  await page.locator('#lang-btn').click();
  await language(page, 'en');
  await page.locator('.masthead__menu-item--lg a').click();
  await language(page, 'en', true);
  await page.locator('#lang-btn').focus();
  await page.keyboard.press('Enter');
  await language(page, 'zh', true);
  await page.keyboard.press('Space');
  await language(page, 'en', true);
  expect(errors).toEqual([]);
});

test('explicit language overrides and updates old preference across navigation', async ({ page }) => {
  await page.goto('/?lang=zh');
  await language(page, 'zh', true);
  await page.goto('/?lang=en');
  await language(page, 'en', true);
  await navigate(page, '/publications/');
  await language(page, 'en');
  await page.goto('/');
  await language(page, 'en', true);
});

test('language and navigation still work when storage is unavailable', async ({ page }) => {
  await page.addInitScript(() => {
    Storage.prototype.getItem = () => { throw new Error('Storage blocked'); };
    Storage.prototype.setItem = () => { throw new Error('Storage blocked'); };
  });
  await page.goto('/');
  await page.locator('#lang-btn').click();
  await language(page, 'zh', true);
  await navigate(page, '/publications/');
  await language(page, 'zh');
  await page.locator('#lang-btn').click();
  await language(page, 'en');
});

test('button works before a slow footer script finishes loading', async ({ page }) => {
  let release;
  const gate = new Promise(resolve => { release = resolve; });
  await page.route('**/assets/js/main.min.js*', async route => {
    await gate;
    await route.continue();
  });
  try {
    await page.goto('/', { waitUntil: 'commit' });
    await expect(page.locator('#lang-btn')).toBeVisible();
    expect(await page.evaluate(() => document.readyState)).toBe('loading');
    await page.locator('#lang-btn').click();
    await language(page, 'zh', true);
  } finally {
    release();
  }
  await page.waitForLoadState('load');
  await language(page, 'zh', true);
});

test('all primary navigation tabs open and language button stays visible', async ({ page }) => {
  await page.goto('/');
  const paths = await page.locator('#site-nav a[data-en]').evaluateAll(links => links.map(link => new URL(link.href).pathname));
  expect(paths.length).toBeGreaterThan(0);
  for (const path of paths) {
    await page.goto('/');
    await navigate(page, path);
    await expect(page.locator('#lang-btn')).toBeVisible();
    await page.locator('#lang-btn').click();
    await language(page, 'zh');
    await page.locator('#lang-btn').click();
    await language(page, 'en');
  }
});
