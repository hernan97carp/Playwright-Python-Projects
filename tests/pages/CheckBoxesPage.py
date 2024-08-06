from tests.testbase import *
from playwright.async_api import Page

class CheckBoxesPage:
    def __init__(self, page: Page):
        self.page = page
        self.labelHome = self.page.get_by_label("home")
        self.result  = self.page.locator("#result")
        self.resultText = "You have selected :homedesktopnotescommandsdocumentsworkspacereactangularveuofficepublicprivateclassifiedgeneraldownloadswordFileexcelFile"
        self.tracePath = "../../../../logs/demoqa/elements/traceCheckboxes.zip"
    async def viewPortSize(self):
        await self.page.set_viewport_size({"width": 1800, "height": 1200})

    async def navigate(self):
        await self.page.goto("https://demoqa.com/checkbox")

    async def checkHome(self):
        await self.page.check('label[for="tree-node-home"]')
    async def screenshot(self):
        await self.page.screenshot(path="../../../../screenshots/demoqa/elements/checkboxes.png")
           
