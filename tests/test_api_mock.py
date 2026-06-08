from playwright.sync_api import expect, Page
import re

def test_api_mock(github_search_page):
    requests_made = []
    github_search_page.page.on("request", lambda req: requests_made.append(req.url) 
                               if "search" in req.url else None)
    github_search_page.navigate()
    github_search_page.search("playwright")
    github_search_page.page.wait_for_load_state("domcontentloaded")
    
    print("\nRequests made:")
    for url in requests_made:
        print(url)
    
    expect(github_search_page.page).to_have_url(re.compile("search"))