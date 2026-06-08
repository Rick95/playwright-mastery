from playwright.sync_api import expect

def test_dynamic(github_login_page):
    github_login_page.navigate()
    github_login_page.click_sign_in()
    expect(github_login_page.page.get_by_role("heading", name="Sign in")).to_be_visible()
    expect(github_login_page.login_button).to_be_visible()
    github_login_page.login("username", "password")
    