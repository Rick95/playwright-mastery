from playwright.sync_api import Page

class WikipediaPage:
    def __init__(self, page : Page):
        self.page = page
        self.searchbox = page.get_by_role("searchbox")

    
    def navigate(self):
        self.page.goto("https://www.wikipedia.org")


    def search(self, term):
        self.searchbox.fill(term)
        self.searchbox.press("Enter")


    def get_heading(self) -> str:
        return self.page.locator("h1#firstHeading").inner_text()


    def heading(self):
        return self.page.locator("h1#firstHeading")