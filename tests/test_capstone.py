from playwright.sync_api import expect

def test_repo_search_journey(github_search_page, github_repo_page):
    github_search_page.navigate()
    term = "playwright"
    github_search_page.search(term)
    github_search_page.click_first_result(term)
    github_search_page.page.wait_for_load_state("domcontentloaded")
    expect(github_repo_page.get_repo_heading).to_be_visible()