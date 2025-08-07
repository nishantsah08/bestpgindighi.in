const puppeteer = require('puppeteer');
const fs = require('fs');
const path = require('path');

const BASE_URL = 'https://bestpg-public.web.app/';
const brokenLinks = [];

const navigationLinks = [
  { text: 'Home', url: '/' },
  { text: 'Rooms & Pricing', url: '/rooms-and-pricing' },
  { text: 'Facilities', url: '/facilities' },
  { text: 'Location & Contact', url: '/location-and-contact' },
];

const footerLinks = [
  { text: 'Home', url: '/' },
  { text: 'Facilities', url: '/facilities' },
  { text: 'Location & Contact', url: '/location-and-contact' },
];

async function runTests(browser, viewportName, viewport) {
  const page = await browser.newPage();
  await page.setViewport(viewport);

  // Response interception for 4xx/5xx errors
  page.on('response', response => {
    if (response.status() >= 400) {
      brokenLinks.push(`[HTTP ERROR] ${response.status()} on ${response.url()}`);
    }
  });

  console.log(`\n--- Running tests for ${viewportName} ---`);

  // Navigate to the base URL once at the beginning of the test run
  await page.goto(BASE_URL, { waitUntil: 'domcontentloaded', timeout: 60000 });
  await page.waitForSelector('h1', { timeout: 15000 }); // Wait for H1 to be visible on initial load

  // Test navigation links
  for (const link of navigationLinks) {
    console.log(`Testing navigation: ${link.text} (${viewportName})`);
    try {
      // Navigate back to the base URL before clicking a new nav link
      if (page.url() !== BASE_URL) {
        await page.goto(BASE_URL, { waitUntil: 'domcontentloaded', timeout: 60000 });
        await page.waitForSelector('h1', { timeout: 15000 });
      }

      const [response] = await Promise.all([
        page.waitForNavigation({ waitUntil: 'domcontentloaded', timeout: 60000 }),
        page.click(`nav a[href="${link.url}"]`),
      ]);

      if (!response.ok()) {
        brokenLinks.push(`[NAVIGATION FAILED] ${link.text} to ${response.url()} - Status: ${response.status()}`);
      }

      // Fallback: Wait for a page-unique selector or URL change
      await page.waitForSelector('h1', { timeout: 15000 }); // Assuming H1 is on all content pages
      const currentUrl = page.url();
      if (!currentUrl.endsWith(link.url)) {
        brokenLinks.push(`[URL MISMATCH] ${link.text} expected ${BASE_URL}${link.url} but got ${currentUrl}`);
      }

    } catch (error) {
      brokenLinks.push(`[NAVIGATION ERROR] ${link.text} (${viewportName}) - ${error.message}`);
    }
  }

  await page.close();
}

(async () => {
  const browser = await puppeteer.launch({ headless: true }); // Set to false for visual debugging

  // Desktop
  await runTests(browser, 'Desktop', { width: 1280, height: 720 });

  // Mobile
  await runTests(browser, 'Mobile', { width: 375, height: 667 }); // iPhone SE

  await browser.close();

  const reportPath = path.join(__dirname, '../../navigation-audit-puppeteer.txt');
  fs.writeFileSync(reportPath, brokenLinks.join('\n'));

  console.log(`\n--- Navigation Audit Complete ---\nBroken Links/Issues Found: ${brokenLinks.length}\nReport saved to: ${reportPath}\n`);

  if (brokenLinks.length > 0) {
    console.log('Broken Links/Issues:');
    brokenLinks.forEach(link => console.log(link));
  }
})();