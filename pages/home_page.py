from playwright.sync_api import expect
from pages.base_page import BasePage

class HomePage(BasePage):

    def __init__(self, page):

        super().__init__(page)
        self.signup_login_link = page.get_by_role(
            "link", name="Signup / Login"
        )

        self.login_section =  page.get_by_text(
            "Login to your account"
        )

    def open_signup_login_page(self):

        self.signup_login_link.click()

    def verify_login_section_visible(self):

        expect(
            self.login_section
        ).to_be_visible()

