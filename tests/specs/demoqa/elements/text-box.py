#to run this: python3 inputs/text-input.py
import asyncio
from playwright.async_api import async_playwright, expect

async def main():
    async with async_playwright() as p:
        browser = await p.chromium.launch(headless=False)
        context = await browser.new_context()
        await context.tracing.start(screenshots=True, snapshots=True, sources=True)
        page = await context.new_page()
        await page.set_viewport_size({"width": 1800, "height": 1200})
        await page.goto("https://demoqa.com/text-box")
        #Filling text-inputs
        await page.fill('#userName', 'Hernan')
        await page.fill('#userEmail', 'testingqa@gmail.com')
        await page.fill('#currentAddress', 'myAddress')
        await page.fill('#permanentAddress', 'myPermanentAddress')
        #Actions
        await page.click('#submit')
        await page.screenshot(path="screenshots/demoqa/elements/text-boxes.png")
        #Assertions
        await expect(page.locator("p#name")).to_have_text("Name:Hernan")
        await expect(page.locator("p#email")).to_have_text("Email:testingqa@gmail.com")
        await expect(page.locator("p#currentAddress")).to_have_text("Current Address :myAddress")
        await expect(page.locator("p#permanentAddress")).to_have_text("Permananet Address :myPermanentAddress")
        #StopTracing
        await context.tracing.stop(path = "logs/demoqa/elements/traceText-box.zip")
        #Closing browser
        await browser.close()


asyncio.run(main())