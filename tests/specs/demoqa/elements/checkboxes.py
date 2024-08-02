#to run this: python inputs/checkboxes.py
import asyncio
from playwright.async_api import async_playwright, expect

async def main():
    async with async_playwright() as p:
        browser = await p.chromium.launch(headless=False)
        context = await browser.new_context()
        await context.tracing.start(screenshots=True, snapshots=True, sources=True)
        page = await context.new_page()
        
        await page.set_viewport_size({"width": 1800, "height": 1200})
        await page.goto("https://demoqa.com/checkbox")
        await page.check('label[for="tree-node-home"]')
        
        #Assertions
        await expect(page.get_by_label('Home')).to_be_checked() 
        await expect(page.locator("#result")).to_have_text("You have selected :homedesktopnotescommandsdocumentsworkspacereactangularveuofficepublicprivateclassifiedgeneraldownloadswordFileexcelFile")
        #screenshot
        await page.screenshot(path="screenshots/checkboxes.png")
        #stopTracing
        await context.tracing.stop(path = "logs/traceCheckboxes.zip")
         #-Closing browser
        await browser.close()

asyncio.run(main())