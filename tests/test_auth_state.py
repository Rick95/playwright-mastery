import re
from playwright.sync_api import expect

def test_auth_state(wiki_auth_page):
    wiki_auth_page.goto("https://en.wikipedia.org/wiki/Playwright")
    expect(wiki_auth_page).to_have_url(re.compile("https://en.wikipedia.org"))