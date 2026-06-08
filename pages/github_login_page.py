from playwright.sync_api import Page
import re

class GithubLoginPage:
    
    def __init__(self, page):
        self.page = page
        self.username = ""
        self.password = ""


    @property
    def sign_in_link(self):
        return self.page.get_by_role("link", name = "Sign in")


    @property
    def username_input(self):
        return self.page.locator("input#login_field")


    @property
    def password_input(self):
        return self.page.locator("input#password")


    @property
    def login_button(self):
        return self.page.locator("input[type='submit']")


    def login(self, username, password):
        self.username_input.fill(username)
        self.password_input.fill(password)
        self.login_button.click()

    def navigate(self):
        self.page.goto("https://github.com")


    def click_sign_in(self):
        self.page.wait_for_load_state("domcontentloaded")
        sign_in_link = self.sign_in_link
        sign_in_link.wait_for(state = "visible")
        sign_in_link.click()
        self.page.wait_for_url(re.compile("login"))