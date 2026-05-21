import asyncio
from playwright.async_api import async_playwright

async def verify():
    async with async_playwright() as p:
        browser = await p.chromium.launch()
        page = await browser.new_page()

        # Go to an admin page
        # Assuming admin/hirata.html exists from previous ls
        url = "file:///app/admin/hirata.html"
        await page.goto(url)

        # Click search input to focus
        search_input = page.locator("#global-search-input")
        await search_input.click()

        # Wait for dropdown to show "Aramaya başlayın..."
        dropdown = page.locator("#search-dropdown")
        await asyncio.sleep(1) # wait for fetch and render

        # Check if dropdown is visible and has results or starting message
        is_visible = await dropdown.is_visible()
        content = await dropdown.inner_text()
        print(f"Dropdown visible: {is_visible}")
        print(f"Dropdown content: {content}")

        # Type something to search
        await search_input.fill("Anime")
        await asyncio.sleep(1)

        content_after_type = await dropdown.inner_text()
        print(f"Dropdown content after typing 'Anime': {content_after_type}")

        await page.screenshot(path="admin_search_verify.png")
        await browser.close()

if __name__ == "__main__":
    asyncio.run(verify())
