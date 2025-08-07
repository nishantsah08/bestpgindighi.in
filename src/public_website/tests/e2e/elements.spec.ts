const { test, expect } = require('@playwright/test');

test('Book Now button is visible', async ({ page }) => {
  await page.goto('https://bestpg-public.web.app/');
  await expect(page.locator('text=Book Now')).toBeVisible();
});
