import pytest
from playwright.sync_api import expect

@pytest.mark.parametrize("search_terms", [("Python"), ("pytest"), ("selenium")])   
def test_guthub_search(github_search_page, search_terms):
    github_search_page.navigate()
    github_search_page.search(search_terms)
    expect(github_search_page.get_results_heading).to_be_visible()