import { test, expect } from '@playwright/test';

test.describe('Properties & Units', () => {
  test('create, toggle, delete property and unit (happy path)', async ({ page }) => {
    await page.goto('/');

    // Add property
    await page.getByPlaceholder('Property Name').fill('E2E Test Property');
    await page.getByPlaceholder('Address Line 1').fill('123 Test St');
    await page.getByPlaceholder('City').fill('Pune');
    await page.getByPlaceholder('State').fill('MH');
    await page.getByPlaceholder('Pincode').fill('411001');
    await page.getByTestId('add-property').click();

    // Wait for row
    const row = page.locator('[data-testid^="property-row-"]', { hasText: 'E2E Test Property' });
    await expect(row).toBeVisible();

    // Expand units
    await row.getByRole('button', { name: 'Show Units' }).click();

    // Add unit
    await page.getByPlaceholder('Unit Number').fill('U-101');
    await page.getByPlaceholder('Unit Type').fill('Room');
    await page.getByRole('button', { name: 'Add Unit' }).click();

    // Toggle property status
    await row.getByRole('button', { name: /Set Non‑Operational/i }).click();

    // Delete property (type delete)
    await row.getByRole('button', { name: 'Delete' }).click();
    await page.getByPlaceholder('type delete').fill('delete');
    await page.getByRole('button', { name: 'Confirm' }).click();

    await expect(row).toHaveCount(0);
  });
});

