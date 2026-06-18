from playwright.sync_api import Page


class GitHubRepoPage:
    def __init__(self, page):
        self.page = page


    @property
    def get_repo_heading(self):
        return self.page.locator("strong[itemprop='name']")    