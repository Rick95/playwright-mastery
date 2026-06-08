from playwright.sync_api import sync_playwright

with sync_playwright() as p:
    browser = p.chromium.launch()
    context = browser.new_context()
    page = context.new_page()
    page.goto("https://wikipedia.org")
    page.get_by_role("link", name="English").click()
    page.wait_for_load_state("domcontentloaded")
    context.storage_state(path="test_data/wiki_state.json")
    browser.close()
    print("State saved.")