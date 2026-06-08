from playwright.sync_api import expect, Page
import re

def test_navigations(page : Page):
    criteria = "Python"
    url = "https://www.wikipedia.org"
    page.goto(url)
    
    locator = page.get_by_role("searchbox")
    locator.fill(criteria)
    locator.press("Enter")
    
    page.wait_for_url(re.compile(criteria))
    expect(page).to_have_title(re.compile(criteria))
    page.go_back()
    
    expect(page).to_have_url(re.compile(re.escape(url)))