from playwright.sync_api import Page, expect

search_word = "Playwright"

def test_actions(page : Page):
    page.goto("https://www.wikipedia.com")
    locator = page.get_by_role("searchbox")
    locator.fill(search_word)
    locator.press("Enter")
    assert search_word in page.title()


def test_actions_bonus(page : Page):
    page.goto("https://www.wikipedia.com")
    locator = page.get_by_role("searchbox")
    locator.fill(search_word)
    locator.press("Enter")
    assert expect(page.get_by_text(search_word).first).to_be_visible() is None
    # locator2 = page.get_by_text(search_word).first
    # assert expect(locator2).to_be_visible() is None