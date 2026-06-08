from playwright.sync_api import Page

def test_wikipedia(page: Page):
    page.goto("https://www.wikipedia.com")
    assert page.title() == "Wikipedia"
    assert "wikipedia.org" in page.url 