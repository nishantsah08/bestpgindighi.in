import { defineConfig, devices } from '@playwright/test';

export default defineConfig({
  testDir: './tests',
  fullyParallel: true, // Run tests in parallel
  workers: 5, // Limits concurrent test workers to 5
  reporter: 'html',
  use: {
    baseURL: 'https://bestpg-public.web.app',
    trace: 'on-first-retry',
    headless: true,
    viewport: { width: 1280, height: 720 },
  },
  projects: [
    {
      name: 'chromium',
      use: { ...devices['Desktop Chrome'] },
    },
    {
      name: 'firefox',
      use: { ...devices['Desktop Firefox'] },
    },
    {
      name: 'webkit',
      use: { ...devices['Desktop Safari'] },
    },
  ],
  // Ensure no webServer is configured
});
