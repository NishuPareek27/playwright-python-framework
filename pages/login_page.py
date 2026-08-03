import allure
from pages.home_page import HomePage
from utils.logger import get_logger
from playwright.sync_api import expect
from pages.base_page import BasePage


logger = get_logger()
class LoginPage(HomePage):

    def __init__(self, page):

        super().__init__(page)
        self.email_input = page.locator(
            "[data-qa='login-email']"
        )

        self.password_input = page.get_by_placeholder(
            "Password"
        )

        self.login_button = page.get_by_role(
            "button", name="Login"
        )

        self.invalid_login_error = page.get_by_text(
            "Your email or password is incorrect!"
        )

        self.logout_link = page.get_by_role(
            "link", name="Logout"
        )


    
    def login(self, email, password):

        with allure.step("Enter email"):
            self.email_input.fill(email)
            logger.info(f"Entering email: {email}")

        with allure.step("Enter password"):
            self.password_input.fill(password)
            logger.info(f"Entering password: {password}")

        with allure.step("Click on the login button"):
            self.login_button.click()
            logger.info("Clicking on the Login button")

    def logout(self):
        with allure.step("Click on the Logout link"):
            self.logout_link.click()
            logger.info("Clicking on the logout link")

    @allure.step("Verify invalid login error message")
    def verify_invalid_login_error(self):

        expect(
            self.invalid_login_error
        ).to_be_visible()


    def verify_user_logout(self):

        expect(
            self.signup_login_link
        ).to_be_visible()