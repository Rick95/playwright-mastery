import pytest
from pages.wikipedia_page import WikipediaPage
from pages.github_login_page import GithubLoginPage
from pages.github_search_page import GithubSearchPage
from pages.github_repo_page import GitHubRepoPage   

@pytest.fixture(scope="function")
def wikipedia_page(page):
    return WikipediaPage(page)


@pytest.fixture(scope="function")
def github_login_page(page):
    return GithubLoginPage(page)


@pytest.fixture(scope="function")
def github_search_page(page):
    return GithubSearchPage(page)


@pytest.fixture(scope="session")
def wiki_auth_context(browser):
    context = browser.new_context(storage_state="test_data/wiki_state.json")
    yield context
    context.close()


@pytest.fixture(scope="session")
def wiki_auth_page(wiki_auth_context):
    page = wiki_auth_context.new_page()
    yield page
    page.close()


@pytest.fixture(scope="function")
def github_repo_page(page):
    return GitHubRepoPage(page)    

