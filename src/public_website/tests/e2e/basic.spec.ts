import { test, expect } from '@playwright/test';

test('has title', async ({ page }) => {
  await page.goto('/');

  // Expect a title "to contain" a substring.
  await expect(page).toHaveTitle(/Best PG in Dighi/);
});

test('has main heading', async ({ page }) => {
  await page.goto('/');

  // Expect the main heading to be visible
  await expect(page.locator('h1')).toContainText('Comfortable & Affordable PG Accommodation in Dighi Hills, Pune');
});

test('navigate to rooms and pricing', async ({ page }) => {
  await page.goto('/');
  await page.getByRole('link', { name: 'Rooms & Pricing' }).click();
  await expect(page).toHaveURL(/.*rooms-and-pricing/);
  await expect(page.locator('h1')).toContainText('Our Rooms & Pricing');
});

test('navigate to location and contact', async ({ page }) => {
  await page.goto('/');
  await page.getByRole('link', { name: 'Location & Contact' }).click();
  await expect(page).toHaveURL(/.*location-and-contact/);
  await expect(page.locator('h1')).toContainText('Location & Contact Us');
});
