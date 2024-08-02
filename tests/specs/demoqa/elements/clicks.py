import asyncio
from playwright.async_api import async_playwright, expect


async def main():
    async with async_playwright() as p:
        browser = await p.chromium.launch(headless= False)
        context = await browser.new_context()
        await context.tracing.start(screenshots=True,snapshots= True, sources= True)
        page = await context.new_page()
        
        await page.set_viewport_size({'width': 1800, 'height': 1200})
        
        await page.goto('https://demoqa.com/buttons')
        
   
        #Double Click
        button = page.locator("text=Click Me").nth(0)
        await button.dblclick()
       
        #Right Click
        await page.locator("text=Click Me").nth(1).click(button="right")
    
        #Simple Click
        button = page.locator('text=Click Me').nth(2)
        await button.click()
        
        #Asserts
        await expect(page.locator('#dynamicClickMessage')).to_have_text('You have done a dynamic click')
        await expect(page.locator('#doubleClickMessage')).to_have_text('You have done a double click')
        await expect(page.locator('#rightClickMessage')).to_have_text('You have done a right click')
        #Screenshot
        await page.screenshot(path='screenshots/dynamicClick.png')
        #StopTracing
        await context.tracing.stop(path= 'logs/traceClicks.zip')
        await browser.close()
        
asyncio.run(main())