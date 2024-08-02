from playwright.async_api import Page
import pytest
def test_title(page: Page):
    page.goto("")
    assert page.title() == "Swag Labs"

#--Skip test by browser
#@pytest.mark.skip_browser("firefox")
#--Run on a specific browser
#@pytest.mark.only_browser("chromium")
def test_inventory_page(page: Page):
    page.goto("/inventory.html")
    assert page.inner_text("h3") == "Epic sadface: You can only access '/inventory.html' when you are logged in."
    
    
    