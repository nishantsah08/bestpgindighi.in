import { test, expect } from '@playwright/test';

test.describe('URL Redirects', () => {
  test('redirects /index.html to /', async ({ page }) => {
    await page.goto('/index.html');
    await expect(page).toHaveURL('/');
  });

  test('redirects /rooms.html to /rooms-and-pricing', async ({ page }) => {
    await page.goto('/rooms.html');
    await expect(page).toHaveURL('/rooms-and-pricing');
  });

  test('redirects /facilities.html to /facilities', async ({ page }) => {
    await page.goto('/facilities.html');
    await expect(page).toHaveURL('/facilities');
  });

  test('redirects /contact.html to /location-and-contact', async ({ page }) => {
    await page.goto('/contact.html');
    await expect(page).toHaveURL('/location-and-contact');
  });

  test('redirects /boys-hostel-dighi.html to /boys-hostel-dighi', async ({ page }) => {
    await page.goto('/boys-hostel-dighi.html');
    await expect(page).toHaveURL('/boys-hostel-dighi');
  });

  test('redirects /ait-student-housing.html to /ait-student-housing', async ({ page }) => {
    await page.goto('/ait-student-housing.html');
    await expect(page).toHaveURL('/ait-student-housing');
  });

  test('redirects /tcl-employee-accommodation.html to /tcl-employee-accommodation', async ({ page }) => {
    await page.goto('/tcl-employee-accommodation.html');
    await expect(page).toHaveURL('/tcl-employee-accommodation');
  });

  test('redirects /student-housing.html to /student-housing', async ({ page }) => {
    await page.goto('/student-housing.html');
    await expect(page).toHaveURL('/student-housing');
  });
});
