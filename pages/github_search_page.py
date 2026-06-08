from playwright.sync_api import Page

class GithubSearchPage:
    def __init__(self, page):
        self.page = page
    

    def navigate(self):
        self.page.goto("https://github.com/search")


    @property
    def search_box(self):
        return self.page.locator("input[data-component='input']")


    def search(self, term):
        s = self.search_box
        s.fill(term)
        s.press("Enter")

    @property
    def result_count_locator(self):
        return self.page.locator("span[class='SearchSubHeader-module__inlineDisplay__AFA2a']")


    @property
    def get_results_heading(self):
        self.page.wait_for_load_state("domcontentloaded")
        result_count_locator = self.result_count_locator
        result_count_locator.wait_for(state = "visible")
        return result_count_locator
