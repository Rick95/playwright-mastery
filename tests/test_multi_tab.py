from playwright.sync_api import Page, expect
import re


def test_multi_tab(page, context):
    page.goto("https://github.com", wait_until="domcontentloaded")
    new_tab = context.new_page()
    new_tab.goto("https://wikipedia.org")
    expect(new_tab).to_have_title(re.compile("Wikipedia"))
    new_tab.close()
    expect(page).to_have_url(re.compile("https://github.com"))