import pytest
from playwright.sync_api import expect
from pages.login_page import LoginPage
from pages.home_page import HomePage
from config.config import BASE_URL
from testdata.login_data import INVALID_LOGIN_DATA

# Test to navigate to the Login Page and verify the URL and visibility of the Login section
def test_navigate_to_login_page(page):
    page.goto(BASE_URL)
    home_page = HomePage(page)

    home_page.open_signup_login_page()

    expect(page).to_have_url(BASE_URL + "/login")

    home_page.verify_login_section_visible()



# Test to verify login functionality with invalid credentials using parameterized test data (DDT - Data Driven Testing)
@pytest.mark.parametrize(
        "email,password", 
        INVALID_LOGIN_DATA
)
def test_login_with_invalid_creds(
    page, 
    email, 
    password
):
    page.goto(BASE_URL)

    home_page = HomePage(page)
    home_page.open_signup_login_page()

    login_page = LoginPage(page)
    login_page.login(email, password)
    login_page.verify_invalid_login_error()