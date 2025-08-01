import { test, expect } from '@playwright/test';

test.describe('Cabinet Secretary Portal E2E Tests', () => {
  test.beforeEach(async ({ page }) => {
    await page.goto('http://localhost:3000');
  });

  test('should display the header', async ({ page }) => {
    await expect(page.getByRole('heading', { name: 'Cabinet Secretary Portal' })).toBeVisible();
  });

  test('should send a message and receive an AI response', async ({ page }) => {
    const userMessage = 'Hello, backend!';
    await page.getByPlaceholder('Type your message...').fill(userMessage);
    await page.getByRole('button', { name: 'Send' }).click();

    // Expect user message to appear
    await expect(page.locator('.message.user').filter({ hasText: userMessage })).toBeVisible();

    // Expect AI thinking message to appear initially
    await expect(page.locator('.message.ai').filter({ hasText: 'Thinking...' })).toBeVisible();

    // Expect AI actual response to appear
    await expect(page.locator('.message.ai').filter({ hasText: `AI received: ${userMessage}` })).toBeVisible();

    // Verify input is cleared
    await expect(page.getByPlaceholder('Type your message...')).toHaveValue('');
  });

  test('should handle empty messages', async ({ page }) => {
    await page.getByPlaceholder('Type your message...').fill('   '); // Only spaces
    await page.getByRole('button', { name: 'Send' }).click();

    // No new messages should appear in the chat display
    await expect(page.locator('.messages-display .message')).toHaveCount(0);

    // Input should not be cleared if it was just spaces (trim() handles this)
    await expect(page.getByPlaceholder('Type your message...')).toHaveValue('   ');
  });

  test('should persist messages after refresh', async ({ page }) => {
    const userMessage1 = 'First message';
    await page.getByPlaceholder('Type your message...').fill(userMessage1);
    await page.getByRole('button', { name: 'Send' }).click();
    await expect(page.locator('.message.ai').filter({ hasText: `AI received: ${userMessage1}` })).toBeVisible();

    const userMessage2 = 'Second message';
    await page.getByPlaceholder('Type your message...').fill(userMessage2);
    await page.getByRole('button', { name: 'Send' }).click();
    await expect(page.locator('.message.ai').filter({ hasText: `AI received: ${userMessage2}` })).toBeVisible();

    // Reload the page
    await page.reload();

    // Expect all messages to be visible after refresh
    await expect(page.locator('.message.user').filter({ hasText: userMessage1 })).toBeVisible();
    await expect(page.locator('.message.ai').filter({ hasText: `AI received: ${userMessage1}` })).toBeVisible();
    await expect(page.locator('.message.user').filter({ hasText: userMessage2 })).toBeVisible();
    await expect(page.locator('.message.ai').filter({ hasText: `AI received: ${userMessage2}` })).toBeVisible();
  });
});
