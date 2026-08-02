import allure
from utils.logger import get_logger
from playwright.sync_api import expect
from pages.base_page import BasePage


logger = get_logger()
class LoginPage(BasePage):

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


    @allure.step("Verify invalid login error message")
    def verify_invalid_login_error(self):

        expect(
            self.invalid_login_error
        ).to_be_visible()