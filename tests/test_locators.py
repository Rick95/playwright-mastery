from playwright.sync_api import Page, expect

def test_locator(page : Page):
    page.goto("https://www.wikipedia.com")
    locator = page.get_by_role("searchbox")
    expect(locator).to_be_visible()