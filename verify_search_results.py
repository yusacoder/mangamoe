import asyncio
from playwright.async_api import async_playwright

async def verify():
    async with async_playwright() as p:
        browser = await p.chromium.launch()
        page = await browser.new_page()

        # Test News Page Search
        await page.goto("file:///app/haberler.html")
        search_input = page.locator("#global-search-input")
        await search_input.fill("Anime")
        await asyncio.sleep(1)
        await page.screenshot(path="news_search_results_v2.png")

        # Test Home Page Enter behavior
        await page.goto("file:///app/index.html")
        await search_input.fill("Something")
        await search_input.press("Enter")
        await asyncio.sleep(0.5)
        await page.screenshot(path="home_search_enter_v2.png")

        await browser.close()

if __name__ == "__main__":
    asyncio.run(verify())
