const { test, expect } = require('@playwright/test');

test('measure homepage load performance', async ({ page }) => {
  await page.goto('https://bestpg-public.web.app/');
  const timing = JSON.parse(
    await page.evaluate(() => JSON.stringify(window.performance.timing))
  );
  console.log('Page load time:', timing.loadEventEnd - timing.navigationStart);
  expect(timing.loadEventEnd - timing.navigationStart).toBeLessThan(3000);
});
