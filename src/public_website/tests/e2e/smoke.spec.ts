const { test, expect } = require('@playwright/test');

test('homepage should load with main elements', async ({ page }) => {
  await page.goto('https://bestpg-public.web.app/');
  await expect(page).toHaveTitle(/Best PG in Dighi/i);
  await expect(page.locator('text=Why Choose Our PG?')).toBeVisible();
});
