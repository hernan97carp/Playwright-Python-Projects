import pytest
import asyncio
from playwright.async_api import async_playwright, expect
from tests.testbase import CheckBoxesPage

@pytest.mark.asyncio
async def test_checkboxes():
    async with async_playwright() as p:
        # Lanzar el navegador
        browser = await p.chromium.launch(headless=False)
        context = await browser.new_context()
        
        # Iniciar el trazado
        await context.tracing.start(screenshots=True, snapshots=True, sources=True)
        
        page = await context.new_page()
        checkBoxPage = CheckBoxesPage(page)
        
        # Realizar las acciones en la página
        await checkBoxPage.viewPortSize()
        await checkBoxPage.navigate()
        await checkBoxPage.checkHome()

        # Assertions
        await expect(checkBoxPage.labelHome).to_be_checked()
        await expect(checkBoxPage.result).to_have_text(checkBoxPage.resultText)
        
        # Tomar una captura de pantalla
        await checkBoxPage.screenshot()
        
        # Detener el trazado
        await context.tracing.stop(path= checkBoxPage.tracePath)
        
        # Cerrar el navegador
        await browser.close()

if __name__ == "__main__":
    pytest.main(["-v", __file__])
