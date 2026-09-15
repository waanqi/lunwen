const { chromium } = require('C:/Users/Administrator/.cache/codex-runtimes/codex-primary-runtime/dependencies/node/node_modules/playwright');
const { pathToFileURL } = require('url');

(async () => {
  const browser = await chromium.launch({
    headless: true,
    executablePath: 'C:/Program Files/Google/Chrome/Application/chrome.exe'
  });
  const page = await browser.newPage({
    viewport: { width: 1600, height: 2140 },
    deviceScaleFactor: 2,
    colorScheme: 'light'
  });
  const svgPath = 'D:/Desk/折纸/kresling大论文/codex老师辅助/研究框架图_三栏式.svg';
  await page.goto(pathToFileURL(svgPath).href, { waitUntil: 'load' });
  await page.locator('svg').waitFor({ state: 'visible' });
  await page.screenshot({
    path: 'D:/Desk/折纸/kresling大论文/codex老师辅助/研究框架图_三栏式.png',
    fullPage: true,
    animations: 'disabled'
  });
  await browser.close();
})();
