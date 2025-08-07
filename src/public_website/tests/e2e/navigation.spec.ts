const { test, expect } = require('@playwright/test');

const pages = [
  { label: 'Rooms & Pricing', urlText: 'Our Rooms & Pricing' },
  { label: 'Facilities', urlText: 'Our Facilities' },
  { label: 'Location & Contact', urlText: 'Location & Contact Us' },
];

pages.forEach(({ label, urlText }) => {
  test(`Nav link "${label}" works`, async ({ page }) => {
    await page.goto('https://bestpg-public.web.app/');
    await page.click(`text=${label}`);
    await expect(page.locator(`text=${urlText}`)).toBeVisible();
  });
});
