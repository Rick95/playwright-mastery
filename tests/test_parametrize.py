import pytest
from playwright.sync_api import Page, expect

@pytest.mark.parametrize("search_term, expected_heading", [("Python", "Python"), ("Java", "Java"), 
    ("Playwright", "Playwright"), (pytest.param("Golang", "Golang", marks=pytest.mark.xfail))])
def test_parametrize(wikipedia_page, search_term, expected_heading):
    wikipedia_page.navigate()
    wikipedia_page.search(search_term)
    assert expected_heading in wikipedia_page.get_heading()