from playwright.sync_api import expect
import re

def test_fixtures(wikipedia_page):
    search_term = "Python"
    wikipedia_page.navigate()
    wikipedia_page.search(search_term)
    expect(wikipedia_page.page).to_have_title(re.compile(search_term))

def test_fixtures2(wikipedia_page):
    search_term = "Java"
    wikipedia_page.navigate()
    wikipedia_page.search(search_term)
    expect(wikipedia_page.page).to_have_title(re.compile(search_term))