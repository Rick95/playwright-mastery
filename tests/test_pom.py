from pages.wikipedia_page import WikipediaPage
from playwright.sync_api import expect, Page
import re

def test_pom(page : Page):
    w = WikipediaPage(page)
    w.navigate()
    searchterm = "Playwright"
    w.search(searchterm)
    assert searchterm in w.get_heading()
    expect(page).to_have_title(re.compile(searchterm))