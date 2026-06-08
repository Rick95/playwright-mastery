from playwright.sync_api import expect, Page
import re

def test_assertions(page : Page):
    page.goto(("https://www.wikipedia.org"))
    locator = page.get_by_role("searchbox")
    locator.fill("Python")
    locator.press("Enter")
    expect(page).to_have_url(re.compile("Python"))
    expect(page).to_have_title(re.compile("Python"))
    heading1 = page.locator("h1#firstHeading")
    expect(heading1).to_contain_text(re.compile("Python"))