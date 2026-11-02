const { defineConfig } = require("@playwright/test");

const frontendUrl = process.env.E2E_BASE_URL || "http://127.0.0.1:4173";
const apiUrl = process.env.E2E_API_URL || "http://127.0.0.1:8000";

module.exports = defineConfig({
  testDir: "./e2e",
  timeout: 60_000,
  expect: { timeout: 10_000 },
  fullyParallel: false,
  reporter: "list",
  use: {
    baseURL: frontendUrl,
    browserName: "chromium",
    headless: true,
    trace: "retain-on-failure",
  },
  webServer: [
    {
      command: "python -m http.server 4173 --directory frontend",
      url: frontendUrl,
      reuseExistingServer: !process.env.CI,
      timeout: 15_000,
    },
    {
      command: "python -c \"import urllib.request; urllib.request.urlopen('" + apiUrl + "/openapi.json', timeout=3)\"",
      url: apiUrl + "/openapi.json",
      reuseExistingServer: true,
      timeout: 15_000,
    },
  ],
});
