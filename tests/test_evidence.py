from playwright.sync_api import expect


def test_intentional_failure(page):
    page.goto("https://github.com")
    expect(page).to_have_title("This will fail")