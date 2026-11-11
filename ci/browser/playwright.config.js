const { defineConfig } = require('@playwright/test');
module.exports = defineConfig({
  testDir: './tests',
  timeout: 45000,
  retries: 0,
  workers: 2,
  reporter: [['list'], ['html', { open: 'never' }]],
  use: {
    baseURL: process.env.BASE_URL || 'http://127.0.0.1:4173',
    trace: 'retain-on-failure',
    screenshot: 'only-on-failure',
    launchOptions: process.env.CHROME_CHANNEL ? { channel: process.env.CHROME_CHANNEL } : {}
  },
  projects: [
    { name: 'desktop', use: { viewport: { width: 1440, height: 1000 } } },
    { name: 'mobile', use: { viewport: { width: 390, height: 844 }, isMobile: true, hasTouch: true } }
  ],
  webServer: process.env.BASE_URL ? undefined : {
    command: 'python3 -m http.server 4173 --bind 127.0.0.1 --directory ../../_site',
    url: 'http://127.0.0.1:4173',
    reuseExistingServer: false
  }
});
