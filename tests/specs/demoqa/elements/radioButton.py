import asyncio
from playwright.async_api import async_playwright, expect


async def main():
    async with async_playwright() as p:
        browser = await p.chromium.launch(headless= False)
        context = await browser.new_context()
        await context.tracing.start(screenshots=True,snapshots= True, sources= True)
        page = await context.new_page()
        
        await page.set_viewport_size({'width': 1280, 'height': 1024})
        
        await page.goto('https://demoqa.com/radio-button')
        
        await page.check('#yesRadio',force= True)

        
        #Assertions
        await page.is_checked('#yesRadio') is  True
        await expect(page.locator('span[class="text-success"]')).to_have_text('Yes')
      
        #Screenshot
        await page.screenshot(path='screenshots/demoqa/elements/radio-button.png')
        #StopTracing
        await context.tracing.stop(path= 'logs/demoqa/elements/traceRadio-button.zip')
        await browser.close()
        
asyncio.run(main())