import { test, expect, devices } from '@playwright/test';

test.describe('Visual and Functional Checks', () => {
  const pagesToTest = [
    { name: 'Home', path: '/' },
    { name: 'Rooms & Pricing', path: '/rooms-and-pricing' },
    { name: 'Facilities', path: '/facilities' },
    { name: 'Location & Contact', path: '/location-and-contact' },
    { name: 'Boys Hostel Dighi', path: '/boys-hostel-dighi' },
    { name: 'AIT Student Housing', path: '/ait-student-housing' },
    { name: 'TCL Employee Accommodation', path: '/tcl-employee-accommodation' },
    { name: 'Student Housing', path: '/student-housing' },
    { name: '404 Page', path: '/non-existent-page' }, // Test 404 page
  ];

  // Visual checks for desktop
  for (const pageInfo of pagesToTest) {
    test(`Visual check for ${pageInfo.name} (Desktop)`, async ({ page }) => {
      await page.goto(pageInfo.path);
      await page.waitForLoadState('networkidle');
      await page.screenshot({ path: `test-results/screenshots/desktop/${pageInfo.name.replace(/ /g, '_')}.png`, fullPage: true });
    });
  }

  // Visual checks for mobile
  for (const pageInfo of pagesToTest) {
    test(`Visual check for ${pageInfo.name} (Mobile)`, async ({ page }) => {
      await page.setViewportSize(devices['iPhone 12'].viewport);
      await page.goto(pageInfo.path);
      await page.waitForLoadState('networkidle');
      await page.screenshot({ path: `test-results/screenshots/mobile/${pageInfo.name.replace(/ /g, '_')}.png`, fullPage: true });
    });
  }

  // Interactive element testing: Click-to-call on Contact page
  test('Click-to-call on Contact page', async ({ page }) => {
    await page.goto('/location-and-contact');
    const salesPhoneNumberLink = page.locator('a[href="tel:+917559421424"]');
    await expect(salesPhoneNumberLink).toBeVisible();
    // Note: Playwright cannot directly test phone calls, but we can verify the link's presence and href.
    await expect(salesPhoneNumberLink).toHaveAttribute('href', 'tel:+917559421424');
  });
});
